import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from heat_kernel_transfer import coeff
from peter_weyl_su3 import c2

def test_character_coefficients_and_semigroup():
    for p,q in [(0,0),(1,0),(1,1),(3,2)]:
        c=float(c2(p,q));t=.17;s=.23
        assert coeff(t,c)>0
        assert abs(coeff(t,c)*coeff(s,c)-coeff(t+s,c))<1e-14
