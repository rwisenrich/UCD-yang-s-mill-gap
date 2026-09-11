import json, math, csv, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from af_summability import infinite_tail_bound,partial_sum,b0
from strong_coupling_endpoint import beta_shen,K_S,g_threshold
from group_generalization import DATA

def test_af_infinite_tail_dominates_large_partial_sum():
    for CA in [2,3,4,9,12,18,30]:
        B=infinite_tail_bound(1.2,CA,p=4,block_factor=2)
        assert partial_sum(20000,1.2,CA,p=4,block_factor=2) < B

def test_af_b0_positive_for_simple_examples():
    assert all(b0(hv)>0 for _,_,_,hv in DATA)

def test_shen_su3_d4_mapping():
    g=math.sqrt(32.0)
    assert abs(beta_shen(3,g)-1/48)<1e-14
    assert abs(K_S(3,4,g))<1e-13
    assert abs(g_threshold(3,4)-math.sqrt(32.0))<1e-14

def test_strong_endpoint_margin_g8():
    assert abs(K_S(3,4,8.0)-0.75)<1e-14

def test_v5_ledger_has_no_open_star_rows_after_reduction():
    p=ROOT/'results'/'jaffe_witten_obligation_ledger_v5.csv'
    if not p.exists():
        import subprocess
        subprocess.run([sys.executable,str(ROOT/'src'/'jw_gate_reducer_v5.py')],check=True,cwd=ROOT)
    rows=list(csv.DictReader(open(p)))
    assert all(not r['status'].startswith('OPEN_') for r in rows)
    assert any(r['status'].startswith('REDUCED_TO_M1') for r in rows)
    assert any(r['status'].startswith('REDUCED_TO_M2') for r in rows)

def test_two_master_estimates_are_exactly_named():
    p=ROOT/'results'/'master_estimates.json'
    if not p.exists():
        import subprocess
        subprocess.run([sys.executable,str(ROOT/'src'/'master_estimates.py')],check=True,cwd=ROOT)
    d=json.load(open(p))
    assert set(d)=={'M1_GLOBAL_RG_GAP','M2_LOCAL_FIELD_CONTINUUM'}
