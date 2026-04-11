# Object relation grammar v1

This note records the **first compact relation grammar** for Knowledge OS.

It is intentionally small.
It does not attempt a full graph ontology.
It does not define every future relation.
It does something narrower and more useful:

> it gives the current system a governed way to name the first relation families,
> say which ones matter for verdict interpretation,
> and stop revision, lineage, publication, and citation from collapsing into one blurry edge soup.

---

## One-sentence ruling

Current ruling:

> **Relations are first-class governed graph semantics, not anonymous links.**
> **The current core floor is deliberately small: evidentiary, citation, dependency, lineage, succession, and publication-pin relations.**

That is the whole point of this note.

---

## Why this note exists now

`ARCHITECTURE.md` already says:

- the system is a governed object graph,
- the graph is a general directed graph,
- actions include a distinct `relation` family,
- revision must remain distinct from lineage,
- publication must remain distinct from truth.

That is enough to establish direction.
It is not enough to govern relation semantics.

Without a compact relation grammar, several confusions appear quickly:

- support gets confused with citation,
- dependency gets confused with mere reference,
- lineage gets faked as revision,
- supersession gets treated as a claim about truth rather than claim routing,
- snapshot membership gets mistaken for epistemic endorsement.

This note resolves that ambiguity at the first useful level.

---

## Core relation families

At the current stage, the system should treat the following as the first governed relation families.

### 1. evidentiary relations

These express directed knowledge pressure on a target object.

#### `supports`

Meaning:

> the source object provides positive governed support for the target object.

Typical examples:

- an evidence object supports a claim,
- a derived claim supports a parent claim in a sub-scope,
- a verdict rationale object supports a verdict state.

#### `challenges`

Meaning:

> the source object places governed pressure against the target object, its support chain, or its admissibility.

Typical examples:

- a dissent challenges a claim,
- an evidence object challenges a prior claim,
- a methodological object challenges an evidence object.

These relations are the strongest first-layer verdict-relevant edges.

### 2. citation / traceability relations

These preserve accountable reference without automatically asserting dependency or support.

#### `cites`

Meaning:

> the source object explicitly references the target object or target source proxy for context, attribution, or traceability.

Typical examples:

- a claim cites a prior claim,
- a snapshot cites a governed object,
- a public note cites a source proxy.

Current rule:

- `cites` is traceability-bearing,
- but `cites` does **not** by itself mean `supports`, `depends_on`, or `challenges`.

This distinction is necessary.
Otherwise the graph becomes full of edges that look meaningful but say almost nothing.

### 3. dependency relations

These express structural reliance.

#### `depends_on`

Meaning:

> the source object requires the target object as an upstream condition, assumption, or necessary governed basis.

Typical examples:

- a claim depends on another claim,
- a verdict depends on a claim and a support neighborhood,
- a public surface depends on a specific upstream snapshot.

Current rule:

- `depends_on` is stronger than `cites`,
- but it is not the same as `supports`,
- because dependency says what must hold upstream, not whether the downstream object is well supported overall.

Dependency relations are verdict-relevant because weakening or removal upstream may change downstream admissibility.

### 4. lineage relations

These express ancestry and descent between distinct governed identities.

#### `descends_from`

Meaning:

> the source object is a historically downstream governed successor or branch of the target object.

Typical examples:

- a weaker successor claim descends from a stronger parent claim,
- a snapshot descends from an earlier snapshot lineage,
- a narrower scoped claim descends from a broader claim.

Current rule:

- `descends_from` is not a revision bump,
- it names historical continuity across distinct governed identities.

This is the first lawful way to talk about claim splitting without faking it as only `2.0` or `3.0`.

### 5. succession relations

These express routing from an older governed object to a newer replacement path.

#### `supersedes`

Meaning:

> the source object is now the preferred governed successor route relative to the target object.

Typical examples:

- a revised public claim supersedes an older claim,
- a newer snapshot supersedes an earlier public release,
- a descendant claim supersedes the older public-facing route without erasing its history.

Current rule:

- `supersedes` is not a truth claim by itself,
- it is a governance and routing claim,
- and it often co-occurs with `descends_from`, lifecycle change, and sometimes major revision,
- but it must not be collapsed into any one of those.

### 6. publication-pin relations

These express release-surface membership rather than knowledge standing.

#### `pinned_in_snapshot`

Meaning:

> the target object at a specified governed state is included in a release surface.

Typical examples:

- an object revision is pinned in a snapshot,
- a public page route pins a specific upstream release state,
- a public case surface pins a selected object neighborhood.

Current rule:

- `pinned_in_snapshot` is publication-bearing,
- but it does **not** by itself mean `supported`, `stabilized`, or `true`.

This is how publication remains accountable without impersonating verdict.

---

## First-layer core relation set

At the current stage, the following relation names are now strong enough to be treated as the first-layer governed floor:

- `supports`
- `challenges`
- `cites`
- `depends_on`
- `descends_from`
- `supersedes`
- `pinned_in_snapshot`

That does **not** mean this set is globally frozen forever.
It means the system now has a compact lawful set strong enough to stop the worst ambiguity.

---

## Verdict relevance classes

Not all relations should be interpreted with the same force.

### A. directly verdict-relevant

These relations can materially affect how a claim or verdict should be read:

- `supports`
- `challenges`
- `depends_on`

Why:

- they bear directly on support strength,
- attack pressure,
- and admissibility of downstream judgment.

### B. interpretively relevant but not direct support-pressure

These relations matter for historical reading and governance routing, but should not be mistaken for direct support or rejection:

- `descends_from`
- `supersedes`

Why:

- they help explain what replaced what,
- what split from what,
- and which route is currently preferred,
- but they do not by themselves prove or disprove the content.

### C. traceability or release relevance only

These relations matter for auditability and publication clarity, but should not be read as verdict force on their own:

- `cites`
- `pinned_in_snapshot`

Why:

- citation is not support,
- release membership is not endorsement.

This three-class distinction is one of the main reasons the note exists.

---

## Direction rule

Relation semantics are directed.

Current compact convention:

> **source -> target** means:
> the source object is making the governed move named by the relation toward the target object.

Examples:

- `E-0007 supports C-0012`
- `D-0003 challenges C-0012`
- `C-0012 depends_on C-0004`
- `C-0013 descends_from C-0012`
- `C-0013 supersedes C-0012`
- `S-0004 pinned_in_snapshot C-0013@2.0`

The UI may phrase some of these in reverse for readability.
The protocol layer should keep direction explicit.

---

## Relation versus revision

Revision and relation must stay separate.

### Revision answers:

> is this still the same governed object, now in a new semantic state?

### Relation answers:

> how does this governed object stand in directed relation to another governed object?

Important consequences:

- adding `supports` or `cites` does **not** automatically require a semantic revision,
- but changing a dependency basis may trigger a revision if the object meaning materially changes,
- claim splitting should not be faked as only a major revision when what actually happened is descent,
- supersession should not be smuggled into revision history as if replacement were only a wording change.

---

## Relation versus lifecycle

Lifecycle answers:

> what is the operational state of this object inside the system?

Relation answers:

> how is this object positioned relative to another object?

Examples:

- an object may `supersede` another object while both remain visible,
- a challenged claim may remain `active`,
- an archived claim may still be heavily cited,
- a superseded object may remain historically important.

So relation semantics must not be collapsed into lifecycle labels.

---

## Relation versus publication

Publication relations are real, but publication is not truth.

Important consequences:

- `pinned_in_snapshot` is not a verdict,
- being shown on a public page is not equivalent to being endorsed,
- snapshot membership should point to governed object states rather than vague floating references,
- public release routing may depend on lineage and supersession without erasing older public objects.

---

## Minimal relation record shape

The system does not need a huge relation ontology to start.
A minimal governed relation record can be described as:

```text
RelationRecord := {
  relation_id: string,
  relation_type:
    "supports" |
    "challenges" |
    "cites" |
    "depends_on" |
    "descends_from" |
    "supersedes" |
    "pinned_in_snapshot",
  source_object_id: string,
  target_object_id: string,
  created_at: ISODateTime,
  created_by: ActorRef,
  summary?: string,
  target_revision?: string,
  status?: "active" | "withdrawn",
}
```

Optional later additions may include:

- relation scope,
- strength or confidence,
- reversible marker,
- policy reference,
- machine validation status,
- public visibility overrides.

But those are not required for the first useful grammar.

---

## Current decision tests

When deciding which relation to use, ask:

### Support test

Is the source actually giving governed positive pressure to the target?

If yes, use `supports`, not merely `cites`.

### Challenge test

Is the source actually placing governed negative pressure on the target or its basis?

If yes, use `challenges`.

### Dependency test

Would the downstream object lose admissibility if the upstream target were removed or materially changed?

If yes, use `depends_on`.

### Citation test

Is the link mainly there for attribution, context, or traceability rather than support-pressure?

If yes, use `cites`.

### Lineage test

Is the relationship about ancestry or descent between distinct governed identities?

If yes, use `descends_from`.

### Succession test

Is the relationship about preferred replacement or routing rather than ancestry alone?

If yes, use `supersedes`.

### Publication-pin test

Is the relationship about inclusion in a release surface rather than a claim about truth or support?

If yes, use `pinned_in_snapshot`.

These tests may co-occur in one workflow.
But they should not be flattened into one generic `links` bucket without typed meaning.

---

## What this note does **not** claim

This note does **not** claim that:

- the full graph ontology is finished,
- every future relation name is frozen,
- relation validation rules are fully automated,
- verdict grammar is now complete,
- or the legal transition matrix is already done.

It claims something smaller:

> the current system now has a compact relation grammar strong enough to make the first object graph legible and governable.

---

## Practical verdict

So the practical verdict is:

- **relations are now named as governed graph semantics rather than anonymous links**
- **the first-layer lawful relation floor is now explicit**
- **support, challenge, dependency, lineage, succession, citation, and publication-pin are no longer muddled together**
- **relation semantics remain distinct from revision, lifecycle, and publication state**
- **the current relation grammar is now strong enough to support later verdict grammar and transition admissibility work**

That is the right size of rule for the current stage.
