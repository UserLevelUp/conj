# Help turn a question into mathematics

A proof, counterexample, or precise reference to an existing theorem is equally welcome.
Start with a [candidate in the atlas](docs/atlas/README.md), then read its full statement and the [review notebook](main.conjectures.analysis.notes.current.md).

## Useful contributions

- **Literature:** cite a primary source and theorem number; compare every relevant hypothesis and normalization.
- **Counterexample:** specify the admissible regime and show exactly which conclusion fails.
- **Proof:** give a complete argument, with references for every imported result.
- **Computation:** include code, seed, parameters, environment, input hashes, and limitations.
- **Sharper statement:** explain what changed, why the old version failed, and what remains unresolved.

Use the candidate ID in the issue or pull-request title, for example `C17: a bound on the projection remainder`.
Keep the existing C01–C25 addresses stable. New candidates belong in the discovery lane; they do not silently replace a rejected claim.

## Status and evidence

`Unresolved in this project` does not mean `known to be open in the literature`.
The six priority tags express a review judgment, not a novelty certificate.
Finite data do not establish an asymptotic limit. Correct marginals do not establish independence.
The original generation used GitHub Copilot; subsequent revisions and review used ChatGPT/Codex.
Human mathematical scrutiny is the point of publishing this project.

Record findings in the notebook with the source, argument, disposition, next check,
and an explicit trace role. A candidate and its review have separate identities:

```text
consumer: main.conjectures.c17
publish: main.conjectures.notes.c17.your-finding concise description
consumer: main.conjectures.category.kind.analytic
consumer: main.conjectures.category.status.unresolved
```

`.current` records attention. A `.complete` review records the scope actually
completed; neither is a generic certificate of truth. See the
[analysis skill](conjecture-analysis/SKILL.md) for the four review gates.

## Reproduce and validate

```bash
python -m pip install -r requirements.txt
python -c "from pathlib import Path; Path('work').mkdir(exist_ok=True)"
python tools/verify_evidence.py
python main.conjectures.sanity.py --output work/checks.json
python tools/build_atlas.py
python tools/check_publication.py
```

Create `work/` before writing experimental outputs. The README also gives the
longer experiment command. Keep the recorded baseline files intact unless you
deliberately refresh evidence and explain the new environment and fingerprints.
Illustrations must say whether they are a toy example, a proposed law, or measured data.
