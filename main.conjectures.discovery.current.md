# Two new directions for sparse random sumsets

These are newly formulated research candidates in this project, not certified
new open problems. Neither has a proof or a complete novelty review. They
are discovery leads N01 and N02, separate from the original 25 slots.
Source lineage: C16 and C17, recovered through `recur reveal main.conjectures.additive`.

## N01 Inhomogeneous sparse deficit fields

Fix a continuously differentiable function w on [0,infinity) with
0 < a <= w <= b < infinity and bounded derivative. Let q -> 0 and let
m=m(q) be integers with q^2 m / log(1/q) -> infinity. Independently include
each integer i in [0,m-1] with probability q w(q^2 i/2); this is a valid
probability for sufficiently small q. For fixed U < infinity define

$$Y_q(u)=\#\{0\le s\le\lfloor2u/q^2\rfloor:s\notin A+A\},
\quad Z_q(u)=q^{3/2}(Y_q(u)-\mathbb E Y_q(u)),\quad 0\le u\le U.$$

The upper bound on s is below m for all sufficiently small q. Set

$$H_w(z)=\int_0^z w(t)w(z-t)\,dt,\qquad
B_u(t)=\int_t^u w(z-t)e^{-H_w(z)}\,dz\quad(0\le t\le u).$$

**Conjecture:** Z_q converges in D[0,U], with the Skorokhod J1 topology,
to a centered continuous Gaussian process with covariance

$$K_w(u,v)=8\int_0^{\min(u,v)}w(t)B_u(t)B_v(t)\,dt.$$

**Why this formula:** pairs with a fixed sum are disjoint, so the exact
missing probability is a product of factors 1-p_i p_{s-i}, with a diagonal
factor when required. Its first-order limit at s=2z/q^2 is exp(-H_w(z)).
The influence of site i, t=q^2 i/2, on Y_q(u) is approximately
-(2/q) B_u(t). Summing independent Bernoulli variances yields K_w.
This is a first-order derivation, not a bound on the full statistic's remainder.

The kernel is positive semidefinite: it is a Gram integral with positive
weight w. For w=1, H_w(z)=z and B_u(t)=e^-t-e^-u, recovering C17 exactly.
For constant w=c, rescaling the effective density to qc predicts
K_w(u,v)=c^-3 K(c^2 u,c^2 v), agreeing with the displayed formula.
These are consistency checks. They do not prove the general statement.

**First falsification:** take w(t)=1+0.3 sin(t), compute exact product
expectations and projection coefficients, and compare full covariance with
K_w. Then bound the higher-order projection remainder uniformly in u.
No inhomogeneous simulation has yet been performed. Literature comparison
must cover non-identically distributed random additive bases, not only C17.

publish: main.conjectures.discovery.n01 inhomogeneous deficit-field proposal
consumer: main.conjectures.c17
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.conjecture
consumer: main.conjectures.category.status.unresolved

## N02 Independence of deficit fluctuations and extreme missing sums

In the homogeneous model of C16-C17, retain the exact definitions of
Z_-(u), Z_+(u), L_-, L_+, and their centering. For each fixed U < infinity,
consider the random element in D[0,U]^2 times R^2:

$$\left(Z_-,Z_+,\frac{q^2L_-}{2}-\log(2/q^2),
\frac{q^2L_+}{2}-\log(2/q^2)\right).$$

**Conjecture:** it converges to (G_-,G_+,E_-,E_+), where G_- and G_+ have
the Gaussian covariance K of C17, E_- and E_+ are standard Gumbels, and all
four components are mutually independent.

C16 and C17's marginal assertions do not imply this joint independence.
The additional content is separation between ordinary deficit fluctuations
and rare extreme holes on the same side. Opposite compact fringes are
already functions of disjoint input sites for all sufficiently small q.

**Heuristic:** the compact Gaussian profile uses sites on scale q^-2,
whereas the final missing sums occur on scale q^-2 log(1/q). The early
sites influence the extreme holes, but their random fluctuation in the
log rare-event probability is plausibly of order sqrt(q), tending to zero.
Turning that observation into conditional rare-event estimates is essential.

In the recorded 1200-replicate runs, correlation of the left extreme with
Z_-(4) was 0.337, 0.312, and 0.225 at q=.1,.05,.025. This is substantial
finite dependence; it neither proves nor refutes limiting independence.
Test mixed characteristic functions or conditional exceedance probabilities,
not only correlation. Complete C17's remainder and tightness estimates before
calling this a theorem. Novelty remains unverified.

publish: main.conjectures.discovery.n02 joint Gaussian and extreme-front independence proposal
consumer: main.conjectures.c16
consumer: main.conjectures.c17
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.conjecture
consumer: main.conjectures.category.status.unresolved
