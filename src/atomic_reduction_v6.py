#!/usr/bin/env python3
"""Reduce the five v6 master estimates to two atomic scale-uniform estimates."""
from __future__ import annotations
import json,math,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def main():
    RES.mkdir(exist_ok=True)
    th={'T13_uniform_source_analyticity_to_composite_bounds':{'statement':'Let W_a(J)=log Z_a(J) be analytic for |z_i|<R_i after coupling finitely many smeared gauge-invariant sources J=sum_i z_i P_i(f_i). If |W_a(J)|<=M uniformly in regulator and volume on the source polydisc, then every connected n-point source derivative obeys a regulator/volume-uniform factorial bound.','bound':'|partial_{z1}...partial_{zn} W_a(0)| <= M n! product_i R_i^{-1}','proof':'Multivariable Cauchy integral formula on the source polydisc.'},'T14_anisotropy_from_insertion_bound':{'statement':'For S_a(lambda)=S_a(0)+lambda a^alpha V_aniso and a normalized expectation <O>_lambda, if |Cov_lambda(O,V_aniso)|<=C_O uniformly for lambda in [0,1], then |<O>_1-<O>_0|<=C_O a^alpha.','proof':'Differentiate: d/dlambda <O>_lambda=-a^alpha Cov_lambda(O,V_aniso), then integrate lambda from 0 to 1.'},'T15_finite_RG_crossing_from_inverse_coupling_drift':{'statement':'If q_k=g_k^{-2} obeys q_{k+1}<=q_k-c with c>0 whenever g_k<g_star, then the trajectory reaches g_k>=g_star in at most ceil(max(0,(g_0^{-2}-g_star^{-2})/c)) RG steps.','proof':'Induction gives q_k<=q_0-kc. Choose k so q_k<=g_star^{-2}.'},'T16_AF_remainder_OPE_summability':{'statement':'Any source/OPE RG remainder bounded by C g_j^p in a scale-localized norm with p>2 is summable over an arbitrarily deep asymptotically-free UV tail under g_j^{-2}>=g_B^{-2}+2b0 log(L)j.','bound':'sum_j ||R_j|| <= C[g_B^p+g_B^(p-2)/(2b0 log(L)(p/2-1))]','proof':'Same monotone integral comparison as the Balaban-AF bridge.'}}
    atomic={'A1_NONPERTURBATIVE_RG_CORRIDOR':{'required':'For each fixed compact simple G, prove a regulator/volume-independent exact RG corridor from the AF domain to a massive terminal domain. In a scalar coupling chart it is sufficient to establish q_{k+1}<=q_k-c_G on the compact intermediate interval together with a terminal perturbation norm epsilon_G<K_G and uniform locality.','then':['T15 gives finite landing time','T10 gives terminal functional-inequality margin or the Schur terminal theorem supplies a spectral margin','T8 transfers uniform Euclidean decay to the continuum Hamiltonian gap']},'A2_SOURCE_EXTENDED_RG_UNIFORMITY':{'required':'For every finite family of gauge-invariant curvature/metric source insertions, prove a regulator/volume-independent source polydisc with |W_a(J)|<=M and scale-localized source RG remainders O(g_j^p), p>2, including the anisotropy insertion and metric source.','then':['T13 gives composite-field factorial Schwartz bounds','T7 gives continuum Schwinger subsequences','T14 gives O(4) restoration when the anisotropy coefficient is O(a^alpha)','T16 gives convergent AF/OPE remainder tails','gauge/metric Ward identities give stress tensor and local YM short-distance structure','T12 closes the OS input package']}}
    payload={'new_reduction_theorems':th,'atomic_estimates':atomic,'count':2,'completion_chain':'A1 + A2 -> all v6 M1/M2 components -> OS reconstruction -> nontrivial 4D Yang-Mills -> positive finite mass gap'}
    (RES/'ATOMIC_PROOF_FRONTIER_v6.json').write_text(json.dumps(payload,indent=2))
    rows=[]
    for g0 in [0.2,0.3,0.5,1.0]:
      for c in [0.01,0.03,0.05]:
       gs=math.sqrt(32.0); n=max(0,math.ceil((g0**-2-gs**-2)/c)); q=max(gs**-2,g0**-2-n*c); rows.append({'g0':g0,'g_star':gs,'c':c,'step_bound':n,'q_after_bound':q,'target_q':gs**-2,'theorem_formula_nonnegative':n>=0})
    with open(RES/'rg_crossing_formula.csv','w',newline='') as f:
      w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    print(json.dumps({'atomic_count':2,'new_reduction_theorems':list(th)},indent=2))
if __name__=='__main__':main()
