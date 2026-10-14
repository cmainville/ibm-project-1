# Pre-recording audit — IBM Project 1

**Audit date:** October 14, 2026
**Repository/commit tested:** `cmainville/ibm-project-1`, current `main` commit recorded in `docs/cold-run-log.md`
**Decision:** Watch / Defer; $145.13 / $182.29 / $224.28 low/base/high per share.

| Requirement | Status | Evidence location | Remaining issue |
|---|---|---|---|
| Five-year linked statements and base-year normalization | PASS | `model/`, `docs/base-year-normalization.md`, tests | None identified. |
| Filed sources; Software, Consulting, Infrastructure and Financing assumptions | PASS | `evidence-ledger.md`, `model/inputs.json`, `docs/assumption-challenge-record.md` | Forecasts remain analyst assumptions. |
| FCFF, WACC, terminal value and EV-to-equity bridge | PASS | `model/valuation.py`, `output/phase3-model-output.json`, deck | WACC/pension/Financing/dilution qualifications remain disclosed. |
| Peer consistency, scenarios, OAT sensitivities, range dependence and reverse DCF | PASS | `docs/stage2-investment-review.md`, deck, valuation tests | Peer comparability remains qualified. |
| Interactive controls, bounds/reset, broken-input recovery | PASS | app/API cold run; validation record; tests | None identified. |
| Published Week 3 known-answer reconciliation | PASS | `docs/week3-known-answer-reconciliation.md`, 2 benchmark tests | Conventional DCF only; not an IBM-engine end-to-end test. |
| Independent source/definition check | PASS | `docs/independent-source-check.md`, validation record | Dividend and H1 2026 $33,079m revenue reconstruction pass; management-FCF proxy gap remains unresolved. |
| Historical Locked Changed-Input Record | PASS | locked text, screenshots, Validation Appendix A | Historical pre-SBC result is correctly separated from current model. |
| Full AI-use disclosure | CORRECTED | `docs/validation-and-ai-use.*` | Student remains responsible for final presentation claims; exact model/version and individual timestamps are unavailable. |
| Partner challenge from earlier labs | CORRECTED | `docs/assumption-challenge-record.md` | Mrigna Goel is attributed only to the student-reported verbal challenge; exact date/notes unavailable and Lab 12 absence is disclosed. |
| Current-model cold run and reproducible setup | PASS | `docs/cold-run-log.md`, `README.md`, `ENVIRONMENT.md` | API-only browser validation if no visible browser is recorded. |
| Saved visible executed output | PASS | `output/visible-base-output.html` | Static output is read-only, not interactive. |
| Research Evolution and Edition A checkpoint | PENDING INSTRUCTOR DETERMINATION | `docs/Research-Evolution.*`, `docs/edition-a-checkpoint-status.md` | Lab 03 attempt/grade does not prove submission to the separate ungraded checkpoint; instructor response pending. |
| Eight-slide decision deck | PASS | `docs/Decision-Deck.*` | None identified. |
| HTML/PDF/Markdown/model consistency | PASS | PDF checks and current audit | Future edits require re-export. |
| Videos, transcripts, manifest, Brightspace submission | DEFERRED UNTIL RECORDING / SUBMISSION STAGE | Submission architecture | Student action required after recordings; do not create now. |

## Final audit limitations

- FY2026 company-style FCF proxy remains approximately $4.78bn below the management-outlook reference; it was not forced to guidance.
- Future dilution, point-in-time diluted shares, IBM-specific borrowing cost, pension treatment, and Financing fair value remain qualified.
- The actual partner exchange is a student-reported retrospective recollection with Mrigna Goel identified as the challenger; the exact date and contemporaneous notes are unavailable. No Lab 12 peer-review evidence exists because the student was absent.

## Published-criteria evidence review

The detailed analytic rubric is not available in this workspace or publicly verified here; no scores or weights are inferred.

| Published criterion | Status | Evidence and limitation |
|---|---|---|
| Problem Definition and Decision Usefulness | QUALIFIED | `README.md`, Research Evolution, and Decision Deck define the no-current-position committee user, September 1 cutoff, valuation range, Watch / Defer decision, and monitoring conditions. The separate Edition A checkpoint remains PENDING INSTRUCTOR DETERMINATION, so complete compliance is not implied. |
| Data Integrity and Traceability | QUALIFIED | `evidence-ledger.md`, primary filings, `docs/independent-source-check.md`, and normalization records provide traceability. WACC inputs, diluted shares, pension, Financing fair value, and management-FCF reconciliation remain qualified. |
| Financial Soundness and Judgment | QUALIFIED | Linked statements, DCF, bridge, scenarios, reverse DCF, peer qualifications, and final judgment are documented. The $4.78bn FCF proxy gap and terminal-value dependence remain material limitations. |
| Technical Execution and Usability | PASS | `README.md`, `ENVIRONMENT.md`, app server, static visible output, bounded controls, reset, and isolated-copy cold-run record support reproducibility. |
| Validation, Sensitivity and Reproducibility | QUALIFIED | 30 tests, deliberate failure/recovery, Week 3 published benchmark, locked changed-input record, and cold run are documented. Separate Edition A checkpoint status remains pending instructor determination. |
| Professional Communication | QUALIFIED | Eight-slide deck, Research Evolution, validation record, PDFs, and this audit are synchronized. Recordings, transcripts, manifest, and Brightspace package remain deferred until the submission stage. |
