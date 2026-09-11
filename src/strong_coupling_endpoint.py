#!/usr/bin/env python3
"""Strong-coupling endpoint normalization and perturbative stability margins."""
from __future__ import annotations
import csv, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def beta_shen(N:int,g:float)->float: return 2.0/(N*g*g)
def K_S(N:int,d:int,g:float)->float:
    beta=beta_shen(N,g); return N/2.0-8.0*N*abs(beta)*(d-1)
def g_threshold_suN(d:int=4)->float: raise RuntimeError('Use g_threshold(N,d); N is required')
def g_threshold(N:int,d:int=4)->float: return math.sqrt(32.0*(d-1)/N)
def main():
    RES.mkdir(exist_ok=True); rows=[]
    for N in range(2,9):
        gt=g_threshold(N,4)
        for g in (gt*1.01,gt*1.25,max(8.0,gt*1.5)):
            beta=beta_shen(N,g); ks=K_S(N,4,g)
            rows.append({'group':f'SU({N})','N':N,'d':4,'g':g,'beta_shen':beta,'beta_threshold':1/48,'strong_coupling_condition':beta<1/48,'K_S':ks,'admissible_uniform_Hessian_perturbation_epsilon_lt':max(0.0,ks)})
    with open(RES/'strong_coupling_endpoint.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    su3_thr=g_threshold(3,4)
    cert={'theorem_external':'Shen-Zhu-Zhu strong-coupling SU(N) lattice Yang-Mills','their_action':'S=N beta Re sum_p Tr(Q_p)','their_condition_d4':'|beta|<1/48','wilson_mapping':'N beta = beta_W/N = 2/g^2, so beta=2/(N g^2)','SU3_standard_g_threshold':su3_thr,'SU3_threshold_squared':su3_thr**2,'SU3_g8_KS':K_S(3,4,8.0),'stability_lemma':'If an added C2 effective interaction Phi has Hess Phi >= -epsilon I uniformly in volume, Bakry-Emery curvature remains >= K_S-epsilon. Thus epsilon<K_S preserves the finite-volume LSI/Poincare constant uniformly in volume.','SU3_g8_epsilon_margin':K_S(3,4,8.0)}
    (RES/'strong_coupling_endpoint_certificate.json').write_text(json.dumps(cert,indent=2)); print(json.dumps(cert,indent=2))
if __name__=='__main__': main()
