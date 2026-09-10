#!/usr/bin/env python3
from __future__ import annotations
import csv, json, math, sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from native_su3_block import h_block, gap, schur_effective
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'results'; RES.mkdir(exist_ok=True)


def block_constants(g:float, lam:float=0.05, LB:float=1.0):
    H,*_=h_block(g,lam,LB)
    Delta,ev=gap(H); E0=float(ev[0])
    _,_,B,D,_=schur_effective(g,lam,LB,E0)
    eta=float(np.linalg.norm(B,2))
    dvals=np.linalg.eigvalsh(D)
    delta=float(np.min(np.abs(dvals-E0)))
    return {'g':g,'lambda':lam,'LB':LB,'E0':E0,'Delta0':Delta,'eta0':eta,'delta0':delta}


def quadratic_schur_certificate(g:float,A:float,lam:float=0.05,LB:float=1.0,
                                delta_fraction:float=1.0,steps:int=12):
    c=block_constants(g,lam,LB)
    eta=c['eta0']; delta0=c['delta0']; Delta0=c['Delta0']
    delta_star=delta_fraction*delta0
    if A<=0 or delta_star<=0: raise ValueError('A and delta_star must be positive')
    x=A*eta/delta_star
    contraction=x<1
    if contraction:
        sum_eps_bound=(delta_star/(A*A))*(x*x/(1-x*x))
        gap_floor=Delta0-2*sum_eps_bound
        sep_floor=delta0-2*sum_eps_bound
        self_consistent=sep_floor>=delta_star
    else:
        sum_eps_bound=float('inf'); gap_floor=float('-inf'); sep_floor=float('-inf'); self_consistent=False
    seq=[]; etak=eta; cumulative=0.0
    for k in range(steps):
        eps=etak*etak/delta_star
        cumulative+=eps
        seq.append({'k':k,'eta_majorant':etak,'self_energy_majorant':eps,'cumulative_self_energy':cumulative})
        etak=A*etak*etak/delta_star
    return {**c,'A':A,'delta_fraction':delta_fraction,'delta_star':delta_star,'x0':x,
            'contraction_condition':contraction,
            'infinite_self_energy_sum_bound':sum_eps_bound,
            'certified_Q_separation_floor':sep_floor,
            'Q_separation_self_consistent':self_consistent,
            'certified_gap_floor':gap_floor,
            'positive_gap_floor':bool(contraction and self_consistent and gap_floor>0),'sequence':seq}


def critical_A(g:float,lam:float=0.05,LB:float=1.0,delta_fraction:float=1.0):
    c=block_constants(g,lam,LB); eta=c['eta0']; delta0=c['delta0']; D=c['Delta0']
    ds=delta_fraction*delta0
    q=2*eta*eta/(ds*D)
    if q>=1: return 0.0
    return (ds/eta)*math.sqrt(1-q)


def run():
    d=4
    Dedge=4*(2*(d-1)-1)
    Atwo=Dedge*Dedge
    geometry={'dimension':d,'plaquette_boundary_links':4,'plaquettes_per_link':2*(d-1),
              'other_plaquettes_per_link':2*(d-1)-1,'edge_overlap_degree':Dedge,
              'ordered_two_step_path_majorant_A':Atwo,
              'derivation':'D=4*(2*(d-1)-1)=20; A=D^2=400 bounds ordered two-step Schur paths per retained plaquette.'}
    scan=[]
    for g in [2.0,2.5,3.0,3.5,4.0,5.0,6.0,7.0,8.0,10.0]:
        ca=critical_A(g,delta_fraction=0.5)
        for A in [20,100,200,400]:
            c=quadratic_schur_certificate(g,A,delta_fraction=0.5)
            scan.append({k:v for k,v in c.items() if k!='sequence'}|{'Acrit_delta_half':ca})
    with open(RES/'schur_rg_quadratic_scan.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=scan[0].keys()); w.writeheader(); w.writerows(scan)
    canonical=quadratic_schur_certificate(8.0,float(Atwo),delta_fraction=0.5)
    canonical['Acrit_delta_half']=critical_A(8.0,delta_fraction=0.5)
    with open(RES/'schur_rg_canonical_certificate.json','w') as f: json.dump(canonical,f,indent=2)
    with open(RES/'hypercubic_overlap_geometry.json','w') as f: json.dump(geometry,f,indent=2)
    print(json.dumps({'canonical':{k:v for k,v in canonical.items() if k!='sequence'},'geometry':geometry},indent=2))

if __name__=='__main__': run()
