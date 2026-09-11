#!/usr/bin/env python3
"""Canonical M1/M2 contracts after v5 gate reduction."""
from __future__ import annotations
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def main():
  RES.mkdir(exist_ok=True)
  rows=[
   {'id':'M1.1','master':'M1_GLOBAL_RG_GAP','quantity':'UV all-field localized RG activity norm','required_bound':'sup_(a,L,k<=kB) ||E_k||_KP <= C_G and locality decay exp(-kappa d)','independence':'C_G,kappa independent of a,L'},
   {'id':'M1.2','master':'M1_GLOBAL_RG_GAP','quantity':'terminal matching norm','required_bound':'epsilon_Hess < K_S(G,beta*) and epsilon_mix < K_mix(G,beta*) OR Schur x0<1 with delta_*>0','independence':'margins independent of a,L'},
   {'id':'M1.3','master':'M1_GLOBAL_RG_GAP','quantity':'physical mass floor','required_bound':'inf_(a,L) m_a,L >= m_G > 0 after terminal matching','independence':'m_G depends on G and renormalized scale, not regulator/volume'},
   {'id':'M2.1','master':'M2_LOCAL_FIELD_CONTINUUM','quantity':'renormalized composite insertions','required_bound':'|S_n,a(P_i;f_i)| <= C_G^n n! prod_i p_N(f_i)','independence':'C_G,N independent of a,L for each finite operator family'},
   {'id':'M2.2','master':'M2_LOCAL_FIELD_CONTINUUM','quantity':'Cauchy/convergence','required_bound':'||S_n,a-S_n,a/2||_(S prime,N) <= C a^alpha','independence':'C,alpha independent of L after thermodynamic passage'},
   {'id':'M2.3','master':'M2_LOCAL_FIELD_CONTINUUM','quantity':'hypercubic anisotropy defect','required_bound':'|S_n,a(Rx)-S_n,a(x)| <= C_R a^alpha for generators/dense set of R in SO(4)','independence':'C_R uniform on compact supports'},
   {'id':'M2.4','master':'M2_LOCAL_FIELD_CONTINUUM','quantity':'short-distance structure','required_bound':'renormalized beta function, stress-tensor Ward identities and OPE coefficients satisfy AF asymptotics','independence':'remainder bounds uniform as a->0'}]
  with open(RES/'master_estimate_contract.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
  out={'M1_GLOBAL_RG_GAP':{'statement':'For each fixed compact simple G, the exact all-field RG from the asymptotically-free Wilson/heat-kernel regulator reaches a volume-uniform massive terminal basin at a fixed physical scale and yields inf_(a,L) gap >= m_G>0.','subestimates':['M1.1','M1.2','M1.3']},'M2_LOCAL_FIELD_CONTINUUM':{'statement':'For every finite family of gauge-invariant curvature differential polynomials, source-extended renormalization produces regulator-uniform tempered-distribution bounds, convergence, O(4) restoration, and the required AF/stress-tensor/OPE short-distance structure.','subestimates':['M2.1','M2.2','M2.3','M2.4']}}
  (RES/'master_estimates.json').write_text(json.dumps(out,indent=2)); print(json.dumps(out,indent=2))
if __name__=='__main__': main()
