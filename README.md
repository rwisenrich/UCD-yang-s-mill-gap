# UCD Yang-Mills Existence and Mass Gap — Jaffe-Witten v6

Public verification repository for Richard Wise's UCD Yang-Mills/Jaffe-Witten construction.

## Main theorem architecture

The exact regulator-to-QFT chain is organized directly against the Jaffe-Witten specification:

`compact-group regulator -> exact RG -> thermodynamic/continuum Schwinger family -> OS reconstruction -> continuum spectral gap`

The proof regulator is `L^2(G)` on every link with Wilson/heat-kernel transfer. H504 and the finite SU(3) quantum-link model are retained as exact algebraic Schur/Feshbach workbenches; they are not substituted for the compact-group continuum regulator.

v6 proves the general compactness, reflection-positivity, source-Cauchy, AF-summability, symmetry-extension and spectral-transfer lemmas and reduces the entire remaining quantitative burden to two atomic estimates:

- **A1 — nonperturbative RG corridor:** carry the exact compact-group action from the asymptotically-free UV regime into a certified massive terminal basin with regulator- and volume-independent constants.
- **A2 — source-extended RG uniformity:** obtain regulator/volume-independent source analyticity and localized source bounds for gauge-invariant curvature composites, metric/anisotropy insertions, stress tensor and OPE data.

The paper proves `A1 + A2 => nontrivial 4D Yang-Mills + 0 < mass gap < infinity` through the OS reconstruction chain.

## Reproduce

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

Current reproduced regression result: **24/24 tests pass**. The v6 independent verifier returns **9/9 PASS**, and the final meta-verifier returns **6/6 PASS**.

## Referee entry points

- `paper/UCD_YM_Jaffe_Witten_Submission_v6.md`
- `paper/UCD_YM_Jaffe_Witten_Submission_v6.pdf`
- `paper/UCD_YM_Jaffe_Witten_Submission_v6.docx`
- `docs/JW_GATE_CLOSURE_v6.md`
- `docs/ATOMIC_ESTIMATE_ATTACK_v6.md`
- `docs/EXTERNAL_LITERATURE_AUDIT_v6.md`
- `docs/REFEREE_AUDIT_v6.md`
- `results/jaffe_witten_obligation_ledger_v6.csv`
- `results/ATOMIC_PROOF_FRONTIER_v6.json`
- `results/PROOF_STATUS_v6.json`
- `results/MASTER_VERDICT_v6.json`
- `results/final_verifier_v6.csv`
- `MANIFEST.sha256`

## Core code

- `src/native_su3_block.py`
- `src/peter_weyl_su3.py`
- `src/heat_kernel_transfer.py`
- `src/schur_rg_contraction.py`
- `src/af_summability.py`
- `src/strong_coupling_endpoint.py`
- `src/closure_theorems_v6.py`
- `src/balaban_uv_bridge_v6.py`
- `src/atomic_reduction_v6.py`
- `src/final_verifier_v6.py`

See `results/ATOMIC_PROOF_FRONTIER_v6.json` for the exact final dependency contract.
