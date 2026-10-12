# Conjecture analysis notebook

Working root: the repository root (`.`). Review date: **12 October 2026**.

All 25 original statements have received an initial mathematical screen.
**C01 is implied by established theorems**, with a complete reduction in
`main.conjectures.analysis.c01.complete.md`. The other 24 statements remain
unresolved; an initial screen is not 24 completed specialist reviews.
New experiments examine C16-C17 and the actual random planar ensemble in
C24. Two new candidates are in `main.conjectures.discovery.current.md`.

This is the editable project notebook used by the notes Reveal lane.
The previous Copilot notebook is preserved in the historical appendix below,
with machine-specific paths replaced by portable repository references.
The unredacted local history remains outside the public Git tree. Current findings take priority
over historical statements such as “all reviews pending.” The original
25 mathematical statements remain identifiable; new leads use N01-N02.

## How to use the editor canvas and Reveal

Run these commands from the working root. Reveal locates notes; explicitly
read or open the returned file to see their body.

```powershell
recur reveal main.conjectures.notes -d .
recur reveal conjecture-analysis -d .
recur reveal main.conjectures.discovery -d .
recur trace-id 'main.conjectures.notes.c17.**' --scope 'main.conjectures.**' -d . --format full
recur trace-id 'main.conjectures.category.status.implied' --scope 'main.conjectures.**' -d . --format full
```

In Codex, open this file in the editor panel to inspect or edit the notebook.
That panel is the local editor continuation of the earlier canvas workflow;
this is not a newly created cloud spatial Canvas. After a user edit, read
the current file before adding findings. Record the claim, concise argument,
source, evidence limits, disposition, next check, and applicable trace labels.
Only mark a scoped review complete when its gates are addressed. `.current`
records attention, not an assertion that every statement is still open.

Loaded guidance: installed and project-local `recur-expert` and
`recur-eventness`, installed `recur-trace-id`, and the project-local
`conjecture-analysis` skill. The existing notes capsule supplies the editor
workflow; there is no separately registered canvas skill in this project.
The write-page guidance is used for clear notebook prose while retaining
the established local-file format.

## C15 subset review — version 0.2.0

The [public paper](main.conjectures.analysis.c15.subset.complete.md) supplies a
complete proof of C15 with full observation, including exact simultaneous
intervals and the Gumbel limit. An explicitly separate oracle result assumes
the nuisance matrix is known under missingness. These are standard
consequences; full C15 remains unresolved and the portfolio counts do not change.

For hypothetical decisions, the paper requires both positive expected return
after costs and a bounded probability of endpoint loss. A simultaneous
historical confidence statement is insufficient on its own: a prospective
mean-transfer bound and a conditional tail model are additional hypotheses.
The note proves the resulting sufficient rule, handles repeated inspection
through error allocation, and distinguishes inference error from future loss.
Its identical-history/opposite-future construction explains the need for those
extra hypotheses. No actual investment window has been validated.

Well-posedness is checked with an admissible rank-two C15 sequence. Falsification
checks expose failures caused by missing contexts and correlated errors.
Primary-source comparisons cover Xia–Yuan's individual-linear-form theorem
and Howard et al.'s time-uniform inference framework. The linked paper records
the limits of the econometric connection and the incomplete novelty review.
The [numerical record](docs/c15-checks.json) binds source hashes; its deterministic
checks and analytic figure illustrate the proof, not market performance.

Next: establish the unknown-nuisance remainder required by full C15; separately
assess whether any empirical application supports prospective calibration.

publish: main.conjectures.notes.c15.subset proved restricted case and unresolved transfer
consumer: main.conjectures.analysis.c15.subset
consumer: main.conjectures.category.topic.statistics
consumer: main.conjectures.category.kind.proof
consumer: main.conjectures.category.status.implied

## Assessment of research interest

Follow-up assessment on 2026-10-12: **six original candidates are a practical
priority shortlist: C03, C06, C07, C13, C15, and C17.** This is a judgment
about which questions merit further work, not a verified count of new open
problems. Twenty-four original statements remain unresolved in our review;
none has yet completed a novelty assessment establishing a new open problem.
The two discovery leads are also preliminary and should not inflate that count.

C03 concerns a precise dynamical-percolation memory law; C06 and C07 concern
universality of spectral behavior under dynamics or thinning; C13 asks for
robust global witnesses under adversarial damage; C15 concerns simultaneous
inference with missing observations; C17 has a concrete fluctuation mechanism
and new tests of its remainder. C06, C07, and C15 have the clearest potential
connections beyond their mathematical specialties. Applications and community
interest are prospective, not established outcomes.

An updated literature search found
[Đanković, Markering, Miller and Yuan's 2026 preprint](https://arxiv.org/pdf/2604.14122),
which establishes chemical-metric scaling limits and existence of an exponent.
Its Section 10 uses a normalization q_n=n^(beta+o(1)). This is substantial
overlap with C02 and updates the older literature context above; it does not
by itself settle C02's exact pure-power normalization and moment statement.
Do not describe the broad existence of chemical-distance scaling as a new
question generated by this project.

For C13, [Almost every Latin square has a decomposition into transversals](https://rhmontgomery.warwick.ac.uk/papers/41decomposingrandomLSs.pdf),
Theorem 1.1, provides a strong established baseline. It does not state C13's
universal adversarial deletion guarantee. For C15,
[Ma, Niu, Zhang and Zhu](https://doi.org/10.1080/01621459.2024.2335591)
already study simultaneous inference using a multiplier bootstrap in a related
auxiliary-covariate matrix-completion model. Exact comparison with C15's
efficient Gumbel law remains necessary; “simultaneous inference” itself is
not a new contribution.

publish: main.conjectures.notes.assessment.priority six provisional research priorities
consumer: main.conjectures.category.kind.literature
consumer: main.conjectures.category.status.unresolved

## Portfolio classification

“Retain for review” means the first screen did not settle the candidate.
It does not establish plausibility, truth, novelty, or publication priority.
The exact hypotheses remain in each source statement. The observations JSON
records hashes for all 25 inputs. C01's completed review separately records
its original input hash before the status-only edit.

| ID | Mathematical area | Initial disposition | Decisive issue or next test |
|---|---|---|---|
| C01 | Boolean analysis | **Known or implied** | Schramm-Steif level one plus BKS proves the claim |
| C02 | Critical percolation | Retain for review | Chemical-distance normalization and uniform integrability |
| C03 | Dynamical percolation | Retain for review | Exact regularly varying spectral-tail amplitude |
| C04 | Near-critical percolation | Retain for review | Uniform second derivative bounds before interchanging limits |
| C05 | Random matrices | Retain for review | Joint spike process and uniform small-gap control in C1 |
| C06 | Matrix dynamics | Retain for review | Tightness of the two-time field including initial time |
| C07 | Prescribed-degree spectra | Retain for review | Existing regular-graph theorems do not directly cover random irregular degrees |
| C08 | Bootstrap percolation | Retain for review | Regular-ensemble critical variance, uniform in growing degree |
| C09 | Random graph entropy | Retain for review | Remainder error relative to a vanishing conditional scale |
| C10 | Random graph mixing | High-risk unresolved | Positivity of conditional scales and mixed-tail behavior |
| C11 | Random hypergraph matching | Retain for review | Uniform weighted matching argument beyond isolation moments |
| C12 | Random topology | Retain for review | Weighted nonlocal cocycles, beyond isolated edges |
| C13 | Random Latin squares | Retain for review | Adaptive local deletion barriers below one third |
| C14 | Random walk extremes | Retain for review | Joint avoidance probabilities and short-return clusters |
| C15 | Statistical inference | Retain for review | Uniform stochastic expansion at the maximum-error scale |
| C16 | Additive extremes | Retain; promising proof route | Joint missing-sum estimates via unions of matchings |
| C17 | Additive fluctuations | Retain; new numerical evidence | Uniform bound on the higher-order projection remainder |
| C18 | Additive energy | Retain for review | Variance after conditioning and lattice anti-concentration |
| C19 | Difference arrival | Retain; promising proof route | Uniform mixed factorial moments and de-Poissonization |
| C20 | Autocorrelation extremes | Retain for review | Joint moderate deviations on arithmetic difference classes |
| C21 | Permutation patterns | Retain for review | Rare-conditioning tilt and the order-n2 correction |
| C22 | Permutation dynamics | Retain for review | Quenched drift and adjacent-site errors across all sparse regimes |
| C23 | Poset entropy | Retain for review | Concentration and existence of the order-n constant |
| C24 | Poset dynamics | High-risk unresolved | Small actual-ensemble gap experiment does not determine exponent |
| C25 | Increasing subsequences | Retain for review | Quenched concentration and uniformity in target length |

## Findings by candidate

### C01 The conjecture is an existing-theorem consequence

Symmetrizing an exact query algorithm gives revealment at most R0/N.
For monotone transitive f, level-one Fourier mass is N tau^2/4. The
Schramm-Steif inequality bounds that by R0/N, and therefore
sum_i I_i^2 <= 2 tau sqrt(R0) <= 2 sqrt(C tau log(1/tau)) -> 0.
BKS yields the requested covariance decay. The full proof, noise-convention
conversion, input hash, and primary theorem references are in
`main.conjectures.analysis.c01.complete.md`. Do not retain this as an
unresolved research target, or rename its immediate weaker-hypothesis
corollary as a new conjecture.

publish: main.conjectures.notes.c01.screen known-theorem implication
consumer: main.conjectures.analysis.c01
consumer: main.conjectures.category.topic.boolean
consumer: main.conjectures.category.status.implied

### C02 Shortest crossings need a metric scaling result

The stated mesh sequence and conditioning are nonvacuous. The range
1 < chi < 7/4 is broad; 7/4 is an interface-related scale, not a derivation
of shortest-path length. A geometric upper bound and a power exponent would
still not establish a nondegenerate law or convergence of its mean.
Damron-Hanson-Sosoe's Corollary 3 concerns shortest versus lowest crossings
in critical bond percolation, a neighboring model and a different conclusion.
Keep both the lattice/model transfer and the stronger limit requirements visible.

publish: main.conjectures.notes.c02.screen metric normalization and integrability unresolved
consumer: main.conjectures.c02
publish: main.conjectures.analysis.c02 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.boolean
consumer: main.conjectures.category.kind.question

### C03 An exponent does not fix an amplitude

The covariance is a positive Laplace transform, so the proposed power is
compatible with positivity and complete monotonicity. If the spectral mass
is b u^(2/3) near zero, integration by parts gives b Gamma(5/3) at long
times. A slowly varying factor can preserve the exponent and prevent the
claimed finite nonzero limit. Establish that regular variation with an
actual constant; scaling-limit existence alone is insufficient.

publish: main.conjectures.notes.c03.screen exact lower-tail constant required
consumer: main.conjectures.c03
publish: main.conjectures.analysis.c03 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.boolean
consumer: main.conjectures.category.kind.analytic

### C04 Smoothness must be uniform before passing to a limit

For each fixed compact parameter interval, the probabilities 1/2+lambda a_n
are valid for all sufficiently large n. Russo's first derivative is a sum
of pivotal probabilities; differentiating again introduces joint discrete
derivatives whose cancellation cannot be inferred from monotonicity.
GPS Theorems 1.4-1.5 establish near-critical configuration/process limits,
not the displayed C2 convergence. Target uniform second-order estimates.

publish: main.conjectures.notes.c04.screen derivative-limit interchange
consumer: main.conjectures.c04
publish: main.conjectures.analysis.c04 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.boolean
consumer: main.conjectures.category.kind.literature

### C05 Convexity is useful but does not supply the topology

GOE with a flat spike supplies a nonempty reference case. The response is
convex and nondecreasing. Convergence of convex functions can help with
derivatives when the limit is differentiable, but neither its required
smoothness nor uniform derivative tightness follows just from a one-point
edge law. Check the rank-one family has no exceptional crossings on the
whole compact interval, not merely simplicity at each fixed w.

publish: main.conjectures.notes.c05.screen derivative topology remains substantive
consumer: main.conjectures.c05
publish: main.conjectures.analysis.c05 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.question

### C06 Initial time is part of the universality target

The OU variance computation is correct but non-Gaussian higher cumulants
persist for short positive times. One cannot replace the process by
stationary GOE merely because the entry variances agree. At the n^-1/3
time scale the question concerns edge eigenvectors and tiny gaps; even
finite-dimensional convergence would need a tightness argument on the square.

publish: main.conjectures.notes.c06.screen initial-law and tightness requirements
consumer: main.conjectures.c06
publish: main.conjectures.analysis.c06 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.question

### C07 Conditional uniformity is correct but is not edge universality

The residual-degree completion argument in the old notebook is exact.
Since q is fixed and d is of order n^(1/5), a binomial tail and union bound
give surviving degrees qd+O(sqrt(d log n)) uniformly with high probability.
That establishes relative near-regularity, not an error small enough at an
edge fluctuation scale. Huang-McKenzie-Yau's Theorem 1.2 treats regular
graphs, including independence discussion in the following remarks. C07
needs irregular prescribed degrees, own-degree normalization, and conditional
moment control to justify standardizing by exact mean and variance.

publish: main.conjectures.notes.c07.screen regular-graph theorem does not directly settle thinning
consumer: main.conjectures.c07
publish: main.conjectures.analysis.c07 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.literature

### C08 The median protects against incorrect centering

A slowly increasing integer degree, adjusted for parity, provides admissible
sequences. The activation probability is a strictly increasing nonconstant
product-measure event probability in the interior, so the median is unique.
The exact median avoids replacing a center by a tree asymptotic whose error
could exceed the Gaussian window. The remaining issue is the fluctuation
coefficient in the regular ensemble uniformly over allowed degree sequences.

publish: main.conjectures.notes.c08.screen regular-ensemble fluctuation coefficient
consumer: main.conjectures.c08
publish: main.conjectures.analysis.c08 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.question

### C09 The needed error is relative to the residual scale

Removing increasingly many cycle counts may leave a variance tending to
zero. An o(1) error in log spanning-tree count then need not be negligible
after dividing by sqrt(v_n). The cited Greenhill-Kwan-Wind version has
Theorem 1.2 for cubic graphs and Conjecture 1.3 for general fixed degree;
do not silently promote the latter to a theorem. Neither is the conditional
growing-cycle residual assertion. Establish a rate compared with v_n.

publish: main.conjectures.notes.c09.screen relative residual error and source scope
consumer: main.conjectures.c09
publish: main.conjectures.analysis.c09 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.literature

### C10 Check each marginal before asserting independence

The path-count subsequences are nonempty after rounding admissible sizes.
The tree-neighborhood event has the stated small collision scale. Quantile
standardization avoids one rare-tail variance problem, but it does not
guarantee a positive interquartile range or a Gaussian shape. First measure
the conditional mixing marginal and entropy marginal separately under exactly
the specified information, then their dependence. This remains high risk.

publish: main.conjectures.notes.c10.screen positive scales and conditional marginals
consumer: main.conjectures.c10
publish: main.conjectures.analysis.c10 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.status.high-risk

### C11 Isolation moments are only a local obstruction calculation

Constant positive weights give an admissible sequence; the balanced sign
construction gives nonconstant examples. For any fixed number h of distinct
vertices, shared incident edges have total weight O(n^(k-2)); multiplied by
critical time this contributes O(log n/n). Thus joint isolation probabilities
factor asymptotically and isolated-vertex factorial moments have the Poisson
scale. This useful local calculation still supplies no perfect matching.
The global weighted hitting-time theorem needs a separate argument.

publish: main.conjectures.notes.c11.screen local factorial moments versus matching
consumer: main.conjectures.c11
publish: main.conjectures.analysis.c11 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.witness
consumer: main.conjectures.category.kind.analytic

### C12 Local topology obstructions also have Poisson-scale moments

Fixed collections of distinct edges share only O(1) triangles per pair.
At critical time the overlap correction is O(log n/n), so the same
factorial-moment reasoning yields the isolated-edge scale with mean e^-c/2.
An isolated edge gives a nontrivial cocycle because its single-edge cochain
is not a cut in the complete skeleton. Eliminating such edges is necessary,
but weighted large-support cocycles remain the global issue.

publish: main.conjectures.notes.c12.screen isolated-edge moments do not prove homology vanishing
consumer: main.conjectures.c12
publish: main.conjectures.analysis.c12 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.witness
consumer: main.conjectures.category.kind.analytic

### C13 The universal adversary is a strong quantifier

Randomness is only in the Latin square; deletion is adversarial after seeing
it. A high survival probability for one random deletion set cannot verify
the universal assertion. The even cyclic-square obstruction does not refute
a statement with probability tending to one over uniform Latin squares.
Search space/divisibility barriers and a uniform absorption argument, with
budgets checked separately on rows, columns, and symbols.

publish: main.conjectures.notes.c13.screen adversarial quantifier requires uniform control
consumer: main.conjectures.c13
publish: main.conjectures.analysis.c13 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.witness
consumer: main.conjectures.category.kind.question

### C14 Stationarity does not prove coupon independence

The units are rounds, and the stationary visit rates are indeed 1/n and
1/m. Excluding degree two removes a genuine deterministic obstruction.
For the requested pair of extreme times, single-vertex avoidance is not
enough: check joint avoidance of nearby left/right vertices and exceptional
short cycles. A few correlations or mean cover times cannot establish the
joint independent Gumbel law.

publish: main.conjectures.notes.c14.screen joint avoidance estimates needed
consumer: main.conjectures.c14
publish: main.conjectures.analysis.c14 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.witness
consumer: main.conjectures.category.kind.question

### C15 The estimator remainder must survive taking a maximum

At p=1, exact Gaussian row averages establish the stated normalization.
For missing data, a useful sufficient route is a uniform expansion into
rowwise Gaussian noise plus a remainder r_i with
max_i |r_i| = o_P(sigma / sqrt(pr log n)). An ordinary coordinatewise
o_P(sigma/sqrt(pr)) error is not enough. Row observation counts concentrate
under the given strong logarithmic sample condition, but nuisance estimation
and dependence need proof. Xia-Yuan Theorem 1 is individual linear-form
normal approximation, not a simultaneous Gumbel theorem.

publish: main.conjectures.notes.c15.screen extreme-scale stochastic remainder
consumer: main.conjectures.c15
publish: main.conjectures.analysis.c15 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.education
consumer: main.conjectures.category.kind.analytic

### C16 A bounded-degree graph may supply the proof

For h distinct candidate sums, the forbidden pairs form a union of h
matchings, with maximum degree h. At the extreme location, the relevant
site interval has size O(q^-2 log(1/q)); the overlapping-edge probability
sum is therefore O_h(q log(1/q)), tending to zero. There are at most h
diagonal constraints, handled by forcing those sites absent. This suggests
uniform relative joint missing probabilities and a factorial-moment Poisson
proof, followed by first-moment tail truncation. It is a proof route,
not a completed proof in this review.

Finite front CDFs show substantial corrections: at x=0 the left front CDF
is .578, .505, .443 versus the proposed limiting .368, as q decreases.
These runs should not be advertised as an already accurate Gumbel fit.

publish: main.conjectures.notes.c16.screen matching-union proof route and finite corrections
consumer: main.conjectures.c16
publish: main.conjectures.analysis.c16 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.analytic
consumer: main.conjectures.category.kind.computational

### C17 Exact projection coefficients give a sharper test

Let P_s be C16's exact missing probability and L=floor(2u/q^2), with L<m.
For X_i the independent site indicator, the first-order projection is
sum_i a_i(X_i-q), where, for 0<=i<=L,

$$a_i=\sum_{s=i}^L\frac{-qP_s}{1-q^2}
 +{\bf1}_{2i\le L}\left(\frac{-P_{2i}}{1-q}
 +\frac{qP_{2i}}{1-q^2}\right).$$

This is E[Y|X_i=1]-E[Y|X_i=0]: an off-diagonal pair requires the partner
with probability q; a diagonal sum is forbidden by that site alone.
Exact rational enumeration of all 128 subsets at L=6,q=1/4 verified every
coefficient independently. The Gaussian kernel is a positive semidefinite
Gram integral; its asymptotic coefficient agrees with the exact formula.

The recorded experiments compare the full four-time covariance, exact
projection covariance, and residual, not just scalar deficit variance.
The scaled residual variance at u=4 falls .166 -> .087 -> .050.
The missing proof step is a uniform-in-u remainder/tightness bound, plus
tail control when passing from compact fringes to the full deficit.
The missing-sums paper's Proposition 5.1 and Section 6 provide second-moment
and leading concentration context; they do not alone establish this kernel.

publish: main.conjectures.notes.c17.projection exact coefficients and residual experiment
consumer: main.conjectures.c17
publish: main.conjectures.analysis.c17 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.analytic
consumer: main.conjectures.category.kind.computational

### C18 A CLT is weaker than the requested local limit

At fixed density bounded away from zero and one, the energy is a nonconstant
integer statistic for sufficiently large primes. Fixed cardinality removes
the first count fluctuation but does not automatically remove all relevant
contractions. The actual lattice gcd only identifies a containing lattice;
it does not fill its central holes. Establish the variance leading order,
then control the characteristic function away from lattice resonances.

publish: main.conjectures.notes.c18.screen lattice support and characteristic functions
consumer: main.conjectures.c18
publish: main.conjectures.analysis.c18 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.question

### C19 Arithmetic cycles may be manageable rather than fatal

A fixed collection of h unoriented differences gives an h-coloured graph
of maximum degree 2h. In the Bernoulli model at density about
sqrt(log(p)/p), shared-edge corrections are O_h(p q^3)=o(1).
This suggests uniform mixed rare-event estimates even for arithmetic
relations between the differences. Transferring to the fixed-size exposure
process and to several arrival thresholds still needs care. Check this
standard-method route before treating the process claim as a deep new target.

publish: main.conjectures.notes.c19.screen bounded-degree rare-event proof route
consumer: main.conjectures.c19
publish: main.conjectures.analysis.c19 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.analytic

### C20 Weak dependence must be controlled in the tail

The exact variance and opposite-difference identification pass the existing
enumeration. Fixed total autocorrelation is compatible with a Gumbel maximum
but rules out literal independence. One needs normal-tail accuracy at
sqrt(2 log N) and joint tail bounds for exceptional arithmetic tuples.
Marginal central limit theorems or pairwise covariance estimates are too weak.

publish: main.conjectures.notes.c20.screen moderate deviations rather than just a CLT
consumer: main.conjectures.c20
publish: main.conjectures.analysis.c20 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.additive
consumer: main.conjectures.category.kind.question

### C21 Rare conditioning must preserve the leading coefficient

For densities in a compact subinterval of (0,1/2), admissible peak counts
exist for large n. The existing exact counts are useful but small. A local
interaction tilt may explain why widely separated triples retain leading
coefficient 1/6 while nearby triples generate an order-n2 correction.
That is a mechanism to prove, not an established fact. First derive the
tilted model's correlation decay and its equivalence to fixed peak count.

publish: main.conjectures.notes.c21.screen tilt and conditional pattern coefficient
consumer: main.conjectures.c21
publish: main.conjectures.analysis.c21 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.order
consumer: main.conjectures.category.kind.question

### C22 A vanishing fraction of adjacent sites is not a full error bound

For a fixed permutation the conditional drift need not vanish identically.
The desired result requires it to be o_P(sqrt(m)) uniformly over time.
The crude number of adjacent selected pairs is O(m^2/n); dividing that
uncentered count by sqrt(m) only tends to zero when m=o(n^(2/3)).
This does not refute C22, but exposes why centered cancellation is essential
to cover its full m=o(n) range. The original annealed simulation misses this gate.

publish: main.conjectures.notes.c22.screen sparse-regime remainder threshold
consumer: main.conjectures.c22
publish: main.conjectures.analysis.c22 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.order
consumer: main.conjectures.category.kind.analytic

### C23 Entropy bounds give tightness, not a unique constant

The deterministic height/width bounds and known subsequence scales restrict
any beta to the given finite interval. They do not force a single limit.
The iid-point model is equivalent to a uniform permutation after sorting x;
it is not uniform sampling of labelled posets. The latter distinction matters
when searching the random-order literature. Seek an approximate additive or
variational argument plus concentration on scale o(n).

publish: main.conjectures.notes.c23.screen ensemble identity and second-order convergence
consumer: main.conjectures.c23
publish: main.conjectures.analysis.c23 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.order
consumer: main.conjectures.category.kind.question

### C24 Actual planar-order gaps now have a small experiment

For each sampled uniform permutation, enumerate its linear extensions and
construct I-P with precisely the candidate's lazy adjacent-swap rates.
Numerical eigensolver residuals were below 2.3e-12. This checks the actual
random planar ensemble, unlike the earlier two-chain illustration.

At n=6 and 8, all 24 samples were computed. At n=10, 6 of 24 were skipped
because they exceeded 10,000 extensions. The n=10 computed-sample median is
therefore censored and cannot be treated as an unbiased ensemble estimate.
These sizes do not determine a power exponent or deterministic constant.
Keep C24 high-risk and use an uncensored sampler or variational bounds next.

publish: main.conjectures.notes.c24.gaps small planar-order experiment with explicit censoring
consumer: main.conjectures.c24
publish: main.conjectures.analysis.c24 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.order
consumer: main.conjectures.category.kind.computational
consumer: main.conjectures.category.status.high-risk

### C25 Annealed bounds cannot replace a quenched free energy

On compact subsets of (0,2), the LIS lower bound gives exponentially many
witnesses on the sqrt(n) scale with high probability. The exact first moment
gives an upper bound by Markov. Their compatibility rules out one elementary
contradiction, but witnesses overlap heavily. A concentration or subadditive
argument must identify one deterministic profile and then control it uniformly
in alpha, not just pointwise along integer subsequence lengths.

publish: main.conjectures.notes.c25.screen witness overlap and uniform quenched convergence
consumer: main.conjectures.c25
publish: main.conjectures.analysis.c25 initial screen; specialist review remains unresolved
consumer: main.conjectures.category.status.unresolved
consumer: main.conjectures.category.topic.order
consumer: main.conjectures.category.kind.question

## Primary sources inspected in this pass

Only C01's sources establish its disposition here. The remaining comparisons
are bounded literature checks; missing specialist coverage remains open.

| Source | Passage inspected | Comparison |
|---|---|---|
| [Benjamini, Kalai, Schramm](https://www.numdam.org/article/PMIHES_1999__90__5_0.pdf) | Theorem 1.3, printed p.8 | C01 noise-sensitivity criterion |
| [Schramm, Steif](https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n2-p01-p.pdf) | Theorem 1.8, printed p.623 | C01 exact randomized revealment inequality |
| [Damron, Hanson, Sosoe](https://arxiv.org/pdf/1506.03461) | Crossing result, Corollary 3 and its proof context | Neighboring chemical-distance model; no pure-power limit clearance |
| [Garban, Pete, Schramm](https://arxiv.org/html/1305.5526) | Theorems 1.4-1.5 | Configuration/process scaling versus C04's derivatives |
| [Huang, McKenzie, Yau](https://arxiv.org/pdf/2412.20263) | Theorem 1.2 and following independence discussion | Regular graphs versus C07's irregular conditional ensemble |
| [Greenhill, Kwan, Wind](https://arxiv.org/html/1309.6710) | Theorem 1.2, Conjecture 1.3, proof discussion | Cubic result and general-degree qualification; not C09's residual |
| [Xia, Yuan](https://arxiv.org/pdf/1909.00116) | Theorem 1 and specific linear-form examples | Individual approximation versus C15's simultaneous extreme |
| [Limiting Behavior in Missing Sums of Sumsets](https://arxiv.org/html/2401.17254v1) | Proposition 5.1 and Section 6 | Fixed-density moment formulas and small-density concentration |

The generic searches did not transmit private statement text. Search snippets
were leads; the above comparisons are tied to primary passages. No absence
of search results is treated as evidence that a candidate is new.

## Evidence and reproduction

Before edits, all 26 fingerprints in the original checks file matched the
sanity producer and the 25 statement files. This verifies applicability of
those recorded observations, not the conjectures. The new experiment below
has its own producer and input hashes. C01's status-only update is tracked
separately from the immutable original input hash in its completed review.

New experiment command, from the project root:

```powershell
$env:OPENBLAS_NUM_THREADS='1'
python main.conjectures.analysis.experiments.py --root .
```

The numerical observations, all parameters, full covariance matrices,
permutation samples, skipped cases, and hashes are in
`main.conjectures.analysis.observations.json`. The mathematical findings
and finite observations have different evidential roles.

## Executed experiment summary

Seed 20261012; Python 3.14.6, NumPy 2.5.3, SciPy 1.18.1.
Each sumset row uses 1200 independent samples and
m=ceil(4 log(1/q)^2/q^2), an admissible asymptotic family.
The scalar full deficit has proposed scaled variance 8.

| q | m | q cubed times sample variance of full deficit | Scaled projection residual variance at u=4 |
|---|---:|---:|---:|
| 0.1 | 2,121 | 7.583572 | 0.165699 |
| 0.05 | 14,360 | 7.700699 | 0.087053 |
| 0.025 | 87,091 | 7.905653 | 0.050222 |

The Gaussian reference scale for the relative standard error of a variance
estimate is about 4.1 percent at 1200 samples. This is an orientation scale,
not a confidence interval: these data were not proved Gaussian. The observed
monotonicity across three q values is not a convergence theorem.

| n | Planar samples drawn | Gaps computed | Median n cubed times gap among computed samples |
|---|---:|---:|---:|
| 6 | 24 | 24 | 8.250466 |
| 8 | 24 | 24 | 8.122342 |
| 10 | 24 | 18 | 7.330161 |

The six skipped n=10 posets exceeded the extension cap. The last median
is conditional on being computable under that cap, with selection bias.
No exponent estimate is reported. FFT sumset counts were independently checked
against direct set addition on 60 small samples. Every computed transition
matrix was symmetric with zero generator row sums; all returned positive
gap eigenpairs passed the stated residual tolerance.

## Trace categories

The following IDs declare classifications used in this notebook. A finding
can consume several categories. They are textual classification and lineage,
not proof dependencies certified by Recur.

publish: main.conjectures.notes project-local editable findings notebook
publish: main.conjectures.category.topic.boolean Boolean functions and percolation
publish: main.conjectures.category.topic.spectral random matrices and random graphs
publish: main.conjectures.category.topic.witness matching topology and cover witnesses
publish: main.conjectures.category.topic.education hypothetical statistical measurement
publish: main.conjectures.category.topic.statistics simultaneous inference and conditional prediction
publish: main.conjectures.category.topic.additive random additive combinatorics
publish: main.conjectures.category.topic.order permutations and partial orders
publish: main.conjectures.category.kind.analytic mathematical derivations
publish: main.conjectures.category.kind.proof complete argument for its explicitly stated scope
publish: main.conjectures.category.kind.computational executed bounded computations
publish: main.conjectures.category.kind.literature primary-source comparisons
publish: main.conjectures.category.kind.counterexample explicit disproof examples
publish: main.conjectures.category.kind.question unresolved mathematical steps
publish: main.conjectures.category.kind.conjecture newly formulated unverified claims
publish: main.conjectures.category.status.implied consequence of existing theorems
publish: main.conjectures.category.status.unresolved mathematical disposition not settled
publish: main.conjectures.category.status.high-risk unresolved claim needing basic scale tests
consumer: main.conjectures.analysis.c01
consumer: main.conjectures.discovery.n01
consumer: main.conjectures.discovery.n02

## Historical Copilot notebook

The following text predates this review. Machine-specific paths have been
replaced with repository-relative references; its pending statuses describe
that earlier session. The active notebook is now this
project-local file; do not resume work by overwriting the historical original.

# Conjecture analysis notebook

Session-scoped review notes. This is a findings notebook, not a proof receipt or a record of private internal deliberation. Record concise mathematical explanations, explicit calculations, evidence, and unresolved questions.

## Review queue

Start with C07, C10, C24, C17, C15, then cover all remaining C01-C25 slots. The project contract is `main.conjectures.analysis.current.md`. Read the registered `conjecture-analysis\SKILL.md` before reviewing.

All review slices are pending. Candidate artifacts remain `.current`; review completion does not establish truth or novelty.

## Active subject: C07

**Candidate:** Independent Tracy-Widom edges after vertex thinning.

**Source:** `main.conjectures.c07.vertex-deletion-expansion.current.md`

**Review status:** Pending. The entries below summarize existing project evidence, not a new completed review.

### Exact target and assumptions

Uniform simple regular graph, degree approximately n^(1/5), independently retained vertices with fixed retention probability. Conditional on the labeled retained set and its degree sequence, compare the centered/standardized upper nontrivial and reflected lower normalized-adjacency eigenvalues with independent standardized real Tracy-Widom variables.

### Established checks

- Conditional uniformity among induced graphs with the same labeled degree sequence is exact: regular-completion constraints depend only on residual degrees.
- The earlier conditional-reference comparison was therefore tautological and has been withdrawn.
- The Perron eigenvalue 1 is excluded; normalization uses surviving degrees.
- Existing enumeration checks all 70 degree-2 regular graphs on six vertices and equal completion multiplicities across 23 feasible induced degree classes.

### Evidence boundary

These facts reject the previous formulation and check definitions. They do not support the replacement's asymptotic Tracy-Widom law or independence of its two edges.

### Open review questions

- Do existing prescribed-degree edge-universality theorems already imply this statement?
- Are conditional edge variances positive and their moments sufficiently controlled?
- Can degree fluctuations create localized extremes or dependence at the two edges?

### Primary literature record

Pending. For each source, record URL, theorem/section, exact hypotheses, and overlap with the candidate. Do not treat a search summary as a theorem.

### Disposition

Unresolved; no fresh specialist literature review has been performed here.

## Template for subsequent candidate notes

Copy this section for each stable candidate ID; keep separate review IDs `main.conjectures.analysis.cNN`.

### C__ — title

**Source path and hash:**

**Review status:** Pending / In progress / Review addressed

**Exact target and nonempty regime:**

**Analytic calculations and counterexamples actually checked:**

**Computations:** Command, producer hash, seed, parameters, results, and limitations.

**Primary literature:** URL, theorem/section, hypotheses, and exact comparison.

**Findings:** Retain / Revise / Reject / Known or implied / Unresolved, with a concise justification.

**Unresolved mathematical obstacle and next check:**

**Evidence versus heuristic:**

## Persistence boundary

This notebook belongs to the current session workspace. Accepted review findings should be integrated explicitly into project artifacts with their source hashes and trace IDs; saving a notebook is not accepting a Warp gate.

## Trace lookup and categories

Stable note IDs identify individual findings; shared category IDs group them.
Use categories `topic.spectral`, `kind.analytic`, `kind.computational`,
`kind.literature`, `kind.counterexample`, `kind.question`, and
`status.unresolved` under `main.conjectures.category` as applicable.
These are declared labels, not automatic mathematical judgments.
Trace roles describe where an ID is defined, published, or consumed; they do
not certify a finding or replace its explanation.

Historical context: this notebook originally lived outside the repository.
For the public copy, search the repository root:

```powershell
recur trace-id "main.conjectures.notes.c07.**" --scope "main.conjectures.**" -d "." --format full
recur trace-id "main.conjectures.category.kind.question" --scope "main.conjectures.**" -d "." --format full
```

### C07 conditional-uniformity finding

defines: main.conjectures.notes.c07.uniformity exact completion-count identity; previous target rejected as tautological
consumer: main.conjectures.c07
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.analytic

### C07 completion enumeration

defines: main.conjectures.notes.c07.completions finite enumeration supports the identity, not Tracy-Widom convergence
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.computational
consumer: main.conjectures.evidence

### C07 literature question

defines: main.conjectures.notes.c07.literature check whether prescribed-degree edge results imply the replacement
consumer: main.conjectures.category.topic.spectral
consumer: main.conjectures.category.kind.question
consumer: main.conjectures.category.status.unresolved

For later entries, give each finding its own heading and stable ID, then add
only applicable category lines. Read the returned site and surrounding section;
trace output is not a full-text faceted database and may classify one line into
multiple keyword roles.
