#!/usr/bin/env python3
from __future__ import annotations
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];RES=ROOT/'results';RES.mkdir(exist_ok=True)
rows=[
 {'id':'JW-00','requirement':'Proof regulator is genuine compact-group lattice gauge theory, not only a finite quantum-link surrogate','formula':'H_link=L2(G); Peter-Weyl H_K -> L2(G)','status':'PASS_CONSTRUCTION','dependency':'peter_weyl_bridge_certificate.json'},
 {'id':'JW-01','requirement':'Compact simple gauge group G and local gauge covariance','formula':'U_xy -> G_x U_xy G_y^-1','status':'PASS_CONSTRUCTION','dependency':'standard Wilson/heat-kernel regulator; SU3 executable check'},
 {'id':'JW-02','requirement':'Gauge-invariant local observables / Gauss-law physical sector','formula':'A_phys=A^G; G_x psi=psi','status':'PASS_CONSTRUCTION','dependency':'native SU3 Gauss reduction + compact-group definition'},
 {'id':'JW-03','requirement':'Positive Euclidean regulator / transfer matrix','formula':'<Theta F F>_a,L >=0','status':'PASS_THEOREM_AT_REGULATOR','dependency':'Wilson reflection positivity (Osterwalder-Seiler); heat-kernel positive-type proof'},
 {'id':'JW-04','requirement':'Independent UV and thermodynamic regulator limits','formula':'a_r=L*/2^r ->0; L_s->infinity','status':'PASS_CONSTRUCTION','dependency':'Gamma_rs and refinement_identity.csv'},
 {'id':'JW-05','requirement':'Local classical Yang-Mills continuum action','formula':'ReTr(I-U_p)=a^4 Tr(F^2)/2+O(a^6)','status':'PASS_LOCAL_ASYMPTOTICS','dependency':'wilson_continuum_scaling.csv'},
 {'id':'JW-06A','requirement':'Asymptotically-free UV trajectory','formula':'g0(a)->0','status':'PASS_PERTURBATIVE_PLUS_BALABAN_SMALL_FIELD_INPUT','dependency':'rg_trajectory.csv; Balaban 1987/88'},
 {'id':'JW-06B','requirement':'All-field nonperturbative RG control from UV to fixed physical block scale','formula':'R^k S_a -> S_LB with uniform polymer bounds','status':'OPEN_BRIDGE_LEMMA','dependency':'large-field/small-field gluing and scale-uniform bounds'},
 {'id':'JW-07A','requirement':'Exact Schur correction has no linear term','formula':'Sigma(E)=B(D-E)^-1 B*','status':'PASS_ALGEBRAIC_THEOREM','dependency':'Schur identity'},
 {'id':'JW-07B','requirement':'Strong-block quadratic contraction basin','formula':'eta_(k+1)<=A eta_k^2/delta*','status':'PASS_ABSTRACT_THEOREM_AND_NUMERIC_CERTIFICATE','dependency':'schur_rg_canonical_certificate.json; locality path count A<=400 under stated extraction norm'},
 {'id':'JW-07C','requirement':'Native/standard Wilson RG enters and remains in certified Schur basin','formula':'exists k0: (eta_k,delta_k,Delta_k) in B_gap for all k>=k0','status':'OPEN_BRIDGE_LEMMA','dependency':'JW-06B + explicit matching of Wilson effective action to Schur extraction norm'},
 {'id':'JW-07D','requirement':'Regulator- and volume-uniform physical spectral gap','formula':'inf_(r,s) gap(H_rs)>=m*>0','status':'DEPENDENT_ON_JW07C','dependency':'JW-07A/B/C'},
 {'id':'JW-07E','requirement':'Rigorous strong-coupling infinite-volume endpoint for SU(N) lattice Yang-Mills','formula':'|beta|<1/[16(d-1)] => unique infinite-volume state + Poincare/LSI + exponential clustering','status':'PASS_EXTERNAL_THEOREM_IN_ITS_NORMALIZATION','dependency':'Shen-Zhu-Zhu arXiv:2204.12737'},
 {'id':'JW-08A','requirement':'Infinite-volume limits of gauge-invariant local expectations for the exact blocked action','formula':'omega_infty(A)=lim_s omega_rs(A)','status':'DEPENDENT_ON_JW07C_AND_JW07E_OR_DIRECT_CLUSTERING','dependency':'match exact blocked action to strong-coupling theorem class, or prove uniform clustering directly'},
 {'id':'JW-08B','requirement':'Continuum Schwinger distributions exist','formula':'S_n=lim_r lim_s S_n^(r,s)','status':'OPEN_CONVERGENCE_LEMMA','dependency':'UV renormalization + composite-operator bounds'},
 {'id':'JW-08C','requirement':'Non-Gaussian/nontrivial continuum state','formula':'S_4^T not identically 0 (or equivalent)','status':'OPEN_PERSISTENCE_LEMMA','dependency':'nonzero connected gauge-invariant continuum correlator'},
 {'id':'JW-08D','requirement':'Local quantum fields corresponding to gauge-invariant curvature polynomials and covariant derivatives','formula':'O_P^(a)=sum_Q Z_PQ(a) P_Q(U)/a^dim(P) -> O_P','status':'OPEN_COMPOSITE_OPERATOR_RENORMALIZATION','dependency':'operator mixing bounds + JW-08B'},
 {'id':'JW-08E','requirement':'Short-distance asymptotic-freedom matching, stress tensor, and OPE structure','formula':'O_P(x)O_Q(0) ~ sum_R C_PQ^R(x,mu,g(mu)) O_R(0); partial^mu T_munu=0','status':'OPEN_SHORT_DISTANCE_STRUCTURE','dependency':'JW-06B + JW-08D + Ward identities'},
 {'id':'JW-09A','requirement':'Reflection positivity survives the limit','formula':'<Theta F F>=lim <Theta F F>_rs >=0','status':'PASS_LIMIT_LEMMA_IF_JW08B','dependency':'JW-03 + convergence'},
 {'id':'JW-09B','requirement':'Euclidean invariance restored','formula':'S_n(Rx_i+a)=S_n(x_i)','status':'OPEN_SYMMETRY_LIMIT_LEMMA','dependency':'rotational restoration / regulator universality'},
 {'id':'JW-09C','requirement':'Regularity, symmetry, clustering OS axioms','formula':'OS0-OS4/appropriate equivalent','status':'OPEN_AXIOM_BOUNDS','dependency':'JW-08 + JW-07D'},
 {'id':'JW-10','requirement':'OS/Wightman reconstruction','formula':'{S_n}->(H,Omega,P_mu,A)','status':'STANDARD_THEOREM_ON_JW09','dependency':'Osterwalder-Schrader reconstruction'},
 {'id':'JW-11','requirement':'Nontrivial relativistic Yang-Mills theory on R4','formula':'connected gauge-invariant scattering/correlator sector nonzero','status':'DEPENDENT_ON_JW08C_JW10','dependency':'JW-08C + reconstruction'},
 {'id':'JW-12A','requirement':'Continuum spectral exclusion','formula':'Spec(H) cap (0,m*)=empty','status':'PASS_SPECTRAL_TRANSFER_LEMMA_IF_JW07D_JW08_JW09','dependency':'positive spectral measure + uniform exponential decay'},
 {'id':'JW-12B','requirement':'Finite positive mass parameter','formula':'0<Delta<infinity','status':'DEPENDENT_ON_JW12A_AND_NONTRIVIAL_SPECTRAL_SUPPORT','dependency':'JW-11 + local finite-energy excitation'},
 {'id':'JW-13','requirement':'Extension from SU3 executable representative to arbitrary compact simple G','formula':'C2(R)>0; Peter-Weyl; positive heat kernel; same closure estimates','status':'OPEN_UNIFORM_GROUP_GENERALIZATION','dependency':'group-uniform construction of JW-06B/JW-07C/JW-08 for each compact simple G'},
]
with open(RES/'jaffe_witten_obligation_ledger_v4.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
closed=[r['id'] for r in rows if r['status'].startswith('PASS')]
openids=[r['id'] for r in rows if r['status'].startswith('OPEN')]
dep=[r['id'] for r in rows if r['status'].startswith('DEPENDENT')]
critical=['JW-06B','JW-07C','JW-08B','JW-08C','JW-08D','JW-08E','JW-09B','JW-09C','JW-13']
out={'release':'v4.0','closed_or_conditional_theorems':closed,'open_primary_lemmas':openids,'dependent_conclusions':dep,'critical_path':critical,
     'shortest_SU3_chain':['JW-06B','JW-07C','JW-07D','JW-08A','JW-08B','JW-08C','JW-08D','JW-08E','JW-09B','JW-09C','JW-10','JW-11','JW-12A','JW-12B'],
     'definition_of_completion':'All primary lemmas on the critical path are promoted to proved theorems with constants independent of regulator and volume; then JW-10/11/12 follow.'}
with open(RES/'PROOF_GRAPH_v4.json','w') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
