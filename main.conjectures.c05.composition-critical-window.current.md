# C05 - Critical spike response is universal in the derivative topology

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $H_n$ be real symmetric Wigner: independent centered
upper-triangular entries, off-diagonal variance $1/n$, diagonal variance
$2/n$, continuous entry densities, and uniformly bounded moments of every
order after multiplication by $\sqrt n$. Let $u_n$ be deterministic unit
vectors with $\|u_n\|_\infty\le C/\sqrt n$. For real $w$ put
$$F_n(w)=n^{2/3}\big(\lambda_{\max}(H_n+
(1+wn^{-1/3})u_nu_n^T)-2\big).$$
Define $F_n^{\mathrm G}$ identically using GOE.

**Proposal.** For every compact interval $K$, the bounded-Lipschitz distance
between the laws of $F_n$ and $F_n^{\mathrm G}$ in $C^1(K)$ tends to zero.
Here $C^1$ has norm $\sup|F|+\sup|F'|$; exceptional nonsimple spectra can
be assigned any measurable value since continuous Wigner spectra are simple
almost surely. Entry laws and vectors satisfying the stated fixed moment
bounds are allowed; this is not a claim for heavy-tailed ensembles.

**Analytic checks performed.** Hellmann-Feynman gives
$$F_n'(w)=n^{1/3}|\langle u_n,v_{\max}(w)\rangle|^2.$$
The scaling therefore matches the critical spike overlap. Moreover $F_n$
is convex and $F_n'\ge0$. These exact identities restrict any proposed
limit and provide deterministic checks on numerical differentiation.

**Alignment/eventness.** Compare the whole critical eigenvalue-response
curve and its spike-alignment derivative with the Gaussian reference.
Misalignment is law discrepancy in $C^1$, not just eigenvalue error at one
parameter. The event is emergence of an aligned spectral outlier.

**Context/falsification.** BBP-type transitions and deformed-Wigner edge
universality are established context; pointwise edge convergence need not
yield derivative-process convergence. Check existing joint eigenvector
universality results, small gaps, and uniformity in $w$. The former Boolean
composition width claim is withdrawn: its basic transported profile follows
the exact identity $\mu_F(p)=\mu_g(\mu_h(p))$ and was not an adequate target.

defines: main.conjectures.c05 derivative-topology critical spike universality
consumer: main.conjectures.evidence
