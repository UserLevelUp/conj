# C22 - Quenched Brownian descent response to sparse reshuffling

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $\pi_n$ be uniform in $S_n$. Independently choose a
uniform $m_n$-subset of positions and uniformly permute the values there,
obtaining $\pi_n'$, with $m_n\to\infty$, $m_n=o(n)$.
For $t\in[0,1]$ let $D_n(t,\pi)$ count descents among adjacent pairs
with left endpoint $i\le\min(n-1,\lfloor tn\rfloor)$.
Put $Z_n(t)=(D_n(t,\pi_n')-D_n(t,\pi_n))/\sqrt{m_n}$.

**Proposal.** Conditional on $\pi_n$, the law of $Z_n$ in $D[0,1]$
converges in probability, in bounded-Lipschitz distance for the Skorokhod
metric, to the law of $B(t)/\sqrt3$ for standard Brownian motion $B$.
There is no unspecified covariance kernel and no Brownian-bridge endpoint
constraint.

**Analytic checks performed.** For four independent continuous uniform
labels $L,R,x,y$, the descent contribution at one replaced site is
$h(x)={\bf1}_{L>x}+{\bf1}_{x>R}$, and
$$
\mathbb E(h(y)-h(x))^2
=2\mathbb E[|L-R|(1-|L-R|)]=1/3.
$$
Enumeration of all 24 relative orders checks that value exactly.
Also $\mathbb E_{L,R}h(x)=1$ for every $x$, so conserving the multiset
of selected values does not force a zero total descent change.
The expected number of neighboring selected pairs is $O(m_n^2/n)$,
a vanishing fraction of selected sites; controlling their centered
contribution remains part of a proof.

**Alignment/eventness.** Compare original and reshuffled descent profiles
under a specified noise operation. $Z_n$ is the rescaled misalignment;
the event is local order-witness change.

**Context/falsification.** Permutation process limits and quenched
normal approximation are neighboring theory. Check known sparse-shuffle
results, conditional drift, permutation-cycle dependence, and all
$m_n=o(n)$ regimes. The finite simulation in the evidence artifact tests
covariance calibration, not the quenched functional limit.

defines: main.conjectures.c22 quenched Brownian sparse-shuffle descent response
consumer: main.conjectures.evidence
