#!/usr/bin/env python3
from pathlib import Path
import csv, json
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; RES=ROOT/'results'; FIG=ROOT/'figures'; FIG.mkdir(exist_ok=True)
with open(RES/'rg_trajectory.csv') as f: rows=list(csv.DictReader(f))
r=[int(x['r']) for x in rows]; g=[float(x['g0']) for x in rows]
plt.figure(figsize=(7,4)); plt.plot(r,g,marker='o'); plt.xlabel('refinement r'); plt.ylabel('bare coupling g0(a_r)'); plt.title('One-loop asymptotically-free trajectory'); plt.tight_layout(); plt.savefig(FIG/'rg_trajectory.png',dpi=180); plt.close()
with open(RES/'wilson_continuum_scaling.csv') as f: rows=list(csv.DictReader(f))
a=[float(x['a']) for x in rows]; e=[float(x['abs_error']) for x in rows]
pts=[(x,y) for x,y in zip(a,e) if y>1e-15]
plt.figure(figsize=(7,4)); plt.loglog([x for x,y in pts],[y for x,y in pts],marker='o'); plt.xlabel('lattice spacing a'); plt.ylabel('scaled Wilson-density error'); plt.title('Wilson small-plaquette continuum scaling'); plt.tight_layout(); plt.savefig(FIG/'wilson_continuum_scaling.png',dpi=180); plt.close()
with open(RES/'spectral_correlator.json') as f: c=json.load(f)
plt.figure(figsize=(7,4)); plt.semilogy(c['times'],c['connected_correlator'],marker='o',label='exact correlator'); plt.semilogy(c['times'],c['exponential_upper_bound'],linestyle='--',label='spectral bound'); plt.xlabel('Euclidean time'); plt.ylabel('connected correlator'); plt.title('Finite-block gauge-invariant spectral decay'); plt.legend(); plt.tight_layout(); plt.savefig(FIG/'spectral_correlator.png',dpi=180); plt.close()
