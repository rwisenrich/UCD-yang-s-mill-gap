#!/usr/bin/env python3
"""Regulator-depth independent asymptotic-freedom summability bounds.

If a UV trajectory obeys
    g_j^{-2} >= g_B^{-2} + c j, c = 2 b0 log L,
then for p>2 the full UV tail obeys an explicit K-independent bound.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results"
GROUPS = {"SU(2)":2,"SU(3)":3,"G2":4,"F4":9,"E6":12,"E7":18,"E8":30}
def b0(CA: float) -> float: return 11.0*CA/(48.0*math.pi**2)
def coupling(j:int,gB:float,CA:float,block_factor:float=2.0)->float:
    c=2.0*b0(CA)*math.log(block_factor); return 1.0/math.sqrt(gB**-2+c*j)
def infinite_tail_bound(gB:float,CA:float,p:float=4.0,block_factor:float=2.0)->float:
    assert p>2 and gB>0 and block_factor>1
    c=2.0*b0(CA)*math.log(block_factor)
    return gB**p+gB**(p-2)/(c*(p/2.0-1.0))
def partial_sum(K:int,gB:float,CA:float,p:float=4.0,block_factor:float=2.0)->float:
    return sum(coupling(j,gB,CA,block_factor)**p for j in range(K+1))
def main():
    RES.mkdir(exist_ok=True); rows=[]
    for name,CA in GROUPS.items():
        for gB in (0.8,1.0,1.2,2.0):
            bound=infinite_tail_bound(gB,CA,4.0,2.0)
            s10=partial_sum(10,gB,CA); s100=partial_sum(100,gB,CA); s10000=partial_sum(10000,gB,CA)
            rows.append({"group":name,"C_A":CA,"b0":b0(CA),"g_B":gB,"p":4,"block_factor":2.0,"sum_K10":s10,"sum_K100":s100,"sum_K10000":s10000,"infinite_bound":bound,"all_partial_below_bound":max(s10,s100,s10000)<=bound+1e-12})
    with open(RES/'af_uv_summability.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    cert={"theorem":"AF ultraviolet remainder summability","hypothesis":"g_j^{-2} >= g_B^{-2}+2 b0 log(L) j, p>2, ||R_j|| <= C_R g_j^p","claim":"sum_j ||R_j|| <= C_R [g_B^p + g_B^(p-2)/(2 b0 log(L)(p/2-1))], independent of UV depth","p4_claim":"sum_j g_j^4 <= g_B^4 + g_B^2/(2 b0 log L)","proof":"monotone integral comparison for f(x)=(g_B^{-2}+cx)^(-p/2)","representative_numeric_checks":len(rows),"checks_pass":all(r['all_partial_below_bound'] for r in rows)}
    (RES/'af_uv_summability_certificate.json').write_text(json.dumps(cert,indent=2)); print(json.dumps(cert,indent=2))
if __name__=='__main__': main()
