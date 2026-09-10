# UCD Yang-Mills Existence and Mass-Gap Construction

This repository is the public verification repository for Richard Wise's UCD Yang-Mills/Jaffe-Witten construction.

The project is organized directly against the Jaffe-Witten Millennium problem specification:

`A -> B -> C -> D`

- A: finite gauge regulator plus regulator- and volume-uniform positive spectral threshold
- B: construction of the nontrivial Euclidean continuum theory on R^4
- C: Osterwalder-Schrader reconstruction to the physical Hilbert-space/Wightman theory
- D: transfer of the positive spectral threshold to the continuum Hamiltonian

## Reproduce

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

## Current release

`UCD_YM_JAFFE_WITTEN_SUBMISSION_v3_0`

Key artifacts:

- `paper/UCD_YM_Jaffe_Witten_Submission.md`
- `paper/UCD_YM_Jaffe_Witten_Submission.pdf`
- `paper/UCD_YM_Jaffe_Witten_Submission.docx`
- `src/native_su3_block.py`
- `src/jw_verifier.py`
- `src/independent_verifier.py`
- `results/jaffe_witten_obligation_ledger.csv`
- `results/MASTER_VERDICT.json`
- `.github/workflows/verify.yml`

The full versioned release archive is stored under `release/` and contains the complete executable package, paper, results, figures, provenance, tests, and SHA-256 manifest.
