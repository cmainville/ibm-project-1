"""September 1 bridge, terminal economics, DCF, and peer consistency tests."""
from copy import deepcopy
from datetime import date
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "model"))
from valuation import (BRIDGE_DATE, VALUE_DATE, dcf_from_rows, implied_peer_values,
                       peer_screen, run_analysis, sep1_bridge, terminal_diagnostics, wacc_build)  # noqa: E402
from ibm_phase3_model import build_model, load_inputs  # noqa: E402


class ValuationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs=load_inputs(); cls.rows=build_model(cls.inputs)
        cls.rate=wacc_build(cls.inputs, cls.rows)["wacc"]

    def test_dates_and_correct_stub_convention(self):
        self.assertEqual(VALUE_DATE, date(2026,9,1)); self.assertEqual(BRIDGE_DATE, VALUE_DATE)
        b=sep1_bridge(self.rows,self.inputs)
        self.assertEqual((b["h2_days"],b["prevaluation_days"],b["residual_days"]),(184,63,121))
        self.assertAlmostEqual(self.rows[2026]["residual_fcff_after_sep1_proportional"],self.rows[2026]["h2_2026_forecast"]["operating_fcff_ex_financing"]*121/184)
        self.assertNotAlmostEqual(self.rows[2026]["residual_fcff_after_sep1_proportional"],self.rows[2026]["h2_2026_forecast"]["operating_fcff_ex_financing"]*122/184)

    def test_sep1_bridge_rollforward_and_dividend_once(self):
        b=sep1_bridge(self.rows,self.inputs); h2=self.rows[2026]["h2_2026_forecast"]
        expected=(7172+h2["cfo_consolidated"]*63/184-h2["capex"]*63/184-h2["software_investment"]*63/184+
                  h2["delta_corporate_debt"]*63/184+h2["delta_financing_debt"]*63/184)
        self.assertAlmostEqual(b["estimated_sep1_cash"],expected)
        self.assertNotEqual(b["estimated_sep1_cash"],7172)
        self.assertAlmostEqual(b["declared_dividend_payable"],1.69*942.134390)
        d=dcf_from_rows(self.rows,self.inputs)
        bridge=d["bridge"]
        self.assertAlmostEqual(bridge["common_equity"],bridge["operating_ev"]+bridge["financing_equity"]+bridge["excess_cash_and_securities"]-bridge["estimated_sep1_corporate_debt"]-bridge["declared_dividend_payable"]-bridge["pension_debt_like_claim"]-bridge["nci"]-bridge["other_claims"])
        self.assertEqual(sum(1 for k in bridge if k == "declared_dividend_payable"),1)

    def test_prevaluation_rollforward_changes_bridge_not_operating_fcff(self):
        altered=deepcopy(self.inputs); altered["draft_assumptions"]["balance_sheet_and_financing"]["corporate_debt"][0]=48000
        rows=build_model(altered)
        self.assertEqual(rows[2026]["h2_2026_forecast"]["operating_fcff_ex_financing"],self.rows[2026]["h2_2026_forecast"]["operating_fcff_ex_financing"])
        self.assertNotEqual(sep1_bridge(rows,altered)["estimated_sep1_corporate_debt"],sep1_bridge(self.rows,self.inputs)["estimated_sep1_corporate_debt"])

    def test_sbc_changes_cash_bridge_not_operating_ev_or_stub(self):
        altered=deepcopy(self.inputs)
        altered["draft_assumptions"]["stock_based_compensation"]["forecast_expense_and_noncash_cfo_addback"][0]=1004
        rows=build_model(altered)
        base=dcf_from_rows(self.rows,self.inputs)
        changed=dcf_from_rows(rows,altered)
        self.assertAlmostEqual(changed["bridge"]["operating_ev"],base["bridge"]["operating_ev"])
        self.assertAlmostEqual(rows[2026]["residual_fcff_after_sep1_proportional"],self.rows[2026]["residual_fcff_after_sep1_proportional"])
        self.assertGreater(sep1_bridge(rows,altered)["estimated_sep1_cash"],sep1_bridge(self.rows,self.inputs)["estimated_sep1_cash"])

    def test_wacc_uses_corporate_debt_and_marginal_tax(self):
        w=wacc_build(self.inputs,self.rows)
        self.assertNotEqual(w["corporate_debt"],48940+13047)
        self.assertAlmostEqual(w["market_equity"],231.40*942.134390)
        self.assertAlmostEqual(w["pretax_cost_debt"],.0479+.0068)
        self.assertEqual(w["marginal_tax_rate_for_wacc"],.21)
        self.assertNotEqual(w["marginal_tax_rate_for_wacc"],self.inputs["draft_assumptions"]["operating_drivers"]["normalized_nopat_tax_rate"][0])

    def test_terminal_reinvestment_and_boundaries(self):
        td=terminal_diagnostics(self.rows,self.inputs,self.rate,.025,.15)
        self.assertGreater(td["terminal_reinvestment"],0); self.assertLess(td["terminal_fcff"],td["terminal_2031_nopat"])
        with self.assertRaisesRegex(ValueError,"ROIC"):
            terminal_diagnostics(self.rows,self.inputs,self.rate,.025,.025)
        with self.assertRaisesRegex(ValueError,"below WACC"):
            terminal_diagnostics(self.rows,self.inputs,self.rate,self.rate,.15)
        self.assertNotEqual(td["terminal_fcff"],td["superseded_naive_terminal_fcff"])

    def test_terminal_monotonicities(self):
        tv_lo=dcf_from_rows(self.rows,self.inputs,self.rate,.02,terminal_roic=.15)["terminal_value"]
        tv_hi=dcf_from_rows(self.rows,self.inputs,self.rate,.03,terminal_roic=.15)["terminal_value"]
        self.assertGreater(tv_hi,tv_lo)
        self.assertGreater(dcf_from_rows(self.rows,self.inputs,self.rate-.005,.025)["terminal_value"],dcf_from_rows(self.rows,self.inputs,self.rate+.005,.025)["terminal_value"])
        self.assertGreater(dcf_from_rows(self.rows,self.inputs,self.rate,.025,terminal_roic=.18)["terminal_value"],dcf_from_rows(self.rows,self.inputs,self.rate,.025,terminal_roic=.12)["terminal_value"])

    def test_wacc_and_growth_value_monotonicity(self):
        a=dcf_from_rows(self.rows,self.inputs,self.rate-.005,.025)["bridge"]["value_per_share"]
        b=dcf_from_rows(self.rows,self.inputs,self.rate,.025)["bridge"]["value_per_share"]
        c=dcf_from_rows(self.rows,self.inputs,self.rate+.005,.025)["bridge"]["value_per_share"]
        self.assertGreater(a,b); self.assertGreater(b,c)
        self.assertGreater(dcf_from_rows(self.rows,self.inputs,self.rate,.03)["bridge"]["value_per_share"],dcf_from_rows(self.rows,self.inputs,self.rate,.02)["bridge"]["value_per_share"])

    def test_cases_reverse_dcf_and_named_scenario_order(self):
        cases={c:run_analysis(case=c) for c in ("low","base","high")}
        self.assertLess(cases["low"]["dcf"]["bridge"]["value_per_share"],cases["base"]["dcf"]["bridge"]["value_per_share"])
        self.assertLess(cases["base"]["dcf"]["bridge"]["value_per_share"],cases["high"]["dcf"]["bridge"]["value_per_share"])
        implied=cases["base"]["reverse_dcf"]["implied_growth"]
        self.assertLess(implied,self.rate); self.assertLess(implied,.15)
        self.assertAlmostEqual(dcf_from_rows(self.rows,self.inputs,self.rate,implied,terminal_roic=.15)["bridge"]["value_per_share"],231.40,places=6)

    def test_peer_and_implied_value_reconciliations(self):
        peers=peer_screen(); self.assertEqual({p["name"] for p in peers},{"Oracle","Accenture"})
        for p in peers:
            self.assertEqual(p["price_date"],"2026-09-01")
            self.assertAlmostEqual(p["enterprise_value"],p["market_cap"]+p["debt"]+p["other_claims"]-p["cash"]-p["securities"])
            self.assertAlmostEqual(p["ev_ebit"],p["enterprise_value"]/p["ebit"]); self.assertAlmostEqual(p["pe"],p["market_cap"]/p["net_income_common"])
        d=dcf_from_rows(self.rows,self.inputs); implied=implied_peer_values(self.rows,self.inputs,d)
        self.assertEqual(len(implied),2)
        for p in implied:
            b=d["bridge"]
            self.assertAlmostEqual(p["implied_common_equity_from_ev_ebit"],p["implied_operating_ev"]+b["financing_equity"]+b["excess_cash_and_securities"]-b["estimated_sep1_corporate_debt"]-b["declared_dividend_payable"]-b["pension_debt_like_claim"]-b["nci"]-b["other_claims"])


if __name__=="__main__": unittest.main(verbosity=2)
