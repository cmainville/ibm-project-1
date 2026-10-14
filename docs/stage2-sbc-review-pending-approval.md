# Stage 2 controlled SBC repair — pending student approval

**Status: uncommitted analyst-review draft.** This report documents the approved accounting repair and its consequences. It does not change the student's Watch / Defer recommendation, does not change the Locked Changed-Input Records, and does not update the deck, PDFs, or screenshots.

## Confirmed evidence and accounting correction

IBM's Q2 2026 Form 10-Q, filed July 23, 2026, reports **$1,004m pre-tax stock-based compensation for the six months ended June 30, 2026**. The filing reports this amount both as cost/SG&A/R&D expense included in income from continuing operations and as a noncash add-back in the GAAP operating cash-flow statement. [IBM Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm)

FY2025 pre-tax SBC was $1,715m and H1 2025 was $842m, implying **$873m H2 2025 SBC**. The forecast schedule is therefore a provisional analyst estimate, not an H2 actual:

| Period | SBC schedule | Basis / status |
|---|---:|---|
| H1 2026 | 1,004.0 | Reported actual; not rolled into H2 again |
| H2 2026 | 938.5 | Provisional midpoint of $873m H2 2025 and $1,004m H1 2026 |
| FY2027-30, each year | 1,877.0 | Provisional annualized H2 2026 amount, held flat |
| H2 2026 sensitivity range | 873.0-1,004.0 | Historical bounds used only for this repair review |

The repair adds forecast SBC once to consolidated CFO because the forecast assumes it is already embedded in the operating-cost ratios that determine EBIT and net income. The same noncash amount is credited once to APIC/total equity. It is explicitly **not** a cash receipt from share issuance. The filing demonstrates SBC is allocated to cost, SG&A, and R&D in the reported base, but cannot prove each future model ratio carries the same allocation; that embedding remains a documented forecast limitation.

## Before-versus-after financial statements

All figures are USD millions. Revenue, EBIT, net income, and operating FCFF are unchanged. CFO, cash, and equity changes are caused only by the SBC CFO add-back/APIC credit.

| Year | CFO before | CFO after | Cash before | Cash after | Equity before | Equity after | Operating FCFF before / after |
|---|---:|---:|---:|---:|---:|---:|---:|
| 2026 | 13,920.6 | 14,859.1 | 9,225.7 | 10,164.2 | 35,379.6 | 36,318.1 | 7,285.7 / 7,285.7 |
| 2027 | 12,240.1 | 14,117.1 | 12,515.1 | 15,330.6 | 37,488.4 | 40,303.9 | 11,596.2 / 11,596.2 |
| 2028 | 13,659.5 | 15,536.5 | 16,896.5 | 21,589.0 | 40,480.8 | 45,173.3 | 12,917.0 / 12,917.0 |
| 2029 | 13,837.1 | 15,714.1 | 21,262.5 | 27,832.0 | 44,209.5 | 50,779.0 | 13,094.1 / 13,094.1 |
| 2030 | 14,265.3 | 16,142.3 | 25,865.6 | 34,312.1 | 48,637.5 | 57,084.0 | 13,514.1 / 13,514.1 |

All forecast balance-sheet and cash-flow checks remain zero within rounding.

## Cash-flow reconciliation

### 1. GAAP consolidated CFO

The repaired H2 2026 CFO is $7,093.1m: forecast net income plus depreciation, amortization, and **$938.5m SBC noncash add-back**, less net operating-asset movements, plus operating-liability movements and taxes payable changes, with zero forecast change in Financing receivables. FY2026 consolidated CFO becomes $14,859.1m.

### 2. IBM management-defined FCF

The historical H1 2026 reconciliation remains exactly: **$7,766m GAAP CFO - $2,264m Financing-receivable adjustment - $743m net capital investment = $4,759m**, rounding to reported $4,760m. The company-defined measure is separate from operating FCFF.

| Item | Before repair | After repair |
|---|---:|---:|
| Model H2 consolidated CFO | 6,154.6 | 7,093.1 |
| Less: H2 Financing-receivable movement | 0.0 | 0.0 |
| Less: model PP&E capex + capitalized software | (934.9) | (934.9) |
| H2 company-style FCF proxy | 5,219.7 | 6,158.2 |
| FY2026 proxy, including reported H1 FCF | 9,979.7 | 10,918.2 |
| Approximate July management-outlook reference | 15,700.0 | 15,700.0 |
| Approximate gap | (5,720.3) | **(4,781.8)** |

The confirmed SBC correction explains **$938.5m**, or about 16% of the original rounded $5.72bn gap. The remaining $4.78bn is unresolved. It must not be closed mechanically because:

- The model retains a $1,641.6m H2 reduction in taxes payable, an unverified cash-tax/timing assumption.
- The model assumes zero H2 Financing-receivable movement. This is a company-defined-FCF comparison item only; it is not added to operating FCFF or the separate Financing sidecar.
- The model's $934.9m of PP&E capex plus capitalized software is not necessarily IBM's company-defined net-capital-investment measure.
- The model already forecasts a $1,236.5m operating-working-capital source of cash. No additional seasonal release is assumed.

### 3. Operating FCFF used in the DCF

Operating FCFF is unchanged. It begins with operating EBIT after the forecast cost ratios, uses normalized operating tax, adds D&A, subtracts operating investment, and excludes Financing. SBC is not added to FCFF because it is economically costly to existing shareholders through dilution even when noncash in the current period. The H1 diluted weighted-average share proxy remains unchanged because no supportable future issuance/dilution schedule was introduced.

## Valuation comparison

| Item | Before | After | Cause |
|---|---:|---:|---|
| September 1 estimated cash | 8,959.2 | 9,280.5 | 63/184 of H2 SBC CFO add-back |
| Operating EV | 220,096.1 | 220,096.1 | Unchanged operating FCFF |
| Common equity | 173,344.1 | 173,665.4 | Higher estimated cash only |
| Low / base / high value per share | 144.80 / 181.95 / 223.94 | 145.13 / 182.29 / 224.28 | +$0.34/share cash-bridge effect |
| WACC / terminal PV share | 7.0708% / 78.0637% | 7.0708% / 78.0637% | Unchanged |
| Reverse-DCF terminal growth | 3.82% | 3.82% | 3.8215% to 3.8150%; bridge-only change |

The WACC/terminal-growth matrix shifts upward by approximately $0.34/share in each cell solely through the cash bridge; terminal economics and the OAT operating sensitivities are unchanged. The low/base/high named cases still all remain below the $231.40 September 1 market price.

## Validation

The expanded suite passed **28/28**: the original 24 tests plus four SBC controls for (1) the $1,004m H1 historical anchor and no H1/H2 double count, (2) CFO add-back and matching APIC/equity treatment, (3) no SBC addition to operating FCFF, and (4) cash-bridge movement without an operating-EV or 121/184-stub change. Existing tests continue to verify IBM Financing separation, date/stub controls, terminal reinvestment, and sensitivity monotonicity.

## Student decision requested

**Recommendation: retain the provisional operating forecast and Watch / Defer recommendation, but qualify the result.** The SBC correction is confirmed accounting treatment. The H2 and FY2027-30 SBC schedule, cash-tax timing, future Financing-receivable movement, capital-investment mapping, and future dilution are still provisional. The $0.34/share valuation increase is not evidence of fundamental operating upside and should not be treated as new shareholder value until a supportable dilution/share-count schedule is reviewed.
