# IBM Project 1 - Validation and AI-use record

**Prepared:** October 14, 2026, America/Indiana/Indianapolis
**Model repository baseline:** `0e3981bd1709ad0c35ef3eff8583c1d3afd0ca02`
**Valuation cutoff:** September 1, 2026, after close
**Decision:** **Watch / Defer** IBM common stock. This is a model-validation record, not a replacement investment decision.

## 1. Final model and execution environment

The final connected model uses USD millions except per-share data. The valuation date is September 1, 2026 after close; IBM's reference closing price is $231.40. The model was independently executed for this record with the repository's `python3` command on macOS (Darwin 24.6.0 arm64), Python 3.14.7. The project requires Python 3.10+ and the standard library only; see `ENVIRONMENT.md`.

| Current calculated output | Result |
|---|---:|
| Low / base / high DCF | $145.1346 / $182.2876 / $224.2811 per share |
| Base WACC | 7.0708% |
| Operating EV | $220,096.1m |
| Terminal PV / operating EV | 78.0637% |
| September 1 estimated cash | $9,280.5m |
| Common equity / diluted-share proxy | $173,665.4m / 952.7m |
| Reverse-DCF terminal growth at $231.40 | 3.8150%, holding 15% terminal incremental ROIC constant |
| FY2026 company-style FCF proxy | $10,918.2m |
| Remaining gap to approximately $15.7bn management-outlook reference | $(4,781.8)m |

## 2. Sources, definitions, and current accounting treatment

| Item | Source, publication date, and treatment |
|---|---|
| H1 2026 history and SBC | [IBM Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm), filed July 23, 2026. It anchors the June 30 balance sheet, H1 results, $7,766m consolidated CFO, and $1,004m H1 SBC noncash adjustment. |
| FY2025 history | [IBM FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231_d2.htm), filed February 24, 2026. It provides FY2025 history and $1,715m SBC; $842m H1 SBC implies $873m H2 2025 SBC. |
| H1 management-defined FCF | $7,766m GAAP CFO - $2,264m Financing-receivable adjustment - $743m net capital investment = $4,759m, rounding to the reported $4.760bn. Consolidated CFO, IBM company-defined FCF, and operating FCFF are distinct measures. |
| SBC schedule | H2 2026: $938.5m, the midpoint of reported H1 2026 $1,004m and historical H2 2025 $873m. FY2027-30: $1,877m annually, provisional and held flat. |
| September 1 price, dividend, WACC, peers | Cutoff-dated records and source URLs are retained in `evidence-ledger.md`; calculation definitions are in `model/valuation.py`. |

Forecast SBC is assumed embedded in the forecast operating-cost ratios that determine EBIT and net income. It is therefore added once to consolidated CFO as a noncash adjustment and credited once to APIC/equity. It is not a cash receipt from share issuance. It is not added again to operating FCFF: the EBIT-based FCFF method already includes the economic expense, while future dilution remains unmodeled. The repair increases estimated September 1 cash by 63/184 of H2 SBC, $321.3m, and raises equity value by approximately $0.34 per share; operating FCFF and operating EV do not change. See `docs/stage2-sbc-review-approved-2026-10-14.md`.

## 3. Validation register: independently executed October 14, 2026

| Check | Expected result | Actual result | Evidence |
|---|---|---|---|
| Full automated suite | 28 passing tests | **28 passed, 0 failed** | Command below; `tests/` |
| Three-statement articulation | All balance-sheet and cash-flow gaps equal zero | PASS; FY2026-30 balance-sheet gaps were 0.0 within floating-point rounding | `test_all_years_articulate`; model run |
| Historical-source reconciliation | Opening balance, segment revenue, and pretax bridges reconcile; H1 FCF rounds to $4,760m | PASS: 0 / 0 / 0.0 gaps; $4,759m calculated, $(1)m rounding difference | `test_historical_base`; model output |
| Enterprise-to-equity bridge | Base bridge produces $182.2876 per share | PASS: $220,096.1m EV, $2,740.5m excess cash/securities, $173,665.4m common equity, 952.7m shares | `test_sep1_bridge_rollforward_and_dividend_once` |
| WACC / terminal-growth direction | Value falls as WACC rises and rises as terminal growth or ROIC rises within controls | PASS | `test_wacc_and_growth_value_monotonicity`; `test_terminal_monotonicities`; `test_terminal_reinvestment_and_boundaries` |
| Peer arithmetic | Each peer multiple bridges consistently to its separately labeled IBM implied value | PASS | `test_peer_and_implied_value_reconciliations` |
| Scenarios | Low < base < high | PASS: $145.13 < $182.29 < $224.28 | `test_cases_reverse_dcf_and_named_scenario_order` |
| September 1 timing | Future stub is 121/184 of H2 FCFF, beginning September 2 | PASS: $4,791.1m residual FCFF | `test_dates_and_correct_stub_convention`; `test_residual_fcff_uses_h2` |
| Deliberate integrity failure | A $1m FY2027 cash break fails without altering inputs | PASS: `SAFE FAILURE DEMONSTRATION: detected as intended — FY2027 balance-sheet check failed: $-1.0000m` | `python3 model/ibm_phase3_model.py --write-output --demo-failure` |
| Recovery | A subsequent normal model build remains articulated | PASS; normal 28-test run and regenerated output completed | same task-run commands |
| SBC controls | One CFO add-back/APIC credit, no H1/H2 double count, no operating-FCFF add-back, bridge-only valuation movement | PASS | four SBC tests listed below |

Commands executed during this task:

```sh
python3 -m unittest discover -s tests -v
python3 model/ibm_phase3_model.py --write-output --demo-failure
python3 app/server.py --port 8770
curl -sS http://127.0.0.1:8770/api/analysis
```

The localhost API returned `statement_articulation: PASS` and `$182.287630` base value. This task did not repeat a fresh GitHub download. The October 14 fresh-download and launcher evidence is historical student-observed evidence in `docs/cold-run-log.md`: the launcher used port 8768 when 8765 was occupied; the then-pre-SBC base was $181.95; and the recorded API/run evidence used 24 tests. It must not be represented as a task-run result for the final SBC model.

### Complete 28-test result list

All returned `ok`: `test_all_years_articulate`, `test_annual_depreciation_after_2026`, `test_bounds_fail`, `test_december_cash_uses_h2_only`, `test_december_equity_uses_h2_only`, `test_fy26_investment_h1_plus_h2`, `test_fy26_net_income_h1_plus_h2`, `test_fy26_revenue_h1_plus_h2`, `test_historical_base`, `test_no_unallocated_corporate_deduction`, `test_one_million_cash_break_fails`, `test_operating_fcff_excludes_financing`, `test_reported_financing_equity`, `test_residual_fcff_not_full_year_prorated`, `test_residual_fcff_uses_h2`, `test_sbc_does_not_change_operating_fcff`, `test_sbc_historical_anchor_and_h2_schedule`, `test_sbc_is_noncash_cfo_addback_with_matching_apic`, `test_cases_reverse_dcf_and_named_scenario_order`, `test_dates_and_correct_stub_convention`, `test_peer_and_implied_value_reconciliations`, `test_prevaluation_rollforward_changes_bridge_not_operating_fcff`, `test_sbc_changes_cash_bridge_not_operating_ev_or_stub`, `test_sep1_bridge_rollforward_and_dividend_once`, `test_terminal_monotonicities`, `test_terminal_reinvestment_and_boundaries`, `test_wacc_and_growth_value_monotonicity`, and `test_wacc_uses_corporate_debt_and_marginal_tax`.

## 4. Historical Locked Changed-Input Record: preserve, do not restate as current

The original locked files and screenshots are preserved unchanged at `docs/locked-changed-input-record-before.txt`, `docs/locked-changed-input-record-after.txt`, `docs/Baseline1.png`, `docs/Baseline2.png`, `docs/Post-Assumption-Change1.png`, and `docs/Post-Assumption-Change2.png`.

| Historical field | Preserved record |
|---|---|
| Prediction time | October 10, 2026, 12:39pm, AI off |
| Input | Software revenue-growth shift: 0pp to +2pp for FY2027-30 |
| Original baseline | $181.95/share, pre-SBC model at baseline commit `f91410f` |
| Prediction | Revenue, operating profit, FCFF, and intrinsic value would rise; Watch / Defer would remain because $231.40 market price was still expected to exceed value |
| Execution time | October 10, 2026, 12:53pm |
| Observed output | $190.31/share; FY2030 EBIT $15,279.2m; FY2030 FCFF $14,152.8m; WACC 7.07% |
| Result and decision effect | Direction matched prediction; value increased by $8.36/share (4.6%); Watch / Defer did not change because $190.31 remained below $231.40 |
| Reset | The AFTER record states the shift returned to 0pp and the original baseline was restored |

**Provenance.** The original predecessor repository `ibm-project-1-b` is reported to contain historical prediction commit `7359ba2`; that object is not available in this repository, so it is not independently verified here. This repository contains archived BEFORE commit `4591725d61928b40a62ea42d5f3a08bd38fabdf1`, committed October 10, 2026 at 18:21:56 -04:00, and results/screenshots commit `2f2384a`. The archived commit time is a later GitHub preservation event, not the original 12:39pm pre-run prediction timestamp. The SBC repair occurred afterward and changed the current base case to $182.29/share; it does not rewrite this historical experiment.

## 5. AI-use record and independently checked corrections

| AI-assisted output or use | Disposition and independent check |
|---|---|
| Code inspection, test execution, documentation, and HTML formatting | OpenAI Codex assisted under student direction. The student remains responsible for sources, assumptions, judgment, and submission. No proprietary terminal, course answers, trade, or submission action was used. Exact model/version metadata beyond the product identity was not provided and is not claimed. |
| September 1 valuation timing / FCFF stub | Material correction. The prior 122/184 convention was independently checked against the September 1 after-close boundary and corrected to 121/184 of H2 FCFF. Automated date/stub tests now enforce it. |
| P/E definition and peer presentation | AI-assisted review identified the need to label FY2026E consolidated net income as a common-earnings proxy rather than NOPAT. Peer arithmetic is now tested. |
| SBC accounting review | The student approved the October 14 repair after review. The $1,004m H1 source, one-time CFO add-back, APIC treatment, no-FCFF add-back, and bridge-only valuation effect are covered by four dedicated tests and `docs/stage2-sbc-review-approved-2026-10-14.md`. |
| Historical experiment | AI did not alter the locked prediction, outcome, screenshots, or timestamps. This document reports them as historical pre-SBC evidence only. |

## 6. Remaining limitations, monitoring conditions, and escalation

- The approximately $4.782bn management-FCF reconciliation gap remains unresolved. It may reflect cash-tax timing, Financing-receivable movement, working-capital seasonality, and nonidentical net-capital-investment definitions. It was not forced to guidance.
- Future dilution and a September 1 point-in-time diluted-share count are unresolved. SBC is economically costly to existing shareholders even though it is noncash in the period.
- Beta is a qualified third-party indication; the cost of debt is a single-A OAS proxy rather than an IBM-specific September 1 borrowing yield.
- Terminal PV represents 78.06% of operating EV. Pension receives no incremental bridge deduction pending a funded-status/cash-funding reconciliation. IBM Financing uses a June 30 book-equity sidecar with no demonstrated fair-value premium or discount.
- Escalate or re-underwrite if reported software growth, gross-margin/SG&A conversion, management-FCF reconciliation, debt/cash conversion, dilution evidence, or dated WACC evidence materially contradicts the base path. The approved action remains Watch / Defer.

## 7. Known-answer training-case status

No IBM course training-case starter file or published answer key is present in the repository. `docs/known-answer-blocker.md` identifies the needed materials. No synthetic substitute was created, and no published known-answer test is claimed as passed.

## 8. PDF status

The final Validation and AI Use PDF was generated from the updated HTML on October 14, 2026, and visually reviewed for readability, table formatting, and content consistency. The PDF contains the approved $182.29 base valuation, 28-test validation record, historical locked experiment, AI-use disclosures, and unresolved financial limitations. The Markdown record provides the more detailed supporting documentation.
