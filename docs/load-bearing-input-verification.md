# Load-bearing input verification

**Scope:** September 1, 2026 after-close IBM valuation. USD millions unless
noted. This is a reproducible lineage and challenge log, not a revision of
approved assumptions. “Available” means the underlying public information was
available by the valuation cutoff, even if this audit accessed it later.

| Input | Model value / definition | Period, publication, primary locator | Transformation and status | Limitation / reproduction |
|---|---|---|---|---|
| IBM reference price | $231.40/share close | Sep. 1; [IBM historic lookup](https://ibm.gcs-web.com/stock-information/historic-stock-lookup) | Price × June 30 basic shares determines WACC market equity; PASS | Historical table access, not a licensed trade tape. |
| Basic / diluted shares | 942.134390 / 952.7m | Jun. 30 balance-sheet/cover count; H1 EPS, Q2 10-Q filed Jul. 23 | Basic for market cap; diluted weighted-average proxy for per-share value | Point-in-time diluted count and future dilution remain QUALIFIED. |
| Corporate / Financing debt | 48,940 / 13,047 | Jun. 30 Q2 10-Q debt and Financing disclosures | $61,987 total − $13,047 Financing = corporate debt; corporate debt only in WACC/operating bridge | Financing sidecar uses $1,450 reported book equity; fair-value premium/discount unknown. |
| Risk-free rate | 4.79% 10-year par yield | Sep. 1; [U.S. Treasury daily curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202609&type=daily_treasury_yield_curve) | Direct nominal 10-year observation; independently rechecked in this audit | Par yield, not a spot/zero rate; maturity choice is an analyst convention. |
| Equity risk premium | 4.14% | Sep. 1; Damodaran implied ERP page, recorded in ledger | CAPM input | External model estimate, not an IBM-specific fact. |
| Beta | 0.70 | Sep. 1 historical Macroaxis page, recorded in ledger | CAPM input | Regression benchmark/window unavailable. No cutoff-valid total-return series was retrieved for an independent regression; **QUALIFIED**. |
| Pre-tax borrowing-cost proxy | 5.47% = 4.79% + 0.68% | Sep. 1 Treasury and [FRED BAMLC0A3CA](https://fred.stlouisfed.org/series/BAMLC0A3CA) | Treasury-plus-single-A OAS proxy | OAS is not IBM bond yield, coupon, interest expense, or weighted average cost; issuer-specific dated yield remains unresolved. |
| WACC tax shield | 21.0% marginal tax rate | Approved valuation convention, inputs file | Applied only to debt leg of WACC | Distinct from operating normalized tax rate. |
| Operating tax rate | Forecast path ending at 16.0% | Analyst assumption in `inputs.json` | Applied to operating NOPAT/FCFF | Not a cash-tax forecast; cash-tax timing remains a key uncertainty. |
| Sep. 1 cash / dividend bridge | Cash $9,280.5; payable $1,592.2 | Jun. 30 Q2 10-Q plus approved 63/184 H2 roll-forward; dividend #446 $1.69 | Cash is estimated mechanically; payable deducted once | No July–Sep actual cash ledger; bridge is model-estimated. |
| Financing sidecar | $1,450 book equity | Q2 10-Q Financing discussion | Added once after operating EV | Book value, not independently estimated fair value. |
| Pension / retirement | $8,603 reported obligations | Jun. 30 Q2 10-Q balance sheet | No incremental bridge claim after operating retirement expense convention | Potential debt-like claim is QUALIFIED, not zero economic risk. |
| SBC / dilution | H2 $938.5; FY27–30 $1,877 | H1 2026 SBC $1,004 and H2 2025 $873; approved schedule | Noncash CFO add-back and APIC/equity credit once; no FCFF add-back | Future incremental dilution / share issuance not forecast. |
| Terminal growth / ROIC | 2.5% / 15.0% | Approved analyst assumptions | Terminal FCFF = NOPAT × (1 − g/ROIC) | Terminal PV is 78.06% of EV; assumptions are decision-critical. |
| Software / Consulting margins and growth | Paths in `inputs.json` | Q2 segment evidence + analyst assumptions | Bounded driver paths feed statements | Forecasts, not management segment guidance; range-dependence documented in investment review. |

## Independent challenges and diagnostic sensitivities

No source/model contradiction was found that warrants changing the frozen model.
The following are diagnostics, not new forecasts:

| Challenge | WACC / value per share | Interpretation |
|---|---:|---|
| Beta 0.50 / 0.70 / 0.90, all else frozen | 6.3946% / **7.0708%** / 7.74698%; $220.17 / **$182.29** / $154.15 | Beta specification materially matters; 0.70 stays qualified pending a reproducible dated regression. |
| Debt-cost proxy −100bp / base / +100bp | 6.9260% / **7.0708%** / 7.2156%; $189.43 / **$182.29** / $175.58 | Proxy sensitivity is smaller than beta sensitivity, but no issuer-specific dated yield was found. |
| Diluted shares +1% | $180.48/share | Mechanical denominator sensitivity; not a dilution forecast. |
| Financing sidecar −$500m | $181.76/share | $500m / 952.7m-share direct bridge effect. |
| Incremental pension/debt-like claim +$1bn | $181.24/share | Off-model bridge diagnostic only; not an asserted pension valuation. |

The $1bn bridge examples are intentionally linear, isolated diagnostics. They
must not be combined as a probability-weighted price target.

## Reproducibility, restrictions, and exclusions

The detailed primary-source URLs and locators are maintained in
[`evidence-ledger.md`](../evidence-ledger.md). SEC, IBM investor-relations,
Treasury, FRED, and Damodaran content remain subject to their respective terms;
this repository records small factual inputs and links, not redistributed market
datasets. No personal data is required. Post-cutoff company results, revised
consensus, current beta quotes, and later prices are excluded from the September
1 case.
