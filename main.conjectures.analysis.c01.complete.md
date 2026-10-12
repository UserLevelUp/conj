# C01 follows from established noise sensitivity theorems

Review date: 2026-10-12. **Disposition: known or implied.** This completes
the review of the original C01 implication, not the portfolio review.
The mathematical statement is a consequence of existing theorems; no new
open problem is claimed.

Original input: `main.conjectures.c01.revealment-pivotal-clusters.current.md`.
Original SHA-256: `61cb6e3e6bbb24e2a9507f56109a48603868b3cd52fac79a32c1036023b7cf18`.
The later status-only edit to that file points here and leaves its hypotheses
and conclusion unchanged.

## Precise implication and proof

Use the fair-product measure, Boolean values in {0,1}, flip influences, and
the zero-error worst-input expected query cost R0 from C01. Write N for the
number of coordinates and tau for their common influence. Transitivity
ensures all influences are equal. The tribes construction in the input
exhibits an admissible balanced sequence with tau tending to zero.

For any eta > 0, choose an exact randomized decision tree whose worst-input
expected cost is at most R0 + eta. It can avoid repeated queries and query
all remaining coordinates if necessary. Randomly conjugate this algorithm
by a uniform element of the finite transitive invariance group of f.
The result still computes f exactly, preserves the expected query bound,
and has equal query probability for every coordinate. Its revealment delta
therefore satisfies

$$\delta\le (R_0+\eta)/N.$$

For a monotone {0,1}-valued function, the magnitude of the singleton
Fourier coefficient is I_i/2. Schramm and Steif's Theorem 1.8 at level one
gives

$$\frac{N\tau^2}{4}=\sum_{|S|=1}\widehat f(S)^2
\le\delta\|f\|_2^2\le\frac{R_0+\eta}{N}.$$

Consequently N tau <= 2 sqrt(R0 + eta). Letting eta decrease to zero,

$$\sum_i I_i^2=N\tau^2\le2\tau\sqrt{R_0}
\le2\sqrt{C\tau\log(1/\tau)}\longrightarrow0.$$

Theorem 1.3 of Benjamini, Kalai and Schramm now gives noise sensitivity.
In C01's convention, resampling each fair bit with probability epsilon
is equivalent to independently flipping it with probability epsilon/2.
The Fourier covariance is

$$\operatorname{Cov}(f(X),f(Y))=
\sum_{S\ne\varnothing}\widehat f(S)^2(1-\epsilon)^{|S|},$$

which tends to zero at every fixed epsilon in (0,1). This is exactly C01's
conclusion. The proof also works under the weaker condition
R0 tau^2 -> 0. That strengthening is a corollary of the same argument,
not another proposed open conjecture.

## Source comparison and checks

- [Schramm and Steif, Quantitative noise sensitivity and exceptional times
  for percolation](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n2-p01-p.pdf),
  Theorem 1.8, printed page 623: the randomized exact-algorithm Fourier-level
  bound applies to the symmetrized algorithm above.
- [Benjamini, Kalai and Schramm, Noise sensitivity of Boolean functions and
  applications to percolation](https://www.numdam.org/article/PMIHES_1999__90__5_0.pdf),
  Theorem 1.3, printed page 8: vanishing sum of squared influences implies
  noise sensitivity. The primary theorem statements were read.

The inference between those theorems is the derivation above. No numerical
experiment is needed to establish it. Majority has R0 of order tau^-2 and
does not meet the sufficient little-o condition; tribes does meet C01's
condition. Neither example contradicts the proof. Exact balance is not
needed for the argument. For sufficiently large n the assumed near-half
mean ensures the function is nonconstant and tau > 0.

All four review gates are addressed: well-posedness and nonvacuity, analytic
falsification, primary-theorem comparison, and a source-bound disposition.
No independent peer review or formal proof-assistant verification is claimed.

publish: main.conjectures.analysis.c01 completed review with implication proof
consumer: main.conjectures.c01
publish: main.conjectures.notes.c01.implied explicit theorem reduction
consumer: main.conjectures.category.topic.boolean
consumer: main.conjectures.category.kind.analytic
consumer: main.conjectures.category.kind.literature
consumer: main.conjectures.category.status.implied
