# Phase 2 Decision Note — Proposed Finance Architecture

**Status: APPROVED WITH USER MODIFICATIONS ON OCTOBER 9, 2026.** This design governs the Phase 3 draft model. It is not a valuation, recommendation, or a selection of the investment action.

## Approved modifications

1. **Financing:** consolidated statements are retained for accounting. Operating FCFF excludes Financing revenue/profit, receivables, debt, and interest. Financing is a separate equity sidecar; its first reference is reported book value, with no unsupported premium/discount.
2. **FY2026:** statements use H1 actual results plus an H2 forecast. The valuation will use only estimated September 1–December 31 residual cash flow, with the July/August removal convention disclosed and tested.
3. **Confluent:** June 30 cash, goodwill, and acquired intangibles are historical. H2 includes ongoing owned operations but no duplicate acquisition payment, purchase-price adjustment, or arbitrary revenue uplift.
4. **Capital inputs:** use the September 1 10-year Treasury rate (4.79%), September 1 implied ERP (4.14%), June 30 basic shares (942.134390m) for market capitalization/WACC weights, and H1 diluted weighted-average shares (952.7m) only as a labeled provisional per-share proxy. Beta and WACC cost of debt require dated support.
5. **Cash:** propose a source-supported operating-cash floor and show a bounded sensitivity before the equity bridge is used.

## Recommended convention set

| Decision | Proposal | Why it is economically consistent |
|---|---|---|
| Forecast dates | FY2026E–FY2030E. FY2026E is a full fiscal year, built from FY2025 actuals and the June 30 actual / H2 implied bridge; FY2027–2030 are full-year forecasts. Discount the residual FY2026 cash flow from September 1 using a dated stub (rather than treating the full year as future cash flow). | The September 1 valuation date falls late in FY2026. A full FY2026 forecast is still needed for statements, but only post-cut-off cash flows may be valued. |
| Opening balance sheet | Use the filed June 30, 2026 balance sheet as the opening balance sheet, clearly labeled “reported at June 30, not Sep. 1.” Forecast the H2 movement to Dec. 31, then annual balances. | It is the latest balance sheet public by the cut-off and preserves articulation without inventing a September 1 balance sheet. |
| Operating drivers | Forecast revenue separately for Software, Consulting, Infrastructure, Financing, and Other/unallocated revenue. Forecast consolidated cost, SG&A, R&D, D&A, taxes, operating working capital, capex, and capitalized software with disclosed bridges to the segments. | IBM reports segment revenue/profit but not a statutory standalone three-statement model by segment. This uses segment-level demand drivers without pretending that segment assets or cash flows are disclosed. |
| Financing convention | Consolidated statements retain Financing for accounting presentation. Operating EBIT, NOPAT, and FCFF exclude Financing revenue, profit, receivables, debt, and interest. IBM Financing is valued separately as an equity sidecar. The June 30 directly reported $1.450bn Financing equity is used once in the valuation bridge. | This matches a non-financial operating FCFF valuation more closely and avoids mixing the financing book with the operating EV. |
| Cash convention | Retain a documented minimum operating-cash balance; add only defined excess cash and marketable securities to the enterprise-to-equity bridge. Acquired Confluent cash is already reflected in the June 30 balance sheet. | Avoids treating all cash as non-operating and avoids adding acquired cash twice. |
| Confluent convention | Treat the March 2026 acquisition as historical by September 1: the June 30 balance sheet includes goodwill/intangibles and H1 cash flow includes $10,480m acquisition cash net of acquired cash. Include Confluent in the reported historical base; do not separately add acquisition cash or a revenue uplift to forecast FCFF. | The same acquisition cannot be included both in the historical base and as future cash spending/incremental value. |
| Debt/interest | Forecast only corporate debt and corporate interest in the operating model. Maintain a separate Financing debt/receivable schedule whose movements net to zero in the operating FCFF convention, subject to a visible reconciliation. | Keeps FCFF pre-financing and prevents double counting Finance debt. |
| Tax rate | Normalize cash taxes using a selected forward marginal cash-tax assumption; do not extrapolate FY2024–25 negative effective tax rates. The documented FY2025 tax-benefit amount is currently unresolved. | Allows forecast NOPAT to reflect a recurring tax basis rather than a discrete benefit. |
| Shares | Use a disclosed June 30 diluted weighted-average count as the starting proxy, then state its limitation. Do not call it a September 1 point-in-time fully diluted count until an as-of reconciliation is available. | Avoids conflating period-average diluted EPS shares with shares outstanding at valuation date. |
| WACC | Capital Asset Pricing Model cost of equity: Sep. 1 10-year Treasury (4.79%) + approved dated beta × Sep. 1 implied ERP (4.14%). Cost of debt must use a supportable Sep. 1 method. Market capitalization uses Sep. 1 IBM close ($231.40) and reconciled shares. | Aligns the observable date with valuation date; does not retain later-dated market data. |
| Terminal value | Perpetuity-growth terminal at Dec. 31, 2030 based on FY2031 FCFF, with terminal growth strictly below WACC. Show terminal value as a share of EV and a  WACC × g sensitivity. | Standard FCFF convention; exposes dependence on the terminal assumption. |

## IBM-specific operating-driver proposal

| Revenue line | Base driver concept | Evidence available by Sep. 1 | Load-bearing judgment still needed |
|---|---|---|---|
| Software | Growth fades from Q2 reported 5.1% YoY / FY2025 historical software momentum toward a sustainable rate; include acquired business only in reported base. | Q2 2026 reported revenue $7.761bn; Q2 growth 5.1%. | FY2026 H2 conversion, recurring growth durability, and fade path. |
| Consulting | Modest recovery / maturity path tied to enterprise project demand and software implementation. | Q2 2026 reported revenue $5.327bn; Q2 growth 0.2%. | Growth path and margin leverage. |
| Infrastructure | Cyclical path with explicit recovery/decline scenario, not software-like terminal growth. | Q2 2026 reported revenue $3.835bn; Q2 growth -7.4%. | Demand recovery, product-cycle timing, and margin. |
| Financing | Separate receivable-book growth, yield/credit-cost, and matched-debt schedule. | Q2 2026 revenue $186m; net financing receivables $13.782bn. | Book runoff/growth and funding match. |
| Other / unallocated | Hold close to reported scale unless evidence supports a different path; bridge to consolidated revenue. | Q2 reported other revenue $52m; H1 $100m. | Materiality threshold / treatment. |

## Material alternatives and consequences

| Alternative | Consequence | Recommendation |
|---|---|---|
| Include Financing receivables in EV and subtract all debt | Could be valid only in a fully consolidated financial-services valuation with a matched net-interest forecast; mixing it with an operating FCFF forecast creates a large double-counting risk. | Do not use unless the entire financing book is modeled as a financial asset/liability business. |
| Value only FY2027–2031 and omit FY2026 residual cash flow | Simpler but discards four months of forecast cash flow after Sep. 1 and weakens as-of-date fidelity. | Use FY2026–2030 with a stub discount. |
| Forecast FY2026 from FY2025 guidance midpoint only | Treats the already-reported first half as if it were unknown and may conflict with the June 30 financial statements. | Use H1 actual plus H2 implied. |
| Add entire $10.48bn Confluent cash spend to FY2026 FCFF after using June 30 balance sheet | Double counts the historical cash use because the June 30 cash balance already reflects it. | Do not do this. |
| Use September 9 beta/price/risk-free inputs | Violates cut-off control. | Do not do this. |

## Approval requested

Please approve, modify, or reject these four load-bearing choices before I build the final connected FCFF model:

1. **IBM Financing treatment:** exclude Financing receivables and matched Financing debt from operating FCFF and from the EV-to-equity bridge, while separately reconciling them.
2. **FY2026 partial-year treatment:** forecast full FY2026 statements from H1 actual plus H2 implied, but value only residual post-Sep. 1 cash flow using a stub discount.
3. **Acquisition treatment:** include Confluent once through the June 30 reported base, with no second cash outflow or extra revenue uplift.
4. **WACC/share-count safeguard:** leave beta, cost of debt, and point-in-time diluted shares unresolved until their Sep. 1 evidence is documented; no silent carryover from the Sep. 9 work.

After approval, I will build the final operating statements and ask you to review the actual forecast-driver paths before treating any valuation range or committee action as provisional.
