#!/usr/bin/env python3
"""Exact AF summability bridge for Balaban-type localized remainders."""
from __future__ import annotations
import json, math, csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def bound(gB,b0,L,p,CR=1.0):
    c=2*b0*math.log(L); return CR*(gB**p + gB**(p-2)/(c*(p/2-1)))
def numeric_sum(gB,b0,L,p,J=200000,CR=1.0):
    c=2*b0*math.log(L); inv=gB**-2; return CR*sum((inv+c*j)**(-p/2) for j in range(J))
def main():
    RES.mkdir(exist_ok=True); b0_su3=11*3/(48*math.pi**2); rows=[]
    for gB in (0.25,0.35,0.5):
      for L in (2,3,4):
       for p in (4,6,8,12):
        B=bound(gB,b0_su3,L,p); S=numeric_sum(gB,b0_su3,L,p); rows.append({'G':'SU3','gB':gB,'L':L,'p':p,'partial_sum_200k':S,'analytic_infinite_bound':B,'pass':S<=B})
    with open(RES/'balaban_af_bridge_numeric.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    cert={'theorem':'Localized AF-tail summability bridge','source_shape':'Balaban CMP119 localized remainder has a small-coupling power times exponential localization; the source-to-project norm dictionary must preserve the power/locality bound.','hypotheses':['||R_j||_kappa <= C_R g_j^p with p>2','g_j^{-2} >= g_B^{-2}+2 b0 log(L) j','constants C_R,kappa,p,b0,L independent of ultraviolet depth and volume'],'conclusion':'sum_{j>=0} ||R_j||_kappa <= C_R [g_B^p + g_B^(p-2)/(2 b0 log(L)(p/2-1))].','proof':'Monotone integral comparison of (g_B^{-2}+c x)^(-p/2).','checks':len(rows),'all_pass':all(r['pass'] for r in rows),'meaning':'The infinite number of asymptotically-free UV steps cannot by itself produce a divergent remainder accumulation once the localized source bound is expressed in this norm.'}
    (RES/'balaban_af_bridge_certificate.json').write_text(json.dumps(cert,indent=2)); print(json.dumps(cert,indent=2))
if __name__=='__main__':main()
