#!/usr/bin/env python3
"""Independent, read-only diagnostics for the IBM Project 1 model.

This is deliberately not a second production valuation engine.  It uses the
connected-statement output as its input, then re-performs the dated DCF cash
flow timing, terminal reinvestment, and equity bridge arithmetic without
calling ``valuation.dcf_from_rows`` or ``valuation.wacc_build``.  It also
prints the period-correct management-FCF proxy reconciliation.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "model"))

from ibm_phase3_model import build_model, load_inputs, opening_row  # noqa: E402


VALUE_DATE = date(2026, 9, 1)


def _years(day: date) -> float:
    return (day - VALUE_DATE).days / 365.0


def independent_dcf(inputs=None, rows=None, *, wacc=None, growth=.025,
                    terminal_roic=.15, minimum_cash=None):
    """Recalculate DCF and bridge arithmetic outside the production module."""
    inputs = load_inputs() if inputs is None else inputs
    rows = build_model(inputs) if rows is None else rows
    market, draft = inputs["market"], inputs["draft_assumptions"]
    balance = draft["balance_sheet_and_financing"]
    opening = opening_row(inputs)
    h2 = rows[2026]["h2_2026_forecast"]

    # Recreate WACC from documented inputs, using corporate debt only.
    h2_days, pre_days, residual_days = 184, 63, 121
    estimated_cash = (
        opening["cash"]
        + h2["cfo_consolidated"] * pre_days / h2_days
        - h2["capex"] * pre_days / h2_days
        - h2["software_investment"] * pre_days / h2_days
        + h2["delta_corporate_debt"] * pre_days / h2_days
        + h2["delta_financing_debt"] * pre_days / h2_days
    )
    estimated_corporate_debt = opening["corporate_debt"] + h2["delta_corporate_debt"] * pre_days / h2_days
    market_equity = market["ibm_price_sep1"] * market["basic_shares_jun30"]
    debt_weight = estimated_corporate_debt / (market_equity + estimated_corporate_debt)
    equity_weight = 1 - debt_weight
    calculated_wacc = (
        equity_weight * (market["risk_free_rate_sep1"] + market["beta_sep1_third_party_indication"] * market["implied_erp_sep1"])
        + debt_weight * (market["risk_free_rate_sep1"] + market["single_a_oas_sep1"])
        * (1 - draft["valuation_assumptions_not_used_in_statements"]["marginal_tax_rate_for_wacc"])
    )
    rate = calculated_wacc if wacc is None else wacc
    if not (0 <= growth < rate and terminal_roic > growth):
        raise ValueError("Independent terminal constraints fail")

    # The only post-valuation-date FY2026 cash flow is 121/184 of H2 FCFF.
    explicit = [(h2["operating_fcff_ex_financing"] * residual_days / h2_days, date(2026, 11, 1))]
    explicit += [(rows[y]["operating_fcff_ex_financing"], date(y, 7, 1)) for y in range(2027, 2031)]
    explicit_pv = sum(cash / (1 + rate) ** _years(day) for cash, day in explicit)
    tax = draft["operating_drivers"]["normalized_nopat_tax_rate"][-1]
    terminal_nopat = rows[2030]["operating_ebit_ex_financing"] * (1 + growth) * (1 - tax)
    terminal_fcff = terminal_nopat * (1 - growth / terminal_roic)
    terminal_value = terminal_fcff / (rate - growth)
    terminal_pv = terminal_value / (1 + rate) ** _years(date(2030, 12, 31))
    operating_ev = explicit_pv + terminal_pv

    reserve = balance["minimum_operating_cash"][0] if minimum_cash is None else minimum_cash
    excess_cash = max(estimated_cash + opening["marketable_securities"] - reserve, 0)
    dividend_payable = 1.69 * market["basic_shares_jun30"]
    common_equity = (
        operating_ev + balance["reported_financing_equity_june"] + excess_cash
        - estimated_corporate_debt - dividend_payable - inputs["reported_non_equity_claims_june"]["nci"]
    )
    return {
        "wacc": rate, "calculated_wacc": calculated_wacc,
        "residual_fraction": residual_days / h2_days,
        "residual_fcff": explicit[0][0], "explicit_pv": explicit_pv,
        "terminal_nopat": terminal_nopat, "terminal_fcff": terminal_fcff,
        "terminal_value": terminal_value, "terminal_pv": terminal_pv,
        "operating_ev": operating_ev, "terminal_share": terminal_pv / operating_ev,
        "estimated_cash": estimated_cash, "estimated_corporate_debt": estimated_corporate_debt,
        "excess_cash": excess_cash, "dividend_payable": dividend_payable,
        "common_equity": common_equity,
        "value_per_share": common_equity / market["diluted_shares_h1_proxy"],
    }


def fcf_bridge(inputs=None, rows=None):
    """Return the source-defined H1 FCF and the model-defined H2 proxy."""
    inputs = load_inputs() if inputs is None else inputs
    rows = build_model(inputs) if rows is None else rows
    h1 = rows[2026]["h1_2026_actual"]
    h2 = rows[2026]["h2_2026_forecast"]
    h1_management = h1["cfo_consolidated"] - 2264 - 743
    h2_proxy = h2["cfo_consolidated"] - h2["delta_financing_receivables"] - h2["capex"] - h2["software_investment"]
    management_reference = 15700.0  # $14.7bn FY25 reported + "about $1bn" FY26 outlook.
    return {
        "h1_cfo": h1["cfo_consolidated"], "h1_financing_adjustment": 2264.0,
        "h1_net_capital_investment": 743.0, "h1_management_fcf": h1_management,
        "h2_cfo": h2["cfo_consolidated"], "h2_financing_adjustment": h2["delta_financing_receivables"],
        "h2_pp_and_e_capex": h2["capex"], "h2_software_investment": h2["software_investment"],
        "h2_net_capital_investment": h2["capex"] + h2["software_investment"], "h2_proxy": h2_proxy,
        "fy_model_proxy": 4760.0 + h2_proxy, "management_reference": management_reference,
        "management_implied_h2": management_reference - 4760.0,
        "unexplained_gap": management_reference - (4760.0 + h2_proxy),
        "h2_cfo_components": {
            "net_income": h2["net_income"], "depreciation": h2["depreciation"],
            "amortization": h2["amortization"], "sbc_noncash_addback": h2["stock_based_compensation"],
            "operating_assets_cash_use": -h2["delta_operating_assets"],
            "operating_liabilities_source": h2["delta_operating_liabilities"],
            "taxes_payable_cash_effect": h2["delta_consolidated_taxes_payable"],
            "financing_receivables_cash_effect": -h2["delta_financing_receivables"],
        },
        "h2_operating_fcff": h2["operating_fcff_ex_financing"],
    }


def main():
    inputs = load_inputs(); rows = build_model(inputs)
    print(json.dumps({"independent_dcf": independent_dcf(inputs, rows), "fcf_bridge": fcf_bridge(inputs, rows)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
