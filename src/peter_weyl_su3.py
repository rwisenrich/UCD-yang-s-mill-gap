#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'; RES.mkdir(exist_ok=True)

def dim_irrep(p:int,q:int)->int:
    return (p+1)*(q+1)*(p+q+2)//2

def c2(p:int,q:int)->Fraction:
    return Fraction(p*p+q*q+p*q+3*p+3*q,3)

def fund_tensor(p:int,q:int):
    out=[]
    out.append((p+1,q))
    if p>=1: out.append((p-1,q+1))
    if q>=1: out.append((p,q-1))
    return out

def truncation(K:int):
    irreps=[]; total=0; shell=0
    for n in range(K+1):
        for p in range(n+1):
            q=n-p; d=dim_irrep(p,q); cc=c2(p,q)
            irreps.append({'p':p,'q':q,'dimension':d,'peter_weyl_multiplicity_dimension':d*d,
                           'C2_numerator':cc.numerator,'C2_denominator':cc.denominator,'C2':float(cc)})
            total+=d*d
            if n==K: shell+=d*d
    return irreps,total,shell

def run():
    summary=[]
    for K in range(0,11):
        irr,total,shell=truncation(K)
        summary.append({'K':K,'number_irreps':len(irr),'link_truncation_dimension':total,
                        'top_shell_dimension':shell,'top_shell_fraction':shell/total})
    with open(RES/'peter_weyl_su3_truncations.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=summary[0].keys()); w.writeheader(); w.writerows(summary)
    irr8,_,_=truncation(8)
    with open(RES/'peter_weyl_su3_irreps_K8.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=irr8[0].keys()); w.writeheader(); w.writerows(irr8)
    edges=[]
    K=8
    for row in irr8:
        p,q=row['p'],row['q']
        for pp,qq in fund_tensor(p,q):
            edges.append({'p':p,'q':q,'target_p':pp,'target_q':qq,'inside_K':pp+qq<=K})
    with open(RES/'peter_weyl_fundamental_edges_K8.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=edges[0].keys()); w.writeheader(); w.writerows(edges)
    cert={
      'fundamental':{'p':1,'q':0,'dimension':dim_irrep(1,0),'C2':str(c2(1,0))},
      'antifundamental':{'p':0,'q':1,'dimension':dim_irrep(0,1),'C2':str(c2(0,1))},
      'adjoint':{'p':1,'q':1,'dimension':dim_irrep(1,1),'C2':str(c2(1,1))},
      'truncation_statement':'H_K = direct_sum_{p+q<=K} V_(p,q) tensor V_(p,q)^*. Peter-Weyl gives closure union_K H_K dense in L2(SU3), hence P_K -> I strongly.',
      'electric_statement':'-Delta_SU3 is diagonal on each Peter-Weyl block with eigenvalue C2(p,q), so the first nonzero electric eigenvalue is C_F=4/3.',
      'wilson_multiplication_statement':'Multiplication by a fundamental matrix coefficient maps irrep (p,q) into (p,q) tensor (1,0); projected finite matrices converge strongly on the algebraic Peter-Weyl core because every finite core vector is eventually interior to the cutoff.'
    }
    with open(RES/'peter_weyl_bridge_certificate.json','w') as f: json.dump(cert,f,indent=2)
    print(json.dumps({'certificate':cert,'summary':summary},indent=2))
if __name__=='__main__': run()
