# Final submission readiness — IBM Project 1

**Audit date:** October 15, 2026

**Submission snapshot identifier:** `project1-submission-v2` (closeout snapshot tag; commit SHA is recorded in Git at closeout).
**Decision:** Watch / Defer IBM common stock; September 1, 2026 after-close
valuation date; $145.13 / $182.29 / $224.28 low/base/high; $231.40 reference
price.

This is an evidence-location and submission-readiness audit, not a claim that
Brightspace delivery or the Edition A checkpoint has been completed. All three
recordings have been made within their duration limits, uploaded to YouTube,
and transcribed from the supplied nine-page transcript PDF. The seven parts and
12-row manifest are distinct requirements.

## Seven-part architecture

| Part | Status | Evidence / verification | Remaining action |
|---|---|---|---|
| 1. Edition A | **PENDING_INSTRUCTOR_DETERMINATION** | `docs/Research-Evolution.*`; `docs/edition-a-checkpoint-status.md` | The student's original Edition A was completed and preserved in the September 1 Lab 03 submission, but the separate designated checkpoint has no recorded receipt. Professor Zhang acknowledged the preservation without explicitly granting equivalence. |
| 2. Research Evolution / Edition B | **QUALIFIED** | `docs/Research-Evolution.md`, `.html`, `.pdf` | Preserve unchanged Edition A; final PDF/source consistency is checked below. |
| 3. Repository and executed output | **LINK_ACCESS_CONFIRMED_BY_STUDENT** | `README.md`, `ENVIRONMENT.md`, `model/`, `app/`, `output/visible-base-output.html`, `docs/cold-run-log.md` | GitHub links work per student confirmation. Logged-out instructional-team access is not separately confirmed. |
| 4. Video 1 | **FINAL; LINK_ACCESS_CONFIRMED_BY_STUDENT** | `docs/transcript-video-1.txt`; `docs/video-evidence-index-plan.md` | Duration 2:58.91 (within 3:00). Transcript proofread; logged-out playback and YouTube-caption correction are not separately confirmed. |
| 5. Video 2 | **FINAL; LINK_ACCESS_CONFIRMED_BY_STUDENT** | `docs/transcript-video-2.txt`; `docs/video-evidence-index-plan.md` | Duration approximately 4:32 (within 5:00). Transcript proofread; logged-out playback and YouTube-caption correction are not separately confirmed. |
| 6. Decision Deck | **VERIFIED** locally | `docs/Decision-Deck.html`, `docs/Decision-Deck.pdf` (8 pages) | Attach `Decision-Deck.pdf`; final artifact/access check still required. |
| 7. Video 3 | **FINAL; LINK_ACCESS_CONFIRMED_BY_STUDENT; VIDEO_3_179_79_CONFIRMED** | `docs/transcript-video-3.txt`; `docs/video-evidence-index-plan.md` | Duration approximately 4:58.8 (within 5:00). Transcript proofread; $179.79 is student-confirmed. Logged-out playback and YouTube-caption correction are not separately confirmed. |

## Requirements-to-evidence matrix

### Project 1 finance system

| Exact requirement | Evidence location / grader verification | Status | Outstanding work / timing |
|---|---|---|---|
| Identify user, horizon, target/security, date, currency, shares and exclusions | `README.md`; `docs/Decision-Deck.pdf` slides 1/5; `docs/validation-and-ai-use.md` §1 | **VERIFIED** | None before recording. |
| Trace historical inputs; distinguish facts, normalizations, forecasts and outputs | `evidence-ledger.md`; `docs/load-bearing-input-verification.md`; `docs/base-year-normalization.md` | **QUALIFIED** | Beta, issuer debt yield, dilution and bridge qualifications remain disclosed; not missing artifacts. |
| Five-year linked statements; personalized drivers; loud articulation | `model/ibm_phase3_model.py`; `tests/test_phase3_model.py`; `output/phase3-model-output.json` | **VERIFIED** | None. |
| Five-year FCFF DCF, WACC, terminal convention and equity bridge | `model/valuation.py`; `scripts/high_risk_diagnostics.py`; `docs/validation-and-ai-use.*` | **VERIFIED** | No production change without student approval. |
| Low/base/high, WACC-growth sensitivity, terminal share, reverse DCF | `docs/Decision-Deck.pdf` slide 7; `model/valuation.py`; validation record | **VERIFIED** | None. |
| Comparable-company policy and consistent EV/equity multiple | `model/valuation.py`; `docs/stage2-investment-review.md`; deck slide 6 | **QUALIFIED** | Peer comparability is intentionally qualified. |
| Explain method disagreement rather than average | `docs/stage2-investment-review.md`; deck slide 6 | **VERIFIED** | None. |
| OAT sensitivity, causal links, range dependence, challenge record and partner challenge | `docs/assumption-challenge-record.md`; `docs/investment-judgment-and-reversal-triggers.md`; deck slide 7 | **VERIFIED** | Lab 12 absence remains correctly disclosed. |
| Valuation range and conditional action | `README.md`; deck slide 1; `docs/investment-judgment-and-reversal-triggers.md` | **VERIFIED** | Watch / Defer remains student-owned. |
| Usable semi-adjustable product with bounds, reset, visible checks | `app/`; `README.md`; `docs/cold-run-log.md`; tests | **VERIFIED** | Demonstrate visually in Video 3. |

### Required validation and source evidence

| Exact requirement | Evidence location / grader verification | Status | Outstanding work / timing |
|---|---|---|---|
| Published synthetic/known-answer reconciliation | `docs/week3-known-answer-reconciliation.md`; `tests/test_week3_dcf_benchmark.py` | **VERIFIED** | Conventional DCF scope is explicitly limited. |
| Independent source/definition check | `docs/independent-source-check.md`; `docs/fy2026-fcf-source-reconciliation.md` | **VERIFIED** | FY2026 management H2 component bridge remains an analytical qualification. |
| Directional changed-input prediction before execution | `docs/supplemental-locked-test-before.txt`, commit `c5a999f` | **VERIFIED** | None. |
| Complete Locked Changed-Input Record | `docs/supplemental-locked-test-after.txt`; complete historical appendix in Validation PDF | **VERIFIED** | Preserve both historical and supplemental records. |
| Articulation, DCF boundary/monotonicity and bridge checks | `tests/test_phase3_model.py`; `tests/test_valuation.py`; `tests/test_high_risk_validation.py` | **VERIFIED** | Current suite: 35 passing. |
| Peer-policy/multiple-definition consistency | `test_peer_and_implied_value_reconciliations`; deck slide 6 | **VERIFIED** | None. |
| Highest-risk failure test and cold run | `docs/high-risk-validation-evidence.md`; `docs/cold-run-log.md` | **VERIFIED** | Cold run was API/static-file, not graphical browser. |
| AI output with independent disposition | `docs/validation-and-ai-use.*` §§5–6 | **VERIFIED** | Video 1 must explain one example orally. |

### Shared architecture, checklist, and Brightspace evidence

| Exact requirement | Evidence location / grader verification | Status | Outstanding work / timing |
|---|---|---|---|
| Unchanged Edition A and Edition B/A-to-B table in Research Evolution PDF | `docs/Research-Evolution.pdf`, source `.md`/`.html` | **PENDING_INSTRUCTOR_DETERMINATION** | Content exists; separate checkpoint receipt is still absent. |
| Repository accessible to instructional team; source, environment, README, map, output | `README.md`; `ENVIRONMENT.md`; manifest row 2 | **PENDING_STUDENT_ACTION** | Confirm access in a logged-out/private-grader test before submission. |
| `.env.example` when credentials are needed | `README.md` says no packages/account/internet needed after download | **VERIFIED** | No credentials are used; `.env.example` is not applicable. |
| Visible executed output shows inputs, as-of date and result without code | `output/visible-base-output.html`; manifest row 3 | **VERIFIED** | Student must open GitHub file/link before submission. |
| Research Evolution PDF attachment | `docs/Research-Evolution.pdf`; manifest row 1 | **PENDING_STUDENT_ACTION** | Attach exact content-equivalent file at final submission. |
| Decision deck ≤8 slides | `docs/Decision-Deck.pdf` (8 pages); manifest row 4 | **PENDING_STUDENT_ACTION** | Attach final PDF. |
| Validation PDF includes sources, tests, limits, named AI uses and complete locked record | `docs/validation-and-ai-use.pdf`; manifest row 5 | **PENDING_STUDENT_ACTION** | Upload as `Validation-and-AI-Use.pdf` while retaining lower-case repository source. |
| Stable video URLs, titles, actual durations, timestamp indexes, access confirmation | manifest rows 6–11; `docs/video-evidence-index-plan.md` | **LINK_ACCESS_CONFIRMED_BY_STUDENT** | URLs work per student confirmation; durations and source-supported timestamp indexes are recorded. Logged-out access and YouTube-caption correction are not separately confirmed. |
| Corrected transcript text files in repo and Brightspace | `docs/transcript-video-1.txt`, `docs/transcript-video-2.txt`, `docs/transcript-video-3.txt`; manifest rows 7/9/11 | **TRANSCRIPT_REVIEWED_AND_CORRECTED** | All three source-PDF transcripts were proofread, including the student-confirmed Video 3 $179.79 result; attach the text files in Brightspace at final submission. |
| Final manifest and Brightspace receipt | `project-submission-manifest.csv`; validator | **PENDING_STUDENT_ACTION** | Complete final-mode fields and save submission receipt. |
| No credentials/private personal data | `.gitignore`, repository scan, no `.env` dependency | **QUALIFIED** | Run a final manual GitHub scan immediately before submission. |

### Six-category Brightspace rubric evidence (300 points)

| Criterion / points | Evidence readiness | Status | Remaining limitation or action |
|---|---|---|---|
| Problem Definition and Decision Usefulness — 45 | Decision/user/range/triggers in README, deck, Research Evolution and judgment record | **QUALIFIED** | Edition A checkpoint is pending instructor determination. |
| Data Integrity and Traceability — 45 | Ledger, load-bearing audit, source checks and FCF reconciliation | **QUALIFIED** | Beta/debt-yield, dilution, pension/Financing and H2 FCF bridge remain explicitly qualified. |
| Financial Soundness and Judgment — 60 | Linked model, independent DCF bridge, scenarios, reverse DCF, triggers | **QUALIFIED** | $4.782bn management-FCF gap weakens confidence but supports Watch / Defer. |
| Technical Execution and Usability — 45 | Local workbench, reset/bounds/failure, README, output, cold-run evidence | **VERIFIED** | Video 2/3 must show this evidence. |
| Validation, Sensitivity and Reproducibility — 75 | 35 tests, known answer, locked prospective test, failure injections, cold run, AI checks | **VERIFIED** | Final recordings/transcripts/timestamp indexes remain required submission evidence. |
| Professional Communication — 30 | Eight-slide deck, research evolution, validation record, final videos, corrected transcripts, and manifest | **QUALIFIED** | Complete final Brightspace attachments; logged-out playback and YouTube-caption correction remain unconfirmed. |

## Final pre-submission access and integrity checklist

| Check | Status now | Required personal verification |
|---|---|---|
| Repository visibility and instructional-team access | **LINK_ACCESS_CONFIRMED_BY_STUDENT** | GitHub links work per student confirmation. Open each manifest GitHub URL while logged out or with a permitted grader account if that separate check is required. |
| Stable video URLs and Unlisted/Public status | **LINK_ACCESS_CONFIRMED_BY_STUDENT** | YouTube watch URLs work per student confirmation; never set videos Private. Logged-out verification is not separately confirmed. |
| Duration, webcam, audio and screen readability | **RECORDED_WITHIN_LIMITS** | V1 2:58.91 (≤3:00); V2 approximately 4:32 (≤5:00); V3 approximately 4:58.8 (≤5:00). Confirm audio/screen readability personally. |
| Captions and transcript correction | **TRANSCRIPT_REVIEWED_AND_CORRECTED; VIDEO_3_179_79_CONFIRMED** | Corrected transcripts are in the repo and Video 3's 0:45 spoken value is student-confirmed as $179.79. No YouTube-caption review or correction is claimed. |
| Manifest timestamp indexes | **PREPARED_FROM_SOURCE_TRANSCRIPT** | Source-supported timestamps are now in the manifest; visual moments still need student confirmation against the uploaded videos. |
| PDFs attached and equivalent to repository | **PENDING_STUDENT_ACTION** | Attach Research-Evolution.pdf, Decision-Deck.pdf and Validation-and-AI-Use.pdf; compare against repo. |
| Final freeze / no private data / no contradictions | **CLOSEOUT_FREEZE_PREPARED** | Run `python3 tests/audit_submission_package.py --pre-submit`; it must continue to block on any undocumented manual confirmation. |
| Brightspace submission receipt | **PENDING_STUDENT_ACTION** | Save receipt after manual submission; do not submit automatically. |

## Naming and consistency decisions

- Repository paths are case-sensitive and remain `docs/Research-Evolution.pdf`,
  `docs/Decision-Deck.pdf`, and `docs/validation-and-ai-use.pdf`.
- Brightspace attachment names should be `Research-Evolution.pdf`,
  `Decision-Deck.pdf`, and **`Validation-and-AI-Use.pdf`**. The latter is a
  submission filename for a content-equivalent copy; no risky repository rename
  is needed.
- Current outputs consistently show September 1, 2026 after close; $231.40;
  $145.13/$182.29/$224.28; 7.07% WACC; 2.5% terminal growth; Watch / Defer;
  the approximately $4.782bn FCF gap; and 35 current tests. Historical
  $181.95/$190.31 and 24/28/30 test counts are retained only where labeled
  historical or stage-specific.

## Readiness decisions

**Ready to record: COMPLETED.** The finance system, evidence, deck, and current
validation record were used for three recordings within their duration limits.
The supplied transcript PDF was split into three corrected text files; the
source-supported timestamps are recorded in the manifest.

**Ready to submit: DOCUMENTATION COMPLETE; BRIGHTSPACE ACTION REMAINS.** All
three recordings are final; their links work per student confirmation, and their
transcripts are proofread. Brightspace attachments/receipt and the instructor's
Edition A determination remain. Logged-out repository/video access and
YouTube-caption correction are not separately confirmed and must not be claimed.
The student's original Edition A was completed and preserved in the September 1
Lab 03 submission, but the separate designated checkpoint has no recorded
receipt. Professor Zhang acknowledged the preservation without explicitly
granting equivalence; that issue remains disclosed.

**Historical validator marker:** `PENDING_RECORDING` appears only as a legacy
literal required by `audit_submission_package.py --pre-recording`; it does not
describe the current recording status. All three recordings are complete.
