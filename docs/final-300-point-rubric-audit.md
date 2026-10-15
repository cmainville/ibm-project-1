# Final 300-point rubric audit — IBM Project 1

**Purpose:** Internal submission-quality audit, not an instructor-assigned grade.

The local course record supplies the six Brightspace criteria, point maxima, and performance labels (Decision-ready, Strong, Developing, and lower), but not the word-for-word LMS descriptors. The Decision-ready tests below are evidence checklists for the supplied criteria, not fabricated quotations. Scores are conservative provisional judgments; each limitation is deducted in its primary criterion only.

| Criterion | Decision-ready test applied | Exact evidence | Level | Score |
|---|---|---|---|---:|
| Problem Definition and Decision Usefulness (45) | Defined user, security, cutoff, action, horizon, conditions, preserved Edition A, and evidence-based evolution. | `README.md`; `docs/Research-Evolution.pdf`; `docs/investment-judgment-and-reversal-triggers.md`; Video 1 `0:00–0:54`; Video 3 `0:00–0:37, 4:14–4:52`. | Strong | 39 / 45 |
| Data Integrity and Traceability (45) | Traceable material inputs, dates, definitions, transformations, forecasts, outputs, and disclosed limitations. | `evidence-ledger.md`; `docs/load-bearing-input-verification.md`; `docs/base-year-normalization.md`; `docs/independent-source-check.md`; `docs/fy2026-fcf-source-reconciliation.md`; validation PDF. | Strong | 37 / 45 |
| Financial Soundness and Judgment (60) | Linked statements support correctly bounded FCFF DCF, WACC, terminal convention, bridge, scenarios, comparables, sensitivities, and action. | `model/`; deck slides 1 and 5–7; `docs/stage2-investment-review.md`; Video 2 `1:13–2:21`; Video 3 `1:26–4:52`. | Strong | 51 / 60 |
| Technical Execution and Usability (45) | Clean user can reproduce/inspect a bounded application and saved executed output; controls and failures are demonstrated. | `README.md`; `ENVIRONMENT.md`; `app/`; `output/visible-base-output.html`; `docs/cold-run-log.md`; Video 2 `0:00–3:30`; Video 3 `0:00–1:26`. | Strong | 40 / 45 |
| Validation, Sensitivity and Reproducibility (75) | Independent checks, known-answer reconciliation, human-authored locked record, AI disposition, failure/recovery, and reproducible tests. | 35-test suite; `docs/week3-known-answer-reconciliation.md`; supplemental and historical locked records; `docs/high-risk-validation-evidence.md`; validation PDF; Video 1 `1:26–2:31`; Video 2 `2:47–4:26`. | Strong | 64 / 75 |
| Professional Communication (30) | Clear, internally consistent decision/evidence/limitations package for a reviewer. | Eight-page deck; Research Evolution and validation PDFs; transcripts; manifest; all video timestamp indexes. | Strong | 25 / 30 |

**Provisional total: 256 / 300.** This is an evidence-based internal estimate, not a prediction of the instructor's grade.

## Deductions and remaining limitations

### Problem Definition and Decision Usefulness — 39 / 45

The committee user, September 1, 2026 boundary, Watch / Defer action, range, and re-underwriting conditions are explicit. The deduction is confined to the separate Edition A checkpoint: the original complete Edition A is preserved in the September 1 Lab 03 attempt and Research Evolution, but no checkpoint receipt exists. Professor Zhang acknowledged preservation/importance but did not grant checkpoint equivalence. This is an administrative uncertainty, not a reason to rewrite Edition A or deduct again elsewhere.

### Data Integrity and Traceability — 37 / 45

Source/definition lineage is documented. The deduction reflects qualified beta methodology, issuer-specific debt cost, future diluted shares, Financing valuation, pension treatment, and the approximately $4.782bn management-style-FCF reconciliation gap. They are disclosed decision-relevant limitations, not hidden source failures.

### Financial Soundness and Judgment — 51 / 60

The linked five-year model, 121/184 September 1 stub, FCFF boundary, WACC, terminal reinvestment, equity bridge, causal cases, reverse DCF, and qualified Oracle/Accenture reference anchors support Watch / Defer. The deduction is for the confidence effect of those qualified inputs, the 78.06% terminal-value share, and the FCF gap, without double-counting the data-traceability issue.

### Technical Execution and Usability — 40 / 45

The app has reproduction instructions, bounded inputs, reset, visible checks, static output, and a deliberate failure/recovery demonstration. The cold run is API/static-file rather than a clean graphical-browser run; the submitted recording mitigates but does not eliminate that limitation.

### Validation, Sensitivity and Reproducibility — 64 / 75

The current 35-test suite passes. The published 12-output benchmark, independent DCF, September 1 stub test, deliberate failures, recovery controls, AI disposition, and supplemental Consulting −1pp human-authored current-model record are present. The historical record is correctly retained as pre-SBC evidence, but its predecessor commit cannot be independently verified here. The benchmark validates conventional DCF arithmetic, not every IBM-specific assumption.

### Professional Communication — 25 / 30

The deck, PDFs, videos, corrected transcripts, and manifest tell a consistent Watch / Defer story. Video 3's `0:45` $179.79 correction is student-confirmed and matches the model. Captions and logged-out repository/video access remain undocumented, and the transcript is not represented as an independently verified verbatim caption file.

## Completed cross-checks

- Current model: $145.13 / $182.29 / $224.28 low/base/high versus $231.40; approximately 7.07% WACC, 2.5% terminal growth, 15% terminal incremental ROIC; Watch / Defer.
- `python3 -m unittest discover -s tests -v`: **35 tests passed**.
- PDFs distinguish current values from historical $181.95 / $190.31 and historical 24/28/30 test counts.
- The complete historical Locked Changed-Input Record remains preserved and unchanged; the current supplemental record is separate.
- `README.md` provides reproduction instructions and links the saved visible executed output.

## Final readiness determination

**ANALYTICAL PACKAGE COMPLETE:** Yes.

**PRE-SUBMISSION REQUIREMENTS VERIFIED:** Not yet. Corrected-caption and logged-out access confirmations cannot be inferred locally.

**READY TO SUBMIT:** Not yet. Complete the manual external checks, download/upload the named Brightspace files, and handle the Edition A checkpoint only as directed by the instructor.

**BRIGHTSPACE SUBMITTED:** No. No receipt is present or claimed.
