# Phase 3 Validation Log — period-error correction

Executed October 9, 2026 with `python3 -m unittest discover -s tests -v` from `ibm-project-1-b`. The 15 Phase 3 tests passed after correction; the combined Phase 3/4 suite has 22 passing tests. This is **not** a Locked Changed-Input Record or an AI-off test.

## Failure discovered

The earlier model began the balance sheet on June 30 but applied *full-year* FY2026 earnings, D&A, investment, dividends, and cash flow to that opening stock. It double-counted H1 while still balancing mathematically, because cash and equity were both generated from the same wrong period flow. That correction remains intact. A second boundary error was then found: the old corrected model treated September 1 as a future cash-flow day. It used H2 FCFF × **122/184 = $4,830.7m**. Because the valuation is after the September 1 market close, the future interval is September 2–December 31: **121/184 × $7,285.7m = $4,791.1m**. The $39.6m difference is retained as a superseded comparison. The historical full-year proxy ($9,173.9m × 122/184 = $6,082.7m) remains a superseded pre-repair result only.

The first test set checked balance-sheet and cash-flow *articulation*, but did not assert the stock/flow period boundary. It therefore could not detect an internally consistent double count. It also used a fabricated $714m `financing_other_assets` to imply sidecar equity. The Q2 10-Q directly reports **$1,450m** Financing equity. The $714m is now `unmapped_other_assets_reconciliation`, a consolidated mapping residual, not a separately reported Financing asset. A later strengthened test that changed Financing profit, revenue and receivables exposed another contamination: consolidated taxes payable and total-revenue-based deferred income affected operating FCFF. Taxes payable now remains in consolidated CFO but is excluded from ex-Financing operating working capital, since FCFF uses an explicit cash-tax rate. Deferred income is forecast on operating revenue only. The intermediate $3,908.5m residual was never retained as final output.

The revised H1 income bridge is exactly $33,079m revenue − $14,222m cost − $10,071m SG&A − $4,485m R&D + $338m IP income + $186m other income − $959m interest = **$3,866m pretax**. A separate unallocated-corporate deduction was removed.

## Corrected FY2026 checkpoint (USD millions)

| Item | H1 actual | H2 forecast | FY2026 full year / Dec. 31 |
|---|---:|---:|---:|
| Revenue | 33,079.0 | 37,826.2 | 70,905.2 |
| Net income | 3,381.0 | 4,004.6 | 7,385.6 |
| Depreciation | 1,088.0 | 1,089.8 | 2,177.8 |
| Amortization | 1,535.0 | 1,465.3 | 3,000.3 |
| PP&E capex | 461.0 | 560.9 | 1,021.9 |
| Capitalized software | 313.0 | 373.9 | 686.9 |
| Dividends | 3,166.0 | 3,166.0 | 6,332.0 |
| Cash | June 30: 7,172.0 | H2 CFO 6,154.6 and H2 investing/financing | Dec. 31: 9,225.7 |
| Equity | June 30: 34,541.0 | H2 NI − H2 dividends; other equity movements = 0 simplifying assumption | Dec. 31: 35,379.6 |

H2 cash is $7,172m beginning cash + $6,154.6m CFO − $560.9m PP&E capex − $373.9m software investment + H2 debt changes − $3,166m dividends. FY2026 full-year CFO includes reported H1 CFO for presentation only; it is never reapplied to June cash.

The depreciation rate is high when measured against *net* PP&E because IBM's equipment includes short-life IT equipment. H1 2026 depreciation $1,088m annualized is $2,176m; average net PP&E from FY2025 year-end $5,899m and June 2026 $5,736m is $5,817.5m, yielding **37.4%**. Thus 19% is an H2 half-year rate and 38% is the forward annual rate. This is a proxy on net PP&E, not an assertion of straight-line lives for individual gross assets. [IBM FY2025 10-K](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231_d2.htm); [IBM June 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm).

## Exact tests added or rewritten

`tests/test_phase3_model.py` asserts FY2026 H1+H2 statement construction, H2-only June-to-December cash/equity roll-forward, Financing exclusion, annual depreciation, articulation, and a reversible $1m failure. `tests/test_valuation.py` adds date/121-of-184 controls; September 1 cash roll-forward; dividend payable once; corporate-debt-only WACC; terminal reinvestment and ROIC/WACC boundaries; monotonicity; named cases; reverse DCF; and peer implied-value reconciliations. The deliberately broken $1m cash check failed loudly as designed in the recorded run.

Earlier initial mapping failure is preserved: the first Phase 3 opening balance attempt was short $9,271m because retirement obligations and restricted cash were omitted; those were corrected from the filing. The remaining $1m reported rounding item is static and neither cash nor equity. No synthetic known-answer training-case run, partner challenge, or human Locked Changed-Input Record is claimed.
