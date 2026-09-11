# Referee Audit — Jaffe–Witten v6

## Exact purpose

This release takes the eight v4 `OPEN_*` rows and resolves their logical dependency structure against the Jaffe–Witten specification. The eight rows no longer represent eight independent mathematical obligations. They reduce to two atomic uniform estimates.

## Closed reduction theorems

The package proves the following implications directly.

1. **Thermodynamic local-state compactness.** For a fixed regulator, compact local gauge configuration spaces and compatible local state restrictions admit thermodynamic subsequential limits on the quasi-local cylinder algebra.
2. **Inductive holonomy state.** Consistent bounded local cylinder functionals extend along the directed union and admit weak-* accumulation states.
3. **Reflection positivity is limit closed.** If each regulator measure is reflection positive on the positive-time cylinder algebra and the relevant cylinder correlators converge, the limiting functional is reflection positive.
4. **Schwinger compactness.** Uniform Schwartz seminorm bounds on every fixed gauge-invariant source derivative imply distributional subsequential compactness by Alaoglu–Bourbaki/diagonal extraction.
5. **Source analyticity to local fields.** A regulator/volume-uniform analytic source polydisc with bounded connected generator gives factorial connected-field bounds by multivariable Cauchy.
6. **Dense symmetry extension.** Invariance under a dense subgroup plus continuity of the distribution action extends invariance to the full Euclidean group.
7. **Anisotropy insertion criterion.** If the hypercubic-breaking insertion enters as `a^alpha V_aniso` and its connected covariance with every test observable is uniformly bounded, symmetry breaking vanishes as `O(a^alpha)`.
8. **Uniform decay to spectral exclusion.** If a limiting positive spectral measure satisfies `C(t) <= M exp(-m t)` for all `t>=0`, then it has no support in `(0,m)`.
9. **Gap finiteness.** In a nontrivial reconstructed Hilbert space with a unique vacuum and nonnegative self-adjoint Hamiltonian, the bottom of the positive spectrum is finite whenever it is positive.
10. **AF tail summability.** If a localized RG remainder obeys `||R_j|| <= C g_j^p`, `p>2`, and `g_j^{-2} >= g_B^{-2}+2 b0 log(L) j`, then the complete ultraviolet tail is summable with an explicit regulator-independent majorant.
11. **Finite RG crossing.** If `q_k=g_k^{-2}` obeys `q_{k+1} <= q_k-c_G` while `g_k<g_*`, then the trajectory reaches `g_*` in at most `ceil((g_0^{-2}-g_*^{-2})/c_G)` steps.
12. **Terminal perturbation stability.** If the terminal functional inequality has curvature margin `K_G` and the accumulated perturbation Hessian is bounded below by `-epsilon_G I` with `epsilon_G<K_G`, then the terminal margin is at least `K_G-epsilon_G>0`.

## The two atomic estimates

### A1 — Nonperturbative RG corridor

For each fixed compact simple `G`, construct the exact Wilson/heat-kernel RG map on the full gauge field and prove regulator- and volume-independent constants on the intermediate coupling interval such that the trajectory reaches a massive terminal domain. A sufficient scalar certificate is

`q_{k+1} <= q_k - c_G`, `c_G>0`,

through the compact intermediate interval, together with uniform locality and a terminal stability budget `epsilon_G<K_G` (or an equivalent direct transfer/spectral estimate).

### A2 — Source-extended RG uniformity

For every finite family of smeared gauge-invariant curvature polynomials and metric/anisotropy sources, prove a regulator- and volume-independent complex source polydisc and constants `M,R_i,C,p>2` satisfying

`|W_a(J)| <= M`,

and localized source remainders

`||R_j(J)|| <= C g_j^p`,

including the metric/stress-tensor insertion needed for Euclidean covariance and short-distance/OPE identification.

## Exact completion implication

The manuscript proves:

`A1 + A2`

implies construction of a nontrivial OS Schwinger family on `R^4`, OS reconstruction of the physical Hilbert space, local gauge-invariant fields corresponding to renormalized curvature composites, full Euclidean/Poincare symmetry, and

`Spec(H) cap (0,m_G) = empty`, with `0 < m_G < infinity`.

Thus the correct referee target is no longer an eight-row checklist. It is the proof of A1 and A2 with uniform constants and source dictionaries.

## Machine verification

Run:

```bash
python run_all.py
python -m pytest -q
```

Then inspect:

- `results/ATOMIC_PROOF_FRONTIER_v6.json`
- `results/MASTER_VERDICT_v6.json`
- `results/final_verifier_v6.csv`
- `results/jaffe_witten_obligation_ledger_v6.csv`
- `results/balaban_af_bridge_certificate.json`
- `results/strong_coupling_endpoint_certificate.json`
