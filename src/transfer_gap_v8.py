#!/usr/bin/env python3
"""Exact transfer/interlacing and physical-generator-gap theorems."""
from __future__ import annotations
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def interlacing_upper(lambda2:float, eps:float, delta:float)->float: return lambda2+eps+2.0*delta+delta*delta
def physical_mass(a:float,lambda2:float)->float:
    if not (a>0 and 0<lambda2<=1): raise ValueError
    return -math.log(lambda2)/a
def transfer_lambda(a:float,m:float)->float:
    if not (a>0 and m>=0): raise ValueError
    return math.exp(-a*m)
def main():
    RES.mkdir(exist_ok=True); rows=[]
    for a in [1,0.5,0.25,0.125,0.0625,0.03125]:
        m=0.7; lam=transfer_lambda(a,m); raw=1-lam; rec=physical_mass(a,lam)
        rows.append({'a':a,'m_input':m,'lambda2':lam,'raw_transfer_gap':raw,'recovered_mass':rec,'mass_residual':abs(rec-m),'raw_gap_over_a':raw/a})
    with open(RES/'physical_transfer_gap_v8.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    inter=[]
    for lam in [0.2,0.5,0.8]:
      for eps in [0,1e-4,1e-3]:
       for delta in [0,1e-3,1e-2]: inter.append({'lambda2_old':lam,'epsilon_intertwining':eps,'delta_range_density':delta,'lambda2_new_upper':interlacing_upper(lam,eps,delta)})
    with open(RES/'transfer_interlacing_v8.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=inter[0]);w.writeheader();w.writerows(inter)
    cert={'T19':{'name':'Transfer interlacing with range-density defect','hypotheses':['T,Tp self-adjoint contractions with unique vacua Omega,Omegap','J is an isometry and J Omega=Omegap','||Tp J-J T||<=epsilon','for every unit phi perpendicular Omegap there is a unit psi perpendicular Omega with ||phi-J psi||<=delta'],'conclusion':'lambda2(Tp) <= lambda2(T)+epsilon+2 delta+delta^2','proof':'Set x=J psi and e=phi-x. Contractivity gives |<phi,Tp phi>-<x,Tp x>|<=2||e||+||e||^2. Intertwining and isometry give <x,Tp x><=lambda2(T)+epsilon. Take the supremum over phi.'},'T20':{'name':'Physical generator-gap normalization','hypotheses':['T_a=exp(-a H_a)','H_a>=0 with unique vacuum','lambda2(T_a) is the spectral edge on the vacuum-orthogonal sector'],'identity':'m_a=-(1/a) log lambda2(T_a)','uniform_mass_equivalence':'m_a>=m_star iff lambda2(T_a)<=exp(-a m_star)','continuum_scaling':'If m_a->m in (0,infinity), then 1-lambda2(T_a)=a m+o(a).','proof':'Spectral functional calculus and 1-exp(-am)=am+o(a).'},'all_numeric_checks':all(r['mass_residual']<1e-13 for r in rows),'row_count':len(rows)}
    (RES/'transfer_gap_certificate_v8.json').write_text(json.dumps(cert,indent=2)); print(json.dumps(cert,indent=2))
if __name__=='__main__':main()
