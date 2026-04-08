# Glossary

This glossary defines the current working language of **Knowledge OS**.
It is not a frozen doctrine. It is a shared vocabulary for the repository, the white paper, the architecture, and early pilots.

The goal is simple:

> keep the language stable enough to build,
> but open enough to evolve through use.

---

## Core object families

### Claim
A **Claim** is a formally stated proposition under governance.

It is not just a sentence in a document.
A claim is an object that can:

- be introduced,
- gather support,
- face dissent,
- split into descendants,
- receive verdicts,
- weaken,
- stabilize,
- or be rejected.

A claim should have boundaries, assumptions, and links to related objects.

---

### Evidence
**Evidence** is a supporting or weakening artifact linked to one or more claims.

Evidence may include:

- derivations,
- experiments,
- computations,
- observations,
- documents,
- code artifacts,
- datasets,
- logs,
- or other auditable materials.

Evidence is not merely attached.
It should be accountable, linkable, and reviewable.

---

### Dissent
**Dissent** is a structured challenge, reservation, attack, boundary concern, or unresolved objection.

Dissent is broader than simple contradiction.
It may include:

- methodological criticism,
- definitional instability,
- scope challenges,
- evidentiary weakness,
- procedural distrust,
- interpretive disagreement,
- or unresolved dependency concerns.

Dissent is a first-class governance object, not a comment.

---

### Verdict
A **Verdict** is the current institutional judgment on a target claim.

A verdict is not just an opinion.
It makes the current standing of a claim visible to a community.

A verdict may later be:

- upgraded,
- downgraded,
- revised,
- superseded,
- or frozen into a public snapshot.

---

## Structural terms

### Object
An **Object** is a governed unit in the system.

In the current model, the primary object families are:

- Claim
- Evidence
- Dissent
- Verdict

Documents are important, but they are downstream artifacts, not the only primary substrate.

---

### Object Graph
The **Object Graph** is the linked universe of objects and their relations inside a project.

Knowledge OS should be understood as working over a directed graph of objects, not merely a folder of documents.

Certain subgraphs may obey stricter rules, but the whole system should not be assumed to be a simple DAG.

---

### Link
A **Link** is a typed relation between objects.

Examples include:

- `supports`
- `weakens`
- `depends_on`
- `attacks`
- `responds_to`
- `rules_on`
- `supersedes`
- `splits_from`
- `descends_from`
- `published_as`
- `derived_from`

Link semantics may evolve, but link discipline is central to the system.

---

### Lineage
**Lineage** describes ancestry and descent relations between claims, verdicts, or snapshots.

Lineage matters because knowledge objects may not simply become true or false.
They may:

- split,
- retreat,
- fork,
- harden,
- or survive in weaker descendant forms.

---

### Snapshot
A **Snapshot** is a frozen publication package derived from live objects.

A snapshot is not identical to the full live object graph.
It is a deliberate release view.

A snapshot may contain:

- selected claims,
- selected evidence summaries,
- selected dissent history,
- verdict states,
- timeline or lineage views,
- and publication metadata.

A paper, white paper, appendix, or public case page may all be snapshot-like outputs.

---

## Product surfaces

### Private Cockpit
The **Private Cockpit** is the workspace where a person or small team drafts, maps, argues, and governs a project from the inside.

This is where objects first become real.

---

### Team Layer
The **Team Layer** is where permissions, review, responsibility, assignment, and audit become explicit.

It is the collaboration surface for governed work, not just shared editing.

---

### Public Layer
The **Public Layer** is where selected objects are released as:

- snapshots,
- living knowledge pages,
- public cases,
- or other public-facing artifacts.

The public layer should expose governed states, not just static documents.

---

## Governance terms

### Lifecycle State
A **Lifecycle State** describes the operational state of an object inside the system.

Examples:

- `draft`
- `active`
- `paused`
- `superseded`
- `withdrawn`
- `archived`

Lifecycle state is about the object as an object.
It is not the same thing as its knowledge standing.

---

### Epistemic Status
**Epistemic Status** describes how a claim currently stands as knowledge.

Examples in the current working language include:

- `under_evaluation`
- `supported`
- `contested`
- `weakened`
- `rejected`
- `split`
- `stabilized`

This vocabulary is still provisional.
The important point is that epistemic status should not be collapsed into lifecycle state.

---

### Action
An **Action** is a governed operation performed on an object.

Examples:

- create claim,
- attach evidence,
- raise dissent,
- request verdict update,
- split claim,
- supersede claim,
- export snapshot.

Knowledge OS is action-centered, not chat-centered.

---

### Actor
An **Actor** is a human or agent that creates, transforms, reviews, or evaluates objects.

Actors should be visible in revision history and audit trails.

---

### Revision
A **Revision** is a recorded change to an object.

Revisions should preserve:

- who changed the object,
- when it changed,
- what changed,
- and why.

Knowledge OS should prefer visible supersession over silent overwrite.

---

### Audit
**Audit** is the trace of actions, revisions, and skill runs that allows later review.

Audit matters because the system is not just storing outcomes.
It is preserving responsibility and history.

---

## Skill terms

### Skill
A **Skill** is a governed capability that acts on objects or object neighborhoods.

A skill is not just a loose plugin.
It should have explicit inputs, outputs, side effects, and audit traces.

Examples:

- object extraction,
- gap scanning,
- counterposition generation,
- snapshot composition,
- case rendering.

---

### Skill Run
A **Skill Run** is one recorded invocation of a skill.

A skill run should preserve:

- who triggered it,
- what inputs it saw,
- what outputs it produced,
- and what, if anything, was accepted into the graph.

---

## Directional phrases

### Living Knowledge
**Living Knowledge** refers to knowledge that remains governable after publication.

It can still:

- receive support,
- face dissent,
- change status,
- split into descendants,
- and leave a visible history.

This does not mean that everything changes all the time.
It means the system preserves the possibility of formal continued governance.

---

### Publish-and-Freeze
**Publish-and-Freeze** names the old default that Knowledge OS is trying to replace.

In that model, knowledge is primarily managed as a static publication artifact.

Knowledge OS instead aims for a living governance model.

---

## Current reminder

This glossary is a working vocabulary.
It should become more stable through real pilots, not by premature abstraction alone.

> Run it alive before you freeze it.
