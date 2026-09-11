import math,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from source_uniformity_v7 import delta,log_bound,single_variable_cumulant_bound,multivariable_distinct_bound
from polymer_norm_v7 import animal_upper,norm_bound,partial_majorant

def test_zero_free_margin():
    rho=0.5
    assert rho < math.log(2)
    assert delta(rho) < 1
    assert 2-math.exp(rho)>0

def test_log_bound_positive_finite():
    assert 0 < log_bound(0.5) < math.inf

def test_cumulant_bounds_finite():
    assert single_variable_cumulant_bound(6,0.25,1.0)>0
    assert multivariable_distinct_bound([0.1]*4,[1.0]*4)>0

def test_animal_count_base_cases():
    assert animal_upper(8,1)==1
    assert animal_upper(8,2)==64

def test_polymer_geometric_bound():
    D=8; alpha=1; mu=alpha+2*math.log(D)+0.5
    assert partial_majorant(1,mu,alpha,D,100) <= norm_bound(1,mu,alpha,D)*(1+1e-12)
