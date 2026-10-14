# Cold-run log

## October 14, 2026 validation record

### Student-observed screenshot evidence (supplied for this record)

- The project launched successfully from a fresh GitHub download on October 14, 2026. The launcher selected port 8768 because port 8765 was occupied.
- Baseline IBM intrinsic value: **$181.95/share**; September 1, 2026 market price: **$231.40/share**; WACC: **7.07%**; terminal-value share: **78.06%**.
- The +2 percentage-point software-growth experiment returned **$190.31/share**. Reset to Base restored **$181.95/share**.
- The deliberate failed check displayed: `SAFE FAILURE DEMONSTRATION: detected as intended — FY2027 balance-sheet check failed: $-1.0000m`.

These are the student's observed results recorded from screenshots, not results independently produced during the October 14 accessibility/documentation update. The independently rerun commands and their results are recorded below.

### Independent technical rerun during the October 14 accessibility/documentation update

- `python3 -m unittest discover -s tests -v` completed successfully: **24 tests passed**.
- `python3 model/ibm_phase3_model.py --write-output --demo-failure` regenerated the model output, retained the base model values, and printed the intended `$-1.0000m` FY2027 balance-sheet safe-failure demonstration.
- `python3 app/server.py --write-static` regenerated `output/visible-base-output.html`; it shows **$181.95/share** base value and no obsolete claim that the Locked Changed-Input Record was unexecuted.
- A localhost API smoke test on port 8768 returned the base **$181.95/share** value and `statement_articulation` `PASS`. Relative links in `output/visible-base-output.html` and `docs/Decision-Deck.html` resolved without missing local targets.

- Date/time: 2026-10-09 America/Chicago.
- Environment: macOS; Python 3.14 (reported executable: `python3`).
- Fresh directory: `/private/tmp/ibm-project-1-cold.VDcgPS`.
- Copied project files: `app/`, `docs/`, `model/`, `output/`, `tests/`, and `README.md`; no external package install or account was used.
- Commands run:
  - `python3 -m unittest discover -s tests -v`
  - `python3 model/ibm_phase3_model.py --write-output --demo-failure`
  - `python3 app/server.py --write-static`
  - `python3 app/server.py --port 8766`
  - `curl -sS http://127.0.0.1:8766/api/analysis`
- Results: 24 tests passed; model output and static HTML were generated; fresh-copy API returned HTTP 200 and the same $181.950342/share base value, 121/184 stub fraction, and statement-articulation PASS.
- Failure demonstration: deliberately reducing FY2027 cash by $1m produced the expected balance-sheet failure (`$-1.0000m`).
- First failure/resolution: none in the cold copy. Earlier in the source workbench, a stale server returned obsolete `cash_tax_rate`; it was identified as a pre-repair process, stopped, and the repaired server returned HTTP 200.
- No git commit/hash is claimed.

## October 14, 2026 final isolated-copy validation

- **Method:** isolated fresh Git clone from the current local `main` repository using `git clone --depth 1 --branch main file://...`; tested commit `ba70b9f58c04000979b211763330df17daae9218`. This was an API/server validation, not a visual browser or Mac-launcher demonstration.
- **Environment:** macOS; `python3` (standard library only); temporary clone at `/tmp/ibm-final-cold.NJfOHT/repo`.
- **Commands:** `python3 -m unittest discover -s tests -v`; `python3 model/ibm_phase3_model.py --write-output --demo-failure`; `python3 app/server.py --write-static`; `python3 app/server.py --port 8773`; GET `/api/analysis`; POST `/api/analysis` with `{"overrides":{"software_growth_shift":0.02}}`; POST with `{"overrides":{}}`.
- **Results:** all **30 tests passed, 0 failures**. The base API value was **$182.287630/share**, statement articulation was `PASS`, and the residual FY2026 fraction was **121/184** (`0.6576086957`). The +2pp backend Software-growth override returned **$190.647402/share**, above the new base; empty overrides restored **$182.287630/share**.
- **Failure and recovery:** the deliberate FY2027 $1m cash break was detected exactly as intended: `SAFE FAILURE DEMONSTRATION: detected as intended — FY2027 balance-sheet check failed: $-1.0000m`. The subsequent normal API requests and test suite passed, confirming recovery.
- **Static output:** `output/visible-base-output.html` was generated successfully in the isolated copy and is available without starting Python. It was not represented as interactive.
