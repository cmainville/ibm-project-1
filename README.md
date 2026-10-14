# IBM Project 1 - Edition B

**Decision:** Watch / Defer IBM common stock. The September 1, 2026 after-close price was **$231.40**. The completed five-year operating DCF produces **$144.80 / $181.95 / $223.94** per diluted share in low/base/high causal cases. Base is below price and terminal value is 78.1% of operating EV. The workbench and deck therefore frame a monitoring decision, not an initiation.

## Start the interactive workbench

The interactive application requires **Python 3.10 or later**. It runs only on your computer and does not require packages, an account, or an internet connection after download.

### Mac (easiest)

In Finder, open the downloaded project folder and double-click `Launch IBM.command`. Keep the Terminal window open while using the workbench; it will open the local site and automatically chooses another port if 8765 is busy.

If macOS says the launcher is not executable, open Terminal in the project folder and run:

```sh
chmod +x "Launch IBM.command"
```

Then double-click it again. This only restores the file's normal executable permission; do not bypass macOS security protections. If macOS asks for confirmation because the file was downloaded, use its normal Open/Allow flow after reviewing the repository source.

### Any platform (manual fallback)

Open a terminal in this project folder and run:

```sh
python3 app/server.py --port 8765
```

Then open [http://127.0.0.1:8765/](http://127.0.0.1:8765/) in a browser. On Windows, if `python3` is unavailable, use the Python launcher instead:

```powershell
py -3 app/server.py --port 8765
```

If port 8765 is already occupied, choose another unused port, for example `python3 app/server.py --port 8768`, and open the matching URL: `http://127.0.0.1:8768/`.

The local workbench is interactive: browser controls send requests to Python, which calculates the statements, valuation, and checks. JavaScript only displays those results. Reset restores the documented base case. “Demonstrate failed check” mutates a temporary copy by $1m, reports the failure, and does not save a bad model.

### Offline, read-only review

For review without starting Python, open `output/visible-base-output.html` for the static base-case output or `docs/Decision-Deck.html` for the decision deck. These are read-only HTML artifacts: unlike the interactive Python-backed workbench, they do not provide controls or recompute the financial model.

### Reproduce the checks

From this directory:

```sh
python3 -m unittest discover -s tests -v
python3 model/ibm_phase3_model.py --write-output --demo-failure
python3 app/server.py --write-static
```

## Project map

- `model/ibm_phase3_model.py` - FY2026 H1 actual plus H2 forecast and FY2027-30 integrated statements.
- `model/valuation.py` - operating FCFF DCF, bridge, WACC, scenarios, reverse DCF, peers and one-at-a-time tests.
- `model/inputs.json` - reported anchors, analyst drivers, bounds, source posture and conventions.
- `app/` - localhost Python server and interactive workbench.
- `output/phase3-model-output.json` and `output/visible-base-output.html` - regenerated visible base outputs.
- `docs/Decision-Deck.html` and `docs/Decision-Deck.pdf` - eight-slide submission deck and matching PDF.
- `docs/validation-and-ai-use.*` - reproducible validation and AI-use record.
- `evidence-ledger.md`, `docs/assumption-challenge-record.md`, and `docs/phase4-5-review.md` - evidence, assumptions and methodology record.

## Key conventions

Currency and statements use USD millions; per-share values use USD. June 30 basic shares calculate market capitalization/WACC; H1 diluted weighted-average shares (952.7m) are the labeled diluted valuation proxy. FY2026 combines H1 actuals with H2 forecast, while the June-to-December cash/equity roll uses H2 only. After a September 1 close, future stub FCFF begins September 2 and equals 121/184 of H2 operating FCFF. IBM Financing is excluded from operating FCFF, then added once as its June 30 reported $1.45bn equity sidecar. Corporate debt, the known-but-unpaid $1.69 September 10 dividend and $89m NCI are bridge deductions. Pension receives no incremental deduction under the stated convention.

Reported facts, analyst forecasts and calculation outputs are deliberately separated. The DCF excludes unverified purchase synergies, future M&A cash outflows, a Financing fair-value premium/discount, issuer-specific debt pricing, and a separate pension debt claim. Comparable values are reference anchors, never mechanically averaged.

## Sources and limitations

Primary history is IBM’s [FY2025 10-K](https://www.sec.gov/Archives/edgar/data/51143/000005114326000010/ibm-20251231_d2.htm) and [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/51143/000005114326000078/ibm-20260630.htm). Cutoff-dated market, peer and dividend records sit in `evidence-ledger.md`. Do not use post-September 1 prices, results, guidance or consensus.

The 0.70 beta is a qualified third-party indication with opaque methodology; 5.47% pre-tax debt cost is a Treasury plus single-A OAS proxy, not an IBM bond yield. The cash reserve, normalized tax rate, terminal ROIC/growth and pension convention are analyst assumptions. The point-in-time diluted share count and Financing fair value remain unresolved. These limitations materially support Watch / Defer.
