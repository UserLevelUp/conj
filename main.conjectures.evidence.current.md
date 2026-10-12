# Mathematical evidence ledger

**Scope:** basic analytic checks, exact finite enumeration, numerical identities,
and bounded simulations. **C01 now has an implication proof from established
theorems in `main.conjectures.analysis.c01.complete.md`. The remaining 24
original statements are unresolved; no novelty clearance is claimed.**

The 2026-10-12 review notebook is `main.conjectures.analysis.notes.current.md`.
Version 0.2.0 adds the scoped C15 proof in
`main.conjectures.analysis.c15.subset.complete.md` and deterministic,
source-bound numerical checks in `docs/c15-checks.json`. The full C15 statement
and all original statement fingerprints remain unchanged.
New C16-C17/C24 experiments and exact projection verification are recorded
in `main.conjectures.analysis.observations.json` and
`main.conjectures.analysis.verification.json`. They do not prove their
asymptotic targets. The original observation file was preserved before its
fingerprints were refreshed for C01's status-only edit.

This ledger replaces the original portfolio's unsupported "no checks" state.
It distinguishes evidence about a proposal from checks of definitions,
necessary conditions, related examples, and counterexamples to withdrawn drafts.
Passing the script does not mean the 25 asymptotic statements passed a test.

## Reproduction and provenance

```powershell
python .\main.conjectures.sanity.py --output .\main.conjectures.checks.json
```

Producer: `main.conjectures.sanity.py`.
Observed environment: Python 3.14.6, NumPy 2.5.3.
Random seed: 20260701. No dependency installation was needed.
The generated JSON includes SHA-256 fingerprints of the producer and all 25
candidate statement files. Check those fingerprints before reusing results
after edits. Floating-point observations may vary slightly across numerical
libraries; rational enumeration is exact. NumPy FFT counts are rounded to
integers in the finite sumset experiments, with a transform length exceeding
the largest possible sum to prevent cyclic aliasing.

The script's assertions cover exact identities or specified numerical
tolerances. Simulation observations are **not** asserted to agree with
asymptotic constants, and do not implement hypothesis acceptance gates.

## Checks actually performed

| ID | Method and actual result | What remains unverified |
|---|---|---|
| C01 | Original tribes calculation retained. The 2026-10-12 review proves the full implication using symmetrized revealment, Schramm-Steif, and BKS. | No unresolved implication remains in this statement; it is not a new open target |
| C02 | A crossing needs order $n$ sites and a self-avoiding witness uses at most order $n^2$; the fully occupied example has a straight order-$n$ witness. These are analytic bounds, not a crossing experiment. | Exponent, pure-power normalization, limit distribution, moment convergence |
| C03 | Fourier covariance is a positive Laplace sum. For three-bit majority the weights are $3/16,1/16$ at spectral levels 1,3, giving variance $1/4$. Integration by parts relates a hypothetical $bu^{2/3}$ spectral tail to amplitude $b\Gamma(5/3)$. | Exact percolation spectral-tail amplitude and its long-time limit |
| C04 | Majority's median logarithmic slope derivative is zero. Its slope ratio one scaled unit away tends to $e^{-2}$; at $n=100001$ the ratio is .1353326, not 1. | Near-critical percolation $C^2$ convergence |
| C05 | On a fixed-seed 12-dimensional Gaussian matrix, finite-difference critical-response derivative is .83680176548 versus scaled overlap .83680176532; absolute error is below $10^{-6}$. | Cross-ensemble derivative-process universality |
| C06 | OU update preserves ensemble variance. A finite three-time fidelity matrix is symmetric, has unit diagonal, and entries in $[0,1]$ to numerical tolerance. Edge-gap/coupling comparison derives the $n^{-1/3}$ time scale. | The two-time field's universality |
| C07 | An irregular connected graph checks the Perron eigenvalue and own-degree normalization. A retained vertex has exact binomial degree. Exhaustive six-vertex regular completions check exact conditional uniformity, rejecting the preceding tautological target. | Conditional joint standardized Tracy-Widom edge law and edge independence |
| C08 | Tangency calculation checked for $r=2,3,4$, $d=10$: seed densities .005,.0298142,.0632574. The $r=2$ value is $1/(2d^2)$. The specified growing-degree regime has $np_*\to\infty$. | Regular-graph finite-size CDF, variance constant, median/tree agreement |
| C09 | Radius $\lfloor\log\log n\rfloor$ has vanishing birthday fraction, not a positive limiting one. Matrix-tree determinant for $K_4$ is exactly 16 to rounding tolerance. | Conditional residual variance and Gaussianity |
| C10 | Exact potential walk-path count $d(d-1)^{t-1}$ and the tree-conditioning collision scale were derived. No independent adaptive-collision claim is made; quantiles avoid assuming rare-history variance calibrates typical mixing fluctuations. | Joint conditional entropy/mixing law; especially high risk |
| C11 | Exponential isolation probabilities derived exactly. Nonconstant parity weights on 12 vertices give weighted vertex degrees 53.75 and 56.25, matching the formula. | Weighted perfect-matching hitting-time equality |
| C12 | Parity-weighted triangle construction gives weighted edge degrees 9.5,10,10.5 on 12 vertices. At critical time the isolated-edge expectation tends to $e^{-c}/2$, with the needed error precision derived. | Weighted homological hitting-time equality |
| C13 | Complete cyclic Latin-square enumeration gives 3 transversals at order 3 and 0 at order 4. Modular summation proves the even-order obstruction; every Latin coordinate has degree $n$ and pair-codegree at most 1. | Adversarial resilience in the uniform random ensemble |
| C14 | The directed-edge nonbacktracking transition on $K_{3,3}$ is doubly stochastic, checking the claimed stationary visit rates. Degree-2 cycles give the excluded linear cover-time counterexample. | Joint cover-time Gumbels and independence |
| C15 | A rank-2 centered-context example recovers row means with error $2.2\,10^{-16}$; its row-mean functional projection error is $1.0\,10^{-16}$ and squared norm is $1/16$. Complete-observation errors are exactly independent Gaussians. $k=n$ regret is exactly zero. | An efficient unknown-nuisance estimator and its uniform maximum-error law under missingness |
| C16 | All 128 subsets of a length-7 interval, weighted with $q=1/4$, match the exact missing-probability formula for every sum, including diagonal and reflected cases. | Gumbel front locations and their joint limit |
| C17 | Exact expectations and five 600-replicate deficit simulations are listed below. The first-order projection yields the proposed covariance kernel and per-fringe variance 4 analytically; the higher-order remainder was not bounded. | Functional Gaussian convergence and the limiting variance constant |
| C18 | All 462 size-5 subsets of $\mathbb F_{11}$: energy mean $215/3$, variance $1760/63$, lattice span 4. This verifies the statistic and nontrivial finite support. | $p^3$ variance order and the lattice local CLT |
| C19 | All subsets of $\mathbb F_7$: missing difference 1 equals independence in the seven-cycle. Independent-set counts by cardinality are $1,7,14,7$ for sizes 0-3. | The joint witness-arrival Poisson point process |
| C20 | All 462 size-5 subsets of $\mathbb F_{11}$ agree with exact nonzero autocorrelation mean 2 and variance $2/3$; opposite-difference duplication and the fixed sum are checked. | Dependent Gumbel maximum |
| C21 | All permutations at $n=4,6,8$ match unconditional 132 mean $\binom n3/6$. Conditional means are recorded below. | The scale-$n^2$, analytic, nonzero conditional response |
| C22 | All 24 orders of four labels give exact single-site descent-change variance $1/3$. 800 sparse-shuffle simulations at $n=2000,m=100$ record a three-time covariance matrix. | The quenched functional law for every $m=o(n)$ regime |
| C23 | Dynamic programming counts extensions for 20 fixed-seed planar orders on 8 points; every count lies between its height-layer factorial product and $w^n$. The antichain-followed-by-chain counterexample was derived explicitly. | A deterministic second-order random-planar entropy constant |
| C24 | Exact finite exclusion matrices for two chains, $n=4,6,8,10$, match $(1-\cos(\pi/n))/(n-1)$ within $10^{-12}$. Their $n^3$ gaps are 6.2484,5.7877,5.5677,5.4382. | The exponent and constant in the random planar ensemble |
| C25 | All 720 permutations of size 6 match increasing-triple mean $10/3$ and the LIS witness bound. Entropy lower/upper bounds are compatible at $\alpha=.5,1,1.5,1.9$. | Uniform quenched entropy-profile convergence; no edge-vanishing claim |

## Finite simulations: observations, not acceptance

For C17, the proposed asymptotic variance is
$q^3\operatorname{Var}D\to8$.
Each row below has 600 independent replicates of the **scalar full deficit**;
these experiments do not test the whole functional covariance kernel.

| $q$ | Interval length | Exact mean | Sample mean | $q^3$ sample variance |
|---|---:|---:|---:|---:|
| .2 | 3000 | 88.0000 | 88.2333 | 6.5135 |
| .15 | 3000 | 162.4444 | 162.5450 | 6.3326 |
| .1 | 3000 | 377.9999 | 377.6267 | 6.8516 |
| .05 | 20000 | 1558.0000 | 1555.3417 | 7.7392 |
| .025 | 80000 | 6318.0000 | 6345.6383 | 7.4949 |

The small-$q$ values are compatible with, but do not establish, the proposed
constant 8. The variance estimates are not monotone, and Monte Carlo error
and finite-$q$ corrections are not separated by these runs. No normality or
functional convergence conclusion follows from the table.

C22's simulation compares times $.25,.5,1$ with proposed covariance
$\min(s,t)/3$. The full empirical matrix and sample parameters are in the
JSON. This is an **annealed finite simulation**, not a quenched test conditional
on one fixed permutation and not a proof of tightness.

## Exact conditional permutation counts

| $n$ | Peaks | Number of permutations | Mean 132 count |
|---|---:|---:|---:|
| 4 | 0 | 8 | 0 |
| 4 | 1 | 16 | 1 |
| 6 | 0 | 32 | 0 |
| 6 | 1 | 416 | $40/13$ |
| 6 | 2 | 272 | $70/17$ |
| 8 | 0 | 128 | 0 |
| 8 | 1 | 7680 | $112/15$ |
| 8 | 2 | 24576 | $917/96$ |
| 8 | 3 | 7936 | $329/31$ |

These support correct centering and a genuine finite conditional response.
They cannot distinguish $n^2$ from another asymptotic correction scale.

## Rejected draft claims and material repairs

The refreshed C07 completion check enumerates all 70 simple degree-2 regular
graphs on six labeled vertices, retaining the fixed set $\{0,1,2,3\}$.
Across 23 feasible labeled induced degree sequences, it verifies that every
induced graph with a given sequence occurs with the same multiplicity and
that no graph with that sequence is omitted. This is a finite check of the
exact analytic completion argument, not an asymptotic edge-law experiment.

- C04: pointwise derivative control was falsely called equivalent to whole-window
  slope flatness. Majority explicitly contradicts that equivalence.
- C05-C06: an exact composition identity and an elementary stronger perturbation
  bound were inadequate advanced targets; they were replaced.
- C07: the full normalized spectral radius is 1. The first replacement was
  also rejected: conditional on labeled retained vertices and degrees,
  induced graphs have exactly equal regular-completion multiplicities.
  Cross-boundary/outside edges depend only on residual degrees, not the
  within-set adjacency. Thus comparison to a uniform degree-matched reference
  was tautological. The current replacement asks for independent standardized
  Tracy-Widom laws at both nontrivial spectral edges, with own-degree
  normalization. Exact conditioning uniformity is now established context,
  not a proposed conjecture.
- C08: corrected the missing $(r-1)/r$ seed-density factor and separated
  macroscopic activation from complete occupancy.
- C09-C10: removed an inconsistent radius regime, trivial scale/collision bound,
  and false adaptive independence language. Residual limits remain speculative.
- C11-C12: removed a suspect matching-median condition and fixed critical-window
  precision and isolated-edge constants. C11's displayed degree hypothesis
  now explicitly has the required additive error
  $+o(\binom{n-1}{k-1}/\log n)$; the prior missing plus sign was a defect.
- C13-C14: replaced an unsafe global deletion budget and unjustified lazy-walk
  cover ratio with precise ensembles, local budgets, and nonbacktracking units.
- C15: discarded the elementary minimax-regret claim, especially false sharpness
  at $k=n$. The replacement is simultaneous low-rank-nuisance inference with
  explicit identifiability, sample regime, and nontrivial selection quantifiers.
- C16-C20: withdrew false retained-size doubling and a vacuous popular-difference
  assertion. Exact lattice support, fixed-cardinality conditioning, opposite
  differences, and nonvacuous thresholds are now explicit.
- C23-C25: discarded the false universal-width entropy and gap bounds and the
  unsupported zero-entropy LIS-edge conclusion.

## Literature consulted and what it establishes here

| Primary source | Material actually consulted | Boundary |
|---|---|---|
| [Garban-Pete-Schramm, near-critical/dynamical scaling limits](https://arxiv.org/abs/1305.5526) | Primary HTML section on measurable mesoscopic networks and almost-sure stabilization; scaling-limit context | Not exact $C^2$ profile or long-time amplitude clearance |
| [Greenhill-Kwan-Wind, spanning trees](https://arxiv.org/abs/1309.6710) | Primary cycle-interaction section and its factorial-moment setup | No search-generated cycle coefficient was imported as a verified formula |
| [Janson-Luczak-Turova-Vallier, bootstrap on the binomial graph](https://arxiv.org/abs/1012.3535) | Primary Gaussian-limit proof section, including the bottleneck factor and process limit | Different random-graph ensemble from C08 |
| [Xia-Yuan, linear-form matrix-completion inference](https://arxiv.org/abs/1909.00116) | Primary introduction, variance/alignment conditions, individual linear-form inference, dependence discussion | Not a proof of C15's sharp simultaneous maximum law |
| [Limiting Behavior in Missing Sums of Sumsets](https://arxiv.org/abs/2401.17254) | Primary exact single-sum probabilities, mean formula, fringe-independence bound, second-moment discussion | These known baseline calculations are not new conjectures; C16-C17 propose additional limit structure |

Search results were used to locate sources, not to certify formulas. Some
summaries mislabeled percolation exponents, conflated two-sumsets with arbitrary
subset sums, or supplied unreliable constants. Such claims are not evidence.
The references above are not exhaustive literature reviews. A proposal may
already be proved, may be refuted by a specialist example, or may need further
hypotheses. Those uncertainties remain visible rather than concealed.

## Recur interpretation

The parent and six focused lanes recover intent, evidence locations, and next
mathematical questions. `tree`, `files`, and `trace-id` check discoverability.
Trace roles are keyword-classified textual relationships, not a formal proof
dependency graph. `consumer:`/`publish:` are used where the installed scanner
recognizes those roles; a scan does not certify mathematical implication.

These JSON observations are not a Recur Warp acceptance manifest. No Warp
completion record, mathematical acceptance contract, or proof receipt is
declared. That is deliberate: the artifacts are candidate proposals, and
their `.current` attention state cannot turn finite checks into truth.

defines: main.conjectures.evidence basic analytic and finite evidence ledger
publish: main.conjectures.evidence recorded observations and limitations
consumer: main.conjectures.portfolio candidate definitions under review
