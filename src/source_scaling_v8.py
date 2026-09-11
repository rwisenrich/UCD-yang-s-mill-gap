#!/usr/bin/env python3
"""Exact source-scaling diagnostic for local curvature observables."""
from __future__ import annotations
import csv,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'
def zero_free_radius(Ba:float)->float: return math.log(2)/Ba
def main():
  RES.mkdir(exist_ok=True); rows=[]; C=2.0
  for r in range(1,13):
    a=2.0**(-r); B=C*a**-4; R=zero_free_radius(B); rows.append({'r':r,'a':a,'supnorm_bound_C_a^-4':B,'bounded_source_radius':R,'radius_over_a4':R/a**4})
  with open(RES/'local_curvature_source_scaling_v8.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
  cert={'T21':{'name':'Naive bounded-source radius collapses for local curvature normalization','statement':'If ||O_a||_infinity <= C a^{-d} and bounded-source analyticity is obtained only from |z| ||O_a||_infinity < log 2, the guaranteed source radius is |z| < (log 2) a^d/C and tends to zero.','d4_F2_specialization':'For plaquette representatives of F^2 with a^{-4} normalization, the guaranteed radius is O(a^4). A regulator-uniform local-field source theorem therefore requires renormalization/localization/cumulant control beyond the fixed bounded-Wilson-loop estimate.','proof':'Substitute B_a=C a^{-d} into |z|B_a<log2.'},'numeric_scaling_constant':math.log(2)/C,'all_rows_constant_ratio':max(abs(r['radius_over_a4']-math.log(2)/C) for r in rows)<1e-14}
  (RES/'source_scaling_certificate_v8.json').write_text(json.dumps(cert,indent=2)); print(json.dumps(cert,indent=2))
if __name__=='__main__':main()
