"""IBM Edition B connected statements. USD millions; forecast inputs remain provisional."""
from __future__ import annotations
import argparse
import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = Path(__file__).with_name("inputs.json")
OUTPUT_PATH = ROOT / "output" / "phase3-model-output.json"
YEARS = (2026, 2027, 2028, 2029, 2030)
SEGMENTS = ("software", "consulting", "infrastructure", "financing", "other")
OPERATING_SEGMENTS = ("software", "consulting", "infrastructure", "other")
ASSETS = ("cash", "restricted_cash", "marketable_securities", "trade_ar", "financing_receivables", "other_ar", "inventory", "deferred_costs", "prepaids_other_current", "ppe", "operating_rou", "prepaid_pension", "deferred_tax_assets", "goodwill", "intangibles", "investments_other", "unmapped_other_assets_reconciliation", "reported_rounding_reconciliation")
CLAIMS = ("taxes_payable", "accounts_payable", "comp_benefits", "deferred_income", "operating_leases", "other_accrued", "other_liabilities", "retirement_obligations", "corporate_debt", "financing_debt", "equity")
OPERATING_ASSETS = ("trade_ar", "other_ar", "inventory", "deferred_costs", "prepaids_other_current")
OPERATING_LIABILITIES = ("accounts_payable", "comp_benefits", "deferred_income", "other_accrued")

def load_inputs(path=INPUT_PATH): return json.loads(Path(path).read_text())
def total_assets(row): return sum(row[k] for k in ASSETS)
def total_liabilities_and_equity(row): return sum(row[k] for k in CLAIMS)

def opening_row(inputs):
    row = deepcopy(inputs["opening_june_2026"])
    gap = total_assets(row) - total_liabilities_and_equity(row)
    if abs(gap) > 1e-6: raise ValueError(f"June 30 opening balance sheet gap ${gap:,.4f}m")
    return row

def h2_ratio(inputs, segment):
    h1 = inputs["actuals"]["h1_2025_revenue"][segment]
    if h1 <= 0: raise ValueError(f"Invalid FY2025 H1 {segment} revenue")
    return (inputs["actuals"]["fy2025_revenue"][segment] - h1) / h1

def check_bounds(inputs):
    b, d = inputs["documented_bounds"], inputs["draft_assumptions"]
    for name, path in d["segment_growth_after_2026"].items():
        for x in path:
            if not b["growth_floor"] <= x <= b["growth_ceiling"]: raise ValueError(f"{name} growth {x:.1%} outside documented bound")
    for name in ("operating_gross_margin", "operating_sga_pct", "rnd_pct"):
        for x in d["operating_drivers"][name]:
            if not b["margin_floor"] <= x <= b["margin_ceiling"]: raise ValueError(f"{name} outside documented bound")
    for x in d["operating_drivers"]["normalized_nopat_tax_rate"]:
        if not b["cash_tax_floor"] <= x <= b["cash_tax_ceiling"]: raise ValueError("Normalized NOPAT tax rate outside documented bound")
    for x in d["balance_sheet_and_financing"]["minimum_operating_cash"]:
        if not b["minimum_cash_floor"] <= x <= b["minimum_cash_ceiling"]: raise ValueError("Minimum cash outside documented bound")
    sbc=d["stock_based_compensation"]
    schedule=sbc["forecast_expense_and_noncash_cfo_addback"]
    low,high=sbc["h2_2026_sensitivity_range"]
    if len(schedule)!=len(YEARS) or any(x<0 for x in schedule): raise ValueError("Invalid stock-based compensation schedule")
    if not low<=schedule[0]<=high: raise ValueError("H2 stock-based compensation outside documented sensitivity range")

def h1_2026_actual(inputs):
    src = inputs["actuals"]["h1_2026"]
    rev, inc, cf = deepcopy(src["revenue"]), src["income_statement"], src["cash_flow"]
    operating_revenue = sum(rev[s] for s in OPERATING_SEGMENTS)
    financing_cost = 232.0  # Q2 10-Q H1 financing cost, consolidated income statement.
    operating_cogs = inc["cost"] - financing_cost
    ebit = operating_revenue - operating_cogs - inc["sga"] - inc["rnd"] + inc["ip_income"] + inc["other_income"]
    row = {**rev, "operating_revenue":operating_revenue, "total_revenue":inc["revenue"], "operating_cogs":operating_cogs,
           "operating_gross_profit":operating_revenue-operating_cogs, "operating_sga":inc["sga"], "rnd":inc["rnd"],
           "ip_income":inc["ip_income"], "other_income":inc["other_income"], "operating_ebit_ex_financing":ebit,
           "financing_pretax_contribution":rev["financing"]-financing_cost, "corporate_interest":inc["interest"],
           "pretax_income":inc["pretax"], "income_tax_provision":inc["income_tax_provision"], "net_income":inc["net_income"],
           "depreciation":cf["depreciation"], "amortization":cf["amortization"], "stock_based_compensation":cf["stock_based_compensation"], "capex":cf["capex"],
           "software_investment":cf["software_investment"], "cfo_consolidated":cf["cfo"], "common_dividends":cf["dividends"]}
    if abs(sum(rev.values())-inc["revenue"])>1e-6: raise ValueError("H1 segment revenue bridge failed")
    if abs(ebit+row["financing_pretax_contribution"]-inc["interest"]-inc["pretax"])>1e-6: raise ValueError("H1 pretax bridge failed")
    return row

def period_statement(rev, previous, inputs, i, half_year=False):
    d=inputs["draft_assumptions"]
    op, cap, bs=d["operating_drivers"],d["working_capital_and_capital"],d["balance_sheet_and_financing"]
    r=sum(rev[s] for s in OPERATING_SEGMENTS)
    cogs=r*(1-op["operating_gross_margin"][i])
    sga=r*op["operating_sga_pct"][i]
    rnd=r*op["rnd_pct"][i]
    ip=r*op["ip_income_pct"][i]
    other=r*op["other_income_pct"][i]
    ebit=r-cogs-sga-rnd+ip+other
    finance_profit=rev["financing"]*op["financing_pretax_margin"][i]
    interest=(previous["corporate_debt"]+bs["corporate_debt"][i])/2*op["corporate_interest_rate"][i]*(0.5 if half_year else 1)
    pretax=ebit+finance_profit-interest
    taxes=max(pretax,0)*op["normalized_nopat_tax_rate"][i]
    return {**rev,"operating_revenue":r,"total_revenue":r+rev["financing"],"operating_cogs":cogs,
            "operating_gross_profit":r-cogs,"operating_sga":sga,"rnd":rnd,"ip_income":ip,"other_income":other,
            "operating_ebit_ex_financing":ebit,"financing_pretax_contribution":finance_profit,"corporate_interest":interest,
            "pretax_income":pretax,"income_tax_provision":taxes,"net_income":pretax-taxes,
            "depreciation":previous["ppe"]*cap["depreciation_pct_beginning_ppe"][i],
            "amortization":previous["intangibles"]*cap["amortization_pct_beginning_intangibles"][i]*(0.5 if half_year else 1),
            "stock_based_compensation":d["stock_based_compensation"]["forecast_expense_and_noncash_cfo_addback"][i],
            "capex":r*cap["capex_pct_operating_revenue"][i],
            "software_investment":r*cap["capitalized_software_pct_operating_revenue"][i]}

def ending_balances(inc, previous, inputs, i):
    d=inputs["draft_assumptions"]
    cap,bs=d["working_capital_and_capital"],d["balance_sheet_and_financing"]
    row={k:previous[k] for k in ASSETS+CLAIMS}
    # Annualize H2 flow only to set year-end working-capital balance ratios.
    r=inc["operating_revenue"]*(2 if i==0 else 1)
    cost=inc["operating_cogs"]*(2 if i==0 else 1)
    row.update({"trade_ar":r*cap["trade_ar_pct_operating_revenue"][i],
                "other_ar":r*cap["other_ar_pct_operating_revenue"][i],
                "inventory":cost*cap["inventory_days_on_operating_cost"][i]/365,
                "deferred_costs":r*cap["deferred_costs_pct_operating_revenue"][i],
                "prepaids_other_current":r*cap["prepaids_pct_operating_revenue"][i],
                "accounts_payable":cost*cap["ap_pct_operating_cost"][i],
                "comp_benefits":r*cap["comp_benefits_pct_operating_revenue"][i],
                "deferred_income":r*cap["deferred_income_pct_operating_revenue"][i],
                "other_accrued":r*cap["other_accrued_pct_operating_revenue"][i],
                "taxes_payable":inc["income_tax_provision"]*(2 if i==0 else 1)*cap["taxes_payable_pct_income_tax_provision"][i],
                "ppe":previous["ppe"]+inc["capex"]-inc["depreciation"],
                "intangibles":previous["intangibles"]+inc["software_investment"]-inc["amortization"],
                "corporate_debt":bs["corporate_debt"][i],
                "financing_receivables":previous["financing_receivables"]*(1+bs["financing_receivables_growth"][i])})
    row["financing_debt"]=row["financing_receivables"]*(previous["financing_debt"]/previous["financing_receivables"])
    return row

def period_cash_flow(inc, ending, previous, inputs, i, half_year=False):
    bs=inputs["draft_assumptions"]["balance_sheet_and_financing"]
    dividends=bs["annual_common_dividends"][i]-(inputs["actuals"]["h1_2026"]["cash_flow"]["dividends"] if half_year else 0)
    da=sum(ending[k]-previous[k] for k in OPERATING_ASSETS)
    dl=sum(ending[k]-previous[k] for k in OPERATING_LIABILITIES)
    dtax=ending["taxes_payable"]-previous["taxes_payable"]
    dfar=ending["financing_receivables"]-previous["financing_receivables"]
    dcorp=ending["corporate_debt"]-previous["corporate_debt"]
    dfdebt=ending["financing_debt"]-previous["financing_debt"]
    # SBC expense is assumed embedded in forecast operating-cost ratios. It is noncash in this period,
    # so add it back once to CFO; credit APIC/equity separately, without modeling cash share issuance.
    cfo=inc["net_income"]+inc["depreciation"]+inc["amortization"]+inc["stock_based_compensation"]-da+dl+dtax-dfar
    ending["cash"]=previous["cash"]+cfo-inc["capex"]-inc["software_investment"]+dcorp+dfdebt-dividends
    equity_movements=inc["stock_based_compensation"]  # Noncash SBC credit to APIC; OCI, treasury and NCI held flat.
    ending["equity"]=previous["equity"]+inc["net_income"]-dividends+equity_movements
    tax_rate=inputs["draft_assumptions"]["operating_drivers"]["normalized_nopat_tax_rate"][i]
    fcff=inc["operating_ebit_ex_financing"]*(1-tax_rate)+inc["depreciation"]+inc["amortization"]-inc["capex"]-inc["software_investment"]-da+dl
    return {"delta_operating_assets":da,"delta_operating_liabilities":dl,"delta_consolidated_taxes_payable":dtax,"delta_financing_receivables":dfar,
            "delta_corporate_debt":dcorp,"delta_financing_debt":dfdebt,"cfo_consolidated":cfo,
            "common_dividends":dividends,"stock_based_compensation_apic":inc["stock_based_compensation"],"other_equity_movements":equity_movements,
            "cash_from_cash_flow":ending["cash"],"cash_change":ending["cash"]-previous["cash"],
            "operating_fcff_ex_financing":fcff}

def fy2026_full_year(h1,h2):
    keys=SEGMENTS+("operating_revenue","total_revenue","operating_cogs","operating_gross_profit","operating_sga","rnd","ip_income","other_income","operating_ebit_ex_financing","financing_pretax_contribution","corporate_interest","pretax_income","income_tax_provision","net_income","depreciation","amortization","stock_based_compensation","capex","software_investment","cfo_consolidated","common_dividends")
    return {k:h1[k]+h2[k] for k in keys}

def assert_checks(model,inputs):
    floors=inputs["draft_assumptions"]["balance_sheet_and_financing"]["minimum_operating_cash"]
    for i,year in enumerate(YEARS):
        row=model[year]
        gap=total_assets(row)-total_liabilities_and_equity(row)
        cash_gap=row["cash"]-row["cash_from_cash_flow"]
        if abs(gap)>1e-6: raise ValueError(f"FY{year} balance-sheet check failed: ${gap:,.4f}m")
        if abs(cash_gap)>1e-6: raise ValueError(f"FY{year} cash-flow check failed: ${cash_gap:,.4f}m")
        if row["cash"]<floors[i]-1e-6: raise ValueError(f"FY{year} cash ${row['cash']:,.1f}m below minimum ${floors[i]:,.1f}m")
        row["balance_gap"],row["cash_flow_gap"]=gap,cash_gap
        row["total_assets"],row["total_liabilities_and_equity"]=total_assets(row),total_liabilities_and_equity(row)

def build_model(inputs=None):
    inputs=load_inputs() if inputs is None else inputs
    check_bounds(inputs)
    opening=opening_row(inputs)
    h1=h1_2026_actual(inputs)
    h2_rev={s:h1[s]*h2_ratio(inputs,s) for s in SEGMENTS}
    h2_inc=period_statement(h2_rev,opening,inputs,0,True)
    h2_bs=ending_balances(h2_inc,opening,inputs,0)
    h2_cf=period_cash_flow(h2_inc,h2_bs,opening,inputs,0,True)
    h2={**h2_inc,**h2_cf}
    full=fy2026_full_year(h1,h2)
    season=inputs["draft_assumptions"]["h2_seasonality"]
    fraction=season["residual_days_after_sep1"]/season["h2_days"]
    model={2026:{**full,**h2_bs,"h1_2026_actual":h1,"h2_2026_forecast":h2,"fy2026_full_year":full,
                 "h2_revenue_by_segment":h2_rev,"h2_operating_fcff_ex_financing":h2_cf["operating_fcff_ex_financing"],
                 "residual_fcff_after_sep1_proportional":h2_cf["operating_fcff_ex_financing"]*fraction,
                 "operating_fcff_ex_financing":h2_cf["operating_fcff_ex_financing"],
                 "cash_from_cash_flow":h2_cf["cash_from_cash_flow"]}}
    previous=h2_bs
    prior={s:full[s] for s in SEGMENTS}
    for i,year in enumerate(YEARS[1:],1):
        growth=inputs["draft_assumptions"]["segment_growth_after_2026"]
        rev={s:prior[s]*(1+growth[s][i-1]) for s in SEGMENTS}
        inc=period_statement(rev,previous,inputs,i)
        bs=ending_balances(inc,previous,inputs,i)
        cf=period_cash_flow(inc,bs,previous,inputs,i)
        model[year]={**inc,**bs,**cf}
        previous=bs
        prior=rev
    assert_checks(model,inputs)
    return model

def reconcile_historical_base(inputs):
    opening=opening_row(inputs)
    h1=h1_2026_actual(inputs)
    fcf=inputs["actuals"]["h1_2026"]["cash_flow"]["cfo"]-2264-743
    return {"opening_balance_gap":total_assets(opening)-total_liabilities_and_equity(opening),
            "h1_segment_to_consolidated_revenue_gap":sum(h1[s] for s in SEGMENTS)-h1["total_revenue"],
            "h1_pretax_bridge_gap":h1["operating_ebit_ex_financing"]+h1["financing_pretax_contribution"]-h1["corporate_interest"]-h1["pretax_income"],
            "h1_management_fcf_recalculated":fcf,"h1_management_fcf_reported":4760,"h1_management_fcf_gap":fcf-4760}

def model_payload(model,inputs):
    return {"metadata":{"status":inputs["model_status"],"valuation_date":inputs["valuation_date"],"units":inputs["units"]},
            "historical_base_checks":reconcile_historical_base(inputs),"model":{str(y):model[y] for y in YEARS},
            "financing_sidecar":{"source":"IBM Q2 2026 Form 10-Q p. 73, Financing equity",
                                 "june_30_reported_equity":inputs["draft_assumptions"]["balance_sheet_and_financing"]["reported_financing_equity_june"],
                                 "premium_or_discount":0}}

def demonstrate_failed_check(inputs):
    broken=deepcopy(build_model(inputs))
    broken[2027]["cash"]-=1
    try: assert_checks(broken,inputs)
    except ValueError as error: return f"SAFE FAILURE DEMONSTRATION: detected as intended — {error}"
    raise AssertionError("Broken cash was not detected")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--write-output",action="store_true")
    p.add_argument("--demo-failure",action="store_true")
    a=p.parse_args()
    inputs=load_inputs()
    model=build_model(inputs)
    print("IBM CORRECTED FY2026–FY2030 DRAFT — USD MILLIONS")
    print("Year | Revenue | Ex-Financing EBIT | Ex-Financing FCFF* | Cash | BS gap")
    for y,r in model.items(): print(f"{y} | {r['total_revenue']:,.1f} | {r['operating_ebit_ex_financing']:,.1f} | {r['operating_fcff_ex_financing']:,.1f} | {r['cash']:,.1f} | {r['balance_gap']:,.4f}")
    print("* FY2026 FCFF column is H2 only; FY2027–2030 are full years.")
    print(f"Sep–Dec 2026 residual FCFF: ${model[2026]['residual_fcff_after_sep1_proportional']:,.1f}m")
    if a.demo_failure: print(demonstrate_failed_check(inputs))
    if a.write_output:
        OUTPUT_PATH.parent.mkdir(exist_ok=True)
        OUTPUT_PATH.write_text(json.dumps(model_payload(model,inputs),indent=2))
        print(f"Wrote {OUTPUT_PATH}")

if __name__=="__main__": main()
