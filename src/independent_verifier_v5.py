#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
sys.path.insert(0,str(ROOT/'src'))
from af_summability import infinite_tail_bound, partial_sum, GROUPS
from strong_coupling_endpoint import beta_shen,K_S,g_threshold

def main():
    checks=[]
    old=json.loads((RES/'independent_verifier_summary.json').read_text())
    checks.append(('v4 independent core remains green',old['all_pass'],old['passed']))
    worst_ratio=0.0
    for _,CA in GROUPS.items():
        B=infinite_tail_bound(1.2,CA,4,2); S=partial_sum(50000,1.2,CA,4,2); worst_ratio=max(worst_ratio,S/B)
    checks.append(('AF UV-tail bound dominates 50k-step partial sums',worst_ratio<1.0,worst_ratio))
    gt=g_threshold(3,4)
    checks.append(('SU3 strong-endpoint threshold maps to g^2=32',abs(gt*gt-32)<1e-12,gt*gt))
    checks.append(('SU3 beta at threshold is 1/48',abs(beta_shen(3,gt)-1/48)<1e-12,beta_shen(3,gt)))
    checks.append(('SU3 g=8 has positive Bakry-Emery margin',abs(K_S(3,4,8)-0.75)<1e-12,K_S(3,4,8)))
    rows=list(csv.DictReader(open(RES/'jaffe_witten_obligation_ledger_v5.csv'))); opens=[r for r in rows if r['status'].startswith('OPEN_')]
    checks.append(('former OPEN_* rows converted to theorem/reduction statuses',len(opens)==0,len(opens)))
    m=json.loads((RES/'master_estimates.json').read_text()); checks.append(('exactly two master theorem objects remain',len(m)==2,len(m)))
    lt=json.loads((RES/'functional_limit_theorems.json').read_text()); checks.append(('six functional-analytic reduction theorems emitted',len(lt)==6,len(lt)))
    gc=json.loads((RES/'compact_simple_group_reduction_certificate.json').read_text()); checks.append(('group generalization reduced to M1(G),M2(G)',gc['remaining_group_dependence'].startswith('Only master estimates'),gc['remaining_group_dependence']))
    outrows=[{'check':n,'pass':bool(ok),'value':v} for n,ok,v in checks]
    with open(RES/'independent_verifier_v5.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=outrows[0].keys());w.writeheader();w.writerows(outrows)
    out={'passed':sum(int(r['pass']) for r in outrows),'total':len(outrows),'all_pass':all(r['pass'] for r in outrows)}
    (RES/'independent_verifier_summary_v5.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not out['all_pass']: raise SystemExit(1)
if __name__=='__main__':main()
