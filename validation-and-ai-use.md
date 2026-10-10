# Validation and AI-use record

**Prepared:** October 9, 2026, America/Chicago. **Cutoff:** September 1, 2026 after close. This record describes actual local runs, not classroom reference-answer validation.

## Reproducible results

Command: `python3 -m unittest discover -s tests -v`  
Result: **24 passed, 0 failed**. The suite covers FY2026 H1 actual + H2 forecast construction; annual balance-sheet articulation; cash-flow-to-cash reconciliation; Financing exclusion from operating FCFF; the 121/184 after-close stub; the bridge and dividend payable; WACC/terminal-growth monotonicity; terminal reinvestment constraints; peer-multiple arithmetic; scenario ordering; and validation bounds.

Command: `python3 model/ibm_phase3_model.py --write-output --demo-failure`  
Result: regenerated `output/phase3-model-output.json`; a synthetic $1m FY2027 cash break produced the expected balance-sheet failure and did not modify saved inputs. The subsequent normal run remained articulated.

Command: `python3 app/server.py --write-static`  
Result: regenerated `output/visible-base-output.html`. A recorded fresh-copy run in `docs/cold-run-log.md` returned HTTP 200 from the local API and the same $181.950342 base value.

## Source and accounting checks

The Q2 2026 IBM 10-Q reconciles the June 30 balance sheet and H1 statement/cash-flow anchors used by the model. The independent definition check in `docs/independent-source-check.md` confirms the $1.69 common dividend, August 10 record date and September 10 payment date. It was declared before the valuation date, unpaid on September 1, and therefore appears once as a bridge payable; no July 1-September 1 cash payment is modeled. The exact declaration calendar date is not preserved in the local ledger and remains explicitly unresolved. The evidence ledger records URLs, publication dates, definitions and cutoff status.

No course reference answers were available, so no known-answer reconciliation is claimed. The test suite uses synthetic known-answer arithmetic only for the reversible $1m integrity-failure demonstration.

## Limits and failed-test evidence

The documented historic failure is the initial June-to-December roll that applied full-year 2026 flows and double-counted H1; `docs/phase3-validation-log.md` records the correction and retest. The deliberate highest-risk current failure is the $1m cash break, which fails loudly and restores because it runs on a copy. No current automated test failed.

Remaining evidence limitations: beta is a dated third-party indication with opaque methodology; debt cost is a single-A spread proxy rather than an IBM bond yield; June diluted weighted-average shares proxy for point-in-time dilution; the $7.5bn cash reserve and zero incremental pension claim are analyst conventions; the Financing sidecar uses June book equity with no fair-value adjustment; and no NCI earnings allocation forecast exists. These items constrain the recommendation to Watch / Defer.

## Material AI contributions

An OpenAI Codex agent assisted on October 9, 2026 with code inspection, test execution, data-consistency checks, repair of the P/E definition, documentation, and HTML/PDF formatting. The agent did not access a proprietary terminal, file a trade, submit work, obtain course answers, or independently verify sources beyond the preserved source ledger. Model/version metadata was not supplied in the project environment; no model version is claimed. The analyst remains responsible for source verification, inputs, judgment and submission.
