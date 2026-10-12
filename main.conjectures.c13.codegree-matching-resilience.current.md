# C13 - Locally resilient transversals in random Latin squares

**Status:** candidate conjecture; truth, exact novelty, and open status unverified.

**Definitions.** Let $L_n$ be a uniformly random labeled Latin square of
order $n$. Its cells are triples (row, column, symbol); each of the $3n$
coordinates has degree $n$, and every pair of coordinates has codegree at
most 1. A transversal consists of $n$ cells using every row, column, and
symbol once. Fix $\rho\in(0,1/3)$.

**Proposal.** With probability tending to one, every cell-deletion set
incident to at most $\rho n$ cells at each individual row, column, and
symbol leaves a transversal.
The adversary may know the whole realized square.

**Analytic checks performed.** All degrees are exactly $n$: no tiny dense
component can hide destruction of a sparse component in a global budget.
Every surviving coordinate has degree at least $(1-\rho)n$.
These local bounds do not by themselves prove a transversal.
For contrast, the deterministic cyclic square $L(i,j)=i+j\bmod n$ has
no transversal when $n$ is even: summing all selected symbols would give
$n(n-1)/2\equiv n/2\pmod n$, while summing all selected row and column
labels gives $n(n-1)\equiv0$. Thus a claim about every Latin square would
be false even with no deletion; the random ensemble is essential.

**Alignment/eventness.** Compare local fault budgets with preservation of
a global transversal witness. Misalignment is an admissible deletion
destroying every witness. The event is transversal survival.

**Context/falsification.** Random Latin-square transversals, rainbow
matchings, absorption, and resilience are neighboring theories; exact
novelty is unresolved. Attack partition barriers and adaptive symbol-biased
deletions below the specified cap. Small cyclic-square enumeration is a
definition/counterexample check, not evidence that random squares satisfy
the resilience conjecture.

defines: main.conjectures.c13 locally resilient random Latin transversals
consumer: main.conjectures.evidence
