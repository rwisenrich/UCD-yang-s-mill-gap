# UCD Yang-Mills Jaffe-Witten Submission v4.0

This repository is the public verification repository for Richard Wise's UCD Yang-Mills existence and mass-gap construction.

The manuscript is organized directly against the Jaffe-Witten Millennium specification as four linked stages:

`A -> B -> C -> D`

- **A**: compact-group lattice regulator, gauge-invariant physical sector, reflection-positive transfer structure, and a regulator/volume-uniform spectral-gap theorem.
- **B**: thermodynamic and continuum convergence of gauge-invariant Schwinger functions to a nontrivial Euclidean theory on R^4.
- **C**: Osterwalder-Schrader reconstruction to the physical Hilbert-space/Wightman theory.
- **D**: transfer of the uniform positive spectral threshold to the reconstructed Hamiltonian.

## Proof regulator

The proof regulator is the genuine compact-group lattice gauge Hilbert space

`H_link = L^2(G)`

with Wilson/heat-kernel transfer structure. The finite 20-dimensional SU(3) quantum-link model is retained as an independent algebraic/computational workbench, not substituted for `L^2(SU(3))`.

The finite-to-continuum bridge is explicit through Peter-Weyl truncations

`H_K = direct_sum_{p+q <= K} V_(p,q) tensor V_(p,q)^*`,

whose dimensions increase to the dense Peter-Weyl subspace of `L^2(SU(3))`.

## Reproduce

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

The current regression suite returns **10/10 tests** and the independent finite-block verifier returns **11/11 checks**.

## Main manuscript and proof graph

- `paper/parts/` — canonical manuscript source in ordered parts.
- `docs/REFEREE_AUDIT.md` — referee-facing dependency audit.
- `results/jaffe_witten_obligation_ledger_v4.csv` — line-item Jaffe-Witten obligation ledger.
- `results/PROOF_GRAPH_v4.json` — machine-readable theorem dependency graph.
- `src/schur_rg_contraction.py` — exact Schur quadratic-contraction theorem and certificates.
- `src/peter_weyl_su3.py` — SU(3) Peter-Weyl truncation bridge.
- `src/heat_kernel_transfer.py` — positive heat-kernel transfer/semigroup checks.
- `src/native_su3_block.py` — finite SU(3) algebraic workbench.
- `.github/workflows/verify.yml` — automated reproducibility checks.
- `.github/workflows/build-release.yml` — builds PDF/DOCX, reruns checks, packages and commits release outputs.

## Central theorem chain

For finite regulator Hamiltonians `H_(r,s)`, the target is

`inf_(r,s) gap(H_(r,s)) = m_* > 0`.

After convergence of the reflection-positive Schwinger family and OS reconstruction, the spectral-transfer theorem yields

`Spec(H) intersect (0,m_*) = empty`.

The exact dependency status is recorded in `results/jaffe_witten_obligation_ledger_v4.csv`; no finite-regulator calculation is silently promoted into a continuum theorem.
