# Published Week 3 known-answer status

**Status: completed October 14, 2026.**

The published FIN 43900 Week 3 DCF training case and its official answer table were located in the course repository:

- [Lab 05: DCF Build](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/lab-05-dcf-build.md)
- [Worked DCF example](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-03/teach-dcf-worked-example.md)

`model/week3_dcf_benchmark.py` implements the published inputs and conventional annual DCF conventions from calculation inputs, rather than copying the answer values. Its two tests passed along with the IBM suite: **30 passed, 0 failed**. All 12 published outputs reconciled within the documented tolerances, and the required 10%-to-11% WACC check decreased value to $23.4140/share before the 10% baseline was restored.

The detailed comparison, commands, tolerances, scope, and limitations are in `docs/week3-known-answer-reconciliation.md`.

This resolves the published Week 3 known-answer requirement. It is a standalone conventional-DCF benchmark, not an assertion that the IBM production model has the same timing or terminal conventions. The IBM-specific validation remains separately documented in `docs/validation-and-ai-use.md`.
