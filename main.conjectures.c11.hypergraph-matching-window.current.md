# C11 - Weighted hypergraph matching and the last isolated vertex

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Fix $k\ge3$ and let $n\to\infty$ through multiples of $k$.
Each $k$-set $e$ of $[n]$ has a deterministic weight $a_e\in[a,b]$,
fixed $0<a<b<\infty$, and an independent exponential arrival clock of
rate $a_e$. Include $e$ when its clock rings. Suppose for some
$\bar a_n\in[a,b]$, uniformly in vertices,
$$
\sum_{e\ni v}a_e=\bar a_n\binom{n-1}{k-1}
+o\!\left(\frac{\binom{n-1}{k-1}}{\log n}\right).
$$
Let $\tau_{\rm iso}$ be the time the last isolated vertex disappears and
$\tau_{\rm pm}$ the first time a perfect matching exists.

**Proposal.** For every weight array satisfying these conditions,
$\Pr(\tau_{\rm pm}=\tau_{\rm iso})\to1$.
This is exact hitting-time alignment, not a comparison of expected matching
size with an unrelated probability threshold.

**Analytic checks performed.** At
$t=(\log n+c)/(\bar a_n\binom{n-1}{k-1})$, a vertex's isolation
probability is exactly $\exp(-t\sum_{e\ni v}a_e)$, so the expected isolated
count tends to $e^{-c}$. The required error is $o(1/\log n)$, not just
$o(1)$. The model is nonempty and inhomogeneous: for even $n$ take balanced
signs $s_i$ and $a_e=1+\delta\prod_{i\in e}s_i$, $0<\delta<1$; fixed-$k$
weighted degree errors are relatively $O(1/n)$ or smaller.

**Alignment/eventness.** Compare the first global perfect-matching witness
with extinction of the last local isolation obstruction. Their unequal
hitting times are misalignment.

**Context/falsification.** Homogeneous random-hypergraph matching and
hitting-time theory are established context. Exact weighted generalizations
need literature review. Test balanced mesoscopic weight patterns for Hall-type
or divisibility obstructions. The earlier $p_*D\to\infty$ condition is
withdrawn: a nibble after high expected retained degree can already cover
nearly all vertices, making that proposed median regime suspect.
The isolation calculation is not a proof of a perfect matching.

defines: main.conjectures.c11 weighted perfect-matching hitting-time alignment
consumer: main.conjectures.evidence
