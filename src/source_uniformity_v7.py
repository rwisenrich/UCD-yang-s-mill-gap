#!/usr/bin/env python3
"""Exact regulator/volume-uniform source theorem for bounded gauge observables.

For a probability state mu and bounded observables O_i with ||O_i||_inf <= B_i,
define F(z)=E_mu exp(sum z_i O_i).  If rho=sum |z_i| B_i < log 2, then
|F(z)-1| <= exp(rho)-1 < 1.  Hence F is zero-free and the branch W=log F
through W(0)=0 is analytic.  Moreover
|W(z)| <= -log(2-exp(rho)).
Cauchy then gives explicit cumulant bounds, uniformly in every regulator and
volume for which the same B_i apply.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'results'

def delta(rho:float)->float:
    if not (0 <= rho < math.log(2)):
        raise ValueError('rho must satisfy 0 <= rho < log 2')
    return math.exp(rho)-1.0

def log_bound(rho:float)->float:
    return -math.log(2.0-math.exp(rho))

def single_variable_cumulant_bound(n:int, r:float, B:float=1.0)->float:
    rho=r*B
    return math.factorial(n)*log_bound(rho)/(r**n)

def multivariable_distinct_bound(radii, bounds):
    rho=sum(r*b for r,b in zip(radii,bounds))
    M=log_bound(rho)
    prod=1.0
    for r in radii: prod*=r
    return M/prod

def main():
    RES.mkdir(exist_ok=True)
    rows=[]
    for nloops in (1,2,4,8,16,32):
        r=0.5/nloops
        rho=nloops*r
        rows.append({
            'observables':nloops,
            'supnorm_each':1.0,
            'radius_each':r,
            'rho_total':rho,
            'log2':math.log(2),
            'zero_free_margin':1-delta(rho),
            'uniform_logZ_bound':log_bound(rho),
            'distinct_mixed_cumulant_bound':multivariable_distinct_bound([r]*nloops,[1.0]*nloops),
            'pass':rho < math.log(2) and 1-delta(rho)>0,
        })
    with open(RES/'bounded_wilson_source_scan_v7.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    cert={
      'theorem':'Uniform zero-free source polydisc for bounded gauge observables',
      'hypotheses':[
        'mu is a probability measure/state',
        'O_i are bounded (possibly regulator-dependent) with ||O_i||_infinity <= B_i uniformly',
        'rho(z)=sum_i |z_i| B_i < log 2'
      ],
      'conclusions':[
        '|E exp(sum z_i O_i)-1| <= exp(rho)-1 < 1',
        'Z(z)/Z(0) is zero-free in rho<log 2',
        'W(z)=log[Z(z)/Z(0)] with W(0)=0 is analytic',
        '|W(z)| <= -log(2-exp(rho))',
        'for multiindex alpha on a polydisc radii r_i: |partial^alpha W(0)| <= alpha! M prod r_i^{-alpha_i}'
      ],
      'proof':'Use |exp X-1| <= exp(|X|)-1, expectation contraction, the disk |F-1|<1, the logarithm power series, and multivariable Cauchy.',
      'wilson_loop_corollary':'For normalized Wilson loop characters O_C=Re chi_R(U_C)/dim R, B_i=1 for every compact G. Therefore every finite Wilson-loop source family has a regulator- and volume-independent zero-free polydisc sum |z_i|<log 2.',
      'status':'THEOREM_CLOSED',
      'checks':len(rows),
      'all_pass':all(r['pass'] for r in rows)
    }
    (RES/'bounded_wilson_source_certificate_v7.json').write_text(json.dumps(cert,indent=2))
    print(json.dumps(cert,indent=2))
if __name__=='__main__': main()
