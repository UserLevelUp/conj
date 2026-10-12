# C07 - Independent Tracy-Widom edges after vertex thinning

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $G_n$ be uniform simple $d_n$-regular on labeled
$[n]$, with $d_n=n^{1/5}+O(1)$ and $nd_n$ even. Retain each vertex
independently with fixed probability $q\in(0,1)$; let $H=G_n[S]$,
$M=|S|$, and $D=(D_i)_{i\in S}$ be its labeled degree sequence.
Set $B=D^{-1/2}A(H)D^{-1/2}$, with zero rows at zero degrees.
For $M\ge2$, order its eigenvalues as $\lambda_1\ge\cdots\ge\lambda_M$.
Let $E_+=\lambda_2$ and $E_-=-\lambda_M$. Define exact conditional
means $\mu_\pm=\mathbb E[E_\pm\mid S,D]$ and variances
$s_\pm^2=\operatorname{Var}(E_\pm\mid S,D)$.

Let $W$ have the standard real Tracy-Widom law: the limiting distribution
of $N^{2/3}(\lambda_{\max}(\mathrm{GOE}_N)-2)$ for off-diagonal variance
$1/N$ and diagonal variance $2/N$. Write
$W^\circ=(W-\mathbb EW)/\sqrt{\operatorname{Var}W}$.
Bounded-Lipschitz distance on $\mathbb R^2$ uses test functions bounded
by 1 and with Euclidean Lipschitz constant at most 1.

**Proposal.** With probability tending to one, $M\ge2$ and both
$s_+,s_-$ are positive. On this event,
$$
d_{\rm BL}\left(
\mathcal L\left(
\left(\frac{E_+-\mu_+}{s_+},\frac{E_--\mu_-}{s_-}\right)
\middle|S,D\right),
\mathcal L(W_1^\circ,W_2^\circ)\right)\longrightarrow0
$$
in probability, where $W_1^\circ,W_2^\circ$ are independent copies.
Set the discrepancy to 1 on the exceptional event.
This proposes a specific non-Gaussian joint edge law and independence.
Exact conditional moments avoid inventing an unverified sparse-edge
centering correction; their use does not imply the proposed shape.

**Analytic rejection of the previous proposal.** Conditional on labeled
$(S,D)$, $H$ is EXACTLY uniform among simple graphs on $S$ with degree
sequence $D$. For each such graph, every regular completion uses only
edges between $S$ and its complement or within the complement.
Its constraints are residual degrees $d_n-D_i$ on $S$ and total degree
$d_n$ on each outside vertex. They do not depend on the identities of
the edges inside $S$. Thus every admissible induced graph has the same
number of completions. Independent retention weights a fixed $S$ equally.
The previous conditional-reference comparison was therefore tautological,
and the assertion that completion counts varied within fixed $(S,D)$
was false. Both are withdrawn.

**Other checks performed.** Given a retained vertex and the original graph,
its degree is $\operatorname{Bin}(d_n,q)$; a union bound makes isolated
vertices negligible. The Perron eigenvalue is exactly 1 on connected graphs,
with eigenvector $\sqrt D$, and is deliberately excluded. The normalization
uses the surviving graph's own degrees. The evidence script exhaustively
checks equal completion multiplicities in the six-vertex degree-2 example.
That finite identity check supports the rejection, not the Tracy-Widom law.

**Alignment/eventness.** Compare both nontrivial spectral edges with a
specified independent real Tracy-Widom pair. The displayed joint-law distance
is misalignment; thinning-induced spectral fluctuation is the event.

**Context/falsification.** Prescribed-degree random graph spectra, sparse
edge corrections, and Tracy-Widom universality are neighboring theory.
The exact conditioning identity reduces the problem to typical random
degree sequences induced by thinning, but does not establish their edge law.
Check existing prescribed-degree edge-universality results, possible
localized extremes, conditional moment tails, and dependence of the two
edges. No asymptotic spectral experiment or exact novelty clearance is
recorded. This may already be covered by specialist results.

defines: main.conjectures.c07 independent conditional Tracy-Widom thinning edges
consumer: main.conjectures.evidence
