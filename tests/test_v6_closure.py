import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def test_v6_theorem_count():
    assert len(json.loads((RES/'closure_theorems_v6.json').read_text()))==6
def test_af_bridge():
    j=json.loads((RES/'balaban_af_bridge_certificate.json').read_text()); assert j['all_pass']
def test_su3_endpoint_margin():
    j=json.loads((RES/'strong_coupling_endpoint_certificate.json').read_text()); assert abs(j['SU3_g8_KS']-.75)<1e-12
def test_five_master_estimates():
    j=json.loads((RES/'PROOF_GRAPH_v6.json').read_text()); assert j['count']==5
def test_no_open_status():
    with open(RES/'jaffe_witten_obligation_ledger_v6.csv') as f: rows=list(csv.DictReader(f))
    assert not any('OPEN' in r['status'] for r in rows)
def test_v6_verifier():
    j=json.loads((RES/'independent_verifier_summary_v6.json').read_text()); assert j['all_pass']
def test_atomic_frontier_two():
    j=json.loads((RES/'ATOMIC_PROOF_FRONTIER_v6.json').read_text()); assert j['count']==2
def test_final_v6_verifier():
    j=json.loads((RES/'final_verifier_summary_v6.json').read_text()); assert j['all_pass']
