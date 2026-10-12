# C12 - Weighted homological hitting-time alignment

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Start with the complete graph on $[n]$ as the 1-skeleton.
Give each triangle $t$ weight $a_t\in[a,b]$, fixed $0<a<b<\infty$,
and an independent exponential arrival clock of rate $a_t$.
Require, uniformly in edges $e$,
$$
\sum_{t\supset e}a_t=\bar a_n(n-2)+o(n/\log n),\qquad
\bar a_n\in[a,b].
$$
An edge is isolated if it lies in no arrived triangle. Let $\tau_I$ be the
last isolation disappearance time and $\tau_H$ the first time
$H_1(-;\mathbb F_2)=0$.

**Proposal.** For every such deterministic weight sequence,
$\Pr(\tau_I=\tau_H)\to1$.
The target is exact process-level alignment for bounded balanced
inhomogeneity, not the established homogeneous threshold restated.

**Analytic checks performed.** At $t=(2\log n+c)/(\bar a_n(n-2))$,
$\mathbb E I=\sum_e\exp(-t\sum_{t'\supset e}a_{t'})\to e^{-c}/2$.
The factor $1/2$ comes from $\binom n2$; an $o(1)$ relative degree
error alone can shift the critical window by $o(1)\log n$.
Nonconstant admissible weights exist: for even $n$ and balanced signs,
$a_{ijk}=1+\delta s_i s_j s_k$ gives edge-degree correction
$-\delta s_i s_j(s_i+s_j)=O(1)$.
An isolated edge supports a nontrivial mod-2 cocycle in the complete
1-skeleton, so $\tau_H\ge\tau_I$ for $n\ge3$.

**Alignment/eventness.** Detect the disappearance of a local obstruction
and compare it to a global homological transition. Their time difference,
not a filename state, is misalignment.

**Context/falsification.** The homogeneous baseline is
[Linial-Meshulam homological connectivity](https://doi.org/10.1007/s00373-006-0643-9).
Check weighted hitting-time literature and structured cocycles with support
too large for local isolation to detect. The exponential-clock model avoids
invalid probabilities $pa_t>1$. No topology simulation has been performed.

defines: main.conjectures.c12 weighted homological hitting-time alignment
consumer: main.conjectures.evidence
