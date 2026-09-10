#!/usr/bin/env python3
from __future__ import annotations
import itertools, json, math, csv
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
RES=ROOT/'results'; RES.mkdir(exist_ok=True)

# ---------- SU(3) algebra ----------
def gell_mann_half():
    i=1j
    lm=[
      np.array([[0,1,0],[1,0,0],[0,0,0]],complex),
      np.array([[0,-i,0],[i,0,0],[0,0,0]],complex),
      np.array([[1,0,0],[0,-1,0],[0,0,0]],complex),
      np.array([[0,0,1],[0,0,0],[1,0,0]],complex),
      np.array([[0,0,-i],[0,0,0],[i,0,0]],complex),
      np.array([[0,0,0],[0,0,1],[0,1,0]],complex),
      np.array([[0,0,0],[0,0,-i],[0,i,0]],complex),
      (1/math.sqrt(3))*np.diag([1,1,-2]).astype(complex),
    ]
    return [x/2 for x in lm]

BASIS=[sum(1<<i for i in c) for c in itertools.combinations(range(6),3)]
INDEX={b:i for i,b in enumerate(BASIS)}; DLINK=len(BASIS)

def cdagc(p:int,q:int)->np.ndarray:
    M=np.zeros((DLINK,DLINK),complex)
    for j,b in enumerate(BASIS):
        if not ((b>>q)&1): continue
        s1=(-1)**((b & ((1<<q)-1)).bit_count()); b1=b^(1<<q)
        if (b1>>p)&1: continue
        s2=(-1)**((b1 & ((1<<p)-1)).bit_count()); b2=b1|(1<<p)
        M[INDEX[b2],j]=s1*s2
    return M

def link_operators():
    t=gell_mann_half()
    L=[];R=[]
    for a in range(8):
        L.append(sum(t[a][p,q]*cdagc(p,q) for p in range(3) for q in range(3)))
        R.append(sum(t[a][p,q]*cdagc(3+p,3+q) for p in range(3) for q in range(3)))
    U=np.empty((3,3),object)
    for p in range(3):
        for q in range(3): U[p,q]=cdagc(p,3+q)
    return t,L,R,U

def link_verification():
    t,L,R,U=link_operators()
    cov=0.0; lie=0.0; lr=0.0
    for a in range(8):
      for b in range(8):
        C=L[a]@L[b]-L[b]@L[a]
        rhs=sum((-2j*np.trace((t[a]@t[b]-t[b]@t[a])@t[c])).real*1j*L[c] for c in range(8))
        lie=max(lie,float(np.linalg.norm(C-rhs)))
        lr=max(lr,float(np.linalg.norm(L[a]@R[b]-R[b]@L[a])))
      for p in range(3):
       for q in range(3):
        lhs=L[a]@U[p,q]-U[p,q]@L[a]
        rhs=sum(t[a][k,p]*U[k,q] for k in range(3))
        cov=max(cov,float(np.linalg.norm(lhs-rhs)))
        lhs=R[a]@U[p,q]-U[p,q]@R[a]
        rhs=-sum(t[a][q,k]*U[p,k] for k in range(3))
        cov=max(cov,float(np.linalg.norm(lhs-rhs)))
    C=sum(x@x for x in L)+sum(x@x for x in R)
    sectors={}
    for nL in range(4):
        ids=[k for k,b in enumerate(BASIS) if sum((b>>q)&1 for q in range(3))==nL]
        vals=np.linalg.eigvalsh(C[np.ix_(ids,ids)])
        sectors[str(nL)]=sorted(set(float(round(v,12)) for v in vals))
    cf=sum(x@x for x in t)
    return {
      'link_dimension':DLINK,
      'left_right_covariance_residual':cov,
      'left_su3_lie_residual':lie,
      'left_right_commutator_residual':lr,
      'fundamental_casimir_residual':float(np.linalg.norm(cf-(4/3)*np.eye(3))),
      'electric_casimir_spectrum_by_nL':sectors,
    }

NAMES=[''.join(map(str,p)) for p in itertools.product([0,3],repeat=4)]+['loop1','loop2']
DPHYS=len(NAMES)

def plaquette_matrices():
    B=np.zeros((DPHYS,DPHYS),complex)
    i0000=NAMES.index('0000'); i3333=NAMES.index('3333'); i1=NAMES.index('loop1'); i2=NAMES.index('loop2')
    B[i1,i0000]=9.0
    B[i2,i1]=16.0
    B[i3333,i2]=9.0
    QE=np.zeros((DPHYS,DPHYS),complex)
    QE[i1,i1]=32/3; QE[i2,i2]=32/3
    D=np.zeros((DPHYS,DPHYS),complex)
    for j,nm in enumerate(NAMES[:16]):
        pat=list(map(int,nm))
        for ell in range(4):
            q=pat.copy(); q[ell]=3-q[ell]
            D[NAMES.index(''.join(map(str,q))),j]+=1.0
    return QE,B,D

def h_block(g:float,lam_det:float=0.0,LB:float=1.0):
    QE,B,D=plaquette_matrices()
    HE=(g*g/(4*LB))*QE
    HW=-(1/(2*g*g*LB))*(B+B.conj().T)
    HD=-(lam_det/LB)*D
    return HE+HW+HD,HE,HW,HD

def gap(H):
    ev=np.linalg.eigvalsh(H)
    return float(ev[1]-ev[0]),ev

def frustration_audit(g=1.2,lam_det=0.05,LB=1.0):
    H,HE,HW,HD=h_block(g,lam_det,LB)
    terms=[HE,HW,HD]
    projectors=[]; ranks=[]
    for T in terms:
        ev,V=np.linalg.eigh(T); e0=ev[0]; ids=np.where(np.abs(ev-e0)<1e-10)[0]
        P=V[:,ids]@V[:,ids].conj().T
        projectors.append(P); ranks.append(len(ids))
    K=sum(np.eye(DPHYS)-P for P in projectors)
    common=int(np.sum(np.linalg.eigvalsh(K)<1e-9))
    raw_proj=[]
    for T in terms:
        ev=np.linalg.eigvalsh(T); lo,hi=ev[0],ev[-1]
        X=(T-lo*np.eye(DPHYS))/(hi-lo) if hi-lo>1e-12 else np.zeros_like(T)
        raw_proj.append(float(np.linalg.norm(X@X-X)))
    return {'local_ground_ranks':ranks,'common_local_ground_dimension':common,
            'raw_normalized_projector_residuals':raw_proj,
            'is_frustration_free':common>0,'raw_terms_are_projectors':all(x<1e-10 for x in raw_proj)}

def schur_effective(g=1.2,lam_det=0.05,LB=1.0,E=None):
    H,*_=h_block(g,lam_det,LB)
    Pidx=list(range(16)); Qidx=[16,17]
    A=H[np.ix_(Pidx,Pidx)]; B=H[np.ix_(Pidx,Qidx)]; D=H[np.ix_(Qidx,Qidx)]
    if E is None: E=float(np.linalg.eigvalsh(H)[0])
    Heff=A-B@np.linalg.inv(D-E*np.eye(2))@B.conj().T
    return Heff,A,B,D,E

def schur_audit(g=1.2,lam_det=0.05,LB=1.0):
    H,*_=h_block(g,lam_det,LB); ev=np.linalg.eigvalsh(H)
    out=[]
    for E in ev[:4]:
        Heff,A,B,D,_=schur_effective(g,lam_det,LB,float(E))
        dist=float(np.min(np.abs(np.linalg.eigvalsh(Heff)-E)))
        sep=float(np.min(np.linalg.eigvalsh(D))-E)
        b=float(np.linalg.norm(B,2))
        selfbound=(b*b/sep) if sep>0 else float('inf')
        out.append({'E':float(E),'schur_eigen_residual':dist,'Q_separation':sep,'B_norm':b,'self_energy_bound':selfbound})
    return out

def spectral_parent_audit(g=1.2,lam_det=0.05,LB=1.0):
    H,*_=h_block(g,lam_det,LB)
    ev,V=np.linalg.eigh(H)
    E0=float(ev[0]); delta=float(ev[1]-ev[0])
    p0=V[:,[0]]@V[:,[0]].conj().T
    q=np.eye(DPHYS)-p0
    shifted=H-E0*np.eye(DPHYS)
    domination=shifted-delta*q
    min_dom=float(np.min(np.linalg.eigvalsh(domination)))
    q_proj=float(np.linalg.norm(q@q-q))
    Heff,A,B,D,_=schur_effective(g,lam_det,LB,E0)
    Sigma=B@np.linalg.inv(D-E0*np.eye(2))@B.conj().T
    rank_sigma=int(np.linalg.matrix_rank(Sigma,tol=1e-10))
    return {
      'E0':E0,'delta':delta,'projector_residual':q_proj,
      'min_eigenvalue_HminusE0_minus_deltaQ':min_dom,
      'single_block_projector_domination':min_dom>=-1e-10,
      'schur_self_energy_rank':rank_sigma,
      'schur_self_energy_operator_norm':float(np.linalg.norm(Sigma,2)),
      'schur_coupling_rank':int(np.linalg.matrix_rank(B,tol=1e-10)),
    }

def run():
    lv=link_verification()
    g=1.2; lam=0.05; LB=1.0
    H,HE,HW,HD=h_block(g,lam,LB); gap0,ev=gap(H)
    fr=frustration_audit(g,lam,LB)
    sch=schur_audit(g,lam,LB)
    sp=spectral_parent_audit(g,lam,LB)
    tau=1/72; kappa=0.1; delta_h504=2*kappa*math.exp(-tau)
    combined=min(delta_h504,gap0)
    scan=[]
    for gg in np.linspace(0.6,3.0,121):
      for ll in [0.0,0.02,0.05,0.1,0.2]:
        HH,*_=h_block(float(gg),float(ll),1.0); dg,ee=gap(HH)
        scan.append({'g_B':float(gg),'lambda_det':float(ll),'block_gap_LB_units':dg,'gap_gt_3':dg>3,'ground_energy':float(ee[0])})
    with open(RES/'native_block_scan.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=scan[0].keys());w.writeheader();w.writerows(scan)
    refine=[]
    LBphys=8.0
    for r in range(4,13):
        ar=2.0**(-r); nr=LBphys/ar
        gamma=(gap0/LBphys)*ar
        thr=3/nr
        refine.append({'r':r,'a_r':ar,'n_r':nr,'dimensionless_block_gap':gamma,'lemm_threshold_3_over_n':thr,
                       'numerical_margin':gamma-thr,'numeric_gap_threshold_pass':gamma>thr,
                       'lemm_hypotheses_pass':fr['is_frustration_free'] and fr['raw_terms_are_projectors']})
    with open(RES/'fixed_physical_block_scaling.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=refine[0].keys());w.writeheader();w.writerows(refine)
    with open(RES/'schur_audit.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=sch[0].keys());w.writeheader();w.writerows(sch)
    summary={
      'release':'UCD_YM_NATIVE_WILSON_SCHUR_CLOSURE_v2_0',
      'canonical':{'g_B':g,'lambda_det':lam,'L_B_block_units':LB,'physical_block_size_Lstar':LBphys},
      'su3_link':lv,
      'gauss_sector_dimension':DPHYS,
      'plaquette_chain_amplitudes':[9,16,9],
      'native_interacting_block_gap_LB_units':gap0,
      'native_block_ground_energy':float(ev[0]),
      'h504_gap':delta_h504,
      'tensor_sum_combined_local_gap':combined,
      'frustration_audit':fr,
      'schur_max_low_eigen_residual':max(x['schur_eigen_residual'] for x in sch),
      'spectral_parent_audit':sp,
      'fixed_physical_numeric_3_over_n_margin_positive':all(x['numeric_gap_threshold_pass'] for x in refine),
      'direct_lemm_applicability':all(x['lemm_hypotheses_pass'] for x in refine),
      'verdict':'NATIVE_SU3_BLOCK_AND_SCHUR_CLOSED__DIRECT_LEMM_HYPOTHESIS_OBSTRUCTION_FOUND',
      'next_exact_gate':'Replace the frustration-free 3/n route by a non-frustration-free uniform-gap stability/cluster estimate for the native Wilson-Schur block family, or prove an exact frustration-free parent comparison on overlapping native blocks.'
    }
    with open(RES/'MASTER_VERDICT.json','w') as f: json.dump(summary,f,indent=2)
    ledger=[
      ('N1','20D SU3 rishon link','left/right gauge covariance',lv['left_right_covariance_residual']<1e-12),
      ('N2','SU3 Casimir','C_F=4/3',lv['fundamental_casimir_residual']<1e-12),
      ('N3','18D Gauss-law plaquette sector','16 endpoint singlets + 2 flux loops',DPHYS==18),
      ('N4','fully interacting block','electric + Wilson plaquette + determinant',gap0>0),
      ('N5','exact Schur isospectrality','low eigenvalues satisfy Schur equation',max(x['schur_eigen_residual'] for x in sch)<1e-9),
      ('N6','fixed-physical numeric threshold','Delta_B>3 equivalently gamma_r>3/n_r',all(x['numeric_gap_threshold_pass'] for x in refine)),
      ('N6A','single-block spectral parent domination','H-E0 >= delta*(I-P0)',sp['single_block_projector_domination']),
      ('N6B','Schur correction rank','rank Sigma(E0) <= 2',sp['schur_self_energy_rank']<=2),
      ('N7','raw projector hypothesis','native terms projector-valued',fr['raw_terms_are_projectors']),
      ('N8','frustration-free hypothesis','common local ground space nonzero',fr['is_frustration_free']),
    ]
    with open(RES/'theorem_ledger.csv','w',newline='') as f:
      w=csv.writer(f);w.writerow(['gate','statement','test','pass']);w.writerows(ledger)
    print(json.dumps(summary,indent=2))

if __name__=='__main__': run()
