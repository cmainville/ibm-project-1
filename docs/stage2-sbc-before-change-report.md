# Stage 2 controlled SBC repair — before-change report

**Captured from commit:** `7c1936af5b86caff2aca8c6f5ffe5e82a84fa52a`
**Command:** `python3 -m unittest discover -s tests -v`
**Units:** USD millions except per-share values. This report preserves the state immediately before the approved stock-based-compensation (SBC) repair. It does not modify the Locked Changed-Input Records or evidence screenshots.

## Connected-model outputs before change

| Year | Revenue | Operating EBIT ex-Financing | Net income | Consolidated CFO | Operating FCFF | Cash | Equity |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 70,905.2 | 9,923.6 | 7,385.6 | 13,920.6 | 7,285.7* | 9,225.7 | 35,379.6 |
| 2027 | 73,720.3 | 11,294.1 | 8,558.8 | 12,240.1 | 11,596.2 | 12,515.1 | 37,488.4 |
| 2028 | 76,610.8 | 12,572.6 | 9,567.4 | 13,659.5 | 12,917.0 | 16,896.5 | 40,480.8 |
| 2029 | 79,450.9 | 13,669.7 | 10,428.7 | 13,837.1 | 13,094.1 | 21,262.5 | 44,209.5 |
| 2030 | 82,218.9 | 14,717.4 | 11,253.0 | 14,265.3 | 13,514.1 | 25,865.6 | 48,637.5 |

\* FY2026 operating FCFF is H2 only.

## Valuation before change

- Low/base/high: **$144.80 / $181.95 / $223.94** per share.
- WACC: **7.0708%**; terminal PV / operating EV: **78.0637%**.
- Operating EV: $220,096.1.
- Equity bridge: +$1,450.0 Financing equity; +$2,419.2 excess cash and securities; -$48,940.0 estimated September 1 corporate debt; -$1,592.2 declared dividend payable; -$89.0 NCI; $0 pension/other claims; = $173,344.1 common equity / 952.7 diluted-share proxy = **$181.95/share**.

## FY2026 company-defined FCF comparison before change

- IBM H1 reconciliation: $7,766 GAAP CFO - $2,264 Financing-receivable adjustment - $743 net capital investment = $4,759m, rounding to reported $4,760m.
- Model H2 company-style proxy: $6,154.6 forecast CFO - $0.0 Financing-receivable movement - $934.9 PP&E capex plus software investment = $5,219.7m.
- Model FY2026 company-style proxy: $4,760.0 H1 reported FCF + $5,219.7 H2 proxy = $9,979.7m.
- July 2026 management outlook reference: approximately $15,700m, based on FY2025 FCF of $14,734m plus about $1bn. Approximate gap: **$5,720.3m**.

## Tests before change — 24 passed

All named tests returned `ok`: Phase 3 `test_all_years_articulate`, `test_annual_depreciation_after_2026`, `test_bounds_fail`, `test_december_cash_uses_h2_only`, `test_december_equity_uses_h2_only`, `test_fy26_investment_h1_plus_h2`, `test_fy26_net_income_h1_plus_h2`, `test_fy26_revenue_h1_plus_h2`, `test_historical_base`, `test_no_unallocated_corporate_deduction`, `test_one_million_cash_break_fails`, `test_operating_fcff_excludes_financing`, `test_reported_financing_equity`, `test_residual_fcff_not_full_year_prorated`, and `test_residual_fcff_uses_h2`; valuation `test_cases_reverse_dcf_and_named_scenario_order`, `test_dates_and_correct_stub_convention`, `test_peer_and_implied_value_reconciliations`, `test_prevaluation_rollforward_changes_bridge_not_operating_fcff`, `test_sep1_bridge_rollforward_and_dividend_once`, `test_terminal_monotonicities`, `test_terminal_reinvestment_and_boundaries`, `test_wacc_and_growth_value_monotonicity`, and `test_wacc_uses_corporate_debt_and_marginal_tax`.
