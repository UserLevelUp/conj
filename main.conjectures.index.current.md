# 25 original mathematical conjecture slots

**Review update, 2026-10-12:** C01 follows from existing theorems; the other
24 original statements remain unresolved after an initial screen. Read
[the editable analysis notebook](main.conjectures.analysis.notes.current.md)
for current dispositions and [the C01 proof](main.conjectures.analysis.c01.complete.md).
[Two discovery leads](main.conjectures.discovery.current.md), N01 and N02,
are separate from these 25 original slots and have unverified truth and novelty.
Recover them with `recur reveal main.conjectures.discovery`.

**Exactly 25 proposals are persisted here.** These are research-level candidate
statements constructed for this project, not certified new open problems.
Except for the C01 implication now proved from known theorems, truth,
exact novelty, and significance remain unresolved; no comparison with
the importance of landmark solved conjectures is warranted.

The first draft contained substantive errors. This revision replaces false,
vacuous, ill-defined, or elementary targets rather than preserving them behind
caveats. Every proposal now has definitions, quantifiers, an explicit
alignment/eventness interpretation, actual basic calculations, neighboring
context, and a falsification route. Calculations do not prove the proposals.

## Alignment and mathematical eventness

Two objects are **aligned only relative to a specified comparison rule**:
overlap, correlation, conditional law, profile convergence, witness preservation,
or synchronized hitting times. **Misalignment** is the corresponding residual
or failure, with its normalization stated in the individual artifact.
There is no cross-domain universal alignment score, and alignment does not mean
truth or moral goodness.

Mathematical eventness means a formally specified change such as witness
arrival, a threshold crossing, spectral memory loss, or a last-obstruction
disappearance. Recur Eventness is different: `.current` marks active review.
No candidate is marked `.complete`, and no mathematical acceptance receipt is
claimed.

## Lane recovery

With Recur installed, run `python tools/init_recur.py` once in a fresh clone.
Then run these from the repository root, or pass that directory with `-d`:

```powershell
recur reveal main.conjectures
recur reveal --type lane
recur reveal main.conjectures.additive
recur tree main
recur files "main.conjectures.**"
recur trace-id "main.conjectures.c*" --scope "main.conjectures.**" --format summary
```

The parent lane owns the count, evidence boundary, and index. Six focused lane
capsules recover the mathematical work without loading the entire portfolio:
`boolean` (C01-C04), `spectral` (C05-C10), `witness` (C11-C14),
`education` (C15), `additive` (C16-C20), and `order` (C21-C25).
They organize review; they do not certify mathematical results.
Historical candidate filenames are retained as stable addresses even where
the mathematical target changed. Titles and this index are authoritative.

## Recommended next Warp

[Conjecture analysis](main.conjectures.analysis.current.md) proposes one
review slice per candidate and a final integration slice. Recover it with
`recur reveal main.conjectures.analysis`. Start with C07, C10, C24, C17,
and C15, then cover every remaining slot. Gates are well-posedness,
falsification, primary-literature overlap, and a source-bound disposition.
This is a recommendation, not a created/dispatched Warp or accepted review.
The original statement paths retain `.current` as stable addresses. C01 has
a completed source-bound review; the remaining specialist reviews are open.
No Warp map or accepted gate receipts are implied by this notebook work.

## The 25 proposals

| ID | Candidate | Specified comparison/event |
|---|---|---|
| C01 | [Near-extremal exact-query efficiency](main.conjectures.c01.revealment-pivotal-clusters.current.md) | Algorithmic efficiency versus persistence under fixed resampling noise |
| C02 | [Shortest critical crossing witness](main.conjectures.c02.certificate-dispersion-threshold-width.current.md) | Conditional certificate-length distribution across mesh scales |
| C03 | [Exact long-time crossing-memory amplitude](main.conjectures.c03.noise-stability-certificates.current.md) | Spectral-sample lower tail versus dynamical memory decay |
| C04 | [Differentiable near-critical crossing profiles](main.conjectures.c04.product-threshold-curvature.current.md) | Probability, pivotal intensity, and curvature in a common continuum profile |
| C05 | [Critical spike derivative universality](main.conjectures.c05.composition-critical-window.current.md) | Eigenvalue-response curves and spike-overlap derivatives in $C^1$ |
| C06 | [Dynamic critical spike fidelity](main.conjectures.c06.spectral-resilience.current.md) | Two-time eigendirection field versus Gaussian-reference dynamics |
| C07 | [Independent Tracy-Widom thinning edges](main.conjectures.c07.vertex-deletion-expansion.current.md) | Both nontrivial spectral edges versus a specified independent Tracy-Widom pair |
| C08 | [Growing-degree bootstrap profiles](main.conjectures.c08.bootstrap-nonbacktracking.current.md) | Activation-density transition versus tree bifurcation and Gaussian calibration |
| C09 | [Cycle-conditioned spanning-tree residual](main.conjectures.c09.local-trees-spanning-trees.current.md) | Unexplained tree entropy versus a conditional Gaussian law |
| C10 | [Joint mixing and tree-entropy fluctuations](main.conjectures.c10.expansion-diameter.current.md) | Conditional dynamical/topological residual independence |
| C11 | [Weighted matching hitting times](main.conjectures.c11.hypergraph-matching-window.current.md) | Perfect matching arrival versus last isolated vertex |
| C12 | [Weighted homological hitting times](main.conjectures.c12.isolated-faces-homology.current.md) | Global homology vanishing versus last isolated edge |
| C13 | [Resilient random Latin transversals](main.conjectures.c13.codegree-matching-resilience.current.md) | Local adversarial fault budgets versus global witness survival |
| C14 | [Joint nonbacktracking cover extremes](main.conjectures.c14.neighborhood-cover-connectivity.current.md) | Two stationary visit rates versus independent last-visit laws |
| C15 | [Simultaneous mastery inference](main.conjectures.c15.education-attention-alignment.current.md) | Context-averaged mastery rank versus low-rank-nuisance-adjusted inference |
| C16 | [Extreme missing-sum fronts](main.conjectures.c16.energy-popular-sums.current.md) | Two additive fringe extremes versus independent Gumbel variables |
| C17 | [Sparse sumset deficit field](main.conjectures.c17.thinning-near-minimal-sumsets.current.md) | Missing-sum profiles versus an explicit Gaussian covariance kernel |
| C18 | [Fixed-cardinality energy local limit](main.conjectures.c18.energy-progression-witness.current.md) | Collision-count point probabilities versus a lattice-corrected Gaussian |
| C19 | [Difference-witness arrival process](main.conjectures.c19.cyclic-difference-coverage.current.md) | Arrival times versus a Poisson point process |
| C20 | [Extreme random-set autocorrelation](main.conjectures.c20.fourier-popular-differences.current.md) | Largest additive overlap versus a nonvacuous dependent-extreme calibration |
| C21 | [Peak-conditioned pattern response](main.conjectures.c21.peaks-pattern-emergence.current.md) | Local-extrema constraint versus analytic global pattern response |
| C22 | [Quenched sparse-shuffle descent response](main.conjectures.c22.resampling-descents.current.md) | Original/reshuffled profiles versus Brownian covariance $\min(s,t)/3$ |
| C23 | [Random planar-order entropy](main.conjectures.c23.poset-width-extension-entropy.current.md) | Extension count versus deterministic second-order entropy |
| C24 | [Random planar extension relaxation](main.conjectures.c24.poset-connectivity-certificates.current.md) | Legal-swap geometry versus a conjectured $n^{-3}$ relaxation constant |
| C25 | [Quenched increasing-witness entropy](main.conjectures.c25.pattern-containment-revealment.current.md) | Pattern counts versus a uniform deterministic interior profile |

C15 preserves the user's hypothetical attention/education question. It is a
mathematical measurement model, not a statement that ADHD implies a particular
ability, outcome, or assessment prescription in the real world.

## Evidence and limitations

Read [the evidence ledger](main.conjectures.evidence.current.md), the
[reproducible check script](main.conjectures.sanity.py), and its
[generated observations](main.conjectures.checks.json).

```powershell
python .\main.conjectures.sanity.py --output .\main.conjectures.checks.json
```

The script uses Python and NumPy, a fixed seed, exact rational enumeration where
feasible, numerical identity checks, and two finite simulation families.
Generated observations fingerprint the script and the 25 statement artifacts.
Some checks deliberately refute the withdrawn draft or test a neighboring
identity; these are NOT experiments verifying the replacement asymptotic claim.
C10 and C24 are explicitly high-risk. C17's first-order kernel has not had its
higher-order remainder proved. Finite evidence is not proof.

Primary material was consulted for near-critical percolation, spanning-tree
cycle interactions, matrix-completion linear-form inference, binomial-graph
bootstrap analysis, and random-sumset moments. These establish related context,
not exact novelty clearance. Search summaries with incorrect formulas were
not treated as authoritative. Several proposals may already follow from
specialist literature; none is advertised as assuredly novel or open.

## Recur lineage

defines: main.conjectures.portfolio exactly 25 candidate statements, not 25 accepted results
consumer: main.conjectures.evidence exact calculations and bounded finite observations
consumer: main.conjectures.analysis next recommended review contract
consumer: main.conjectures.notes current review notebook
consumer: main.conjectures.discovery new candidates distinct from original slots
consumer: main.conjectures.c01
consumer: main.conjectures.c02
consumer: main.conjectures.c03
consumer: main.conjectures.c04
consumer: main.conjectures.c05
consumer: main.conjectures.c06
consumer: main.conjectures.c07
consumer: main.conjectures.c08
consumer: main.conjectures.c09
consumer: main.conjectures.c10
consumer: main.conjectures.c11
consumer: main.conjectures.c12
consumer: main.conjectures.c13
consumer: main.conjectures.c14
consumer: main.conjectures.c15
consumer: main.conjectures.c16
consumer: main.conjectures.c17
consumer: main.conjectures.c18
consumer: main.conjectures.c19
consumer: main.conjectures.c20
consumer: main.conjectures.c21
consumer: main.conjectures.c22
consumer: main.conjectures.c23
consumer: main.conjectures.c24
consumer: main.conjectures.c25
