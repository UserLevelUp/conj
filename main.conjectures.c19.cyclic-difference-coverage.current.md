# C19 - A point process for difference-witness arrival

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Expose $\mathbb F_p$ in a uniformly random order and let
$A_j$ be the first $j$ exposed residues. For each unoriented nonzero
difference class $[d]=\{d,-d\}$, let $\tau_d$ be the first $j$ with
$d\in A_j-A_j$. Let $N_p=(p-1)/2$.

**Proposal.** The random point measure
$$\sum_{[d]}\delta_{\tau_d^2/p-\log N_p}$$
converges to a Poisson point process on $\mathbb R$ of intensity
$e^{-x}\,dx$, in the vague topology and jointly with its upper tail
counts on every finite family of intervals $(x,\infty)$.
In particular the last difference-witness time has Gumbel normalization.

**Analytic checks performed.** For a Bernoulli sample of density $q$, a
fixed nonzero difference is absent precisely when the sample is an
independent set in the length-$p$ cycle with edges $\{a,a+d\}$.
Its expected edge-witness count is $pq^2$; neighboring witness dependence
has first correction scale $pq^3$.
At $q^2p=\log N_p+x$, that correction tends to zero, supporting the
single-class rare-event scale. Opposite differences are identical events,
so counting $p-1$ independent classes would be wrong.

**Alignment/eventness.** Compare the whole witness-arrival process with
a specified rare-event point process, not just one critical-window count.
Misalignment is its joint distributional discrepancy.

**Context/falsification.** Random difference bases and coupon-collector
extremes are neighboring theory. Check existing process-level results;
joint auxiliary graphs for several differences have arithmetic cycles
that a single-witness calculation misses. Exact small-prime cycle
independent-set enumeration checks the local event definition. It is not
evidence of Poisson-process convergence.

defines: main.conjectures.c19 difference-witness arrival point process
consumer: main.conjectures.evidence
