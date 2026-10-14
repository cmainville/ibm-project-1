# Final submission readiness — IBM Project 1

**Audit date:** October 14, 2026

**Current review commit:** `38c2f9fef188b0b5d36aac6b2d14d8902e47531a` (not a final frozen-submission commit)
**Decision:** Watch / Defer IBM common stock; September 1, 2026 after-close
valuation date; $145.13 / $182.29 / $224.28 low/base/high; $231.40 reference
price.

This is an evidence-location and submission-readiness audit, not a claim that
recordings, Brightspace delivery, or the Edition A checkpoint have been
completed. The seven parts and 12-row manifest are distinct requirements.

## Seven-part architecture

| Part | Status | Evidence / verification | Remaining action |
|---|---|---|---|
| 1. Edition A | **PENDING_INSTRUCTOR_DETERMINATION** | `docs/Research-Evolution.*`; `docs/edition-a-checkpoint-status.md` | Lab 03 attempt contains Edition A, but the separate checkpoint has no recorded receipt. Await Professor Zhang’s ruling. |
| 2. Research Evolution / Edition B | **QUALIFIED** | `docs/Research-Evolution.md`, `.html`, `.pdf` | Preserve unchanged Edition A; final PDF/source consistency is checked below. |
| 3. Repository and executed output | **VERIFIED** locally | `README.md`, `ENVIRONMENT.md`, `model/`, `app/`, `output/visible-base-output.html`, `docs/cold-run-log.md` | Student must verify instructional-team GitHub access while logged out before submission. |
| 4. Video 1 | **PENDING_RECORDING** | `docs/video-evidence-index-plan.md` | Record ≤3:00, correct captions, upload/link, transcript, timestamp index, logged-out access check. |
| 5. Video 2 | **PENDING_RECORDING** | `docs/video-evidence-index-plan.md` | Record ≤5:00 with actual repository and high-risk validation/failure evidence. |
| 6. Decision Deck | **VERIFIED** locally | `docs/Decision-Deck.html`, `docs/Decision-Deck.pdf` (8 pages) | Attach `Decision-Deck.pdf`; final artifact/access check still required. |
| 7. Video 3 | **PENDING_RECORDING** | `docs/video-evidence-index-plan.md` | Record ≤5:00; open with live product demonstration, not an API-only demonstration. |

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
| Stable video URLs, titles, actual durations, timestamp indexes, access confirmation | manifest rows 6–11; `docs/video-evidence-index-plan.md` | **PENDING_RECORDING** | Record, upload Unlisted/Public, correct captions, fill actual fields and test logged out. |
| Corrected transcript text files in repo and Brightspace | planned paths in video plan; manifest rows 7/9/11 | **PENDING_RECORDING** | Do not create before recordings; correct and attach after recording. |
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
| Professional Communication — 30 | Eight-slide deck, research evolution, validation record, manifest plan | **PENDING_RECORDING** | Record clear, bounded videos; correct captions and transcripts. |

## Final pre-submission access and integrity checklist

| Check | Status now | Required personal verification |
|---|---|---|
| Repository visibility and instructional-team access | **PENDING_STUDENT_ACTION** | Open each manifest GitHub URL while logged out or with a permitted grader account. |
| Stable video URLs and Unlisted/Public status | **PENDING_RECORDING** | Never set videos Private; verify each link logged out. |
| Duration, webcam, audio and screen readability | **PENDING_RECORDING** | Confirm actual duration: V1 ≤3:00, V2/V3 ≤5:00; webcam unless accommodation. |
| Captions and transcript correction | **PENDING_RECORDING** | Correct IBM, FCFF, WACC, values, names, and speaker attribution; add repo/Brightspace text files. |
| Manifest timestamp indexes | **PENDING_RECORDING** | Replace planned segments with actual timestamps after uploads. |
| PDFs attached and equivalent to repository | **PENDING_STUDENT_ACTION** | Attach Research-Evolution.pdf, Decision-Deck.pdf and Validation-and-AI-Use.pdf; compare against repo. |
| Final freeze / no private data / no contradictions | **PENDING_STUDENT_ACTION** | Run `python3 tests/audit_submission_package.py --final`, inspect `git status`, and make final commit. |
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

**Ready to record: YES, with a recording plan.** The finance system, evidence,
deck, current validation record and planned timestamps are available. The
student must use the planned evidence moments and preserve the live-product
opening for Video 3.

**Ready to submit: NO.** Required videos, corrected transcripts, stable URLs,
actual durations/timestamps, logged-out access checks, final frozen commit,
Brightspace attachments/receipt, and the instructor’s Edition A determination
are not yet complete.
