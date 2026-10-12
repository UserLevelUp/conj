# C08 - Growing-degree bootstrap transition profiles

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Fix $r\ge2$. Let $G_n$ be uniform among simple
$d_n$-regular graphs, $nd_n$ even, with
$d_n\to\infty$ and $d_n\le\log\log n$. Seed vertices independently with
probability $p$, then repeatedly activate every vertex having at least $r$
active neighbors. Let $B_n$ be the event that the final active set has at
least $0.9n$ vertices; this is not the event of full occupancy.
Write $p_n$ for the unique median of $\Pr_p(B_n)$.

Define $p_{\mathrm{tree}}(d,r)$ as the supremum of $p$ for which the least
fixed point of
$$x=p+(1-p)\Pr[\operatorname{Bin}(d-1,x)\ge r]$$
is below 1.

**Proposal.** There is $c_r\in(0,\infty)$ such that, uniformly for bounded $z$,
$$
\Pr_{p_n+z\sqrt{p_{\mathrm{tree}}(d_n,r)/n}}(B_n)
\longrightarrow\Phi(c_r z).
$$
Also $p_n/p_{\mathrm{tree}}(d_n,r)\to1$. The uniform growing-degree
finite-size profile, rather than the leading tree heuristic alone, is the
target. $\Phi$ denotes the standard normal CDF.

**Analytic check performed.** The dilute recursion
$x=p+(dx)^r/r!$ has tangency when
$1=d^r x^{r-1}/(r-1)!$. Consequently
$$x_*=\big((r-1)!/d^r\big)^{1/(r-1)},\qquad
p_*=(r-1)x_*/r.$$
For $r=2$, $p_*=1/(2d^2)$, not $1/d^2$.
The exact binomial fixed point above avoids replacing a finite-size center by
an asymptotic approximation whose error may exceed the proposed window.
The regime is nonempty: $d_n\le\log\log n$ gives $np_*\to\infty$.

**Alignment/eventness.** Compare an activation-density transition with the
tree bifurcation and its Gaussian finite-size calibration. Misalignment is
the CDF residual; survival on an infinite tree and complete finite activation
are explicitly different events.

**Context/falsification.** [Janson et al.](https://arxiv.org/abs/1012.3535)
analyze bootstrap thresholds and Gaussian limits for the binomial random
graph, a neighboring ensemble, not this stated growing-degree regular model.
Test degree-conditioning effects, critical fluctuation variance, and the
$0.9n$ choice. The tangency calculation is analytic evidence only; no
simulation of this conjectured profile has been run.

defines: main.conjectures.c08 growing-degree activation-density profile
consumer: main.conjectures.evidence
