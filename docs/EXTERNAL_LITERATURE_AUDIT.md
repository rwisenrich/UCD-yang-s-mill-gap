# External theorem and methods audit

This audit records the external mathematical machinery used or tested against the UCD A→B→C→D Yang–Mills construction. Its purpose is to keep the proof dependencies explicit and prevent a numerical regulator statement from being substituted for a continuum theorem.

## Official target

**Jaffe–Witten, Quantum Yang–Mills Theory.** Target: for any compact simple gauge group G, construct a nontrivial quantum Yang–Mills theory on R^4 with a mass gap Delta > 0, with axiomatic properties at least as strong as the cited constructive/Wightman frameworks. The problem statement also asks for local quantum fields corresponding to gauge-invariant curvature polynomials and their covariant derivatives, with short-distance behavior matching asymptotic freedom and perturbative renormalization, including a stress tensor and OPE structure.

## Regulator positivity and reconstruction

**Osterwalder–Seiler (1978).** Supplies reflection positivity/positive-transfer structure for lattice gauge theory and strong-coupling cluster-expansion control.

**Osterwalder–Schrader (1973, 1975).** Supplies the reconstruction theorem from reflection-positive Euclidean Schwinger functions to a Hilbert-space relativistic QFT once the OS hypotheses are established.

## Ultraviolet renormalization

**Balaban (1987–1989).** Supplies rigorous four-dimensional lattice-gauge renormalization machinery in the ultraviolet/small-field regime, including effective actions, coupling-constant renormalization, cluster expansions, and large-field R-operation estimates. The UCD proof uses this as the rigorous UV input and states the remaining all-field matching to a fixed physical block as Bridge Lemma A.

**Magnen–Rivasseau–Seneor (1993).** Constructed YM4 with an infrared cutoff. This is a comparison point for the ultraviolet construction but does not by itself supply the full R^4 infrared/mass-gap theorem.

## Strong-coupling infrared endpoint

**Shen–Zhu–Zhu, arXiv:2204.12737, revised 2026.** For SU(N) lattice Yang–Mills in their t'Hooft-scaled normalization, |beta| < 1/[16(d-1)] gives uniqueness of the infinite-volume invariant measure, finite-volume convergence, Poincare and logarithmic-Sobolev inequalities, and exponential decay of correlations. In d=4 the explicit sufficient condition is |beta| < 1/48. This supplies a rigorous strong-coupling thermodynamic/mass-gap endpoint once the exact blocked action is matched to the theorem's action class.

**Yarotsky-type gapped-phase stability.** Supplies a second infrared lane for bounded finite-range perturbations of a gapped product phase, subject to its operator hypotheses.

## Correlation and spectral transfer

**Hastings–Koma.** For local Hamiltonian systems under its hypotheses, a spectral gap implies exponential clustering. The submission also proves the converse spectral-exclusion lemma needed after OS reconstruction: a positive spectral measure with a uniform exp(-m t) Euclidean-time bound has no support in (0,m).

## Positivity bootstrap

**Guo–Li–Yang–Zhu (2025), Bootstrapping SU(3) Lattice Yang–Mills Theory.** Hermitian positivity, reflection positivity, and Schwinger–Dyson loop equations generate rigorous finite-lattice convex bounds. This is retained as an independent lane for bounding block observables and, in a future extension, the Schur/RG constants eta, delta, and Delta.

## Public claimed-proof audit

Public repositories and preprints claiming Yang–Mills mass-gap proofs were searched as idea sources. No step from a claimed proof is imported merely because it is public. A claimed theorem can enter the proof graph only after its hypotheses and derivation have been checked independently against the same Jaffe–Witten obligation ledger.

## Result of the audit

The literature supplies rigorous endpoints on both sides of the remaining central bridge: ultraviolet RG control at weak bare coupling and infrared uniqueness/exponential clustering at sufficiently strong lattice coupling. The precise high-leverage theorem is therefore the regulator-uniform all-field matching that carries the exact four-dimensional compact-group blocked action from the asymptotically-free UV regime into a quantitatively certified infrared gap basin while preserving gauge invariance, reflection positivity, locality, and the operator bounds required for continuum Schwinger-function convergence.
