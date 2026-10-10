# Material-Input Ledger — IBM Project 1 Edition B

**Valuation cut-off:** September 1, 2026, after the NYSE market close.  
**Units:** USD millions unless stated otherwise.  
**Availability key:** `Yes` means public no later than the cut-off; `No` means excluded; `Unresolved` means an as-of-valid source/value has not been established.  
**Important:** June 30, 2026 is the latest *reported* balance sheet. It is not treated as a September 1 balance sheet.

## Primary reported operating and balance-sheet inputs

| Input | Value | Unit / definition | Reporting period | Filing / publication date | Source URL and locator | Available Sep. 1? | Treatment |
|---|---:|---|---|---|---|---|---|
| Total revenue | 67,535 | USD m; GAAP revenue | FY ended Dec. 31, 2025 | Form 10-K filed Feb. 24, 2026 | [IBM 2025 10-K](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231.htm), incorporated Annual Report financial statements pp. 42–45 | Yes | Reported historical base; reconcile in final model. |
| Software revenue | 29,962 | USD m; segment revenue | FY ended Dec. 31, 2025 | Feb. 24, 2026 | [IBM 2025 10-K](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231.htm), Annual Report segment information pp. 65–68 | Yes | Reported historical segment base. |
| Consulting revenue | 21,055 | USD m; segment revenue | FY ended Dec. 31, 2025 | Feb. 24, 2026 | Same 10-K, segment information | Yes | Reported historical segment base. |
| Infrastructure revenue | 15,718 | USD m; segment revenue | FY ended Dec. 31, 2025 | Feb. 24, 2026 | Same 10-K, segment information | Yes | Reported historical segment base. |
| Financing revenue | 737 | USD m; segment revenue | FY ended Dec. 31, 2025 | Feb. 24, 2026 | Same 10-K, segment information | Yes | Reported historical segment base. |
| Cash and equivalents | 7,172 | USD m; balance-sheet asset | June 30, 2026 | Form 10-Q filed July 23, 2026 | [IBM Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm), Consolidated Balance Sheet, p. 5 | Yes | June 30 reported balance only. |
| Marketable securities | 960 | USD m; balance-sheet asset | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Need explicit cash-excess convention; do not automatically add all cash to EV bridge. |
| Restricted cash | 45 | USD m; balance-sheet asset | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Retained in the consolidated accounting model; not assumed excess cash. |
| Trade receivables | 6,044 | USD m; notes/accounts receivable, trade, net | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Operating working-capital base. |
| Financing receivables, net | 13,782 | USD m; current plus long-term | June 30, 2026 | July 23, 2026 | Same 10-Q, Note 10, pp. 22–23 | Yes | Separate financing convention required; not operating NWC by default. |
| Inventory | 1,746 | USD m; balance-sheet inventory | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Operating working-capital base. |
| PP&E, net | 5,736 | USD m; balance-sheet PP&E, net | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Capital base. |
| Goodwill | 74,599 | USD m; balance-sheet goodwill | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Includes Confluent acquisition effect; do not forecast as ordinary operating investment. |
| Net intangibles | 13,955 | USD m; balance-sheet intangible assets, net | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet, p. 5 | Yes | Includes Confluent-related acquired intangibles. |
| Total debt | 61,987 | USD m; short-term debt + long-term debt | June 30, 2026 | July 23, 2026 | Same 10-Q, Balance Sheet pp. 6; 5,775 + 56,212 | Yes | Reported debt; financing-debt split must be established before FCFF bridge. |
| Financing debt | 13,047 | USD m; Financing segment debt | June 30, 2026 | July 23, 2026 | Same 10-Q, Liquidity / Financing debt discussion p. 68 | Yes | Excluded from operating FCFF and the operating EV bridge; used to calculate Financing book-equity reference. |
| IBM Financing equity | 1,450 | USD m; **directly reported** Financing segment equity | June 30, 2026 | July 23, 2026 | [IBM Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm), Financing discussion p. 73 | Yes | June book-value sidecar reference added once; no $714m invented Financing asset. |
| Corporate debt | 48,940 | USD m; total reported debt less Financing debt | June 30, 2026 | July 23, 2026 | Same 10-Q, total debt and Financing debt disclosures; 61,987 − 13,047 | Yes | Only debt in operating WACC and EV bridge. |
| Retirement obligations | 8,603 | USD m | June 30, 2026 | July 23, 2026 | Same 10-Q, Consolidated Balance Sheet p. 6 | Yes | Consolidated accounting liability; future enterprise-to-equity treatment must be disclosed separately. |
| IBM stockholders’ equity | 34,452 | USD m | June 30, 2026 | July 23, 2026 | Same 10-Q, Balance Sheet p. 6 | Yes | Accounting check base. |
| Noncontrolling interests | 89 | USD m | June 30, 2026 | July 23, 2026 | Same 10-Q, Balance Sheet p. 6 | Yes | Enterprise-to-equity bridge item only if using consolidated FCFF. |
| H1 net cash from operations | 7,766 | USD m; GAAP cash flow | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, Cash Flows p. 7 | Yes | Historical cash-flow anchor, not full-year base. |
| H1 PP&E capex | 461 | USD m; payments for PP&E | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, Cash Flows p. 7 | Yes | Cash-investment anchor. |
| H1 investment in software | 313 | USD m; investing cash flow | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, Cash Flows p. 7 | Yes | Cash-investment anchor. |
| H1 depreciation | 1,088 | USD m | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, Cash Flows p. 7 | Yes | Reported add-back. |
| H1 intangible/software amortization | 1,535 | USD m | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, Cash Flows p. 7 | Yes | Reported add-back; distinguish acquired-intangible amortization in model. |
| H1 diluted weighted-average shares | 952.7 | million shares | Six months ended June 30, 2026 | July 23, 2026 | Same 10-Q, EPS statement p. 3 | Yes | Period-average; do not mislabel as Sep. 1 point-in-time shares. |
| Basic shares outstanding | 942.134390 | million point-in-time shares | June 30, 2026 / latest reported count | July 23, 2026 | Same 10-Q, cover-page / share disclosure | Yes | Market capitalization and WACC equity weight with Sep. 1 close; not the diluted per-share denominator. |
| June 30 issued shares | 1,354 | million shares; balance-sheet presentation | June 30, 2026 | July 23, 2026 | Same 10-Q, Balance Sheet p. 6 | Yes | **Not a valuation share count.** Do not use without reconciling treasury shares and dilutive instruments. |

## Latest operating evidence and company outlook available by cut-off

| Input | Value | Unit / definition | Reporting period | Filing / publication date | Source URL and locator | Available Sep. 1? | Treatment |
|---|---:|---|---|---|---|---|---|
| Q2 total revenue | 17,162 | USD m | Three months ended June 30, 2026 | July 23, 2026 10-Q; July 22 release | [IBM Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm), income statement p. 3 | Yes | Latest reported quarter. |
| Q2 segment revenue | Software 7,761; Consulting 5,327; Infrastructure 3,835; Financing 186 | USD m | Three months ended June 30, 2026 | July 23, 2026 | Same 10-Q, segment view p. 12 | Yes | Supports segment-driver calibration, not separate statutory segment financial statements. |
| Q2 segment revenue growth | Software 5.1%; Consulting 0.2%; Infrastructure -7.4%; Financing 12.2% | YoY reported | Three months ended June 30, 2026 | July 23, 2026 | Same 10-Q, segment view p. 12 | Yes | Evidence, not management guidance. |
| FY2026 constant-currency revenue outlook | 4%–5% | Management outlook | FY2026 | July 22, 2026 | [IBM Q2 2026 release](https://newsroom.ibm.com/2026-07-22-IBM-RELEASES-SECOND-QUARTER-RESULTS), Full-Year 2026 Expectations | Yes | Company outlook; a driver constraint, not an independent forecast. |
| FY2026 free-cash-flow outlook | about $1bn YoY increase | Management outlook | FY2026 | July 22, 2026 | Same release, Full-Year 2026 Expectations | Yes | Company outlook; model must disclose FCF definition and Financing treatment. |

## Market inputs — September 1 close

| Input | Value | Unit / definition | Market as-of date | Publication / access date | Source URL and locator | Available Sep. 1? | Status |
|---|---:|---|---|---|---|---|---|
| IBM closing price | 231.40 | USD per share; NYSE close | Sep. 1, 2026 | Historical table accessed after date | [IBM Historical Stock Lookup](https://ibm.gcs-web.com/stock-information/historic-stock-lookup), Sep. 1 row | Yes | Verified market input. Earlier Sep. 9 price ($239.94) is excluded. |
| Oracle closing price | 141.32 | USD per share; NYSE close | Sep. 1, 2026 | Historical table accessed after date | [Oracle price history](https://stockanalysis.com/stocks/orcl/history/), Sep. 1 row | Yes | Secondary source; use consistently if Oracle remains a qualified peer. |
| Accenture closing price | 188.09 | USD per share; NYSE close | Sep. 1, 2026 | Historical table accessed after date | [Accenture price history](https://stockanalysis.com/stocks/acn/history/), Sep. 1 row | Yes | Secondary source; use consistently if Accenture remains a qualified peer. |
| U.S. Treasury 10-year par yield | 4.79% | Nominal Treasury par yield | Sep. 1, 2026 | Treasury daily curve | [U.S. Treasury Daily Treasury Par Yield Curve](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?field_tdr_date_value_month=202609&type=daily_treasury_yield_curve), Sep. 1 / 10-year column | Yes | Candidate risk-free rate; term choice needs approval. |
| Implied U.S. ERP | 4.14% | Damodaran trailing-12-month adjusted-payout implied ERP | Sep. 1, 2026 | Source page says “on September 1, 2026” | [Damodaran Online](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm) | Yes | Method identified; must be labeled as an external market estimate. |
| IBM beta indication | 0.70 | Third-party technical-page beta; regression window/benchmark undisclosed | Page labeled Sep. 1, 2026 | Historical page accessed Oct. 9, 2026 | [Macroaxis IBM historical-page Sep. 1 snapshot](https://ns2.macroaxis.com/international-business-machines-stock-price-history), beta field | Provisional | Used for a screen, but independently reproducible cutoff beta remains **unresolved**. Do not reuse Sep. 9 values. |
| Single-A credit OAS | 0.68% | ICE BofA U.S. Single-A Corporate Index option-adjusted spread | Sep. 1, 2026 | FRED series accessed Oct. 9, 2026 | [FRED BAMLC0A3CA](https://fred.stlouisfed.org/data/BAMLC0A3CA), Sep. 1 observation | Yes | Treasury-plus-A-spread proxy; not an IBM bond yield. |
| Marginal pre-tax cost of debt proxy | 5.47% | 4.79% 10-year Treasury + 0.68% single-A OAS | Sep. 1, 2026 | Computed Oct. 9 from dated observations | Treasury and FRED rows above | Provisional | Used in WACC; maturity and issuer-specific spread verification pending. Do **not** reuse 5.75%. |

## One-time items, normalization, and acquisition control

| Item | Reported evidence | Proposed analysis treatment | Status / required evidence |
|---|---|---|---|
| FY2025 income-tax benefit / claimed tax-audit benefit | FY2025 reported provision was a $242m benefit in prior preserved work; prior peer narrative asserts a tax-audit benefit. | Reported FY2025 income is **not** assumed to be normalized. Any after-tax EBIT / EPS normalization will remain blank until the primary filing supplies an amount, location, and tax treatment. | **Unresolved.** Do not use the prior narrative alone as a normalization receipt. |
| Confluent acquisition | Completed Mar. 17, 2026. Q2 10-Q reports $11,537m cash consideration; $11,602m total consideration; cash paid, net of acquired cash, appears as $10,480m in H1 investing cash flow. | Treat the acquisition as a historical H1 2026 balance-sheet and cash-flow event. The forward operating forecast will include acquired revenue only through the starting segment/reported base; no separate future acquisition spend or revenue uplift without a supportable assumption. | Verified from Q2 10-Q Note 4 and cash-flow statement. Avoids double counting cash outflow and asset creation. |
| Confluent assets | Purchase-price allocation: $7,238m goodwill, $2,122m client relationships, $1,590m completed technology, $122m trademarks; acquired cash $1,165m and marketable securities $917m. | Base balance sheet includes reported post-acquisition assets. Forecast acquired-intangible amortization from documented schedules/assumptions only; no second addition of purchase consideration in FCFF. | Verified allocation at June 30 was provisional; model must say so. |
| IBM Financing receivables and debt | Net financing receivables were $13,782m and Financing debt $13,047m at June 30; Financing equity is directly reported $1,450m. | Approved separate sidecar; no revenue, profit, receivable, debt or related tax-payable movement appears in operating FCFF. Add June book equity once in bridge. | Implemented provisionally; sidecar fair-value premium/discount remains unsupported. |

## Excluded post-cut-off information

| Item | Why excluded |
|---|---|
| September 9 and September 24 IBM prices and September 9 peer prices from prior files | They occurred after the September 1 valuation-date close. |
| Any results, guidance, consensus, or market prices published after September 1, 2026 | Not public at the stated valuation cut-off. |
| Current beta statistics without a dated Sep. 1 archive | They cannot establish what was known at the cut-off. |
