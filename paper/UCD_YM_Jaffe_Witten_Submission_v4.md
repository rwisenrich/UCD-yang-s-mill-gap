---
title: "UCD Yang–Mills Existence and Mass-Gap Construction"
subtitle: "Jaffe–Witten Specification: Compact-Group Regulator, Exact Schur Renormalization, Reflection Positivity, and Spectral Transfer"
author: "Richard Wise"
date: "10 September 2026"
geometry: margin=0.9in
fontsize: 10pt
---

# Abstract

The Yang–Mills existence and mass-gap problem requires, for a compact simple gauge group $G$, a nontrivial quantum Yang–Mills theory on $\mathbb R^4$ with a physical Hamiltonian whose spectrum has a strictly positive interval above the vacuum containing no spectrum. This manuscript places the UCD construction directly into the Jaffe–Witten proof architecture.

The proof regulator is the standard compact-group lattice gauge system with link Hilbert space $L^2(G)$, gauge-invariant plaquette action, positive transfer structure, and independent ultraviolet and thermodynamic limits. For $SU(3)$ the Peter–Weyl decomposition

$$
L^2(SU(3))=\widehat\bigoplus_{p,q\ge0}V_{p,q}\otimes V_{p,q}^*
$$

gives a controlled finite-matrix verification hierarchy. The previously constructed 20-dimensional UCD quantum-link block is retained as an independent finite algebraic workbench; it is not substituted for $L^2(SU(3))$ in the continuum proof.

The manuscript proves an exact quadratic Schur-stability theorem. If the eliminated spectral sector has scale-uniform separation $\delta_*>0$ and the local interface norm is $\eta_k$, then exact Feshbach reduction generates no term linear in the eliminated coupling and a local two-step path count $A$ gives

$$
\eta_{k+1}\le {\frac{A}{\delta_*}}\eta_k^2.
$$

For $x_0=A\eta_0/\delta_*<1$ this yields double-exponential contraction and the summable self-energy bound

$$
\sum_{k\ge0}\|\Sigma_k\|
\le
{\frac{\delta_*}{A^2}}{\frac{x_0^2}{1-x_0^2}}.
$$

Consequently an initial spectral gap $\Delta_0$ survives all subsequent exact Schur steps whenever

$$
\Delta_0>
{\frac{2\delta_*}{A^2}}{\frac{x_0^2}{1-x_0^2}}.
$$

The 4-dimensional hypercubic plaquette overlap graph has degree at most $20$ through shared links, giving the conservative ordered two-step path majorant $A\le400$. The executable UCD $SU(3)$ block provides a numerical stress certificate for this theorem with $x_0=0.3294450611$ and a positive infinite-step gap floor $0.09985923249$ in the specified strong-block test point.

The remaining Jaffe–Witten chain is formulated as explicit lemmas: all-field UV-to-block renormalization control, entrance of the standard Wilson/heat-kernel regulator into the Schur gap basin, convergence and nontriviality of the gauge-invariant Schwinger family, restoration of Euclidean symmetry, Osterwalder–Schrader reconstruction, and spectral-gap transfer. The package includes executable tests, machine-readable proof dependencies, Peter–Weyl truncation data, reflection-positive heat-kernel checks, Wilson continuum scaling, Schur certificates, and independent verification.

# 1. Exact Jaffe–Witten target

Let $G$ be a compact simple Lie group. We seek a quantum gauge theory on $\mathbb R^4$ with Hilbert space $\mathcal H$, vacuum $\Omega$, local gauge-invariant observable algebra $\mathcal A$, translation generators $P_\mu$, positive Hamiltonian $H=P_0$, and

$$
\boxed{\operatorname{Spec}(H)\cap(0,\Delta)=\varnothing}
$$

for some finite $\Delta>0$.

The construction must satisfy axiomatic properties at least as strong as the Wightman/Osterwalder–Schrader formulations used in the Jaffe–Witten specification. In Euclidean form this means constructing gauge-invariant Schwinger distributions $S_n$ with the positivity, covariance, locality/symmetry, regularity, and clustering properties required for reconstruction.

We organize the proof as

$$
\boxed{A\Longrightarrow B\Longrightarrow C\Longrightarrow D}
$$

with:

**A.** a regulator- and volume-uniform positive physical spectral threshold;

**B.** existence of a non-Gaussian Euclidean continuum Yang–Mills state on $\mathbb R^4$;

**C.** Osterwalder–Schrader reconstruction of the physical relativistic theory;

**D.** transfer of the regulator-uniform spectral threshold to the reconstructed Hamiltonian.

# 2. Proof regulator: compact-group lattice Yang–Mills

Let $\Lambda_{a,L}\subset a\mathbb Z^4$ be a periodic hypercubic lattice with physical side $L$. Each oriented edge $e$ carries a group element $U_e\in G$ with $U_{\bar e}=U_e^{-1}$. The Euclidean lattice configuration space is

$$
\mathcal C_{a,L}=G^{E(\Lambda_{a,L})}.
$$

For a vertex gauge transformation $g=(g_x)$,

$$
U_{xy}\mapsto g_xU_{xy}g_y^{-1}.
$$

For an oriented plaquette $p$,

$$
U_p=\prod_{e\in\partial p}U_e,
\qquad
U_p\mapsto g_xU_pg_x^{-1},
$$

so every class function of $U_p$ is gauge invariant.

The Wilson action in a unitary representation $R$ is

$$
S_W(U)=\beta\sum_p\left(1-{\frac{1}{d_R}}\operatorname{Re}\chi_R(U_p)\right).
$$

The finite Euclidean measure is

$$
d\mu_{a,L}(U)=Z_{a,L}^{-1}e^{-S_W(U)}\prod_e dU_e,
$$

where $dU$ is normalized Haar measure. Compactness of $G$ makes every finite-volume integral well-defined.

For transfer-positivity arguments one may equivalently use the heat-kernel plaquette weight

$$
K_t(g)=\sum_{\lambda\in\widehat G}d_\lambda e^{-tC_2(\lambda)}\chi_\lambda(g),
$$

whose character coefficients are strictly positive and obey

$$
K_t*K_s=K_{t+s}.
$$

For any finite collection $g_i\in G$ and coefficients $c_i$,

$$
\sum_{i,j}\bar c_ic_jK_t(g_i^{-1}g_j)
=
\sum_\lambda d_\lambda e^{-tC_2(\lambda)}
\left\|\sum_i c_i\pi_\lambda(g_i)\right\|_{HS}^2
\ge0.
$$

Thus $K_t$ is of positive type for every $t>0$. This is the algebraic core of the positive transfer kernel.

# 3. Hamiltonian regulator and Gauss law

On a spatial lattice, the link Hilbert space is

$$
\mathcal H_e=L^2(G,dU),
$$

and

$$
\mathcal H_\Lambda=\bigotimes_{e\in E(\Lambda)}L^2(G).
$$

Left and right regular actions implement local color rotations. The gauge-invariant physical space is

$$
\mathcal H_\Lambda^{\mathrm{phys}}
=
\{\psi: G_x\psi=\psi\ \forall x\}.
$$

A Kogut–Susskind-type Hamiltonian is

$$
H_{a,L}
=
{\frac{g_0(a)^2}{2a}}\sum_e(-\Delta_G)_e
+
{\frac{1}{2g_0(a)^2a}}\sum_p
\left(2d_R-\chi_R(U_p)-\overline{\chi_R(U_p)}\right).
$$

Both terms are gauge invariant. The electric operator is positive. The magnetic bracket is nonnegative because $|\chi_R(U)|\le d_R$.

# 4. Peter–Weyl finite verification hierarchy for SU(3)

The Peter–Weyl theorem gives

$$
L^2(SU(3))
=
\widehat\bigoplus_{p,q\ge0}
V_{p,q}\otimes V_{p,q}^*.
$$

The irreducible representation $(p,q)$ has

$$
d_{p,q}={\frac{(p+1)(q+1)(p+q+2)}{2}}
$$

and quadratic Casimir
$$
C_2(p,q)={\frac{p^2+q^2+pq+3p+3q}{3}}.
$$

Hence

$$
C_F=C_2(1,0)=\frac43,
\qquad
C_A=C_2(1,1)=3.
$$

Define the finite Peter–Weyl truncation

$$
\mathcal H_K=
\bigoplus_{p+q\le K}V_{p,q}\otimes V_{p,q}^*.
$$

Then $P_K\to I$ strongly because the algebraic Peter–Weyl sum is dense. The executable dimensions are

$$
1,19,155,805,3136,9996,27468,67320,150645,\ldots
$$

for $K=0,1,\ldots,8$.

Multiplication by a fundamental matrix coefficient obeys the exact tensor rule

$$
(p,q)\otimes(1,0)
=
(p+1,q)\oplus(p-1,q+1)\oplus(p,q-1),
$$

with terms of negative Dynkin label omitted. Therefore, on every finite algebraic Peter–Weyl core vector, $P_KUP_K$ agrees with $U$ for all sufficiently large $K$. This gives a finite-matrix verification route to the genuine $L^2(SU(3))$ link regulator.

# 5. UCD native refinement family

The UCD spatial refinement family is

$$
\Gamma_{r,s}
=
\mathbb Z_{3\,2^{r+s}}
\times
\mathbb Z_{2\,2^{r+s}}
\times
\mathbb Z_{2\,2^{r+s}},
$$

with

$$
a_r=L_*2^{-r}.
$$

The parameter $r$ removes the short-distance regulator; $s$ supplies independent thermodynamic enlargement. A fixed physical block of side $L_B$ contains

$$
n_r={\frac{L_B}{a_r}},
\qquad
n_ra_r=L_B.
$$

The executable refinement ledger verifies this identity exactly in dyadic arithmetic for the tested range.

The finite UCD carrier

$$
\mathcal H_{504}=V_7\otimes\mathbb C[\mathbb Z_3]\otimes\mathbb C[\operatorname{Dic}_6]
$$

has a separately proved ring translation

$$
\Delta_{504}=2\kappa e^{-1/72}.
$$

Its exact Schur inheritance identity

$$
H_{\mathrm{eff}}(z)
=
H_{cc}-H_{c\ell}(H_{\ell\ell}-zI)^{-1}H_{\ell c}
$$

supplies the finite-registry model for information-preserving elimination. This finite H504 gap is not inserted as the continuum Yang–Mills mass; it supplies algebraic Schur structure and a finite-registry sector.

# 6. Local Yang–Mills continuum asymptotics

For a smooth connection, a small plaquette satisfies

$$
U_p
=
\exp\big(a^2F_{\mu\nu}+O(a^3)\big).
$$

After taking the real trace, the linear anti-Hermitian term cancels and

$$
\operatorname{ReTr}(I-U_p)
=
{\frac{a^4}{2}}\operatorname{Tr}(F_{\mu\nu}^\dagger F_{\mu\nu})+O(a^6).
$$

The executable constant-color test uses

$$
U_p=\exp(ia^2X)
$$

and verifies that the scaled density tends to $\frac12\operatorname{Tr}(X^2)$ with the expected $O(a^4)$ remainder in that commuting test.

# 7. Independent finite quantum-link workbench

The finite UCD $SU(3)$ workbench uses

$$
\mathcal H_{\mathrm{link}}=\Lambda^3\mathbb C^6,
\qquad
\dim\mathcal H_{\mathrm{link}}=20,
$$

with

$$
L^a=\sum_{ij}t^a_{ij}c_{L,i}^\dagger c_{L,j},
\quad
R^a=\sum_{ij}t^a_{ij}c_{R,i}^\dagger c_{R,j},
\quad
U_{ij}=c_{L,i}^\dagger c_{R,j}.
$$

The machine verifies left/right $SU(3)$ covariance, $[L^a,R^b]=0$, and

$$
\sum_at^at^a={\frac{4}{3}}I_3
$$

to numerical roundoff. Exact Gauss reduction of one plaquette gives an 18-dimensional gauge-singlet sector.

The finite interacting diagnostic Hamiltonian is

$$
H_B(g,\lambda;L_B)
=
{\frac{g^2}{4L_B}}Q_E
-
{\frac{1}{2g^2L_B}}(B_p+B_p^\dagger)
-
{\frac{\lambda}{L_B}}D.
$$

This block is used to test Schur, spectral-parent, transfer-matrix, and contraction machinery. The continuum proof regulator remains the compact-group $L^2(G)$ system of Sections 2–4.

# 8. Exact Feshbach–Schur theorem

Let a self-adjoint operator be decomposed by complementary projections $P,Q$:

$$
H=
\begin{pmatrix}
A&B\\
B^\dagger&D
\end{pmatrix}.
$$

If $D-E$ is invertible, define

$$
F_E(H)=A-E-B(D-E)^{-1}B^\dagger.
$$

Then

$$
0\in\operatorname{Spec}F_E(H)
\Longleftrightarrow
E\in\operatorname{Spec}H
$$

away from $\operatorname{Spec}D$. Moreover, if

$$
D-E\ge\delta Q,
$$

then

$$
\boxed{
\|B(D-E)^{-1}B^\dagger\|
\le {\frac{\|B\|^2}{\delta}}.
}
$$

The correction is exactly quadratic in the retained–eliminated coupling $B$. There is no first-order Schur self-energy term.

The finite $SU(3)$ workbench verifies the four lowest full eigenvalues against their energy-dependent Schur operators with maximum residual $1.33\times10^{-14}$.

# 9. Quadratic Schur contraction theorem

Consider a sequence of exact block eliminations. At scale $k$, absorb the complete $PHP$ term into the next retained Hamiltonian and write the remaining retained–eliminated coupling as a sum of local interface operators whose local interaction norm is at most $\eta_k$.

Assume:

1. the eliminated sector in the spectral window is separated by
   $$Q(H_k-E)Q\ge\delta_*Q,$$
   with $\delta_*>0$ independent of $k$;
2. a retained local cell participates in at most $A$ ordered two-step paths through one eliminated cell;
3. the next-scale residual interaction norm is defined by summing the norms of local Schur-generated paths touching a fixed retained cell.

Then each two-step term satisfies

$$
\|B_Y(Q(H_k-E)Q)^{-1}B_Z^\dagger\|
\le {\frac{\eta_k^2}{\delta_*}},
$$

and at most $A$ such ordered paths contribute. Therefore

$$
\boxed{
\eta_{k+1}\le {\frac{A}{\delta_*}}\eta_k^2.
}
$$

Set

$$
x_k={\frac{A\eta_k}{\delta_*}}.
$$

Then

$$
x_{k+1}\le x_k^2.
$$

If $0<x_0<1$,

$$
\boxed{x_k\le x_0^{2^k}}
$$

and therefore

$$
\eta_k
\le
{\frac{\delta_*}{A}}x_0^{2^k}.
$$

The $k$th self-energy satisfies

$$
\epsilon_k\le{\frac{\eta_k^2}{\delta_*}}
\le
{\frac{\delta_*}{A^2}}x_0^{2^{k+1}}.
$$

Since $2^{k+1}\ge2(k+1)$,

$$
\sum_{k=0}^\infty x_0^{2^{k+1}}
\le
\sum_{j=1}^\infty x_0^{2j}
=
{\frac{x_0^2}{1-x_0^2}}.
$$

Hence

$$
\boxed{
\sum_{k\ge0}\epsilon_k
\le
{\frac{\delta_*}{A^2}}
{\frac{x_0^2}{1-x_0^2}}.
}
$$

By Weyl's inequality, a perturbation of operator norm $\epsilon$ moves each of the two lowest spectral edges by at most $\epsilon$, so the gap decreases by at most $2\epsilon$. Thus an initial gap $\Delta_0$ satisfies

$$
\boxed{
\Delta_\infty
\ge
\Delta_0-
{\frac{2\delta_*}{A^2}}
{\frac{x_0^2}{1-x_0^2}}.
}
$$

This is a regulator-step-independent sufficient criterion for gap survival through an exact Schur tower.

# 10. Four-dimensional local path constant

On a 4-dimensional hypercubic lattice, a link belongs to

$$
2(d-1)=6
$$

plaquettes. Fix one plaquette. Each of its four boundary links is shared with five other plaquettes. Distinct edge-sharing neighboring plaquettes therefore number at most

$$
D=4(6-1)=20.
$$

An ordered Schur path retained $\to$ eliminated $\to$ retained is bounded by

$$
\boxed{A\le D^2=400.}
$$

This is deliberately a path-count majorant; additional cancellations can only reduce it.

For the finite quantum-link stress point $g=8$, $\lambda=0.05$, $L_B=1$, the machine obtains

$$
\Delta_0=0.09998915391358655,
$$

$$
\eta_0=0.0703125,
$$

$$
\delta_0=170.74167028648398.
$$

Taking the conservative invariant target

$$
\delta_*=\frac12\delta_0=85.37083514324199
$$

and $A=400$ gives

$$
x_0=0.32944506110089744<1,
$$

$$
\sum_k\epsilon_k\le6.496071390629655\times10^{-5},
$$

and

$$
\boxed{
\Delta_\infty\ge0.09985923248577395>0.
}
$$

The corresponding separation floor is

$$
170.74154036505618>\delta_*;
$$

hence the assumed half-separation is self-consistent for this abstract Schur tower.

# 11. Strong-coupling gap basin for the standard compact-group Hamiltonian

For the genuine $L^2(G)$ Hamiltonian, split

$$
H=H_E+V_B.
$$

The unperturbed electric operator is a sum of independent positive group Laplacians. By Peter–Weyl,

$$
-\Delta_G|_{V_\lambda\otimes V_\lambda^*}=C_2(\lambda).
$$
For compact simple $G$, every nontrivial irreducible representation has

$$
C_2(\lambda)>0.
$$

Thus the product electric vacuum is unique and has a local spectral gap. The magnetic plaquette term is a bounded finite-range perturbation because $|\chi_R(U)|\le d_R$. Standard relatively-bounded perturbation theorems for gapped lattice systems therefore give a volume-independent gapped phase whenever the local magnetic interaction is sufficiently small relative to the electric gap. For $SU(3)$ the dimensionless local scale ratio behaves as

$$
{\frac{\|V_p\|}{\Delta_E}}
\lesssim
{\frac{9}{g^4}},
$$

so the large-$g$ region lies in a rigorous gapped strong-coupling basin.

The purpose of Sections 8–10 is to give a UCD-native exact Schur mechanism for maintaining such a basin under subsequent coarse elimination, with explicit summable error control.

# 12. Ultraviolet asymptotic freedom and renormalized trajectory

For pure $SU(N)$,

$$
\mu{\frac{dg}{d\mu}}=-b_0g^3+O(g^5),
\qquad
b_0={\frac{11N}{48\pi^2}}>0.
$$

For $SU(3)$,

$$
b_0={\frac{11}{16\pi^2}}=0.0696583137541\ldots.
$$

At one loop, fixing a block coupling $g_B$ at physical scale $L_B$ gives

$$
{\frac{1}{g_0(a)^2}}
=
{\frac{1}{g_B^2}}
+2b_0\log{\frac{L_B}{a}}.
$$

Thus

$$
g_0(a)\to0
\qquad(a\to0).
$$

The executable trajectory verifies the algebraic round-trip relation to machine precision. Balaban's four-dimensional small-field renormalization construction provides rigorous localized effective actions and coupling-constant renormalization in the weak-coupling ultraviolet regime. The complete Jaffe–Witten bridge is the all-field continuation from that ultraviolet regime into a fixed-physical-scale gapped basin with constants uniform in $a$ and $L$.

We isolate that step as the following lemma.

**Bridge Lemma A (UV-to-gap-basin).** There exist $L_B>0$, $a_0>0$, and regulator couplings $g_0(a)$ for $0<a<a_0$ such that the exact gauge-invariant Wilson/heat-kernel RG map to scale $L_B$ produces an effective Hamiltonian satisfying the hypotheses of Theorem 9 with constants $A,\delta_*,\eta_0,\Delta_0$ independent of $a$ and thermodynamic volume, with

$$
{\frac{A\eta_0}{\delta_*}}<1
$$

and

$$
\Delta_0>
{\frac{2\delta_*}{A^2}}
{\frac{(A\eta_0/\delta_*)^2}{1-(A\eta_0/\delta_*)^2}}.
$$

Once Bridge Lemma A is established, Theorem 9 produces a regulator- and volume-uniform positive spectral threshold $m_*>0$.

# 13. A: regulator-uniform mass gap

Let $P_{0,a,L}$ be the finite-volume vacuum projection. Under Bridge Lemma A and the exact Schur contraction theorem,

$$
H_{a,L}-E_{0,a,L}
\ge
m_*(I-P_{0,a,L})
$$

with one $m_*>0$ independent of sufficiently small $a$ and sufficiently large $L$. Therefore

$$
\boxed{
\inf_{a<a_0,L>L_0}
\left(E_1(a,L)-E_0(a,L)\right)
\ge m_*>0.
}
$$

This is precisely the form of uniform finite-volume gap singled out in the Jaffe–Witten discussion as the spectral input needed for the thermodynamic construction.

# 14. B: infinite-volume local state

For a bounded gauge-invariant observable $A$ supported in a fixed compact physical region $K$, define

$$
\omega_{a,L}(A)
=
\langle\Omega_{a,L},A\Omega_{a,L}\rangle.
$$

A volume-uniform gap and finite-range locality give exponential decay of connected correlations in the Hamiltonian lattice theory. The required thermodynamic theorem is:

**Bridge Lemma B1 (thermodynamic uniqueness and convergence).** For each sufficiently small $a$, the local expectations $\omega_{a,L}(A)$ converge as $L\to\infty$, independently of boundary conditions compatible with the vacuum phase, and the limit obeys a uniform exponential clustering estimate

$$
|\omega_a(AB)-\omega_a(A)\omega_a(B)|
\le C_{A,B}e^{-m_*d(A,B)}.
$$

The quasi-local algebra is the norm closure

$$
\mathcal A_a
=
\overline{\bigcup_{K\Subset\mathbb R^3}\mathcal A_a(K)}.
$$

The thermodynamic state $\omega_a$ is positive and normalized by construction.

# 15. B: continuum Schwinger family

Let $\mathcal O_i^{(a)}(f_i)$ be renormalized gauge-invariant local composite observables smeared with test functions. Define

$$
S_n^{(a)}(f_1,\ldots,f_n)
=
\omega_a\left(
\mathcal O_1^{(a)}(f_1)\cdots\mathcal O_n^{(a)}(f_n)
\right).
$$

The continuum construction requires scale-dependent field/operator renormalizations $Z_{\mathcal O}(a)$ and counterterms fixed by gauge-invariant renormalization conditions.

**Bridge Lemma B2 (continuum convergence).** For every finite collection of gauge-invariant local test observables, the renormalized distributions converge in $\mathcal S'(\mathbb R^{4n})$:

$$
S_n=\lim_{a\to0}S_n^{(a)}.
$$

The bounds are uniform on bounded sets of Schwartz test functions and compatible with the exponential clustering constant $m_*$.

**Bridge Lemma B3 (nontriviality).** At least one connected gauge-invariant continuum distribution is nonzero, equivalently

$$
S_n^T\not\equiv0
$$

for some $n\ge4$, or another equivalent non-Gaussian observable criterion holds.

The finite workbench already contains nonzero connected Wilson spectral weight; B3 is its continuum persistence statement.

# 15.1 Local curvature fields, stress tensor, and short-distance operator structure

The Jaffe–Witten specification requires the continuum theory to contain local gauge-invariant quantum fields corresponding to classical gauge-invariant differential polynomials in the curvature and its covariant derivatives. Let

$$
P(F,DF,D^2F,\ldots)
$$

be such a polynomial of engineering dimension $d_P$. On a lattice, curvature is represented by oriented plaquette combinations. For $SU(N)$ one convenient Lie-algebra-valued representative is

$$
F_{\mu\nu}^{(a)}(x)
=
\frac{1}{2ia^2g_0(a)}
\left[
U_{\mu\nu}(x)-U_{\mu\nu}(x)^\dagger
-\frac{1}{N}\operatorname{Tr}\big(U_{\mu\nu}(x)-U_{\mu\nu}(x)^\dagger\big)I
\right],
$$

and covariant finite differences give approximants to $D_\rho F_{\mu\nu}$. Gauge-invariant lattice composites $P_j^{(a)}$ are then mixed and renormalized by a finite matrix at each engineering dimension,

$$
\mathcal O_P^{(a)}
=
\sum_{j:\,d_j\le d_P}Z_{Pj}(a,\mu)P_j^{(a)}.
$$

The required continuum statement is:

**Bridge Lemma B4 (composite-field convergence).** For every gauge-invariant differential polynomial $P(F,DF,\ldots)$ there is a renormalized lattice approximant $\mathcal O_P^{(a)}$ such that all mixed Schwinger distributions containing finitely many such insertions converge in $\mathcal S'$ as $a\to0$, and the limiting operators transform covariantly under the restored Euclidean group.

The stress tensor is obtained by differentiating an anisotropic/background-metric lattice action with respect to the metric and then renormalizing the finite set of operators allowed by symmetry. Its continuum Ward identity is

$$
\partial^\mu T_{\mu\nu}=0,
$$

and after OS reconstruction

$$
H=\int_{\mathbb R^3}T_{00}(0,\mathbf x)\,d^3x
$$

in the standard quadratic-form sense on the energy domain.

At short distance, asymptotic freedom fixes the ultraviolet coefficients in products of local fields. The required operator-product statement is

$$
\mathcal O_P(x)\mathcal O_Q(0)
\sim
\sum_R C_{PQ}^{\ R}(x,\mu,g(\mu))\mathcal O_R(0),
\qquad |x|\downarrow0,
$$

with $g(\mu)\to0$ as $\mu\to\infty$ and Wilson coefficients having the perturbative asymptotic expansion determined by Yang–Mills renormalization.

**Bridge Lemma B5 (short-distance matching).** The renormalized continuum composite fields of B4 obey the Yang–Mills Ward identities and their short-distance Schwinger distributions have the asymptotic-freedom/OPE singular structure fixed by perturbative renormalization. In particular a conserved renormalized stress tensor exists.

B4 and B5 are the exact operator-theoretic form of the local-field and ultraviolet requirements in the Jaffe–Witten problem statement; they prevent a merely gapped lattice theory from being substituted for four-dimensional quantum Yang–Mills.

# 16. Reflection positivity and passage to the limit

At finite regulator the Wilson approximation is reflection positive; the heat-kernel formulation exhibits positivity directly through nonnegative character coefficients.

Let $F$ be a polynomial in positive-time gauge-invariant smeared observables. Then

$$
\langle\Theta F,F\rangle_{a,L}\ge0.
$$

If Bridge Lemma B2 gives convergence of every correlator entering this finite quadratic form, then

$$
\langle\Theta F,F\rangle
=
\lim_{a\to0}\lim_{L\to\infty}
\langle\Theta F,F\rangle_{a,L}
\ge0.
$$

Therefore reflection positivity is closed under the continuum limit once the Schwinger distributions converge.

The same argument passes permutation symmetry. Translation invariance passes from the translation-invariant regulators. Full Euclidean rotation invariance requires restoration from the hypercubic subgroup:

**Bridge Lemma C1 (Euclidean restoration).** The limiting Schwinger distributions are invariant under $E(4)$ rather than only the hypercubic subgroup, with all Lorentz-breaking irrelevant operators vanishing under the renormalized trajectory.

# 17. C: Osterwalder–Schrader reconstruction

Assume B1–B5 and C1 together with the standard OS regularity bounds. Then the limiting Schwinger family satisfies the reconstruction hypotheses. The OS quotient is formed from positive-time test polynomials by

$$
(F,G)_{OS}=\langle\Theta F,G\rangle,
$$

modulo null vectors and completed to a Hilbert space $\mathcal H$. Euclidean time translations generate a positive contraction semigroup

$$
T(t)=e^{-tH},
\qquad H\ge0.
$$

Spatial translations and rotations continue to unitary operators, analytic continuation produces the Poincaré representation, and the reconstructed local observable fields satisfy the corresponding Wightman-strength axioms.

Thus

$$
\boxed{
\{S_n\}_{n\ge0}
\xrightarrow{OS}
(\mathcal H,\Omega,H,P_\mu,\mathcal A).
}
$$

# 18. D: spectral-gap transfer

For a local gauge-invariant observable $A$ with $\langle\Omega,A\Omega\rangle=0$,

$$
C_A(t)
=
\langle\Omega,Ae^{-tH}A\Omega\rangle
=
\int_{[0,\infty)}e^{-Et}\,d\rho_A(E),
$$

where $\rho_A$ is a positive spectral measure.

If the uniform regulator gap gives

$$
|C_A^{(a,L)}(t)|\le C_Ae^{-m_*t}
$$

with $C_A$ stable under the limits, then

$$
|C_A(t)|\le C_Ae^{-m_*t}.
$$

Suppose $\rho_A([E_1,E_2])>0$ for some

$$
0<E_1\le E_2<m_*.
$$

Then positivity implies

$$
C_A(t)
\ge e^{-E_2t}\rho_A([E_1,E_2]),
$$

which cannot be bounded by $C_Ae^{-m_*t}$ as $t\to\infty$. Hence

$$
\rho_A((0,m_*))=0.
$$

If local gauge-invariant vectors $A\Omega$ are dense in $\Omega^\perp$, then the bounded spectral projection $1_{(0,m_*)}(H)$ vanishes on a dense set and therefore vanishes identically. Thus

$$
\boxed{
\operatorname{Spec}(H)
\subset
\{0\}\cup[m_*,\infty).
}
$$

# 19. Finite upper edge and nontrivial spectral support

The Jaffe–Witten definition also requires the supremal gap parameter to be finite. It is enough to construct one non-vacuum local state of finite energy. For a compactly supported gauge-invariant local operator $A$ in the Hamiltonian form domain,

$$
0<\|(I-P_0)A\Omega\|<\infty,
$$

and

$$
\frac{\langle A\Omega,HA\Omega\rangle}
{\|(I-P_0)A\Omega\|^2}<\infty
$$

places spectrum at finite positive energy. The continuum nontriviality lemma B3 supplies the required non-vacuum local sector.

# 20. Arbitrary compact simple gauge group

The argument above is not special to $SU(3)$ at the structural level. For compact simple $G$:

1. Haar measure exists and is finite.
2. Peter–Weyl gives
   $$
   L^2(G)=\widehat\bigoplus_{\lambda\in\widehat G}V_\lambda\otimes V_\lambda^*.
   $$
3. The Laplace–Casimir eigenvalue obeys $C_2(\lambda)>0$ for every nontrivial irreducible representation.
4. Heat-kernel character coefficients are positive.
5. Wilson/character plaquette observables are local and gauge invariant.
6. The Schur theorem is representation independent.
7. The OS reconstruction and spectral-transfer arguments are group independent.

The group-dependent part is therefore concentrated in the uniform RG estimates of Bridge Lemmas A and B2. A complete “for any compact simple $G$” proof supplies those estimates for each compact simple group, with no requirement that the numerical constant $m_*$ be universal across different groups.

# 21. Positivity-bootstrap cross-check lane

Hermitian positivity, reflection positivity, and Schwinger–Dyson loop equations can be imposed simultaneously on finite sets of Wilson loops. The 2025 $SU(3)$ lattice bootstrap literature demonstrates rigorous expectation-value bounds from these constraints in 2D, 3D, and 4D. In this package that machinery is assigned as an independent finite-regulator cross-check lane:

$$
\text{Wilson loop algebra}
+\text{reflection positivity}
+\text{SD equations}
\Longrightarrow
\text{certified convex feasible region}.
$$

The natural next use is to bound the renormalized block parameters $(\eta_k,\delta_k,\Delta_k)$ entering Bridge Lemma A rather than merely bound the plaquette expectation.

# 22. Machine-verifiable results

The package runs the following independent checks:

- $SU(3)$ left/right covariance and fundamental Casimir;
- exact 18-dimensional finite Gauss-sector construction;
- positive interacting finite-workbench block gap;
- low-spectrum Feshbach–Schur isospectrality;
- exact spectral-parent inequality;
- positive self-adjoint transfer matrix and transfer-gap identity;
- positive-kernel preservation under coarse pullback;
- nonzero gauge-invariant finite spectral weight and exponential spectral bound;
- Wilson small-plaquette continuum scaling;
- one-loop asymptotically-free trajectory arithmetic;
- exact $SU(3)$ Peter–Weyl dimensions and Casimir values;
- fundamental tensor-product adjacency graph;
- heat-kernel positive coefficients and convolution semigroup coefficients;
- 4D hypercubic overlap/path-count constants;
- quadratic Schur contraction and infinite-step gap-floor certificate.

The current automated test suite returns **10/10 tests passed**. The prior independent finite-block verifier returns **11/11 checks passed**.

# 23. Jaffe–Witten proof ledger

The machine-readable file `results/jaffe_witten_obligation_ledger_v4.csv` maps every theorem to its dependencies. The shortest remaining $SU(3)$ proof chain is:

$$
\boxed{
\begin{aligned}
&\text{all-field UV RG control}\\
&\Downarrow\\
&\text{entry into the exact Schur gap basin}\\
&\Downarrow\\
&\inf_{a,L}\Delta(a,L)=m_*>0\\
&\Downarrow\\
&\text{thermodynamic + continuum Schwinger convergence}\\
&\Downarrow\\
&\text{Euclidean symmetry + OS axioms}\\
&\Downarrow\\
&\text{OS reconstruction}\\
&\Downarrow\\
&\operatorname{Spec}(H)\subset\{0\}\cup[m_*,\infty).
\end{aligned}}
$$

The ledger deliberately separates a theorem already proved in the package, a standard theorem invoked from the literature, and a bridge lemma that must be discharged by the UCD/Wilson construction. That separation is part of the proof object: no finite-matrix eigenvalue is silently relabeled as a continuum mass.

# 24. Reproducibility

Install and run:

```bash
python -m pip install -r requirements.txt
python run_all.py
python -m pytest -q
```

The GitHub Actions workflow runs the same verification on each push and pull request. Every release file is hashed in `MANIFEST.sha256`.

# 25. Conclusion

The Jaffe–Witten problem has been converted into an explicit finite dependency graph. The compact-group proof regulator, gauge symmetry, Gauss sector, local Yang–Mills continuum asymptotics, Peter–Weyl finite verification hierarchy, positive Euclidean transfer structure, exact Feshbach–Schur identity, and a quantitative quadratic Schur gap-stability theorem are all written in one common normalization.

The new quantitative result is the exact summable Schur criterion

$$
\boxed{
\Delta_\infty
\ge
\Delta_0-
{\frac{2\delta_*}{A^2}}
{\frac{(A\eta_0/\delta_*)^2}{1-(A\eta_0/\delta_*)^2}}.
}
$$

This converts the infrared part of the mass-gap problem into measured/derived block constants. The continuum proof then rests on an equally explicit ultraviolet-to-block bridge and continuum Schwinger convergence estimates. Once those bridge lemmas are discharged, the OS and spectral-transfer sections give the required theory on $\mathbb R^4$ and

$$
\boxed{
\operatorname{Spec}(H)\cap(0,\Delta)=\varnothing,
\qquad \Delta>0.
}
$$

# References

1. A. Jaffe and E. Witten, *Quantum Yang–Mills Theory*, in *The Millennium Prize Problems*, Clay Mathematics Institute / American Mathematical Society.
2. K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions I*, Communications in Mathematical Physics 31 (1973).
3. K. Osterwalder and R. Schrader, *Axioms for Euclidean Green's Functions II*, Communications in Mathematical Physics 42 (1975).
4. K. Osterwalder and E. Seiler, *Gauge Field Theories on a Lattice*, Annals of Physics 110 (1978), 440–471.
5. T. Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories I: Generation of Effective Actions in a Small Field Approximation and a Coupling Constant Renormalization in Four Dimensions*, Communications in Mathematical Physics 109 (1987), 249–301.
6. T. Balaban, *Renormalization Group Approach to Lattice Gauge Field Theories II: Cluster Expansions*, Communications in Mathematical Physics 116 (1988), 1–22.
7. T. Balaban, *Convergent Renormalization Expansions for Lattice Gauge Theories*, Communications in Mathematical Physics 119 (1988), 243–285.
8. T. Balaban, *Large Field Renormalization I: The Basic Step of the R Operation*, Communications in Mathematical Physics 122 (1989), 175–202.
9. T. Balaban, *Large Field Renormalization II: Localization, Exponentiation, and Bounds for the R Operation*, Communications in Mathematical Physics 122 (1989), 355–392.
10. D. A. Yarotsky, *Ground States in Relatively Bounded Quantum Perturbations of Classical Lattice Systems*, Communications in Mathematical Physics 261 (2006), 799–819.
11. M. B. Hastings and T. Koma, *Spectral Gap and Exponential Decay of Correlations*, Communications in Mathematical Physics 265 (2006), 781–804.
12. Y. Guo, Z. Li, G. Yang, and G. Zhu, *Bootstrapping SU(3) Lattice Yang–Mills Theory*, JHEP 12 (2025) 033; arXiv:2502.14421.
13. R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That*, Princeton University Press.
14. R. Haag, *Local Quantum Physics*, Springer.
