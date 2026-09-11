# UCD Yang-Mills Existence and Mass Gap — Jaffe-Witten Submission

Public verification repository for Richard Wise's UCD Yang-Mills/Jaffe-Witten construction.

This repository is now maintained as **one stable submission surface**. Ordinary updates replace or extend the canonical files; they do not require another version-number increment. The frozen `v6` filenames remain only as provenance for the build that produced the canonical submission.

## Canonical deliverables

- `paper/UCD_YM_Jaffe_Witten_Submission.md`
- `paper/UCD_YM_Jaffe_Witten_Submission.pdf`
- `paper/UCD_YM_Jaffe_Witten_Submission.docx`
- `STATUS.md`
- `docs/ATOMIC_ESTIMATE_ATTACK.md`
- `docs/JW_GATE_CLOSURE.md`
- `docs/REFEREE_AUDIT.md`
- `results/ATOMIC_PROOF_FRONTIER_v6.json`
- `results/PROOF_STATUS_v6.json`
- `results/MASTER_VERDICT_v6.json`
- `results/final_verifier_v6.csv`
- `MANIFEST.sha256`

## Main theorem architecture

`compact-group regulator -> exact RG -> thermodynamic/continuum Schwinger family -> OS reconstruction -> continuum spectral gap`

The proof regulator is `L^2(G)` on every link with Wilson/heat-kernel transfer. H504 and the finite SU(3) quantum-link system are retained as exact algebraic Schur/Feshbach workbenches and are not substituted for the compact-group regulator.

The current manuscript proves the general compactness, reflection-positivity, source-Cauchy, AF-summability, symmetry-extension and spectral-transfer reduction lemmas and isolates the remaining quantitative dependency contract as:

- `A1_NONPERTURBATIVE_RG_CORRIDOR`
- `A2_SOURCE_EXTENDED_RG_UNIFORMITY`

The exact dependency statement is in `results/ATOMIC_PROOF_FRONTIER_v6.json`.

## Reproduce

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

Frozen build verification:

- **24/24 pytest tests PASS**
- **9/9 independent v6 checks PASS**
- **6/6 final meta-verification checks PASS**

## Repository policy

`STATUS.md` is the single current status record. Historical numbered artifacts may remain in Git history, but the canonical files above are the only files a reviewer needs to start from.
