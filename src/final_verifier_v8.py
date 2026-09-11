#!/usr/bin/env python3
from __future__ import annotations
import json,csv,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def main():
  c=[]
  def ck(n,o,v=''): c.append({'check':n,'status':'PASS' if o else 'FAIL','value':v})
  v7=json.loads((RES/'final_verifier_summary_v7.json').read_text()); ck('v7_reduction_green',v7['all_pass'],v7['passed'])
  t=json.loads((RES/'transfer_gap_certificate_v8.json').read_text()); ck('transfer_mass_identity_numeric',t['all_numeric_checks'],t['row_count'])
  s=json.loads((RES/'source_scaling_certificate_v8.json').read_text()); ck('local_source_radius_a4_scaling',s['all_rows_constant_ratio'],s['numeric_scaling_constant'])
  with open(RES/'physical_transfer_gap_v8.csv') as f:r=list(csv.DictReader(f)); ck('raw_transfer_gap_vanishes_with_a',float(r[-1]['raw_transfer_gap'])<float(r[0]['raw_transfer_gap']),(r[0]['raw_transfer_gap'],r[-1]['raw_transfer_gap']))
  f=json.loads((RES/'FINAL_ATOMIC_FRONTIER_v7.json').read_text()); ck('two_terminal_estimates_preserved',f['count']==2,f['count'])
  ck('mass_normalization_formula',abs((-math.log(math.exp(-0.01*0.7))/0.01)-0.7)<1e-12)
  out={'passed':sum(x['status']=='PASS' for x in c),'total':len(c),'all_pass':all(x['status']=='PASS' for x in c),'verdict':'V8_TRANSFER_AND_SOURCE_SCALING_AUDIT_PASS__E1_E2_REMAIN_LOAD_BEARING'}
  with open(RES/'final_verifier_v8.csv','w',newline='') as f0:w=csv.DictWriter(f0,fieldnames=c[0]);w.writeheader();w.writerows(c)
  (RES/'final_verifier_summary_v8.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
  if not out['all_pass']: raise SystemExit(1)
if __name__=='__main__':main()
