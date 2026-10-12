# C25 - A quenched increasing-witness entropy profile

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** For uniform $\pi\in S_n$, let $X_{n,k}$ count increasing
subsequences of length $k$. Define
$F_n(\alpha)=n^{-1/2}\log(1+X_{n,\lfloor\alpha\sqrt n\rfloor})$.

**Proposal.** There is a deterministic continuous positive
$F:(0,2)\to(0,\infty)$ such that, for every compact $K\subset(0,2)$,
$$\sup_{\alpha\in K}|F_n(\alpha)-F(\alpha)|
\xrightarrow{\Pr}0.$$
No vanishing-entropy assertion at $\alpha=2$ is made.

**Analytic checks performed.** If $L_n$ is the LIS length, then
$X_{n,k}\ge\binom{L_n}{k}$ for $k\le L_n$.
Using $L_n/\sqrt n\to2$ and Stirling gives a required lower bound
$F(\alpha)\ge2H(\alpha/2)$, where
$H(t)=-t\log t-(1-t)\log(1-t)$.
Exactly $\mathbb EX_{n,k}=\binom nk/k!$; Markov and Stirling give the
required upper bound $F(\alpha)\le2\alpha(1-\log\alpha)$.
These bounds are compatible and strictly positive in the interior.
The lower bound tending to zero at the LIS edge does NOT force the
actual entropy to tend to zero, so the old endpoint claim is withdrawn.

**Alignment/eventness.** Compare witness entropy across target-length
scales with one deterministic profile. Uniform residual is misalignment;
approaching the maximum-witness-length regime is the event.

**Context/falsification.** LIS asymptotics, quenched subsequence counts,
and annealed/quenched free energies are neighboring theory. Search
existing entropy-profile results and attack nonconcentration caused by
overlapping witnesses. Exact finite subsequence counts in the evidence
script check the first moment and LIS witness bound, not the proposed
uniform quenched limit.

defines: main.conjectures.c25 quenched increasing-witness entropy profile
consumer: main.conjectures.evidence
