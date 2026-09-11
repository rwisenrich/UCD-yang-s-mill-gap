# Repository Status

## Upload status

**COMPLETE.** The repository has one stable canonical submission surface. No further version-number increments are required for ordinary updates.

Canonical deliverables:

- `paper/UCD_YM_Jaffe_Witten_Submission.md`
- `paper/UCD_YM_Jaffe_Witten_Submission.pdf`
- `paper/UCD_YM_Jaffe_Witten_Submission.docx`
- `docs/ATOMIC_ESTIMATE_ATTACK.md`
- `docs/JW_GATE_CLOSURE.md`
- `docs/REFEREE_AUDIT.md`
- `results/ATOMIC_PROOF_FRONTIER_v6.json`
- `results/PROOF_STATUS_v6.json`
- `results/MASTER_VERDICT_v6.json`
- `results/final_verifier_v6.csv`

The v6-suffixed files are retained as frozen provenance identifiers for the completed build that produced the canonical files above. They are not a signal that another version is planned.

## Reproducibility status

Local clean verification on the frozen build:

- `pytest`: **24/24 PASS**
- independent v6 verifier: **9/9 PASS**
- final meta-verifier: **6/6 PASS**

Run:

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

## Mathematical dependency status

The paper reduces the remaining quantitative Jaffe-Witten burden to the two explicitly named estimates in `results/ATOMIC_PROOF_FRONTIER_v6.json`:

- `A1_NONPERTURBATIVE_RG_CORRIDOR`
- `A2_SOURCE_EXTENDED_RG_UNIFORMITY`

All repository claims should be read against `results/MASTER_VERDICT_v6.json` and the referee audit.
