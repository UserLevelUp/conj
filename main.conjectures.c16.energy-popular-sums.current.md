# C16 - Independent extreme missing-sum fronts

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Include each integer of $[0,m-1]$ independently with
probability $q=q_m\to0$, obtaining $A$. Assume
$q^2m/\log(1/q)\to\infty$. Let $L_-$ be the largest missing sum in
$[0,m-1]$; let $L_+$ be the largest distance $2m-2-s$ of a missing sum
$s$ in $[m,2m-2]$. Set a maximum over an empty set to $-1$.

**Proposal.**
$$
\left(\frac{q^2L_-}{2}-\log(2/q^2),
\frac{q^2L_+}{2}-\log(2/q^2)\right)
\Longrightarrow(G_-,G_+),
$$
where the two limits are independent standard Gumbel variables.

**Analytic checks performed.** For $0\le s<m$, distinct unordered pairs
summing to $s$ are disjoint. There are
$u_s=\lfloor(s+1)/2\rfloor$ such pairs and one diagonal pair when $s$ is
even. Exactly
$$\Pr(s\notin A+A)=(1-q^2)^{u_s}(1-q)^{1_{\{s\ {\rm even}\}}}.$$
Summing the leading tail above $L$ gives
$(2/q^2)e^{-q^2L/2}$, explaining the proposed centering. The two relevant
fringes have size order $q^{-2}\log(1/q)=o(m)$, allowing disjoint underlying
sample regions. Dependence among sums within a fringe remains unresolved.

**Alignment/eventness.** Compare the last missing-sum locations with
independent rare-event fronts; their joint law is the alignment target.
The event is completion of the additive interior.

**Context/falsification.** The primary text of
[Limiting Behavior in Missing Sums of Sumsets](https://arxiv.org/abs/2401.17254)
was consulted. It already gives exact single-sum probabilities, moments,
and fringe-independence bounds; those are baseline facts, not claimed new.
Test clusters of missing sums for a nonunit extremal index, and search for
existing extreme-front laws. The one-point calculation is not a Gumbel proof.

defines: main.conjectures.c16 extreme missing-sum fronts
consumer: main.conjectures.evidence
