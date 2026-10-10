# Pension and other-claim bridge convention

**Selected provisional convention: $0 separate pension debt-like claim.** This is a convention, not a conclusion that IBM has no pension economics.

IBM’s FY2025 annual report (retirement-benefits note; reporting period December 31, 2025; filed February 24, 2026) says its qualified defined-benefit plans were well funded and reports an overall net underfunded position of $2,283m. The June 2026 Form 10-Q (reporting period June 30, 2026; filed July 2026) reports $7,645m prepaid pension assets and $8,603m retirement obligations on the consolidated balance sheet. The $8,603m line must not be subtracted in full: it is not a net defined-benefit deficit, and mechanically deducting it while retaining prepaid assets would overstate net debt. Nonpension postretirement and current-benefit detail requires the complete filing-note reconciliation before a separate claim is supportable.

The operating model includes continuing retirement expense in consolidated operating results and has no independent pension cash-funding schedule. Therefore the bridge contains one explicit `pension_debt_like_claim = 0` and no offsetting pension asset. This avoids double counting a gross liability/asset combination. This conclusion must be revisited if the annual-report plan-group funded-status table, current benefit-liability detail, or a forward cash-contribution schedule supports a net debt-like shortfall not captured in FCFF. `test_sep1_bridge_rollforward_and_dividend_once` verifies it appears once in the bridge.

