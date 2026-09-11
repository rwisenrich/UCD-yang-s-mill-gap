#!/usr/bin/env python3
from __future__ import annotations
import json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def main():
  c=[]
  def ck(n,o,d=''): c.append({'check':n,'pass':bool(o),'detail':str(d)})
  q=json.loads((RES/'ATOMIC_PROOF_FRONTIER_v6.json').read_text()); ck('two_atomic_estimates',q['count']==2,list(q['atomic_estimates'])); ck('four_new_reduction_theorems',len(q['new_reduction_theorems'])==4)
  v=json.loads((RES/'independent_verifier_summary_v6.json').read_text());ck('v6_verifier_green',v['all_pass'],v)
  with open(RES/'rg_crossing_formula.csv') as f:r=list(csv.DictReader(f));ck('rg_crossing_examples',len(r)==12 and all(x['theorem_formula_nonnegative']=='True' for x in r),len(r))
  j=json.loads((RES/'balaban_af_bridge_certificate.json').read_text());ck('UV_AF_summability',j['all_pass'],j['checks'])
  with open(RES/'jaffe_witten_obligation_ledger_v6.csv') as f:l=list(csv.DictReader(f));ck('Jaffe_Witten_ledger_present',len(l)>=25,len(l))
  out={'passed':sum(x['pass'] for x in c),'total':len(c),'all_pass':all(x['pass'] for x in c)}
  with open(RES/'final_verifier_v6.csv','w',newline='') as f:w=csv.DictWriter(f,fieldnames=c[0]);w.writeheader();w.writerows(c)
  (RES/'final_verifier_summary_v6.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
  if not out['all_pass']:raise SystemExit(1)
if __name__=='__main__':main()
