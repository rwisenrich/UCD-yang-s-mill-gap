import math,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/'src'))
from transfer_gap_v8 import interlacing_upper,physical_mass,transfer_lambda
from source_scaling_v8 import zero_free_radius
def test_transfer_generator_identity():
  for a in [1,.5,.1,.01]: assert abs(physical_mass(a,transfer_lambda(a,.7))-.7)<1e-12
def test_transfer_interlacing_zero_defect(): assert interlacing_upper(.4,0,0)==.4
def test_transfer_interlacing_positive_defects(): assert abs(interlacing_upper(.4,.01,.02)-(.4+.01+.04+.0004))<1e-15
def test_local_source_radius_collapses():
  r1=zero_free_radius(2*(.5)**-4); r2=zero_free_radius(2*(.25)**-4); assert r2<r1 and abs((r2/r1)-(.25/.5)**4)<1e-14
