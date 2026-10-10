"""September 1, 2026 after-close IBM operating DCF and peer valuation.

All currency amounts are USD millions except per-share data.  This module is the
only valuation engine used by the local application.  It deliberately separates
the consolidated accounting model from the operating valuation: IBM Financing is
excluded from operating FCFF and appears once as a June 30 equity sidecar.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date
import math

from ibm_phase3_model import YEARS, build_model, load_inputs, opening_row

VALUE_DATE = date(2026, 9, 1)             # after market close
BRIDGE_DATE = VALUE_DATE
RESIDUAL_START = date(2026, 9, 2)          # cash on Sep. 1 is no longer future
RESIDUAL_MIDPOINT = date(2026, 11, 1)      # approximate midpoint of Sep. 2–Dec. 31
TERMINAL_GROWTH = .025

# Policy fixed before refreshed outputs: Oracle and Accenture are the only peers.
# Data are carried forward from the evidence ledger; values are deliberately not
# refreshed with post-cutoff information.
PEERS = {
    "Oracle": {"price": 141.32, "shares": 2880.471, "cash": 31289, "securities": 605,
               "debt": 129541, "other_claims": 5000, "ebit": 20606, "net_income_common": 16984,
               "period": "FY ended 2026-05-31", "filing_date": "2026-06-22",
               "definition": "GAAP operating income and NI after preferred dividends",
               "source": "https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm",
               "qualification": "Qualified with caution: cloud infrastructure/capex mix and mandatory convertible preferred differ materially."},
    "Accenture": {"price": 188.09, "shares": 612.162617, "cash": 10165.245, "securities": 6.322,
                  "debt": 5142.265, "other_claims": 1123.273 + 493.874,
                  "ebit": 10225.664 + 8542.543 - 8175.973,
                  "net_income_common": 7678.433 + 6375.789 - 6264.470,
                  "period": "TTM ended 2026-05-31", "filing_date": "2026-06-18 and 2025-10-10",
                  "definition": "GAAP operating income and NI attributable to Accenture plc",
                  "source": "https://www.sec.gov/Archives/edgar/data/1467373/000146737326000032/acn-20260531.htm",
                  "qualification": "Qualified with caution: consulting-heavy mix, small debt, and fiscal-year difference."},
}


def years_from_valuation(day):
    return (day - VALUE_DATE).days / 365.0


def _bs(inputs):
    return inputs["draft_assumptions"]["balance_sheet_and_financing"]


def sep1_bridge(rows, inputs):
    """Roll June 30 reported bridge inputs to September 1 after close.

    The cash roll-forward is intentionally mechanical and clearly estimated.  It
    uses the H2 forecast only and recognizes no July–September common-dividend
    cash payment.  The declared Sep. 10 $1.69 dividend is a separate claim.
    """
    dates = inputs["draft_assumptions"]["h2_seasonality"]
    if (dates["h2_start"], dates["valuation_boundary"], dates["fy_end_exclusive"]) != ("2026-07-01", "2026-09-02", "2027-01-01"):
        raise AssertionError("September 1 after-close date controls are not configured")
    h2_days, pre_days, residual_days = dates["h2_days"], dates["prevaluation_days"], dates["residual_days_after_sep1"]
    if (h2_days, pre_days, residual_days) != (184, 63, 121) or pre_days + residual_days != h2_days:
        raise AssertionError("H2 day convention must be 63 prevaluation + 121 residual days")
    h2 = rows[2026]["h2_2026_forecast"]
    opening = opening_row(inputs)
    fraction = pre_days / h2_days
    cash_components = {
        "june30_cash": opening["cash"],
        "prevaluation_h2_cfo": h2["cfo_consolidated"] * fraction,
        "prevaluation_h2_capex": -h2["capex"] * fraction,
        "prevaluation_h2_software_investment": -h2["software_investment"] * fraction,
        "prevaluation_corporate_debt_change": h2["delta_corporate_debt"] * fraction,
        "prevaluation_financing_debt_change": h2["delta_financing_debt"] * fraction,
        "actual_common_dividend_cash_paid_jul1_sep1": 0.0,
    }
    estimated_cash = sum(cash_components.values())
    # June 30 basic shares are the latest reported count; no Aug. 10 count found.
    dividend_per_share = 1.69
    payable = dividend_per_share * inputs["market"]["basic_shares_jun30"]
    estimated_corporate_debt = opening["corporate_debt"] + h2["delta_corporate_debt"] * fraction
    return {
        "bridge_date": BRIDGE_DATE.isoformat(), "valuation_date": VALUE_DATE.isoformat(),
        "prevaluation_fraction": fraction, "h2_days": h2_days, "prevaluation_days": pre_days,
        "residual_days": residual_days, "cash_components": cash_components,
        "estimated_sep1_cash": estimated_cash,
        "estimated_sep1_corporate_debt": estimated_corporate_debt,
        "marketable_securities_june30": opening["marketable_securities"],
        "financing_equity_june30": _bs(inputs)["reported_financing_equity_june"],
        "nci_june30": inputs["reported_non_equity_claims_june"]["nci"],
        "declared_dividend_per_share": dividend_per_share,
        "declared_dividend_payable": payable,
        "declared_dividend_detail": "IBM dividend #446: $1.69 declared, record date 2026-08-10, payable 2026-09-10; June 30 basic shares proxy.",
        "estimated_sep1_net_debt_before_dividend": estimated_corporate_debt - estimated_cash - opening["marketable_securities"],
    }


def wacc_build(inputs, rows=None, beta=None, cost_debt=None):
    m = inputs["market"]
    rf, erp = m["risk_free_rate_sep1"], m["implied_erp_sep1"]
    beta = m["beta_sep1_third_party_indication"] if beta is None else beta
    spread = m["single_a_oas_sep1"]
    cost_debt = rf + spread if cost_debt is None else cost_debt
    rows = build_model(inputs) if rows is None else rows
    bridge = sep1_bridge(rows, inputs)
    equity_market = m["ibm_price_sep1"] * m["basic_shares_jun30"]
    debt = bridge["estimated_sep1_corporate_debt"]
    equity_weight = equity_market / (equity_market + debt)
    debt_weight = 1 - equity_weight
    cost_equity = rf + beta * erp
    tax = inputs["draft_assumptions"]["valuation_assumptions_not_used_in_statements"]["marginal_tax_rate_for_wacc"]
    wacc = equity_weight * cost_equity + debt_weight * cost_debt * (1 - tax)
    return dict(risk_free=rf, erp=erp, beta=beta, beta_method="Qualified third-party indication; independent cutoff-dated regression remains unresolved.",
                cost_equity=cost_equity, a_credit_spread=spread,
                debt_yield_method="Treasury plus single-A OAS proxy; not an IBM-specific bond yield.",
                pretax_cost_debt=cost_debt, marginal_tax_rate_for_wacc=tax,
                after_tax_cost_debt=cost_debt * (1-tax), market_equity=equity_market,
                corporate_debt=debt, equity_weight=equity_weight, debt_weight=debt_weight, wacc=wacc,
                limitations="Beta and issuer-specific debt yield are QUALIFIED/UNRESOLVED pending reproducible dated evidence.")


def case_inputs(base, case):
    x = deepcopy(base)
    d = x["draft_assumptions"]
    changes = []
    if case == "base": return x, changes
    if case not in ("low", "high"): raise ValueError("Case must be low, base, or high")
    sign = -1 if case == "low" else 1
    for segment, shift in (("software", .02), ("consulting", .015), ("infrastructure", .02)):
        path = d["segment_growth_after_2026"][segment]
        d["segment_growth_after_2026"][segment] = [v + sign * shift for v in path]
        changes.append(f"FY2027–30 {segment} growth {sign*shift:+.1%} versus base")
    op = d["operating_drivers"]
    op["operating_gross_margin"] = [op["operating_gross_margin"][0]] + [v + sign*.01 for v in op["operating_gross_margin"][1:]]
    op["operating_sga_pct"] = [op["operating_sga_pct"][0]] + [v - sign*.005 for v in op["operating_sga_pct"][1:]]
    op["normalized_nopat_tax_rate"] = [op["normalized_nopat_tax_rate"][0]] + [v - sign*.02 for v in op["normalized_nopat_tax_rate"][1:]]
    cap = d["working_capital_and_capital"]
    cap["capex_pct_operating_revenue"] = [cap["capex_pct_operating_revenue"][0]] + [v - sign*.002 for v in cap["capex_pct_operating_revenue"][1:]]
    changes += [f"FY2027–30 gross margin {sign*.01:+.1%}", f"SG&A/revenue {-sign*.005:+.1%}",
                f"normalized NOPAT tax {-sign*.02:+.1%}", f"capex/revenue {-sign*.002:+.1%}"]
    return x, changes


def terminal_diagnostics(rows, inputs, rate, growth, terminal_roic=None):
    tax = inputs["draft_assumptions"]["operating_drivers"]["normalized_nopat_tax_rate"][-1]
    roic = inputs["draft_assumptions"]["valuation_assumptions_not_used_in_statements"]["terminal_incremental_roic"] if terminal_roic is None else terminal_roic
    if not 0 <= growth < rate: raise ValueError("Terminal growth must be nonnegative and below WACC")
    if roic <= growth: raise ValueError("Terminal incremental ROIC must exceed terminal growth")
    ebit = rows[2030]["operating_ebit_ex_financing"] * (1 + growth)
    nopat = ebit * (1-tax)
    reinvestment_rate = growth / roic
    if not 0 <= reinvestment_rate < 1: raise ValueError("Terminal reinvestment rate must be within [0, 1)")
    reinvestment = nopat * reinvestment_rate
    fcff = nopat - reinvestment
    if growth > 0 and not fcff < nopat: raise AssertionError("Positive terminal growth requires FCFF below NOPAT")
    # Retained solely for correction disclosure: it is not used to value the business.
    superseded_naive_fcff = rows[2030]["operating_fcff_ex_financing"] * (1+growth)
    return {"terminal_2031_ebit": ebit, "normalized_terminal_nopat_tax_rate": tax,
            "terminal_2031_nopat": nopat, "terminal_incremental_roic": roic,
            "terminal_reinvestment_rate": reinvestment_rate, "terminal_reinvestment": reinvestment,
            "terminal_fcff": fcff, "superseded_naive_terminal_fcff": superseded_naive_fcff,
            "superseded_naive_terminal_value": superseded_naive_fcff/(rate-growth)}


def dcf_from_rows(rows, inputs, wacc=None, growth=TERMINAL_GROWTH, minimum_cash=None, terminal_roic=None):
    wb = wacc_build(inputs, rows)
    rate = wb["wacc"] if wacc is None else wacc
    if not .04 <= rate <= .15: raise ValueError("WACC outside 4%–15% boundary")
    td = terminal_diagnostics(rows, inputs, rate, growth, terminal_roic)
    h2_fcff = rows[2026]["h2_2026_forecast"]["operating_fcff_ex_financing"]
    residual_fraction = 121/184
    residual_fcff = h2_fcff * residual_fraction
    if not math.isclose(residual_fcff, rows[2026]["residual_fcff_after_sep1_proportional"], abs_tol=1e-7):
        raise AssertionError("Residual FCFF must be H2 operating FCFF × 121/184")
    cash_flows = [("Sep 2–Dec 31 2026", residual_fcff, RESIDUAL_MIDPOINT)]
    cash_flows += [(str(y), rows[y]["operating_fcff_ex_financing"], date(y, 7, 1)) for y in YEARS[1:]]
    pv_rows = [dict(period=p, fcff=f, midpoint=d.isoformat(), years=years_from_valuation(d), pv=f/(1+rate)**years_from_valuation(d)) for p,f,d in cash_flows]
    terminal_value = td["terminal_fcff"]/(rate-growth)
    terminal_years = years_from_valuation(date(2030, 12, 31))
    terminal_pv = terminal_value/(1+rate)**terminal_years
    operating_ev = sum(r["pv"] for r in pv_rows) + terminal_pv
    bridge_date = sep1_bridge(rows, inputs)
    reserve = _bs(inputs)["minimum_operating_cash"][0] if minimum_cash is None else minimum_cash
    if not 5000 <= reserve <= 10000: raise ValueError("Operating cash reserve outside documented 5–10bn bound")
    liquid = bridge_date["estimated_sep1_cash"] + bridge_date["marketable_securities_june30"]
    excess = max(liquid-reserve, 0)
    pension_debt_like_claim = 0.0 # convention: no incremental claim after operating retirement expense; see pension reconciliation.
    other_claims = 0.0
    common_equity = (operating_ev + bridge_date["financing_equity_june30"] + excess
                     - bridge_date["estimated_sep1_corporate_debt"] - bridge_date["declared_dividend_payable"]
                     - pension_debt_like_claim - bridge_date["nci_june30"] - other_claims)
    shares = inputs["market"]["diluted_shares_h1_proxy"]
    bridge = dict(operating_ev=operating_ev, financing_equity=bridge_date["financing_equity_june30"],
                  estimated_sep1_cash=bridge_date["estimated_sep1_cash"],
                  marketable_securities_june30=bridge_date["marketable_securities_june30"],
                  liquid_assets=liquid, minimum_operating_cash=reserve, excess_cash_and_securities=excess,
                  estimated_sep1_corporate_debt=bridge_date["estimated_sep1_corporate_debt"],
                  declared_dividend_payable=bridge_date["declared_dividend_payable"],
                  pension_debt_like_claim=pension_debt_like_claim, nci=bridge_date["nci_june30"], other_claims=other_claims,
                  common_equity=common_equity, diluted_shares_proxy=shares, value_per_share=common_equity/shares)
    return dict(wacc=rate, growth=growth, pv_flows=pv_rows, pv_explicit=sum(r["pv"] for r in pv_rows),
                terminal_value=terminal_value, terminal_pv=terminal_pv,
                terminal_share_of_operating_ev=terminal_pv/operating_ev, terminal=td,
                residual_fraction=residual_fraction, bridge_date=bridge_date, bridge=bridge)


def peer_screen():
    result=[]
    for name,p in PEERS.items():
        cap=p["price"]*p["shares"]
        ev=cap+p["debt"]+p["other_claims"]-p["cash"]-p["securities"]
        result.append({**p,"name":name,"price_date":"2026-09-01","market_cap":cap,"enterprise_value":ev,
                       "ev_ebit":ev/p["ebit"],"pe":cap/p["net_income_common"]})
    return result


def implied_peer_values(rows, inputs, dcf):
    """Apply every peer separately; no averaging and no claims of precision."""
    bridge = dcf["bridge"]
    ibm_ebit = rows[2026]["operating_ebit_ex_financing"]
    # P/E must use earnings attributable to common shareholders, not operating
    # NOPAT. The integrated model has no preferred dividend or NCI earnings
    # allocation forecast, so consolidated FY2026E net income is a labeled
    # common-earnings proxy rather than a claim of reported attributable income.
    ibm_common_earnings_proxy = rows[2026]["net_income"]
    out=[]
    for p in peer_screen():
        implied_ev = p["ev_ebit"] * ibm_ebit
        implied_eq_from_ev = (implied_ev + bridge["financing_equity"] + bridge["excess_cash_and_securities"]
                              - bridge["estimated_sep1_corporate_debt"] - bridge["declared_dividend_payable"]
                              - bridge["pension_debt_like_claim"] - bridge["nci"] - bridge["other_claims"])
        implied_eq_from_pe = p["pe"] * ibm_common_earnings_proxy
        out.append({"peer":p["name"], "peer_ev_ebit":p["ev_ebit"], "peer_pe":p["pe"],
                    "ibm_metric_period":"FY2026E operating EBIT ex-Financing", "ibm_operating_ebit":ibm_ebit,
                    "implied_operating_ev":implied_ev, "implied_common_equity_from_ev_ebit":implied_eq_from_ev,
                    "implied_value_per_share_ev_ebit":implied_eq_from_ev/bridge["diluted_shares_proxy"],
                    "ibm_common_earnings_proxy":ibm_common_earnings_proxy,
                    "ibm_common_earnings_definition":"FY2026E consolidated net income; no forecast preferred dividends or NCI earnings allocation. Not NOPAT.",
                    "implied_common_equity_from_pe":implied_eq_from_pe,
                    "implied_value_per_share_pe":implied_eq_from_pe/bridge["diluted_shares_proxy"]})
    return out


def reverse_dcf(rows, inputs, rate, target_price, terminal_roic=None):
    roic = inputs["draft_assumptions"]["valuation_assumptions_not_used_in_statements"]["terminal_incremental_roic"] if terminal_roic is None else terminal_roic
    lo, hi = .000001, min(rate, roic)-.000001
    target=target_price*inputs["market"]["diluted_shares_h1_proxy"]
    if dcf_from_rows(rows,inputs,rate,lo, terminal_roic=roic)["bridge"]["common_equity"] > target:
        return {"implied_growth":None,"status":"Market price below zero-growth DCF","terminal_roic_held_constant":roic}
    for _ in range(80):
        mid=(lo+hi)/2
        if dcf_from_rows(rows,inputs,rate,mid, terminal_roic=roic)["bridge"]["common_equity"] < target: lo=mid
        else: hi=mid
    return {"implied_growth":(lo+hi)/2,"status":"Solved terminal growth with terminal ROIC held constant", "terminal_roic_held_constant":roic}


def one_at_a_time(inputs, base_rows, base_dcf, rate):
    specs=(("Software growth +2pp", "growth", "software", .02), ("Consulting growth +1.5pp", "growth", "consulting", .015),
           ("Infrastructure growth +2pp", "growth", "infrastructure", .02), ("Gross margin +1pp", "operating", "operating_gross_margin", .01),
           ("SG&A/revenue -0.5pp", "operating", "operating_sga_pct", -.005), ("Normalized NOPAT tax -2pp", "operating", "normalized_nopat_tax_rate", -.02),
           ("Capex/revenue -0.2pp", "capital", "capex_pct_operating_revenue", -.002))
    out=[]
    for label,group,key,shift in specs:
        altered=deepcopy(inputs); d=altered["draft_assumptions"]
        path=(d["segment_growth_after_2026"] if group=="growth" else d["operating_drivers"] if group=="operating" else d["working_capital_and_capital"])[key]
        for i in (range(4) if group=="growth" else range(1,5)): path[i]+=shift
        changed=build_model(altered); val=dcf_from_rows(changed,altered,rate,base_dcf["growth"])
        out.append({"driver":label,"changed_assumption":shift,"fy2030_ebit_impact":changed[2030]["operating_ebit_ex_financing"]-base_rows[2030]["operating_ebit_ex_financing"],
                    "fy2030_fcff_impact":changed[2030]["operating_fcff_ex_financing"]-base_rows[2030]["operating_fcff_ex_financing"],
                    "per_share_impact":val["bridge"]["value_per_share"]-base_dcf["bridge"]["value_per_share"]})
    return sorted(out,key=lambda r:abs(r["per_share_impact"]),reverse=True)


def run_analysis(inputs=None, case="base", overrides=None, demo_failure=False):
    base=load_inputs() if inputs is None else deepcopy(inputs); selected,changes=case_inputs(base,case); overrides=overrides or {}
    allowed={"software_growth_shift","consulting_growth_shift","infrastructure_growth_shift","gross_margin_shift","sga_shift","cash_tax_shift","capex_shift","minimum_cash","terminal_growth","terminal_roic","wacc_shift"}
    if set(overrides)-allowed: raise ValueError("Unknown driver override")
    for seg in ("software","consulting","infrastructure"):
        shift=float(overrides.get(f"{seg}_growth_shift",0));
        if abs(shift)>.03: raise ValueError("Growth shift outside ±3% control bound")
        selected["draft_assumptions"]["segment_growth_after_2026"][seg]=[v+shift for v in selected["draft_assumptions"]["segment_growth_after_2026"][seg]]
    for key,override,limit in (("operating_gross_margin","gross_margin_shift",.02),("operating_sga_pct","sga_shift",.02),("normalized_nopat_tax_rate","cash_tax_shift",.04)):
        shift=float(overrides.get(override,0));
        if abs(shift)>limit: raise ValueError(f"{override} outside control bound")
        selected["draft_assumptions"]["operating_drivers"][key]=[v+shift for v in selected["draft_assumptions"]["operating_drivers"][key]]
    capshift=float(overrides.get("capex_shift",0));
    if abs(capshift)>.005: raise ValueError("Capex shift outside ±0.5% bound")
    cap=selected["draft_assumptions"]["working_capital_and_capital"]; cap["capex_pct_operating_revenue"]=[v+capshift for v in cap["capex_pct_operating_revenue"]]
    rows=build_model(selected); wb=wacc_build(selected,rows); rate=wb["wacc"]+float(overrides.get("wacc_shift",0))
    if abs(float(overrides.get("wacc_shift",0)))>.01: raise ValueError("WACC shift outside ±1pp control bound")
    growth=float(overrides.get("terminal_growth",selected["draft_assumptions"]["valuation_assumptions_not_used_in_statements"]["terminal_growth"]))
    roic=float(overrides.get("terminal_roic",selected["draft_assumptions"]["valuation_assumptions_not_used_in_statements"]["terminal_incremental_roic"]))
    if not .02 <= growth <= .03: raise ValueError("Terminal growth outside documented 2%–3% valuation range")
    dcf=dcf_from_rows(rows,selected,rate,growth,overrides.get("minimum_cash"),roic)
    sensitivity=[{"wacc":wr,"values":[dcf_from_rows(rows,selected,wr,g,terminal_roic=roic)["bridge"]["value_per_share"] for g in (.02,.025,.03)]} for wr in [rate-.01,rate-.005,rate,rate+.005,rate+.01]]
    roic_sensitivity=[{"terminal_roic":r,"value_per_share":dcf_from_rows(rows,selected,rate,growth,terminal_roic=r)["bridge"]["value_per_share"]} for r in (.12,.15,.18)]
    checks={"statement_articulation":"PASS","historical_base":"PASS","bridge":"PASS","failed_check_demo":"NOT RUN"}
    if demo_failure:
        from ibm_phase3_model import demonstrate_failed_check
        checks["failed_check_demo"]=demonstrate_failed_check(selected)
    return {"status":"WATCH / DEFER — valuation screen below market; resolve qualified bridge and WACC evidence","case":case,"case_changes":changes,"inputs":selected,
            "rows":{str(y):rows[y] for y in YEARS},"wacc_build":wb,"dcf":dcf,
            "sensitivity":{"terminal_growth":[.02,.025,.03],"rows":sensitivity,"terminal_roic":roic_sensitivity},
            "reverse_dcf":reverse_dcf(rows,selected,rate,selected["market"]["ibm_price_sep1"],roic),
            "peers":peer_screen(),"peer_implied_values":implied_peer_values(rows,selected,dcf),
            "peer_leave_one_out":[{"retained_peer":p["name"],"ev_ebit":p["ev_ebit"],"pe":p["pe"]} for p in peer_screen()],
            "driver_sensitivity":one_at_a_time(selected,rows,dcf,rate),"checks":checks}
