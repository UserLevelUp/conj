# C20 - Extreme autocorrelation in a fixed-density random set

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Fix $\alpha\in(0,1)$; sample $A$ uniformly among
$m=\lfloor\alpha p\rfloor$ element subsets of $\mathbb F_p$.
For each unoriented nonzero difference class set
$R_d=|A\cap(A+d)|$. For $p\ge5$ let
$P_j=(m)_j/(p)_j$,
$$\mu_p=pP_2,\qquad
\sigma_p^2=pP_2+2pP_3+p(p-3)P_4-(pP_2)^2.$$
Put $N=(p-1)/2$ and use $a_N,b_N$ from C15.

**Proposal.** For every real $x$,
$$
\Pr\left[a_N\left(\max_{[d]}
(R_d-\mu_p)/\sigma_p-b_N\right)\le x\right]
\longrightarrow \exp(-e^{-x}).
$$
This has a fixed, nonvacuous extreme threshold rather than an existential
threshold which could include all residues.

**Analytic checks performed.** The $p$ directed edges of the difference
cycle give $p$ identical-pair terms, $2p$ ordered overlapping terms, and
$p(p-3)$ disjoint terms in $\mathbb ER_d^2$, yielding the exact variance
above. Expanding it gives
$\sigma_p^2\sim\alpha^2(1-\alpha)^2p$.
Also $R_d=R_{-d}$ and $\sum_{d\ne0}R_d=m(m-1)$: the variables are not
independent. These constraints neither prove nor immediately contradict
the proposed maximum law.

**Alignment/eventness.** Compare the strongest nonzero autocorrelation
with a dependent Gaussian-extreme calibration. The event is an extreme
additive alignment witness; misalignment is a wrong limiting tail law.

**Context/falsification.** Fourier autocorrelation identities and
dependent extreme-value theory are neighboring context. Test arithmetic
clusters, moderate-deviation accuracy, and the fixed-sum dependence.
The evidence script compares the moment formula with exhaustive finite
enumeration; it does not test the prime-asymptotic Gumbel assertion.

defines: main.conjectures.c20 fixed-density extreme autocorrelation
consumer: main.conjectures.evidence
