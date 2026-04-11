# Record consistency check floor v1

This note records the **first minimal consistency-check floor** for the protocol layer.

It exists to make the current grammar family more than elegant prose.

At the current stage, the system now has:

- a working object envelope,
- a compact relation grammar,
- a compact verdict grammar,
- and a first transition-admissibility rule.

That is enough to say something harder:

> some protocol commitments should now be treated as checkable obligations rather than only documentation.

---

## One-sentence ruling

Current ruling:

> **Object envelopes, relation records, and verdict records must now satisfy a small shared consistency floor.**
> **If they do not, later governance language will drift faster than the system can trust its own graph.**

That is the whole point of this note.

---

## Why this note exists now

The repository has crossed an important threshold.

It no longer only has:

- founding language,
- a pilot page,
- and loosely suggestive protocol notes.

It now has named rules for:

- revision,
- action families,
- relation types,
- verdict levels,
- and transition admissibility.

Once that happens, a new failure mode appears:

> the documents may become sharper while the records underneath still quietly contradict them.

This note exists to stop that.

---

## Scope

This note governs the first compact consistency floor across three layers:

### A. object envelope

The frontmatter-bearing governed object shape described in:

- `protocol/object-envelope.md`

### B. relation record

The minimal typed relation shape implied by:

- `object-relation-grammar-v1.md`

### C. verdict record

The minimal verdict-bearing shape implied by:

- `verdict-grammar-v1.md`

At the current stage, these may still live in markdown object files rather than a fully separated database schema.
That is acceptable.
The consistency floor still applies.

---

## What this note does **not** try to do yet

This note does **not** attempt to prove:

- that the content of a claim is true,
- that support pressure is sufficient in substance,
- that every transition burden is fully quantified,
- or that the full graph ontology is finished.

It checks something smaller:

> whether the current records are at least typed, aligned, and non-contradictory at the first useful level.

---

## First minimal consistency obligations

The following obligations should now be treated as the first hard check floor.

### 1. object id / object type coherence

If an object uses the current pilot-style id family, the id prefix should cohere with `object_type`.

Current pilot expectation:

- `C-` -> `claim`
- `E-` -> `evidence`
- `D-` -> `dissent`
- `V-` -> `verdict`

This is not eternal law.
But while the repository still uses this convention, violating it should be a consistency failure.

### 2. required envelope fields must exist

At the current stage, every governed object should have at least:

- `id`
- `object_type`
- `title`
- `lifecycle_state`
- `visibility`
- `links`

Claim-like objects should additionally carry governed epistemic reading where required by the current pilot.
Verdict objects should carry governed verdict reading where required by the current pilot.

### 3. link targets must resolve

Every object-level typed link or relation reference should resolve to a real governed target object id, unless the target is explicitly declared to be an external source proxy or release-surface proxy.

No dangling target ids.
No ghost objects.

### 4. relation type must be canonical or explicitly migrated

At the current stage, canonical relation types are now defined by the compact relation floor:

- `supports`
- `challenges`
- `cites`
- `depends_on`
- `descends_from`
- `supersedes`
- `pinned_in_snapshot`

Current rule:

- a record should either use one of these canonical names,
- or the repository must explicitly declare a lawful migration alias table.

Silently mixing canonical relation names with older pilot-local names is now a consistency problem.

### 5. mirrored reverse names should not be primary canonical graph edges

Names such as:

- `supported_by`
- `attacked_by`
- `cited_by`
- `ruled_on`

may still exist temporarily in older pilot materials.
But they should not remain the primary canonical graph language once a directed canonical floor has been named.

Current rule:

- reverse views may exist as derived presentation semantics,
- but the governed graph should prefer one canonical direction.

### 6. verdict target must point to a claim

A verdict record must name a real target claim.

Current rule:

- `target_claim_id` must resolve,
- and it must resolve to an object whose `object_type` is `claim`.

A verdict does not target a vague neighborhood in the abstract.
It targets a claim.

### 7. verdict level must belong to the verdict floor

At the current compact stage, lawful verdict levels are:

- `under_evaluation`
- `supported`
- `contested`
- `weakened`
- `rejected`
- `stabilized`

Anything else should currently fail unless a project-specific extension is explicitly declared.

### 8. nontrivial verdicts need basis

If a verdict level is stronger than `under_evaluation`, then it should not float basis-free.

Current rule:

- verdicts at `supported`, `contested`, `weakened`, `rejected`, or `stabilized` should carry at least one resolvable basis object id.

This does not prove the verdict is correct.
It only proves that the verdict is not pretending to be basisless authority.

### 9. basis refs must resolve and remain type-legible

Every verdict `basis_object_id` or pilot `basis_ref` should resolve to a real governed object.

At the current stage, lawful basis objects will usually be drawn from:

- `evidence`
- `dissent`
- `claim`
- and in some cases prior `verdict` objects where the project explicitly allows that layer.

A missing basis target is a consistency failure.

### 10. lineage and succession cannot be self-relations

For:

- `descends_from`
- `supersedes`

current rule:

- source and target may not be identical,
- because a claim cannot descend from or supersede itself.

If that appears, something upstream is malformed.

### 11. publication membership must not impersonate verdict

If a record uses:

- `pinned_in_snapshot`
- or other public-surface pin semantics,

that relation must not be interpreted as verdict-bearing on its own.

This is partly semantic, but one checkable form already exists:

- publication-pin relations should not be the only basis objects cited for a substantive verdict.

### 12. transition-sensitive verdict changes need explicit from/to trace

Where a project begins to record verdict movement explicitly, a verdict change should not appear as a silent rewrite.

Current rule:

- if the repository records verdict transitions, it should preserve at least:
  - `from`
  - `to`
  - `target_claim_id`
  - and basis/rationale trace

This obligation may initially be enforced at the note/process level before it becomes a code checker.

---

## First check classes

At the current stage, the most useful checker classes are:

### A. hard fail

Use hard fail for:

- missing required envelope fields,
- unresolved target ids,
- unknown verdict levels,
- verdict targeting non-claims,
- basis refs pointing nowhere,
- self-lineage or self-supersession,
- structurally malformed typed links.

### B. warning

Use warning for:

- legacy relation aliases still present,
- mirrored reverse names still being authored directly,
- claim objects carrying stale local status wording that has not yet been migrated,
- verdicts whose rationale is too thin even though a basis exists.

### C. future hardening candidates

Reserve later hardening for:

- transition burden quantification,
- relation-strength qualifiers,
- release-surface consistency against pinned revisions,
- theorem-grade or domain-specific verdict ladders.

---

## Immediate repository finding

This note already surfaces one real current consistency risk:

- `protocol/object-envelope.md` still shows legacy example links such as `supported_by`,
- and `protocol/link-types.md` still preserves a wider older working set including names like `attacks`, `supported_by`, `splits_from`, and `published_as`.

That does **not** mean the repository is broken.
It means the repository has now crossed into a stage where:

> legacy pilot vocabulary and newly named canonical grammar can no longer be allowed to drift past each other silently.

This is exactly the kind of thing the first check floor should catch.

---

## Minimum checker output shape

A future checker built from this note does not need a huge framework.
A compact output shape would already be enough:

```text
ConsistencyCheckResult := {
  status: "passed" | "warnings" | "failed",
  hard_failures: string[],
  warnings: string[],
  checked_objects: string[],
  checked_relations: string[],
  checked_verdicts: string[],
}
```

That is sufficient for the first useful machine-legible pass.

---

## What this note does **not** claim

This note does **not** claim that:

- a full checker already exists,
- the repository has already migrated every legacy relation name,
- the protocol is frozen,
- or consistency checking can replace governance judgment.

It claims something smaller:

> the grammar family has now matured enough that some contradictions should officially count as checkable failures rather than stylistic looseness.

---

## Practical verdict

So the practical verdict is:

- **the protocol layer now has a first shared consistency floor**
- **object envelopes, relation records, and verdict records can no longer drift independently without being treated as a governance problem**
- **legacy relation vocabulary has now become an explicit migration issue rather than harmless variety**
- **the next natural step is an actual checker that enforces this floor against live pilot records**

That is the right size of hardening for the current stage.
