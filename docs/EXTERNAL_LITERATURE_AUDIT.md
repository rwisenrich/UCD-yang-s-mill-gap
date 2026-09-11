# External literature audit — v6

## Official specification

Jaffe and Witten require a nontrivial four-dimensional quantum Yang-Mills theory for any compact simple gauge group, with axiomatic properties at least at the Wightman/Osterwalder-Schrader level and a positive finite mass gap. Their problem discussion also calls for local operators corresponding to gauge-invariant curvature differential polynomials, asymptotically-free short-distance behavior, a stress tensor and OPE structure.

## Rigorous ultraviolet side

Balaban's 1987–1989 renormalization-group series develops localized effective actions, coupling renormalization, cluster expansions and large-field R-operation estimates. The abstract of *Large field renormalization II* states that those bounds complete the ultraviolet-stability proof for four-dimensional pure gauge field theories. The v6 AF-tail theorem uses only a source-shaped localized bound `||R_j|| <= C g_j^p` with `p>2`; it then proves ultraviolet-depth summability independently.

Magnen–Rivasseau–Seneor (CMP 155, 1993) construct pure SU(2) Yang-Mills Schwinger functions with a fixed infrared cutoff and no ultraviolet cutoff and verify the associated Slavnov identities nonperturbatively. This is an independent ultraviolet comparison route.

## Rigorous strong-coupling side

Shen–Zhu–Zhu prove for SU(N), under `|beta| < 1/[16(d-1)]` in their normalization, uniqueness of the infinite-volume measure, finite-volume convergence, Poincare/log-Sobolev inequalities and exponential decay for a large observable class. Matching `N beta = 2/g^2` gives the explicit SU(3), d=4 sufficient threshold `g^2>32`. At g=8 the Bakry-Emery margin used by v6 is `K_S=0.75`.

## Positivity/bootstrap lane

Guo–Li–Yang–Zhu (JHEP 2025) derive rigorous convex bounds for SU(3) lattice Yang-Mills loop expectation values from Hermitian positivity, reflection positivity and Schwinger–Dyson loop equations. This provides an independent finite-lattice route for constraining the intermediate-coupling corridor.

## Formal finite-lattice comparison lane

The public David J. Fox Lean repository was inspected as an independent formal-lattice comparison. Its own roadmap explicitly separates its formal lattice lower-bound tower from “YM Surface #1,” the continuum Clay problem, which it marks as open. No continuum theorem is imported from that repository.

## Current mathematical concentration

The published rigorous literature supplies strong control of the ultraviolet end and a rigorous massive strong-coupling endpoint. v6 proves that all intervening compactness, reflection-positivity, spectral-transfer, source-Cauchy and ultraviolet-summability steps can be reduced to two atomic estimates: A1 (the exact nonperturbative RG corridor) and A2 (uniform source-extended RG).
