# UCD Yang-Mills Existence and Mass Gap — Jaffe-Witten v8

Public verification package for Richard Wise's UCD Yang-Mills/Jaffe-Witten construction.

## Canonical proof chain

`compact-group regulator -> source-extended exact RG -> massive physical-scale endpoint -> Schwinger distributions -> OS reconstruction -> continuum Hamiltonian gap`

The continuum regulator is `L^2(G)` per link with Wilson/heat-kernel transfer. The H504 and finite SU(3) quantum-link systems remain exact algebraic workbenches; they are not substituted for the compact-group continuum regulator.

## v8 additions

v8 adds three exact results that tighten the proof interface:

1. **Transfer interlacing with range-density defect**
   `lambda2(T') <= lambda2(T) + epsilon + 2 delta + delta^2`.
2. **Physical generator-gap normalization**
   `m_a = -log(lambda2(T_a))/a`, so the correct uniform continuum condition is `lambda2(T_a) <= exp(-a m_*)`.
3. **Local-curvature source-scaling theorem**
   the elementary bounded-source disc for an `a^-4` normalized local `F^2` operator shrinks like `O(a^4)`, proving that the local-field source sector needs the renormalized all-field RG/cumulant estimate rather than fixed-loop boundedness alone.

## Terminal proof dependency

All generic limit, positivity, compact-group, UV summability, source-Cauchy, polymer-counting, transfer-normalization and spectral-transfer steps have been reduced to two load-bearing regulator/volume-uniform estimates for each fixed compact simple `G`:

- `E1_SOURCE_EXTENDED_ALL_FIELD_RG`
- `E2_INTERMEDIATE_RG_PROGRESS`

Their exact norm statements are in `results/FINAL_ATOMIC_FRONTIER_v7.json` and `docs/V8_TRANSFER_SOURCE_AUDIT.md`.

## Reproduce

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

Current local regression: **33/33 tests PASS**. v6 independent verifier: **9/9 PASS**. v7 terminal-reduction verifier: **7/7 PASS**. v8 transfer/source verifier: **6/6 PASS**.

## Referee entry points

- `paper/UCD_YM_Jaffe_Witten_Submission_v8.md`
- `docs/V8_TRANSFER_SOURCE_AUDIT.md`
- `docs/V7_TERMINAL_REDUCTION.md`
- `docs/JW_GATE_CLOSURE_v6.md`
- `docs/ATOMIC_ESTIMATE_ATTACK_v6.md`
- `results/FINAL_ATOMIC_FRONTIER_v7.json`
- `results/transfer_gap_certificate_v8.json`
- `results/source_scaling_certificate_v8.json`
- `results/final_verifier_summary_v8.json`
