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
| Independent source/definition check | PASS | `docs/independent-source-check.md`, validation record | Management-FCF proxy gap remains unresolved. |
| Historical Locked Changed-Input Record | PASS | locked text, screenshots, Validation Appendix A | Historical pre-SBC result is correctly separated from current model. |
| Full AI-use disclosure | PASS | `docs/validation-and-ai-use.*` | Student remains responsible for final presentation claims. |
| Partner challenge from earlier labs | CORRECTED | `docs/assumption-challenge-record.md` | Partner name/date/notes unavailable; Lab 12 absence is disclosed. |
| Current-model cold run and reproducible setup | PASS | `docs/cold-run-log.md`, `README.md`, `ENVIRONMENT.md` | API-only browser validation if no visible browser is recorded. |
| Saved visible executed output | PASS | `output/visible-base-output.html` | Static output is read-only, not interactive. |
| Research Evolution | PASS | `docs/Research-Evolution.*` | Edition A remains unchanged; checkpoint receipt absent locally. |
| Eight-slide decision deck | PASS | `docs/Decision-Deck.*` | None identified. |
| HTML/PDF/Markdown/model consistency | PASS | PDF checks and current audit | Future edits require re-export. |
| Videos, transcripts, manifest, Brightspace submission | DEFERRED UNTIL RECORDING / SUBMISSION STAGE | Submission architecture | Student action required after recordings; do not create now. |

## Final audit limitations

- FY2026 company-style FCF proxy remains approximately $4.78bn below the management-outlook reference; it was not forced to guidance.
- Future dilution, point-in-time diluted shares, IBM-specific borrowing cost, pension treatment, and Financing fair value remain qualified.
- The actual partner exchange is a student-reported retrospective recollection; the partner identity, date, and original notes are unavailable. No Lab 12 peer-review evidence exists because the student was absent.
