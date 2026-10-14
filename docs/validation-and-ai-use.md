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
| FCF definition / period check | The Q2 10-Q definition and H1 reconciliation were independently recomputed; the H2 model proxy is then kept separate from IBM guidance. See `docs/fy2026-fcf-source-reconciliation.md`. |
| Independent historical-anchor check | IBM's Q2 2026 Form 10-Q, filed July 23, 2026: reported H1 segment revenue reconstructs to Software $14,813m + Consulting $10,599m + Infrastructure $7,161m + Financing $406m + Other $100m = $33,079m. This equals the model's H1 consolidated revenue anchor; difference $0m. See `docs/independent-source-check.md`. |
| SBC schedule | H2 2026: $938.5m, the midpoint of reported H1 2026 $1,004m and historical H2 2025 $873m. FY2027-30: $1,877m annually, provisional and held flat. |
| September 1 price, dividend, WACC, peers | Cutoff-dated records and source URLs are retained in `evidence-ledger.md`; calculation definitions are in `model/valuation.py`. |

Forecast SBC is assumed embedded in the forecast operating-cost ratios that determine EBIT and net income. It is therefore added once to consolidated CFO as a noncash adjustment and credited once to APIC/equity. It is not a cash receipt from share issuance. It is not added again to operating FCFF: the EBIT-based FCFF method already includes the economic expense, while future dilution remains unmodeled. The repair increases estimated September 1 cash by 63/184 of H2 SBC, $321.3m, and raises equity value by approximately $0.34 per share; operating FCFF and operating EV do not change. See `docs/stage2-sbc-review-approved-2026-10-14.md`.

## 3. Validation register: independently executed October 14, 2026

| Check | Expected result | Actual result | Evidence |
|---|---|---|---|
| Full automated suite at final-documentation baseline | 30 passing tests | **30 passed, 0 failed** | Command below; `tests/` |
| Published Week 3 known-answer case | All 12 published outputs reconcile; 11% WACC decreases value and 10% restores baseline | **PASS:** all 12 within tolerance; $23.4140/share at 11%; $27.4974/share restored at 10% | `test_week3_dcf_benchmark.py`; `docs/week3-known-answer-reconciliation.md` |
| Three-statement articulation | All balance-sheet and cash-flow gaps equal zero | PASS; FY2026-30 balance-sheet gaps were 0.0 within floating-point rounding | `test_all_years_articulate`; model run |
| Historical-source reconciliation | Opening balance, segment revenue, and pretax bridges reconcile; H1 FCF rounds to $4,760m | PASS: 0 / 0 / 0.0 gaps; $4,759m calculated, $(1)m rounding difference | `test_historical_base`; model output |
| Enterprise-to-equity bridge | Base bridge produces $182.2876 per share | PASS: $220,096.1m EV, $2,740.5m excess cash/securities, $173,665.4m common equity, 952.7m shares | `test_sep1_bridge_rollforward_and_dividend_once` |
| WACC / terminal-growth direction | Value falls as WACC rises and rises as terminal growth or ROIC rises within controls | PASS | `test_wacc_and_growth_value_monotonicity`; `test_terminal_monotonicities`; `test_terminal_reinvestment_and_boundaries` |
| Peer arithmetic | Each peer multiple bridges consistently to its separately labeled IBM implied value | PASS | `test_peer_and_implied_value_reconciliations` |
| Scenarios | Low < base < high | PASS: $145.13 < $182.29 < $224.28 | `test_cases_reverse_dcf_and_named_scenario_order` |
| September 1 timing | Future stub is 121/184 of H2 FCFF, beginning September 2 | PASS: $4,791.1m residual FCFF | `test_dates_and_correct_stub_convention`; `test_residual_fcff_uses_h2` |
| Deliberate integrity failure | A $1m FY2027 cash break fails without altering inputs | PASS: `SAFE FAILURE DEMONSTRATION: detected as intended — FY2027 balance-sheet check failed: $-1.0000m` | `python3 model/ibm_phase3_model.py --write-output --demo-failure` |
| Recovery | A subsequent normal model build remains articulated | PASS; the historical recovery run at that review stage had 28 tests; the final-documentation baseline had 30. The current high-risk extension has 35 tests and passed in full. | same task-run commands; complete current result below |
| SBC controls | One CFO add-back/APIC credit, no H1/H2 double count, no operating-FCFF add-back, bridge-only valuation movement | PASS | four SBC tests listed below |
| Independent DCF / bridge recalculation | Separate arithmetic reproduces timing, WACC, terminal reinvestment, EV and equity bridge | PASS: $220,096.1069m EV, $173,665.4251m equity, $182.287630/share | `scripts/high_risk_diagnostics.py`; `test_independent_dcf_ties_out_without_production_dcf_call` |
| High-risk definition / failure controls | Period-correct H1/H2 FCF boundary plus terminal and bridge invalid-input rejection | PASS | `tests/test_high_risk_validation.py`; `docs/high-risk-validation-evidence.md` |

Commands executed during this task:

```sh
python3 -m unittest discover -s tests -v
python3 model/ibm_phase3_model.py --write-output --demo-failure
python3 app/server.py --port 8770
curl -sS http://127.0.0.1:8770/api/analysis
```

The localhost API returned `statement_articulation: PASS` and `$182.287630` base value. This task did not repeat a fresh GitHub download. The October 14 fresh-download and launcher evidence is historical student-observed evidence in `docs/cold-run-log.md`: the launcher used port 8768 when 8765 was occupied; the then-pre-SBC base was $181.95; and the recorded API/run evidence used 24 tests. It must not be represented as a task-run result for the final SBC model.

### Complete 30-test result list at the final-documentation baseline

All returned `ok`: the 28 IBM tests listed in the prior record, plus `test_published_twelve_outputs` and `test_wacc_sensitivity_decreases_value_and_baseline_restores` in `test_week3_dcf_benchmark.py`.

### Post-baseline high-risk validation extension

Five nonredundant tests were then added to test a separate DCF/bridge
calculation path, source-defined FCF period boundary, terminal-reinvestment
guardrail, operating-cash bridge guardrail, and articulated material Consulting
shock. The current project suite is therefore **35 tests**; its actual final
run is recorded in `docs/high-risk-validation-evidence.md` and
`docs/cold-run-log.md`. This update does not recharacterize the historical
28-test recovery run or the final-documentation 30-test record.

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

## 4A. Supplemental prospective Locked Changed-Input Record — current model

This supplemental validation is separate from, and does not replace, the October 10 historical experiment. The student declared that Part A was independently written with generative AI assistance and autocomplete off before execution. The committed BEFORE file is `docs/supplemental-locked-test-before.txt` at Git commit `c5a999f5942b3220bd085c59b3f4d6e9a872d587` (October 14, 2026, 17:22:31 -04:00). The completed objective record and student evaluation are in `docs/supplemental-locked-test-after.txt`.

**Human-authored Part A prediction (verbatim):**

> Human prediction date and time: 10/14 @ 5:18pm
> Tested baseline Git commit: a2084eaddc466784f27a6187139615be08099d5f
> Driver name and units: Consulting revenue-growth shift, percentage points
> Old driver value: 0 percentage points
> New driver value: -1 percentage points
> Why the change is economically meaningful: Consulting is one of IBM's main operating segments and weaker demand could reduce projected sales and profitability.
> Expected revenue direction: Lower
> Expected operating-profit direction: Lower
> Expected FCFF direction: Lower
> Expected intrinsic-value direction: Lower
> Expected investment-decision effect: Watch/Defer
> Reason for the prediction: Lower forecast operating cash flows would generally lower discounted operating value for IBM.

Part B was blank in commit `c5a999f` and the BEFORE file remained unchanged before execution.

| Item | Verified supplemental evidence |
|---|---|
| Execution | Started October 14, 2026, 17:25:03 -04:00. Existing local API: GET `/api/analysis`; POST `{"overrides":{"consulting_growth_shift":-0.01}}`; POST with `0` for reset. |
| FY2030 revenue / operating EBIT / operating FCFF | Baseline $82,218.920m / $14,717.413m / $13,514.090m; changed $81,296.371m / $14,550.431m / $13,329.082m; changes $(922.549)m / $(166.981)m / $(185.008)m. |
| WACC and intrinsic value | WACC unchanged at 7.070782%. Value $182.287630 to $179.793423 per share: $(2.494207), or -1.368281%. |
| Integrity, decision, and reset | Baseline, changed, and reset API results articulated PASS. Changed value remained below $231.40 and status remained Watch / Defer. Reset returned exactly $182.287630; low/high after reset were $145.1346/$224.2811 and articulated PASS. |
| Expected-versus-observed / student conclusion | The observed directions matched the pre-run prediction. The student wrote: “Yes, the results matched my prediction” because weaker Consulting growth reduced projected revenue, operating profit, FCFF, and discounted value; and “No, my recommendation remains Watch / Defer” because $179.79 remained further below $231.40 and did not provide sufficient margin of safety. |
| Tests | `python3 -m unittest discover -s tests -v`: 30 passed, 0 failed. |

The Git precommit, blank committed Part B, later execution time, reset, and objective observations make this **VERIFIED** prospective precommit evidence. This verification does not retroactively confer the same precommit verification on the original October 10 record.

## 5. AI-use record and independently checked corrections

Exact model/version identifiers and individual interaction timestamps were not retained and are not claimed. Dates below are documented work dates or defensible October 2026 ranges. AI assistance is not itself independent evidence; the student owns the investment decision, approved assumptions, and all final claims.

| Tool | Date/range | Material assistance/output | Disposition, independent check, and impact |
|---|---|---|---|
| ChatGPT — OpenAI | October 2026 project work; exact sessions unavailable | Project planning, course-requirement interpretation, financial-model methodology/accounting discussion, research/source-location assistance, model-limitation review, independent-check planning, Codex implementation instructions, Research Evolution/written-deliverable preparation, Week 3 benchmark discovery, and rubric/compliance review. | Used as planning and drafting support. Material financial claims were checked against filings, model output, tests, and the stated course source; it did not determine the student's Watch / Defer judgment. |
| Codex — OpenAI | October 2026 implementation/validation work; exact sessions unavailable | Python implementation/debugging, interactive workbench, automated tests, student-reviewed valuation/accounting corrections, documentation, HTML/PDF export, and Git operations under student direction. | Changes were reviewed through model output, 30 automated tests, PDF inspection, and student approval where required. No exact model/version is claimed. |
| September 1 timing / FCFF stub | October 2026 | AI-assisted inspection identified an incorrect 122/184 stub convention. | Independently checked against the after-close September 1 boundary; corrected to 121/184 and enforced by automated tests. |
| SBC accounting review | October 14, 2026 | AI-assisted implementation of a forecast SBC noncash CFO add-back/APIC treatment. | Student approved the $938.5m H2 2026 and $1.877bn FY2027-30 provisional schedule. Four dedicated tests verify one add-back/APIC credit, no H1/H2 double count, no operating-FCFF add-back, and bridge-only movement. |
| Published Week 3 benchmark | October 2026 | AI assistance located, interpreted, and implemented the public Lab 05 benchmark. | The publicly available Week 3 Lab 05 training-case inputs and published expected outputs were consulted to complete the Project 1 known-answer reconciliation required by the course. AI assistance helped locate, interpret, and implement the benchmark. The calculated results were generated from the published inputs and compared against the official reference outputs. This was a disclosed validation exercise, not the use of private or unreleased grading answers. All 12 comparisons and the 10%-to-11% WACC direction check passed. |
| Historical experiment | October 10, 2026 historical evidence | The locked prediction, outcome, screenshots, and timestamps were not altered by AI. | The record remains historical pre-SBC evidence only; reported times are distinguished from later Git preservation events. |

The published answers are a required reference for the known-answer validation, not hardcoded calculation inputs. The standalone conventional DCF benchmark does not independently prove every IBM-specific timing, Financing, or ROIC-based terminal-reinvestment convention. No private or unreleased course solution is claimed.

## 6. Remaining limitations, monitoring conditions, and escalation

- The approximately $4.782bn management-FCF reconciliation gap remains unresolved. IBM company-defined FCF begins with consolidated CFO and adjusts Financing receivables and net capital investment, whereas the DCF uses EBIT-based operating FCFF that excludes IBM Financing and applies an operating tax/reinvestment convention. They are therefore different measures, not interchangeable targets. The source-defined H1 arithmetic ties; the model’s H2 proxy has a $1.642bn taxes-payable draw, $1.639bn operating-asset use, $934.9m capital investment, and zero modeled Financing-receivable movement, but IBM did not disclose an H2 component bridge. The management outlook was not forced into the forecast because that would conceal, rather than resolve, the analytical difference. See `docs/fy2026-fcf-source-reconciliation.md`.
- Future dilution and a September 1 point-in-time diluted-share count are unresolved. SBC is economically costly to existing shareholders even though it is noncash in the period.
- Beta is a qualified third-party indication; the cost of debt is a single-A OAS proxy rather than an IBM-specific September 1 borrowing yield.
- Terminal PV represents 78.06% of operating EV. Pension receives no incremental bridge deduction pending a funded-status/cash-funding reconciliation. IBM Financing uses a June 30 book-equity sidecar with no demonstrated fair-value premium or discount.
- Even favorable Software-growth cases remain below the $231.40 reference price under the named causal scenarios. Qualified beta and debt-yield inputs, 78.06% terminal-value dependence, and unresolved future dilution reduce confidence in favorable valuation outcomes. Escalate or re-underwrite if reported software growth, gross-margin/SG&A conversion, management-FCF reconciliation, debt/cash conversion, dilution evidence, or dated WACC evidence materially contradicts the base path. The approved action remains Watch / Defer.

## 7. Known-answer training-case status

The published Week 3 training case and official answer table were located in the FIN 43900 course repository. A standalone conventional-DCF implementation calculates all 12 outputs from the published inputs; every comparison passed the documented tolerance. At 11% WACC it calculates $23.4140/share, below the restored 10% baseline of $27.4974/share. See `docs/week3-known-answer-reconciliation.md` and `docs/known-answer-blocker.md` for source links, complete comparisons, commands, and scope.

This resolves the course's published Week 3 known-answer check. It does not represent the training case as an end-to-end test of IBM-specific timing, ROIC-terminal, Financing, or forecast logic.

## 8. PDF status

The final Validation and AI Use PDF was regenerated from `docs/validation-and-ai-use.html` on October 14, 2026, following six-page visual and text-extraction validation. It includes:

- The historical 30-test final-documentation record and the current 35-test result, with 0 failures.
- The independent DCF/bridge tie-out, period-correct H1/H2 FCF definition check, and targeted terminal/bridge failure controls.
- All 12 published Week 3 DCF reconciliations and the 10%-to-11% WACC sensitivity verification.
- IBM's revised $182.29 per-share base valuation (with $145.13 low and $224.28 high cases).
- The historical Locked Changed-Input Record ($181.95 to $190.31 per share).
- The separately verified supplemental prospective Consulting-growth test and its student-authored evaluation.
- AI-use disclosures and the unresolved approximately $4.78bn FY2026 management-FCF reconciliation gap, dilution, WACC, terminal-value, pension, and IBM Financing limitations.

This PDF was generated from the corresponding HTML validation record. The Markdown source provides additional supporting detail.

## Appendix A — Complete historical Locked Changed-Input AFTER record

The following AFTER record is reproduced verbatim from `docs/locked-changed-input-record-after.txt`. The separate BEFORE snapshot contains Part A's pre-run prediction with Part B blank. This historical experiment preceded the later SBC accounting repair; its $181.95 baseline and $190.31 observed value are not the current approved $182.29 base. The reported predecessor commit `7359ba2` has not been independently verified in this repository. Archived BEFORE commit `4591725` is a later preservation event, not evidence that the original 12:39pm prediction was first created at that upload time.

```text
FIN 43900 PROJECT 1 - LOCKED CHANGED-INPUT RECORD
IBM Software Revenue Growth Test

PART A - BEFORE RUNNING THE TEST (AI OFF)

Date and time of prediction: 10/10/2026 @ 12:39pm
Baseline model Git commit ID: f91410f
Prediction-file Git commit ID (save after committing, before running): 4591725

Input being changed: Software revenue growth shift
Original input: 0 percentage points
New input: +2 percentage points (for 2027-2030)
Original IBM intrinsic value: $181.95 per share

MY PREDICTION (before running the test):
Expected effect on revenue, operating profit, and FCFF: I expect IBM's revenue, operating profit, and free cash flow to increase as stronger software growth generates additional sales and earnings over the forecast period.

Expected effect on intrinsic value per share: I expect IBM's intrinsic value to increase above the baseline valuation of $181.95 per share because higher projected free cash flows should increase the present value of the business.

Expected effect on my investment recommendation: I expect IBM's valuation to become more attractive, but I do not anticipate this adjustment alone will change my Watch/Defer recommendation, given the current market price of $231.40.

Why I expect these changes: I believe IBM's AI and hybrid-cloud businesses could drive stronger software revenue growth than my baseline forecast assumes. Higher software demand could improve operating earnings and free cash flow, supporting a higher intrinsic valuation over time.


PART B - AFTER RUNNING THE TEST

Test date and time: 10/10/2026 @ 12:53pm
New IBM intrinsic value per share: $190.31
New 2030 operating profit (EBIT), $ millions: $15,279.2M
New 2030 FCFF, $ millions: $14,152.8M
WACC after change: 7.07%

Did the results move as I predicted?: Yes, as increasing IBM's software revenue growth by 2 percentage points raised its intrinsic value from $181.95 to $190.31 per share,(+ $8.36 (4.6%)). Operating profit and free cash flow also increased, which supports my prediction that stronger software growth would improve IBM's financial performance and valuation.

Did my investment recommendation change?: No. My recommendation remains Watch/Defer. Although the higher software growth assumption increased IBM's intrinsic value to $190.31, it remains below the market price of $231.40. This suggests stronger growth alone is not enough to justify initiating a position at the current valuation.

If results differed from my prediction?: The results moved in the direction I expected, so there was no directional difference from my prediction. However, the valuation increase was not large enough to change my investment recommendation. This shows that even with stronger software growth, IBM's current market price remains above my model's estimated intrinsic value.

Location of before/after saved results: Screenshots of the original baseline ($181.95/share) and the +2 percentage-point software growth test ($190.31/share) are saved in my project’s GitHub repository.
Did I reset the model to its original baseline? Yes. I reset the software growth adjustment to 0 percentage points and restored the original baseline model.
```
