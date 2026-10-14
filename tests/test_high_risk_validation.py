"""Independent high-risk checks: timing/bridge, FCF definitions, and guardrails."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "model"))
sys.path.insert(0, str(ROOT / "scripts"))

from ibm_phase3_model import build_model, load_inputs  # noqa: E402
from valuation import dcf_from_rows, run_analysis  # noqa: E402
from high_risk_diagnostics import fcf_bridge, independent_dcf  # noqa: E402


class HighRiskValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs = load_inputs(); cls.rows = build_model(cls.inputs)

    def test_independent_dcf_ties_out_without_production_dcf_call(self):
        diagnostic = independent_dcf(self.inputs, self.rows)
        production = dcf_from_rows(self.rows, self.inputs)
        self.assertAlmostEqual(diagnostic["wacc"], production["wacc"], places=12)
        self.assertAlmostEqual(diagnostic["operating_ev"], production["bridge"]["operating_ev"], places=6)
        self.assertAlmostEqual(diagnostic["common_equity"], production["bridge"]["common_equity"], places=6)
        self.assertAlmostEqual(diagnostic["value_per_share"], production["bridge"]["value_per_share"], places=9)
        self.assertEqual(diagnostic["residual_fraction"], 121 / 184)

    def test_period_correct_management_fcf_reconciliation(self):
        b = fcf_bridge(self.inputs, self.rows)
        self.assertEqual(b["h1_cfo"] - b["h1_financing_adjustment"] - b["h1_net_capital_investment"], 4759.0)
        self.assertAlmostEqual(b["h1_management_fcf"], 4759.0)
        self.assertAlmostEqual(b["h2_proxy"], 6158.232603241117, places=6)
        self.assertAlmostEqual(b["fy_model_proxy"], 10918.232603241117, places=6)
        self.assertAlmostEqual(b["unexplained_gap"], 4781.767396758883, places=6)

    def test_invalid_terminal_reinvestment_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "ROIC"):
            run_analysis(overrides={"terminal_growth": .03, "terminal_roic": .03})

    def test_invalid_operating_cash_bridge_reserve_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Operating cash reserve"):
            run_analysis(overrides={"minimum_cash": 10001})

    def test_material_consulting_shock_articulates_and_moves_value_down(self):
        base = run_analysis()
        shock = run_analysis(overrides={"consulting_growth_shift": -.03})
        self.assertEqual(shock["checks"]["statement_articulation"], "PASS")
        self.assertLess(shock["dcf"]["bridge"]["value_per_share"], base["dcf"]["bridge"]["value_per_share"])
        self.assertLess(shock["rows"]["2030"]["operating_fcff_ex_financing"], base["rows"]["2030"]["operating_fcff_ex_financing"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
