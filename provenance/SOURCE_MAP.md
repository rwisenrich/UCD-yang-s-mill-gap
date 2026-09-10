# Source and provenance map — v4.0

## Native UCD inputs

1. H504 finite Hamiltonian, right-Dic6 equivariance, exact ring-gap theorem, and exact Feshbach-Schur inheritance.
2. Native refinement family `Gamma_(r,s)` with `a_r = L_star / 2^r` and independently increasing thermodynamic volume.
3. Wilson gauge action, exact local gauge covariance, and the small-plaquette `F_{mu nu}^2` expansion.
4. Strong-coupling SU(3) closed-fundamental-flux energy `Delta E_loop = (8/3) g^2/a` in the stated normalization.
5. Infinite quasi-local observable algebra and finite-range compatible dynamics.
6. Continuum spectral-transfer lemma from a uniform positive spectral threshold / exponential Euclidean correlation decay.
7. Native Wilson-Schur v2 workbench: explicit 20D SU(3) quantum-link carrier, 18D Gauss-reduced block, interacting finite spectrum, Schur audit, and spectral-parent inequality.

## v4 architectural correction

The Jaffe-Witten proof regulator is the compact-group link Hilbert space `L^2(G)`, not the finite 20D quantum-link carrier. The quantum-link model remains a finite algebraic stress test. `src/peter_weyl_su3.py` supplies the finite matrix bridge through increasing Peter-Weyl truncations dense in `L^2(SU(3))`.

## External mathematical specification and theorem inputs

- Jaffe-Witten official Yang-Mills Millennium problem statement.
- Osterwalder-Schrader Euclidean reconstruction framework.
- Osterwalder-Seiler lattice-gauge reflection positivity / transfer-matrix framework.
- Balaban four-dimensional lattice-gauge renormalization results for ultraviolet/small-field control.
- Yarotsky-style volume-independent gap stability in sufficiently weak perturbations of a gapped local product phase; used to formalize the strong-coupling basin, not as the UV-to-IR bridge.
- Hastings-Koma spectral-gap/exponential-clustering theorem where local-Hamiltonian hypotheses apply.
- SU(3) positivity-bootstrap bounds (Guo-Li-Yang-Zhu, 2025) as an independent finite-lattice inequality/checking lane.

## Deliberately excluded substitutions

- The historical `Delta_YM=1/9` identification is excluded.
- The H504 finite ring gap is not relabeled as the continuum Yang-Mills mass gap.
- The finite quantum-link block is not relabeled as `L^2(SU(3))`.
- A one-loop beta function is not substituted for the all-field nonperturbative RG bridge.
- A finite-volume numerical gap is not substituted for the regulator- and volume-uniform continuum spectral statement.
