# C02 - A scaling law for the shortest critical crossing witness

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** In critical triangular-lattice site percolation of mesh
$1/n$ in the unit square, let $H_n$ be the occupied left-right crossing
event. On $H_n$, let $L_n$ be the smallest number of sites in such a path.
This is a minimum crossing certificate, not the exploration interface length.

**Proposal.** There exist $\chi\in(1,7/4)$ and a positive, finite,
nonconstant random variable $L$ such that
$$
\mathcal L(n^{-\chi}L_n\mid H_n)\Longrightarrow\mathcal L(L),
\qquad
n^{-\chi}\mathbb E[L_n\mid H_n]\longrightarrow\mathbb E L\in(0,\infty).
$$
The pure power normalization, nondegenerate distribution, and moment
convergence are substantive requirements; logarithmic exponent bounds alone
would not establish this proposal.

**Analytic checks performed.** A crossing needs at least order $n$ sites;
a self-avoiding crossing uses at most order $n^2$. Thus the elementary
geometric bounds do not settle the proposed exponent. On the all-occupied
configuration a straight path has order $n$ length, showing why the law must
condition on typical critical configurations rather than claim a deterministic
lower bound $n^\chi$ for every crossing. Certificate length need not have
vanishing relative variance: that erroneous concentration intuition is dropped.

**Alignment/eventness.** Compare minimum witness size across mesh scales.
Misalignment is failure of the normalized witness distribution to stabilize.
The detection event is existence of a macroscopic crossing.

**Context/falsification.** Critical chemical distance, shortest crossings,
and arm estimates are neighboring theory. This proposes scaling-limit
structure, not a renamed famous solved conjecture or an asserted exact
chemical-distance exponent. Test log corrections, nonuniform integrability,
boundary conventions, and known shortest-crossing results. No crossing
length simulation or exact novelty clearance has been performed.

defines: main.conjectures.c02 critical shortest-crossing witness scaling
consumer: main.conjectures.evidence
