# C23 - Second-order extension entropy of random planar orders

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Sample $n$ independent uniform points $(x_i,y_i)$ in
the unit square. Order them by coordinatewise dominance:
$i<_{P_n}j$ iff $x_i<x_j$ and $y_i<y_j$. Ties have probability zero.
Let $e(P_n)$ be the number of linear extensions and use natural logs.
Equivalently sort by $x$ and use a uniform permutation of the $y$ ranks.

**Proposal.** There is a finite deterministic constant $\beta$ such that
$$
\frac{\log e(P_n)}n-\frac12\log n\xrightarrow{\Pr}\beta.
$$
The deterministic order-$n$ correction, not the leading entropy scale,
is the proposed target.

**Analytic checks performed.** For any poset of width $w$ and height $h$,
$e(P)\le w^n$, since every extension step has at most $w$ available
minimal elements. Ordering the height layers gives
$e(P)\ge\prod_j n_j!$ and hence
$\log e(P)\ge n\log(n/h)-n$.
For this ensemble, the classical increasing/decreasing-subsequence scale
$h,w=(2+o_{\Pr}(1))\sqrt n$ puts any proposed $\beta$ in
$[-1-\log2,\log2]$; it does not prove convergence.
The previous universal-width statement is rejected: an antichain of
$\alpha n$ followed by a chain has exactly $(\alpha n)!$ extensions,
not leading entropy $n\log n$.

**Alignment/eventness.** Compare random planar order constraints with
extension entropy at a fixed normalization. Failure to approach one
second-order constant is misalignment; an extension is a global witness.

**Context/falsification.** Random multidimensional orders, poset entropy,
and LIS theory are neighboring context. Exact second-order results may
already exist and require specialist literature review. The evidence
script counts finite planar-order extensions by dynamic programming and
checks both deterministic bounds, not the proposed limiting constant.

defines: main.conjectures.c23 random planar-order second-order extension entropy
consumer: main.conjectures.evidence
