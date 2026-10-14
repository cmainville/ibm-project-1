# Phase 4–5 repair review — final Watch / Defer view, September 1, 2026 after close

**Recommendation: Watch / Defer.** USD millions except per-share values.

## Timing and corrected residual FCFF

FY2026 is H1 reported actual plus H2 forecast. December cash/equity start with June 30 and use only H2 activity. H2 operating FCFF is $7,285.7. After the September 1 close, future cash begins September 2, so residual FCFF is **$4,791.1 = $7,285.7 × 121/184**. The prior 122/184 output ($4,830.7) is superseded; the earlier full-year proxy ($6,082.7) remains historical correction evidence only.

## WACC and valuation

| Item | Base result / method |
|---|---:|
| Risk-free / ERP | 4.79% / 4.14%, September 1 market inputs |
| Beta | 0.70 third-party indication; **QUALIFIED**, regression unresolved |
| Debt cost | 5.47% = 4.79% Treasury + 0.68% single-A OAS proxy; **not** IBM bond yield |
| Marginal WACC tax | 21% assumption, separately disclosed |
| WACC | 7.07% |
| Terminal growth / incremental ROIC | 2.5% / 15.0%, analyst assumptions; ROIC range 12–18% |
| Terminal FCFF | $10,559.7 = $12,671.7 NOPAT − $2,111.9 reinvestment |
| SUPERSEDED naïve terminal FCFF | $13,851.9 |
| Operating EV | $220,096.1 |
| Terminal PV share | 78.1% |

The bridge rolls June cash through 63/184 of modeled H2 activity to **$8,959.2** estimated September 1 cash. Marketable securities ($960.0), Financing equity ($1,450.0), and NCI ($89.0) remain latest reported June 30 values. Corporate debt is $48,940.0. The $1.69 September 10 declared dividend is a **$1,592.2** payable using June 30 basic shares as proxy and appears once. The selected pension bridge claim is $0 under the documented non-double-counting convention. Base common equity is $173,344.1 and base value is **$181.95 per 952.7m diluted-share proxy**.

## Named scenarios and market expectation

| Scenario | Causal description | Value/share |
|---|---|---:|
| LOW — Integration and renewal shortfall | weaker Software/Confluent conversion, Consulting recovery failure, Infrastructure weakness, margin pressure, higher tax/investment | $144.80 |
| BASE — Execution with gradual mix improvement | documented base paths; no probability | $181.95 |
| HIGH — Software and AI conversion upside | stronger Software/AI conversion, Consulting productivity, favorable mix | $223.94 |

At the $231.40 September 1 market close, reverse DCF solves **3.82%** terminal growth while holding terminal ROIC at 15%; this exceeds the selected 2–3% terminal-growth sensitivity and is a diagnostic, not a forecast.

## Peer methods

| Peer | EV/EBIT implied IBM value/share | P/E implied IBM value/share |
|---|---:|---:|
| Oracle | $208.59 | $185.80 |
| Accenture | $60.80 | $114.59 |

Each peer is applied separately. No values are averaged. Differences reflect Oracle cloud/capex and preferred-equity differences, Accenture’s consulting mix and fiscal-year timing, IBM Financing, tax basis, capital intensity, and DCF terminal dependence. IBM P/E uses FY2026E consolidated net income as a labeled common-earnings proxy, not NOPAT or FY2025 tax-distorted GAAP income; no preferred-dividend or NCI earnings-allocation forecast is modeled.

## Tests and remaining work

The recorded run passed 24 tests, including statement articulation, 121/184 boundary, bridge/date/payable controls, terminal ROIC boundaries, peer reconciliations, named scenario ordering, reverse DCF, and a deliberate $1m failure. Start the app with:

`python3 app/server.py --port 8765`

Remaining load-bearing limitations: reproducible cutoff-dated beta; IBM-specific September 1 bond yield; August 10 share count; full pension funded-status/current-liability reconciliation; independently sourced cash taxes; primary-filing quantification of all base-year tax/discrete items; and course training-case answers. The human-only Locked Changed-Input Record experiment was completed October 10, 2026; its BEFORE/AFTER records and screenshots remain preserved in `docs/`.
