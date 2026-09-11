# GitHub handoff

This repository is now the canonical public submission surface. No further version-number increment is required for ordinary updates.

## Reproduction

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

Frozen build verification:

- `24/24` pytest tests pass
- `9/9` independent v6 verifier checks pass
- `6/6` final meta-verifier checks pass

## Mathematical dependency frontier

The current manuscript reduces the remaining quantitative dependency contract to two named estimates:

- `A1_NONPERTURBATIVE_RG_CORRIDOR`
- `A2_SOURCE_EXTENDED_RG_UNIFORMITY`

The exact implications and constants demanded by these estimates are specified in `docs/ATOMIC_ESTIMATE_ATTACK.md`, `results/ATOMIC_PROOF_FRONTIER_v6.json`, and `results/MASTER_VERDICT_v6.json`.

## Canonical reviewer files

Start with `STATUS.md`, then `paper/UCD_YM_Jaffe_Witten_Submission.pdf`, then the referee audit and machine-readable ledgers.
