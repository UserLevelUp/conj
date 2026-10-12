---
name: conjecture-analysis
description: Analyze candidate mathematical conjectures through precise quantifiers, nonvacuity, counterexample search, primary literature, and source-bound evidence. Use with this project's Recur analysis lane; never equate review completion with proof or novelty.
---

# Conjecture analysis

## Recover one bounded subject

Work in the authorized project root. Run `recur reveal main.conjectures.analysis`
and read `main.conjectures.analysis.current.md`, the relevant candidate, and its
focused domain capsule. Read the evidence ledger and inspect the generated
checks' source hashes before reusing observations. Reveal supplies pointers;
explicitly read this skill and the referenced artifacts.

Stable candidate IDs are `main.conjectures.c01` through
`main.conjectures.c25`. A review has its own identity
`main.conjectures.analysis.cNN`: a review is not the claim it examines.
Use tree/files/trace-id to recover evidence, not to infer truth.

## Four review gates

1. **Well-posedness and nonvacuity.** Specify probability space, deterministic
   and random inputs, all quantifiers, limits, conditioning, exceptional events,
   conventions, and normalization. Exhibit an admissible asymptotic regime.
   Check dimensions, sign, boundary cases, positivity of denominators, and
   whether an existential parameter can trivialize the claim.
2. **Analytic falsification.** Derive basic examples before simulating. Try
   extremizers, disconnected/planted structures, concentration of mass,
   degenerate parameters, exact symmetries, and conditional counting identities.
   Ask whether elementary algebra or an existing inequality already proves the
   target. An advanced-looking notation is not an advanced research question.
   Reject displayed counterexamples and tautologies, not merely annotate them.
3. **Primary-literature comparison.** Locate and read relevant theorem
   statements or proof sections. Record authors, source URL, theorem/section
   identifier where available, hypotheses, and the exact overlap or difference.
   Search summaries are leads only. Do not send private project content to
   third-party services. An unsuccessful search cannot establish novelty.
4. **Evidence-bound disposition.** Separate proved local facts, numerical
   identities, exact enumeration, simulation observations, heuristics, and
   planned checks. Give retain/revise/reject/known-or-implied/unresolved status
   with reasons. Identify the next genuinely unresolved mathematical step.
   Record statement and producer hashes, command, environment, seed, parameter
   range, and limitations for computational evidence.

## Computation and proof discipline

Use exact rational enumeration when feasible, existing tools rather than
unnecessary installations, and deterministic seeds for experiments.
Check the requested observable rather than an easier proxy. Do not infer
quenched limits from annealed simulations, functional convergence from one
variance, independence from correct marginals, or asymptotic truth from finite
agreement. Do not claim a computation was performed unless its output exists.
Avoid guessed centering constants whose error can exceed a critical window.

Clearly distinguish a counterexample to an old draft from evidence about its
replacement. If a claim changes, retain the rejection rationale, update related
index/lane surfaces, and refresh affected source-bound observations. Do not
silently preserve a rejected claim to maintain the portfolio count.

## Review receipts, trace lineage, and Eventness

A completed review addresses the gates honestly; it need not prove the
conjecture. A negative or unresolved mathematical disposition can be an accepted
review outcome. Record real missing inputs as blockers; "unproved" alone is not
an operational blocker.

Keep candidate artifacts `.current` during scrutiny. Use `.strange` for a
specific unexpected finding and `.blocked` for a named obstacle.
Only mark an explicitly scoped review artifact or receipt `.complete`;
never imply that this proves its candidate. Preserve historical receipts when
source changes make them stale.

In actual review artifacts declare their review ID, use
`consumer: main.conjectures.cNN` for the examined candidate, and
`publish: main.conjectures.analysis.cNN` for the recorded disposition.
Planned reviews have no produced receipts. Installed trace keyword matching is
textual lineage, not a formal mathematical dependency proof.

Do not create/dispatch/accept Warp work merely because this skill or a capsule
mentions it. Inspect installed help, user authorization, preview output, and
the actual map before any lifecycle mutation. Review slices are independent
except for real prerequisites; final portfolio integration depends on all 25.

## Project boundaries

Alignment must name its comparison, normalization, and allowed symmetries.
Mathematical eventness means the defined witness/threshold transition; Recur
Eventness means recorded attention. Neither is a certificate of truth.

C15's user-requested hypothetical education/attention model is mathematical,
not clinical or empirical. Do not infer diagnoses, intelligence, real-world
eligibility, or high-stakes assessment policies from it.

Remain explicit about truth, exact novelty, open status, and significance being
unverified. Claim proof only when a complete valid argument has been established.
