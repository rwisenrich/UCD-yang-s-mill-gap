import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from schur_rg_contraction import quadratic_schur_certificate,critical_A

def test_quadratic_schur_conservative_geometry():
    c=quadratic_schur_certificate(8.0,400.0,delta_fraction=0.5)
    assert c['contraction_condition']
    assert c['Q_separation_self_consistent']
    assert c['positive_gap_floor']
    assert c['certified_gap_floor']>0.0998

def test_quadratic_majorant_decreases():
    c=quadratic_schur_certificate(8.0,400.0,delta_fraction=0.5,steps=6)
    e=[x['eta_majorant'] for x in c['sequence']]
    assert all(e[i+1]<e[i] for i in range(len(e)-1))
