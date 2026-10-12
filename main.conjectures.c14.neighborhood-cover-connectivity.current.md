# C14 - Joint nonbacktracking cover-time extremes on biregular graphs

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Fix integers $d,k\ge3$. Let $B_n$ be uniform connected
simple bipartite graphs with $n$ left vertices of degree $d$ and
$m=dn/k$ right vertices of degree $k$, through admissible sizes.
Start from a uniformly chosen directed right-to-left edge. Continue the
nonbacktracking walk. One round traverses left-to-right-to-left.
Let $T_L,T_R$ be the numbers of rounds until all vertices on the respective
sides have been visited, counting the initial left vertex as visited.

**Proposal.**
$$
\left(T_L/n-\log n,\ T_R/m-\log m\right)
\Longrightarrow(G_L,G_R),
$$
where $G_L,G_R$ are independent standard Gumbel variables with CDF
$\exp(-e^{-x})$.
Both the Gumbel calibration and independence, not merely a ratio of side
sizes, are targets.

**Analytic checks performed.** Uniform directed-edge measure is invariant
under the nonbacktracking transition: every outgoing directed edge has
exactly degree-minus-one eligible predecessors. Hence visits per round
are uniform on each side, giving rates $1/n$ and $1/m$. This does not
make successive visits independent. Degree-2 cycles have cover time order
$n$ rather than $n\log n$ for nonbacktracking walks and are excluded.
Ordinary lazy walks have local-return corrections, so the former universal
side-size ratio was not justified.

**Alignment/eventness.** Compare the two stationary visit rates with their
separate last-unvisited-vertex events. Dependence or incorrect extreme-value
centering is misalignment.

**Context/falsification.** Expander cover times and random-regular
nonbacktracking mixing provide context. Check the effect of short cycles,
adjacent unvisited vertices, and bipartite round periodicity. No cover-time
simulation or exact novelty clearance has been performed.

defines: main.conjectures.c14 joint nonbacktracking biregular cover extremes
consumer: main.conjectures.evidence
