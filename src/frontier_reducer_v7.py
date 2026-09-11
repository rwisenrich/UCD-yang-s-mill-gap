#!/usr/bin/env python3
"""v7 exact reduction of the remaining Jaffe-Witten quantitative frontier.

The v6 masters A1 and A2 share the same source-extended RG activity. Once the
source family contains z=0, the physical hRpoly estimate is its zero-source
slice while local-field/OPE estimates are source derivatives. Therefore these
are one all-field source theorem plus one compact intermediate-coupling progress
theorem.
"""
from __future__ import annotations
import json,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'

def main():
    RES.mkdir(exist_ok=True)
    closed={
      'V7-T17':'bounded Wilson-source zero-free polydisc and cumulant bounds',
      'V7-T18':'pointwise exponential activity decay -> weighted polymer norm with explicit entropy threshold',
      'V6-T7-T16':'state/distribution compactness, RP closure, dense symmetry extension, AF-tail summability, terminal stability, spectral transfer'
    }
    frontier={
      'E1_SOURCE_EXTENDED_ALL_FIELD_RG':{
        'statement':'For each fixed compact simple G and each finite family of gauge-invariant curvature/metric sources, construct the exact 4D Wilson/heat-kernel RG activity R_{k,z}(X) on a regulator/volume-independent source polydisc, including small- and large-field regions, with source-to-physical norm dictionary and localized power decay uniform in RG depth.',
        'sufficient_form':'There exist R_i>0, B_G,C_G,kappa_G>0 and p>2, independent of regulator depth and volume, such that for |z_i|<R_i: |log Z_{a,L}(z)/Z_{a,L}(0)|<=M_G on the required finite source family and |R_{k,z}(X)|<=B_G g_k^p exp(-kappa_G d_k(X)); source derivatives/metric insertions obey the same localized majorant after the prescribed finite renormalizations.',
        'zero_source_slice':'z=0 is the physical hRpoly/all-field activity estimate needed by A1.',
        'source_derivative_slice':'Cauchy derivatives give the local curvature fields, metric/stress tensor, anisotropy insertions and AF/OPE remainder bounds needed by A2.',
        'generic_consumers_already_closed':'AF-tail summability, polymer-norm conversion, Schwinger compactness, RP closure, dense symmetry extension and spectral transfer are separate proved lemmas.'
      },
      'E2_INTERMEDIATE_RG_PROGRESS':{
        'statement':'On the compact coupling interval between the rigorously controlled asymptotically-free weak-coupling domain and a rigorously controlled massive terminal domain, prove a regulator/volume-independent RG progress inequality.',
        'sufficient_form':'q_{k+1}<=q_k-c_G for q_k=g_k^{-2} and c_G>0 on the interval, or an equivalent Lyapunov/step-scaling inequality that forces finite entry into the terminal basin while preserving the E1 locality/source bounds.',
        'consumer':'The exact finite-crossing lemma gives a bounded landing time; the terminal Poincare/LSI or Schur basin gives a positive physical decay rate; OS spectral transfer gives Spec(H) cap (0,m_G)=empty.'
      }
    }
    payload={
      'release':'v7.0','closed_new_theorems':closed,'remaining_atomic_estimates':frontier,'count':2,
      'reduction_identity':'E1(z=0)=A1 physical-activity slice; derivatives of E1 in z supply A2 source/composite slice. E2 is the compact intermediate-coupling corridor. Hence E1+E2 implies v6 A1+A2.',
      'completion_chain':'E1 + E2 -> regulator/volume-uniform massive RG flow + local YM Schwinger fields + O(4)/stress tensor/OPE/AF structure -> OS reconstruction -> nontrivial Yang-Mills on R4 -> finite positive Hamiltonian mass gap.',
      'claim_boundary':'No finite-dimensional computation or source transcription is substituted for E1 or E2.'
    }
    (RES/'FINAL_ATOMIC_FRONTIER_v7.json').write_text(json.dumps(payload,indent=2))
    with open(RES/'final_atomic_frontier_v7.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['id','statement','sufficient_form','consumer'])
        for k,v in frontier.items(): w.writerow([k,v['statement'],v['sufficient_form'],v.get('consumer',v.get('generic_consumers_already_closed',''))])
    print(json.dumps(payload,indent=2))
if __name__=='__main__': main()
