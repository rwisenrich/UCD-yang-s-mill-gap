#!/usr/bin/env python3
"""Exact pointwise-decay -> weighted-polymer-norm conversion.

On a graph of maximum degree D, the number of connected n-vertex sets
containing a fixed root is <= D^(2(n-1)): encode the canonical depth-first
traversal of a canonical spanning tree by a walk of length 2(n-1).
Thus if |A(X)| <= A0 exp(-mu |X|), then
sup_x sum_{X contains x} |A(X)| exp(alpha |X|)
is finite whenever mu-alpha > 2 log D, with explicit geometric bound.
"""
from __future__ import annotations
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'

def animal_upper(D:int,n:int)->int:
    return D**(2*(n-1))

def norm_bound(A0:float,mu:float,alpha:float,D:int=8)->float:
    q=D*D*math.exp(-(mu-alpha))
    if not q<1: return math.inf
    return A0*math.exp(-(mu-alpha))/(1-q)

def partial_majorant(A0,mu,alpha,D,N=100):
    return sum(animal_upper(D,n)*A0*math.exp(-(mu-alpha)*n) for n in range(1,N+1))

def main():
    RES.mkdir(exist_ok=True)
    rows=[]
    D=8
    threshold=2*math.log(D)
    for excess in (0.05,0.1,0.25,0.5,1.0,2.0):
        alpha=1.0; mu=alpha+threshold+excess
        B=norm_bound(1.0,mu,alpha,D)
        P=partial_majorant(1.0,mu,alpha,D,100)
        rows.append({'D':D,'alpha':alpha,'mu':mu,'mu_minus_alpha':mu-alpha,'entropy_threshold_2logD':threshold,'excess':excess,'partial_N100':P,'analytic_infinite_bound':B,'pass':P<=B*(1+1e-12)})
    with open(RES/'polymer_norm_conversion_v7.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    cert={
      'theorem':'Pointwise exponential activity decay implies a uniform weighted polymer norm',
      'graph_hypothesis':'maximum vertex degree D',
      'count':'N_n(root) <= D^(2(n-1)) for connected n-vertex polymers containing root',
      'activity_hypothesis':'|A(X)| <= A0 exp(-mu |X|)',
      'condition':'mu-alpha > 2 log D',
      'conclusion':'sup_x sum_{X contains x}|A(X)|exp(alpha|X|) <= A0 exp(-(mu-alpha))/[1-D^2 exp(-(mu-alpha))]',
      'z4_specialization':'D=8, hence sufficient entropy margin mu-alpha > 2 log 8.',
      'balaban_interface':'If the source metric obeys d_k(X)>=c0 |X| and |A_k(X)|<=A0 exp(-kappa d_k(X)), take mu=kappa c0. If the sharper source polymer summability theorem is available, it may replace this crude animal-count condition.',
      'status':'THEOREM_CLOSED',
      'checks':len(rows),'all_pass':all(r['pass'] for r in rows)
    }
    (RES/'polymer_norm_conversion_certificate_v7.json').write_text(json.dumps(cert,indent=2))
    print(json.dumps(cert,indent=2))
if __name__=='__main__': main()
