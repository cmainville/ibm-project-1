# Cold-run log

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

