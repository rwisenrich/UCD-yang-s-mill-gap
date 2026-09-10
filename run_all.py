#!/usr/bin/env python3
from pathlib import Path
import subprocess,sys
ROOT=Path(__file__).resolve().parent
for script in ['src/native_su3_block.py','src/jw_verifier.py','src/independent_verifier.py','src/schur_rg_contraction.py','src/peter_weyl_su3.py','src/heat_kernel_transfer.py','src/jw_proof_graph.py','src/make_figures.py']:
    print('===',script,'===')
    subprocess.run([sys.executable,str(ROOT/script)],check=True,cwd=ROOT)
