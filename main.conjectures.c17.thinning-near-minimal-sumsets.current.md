# C17 - A Gaussian field for sparse sumset deficits

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Use $A,m,q$ from C16. Let $Y_-(u)$ count missing sums
$0\le s\le\min(m-1,\lfloor2u/q^2\rfloor)$.
Let $Y_+(u)$ count missing sums $m\le s\le2m-2$ with
$2m-2-s\le\lfloor2u/q^2\rfloor$. Center by their exact expectations and
put $Z_\pm(u)=q^{3/2}(Y_\pm(u)-\mathbb EY_\pm(u))$.

**Proposal.** On every finite $[0,U]$, $(Z_-,Z_+)$ converges in
$D([0,U])^2$ to independent centered continuous Gaussian processes with
common covariance
$$
K(u,v)=8\int_0^{\min(u,v)}
(e^{-z}-e^{-u})(e^{-z}-e^{-v})\,dz.
$$
Also, for the full deficit $D=2m-1-|A+A|$,
$q^3\operatorname{Var}D\to8$ and
$q^{3/2}(D-\mathbb ED)\Longrightarrow N(0,8)$.

**Analytic checks performed.** The exact single-sum formula in C16 gives
$\mathbb ED\sim4/q^2$. Thus thinning an interval at $q=1/2$ produces
doubling near $4$, not $2$; the old retained-size-normalized doubling claim
is withdrawn. A first-order projection calculation gives the influence of
site $i$ on $Y_-(u)$ approximately
$-(2/q)(e^{-q^2i/2}-e^{-u})_+$.
Summing its Bernoulli variances yields the displayed $K$;
$K(\infty,\infty)=4$ per fringe. This is a derived first-order candidate,
NOT a verified remainder estimate for the full field.

**Alignment/eventness.** Compare the missing-sum profile at all fringe
distances with a specified fluctuation field. Departures in covariance or
law are misalignment; filling an additive fringe is the event.

**Context/falsification.** [The missing-sums primary source](https://arxiv.org/abs/2401.17254)
already studies expectation and second moments. The proposed functional
law and its explicit sparse-limit kernel require separate novelty review.
Compute higher-order projections and test whether they remain negligible
uniformly in $u$; failure would reject the proposed kernel.

defines: main.conjectures.c17 sparse sumset Gaussian deficit field
consumer: main.conjectures.evidence
