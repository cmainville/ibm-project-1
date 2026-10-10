# AI-output disposition

**Status: CORRECTED.** The earlier AI-produced valuation applied a 122/184 stub convention and a June 30 bridge to a September 1 after-close DCF. It was wrong because cash available after September 1 begins September 2, and the dividend payable September 10 was already a known financing claim.

Independent evidence: calendar arithmetic (2026-07-01 to 2027-01-01 = 184 days; 2026-07-01 to 2026-09-02 = 63 days), IBM dividend #446 ($1.69 record date August 10, payable September 10), and IBM June 30 2026 Form 10-Q balance sheet.

Exact repair: residual FCFF is H2 operating FCFF × 121/184; the bridge rolls June cash and corporate debt through 63/184 of modeled H2 activity; the dividend payable is deducted once. The former 122/184 residual is retained only as a superseded comparison. Tests `test_dates_and_correct_stub_convention` and `test_sep1_bridge_rollforward_and_dividend_once` prevent recurrence.

