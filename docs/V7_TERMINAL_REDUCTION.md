# Jaffe-Witten terminal reduction v7

v7 adds two exact theorems and then recompresses the remaining proof dependency.

## T17 — bounded Wilson-source theorem

For bounded observables `||O_i||_infty <= B_i`, with `rho=sum |z_i|B_i < log 2`,

`|E exp(sum z_i O_i)-1| <= exp(rho)-1 < 1`.

Therefore the normalized source partition function is zero-free, its logarithm is analytic, and

`|W(z)| <= -log(2-exp(rho))`.

For normalized Wilson characters `B_i=1`, giving the universal domain `sum |z_i| < log 2` independently of regulator and volume.

## T18 — pointwise activity to polymer norm

On maximum-degree `D` graphs, rooted connected `n`-site polymers satisfy

`N_n <= D^(2(n-1))`.

If `|A(X)| <= A0 exp(-mu |X|)`, then for `mu-alpha > 2 log D`,

`sup_x sum_{X contains x}|A(X)|exp(alpha|X|) <= A0 exp(-(mu-alpha))/(1-D^2 exp(-(mu-alpha)))`.

For `Z^4`, `D=8`.

## Final two estimates

**E1_SOURCE_EXTENDED_ALL_FIELD_RG** supplies one exact localized RG activity theorem for the physical 4D compact-group action with curvature/metric sources. Its `z=0` slice is the physical Yang-Mills remainder estimate; its source derivatives generate the local field/stress-tensor/OPE sector.

**E2_INTERMEDIATE_RG_PROGRESS** supplies a regulator/volume-independent Lyapunov or step-scaling inequality on the compact coupling interval between the controlled AF regime and the rigorously massive terminal basin.

The exact implication implemented in the paper is

`E1 + E2 -> A1 + A2 -> OS/Wightman Yang-Mills on R4 with 0 < m_G < infinity`.
