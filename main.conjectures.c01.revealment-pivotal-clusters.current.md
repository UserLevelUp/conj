# C01 - Near-extremal exact-query efficiency forces noise sensitivity

**Status (2026-10-12):** implied by established theorems. The original
implication below follows from Schramm-Steif Theorem 1.8 and BKS Theorem 1.3;
see `main.conjectures.analysis.c01.complete.md` for the source-bound proof.
This slot is no longer an unresolved research target. Its `.current` filename
is retained as a stable address during portfolio integration.

**Definitions.** Let $f_n$ be monotone Boolean functions on $N_n$ bits,
invariant under a transitive permutation group of coordinates, with
$\mathbb E_{1/2}f_n\to1/2$.
Let $\tau_n=\max_i\Pr[f_n(X)\ne f_n(X^{\oplus i})]\to0$.
Define $R_0(f)$ as the infimum over zero-error randomized adaptive decision
trees of their maximum, over all inputs, expected number of queries.

**Original proposal, now an established consequence.** For every such sequence and every fixed $C<\infty$,
$R_0(f_n)\le C\log(1/\tau_n)/\tau_n$ implies
$$
\operatorname{Cov}(f_n(X),f_n(Y))\longrightarrow0
$$
for every fixed $\epsilon\in(0,1)$, where each bit of $Y$ is independently
resampled from $X$ with probability $\epsilon$.

**Analytic checks performed.** Tribes with $m=\lfloor(\log2)2^k\rfloor$
blocks of size $k$ has $N=mk$, mean tending to $1/2$, and
$\tau=2^{-(k-1)}(1-2^{-k})^{m-1}\sim2^{-k}$.
Querying all bits gives $R_0\le N=O(\log(1/\tau)/\tau)$: the hypotheses
are nonempty without demanding impossible exact balance from tribes.
Its covariance is exactly
$$
\big(1-2^{1-k}+2^{-k}(1-\epsilon/2)^k\big)^m
-(1-2^{-k})^{2m}\longrightarrow0.
$$
Majority has $\tau=\Theta(N^{-1/2})$ but requires order $N$ expected
queries on near-tied inputs, so it does not supply a noise-stable example
in this near-extremal query regime.

**Alignment/eventness.** Compare decision-tree efficiency with persistence
of the event under fixed noise. Persistent covariance is misalignment.
The event is loss of outcome memory, not just small individual influence.

**Context/falsification.** Decision-tree influence inequalities and
Schramm-Steif revealment bounds are established neighboring theory. Check
whether their sharper variants already imply this implication; examine
recursive tribes/majority mixtures and adversarial input costs. The tribes
calculation does not prove the general implication.

defines: main.conjectures.c01 exact-query efficiency and noise sensitivity
consumer: main.conjectures.evidence
consumer: main.conjectures.analysis.c01
