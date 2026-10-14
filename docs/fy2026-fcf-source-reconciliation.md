# FY2026 free-cash-flow source reconciliation

**Purpose.** This is a diagnostic reconciliation of measures that are often
mistakenly treated as interchangeable. It does not revise the approved FCFF
forecast, the $182.29/share base DCF, or the Watch / Defer decision.

**Cutoff discipline.** All source observations below were publicly available by
the September 1, 2026 after-close valuation date. Figures are USD millions;
model figures were reproduced on October 14, 2026 with
`python3 scripts/high_risk_diagnostics.py`.

## Definitions and source evidence

IBM defines free cash flow as net cash from operating activities **less the
change in Financing receivables and net capital investment**, with net capital
investment including capital expenditures, software investment, and other asset
sales. See [IBM Q2 2026 Form 10-Q, Liquidity and Capital
Resources](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm)
(filed July 23, 2026). The same definition and H1 reconciliation appear in
[IBM's July 22 Q2 release](https://newsroom.ibm.com/2026-07-22-IBM-RELEASES-SECOND-QUARTER-RESULTS).

The three measures are deliberately separated:

1. **GAAP consolidated CFO** includes IBM Financing cash flows, interest,
   cash-tax timing, and noncash add-backs.
2. **IBM management-defined FCF** starts with that CFO, removes the change in
   Financing receivables, and subtracts net capital investment. A positive
   reported $2,264m H1 Financing-receivable adjustment is subtracted; it must
   not also be subtracted a second time from CFO.
3. **Operating FCFF in the DCF** excludes IBM Financing and uses operating
   EBIT after normalized operating tax plus D&A less investment and operating
   working-capital movement. It is an unlevered valuation measure, not
   management FCF and not a cash-available-to-common-shareholders measure.

The DCF discounts only the September 2–December 31 portion of H2 FCFF, using
the approved **121/184** residual convention, then FY2027–30 FCFF and a
ROIC-based terminal FCFF. It does not discount FY2026 management FCF.

## Period-correct H1/H2/FY bridge

| Component | H1 actual | H2 model forecast | FY2026 source/model bridge | Management reference |
|---|---:|---:|---:|---:|
| Consolidated CFO | 7,766.0 | 7,093.1 | — | No component forecast disclosed |
| Less: change in Financing receivables | (2,264.0) | 0.0 | — | No component forecast disclosed |
| Less: net capital investment | (743.0) | (934.9) | — | No component forecast disclosed |
| Company-style FCF | **4,759.0** | **6,158.2** | **10,918.2** | **about 15,700** |

H1 calculation: $7,766.0 − $2,264.0 − $743.0 = **$4,759.0m**, which rounds to
IBM's reported **$4,760m**. The H2 proxy uses the model’s CFO less its modeled
change in Financing receivables and H2 PP&E/software investment. It has no
modeled asset-sale proceeds, whereas IBM's reported *net* capital investment
definition can include them.

IBM reported about **$14.7bn** FY2025 FCF and said on July 22 that FY2026 FCF
was expected to increase by about **$1bn**. That is an approximate full-year
reference of **about $15.7bn**, not a management component forecast. It implies
about $10.94bn for H2 after the reported $4.760bn H1 amount. The modeled H2
proxy is $6.158bn, leaving **about $4.782bn** ($15.700bn − $10.918bn) below the
reference. The precision belongs to the model arithmetic, not to IBM's
“about $1bn” guidance language.

## H2 model-CFO waterfall (not a claimed management-guidance reconciliation)

| Modeled H2 CFO component | USD m | Cash effect |
|---|---:|---|
| Net income | 4,004.6 | source |
| Depreciation | 1,089.8 | noncash add-back |
| Amortization | 1,465.3 | noncash add-back |
| Stock-based compensation | 938.5 | noncash add-back; credited once to APIC/equity |
| Operating assets | (1,639.4) | use of cash |
| Operating liabilities | 2,875.9 | source of cash |
| Taxes payable | (1,641.6) | use of cash |
| Financing receivables | 0.0 | model assumes no H2 balance movement; not described as runoff |
| **Modeled consolidated CFO** | **7,093.1** |  |
| PP&E capex plus capitalized software | (934.9) | investment |
| **Modeled H2 company-style FCF proxy** | **6,158.2** |  |

This waterfall exactly reconstructs the model’s H2 forecast. It does **not**
prove how IBM expected to produce the $15.7bn outlook: IBM did not disclose an
H2 CFO, Financing-receivable, capital-investment, or asset-sale bridge in the
July outlook. Thus the $4.782bn cannot responsibly be allocated among these
lines as if it were a sourced management reconciliation.

## What is demonstrated versus unresolved

**Demonstrated accounting/definition controls.** The H1 reported definition
ties; Financing receivables are removed once in the management-FCF calculation;
the H2 model assumes zero Financing-receivable movement; SBC is present once as
a noncash CFO add-back and is not added again to operating FCFF. Therefore the
remaining gap is not explained by omission of the approved $938.5m H2 SBC
add-back or by double-counting the H1 $2.264bn Financing adjustment.

**Model-assumption drivers.** Within the model, the largest H2 cash drags are
the $1.642bn tax-payable draw, the $1.639bn operating-asset build, and $934.9m
of PP&E/software investment. Operating liabilities provide a $2.876bn offset.
The model does not separately forecast cash taxes or asset-sale proceeds, so
those items cannot be compared line-for-line with management's definition.
H1 IBM commentary attributes flat year-over-year FCF in part to inventory,
higher cash taxes, and net interest; that supports the relevance of cash
conversion, but does not quantify H2.

**Investment implication.** The evidence does not establish a production-model
error or justify forcing management guidance into FCFF. It does weaken
confidence in cash-conversion calibration and reinforces Watch / Defer: before
an initiation, the committee should re-underwrite after a disclosed H2 CFO/FCF
bridge, cash-tax detail, Financing-receivable movement, and capex/software
investment outcome become available. A stronger Software-growth case alone
does not resolve this cash-conversion uncertainty.

## Sources and reproducibility

- [IBM 2025 year-end earnings materials](https://www.ibm.com/downloads/documents/us-en/1550f7eea8c0ded6)
  (January 28, 2026): FY2025 CFO/FCF and FY2026 “about $1bn” outlook context.
- [IBM Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm)
  (July 23, 2026): H1 CFO, cash-flow line items, Financing receivables, and
  management FCF definition/reconciliation.
- [IBM Q2 2026 earnings release](https://newsroom.ibm.com/2026-07-22-IBM-RELEASES-SECOND-QUARTER-RESULTS)
  (July 22, 2026): FY2026 FCF outlook and H1 reconciliation.
- Reproduce model arithmetic: `python3 scripts/high_risk_diagnostics.py`.
