# C24 - A deterministic relaxation scale for random planar extension walks

**Status:** high-risk candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Use the random planar poset $P_n$ of C23. On its linear
extensions, stay put with probability $1/2$; otherwise choose an adjacent
position uniformly from $1,\ldots,n-1$ and swap the pair if incomparable.
This symmetric irreducible chain has uniform stationary measure.
Let $\gamma(P_n)=1-\lambda_2$ for its transition matrix, setting the gap
to 1 when there is just one extension.

**Proposal.** There exists $\gamma_*\in(0,\infty)$ such that
$$n^3\gamma(P_n)\xrightarrow{\Pr}\gamma_*.$$
This fixes the ensemble and asks for a deterministic relaxation constant;
it makes no width-only bound for arbitrary posets.

**Analytic checks performed.** For two disjoint nonempty chains on $n$
elements, extensions are binary words of fixed weight. This walk is
adjacent exclusion and has
$$\gamma=\frac{1-\cos(\pi/n)}{n-1}\sim\frac{\pi^2}{2n^3}.$$
Thus width 2 does not give an $n^{-1}$ gap. The finite transition matrices
in the evidence script independently check this counterexample and the
specified laziness convention. For an antichain the adjacent-transposition
chain has the same slow single-label mode.

**Alignment/eventness.** Compare order geometry with a specified relaxation
scale of witness exploration. Fluctuation or drift of $n^3\gamma(P_n)$
is misalignment; the event is loss of ordering memory.

**Context/falsification.** Linear-extension sampling and adjacent-swap
mixing are established context. Random planar constraints may change the
exponent, not merely its constant; seek a faster collective relaxation
mode or a bottleneck. No spectral-gap experiment on large random planar
posets has been performed, and the two-chain calculation is not evidence
of this ensemble's conjectured limit.

defines: main.conjectures.c24 random planar extension-walk relaxation constant
consumer: main.conjectures.evidence
