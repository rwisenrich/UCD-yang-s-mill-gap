# Atomic Estimate Attack — v6

## Objective

The original eight Jaffe–Witten `OPEN_*` rows have been attacked individually and reduced by exact implications. The remaining proof burden is concentrated in two estimates on the genuine compact-link Wilson/heat-kernel regulator.

## A1 — nonperturbative RG corridor

Let `R_k` be an exact gauge-covariant block-spin map from lattice spacing `a_k` to `a_{k+1}=L a_k`, and write the effective action in a local chart as

`S_k = S_YM(g_k) + E_k + sum_X R_k(X)`.

The required uniform corridor consists of constants depending on the fixed compact simple group `G` but not on ultraviolet depth or volume:

`c_G>0`, `K_G>0`, `epsilon_G<K_G`, `mu_G>0`, `C_G<infinity`,

such that, until the strong-coupling terminal threshold `g_*` is reached,

`q_{k+1} <= q_k-c_G`, where `q_k=g_k^{-2}`,

and the polymer/nonlocal tail obeys

`sum_{X contains 0} exp(mu_G diam(X)) ||R_k(X)|| <= C_G g_k^p`, `p>2`.

The AF tail of this estimate is already summable by the v6 theorem. The strong endpoint is supplied by the Shen–Zhu–Zhu criterion. The missing interval is the compact intermediate coupling corridor, not either endpoint.

For SU(3) in four dimensions the rigorous terminal sufficient condition used here is

`g_*^2=32`.

Thus a scalar drift proof gives the explicit landing bound

`N <= ceil((g_0^{-2}-1/32)/c_SU3)`.

At the terminal point, an accumulated effective perturbation with Hessian lower bound `-epsilon I` preserves the endpoint functional-inequality margin when `epsilon<K_S`.

## A2 — source-extended RG uniformity

For a finite family of smeared gauge-invariant local polynomials `P_i(F,DF,...)` and a metric/anisotropy source, define

`Z_a(z)=integral exp[-S_a(U)+sum_i z_i P_{i,a}(U)] dU`,

`W_a(z)=log Z_a(z)`.

The required estimate is a regulator/volume-independent source polydisc

`|z_i|<R_i`,

and constants `M,C,p>2` such that

`|W_a(z)|<=M`

for normalized connected generating functionals on fixed physical supports, while the source-dependent localized RG remainder satisfies

`||R_{j,z}||_mu <= C g_j^p`.

Once this bound is available, multivariable Cauchy gives

`|partial_{z_1}...partial_{z_n}W_a(0)| <= M n! product_i R_i^{-1}`,

uniformly in regulator and volume. Those factorial bounds give the fixed-support distributional compactness required for local quantum fields. The same estimate with the metric source controls the stress tensor and hypercubic anisotropy insertion.

## Literature endpoint audit

Balaban supplies the rigorous weak-coupling ultraviolet RG/stability architecture. Magnen–Rivasseau–Seneor supply an independent ultraviolet construction with a fixed infrared cutoff for SU(2). Shen–Zhu–Zhu supply a rigorous strong-coupling infinite-volume massive endpoint. Osterwalder–Seiler supply lattice reflection positivity. Guo–Li–Yang–Zhu supply independent finite-lattice positivity/Schwinger–Dyson bounds. None of these sources supplies a theorem that spans the complete weak-to-strong compact intermediate interval with the A1 constants, or the full A2 source family with regulator-independent stress-tensor/OPE bounds.

## Exact completion contract

A proof of A1 and A2 closes the dependency graph in `results/ATOMIC_PROOF_FRONTIER_v6.json`. No additional unnamed mathematical gate is introduced by the v6 argument.
