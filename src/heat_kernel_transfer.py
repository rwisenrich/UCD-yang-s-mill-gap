#!/usr/bin/env python3
from __future__ import annotations
import csv,json,math
from pathlib import Path
from peter_weyl_su3 import truncation
ROOT=Path(__file__).resolve().parents[1];RES=ROOT/'results';RES.mkdir(exist_ok=True)

def coeff(t:float,c2:float)->float: return math.exp(-t*c2)

def run():
    irr,_,_=truncation(8)
    rows=[]
    t=0.17;s=0.23
    max_semigroup=0.0;min_coeff=1.0
    for x in irr:
        c=float(x['C2']); a=coeff(t,c); b=coeff(s,c); ab=coeff(t+s,c)
        residual=abs(a*b-ab);max_semigroup=max(max_semigroup,residual);min_coeff=min(min_coeff,ab)
        rows.append({'p':x['p'],'q':x['q'],'C2':c,'k_t':a,'k_s':b,'k_t_times_k_s':a*b,'k_t_plus_s':ab,'semigroup_residual':residual})
    with open(RES/'heat_kernel_semigroup_su3_K8.csv','w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    cert={'t':t,'s':s,'K':8,'all_character_coefficients_positive':all(r['k_t_plus_s']>0 for r in rows),
          'max_character_semigroup_residual':max_semigroup,
          'minimum_character_coefficient':min_coeff,
          'general_positive_type_identity':'sum_ij c_i^* c_j K_t(g_i^-1 g_j) = sum_lambda d_lambda exp(-t C2(lambda)) ||sum_i c_i pi_lambda(g_i)||_HS^2 >= 0',
          'convolution_semigroup':'Fourier coefficient of K_t * K_s is exp(-(t+s)C2(lambda)); hence K_t*K_s=K_(t+s).'}
    with open(RES/'heat_kernel_transfer_certificate.json','w') as f:json.dump(cert,f,indent=2)
    print(json.dumps(cert,indent=2))
if __name__=='__main__':run()
