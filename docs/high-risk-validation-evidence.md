# High-risk validation evidence

**Date:** October 14, 2026. **Scope:** read-only diagnostics and tests against
the approved IBM model; no production valuation input, formula, or decision was
changed.

## Independent-output matrix

| Highest-risk claim | Independent expectation / source | Independent result | Production result | Tolerance / result | Decision implication if failed |
|---|---|---:|---:|---|---|
| September 1 residual timing | 121/184 of H2 FCFF after Sep. 1 | 121/184; residual FCFF independently recalculated | 121/184 | Exact fraction; PASS | DCF would include already-realized cash flow. |
| DCF / terminal reinvestment / bridge | Separate arithmetic in `scripts/high_risk_diagnostics.py` | EV $220,096.1069m; equity $173,665.4251m; $182.287630/share | Same | < $0.000001m bridge and < $0.000000001/share; PASS | Base valuation would not be independently supported. |
| H1 management FCF definition | Q2 10-Q: CFO − Financing adjustment − net capital investment | $7,766 − $2,264 − $743 = $4,759m | Historical reconciliation reports $4,760m rounded | $1m reporting rounding; PASS | Financing cash flows could be double counted. |
| H2/FY period boundary | H1 actual plus H2-only model proxy | H2 $6,158.2326m; FY $10,918.2326m | Same model arithmetic | < $0.000001m; PASS | H1 actual might be forecast twice. |
| Published conventional DCF | Week 3 published inputs and answers | all 12 outputs match; 10% $27.4974, 11% $23.4140 | benchmark test | stated course tolerance; PASS | Basic DCF arithmetic would need repair. |
| Supplemental prospective test | Student’s precommitted Consulting −1pp prediction | $182.287630 → $179.793423; Watch / Defer unchanged | API/model result | directions and arithmetic match; PASS | Decision-driver response would be less credible. |

The Week 3 test validates conventional end-of-year DCF arithmetic only; it is
not an end-to-end validation of IBM’s 121/184 stub, Financing sidecar, or
ROIC-based terminal reinvestment.

## Added nonredundant automated tests

`tests/test_high_risk_validation.py` adds five tests (35 total project tests):

1. Recomputes WACC, residual cash-flow timing, terminal reinvestment, operating
   EV, and equity bridge without calling production DCF/WACC functions.
2. Tests the source-defined H1 management-FCF arithmetic, H2 model proxy, and
   FY $10.918bn bridge separately to prevent period/definition mixing.
3. Injects an invalid terminal case (terminal ROIC equal to terminal growth);
   expected failure: `Terminal incremental ROIC must exceed terminal growth`.
4. Injects a $10.001bn operating-cash reserve outside the documented $5–10bn
   bridge range; expected failure: `Operating cash reserve outside documented
   5–10bn bound`.
5. Applies a material −3pp Consulting-growth shock and confirms articulated
   statements plus lower FCFF/value; this is a robustness test, not a forecast.

Both newly targeted failure injections occurred only in in-memory analysis; no
production inputs were persisted. Existing tests retain the $1m FY2027
balance-sheet failure/recovery and SBC/Financing controls.

## Current isolated-copy cold run

An isolated local clone was created from `c6cce9edcfd3aac8ec940269aac945930bfbb86e`
and the reviewed staged patch was applied; this was a clean working-copy method
before the final documentation commit, not a claim that the later commit had
already existed. In `/private/tmp/ibm-high-risk-cold-20261014/repo`, macOS
`python3` (standard library only) ran:

```sh
python3 -m unittest discover -s tests -v
python3 model/ibm_phase3_model.py --write-output --demo-failure
python3 app/server.py --write-static
python3 app/server.py --port 8785
```

The test suite returned **35 passed, 0 failed**. API-only requests returned
$182.287630/share and articulation `PASS`; the bounded +2pp Software override
returned $190.647402/share and `PASS`; an empty override reset returned exactly
$182.287630/share and `PASS`. A +4pp Software request produced HTTP 400 with
`Growth shift outside ±3% control bound`. The model’s existing deliberate $1m
FY2027 balance-sheet failure was detected, and the subsequent normal API
requests/tests passed. `output/visible-base-output.html` was regenerated,
exists (5,970 bytes), and contains the $182.29 base label for standalone
opening. This was not a graphical browser or Mac-launcher test.
