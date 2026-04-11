# Action governance grammar v1

This note records the **first compact action grammar** for Knowledge OS.

It is intentionally small.
It does not attempt a full protocol freeze.
It does not define every future action.
It does something narrower and more useful:

> it gives the current system a governed way to talk about what kinds of actions exist,
> what they are allowed to change,
> and how they relate to object lifecycle versus epistemic standing.

---

## One-sentence ruling

Current ruling:

> **Actions are first-class governed operations on objects.**
> **They must not collapse lifecycle change, epistemic change, relation change, and publication change into one undifferentiated event stream.**

That is the whole grammar floor.

---

## Why this note exists now

`ARCHITECTURE.md` already says:

- **Actions, not chats**
- AI should enter through governed operations on objects

That is enough to establish direction.
It is not enough to govern action semantics.

Without a compact grammar, the following risks appear quickly:

- lifecycle events get confused with epistemic judgments,
- object-link changes get confused with claim-state changes,
- publication moves get confused with object revision moves,
- audit logs become noisy but semantically weak.

This note resolves that ambiguity at the first useful level.

---

## Core action families

At the current stage, actions should be grouped into five families.

### 1. object-creation actions

These create a new governed object.

Examples:

- `create_claim`
- `create_evidence`
- `create_dissent`
- `create_verdict`

Effect:

- introduces a new object identity
- initializes lifecycle state
- initializes revision history at `1.0`

### 2. object-revision actions

These revise the semantic state of an existing governed object.

Examples:

- `revise_claim`
- `revise_evidence`
- `revise_dissent`
- `revise_verdict`

Effect:

- creates a new semantic revision state
- may be major or minor
- does **not** create a new object identity by default

This family is governed by:

- `revision-model-v1.md`

### 3. relation actions

These create, remove, or modify governed relations between objects.

Examples:

- `attach_evidence`
- `detach_evidence`
- `link_dissent`
- `set_dependency`
- `declare_lineage`
- `supersede_with_descendant`

Effect:

- changes graph structure
- may change downstream interpretation
- does **not** automatically imply semantic revision unless the object meaning itself changes

This matters because graph mutation and object revision are not the same thing.

### 4. lifecycle actions

These change the operational state of an object inside the system.

Examples:

- `activate_object`
- `pause_object`
- `withdraw_object`
- `archive_object`
- `supersede_object`

Effect:

- changes lifecycle state
- does **not** automatically decide whether the claim is supported, weakened, contested, or rejected

Lifecycle is an operational axis, not the whole knowledge judgment.

### 5. epistemic / institutional actions

These change the object’s institutional standing as knowledge.

Examples:

- `mark_under_evaluation`
- `mark_supported`
- `mark_contested`
- `mark_weakened`
- `mark_rejected`
- `stabilize_verdict`

Effect:

- changes epistemic or institutional standing
- does **not** automatically imply that the object should be archived, withdrawn, or superseded operationally

This family is especially important for verdict handling.

### 6. publication actions

These govern release surfaces rather than only underlying object state.

Examples:

- `compose_snapshot`
- `publish_snapshot`
- `update_public_page`
- `depublish_snapshot`

Effect:

- changes what is publicly surfaced
- should pin exact object revisions where relevant
- should not be confused with rewriting the underlying object history

### 7. skill-run actions

These invoke a model or computational skill inside a governed action frame.

Examples:

- `extract_candidate_objects`
- `scan_missing_support`
- `scan_unresolved_dissent`
- `generate_counterposition`
- `draft_snapshot`

Effect:

- produces candidate outputs, analyses, or drafts
- must create audit records
- does **not** bypass governance by itself

Skill output is never the governance layer by default.

---

## Two-axis rule for action interpretation

The current grammar must preserve the distinction already named in `ARCHITECTURE.md`.

### Axis A. lifecycle state

Operational state inside the system.

### Axis B. epistemic / institutional standing

Current knowledge standing of the object.

### Action rule

No action family should silently collapse these two axes.

Examples:

- `archive_object` is not the same as `mark_rejected`
- `mark_contested` is not the same as `pause_object`
- `supersede_with_descendant` is not the same as a major revision bump
- `publish_snapshot` is not the same as `mark_supported`

That separation is a protocol requirement, not a UI preference.

---

## Minimal action record shape

The system does not need a huge action schema to start.
A minimal governed action record can be described as:

```text
ActionRecord := {
  action_id: string,
  action_type: string,
  action_family:
    "object_creation" |
    "object_revision" |
    "relation" |
    "lifecycle" |
    "epistemic" |
    "publication" |
    "skill_run",
  actor: ActorRef,
  target_object_ids: string[],
  occurred_at: ISODateTime,
  summary: string,
  resulting_revision_ids?: string[],
  resulting_snapshot_ids?: string[],
}
```

Optional later additions may include:

- permissions decision record
- validator result
- skill run trace
- reversible / irreversible marker
- policy reference

But those are not required for the first useful grammar.

---

## Current decision rules

When deciding how to model an action, ask:

### Revision test

Did the object’s semantic meaning change?

If yes, an object-revision action is probably involved.

### Relation test

Did the graph change while the object meaning remained materially the same?

If yes, a relation action is probably involved.

### Lifecycle test

Did the system’s operational handling of the object change?

If yes, a lifecycle action is probably involved.

### Epistemic test

Did the knowledge standing or institutional judgment change?

If yes, an epistemic action is probably involved.

### Publication test

Did the release surface change without rewriting underlying semantic history?

If yes, a publication action is probably involved.

These tests may co-occur in one workflow.
But they should not be semantically merged without naming the distinction.

---

## What this note does **not** claim

This note does **not** claim that:

- every action name is now frozen,
- the full permission model is finished,
- the protocol now has a complete legal transition matrix,
- or the system already has a final verdict grammar.

It claims something smaller:

> the current system now has a compact action grammar strong enough to stop the worst category confusion.

---

## Practical verdict

So the practical verdict is:

- **actions are now named as protocol objects, not only UI verbs**
- **revision, relation, lifecycle, epistemic, publication, and skill-run actions are distinct families**
- **the two-axis rule must remain preserved**
- **publication and lineage must not be smuggled into revision history**
- **the current action grammar is now strong enough to support later governance refinement**

That is the right size of rule for the current stage.
