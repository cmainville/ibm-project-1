"""Standalone conventional DCF benchmark for FIN 43900 Week 3.

This module intentionally does not use the IBM valuation engine.  The course
case uses annual end-of-year discounting and a Gordon-growth terminal value,
whereas the IBM production model uses a September 1 residual-FCFF stub and
an ROIC-based terminal convention.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Week3DcfResult:
    fcff: tuple[float, ...]
    pv_explicit_fcff: float
    terminal_value: float
    pv_terminal_value: float
    enterprise_value: float
    equity_value: float
    value_per_share: float
    terminal_pv_to_ev: float


def calculate_week3_dcf(
    starting_fcff: float = 100.0,
    growth_rates: tuple[float, ...] = (0.08, 0.06, 0.05, 0.04, 0.03),
    wacc: float = 0.10,
    terminal_growth: float = 0.03,
    non_operating_cash: float = 50.0,
    debt: float = 300.0,
    diluted_shares: float = 50.0,
) -> Week3DcfResult:
    """Calculate the published training case from inputs, in USD millions."""
    if len(growth_rates) != 5:
        raise ValueError("The Week 3 training case requires five explicit years")
    if terminal_growth >= wacc:
        raise ValueError("Terminal growth must be less than WACC")
    if diluted_shares <= 0:
        raise ValueError("Diluted shares must be positive")

    fcff = []
    annual_fcff = starting_fcff
    for growth in growth_rates:
        annual_fcff *= 1 + growth
        fcff.append(annual_fcff)

    pv_explicit = sum(value / (1 + wacc) ** year for year, value in enumerate(fcff, start=1))
    terminal_value = fcff[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / (1 + wacc) ** len(fcff)
    enterprise_value = pv_explicit + pv_terminal
    equity_value = enterprise_value + non_operating_cash - debt

    return Week3DcfResult(
        fcff=tuple(fcff),
        pv_explicit_fcff=pv_explicit,
        terminal_value=terminal_value,
        pv_terminal_value=pv_terminal,
        enterprise_value=enterprise_value,
        equity_value=equity_value,
        value_per_share=equity_value / diluted_shares,
        terminal_pv_to_ev=pv_terminal / enterprise_value,
    )


if __name__ == "__main__":
    result = calculate_week3_dcf()
    for year, value in enumerate(result.fcff, start=1):
        print(f"FCFF Year {year}: {value:.4f}")
    print(f"PV of explicit FCFF: {result.pv_explicit_fcff:.4f}")
    print(f"Terminal value: {result.terminal_value:.4f}")
    print(f"PV of terminal value: {result.pv_terminal_value:.4f}")
    print(f"Enterprise value: {result.enterprise_value:.4f}")
    print(f"Equity value: {result.equity_value:.4f}")
    print(f"Value/share: {result.value_per_share:.4f}")
    print(f"Terminal PV / EV: {result.terminal_pv_to_ev:.4f}")
