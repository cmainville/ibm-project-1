# Week 3 published known-answer reconciliation

**Status:** Completed October 14, 2026. This is a standalone benchmark of conventional DCF arithmetic; it does not replace or alter the specialized IBM production DCF.

## Sources and course conventions

- [FIN 43900 Week 3 Lab 05: DCF Build](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md), including the published answer table and WACC check.
- [FIN 43900 Week 3 worked DCF example](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/teach-dcf-worked-example.md), explaining the annual discounting, Gordon-growth terminal value, and enterprise-to-equity bridge.
- [Project 1 corporate-finance application requirement](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-1-corporate-finance-application.md).

The published case uses USD millions: starting FCFF $100; Year 1-5 growth of 8%, 6%, 5%, 4%, and 3%; WACC 10%; terminal growth 3%; non-operating cash $50; debt $300; and 50 diluted shares. The implementation forecasts annual end-of-year FCFF, applies the Gordon-growth terminal value at the end of Year 5, discounts that terminal value exactly five years, calculates EV as the explicit-FCFF PV plus terminal PV, then bridges to equity and per-share value.

## Reproducible implementation and results

`model/week3_dcf_benchmark.py` calculates the case from those inputs. It is deliberately separate from `model/valuation.py`: IBM uses a September 1 residual-FCFF stub, timing-specific bridge, and ROIC-based terminal convention rather than this classroom case's annual Gordon-growth convention.

| Output (USD m except per share and fraction) | Published answer | Independently calculated | Difference | Result |
|---|---:|---:|---:|---|
| FCFF Year 1 | 108.0000 | 108.0000000 | 0.0000000 | PASS |
| FCFF Year 2 | 114.4800 | 114.4800000 | 0.0000000 | PASS |
| FCFF Year 3 | 120.2040 | 120.2040000 | 0.0000000 | PASS |
| FCFF Year 4 | 125.0122 | 125.0121600 | -0.0000400 | PASS |
| FCFF Year 5 | 128.7625 | 128.7625248 | +0.0000248 | PASS |
| PV of explicit FCFF | 448.4408 | 448.4408174 | +0.0000174 | PASS |
| Terminal value | 1,894.6486 | 1,894.6485792 | -0.0000208 | PASS |
| PV of terminal value | 1,176.4277 | 1,176.4277025 | +0.0000025 | PASS |
| Enterprise value | 1,624.8685 | 1,624.8685199 | +0.0000199 | PASS |
| Equity value | 1,374.8685 | 1,374.8685199 | +0.0000199 | PASS |
| Value/share | 27.4974 | 27.4973704 | -0.0000296 | PASS |
| Terminal PV / EV | 0.7240 | 0.7240141 | +0.0000141 | PASS |

Money and per-share comparisons use an absolute tolerance of $0.01 million or $0.01 per share, respectively, consistent with the lab's “within a cent” instruction. The terminal-PV/EV fraction is reported to four decimals and uses a ±0.00005 tolerance. The small differences above are normal unrounded-calculation versus published-four-decimal rounding differences. No discrepancy remains.

## WACC sensitivity and reset

Holding all other published inputs constant, increasing WACC from 10% to 11% produces **$23.4140327/share** (about **$23.41/share**), below the 10% baseline of $27.4973704/share. Re-running the unchanged 10% input returns $27.4973704/share. The test records both the expected inverse WACC/value direction and baseline restoration.

## Execution record

Executed October 14, 2026, in the repository's standard-library-only Python 3 environment:

```sh
python3 model/week3_dcf_benchmark.py
python3 -m unittest discover -s tests -v
```

The two new benchmark tests passed. The combined suite passed **30 tests, 0 failures**.

## Scope of the check

This validates core DCF mechanics: FCFF compounding, annual end-of-year discounting, Gordon-growth terminal value, terminal-value discounting, EV-to-equity bridge, diluted-share division, and the direction of a WACC sensitivity.

It does **not** independently validate IBM-specific mechanics such as H1/H2 forecast construction, the September 1 121/184 residual-FCFF convention, timing-specific cash/debt roll-forward, IBM Financing separation, ROIC-based terminal reinvestment, pension conventions, share-count uncertainty, or IBM forecast assumptions. Those remain covered by the separate IBM model tests and source-validation records.
