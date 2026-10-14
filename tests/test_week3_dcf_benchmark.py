import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "model"))

from week3_dcf_benchmark import calculate_week3_dcf


class Week3DcfBenchmarkTests(unittest.TestCase):
    def test_published_twelve_outputs(self):
        result = calculate_week3_dcf()
        published = {
            "fcff": (108.0000, 114.4800, 120.2040, 125.0122, 128.7625),
            "pv_explicit_fcff": 448.4408,
            "terminal_value": 1894.6486,
            "pv_terminal_value": 1176.4277,
            "enterprise_value": 1624.8685,
            "equity_value": 1374.8685,
            "value_per_share": 27.4974,
        }
        for calculated, expected in zip(result.fcff, published["fcff"]):
            self.assertAlmostEqual(calculated, expected, delta=0.01)
        for field, expected in published.items():
            if field != "fcff":
                self.assertAlmostEqual(getattr(result, field), expected, delta=0.01)
        self.assertAlmostEqual(result.terminal_pv_to_ev, 0.7240, delta=0.00005)

    def test_wacc_sensitivity_decreases_value_and_baseline_restores(self):
        baseline = calculate_week3_dcf()
        higher_wacc = calculate_week3_dcf(wacc=0.11)
        restored = calculate_week3_dcf()

        self.assertAlmostEqual(higher_wacc.value_per_share, 23.41, delta=0.01)
        self.assertLess(higher_wacc.value_per_share, baseline.value_per_share)
        self.assertAlmostEqual(restored.value_per_share, 27.4974, delta=0.01)


if __name__ == "__main__":
    unittest.main()
