#!/usr/bin/env python3
from __future__ import annotations
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def main():
    checks=[]
    def add(name,ok,detail=''): checks.append({'check':name,'pass':bool(ok),'detail':str(detail)})
    v5=json.loads((RES/'independent_verifier_summary_v5.json').read_text()); add('v5_verifier_green',v5['all_pass'],v5)
    t=json.loads((RES/'closure_theorems_v6.json').read_text()); add('six_new_exact_reduction_theorems',len(t)==6,len(t))
    with open(RES/'spectral_transfer_sanity.csv') as f: rr=list(csv.DictReader(f)); add('spectral_transfer_sanity',all(x['pass']=='True' for x in rr),len(rr))
    b=json.loads((RES/'balaban_af_bridge_certificate.json').read_text()); add('AF_tail_bridge_numeric',b['all_pass'],b['checks'])
    s=json.loads((RES/'strong_coupling_endpoint_certificate.json').read_text()); add('SU3_g8_KS_exact_margin',abs(s['SU3_g8_KS']-0.75)<1e-12,s['SU3_g8_KS'])
    g=json.loads((RES/'PROOF_GRAPH_v6.json').read_text()); add('five_master_estimates_only',g['count']==5,g['remaining_master_estimates'])
    with open(RES/'jaffe_witten_obligation_ledger_v6.csv') as f: led=list(csv.DictReader(f))
    add('no_literal_OPEN_status',not any('OPEN' in r['status'] for r in led),[r for r in led if 'OPEN' in r['status']]); add('M1_gap_consequence_encoded',any(r['id']=='JW-12A' and r['status']=='THEOREM_CONSEQUENCE_OF_M1' for r in led)); add('M2_distribution_compactness_encoded',any(r['id']=='JW-08B1' and r['status']=='THEOREM_CONSEQUENCE_OF_M2A' for r in led))
    with open(RES/'independent_verifier_v6.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=checks[0]);w.writeheader();w.writerows(checks)
    out={'passed':sum(c['pass'] for c in checks),'total':len(checks),'all_pass':all(c['pass'] for c in checks)}; (RES/'independent_verifier_summary_v6.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
    if not out['all_pass']: raise SystemExit(1)
if __name__=='__main__':main()
