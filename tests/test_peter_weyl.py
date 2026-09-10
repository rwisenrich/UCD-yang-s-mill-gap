import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from peter_weyl_su3 import dim_irrep,c2,truncation,fund_tensor

def test_su3_irrep_data():
    assert dim_irrep(1,0)==3 and c2(1,0).numerator==4 and c2(1,0).denominator==3
    assert dim_irrep(1,1)==8 and c2(1,1)==3

def test_peter_weyl_dimensions():
    expected={0:1,1:19,2:155,3:805,4:3136,5:9996,6:27468,7:67320,8:150645}
    for K,v in expected.items(): assert truncation(K)[1]==v

def test_fundamental_tensor_rule_examples():
    assert set(fund_tensor(1,0))=={(2,0),(0,1)}
    assert set(fund_tensor(1,1))=={(2,1),(0,2),(1,0)}
