# Revision model v1

This note records the **first explicit revision model** for Knowledge OS object envelopes.

It is deliberately small.
It does not try to freeze the full protocol.
It does not introduce an overbuilt release-management system.
It does something narrower and more useful:

> it turns the current `revisions` field from an empty placeholder into a governed semantic revision rule.

---

## One-sentence ruling

Current ruling:

> **Every substantive object change must be revisioned.**
> **Revisions use a simple major/minor semantic model.**

That is the whole point of this note.

---

## Why this note exists now

`ARCHITECTURE.md` already names:

- `revisions: RevisionRef[]`
- a `revisions` table in the suggested core data model

That is enough to establish intent.
It is not enough to govern change.

Without a revision rule, later object editing will drift into ambiguity:

- what counts as a new revision,
- when a change is major versus minor,
- whether snapshots pin exact historical states,
- and whether operational metadata edits should be confused with semantic object evolution.

This note resolves that ambiguity at the first useful level.

---

## Current model

### 1. Every object has a current semantic version

The current object state should always correspond to a semantic revision identifier of the form:

```text
MAJOR.MINOR
```

Examples:

- `1.0`
- `1.1`
- `2.0`

### 2. Object creation starts at `1.0`

When an object is first created as a governed object, its first revision is:

```text
1.0
```

This is the first accountable semantic state of that object.

### 3. Revisions are append-only history, not mutable overwrite

A revision record should describe a semantic state transition in object history.

That means:

- older revisions remain addressable,
- the current object is the latest projection,
- revision history is not rewritten in place.

---

## Revision kinds

The current model uses two revision kinds only:

- **major**
- **minor**

This is intentionally enough for V1.

### Minor revision

A **minor** revision is used when the object remains the same governed object and its semantic identity is preserved.

Typical minor cases:

- wording clarification without changing claim meaning
- summary improvement
- body restructuring that preserves meaning
- source reference additions
- reproducibility detail additions
- link enrichment that does not change object-level relation semantics
- non-breaking evidence expansion
- non-breaking dissent elaboration
- rationale clarification on a verdict without changing verdict level or institutional stance

Rule:

```text
1.0 -> 1.1 -> 1.2
```

### Major revision

A **major** revision is used when the object remains historically continuous, but its governed semantic state changes enough that downstream readers must treat the new state as materially different.

Typical major cases:

- claim boundary change
- assumption set change that alters claim meaning
- target proposition re-scope
- verdict level change with materially different institutional standing
- evidence interpretation shift that changes what the object now asserts or supports
- dissent reframing that changes the actual challenge being made
- public-facing release meaning changes that would mislead downstream readers if treated as only a minor clarification

Rule:

```text
1.3 -> 2.0
2.4 -> 3.0
```

A major bump resets the minor counter to zero.

---

## What should not be treated as a revision bump by default

Not every object-related change needs to become a semantic revision.

The following may remain operational or audit-level events unless they alter governed semantic meaning:

- access-control changes
- visibility changes when they do not alter object meaning
- label changes for organization only
- assignment / review routing changes
- comment-only activity
- non-semantic formatting cleanup

These should still be logged.
They just should not be confused with semantic revision history unless they cross into meaning change.

---

## Snapshot rule

Snapshots should pin exact object revisions, not only floating object ids.

That means a snapshot should be interpretable as:

> this publication surface corresponds to these object states at these revision points.

This is essential for historical auditability.

---

## Relation to lineage

Revision history is **not** the same as lineage.

Keep these two ideas separate.

### Revision

Revision means:

- the same governed object evolving through accountable semantic states.

### Lineage

Lineage means:

- ancestry / descent relations between distinct objects or distinct release surfaces.

Examples:

- a claim can receive a major revision and still remain the same claim object,
- a claim can also split into descendants, in which case lineage is involved,
- a superseded claim should not be faked as merely a larger major bump if what actually happened is object descent.

This distinction matters.
Otherwise revision history will be forced to do lineage’s job and become muddy.

---

## Minimal revision record shape

The revision system does not need a large schema to start.
A minimal revision record can be described as:

```text
RevisionRef := {
  revision_id: string,
  object_id: string,
  version: string,        # e.g. 1.0, 1.1, 2.0
  revision_kind: "major" | "minor",
  parent_revision_id: string | null,
  changed_at: ISODateTime,
  changed_by: ActorRef,
  change_summary: string,
}
```

Optional later additions may include:

- compatibility note
- diff summary
- release note text
- linked action id

But those are not required for the first useful model.

---

## Current practical decision rules

When deciding whether a change is major or minor, ask:

### Minor test

Would a downstream reader still say:

> this is materially the same governed object making the same core semantic move,
> now stated more clearly or more fully?

If yes, it is probably **minor**.

### Major test

Would a downstream reader need to say:

> this object now means something materially different enough that treating it as a small clarification would be misleading?

If yes, it is probably **major**.

### Lineage test

Would a downstream reader instead say:

> this is no longer just the same object revised;
> this is now a split, descendant, supersession, or separately governed successor?

If yes, do **not** solve it only through revision bumping.
That is a lineage-level event.

---

## Practical verdict

So the practical verdict is:

- **`revisions` is no longer an empty placeholder concept**
- **new objects start at `1.0`**
- **minor = same object, same semantic identity, clearer or richer state**
- **major = same object, materially different governed semantic state**
- **lineage remains distinct from revision history**
- **snapshots should pin exact revisions**

That is the right size of rule for the current stage.
