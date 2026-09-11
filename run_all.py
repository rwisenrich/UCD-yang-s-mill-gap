#!/usr/bin/env python3
import subprocess,sys
SCRIPTS=[
 'src/native_su3_block.py','src/jw_verifier.py','src/independent_verifier.py','src/schur_rg_contraction.py',
 'src/peter_weyl_su3.py','src/heat_kernel_transfer.py','src/af_summability.py','src/strong_coupling_endpoint.py',
 'src/group_generalization.py','src/limit_closure.py','src/master_estimates.py','src/jw_gate_reducer_v5.py',
 'src/independent_verifier_v5.py','src/closure_theorems_v6.py','src/balaban_uv_bridge_v6.py',
 'src/master_reducer_v6.py','src/atomic_reduction_v6.py','src/source_uniformity_v7.py','src/polymer_norm_v7.py',
 'src/frontier_reducer_v7.py','src/independent_verifier_v6.py','src/final_verifier_v6.py',
 'src/build_master_verdict_v6.py','src/final_verifier_v7.py','src/make_figures.py'
]
for s in SCRIPTS:
 print(f'=== {s} ===',flush=True)
 subprocess.run([sys.executable,s],check=True)
