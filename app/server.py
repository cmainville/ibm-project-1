"""Local-only IBM valuation workbench. Standard library; no network deployment."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import html
import json
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"model"))
from valuation import run_analysis  # noqa: E402

APP=Path(__file__).resolve().parent
CONTENT={"/":"index.html","/index.html":"index.html","/styles.css":"styles.css","/app.js":"app.js"}
MIME={".html":"text/html; charset=utf-8",".css":"text/css; charset=utf-8",".js":"application/javascript; charset=utf-8"}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=self.path.split("?",1)[0]
        if path=="/api/analysis":
            try: self.respond(200,json.dumps(run_analysis()).encode(),"application/json; charset=utf-8")
            except Exception as exc: self.respond(500,json.dumps({"error":str(exc)}).encode(),"application/json")
            return
        name=CONTENT.get(path)
        if not name: self.respond(404,b"Not found","text/plain");return
        self.respond(200,(APP/name).read_bytes(),MIME[Path(name).suffix])

    def do_POST(self):
        if self.path!="/api/analysis": self.respond(404,b"Not found","text/plain");return
        try:
            size=int(self.headers.get("Content-Length","0"))
            if size>10000: raise ValueError("Request too large")
            req=json.loads(self.rfile.read(size))
            out=run_analysis(case=req.get("case","base"),overrides=req.get("overrides",{}),demo_failure=req.get("demo_failure",False))
            self.respond(200,json.dumps(out).encode(),"application/json; charset=utf-8")
        except (ValueError,TypeError,KeyError) as exc:
            self.respond(400,json.dumps({"error":str(exc)}).encode(),"application/json; charset=utf-8")

    def respond(self,status,body,mime):
        self.send_response(status)
        self.send_header("Content-Type",mime)
        self.send_header("Content-Length",str(len(body)))
        self.send_header("Cache-Control","no-store")
        self.end_headers()
        self.wfile.write(body)

def static_output(path):
    r=run_analysis()
    e=html.escape
    money=lambda n:f"${n:,.1f}m"
    d=r["dcf"];b=d["bridge"];w=r["wacc_build"]
    lines=["<!doctype html><html lang='en'><meta charset='utf-8'><title>IBM September 1, 2026 visible output</title>",
           "<style>body{font:16px system-ui;max-width:1100px;margin:2rem auto;color:#172433}table{border-collapse:collapse;width:100%;margin:1rem 0}td,th{border:1px solid #ccd4dc;padding:.45rem;text-align:right}th:first-child,td:first-child{text-align:left}h1,h2{color:#123c67}.flag{background:#fff0cb;padding:1rem}</style>",
           "<h1>IBM valuation — September 1, 2026 after close</h1><p class='flag'>WATCH / DEFER. Base valuation is below market and qualified bridge/WACC evidence remains open. USD millions except per-share data. Filing balance sheet: June 30, 2026.</p>",
           f"<p>Valuation/bridge date: September 1, 2026 after close. IBM close: $231.40; Sep. 2–Dec. 31 FCFF (121/184): {money(r['rows']['2026']['residual_fcff_after_sep1_proportional'])}; WACC: {w['wacc']:.2%}; base value: ${b['value_per_share']:.2f}/share.</p>",
           "<h2>Cases</h2><table><tr><th>Case</th><th>Per share</th><th>Changes</th></tr>"]
    for case in ("low","base","high"):
        c=run_analysis(case=case)
        lines.append(f"<tr><td>{case}</td><td>${c['dcf']['bridge']['value_per_share']:.2f}</td><td>{e('; '.join(c['case_changes']) or 'Documented base paths')}</td></tr>")
    lines.append("</table><h2>Five-year statements and operating FCFF</h2><table><tr><th>USD m</th><th>2026 full year</th><th>2027</th><th>2028</th><th>2029</th><th>2030</th></tr>")
    for label,key in (("Revenue","total_revenue"),("Operating EBIT ex-Financing","operating_ebit_ex_financing"),("Consolidated net income","net_income"),("Cash","cash"),("Balance-sheet gap","balance_gap"),("Operating FCFF (2026 H2 only)","operating_fcff_ex_financing")):
        lines.append(f"<tr><td>{label}</td>"+"".join(f"<td>{r['rows'][str(y)][key]:,.1f}</td>" for y in range(2026,2031))+"</tr>")
    lines.append("</table><p>FY2026 revenue/net income include H1 actual + H2 forecast; FY2026 FCFF cell is H2 only. December cash/equity roll from June using H2 only.</p>")
    lines.append("<h2>WACC</h2><table><tr><th>Input</th><th>Value</th></tr>")
    for k in ("risk_free","erp","beta","cost_equity","a_credit_spread","pretax_cost_debt","marginal_tax_rate_for_wacc","after_tax_cost_debt","market_equity","corporate_debt","equity_weight","debt_weight","wacc"):
        lines.append(f"<tr><td>{e(k.replace('_',' '))}</td><td>{w[k]:,.6f}</td></tr>")
    lines.append("</table><h2>DCF and bridge</h2><table><tr><th>Item</th><th>USD m except shares</th></tr>")
    for k in ("operating_ev","financing_equity","estimated_sep1_cash","marketable_securities_june30","minimum_operating_cash","excess_cash_and_securities","estimated_sep1_corporate_debt","declared_dividend_payable","pension_debt_like_claim","nci","common_equity","diluted_shares_proxy","value_per_share"):
        lines.append(f"<tr><td>{e(k.replace('_',' '))}</td><td>{b[k]:,.3f}</td></tr>")
    t=d['terminal']
    lines.append(f"</table><h2>Terminal reinvestment framework</h2><p>FY2031 EBIT {money(t['terminal_2031_ebit'])}; NOPAT {money(t['terminal_2031_nopat'])}; incremental ROIC {t['terminal_incremental_roic']:.1%}; reinvestment rate {t['terminal_reinvestment_rate']:.1%}; reinvestment {money(t['terminal_reinvestment'])}; normalized FCFF {money(t['terminal_fcff'])}. SUPERSEDED naïve FCFF: {money(t['superseded_naive_terminal_fcff'])}. Terminal PV / operating EV: {d['terminal_share_of_operating_ev']:.1%}; reverse DCF g at $231.40: {r['reverse_dcf']['implied_growth']:.2%} holding ROIC fixed.</p>")
    lines.append("<h2>Peers</h2><table><tr><th>Peer</th><th>EV/GAAP EBIT</th><th>P/GAAP E</th><th>Period</th></tr>")
    for p in r["peers"]: lines.append(f"<tr><td>{p['name']}</td><td>{p['ev_ebit']:.2f}×</td><td>{p['pe']:.2f}×</td><td>{p['period']}</td></tr>")
    lines.append("</table><h2>IBM implied peer values</h2><table><tr><th>Peer</th><th>EV/EBIT value/share</th><th>P/E value/share</th></tr>")
    for p in r['peer_implied_values']: lines.append(f"<tr><td>{p['peer']}</td><td>${p['implied_value_per_share_ev_ebit']:.2f}</td><td>${p['implied_value_per_share_pe']:.2f}</td></tr>")
    lines.append("</table><p>Oracle/Accenture are reference anchors, not a mechanically averaged IBM target. IBM P/E uses FY2026E consolidated net income as a labeled common-earnings proxy, not NOPAT.</p>")
    lines.append("<h2>Sources and limitations</h2><p><a href='../evidence-ledger.md'>Evidence ledger</a> · <a href='../docs/phase4-5-review.md'>Review note</a>. Beta 0.70 is a dated third-party indication with opaque method; 5.47% cost of debt is 10-year Treasury plus single-A corporate OAS, not an IBM bond yield. Pension/NCI bridge deductions and point-in-time future dilution remain unresolved. The approved SBC repair is a noncash CFO add-back and APIC credit, not an addition to operating FCFF. FY2026 company-style FCF proxy is $10.918bn, approximately $4.782bn below the July management-outlook reference. The $7.5bn operating cash floor is an analyst estimate. The human-only Locked Changed-Input Record experiment was completed October 10, 2026; its BEFORE/AFTER records and screenshots are stored in <code>docs/</code> as historical pre-SBC evidence.</p></html>")
    path.parent.mkdir(exist_ok=True)
    path.write_text("\n".join(lines))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--port",type=int,default=8765)
    parser.add_argument("--write-static",action="store_true")
    a=parser.parse_args()
    if a.write_static:
        static_output(ROOT/"output"/"visible-base-output.html")
        print("Wrote output/visible-base-output.html")
        return
    server=ThreadingHTTPServer(("127.0.0.1",a.port),Handler)
    print(f"IBM local workbench: http://127.0.0.1:{a.port}/",flush=True)
    server.serve_forever()

if __name__=="__main__":main()
