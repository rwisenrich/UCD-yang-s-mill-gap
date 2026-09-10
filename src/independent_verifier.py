#!/usr/bin/env python3
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from native_su3_block import link_verification,h_block,gap,schur_audit,spectral_parent_audit
from jw_verifier import transfer_matrix_certificate, reflection_pushforward_certificate, spectral_correlator_certificate
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'

def main():
    checks=[]
    lv=link_verification()
    checks += [
      ('SU3 covariance',lv['left_right_covariance_residual']<1e-12,lv['left_right_covariance_residual']),
      ('SU3 fundamental Casimir',lv['fundamental_casimir_residual']<1e-12,lv['fundamental_casimir_residual']),
      ('left-right commute',lv['left_right_commutator_residual']<1e-12,lv['left_right_commutator_residual']),
    ]
    H,*_=h_block(1.2,0.05,1.0); d,ev=gap(H)
    checks.append(('positive interacting block gap',d>3.0,d))
    sc=schur_audit(1.2,0.05,1.0)
    checks.append(('Schur low-spectrum residual',max(x['schur_eigen_residual'] for x in sc)<1e-10,max(x['schur_eigen_residual'] for x in sc)))
    sp=spectral_parent_audit(1.2,0.05,1.0)
    checks.append(('spectral parent domination',sp['single_block_projector_domination'],sp['min_eigenvalue_HminusE0_minus_deltaQ']))
    tm=transfer_matrix_certificate()
    checks.append(('positive transfer matrix',tm['positive_self_adjoint_transfer'],tm['transfer_min_eigenvalue']))
    checks.append(('transfer gap identity',tm['gap_residual']<1e-10,tm['gap_residual']))
    rp=reflection_pushforward_certificate(seed=999,trials=100)
    checks.append(('positive-kernel coarse pushforward',rp['pass'],rp['minimum_coarse_kernel_eigenvalue']))
    co=spectral_correlator_certificate()
    checks.append(('nonzero gauge-invariant probe spectral weight',co['nontrivial_probe_weight'],co['spectral_weight_total']))
    checks.append(('spectral exponential bound',co['max_exponential_bound_violation']<1e-10,co['max_exponential_bound_violation']))
    import csv
    rows=[]
    for name,ok,val in checks: rows.append({'check':name,'pass':bool(ok),'value':val})
    with open(RES/'independent_verifier.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    out={'passed':sum(int(x['pass']) for x in rows),'total':len(rows),'all_pass':all(x['pass'] for x in rows)}
    with open(RES/'independent_verifier_summary.json','w') as f: json.dump(out,f,indent=2)
    print(json.dumps(out,indent=2))
    if not out['all_pass']: raise SystemExit(1)
if __name__=='__main__': main()
