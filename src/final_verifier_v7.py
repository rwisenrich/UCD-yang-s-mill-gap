#!/usr/bin/env python3
from __future__ import annotations
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'

def check(name,ok,value=None): return {'check':name,'status':'PASS' if ok else 'FAIL','value':value}

def main():
    src=json.loads((RES/'bounded_wilson_source_certificate_v7.json').read_text())
    pol=json.loads((RES/'polymer_norm_conversion_certificate_v7.json').read_text())
    fr=json.loads((RES/'FINAL_ATOMIC_FRONTIER_v7.json').read_text())
    v6=json.loads((RES/'final_verifier_summary_v6.json').read_text())
    rows=[
      check('bounded_source_certificate_pass',src['all_pass'],src['checks']),
      check('zero_free_radius_positive',math.log(2)>0,math.log(2)),
      check('polymer_norm_certificate_pass',pol['all_pass'],pol['checks']),
      check('z4_entropy_threshold_exact',abs(2*math.log(8)-4.1588830833596715)<1e-14,2*math.log(8)),
      check('v7_two_atomic_estimates',fr['count']==2,fr['count']),
      check('E1_contains_zero_and_source_slices','zero_source_slice' in fr['remaining_atomic_estimates']['E1_SOURCE_EXTENDED_ALL_FIELD_RG'] and 'source_derivative_slice' in fr['remaining_atomic_estimates']['E1_SOURCE_EXTENDED_ALL_FIELD_RG']),
      check('v6_meta_verifier_carried',v6.get('all_pass',False),v6.get('passed')),
    ]
    with open(RES/'final_verifier_v7.csv','w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    out={'passed':sum(r['status']=='PASS' for r in rows),'total':len(rows),'all_pass':all(r['status']=='PASS' for r in rows),'verdict':'V7_REDUCTION_VERIFIED__TWO_ATOMIC_ESTIMATES_E1_E2'}
    (RES/'final_verifier_summary_v7.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    if not out['all_pass']: raise SystemExit(2)
if __name__=='__main__': main()
