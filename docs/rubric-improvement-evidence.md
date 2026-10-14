# Rubric-improvement evidence — Data, financial judgment, and validation
INSTRUCTOR DETERMINATION**; recordings/submission artifacts are outside this
workstream.
This document evaluates evidence against the three published 45/60/75-point
descriptors supplied by the student. It does not self-award points or override
the separate Edition A checkpoint, which remains **PENDING INSTRUCTOR
DETERMINATION**.

## Data Integrity and Traceability — 45 points

| Initial weakness | New independently verified work | Supporting evidence | Status / limitation |
|---|---|---|---|
| Material FCF guidance gap was disclosed but not reconstructed by period or definition. | Rebuilt H1 reported FCF, H2 model proxy, and FY bridge; separated management FCF, CFO, and operating FCFF. | `docs/fy2026-fcf-source-reconciliation.md`; `scripts/high_risk_diagnostics.py`; FCF boundary test | **QUALIFIED BUT DECISION-DEFENSIBLE** — management did not publish the needed H2 component bridge. |
| WACC/bridge source lineage had qualifications scattered across files. | Created one load-bearing audit with values, dates, definitions, transformations, exclusions, restrictions, and diagnostic sensitivities. | `docs/load-bearing-input-verification.md`; `evidence-ledger.md` | **QUALIFIED BUT DECISION-DEFENSIBLE** — beta window and IBM-specific dated bond yield remain unresolved. |
| An independent definition check was narrow. | Reperformed H1 management FCF from the 10-Q and tested it in code. | `docs/independent-source-check.md`; high-risk test | **RESOLVED WITH EVIDENCE** for the cited definition, not for all forecast inputs. |

Why this supports the descriptor: load-bearing inputs now have source and
transformation lineage, and the material residual uncertainty is explicitly
identified rather than hidden. Required student approval: none unless a future
source contradiction prompts a model revision.

## Financial Soundness and Judgment — 60 points

| Initial weakness | New independently verified work | Supporting evidence | Status / limitation |
|---|---|---|---|
| Base valuation relied mainly on the production path. | Independently recalculated stub FCFF, WACC, terminal reinvestment, EV, and equity bridge. | `scripts/high_risk_diagnostics.py`; `tests/test_high_risk_validation.py` | **RESOLVED WITH EVIDENCE** within numerical tolerance. |
| Watch / Defer lacked a single quantitative reversal framework. | Calculated market gaps, price-crossing WACC/growth combinations, terminal/ROIC/beta/debt/bridge diagnostics, and explicit monitoring triggers. | `docs/investment-judgment-and-reversal-triggers.md` | **QUALIFIED BUT DECISION-DEFENSIBLE** — diagnostics are not probability-weighted forecasts. |
| FCF discrepancy could be mistaken for an FCFF valuation error. | Identified definition difference and tested model cash-flow components without forcing guidance into operating FCFF. | `docs/fy2026-fcf-source-reconciliation.md` | **UNRESOLVED AND MATERIAL** — $4.782bn approximate gap weakens confidence, reinforcing the approved action. |

Why this supports the descriptor: conventions, timing, bridge, terminal
reinvestment, scenarios, and action boundaries are explicit; the decision is a
range/action with risks and reversal triggers, not a single asserted price
target. Required student approval: only if they want to change the approved
forecast or recommendation after future disclosures.

## Validation, Sensitivity and Reproducibility — 75 points

| Initial weakness | New independently verified work | Supporting evidence | Status / limitation |
|---|---|---|---|
| Existing suite did not independently tie out full IBM DCF/bridge arithmetic. | Added standalone calculation-path test and validation matrix. | `scripts/high_risk_diagnostics.py`; `tests/test_high_risk_validation.py`; `docs/high-risk-validation-evidence.md` | **RESOLVED WITH EVIDENCE**. |
| Boundary failures concentrated in the $1m balance-sheet demonstration. | Added terminal-reinvestment and bridge-reserve failure injections with expected error and recovery controls. | high-risk test file and evidence document | **RESOLVED WITH EVIDENCE**. |
| Cash-flow definition and period boundary were not separately testable. | Added H1 actual + H2 forecast reconciliation test. | high-risk test file | **RESOLVED WITH EVIDENCE**. |
| Original changed-input provenance was historical. | Preserved it and added the student-authored, AI-off, precommitted Consulting −1pp experiment with student conclusion. | `docs/supplemental-locked-test-before.txt`, `docs/supplemental-locked-test-after.txt`, validation record | **RESOLVED WITH EVIDENCE** for the supplemental test; original October 10 record remains historical, not retroactively precommitted. |

Known-answer reconciliation, AI-use disclosures, the cold run, and limitations
remain in `docs/validation-and-ai-use.md` and `docs/cold-run-log.md`. The
isolated-copy current-version test is recorded after its execution. Required
student/instructor action: the Edition A checkpoint remains **PENDING
INSTRUCTOR DETERMINATION**; recordings/submission artifacts are outside this
workstream.
