# Project 1 Edition B — Inventory

Inventory completed: October 9, 2026. This document records what was found; it does not alter the source work.

## Existing work classified

| Category | Files | Treatment in Edition B |
|---|---|---|
| **Unchanged Edition A baseline** | `CadenMainville/Project 1 Edition A - IBM.md` | Preserve unchanged. It is a preliminary WATCH / DEFER research baseline with no valuation conclusion. |
| **Older September 9 FCFF DCF** | `IBM Report/IBM DCF/dcf.py`; `IBM Report/IBM DCF/ibm_inputs.md` | Preserve as prior work only. It uses September 9 prices/rates and contains labeled placeholders. Its $270.45 output is not a September 1 final valuation. |
| **Lab 10/11 five-year linked IBM FCFE model and sensitivities** | `lab10_proforma_IBM.py`; `lab10_proforma_IBM.md`; `lab11_sensitivity_IBM.py`; `lab11_sensitivity_IBM.md` | Preserve as useful model-learning evidence only. It is FCFE-based, uses an FY2025 opening balance sheet, and reports the obsolete $180.39 output. It is not the final FCFF valuation. |
| **September 9 peer analysis** | `lab08_ibm_comps.py`; `IBM Report/Lab_08_Deal_Evidence_and_Valuation_Triangulation_IBM.md` | Preserve as prior peer-policy work. Its price date and P/E figures are not September 1 inputs. |
| **Prior narrative/sources** | `IBM Report/Lab_4_Report_IBM - 09:03:2026 - Caden Mainville.md`; `IBM Report/IBM_Sources_09:03:2026_Report.md`; `IBM Report/ibm-20251231.html` | Historical reference only. The narrative’s INITIATE / BUY call is not adopted for Edition B. The local HTML is the FY2025 SEC filing copy. |
| **Unrelated ABG training case** | `proforma.py`; `lab09.md`; `lab07_comps.py`; `lab07_comparable_policy.md` | Do not use ABG operating, peer, or valuation inputs in IBM analysis. It may be used only for a known-answer test if the published training-case answer is confirmed to be the stated one. |

## Missing required materials

These materials are not present in the workspace. No contents have been invented.

| Missing item | Consequence / independent work still possible |
|---|---|
| Project 1 assignment | Need it to verify exact deliverable/rubric language and the Locked Changed-Input Record format. Evidence control and model scaffolding can still proceed. |
| Major-project checklist | Need it to verify checklist-specific items. |
| Submission architecture | Need it to verify final folder/URL/material architecture. |
| Annotated excerpt | Need it to follow any instructor-specific annotation requirements. |
| Templates | Need them before producing template-constrained deck, manifest, or video documents. |
| Local copy of IBM Q2 2026 Form 10-Q | The filing is publicly accessible on SEC EDGAR and used through its source URL; no local filing was created or altered. |
| Checkpoint receipt / partner-review record / verified AI-use history | No receipt, actual partner challenge, or complete historical AI log is available. These remain pending, rather than attributed or reconstructed. |

## Phase 1 checks completed

- Confirmed that the latest reported balance sheet available by the valuation date is June 30, 2026, not September 1, 2026.
- Replaced the old September 9 market prices with September 1 closing prices in the evidence ledger.
- Recorded the September 1 Treasury 10-year rate and the September 1 Damodaran ERP observation.
- Marked historical beta and an independently supportable marginal borrowing cost as unresolved because an as-of snapshot was not preserved.
- Preserved the distinction between reported facts, analyst normalizations, and unresolved inputs.

## Still open before a final valuation

1. Human approval of finance conventions and load-bearing drivers in `finance-architecture-decision-note.md`.
2. Source-supported amount and accounting treatment for the claimed FY2025 tax-audit benefit. It is mentioned in prior narrative, but this review has not found a primary-source amount/locator adequate to normalize earnings.
3. A defensible September 1 beta observation or a documented alternative beta convention, and a supportable cost-of-debt method.
4. A human-authored, timestamped Locked Changed-Input Record before its required AI-off execution.
