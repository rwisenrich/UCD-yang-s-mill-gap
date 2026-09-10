import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from native_su3_block import link_verification,h_block,gap,schur_audit,spectral_parent_audit
from jw_verifier import transfer_matrix_certificate,reflection_pushforward_certificate,spectral_correlator_certificate

def test_native_su3():
    x=link_verification(); assert x['left_right_covariance_residual']<1e-12; assert x['fundamental_casimir_residual']<1e-12

def test_block_and_schur():
    H,*_=h_block(1.2,0.05,1.0); d,_=gap(H); assert d>3
    assert max(x['schur_eigen_residual'] for x in schur_audit())<1e-10
    assert spectral_parent_audit()['single_block_projector_domination']

def test_transfer_and_reflection():
    t=transfer_matrix_certificate(); assert t['positive_self_adjoint_transfer']; assert t['gap_residual']<1e-10
    assert reflection_pushforward_certificate(trials=20)['pass']

def test_correlator():
    c=spectral_correlator_certificate(); assert c['nontrivial_probe_weight']; assert c['max_exponential_bound_violation']<1e-10
