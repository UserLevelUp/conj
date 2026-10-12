# Next recommended Warp: conjecture analysis

**Eventness:** active review. An initial screen of all 25 statements and a
completed C01 implication review are recorded in
`main.conjectures.analysis.notes.current.md`; 24 specialist reviews remain
unresolved. This is not an executed or accepted Warp.
The restricted C15 proof is now in
`main.conjectures.analysis.c15.subset.complete.md`; this does not complete the
full C15 review or change the count of unresolved original claims.
**Recommended Warp ID:** `main.conjectures.analysis`.
**Goal:** give each of C01-C25 an evidence-bound mathematical review and
integrate its disposition without confusing review completion with proof.

Recover with `recur reveal main.conjectures.analysis -d .`.
Load the local guidance with `recur reveal conjecture-analysis`, then explicitly
read `conjecture-analysis\SKILL.md`; reveal does not load the skill automatically.
No bubble map, worker dispatch, or acceptance layer has been created by this
recommendation. The installed `recur-warp create` supports a preview before
confirmed creation; the preview must be inspected and its proposed slices
adapted to this contract before any confirmed write.

## Scope and gates for every candidate slice

One slice per stable candidate ID, with these four gates:

1. **Well-posedness:** restate the exact hypotheses, limits, conditioning,
   normalizations, observables, and conclusion. Exhibit a nonempty asymptotic
   regime. Check exceptional cases and identify which assumptions are essential.
2. **Falsification:** derive at least one pertinent model calculation and attack
   an adversarial or degenerate example. Distinguish checks of the proposed
   conclusion from checks of its definition or a withdrawn predecessor.
   Record counterexamples, vacuity, exact identities, and elementary implications.
3. **Literature overlap:** inspect primary statements, not search summaries.
   Record URLs, theorem/section identifiers where available, exact hypotheses,
   and a comparison with this candidate. An incomplete search means novelty
   remains unverified; it is not evidence of novelty.
4. **Disposition and evidence:** give a reasoned disposition: retain as a
   candidate, revise, reject, known/implied, or unresolved. List checked facts,
   heuristic steps, unperformed experiments, and the next mathematical obstacle.
   Bind the review to the statement's content hash and evidence version.

Review acceptance means these gates were addressed honestly with an auditable,
recoverable record of findings, not that the conclusion is true, new,
important, or proved. A negative review
can be a successfully completed analysis slice. A missing proof is not itself
a blocker; missing inputs, inaccessible primary material, or an unverified
critical calculation can be blockers for a particular gate.

## Proposed slices and first attacks

The C01 review is complete in `main.conjectures.analysis.c01.complete.md`.
The other specialist review slices remain **pending**, with initial findings
in the notebook. Order below is suggested attention
priority, not a dependency graph. Each consumes its own candidate and the
existing evidence ledger. C05-C06 and C09-C10 require reading their shared
definitions, not acceptance of a sibling review.

| Slice | Lane | First mathematical pressure |
|---|---|---|
| C07 | spectral | Prescribed-degree joint edge universality; exact conditional uniformity is already proved context, not a target |
| C10 | spectral | Positive conditional scales, rare-history effects, mixed entropy/mixing tails |
| C24 | order | Test the conjectured random-planar relaxation exponent before targeting a constant |
| C17 | additive | Bound higher-order projection remainder and verify the whole covariance kernel |
| C15 | education | Identifiability with missingness and sharp uniform simultaneous-inference literature |
| C01 | boolean | Can established query/revealment inequalities already imply the noise claim? |
| C02 | boolean | Pure-power versus logarithmic corrections for shortest critical crossings |
| C03 | boolean | Exact spectral-tail amplitude versus exponent-only results |
| C04 | boolean | Justify derivative-limit interchange and control second-order pivotals |
| C05 | spectral | Existing critical spike process and eigenvector results in derivative topology |
| C06 | spectral | Short-time initial-law memory and tiny-gap fidelity effects |
| C08 | spectral | Regular-ensemble critical fluctuation scale and growing-degree uniformity |
| C09 | spectral | Conditional residual variance and quantitative growing-cycle errors |
| C11 | witness | Weighted perfect-matching hitting-time theorems and partition barriers |
| C12 | witness | Weighted cocycles beyond isolated edges and precise degree calibration |
| C13 | witness | Adversarial row/column/symbol partition barriers below the local cap |
| C14 | witness | Return clusters and dependence between last visits on opposite sides |
| C16 | additive | Missing-sum clustering and a possible nonunit extremal index |
| C18 | additive | Fixed-cardinality chaos variance and persistent lattice support holes |
| C19 | additive | Multi-difference arithmetic cycles and process-level novelty |
| C20 | additive | Moderate deviations and dependence among autocorrelation extremes |
| C21 | order | Does rare peak conditioning change the leading pattern coefficient? |
| C22 | order | Quenched drift and tightness across every sparse-shuffle regime |
| C23 | order | Known second-order planar-order entropy results and concentration |
| C25 | order | Existing quenched witness free energies and overlap-induced nonconcentration |

**Integration slice:** depends on all 25 review slices. Reconcile dispositions
with the index, focused lane capsules, trace lineage, and evidence ledger.
Do not silently replace a rejected candidate merely to preserve the count:
record the rejection and the replacement rationale, then review the replacement.
The portfolio must retain exactly 25 candidate slots, but no slot is guaranteed
to contain a viable research target before this analysis.

## Eventness transitions and lineage

- Candidate artifacts stay `.current` while their claims are being scrutinized.
- `.strange` may mark a concrete unexpected finding, not mere speculative risk.
- `.blocked` requires a named operational/input obstacle, not "unproved."
- `.complete` is reserved for an explicitly scoped completed review artifact or
  accepted review receipt; never use it to suggest an unproved claim is settled.
- A revised statement invalidates the old review's freshness, not its history.
  Keep hashes and rerun only the checks affected by the revision.

Future reviews should use distinct trace IDs
`main.conjectures.analysis.cNN`, consume `main.conjectures.cNN`, and publish
their review disposition under that analysis ID. C01 now has such an artifact;
no Warp acceptance receipts exist. No planned output is represented as produced evidence.

The bounded `warp.slicing` prompt inspected during this recommendation was
truncated (four-file/12000-byte budget). It supplied general gate guidance,
not a complete portfolio assessment. The proposed slice coverage above comes
from the persisted 25-entry index and its explicitly recorded pressure points.

defines: main.conjectures.analysis proposed 25-slice mathematical review contract
consumer: main.conjectures.portfolio
consumer: main.conjectures.evidence
consumer: main.conjectures.analysis.skill
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
