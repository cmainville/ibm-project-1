"""Tests of the H1/H2 boundary and connected statement articulation."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "model"))
import ibm_phase3_model as m  # noqa: E402


class Phase3Tests(unittest.TestCase):
    def setUp(self):
        self.inputs = m.load_inputs()
        self.rows = m.build_model(self.inputs)
        self.y26 = self.rows[2026]
        self.h1 = self.y26["h1_2026_actual"]
        self.h2 = self.y26["h2_2026_forecast"]
        self.open = m.opening_row(self.inputs)

    def test_historical_base(self):
        checks = m.reconcile_historical_base(self.inputs)
        self.assertEqual(checks["opening_balance_gap"], 0)
        self.assertEqual(checks["h1_segment_to_consolidated_revenue_gap"], 0)
        self.assertEqual(checks["h1_pretax_bridge_gap"], 0)
        self.assertLessEqual(abs(checks["h1_management_fcf_gap"]), 1)

    def test_fy26_revenue_h1_plus_h2(self):
        for key in (*m.SEGMENTS, "operating_revenue", "total_revenue"):
            self.assertAlmostEqual(self.y26[key], self.h1[key] + self.h2[key])

    def test_fy26_net_income_h1_plus_h2(self):
        self.assertAlmostEqual(self.y26["net_income"], self.h1["net_income"] + self.h2["net_income"])

    def test_december_cash_uses_h2_only(self):
        expected = (self.open["cash"] + self.h2["cfo_consolidated"] - self.h2["capex"] - self.h2["software_investment"]
                    + self.h2["delta_corporate_debt"] + self.h2["delta_financing_debt"] - self.h2["common_dividends"])
        self.assertAlmostEqual(self.y26["cash"], expected)
        self.assertNotAlmostEqual(self.y26["cash"], expected + self.h1["cfo_consolidated"])

    def test_december_equity_uses_h2_only(self):
        expected = self.open["equity"] + self.h2["net_income"] - self.h2["common_dividends"] + self.h2["other_equity_movements"]
        self.assertAlmostEqual(self.y26["equity"], expected)
        self.assertNotAlmostEqual(self.y26["equity"], expected + self.h1["net_income"])

    def test_residual_fcff_uses_h2(self):
        self.assertAlmostEqual(self.y26["residual_fcff_after_sep1_proportional"], self.h2["operating_fcff_ex_financing"] * 121 / 184)

    def test_residual_fcff_not_full_year_prorated(self):
        h1_proxy = self.h1["operating_ebit_ex_financing"] * .84 + self.h1["depreciation"] + self.h1["amortization"]
        self.assertNotAlmostEqual(self.y26["residual_fcff_after_sep1_proportional"], (h1_proxy + self.h2["operating_fcff_ex_financing"]) * 121 / 184)

    def test_no_unallocated_corporate_deduction(self):
        self.assertNotIn("unallocated_corporate_pct", self.inputs["draft_assumptions"]["operating_drivers"])
        self.assertAlmostEqual(self.h2["pretax_income"], self.h2["operating_ebit_ex_financing"] + self.h2["financing_pretax_contribution"] - self.h2["corporate_interest"])
        self.assertAlmostEqual(self.h1["pretax_income"], 3866)

    def test_annual_depreciation_after_2026(self):
        self.assertAlmostEqual(self.rows[2027]["depreciation"], self.y26["ppe"] * .38)
        self.assertNotAlmostEqual(self.rows[2027]["depreciation"], self.y26["ppe"] * .19)
        self.assertAlmostEqual(self.y26["depreciation"], 1088 + self.open["ppe"] * .19)

    def test_fy26_investment_h1_plus_h2(self):
        self.assertAlmostEqual(self.y26["capex"], 461 + self.h2["operating_revenue"] * .015)
        self.assertAlmostEqual(self.y26["software_investment"], 313 + self.h2["operating_revenue"] * .01)

    def test_sbc_historical_anchor_and_h2_schedule(self):
        schedule=self.inputs["draft_assumptions"]["stock_based_compensation"]
        self.assertEqual(self.h1["stock_based_compensation"],1004)
        self.assertAlmostEqual(self.h2["stock_based_compensation"],938.5)
        self.assertNotEqual(self.h2["stock_based_compensation"],self.h1["stock_based_compensation"])
        self.assertGreaterEqual(self.h2["stock_based_compensation"],schedule["h2_2026_sensitivity_range"][0])
        self.assertLessEqual(self.h2["stock_based_compensation"],schedule["h2_2026_sensitivity_range"][1])

    def test_sbc_is_noncash_cfo_addback_with_matching_apic(self):
        expected=(self.h2["net_income"]+self.h2["depreciation"]+self.h2["amortization"]+
                  self.h2["stock_based_compensation"]-self.h2["delta_operating_assets"]+
                  self.h2["delta_operating_liabilities"]+self.h2["delta_consolidated_taxes_payable"]-
                  self.h2["delta_financing_receivables"])
        self.assertAlmostEqual(self.h2["cfo_consolidated"],expected)
        self.assertAlmostEqual(self.h2["stock_based_compensation_apic"],self.h2["stock_based_compensation"])
        expected_equity=(self.open["equity"]+self.h2["net_income"]-self.h2["common_dividends"]+
                         self.h2["stock_based_compensation_apic"])
        self.assertAlmostEqual(self.y26["equity"],expected_equity)

    def test_sbc_does_not_change_operating_fcff(self):
        altered=deepcopy(self.inputs)
        altered["draft_assumptions"]["stock_based_compensation"]["forecast_expense_and_noncash_cfo_addback"][0]=1004
        changed=m.build_model(altered)
        self.assertNotEqual(changed[2026]["h2_2026_forecast"]["cfo_consolidated"],self.h2["cfo_consolidated"])
        self.assertAlmostEqual(changed[2026]["operating_fcff_ex_financing"],self.y26["operating_fcff_ex_financing"])

    def test_operating_fcff_excludes_financing(self):
        for year, row in self.rows.items():
            p = self.h2 if year == 2026 else row
            expected = (p["operating_ebit_ex_financing"] * .84 + p["depreciation"] + p["amortization"] - p["capex"]
                        - p["software_investment"] - p["delta_operating_assets"] + p["delta_operating_liabilities"])
            self.assertAlmostEqual(row["operating_fcff_ex_financing"], expected)
        self.assertNotIn("financing_receivables", m.OPERATING_ASSETS)
        self.assertNotIn("financing_debt", m.OPERATING_LIABILITIES)
        altered = deepcopy(self.inputs)
        altered["draft_assumptions"]["operating_drivers"]["financing_pretax_margin"][1] = .40
        altered["draft_assumptions"]["balance_sheet_and_financing"]["financing_receivables_growth"][1] = .08
        altered["draft_assumptions"]["segment_growth_after_2026"]["financing"][0] = .04
        changed = m.build_model(altered)
        self.assertAlmostEqual(changed[2027]["operating_fcff_ex_financing"],self.rows[2027]["operating_fcff_ex_financing"])

    def test_reported_financing_equity(self):
        self.assertEqual(m.model_payload(self.rows, self.inputs)["financing_sidecar"]["june_30_reported_equity"], 1450)
        self.assertEqual(self.open["unmapped_other_assets_reconciliation"], 714)
        self.assertNotIn("financing_other_assets", self.open)

    def test_all_years_articulate(self):
        m.assert_checks(self.rows, self.inputs)
        for year, row in self.rows.items():
            self.assertAlmostEqual(m.total_assets(row), m.total_liabilities_and_equity(row), msg=str(year))
            self.assertAlmostEqual(row["cash"], row["cash_from_cash_flow"], msg=str(year))

    def test_bounds_fail(self):
        broken = deepcopy(self.inputs)
        broken["draft_assumptions"]["segment_growth_after_2026"]["software"][0] = .50
        with self.assertRaisesRegex(ValueError, "outside documented bound"):
            m.build_model(broken)

    def test_one_million_cash_break_fails(self):
        self.assertIn("detected as intended", m.demonstrate_failed_check(self.inputs))


if __name__ == "__main__":
    unittest.main(verbosity=2)
