# Stage 2 investment-judgment review — historical analyst-review draft; Watch / Defer subsequently approved by the student

**Scope and cutoff.** This was an objective analyst-review draft, not a replacement investment decision. It uses the September 1, 2026 after-close cutoff and current Python output only. The student subsequently approved and retained the Watch / Defer recommendation. The October 14, 2026 approved SBC accounting repair changes consolidated CFO, cash, equity, and the bridge; it does not change the operating forecast, operating FCFF methodology, WACC, or recommendation.

**Deck-export status.** `docs/Decision-Deck.html` is synchronized to the current output and contains eight main slides. PDF-export status is stated separately in the current repository validation record; the HTML is the controlling presentation artifact unless and until a matching PDF is verified.

## 1. Current financial conclusions

All figures are USD millions except per-share amounts. The current engine reports the following connected statement outputs. FY2026 revenue and net income combine H1 actual with H2 forecast; its displayed operating FCFF is H2 only.

| Fiscal year | Revenue | Operating EBIT ex-Financing | Net income | Operating FCFF | Cash | Corporate debt | Balance-sheet check |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 70,905.2 | 9,923.6 | 7,385.6 | 7,285.7 | 10,164.2 | 48,940.0 | 0.0 |
| 2027 | 73,720.3 | 11,294.1 | 8,558.8 | 11,596.2 | 15,330.6 | 48,000.0 | 0.0 |
| 2028 | 76,610.8 | 12,572.6 | 9,567.4 | 12,917.0 | 21,589.0 | 47,000.0 | 0.0 |
| 2029 | 79,450.9 | 13,669.7 | 10,428.7 | 13,094.1 | 27,832.0 | 46,000.0 | 0.0 |
| 2030 | 82,218.9 | 14,717.4 | 11,253.0 | 13,514.1 | 34,312.1 | 45,000.0 | 0.0 |

The September 1 operating EV is $220,096.1. The full bridge adds $1,450.0 of June 30 Financing equity and $2,740.5 of excess cash/securities, then deducts $48,940.0 of estimated September 1 corporate debt, $1,592.2 of declared-but-unpaid dividend, and $89.0 of NCI. This yields $173,665.4 of common equity, or **$182.29 per 952.7m diluted-share proxy**.

Current named cases are low **$145.13**, base **$182.29**, and high **$224.28** per share, compared with the September 1 close of **$231.40**. Base WACC is 7.0708%, terminal growth is 2.5%, terminal incremental ROIC is 15%, and terminal PV is 78.06% of operating EV. The reverse DCF solves 3.815% terminal growth at the $231.40 price while holding the 15% ROIC constant.

## 2. Assumption-by-assumption challenge

- **Software growth:** the 6.0% to 4.5% FY2027-30 path fades from reported H1 growth. It is exposed to renewal, Red Hat/Data, Confluent conversion, and ARR evidence. The official +2pp test adds $561.8m of FY2030 EBIT, $638.7m of FCFF, and $8.36/share.
- **Gross margin:** the 57.2% to 59.0% path assumes product mix and productivity. A +1pp test is the largest displayed OAT shock: +$813.1m FY2030 EBIT, +$680.1m FCFF, and +$12.20/share.
- **SG&A:** the 30.8% to 29.0% decline assumes productivity leverage despite potential selling and AI-investment needs. A -0.5pp test adds $406.6m FY2030 EBIT, $341.5m FCFF, and $6.14/share.
- **Normalized NOPAT tax:** the 16% rate is an analyst normalization, not reported cash tax. A -2pp test adds no EBIT, adds $294.3m FCFF, and adds $5.23/share. Primary-source support for a sustainable cash-tax rate remains unresolved.
- **Capital investment and working capital:** PP&E capex and capitalized software are projected from operating revenue; receivable, inventory, AP, deferred-income, and other operating ratios drive cash conversion. These are the key source of the FY2026 management-FCF reconciliation issue below.
- **WACC and terminal inputs:** beta is a qualified third-party indication, and cost of debt is Treasury plus a single-A OAS proxy rather than IBM-specific debt pricing. A 2.5% growth rate, 15% incremental ROIC, and 78.06% terminal-value share make the valuation particularly sensitive to steady-state assumptions.

## 3. FY2026 company-defined FCF reconciliation — material unresolved qualification

IBM's published company-defined FCF adjusts consolidated cash from operations for changes in Financing receivables and net capital investment. The historical model check replicates H1 2026 as **$7,766m CFO - $2,264m Financing-receivable change - $743m net capital investment = $4,759m**, which rounds to IBM's reported **$4.760bn**.

IBM reported approximately $14.7bn of company-defined FCF for FY2025 and stated on July 22, 2026 that FY2026 FCF was expected to increase by about $1bn. That indicates a management-outlook reference of approximately **$15.7bn** for FY2026, not a revised forecast imported into this model.

| Reconciliation item | USD m |
|---|---:|
| H1 2026 reported company-defined FCF | 4,760.0 |
| Model H2 consolidated CFO | 7,093.1 |
| Less: model H2 Financing-receivable change | 0.0 |
| Less: model H2 PP&E capex plus capitalized software | (934.9) |
| Model-derived H2 company-style FCF proxy | 6,158.2 |
| Model-derived FY2026 company-style FCF proxy | **10,918.2** |
| Approximate July 22 management-outlook reference | **15,700.0** |
| Unresolved shortfall versus outlook reference | **(4,781.8)** |

The approved SBC repair explains $938.5m of the original $5.72bn gap by adding H2 SBC once to CFO, with the same noncash credit to APIC/equity. The remaining difference is not resolved by the modeled Financing-receivable line: the H2 forecast assumes no change there. It instead reflects the model's lower H2 consolidated-CFO/cash-conversion forecast and a metric-definition gap. The model uses $934.9m of H2 PP&E capex plus capitalized software, while IBM's H1 company-defined “net capital investment” was $743m versus $774m of those two reported investment lines; therefore the company metric cannot yet be reproduced by simply summing the two model investment fields. Cash-tax timing, seasonality, model working-capital assumptions, capital-investment classification, and an incomplete reconciliation from consolidated CFO to IBM's company metric can all contribute. The current record cannot allocate the remaining $4.78bn gap among them.

**Definitions:** consolidated CFO is GAAP cash from operations for the consolidated company; company-defined FCF is IBM's CFO measure adjusted for Financing receivables and net capital investment; operating FCFF is the model's unlevered, ex-Financing valuation cash flow and is not management FCF. This unresolved company-defined-FCF shortfall is a **material investment-judgment qualification requiring the student's approval**. The model has not been forced to management guidance.

## 4. Sensitivity range-dependence assessment

The observed OAT ranking is gross margin (+$12.20/share for +1pp), software growth (+$8.36 for +2pp), SG&A (-$6.14 for -0.5pp), normalized tax (-$5.23 for -2pp), then consulting, infrastructure, and capex. The economics are direct: growth expands revenue and therefore gross profit/EBIT; gross margin changes gross profit on the revenue base; lower SG&A improves EBIT dollar for dollar before tax; and lower cash tax affects FCFF but not EBIT.

That ranking is **not** a standardized importance ranking. The shocks differ in size and unit: gross margin is +1pp, software growth is +2pp, SG&A is -0.5pp, and tax is -2pp. On a simple per-percentage-point value basis, the displayed effects are approximately $12.20 for gross margin, $4.18 for software growth, $12.28 for SG&A, and $2.61 for tax; this rescaling is illustrative, not a claim that the drivers are economically interchangeable. Documented ranges also differ (gross margin 56%-60%, SG&A 29%-32%, cash tax 14%-20%, software growth 3%-8%). Therefore the official OAT ordering should be described as observed output under named shocks, not as a universal ranking of economic importance.

The WACC/g matrix exceeds $231.40 only in the 6.07% WACC row at 2.5% growth ($243.39) and 3.0% growth ($272.66). The 6.57%/3.0% cell is $229.71. Watch / Defer remains defensible because the base 7.07%/2.5% value is below price, all named causal cases remain below price, the market price implies 3.815% terminal growth at base WACC/ROIC, and key WACC, bridge, cash-conversion, and future-dilution evidence remains qualified.

## 5. Peer valuation qualifications

Oracle and Accenture are reference anchors rather than equivalent peers or a blended target. Oracle implies $208.59/share on EV/EBIT and $185.80 on P/E; Accenture implies $60.80 and $114.59. IBM's P/E application uses FY2026E consolidated net income as a labeled common-earnings proxy, not NOPAT, and it has no separate NCI earnings allocation. Business mix, cloud capital intensity, preferred-equity structure, fiscal timing, IBM Financing, tax basis, and capital intensity limit comparison precision.

## 6. Remaining valuation limitations

- **WACC:** reproducible September 1 beta and IBM-specific September 1 bond yield remain unresolved.
- **Terminal value:** 78.06% of operating EV is terminal PV; terminal growth and incremental ROIC dominate the outcome.
- **Pension:** the bridge assigns no separate debt-like pension claim to avoid double counting, but funded status, current liabilities, and cash funding need reconciliation.
- **Financing:** the $1.450bn June book-equity sidecar is a reference, not demonstrated fair value; the operating model excludes Financing receivables and matched debt.
- **Diluted shares:** 952.7m is an H1 weighted-average proxy, not a September 1 point-in-time diluted count.

## 7. Proposed Watch / Defer committee rationale

The student has retained the Watch / Defer recommendation. At the cutoff price, the base value is $49.11/share lower and even the named high case is $7.12/share lower. A lower-WACC/higher-growth matrix can clear price, but it requires a more favorable steady-state combination than the selected base. The unresolved $4.78bn FY2026 management-style FCF gap, high terminal-value share, future-dilution limitation, and qualified WACC/bridge inputs argue for monitoring rather than initiation. Positive review evidence would be reported support for software growth, margin/SG&A conversion, management-FCF reconciliation, debt/cash conversion, a point-in-time diluted-share count, and stronger WACC/bridge evidence.

## 8. Questions requiring the student's approval

The questions below are preserved as historical review questions from the former draft. They do not supersede the student's subsequent approval and retention of Watch / Defer.

1. Is the remaining approximately $4.78bn difference between model-derived FY2026 company-style FCF and the July management-outlook reference acceptable as a disclosed qualification, or should the student perform a separate source-level reconciliation before retaining Watch / Defer?
2. Does the student approve retaining Watch / Defer despite favorable values in the 6.07% WACC / 2.5%-3.0% terminal-growth matrix cells?
3. Does the student approve the current $0 pension bridge convention pending funded-status and cash-funding reconciliation?
4. Does the student approve using the $1.450bn Financing book-equity sidecar with no fair-value premium/discount?
5. Does the student approve the H1 diluted weighted-average share proxy until an as-of-September-1 diluted count can be supported?
