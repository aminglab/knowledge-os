# CEDV Canonical Object Schema v1

## Status

Protocol skeleton floor.

## Function

This file defines the first canonical schema floor for the four core Knowledge OS object families:

- Claim
- Evidence
- Dissent
- Verdict

This is not another cockpit governance note.
It is the minimum protocol skeleton required for interoperable object authoring, validation, rendering, indexing, and later publication flow.

---

## Design principle

The system should make knowledge work portable by turning intellectual moves into typed objects.

A valid CEDV object must therefore answer four questions before any prose is read:

1. What object family is this?
2. What object state is it in?
3. What sources or internal objects ground it?
4. What governed relations connect it to other objects?

---

## Shared object envelope

Every CEDV object uses the shared object envelope already defined in `protocol/object-envelope.md`:

```yaml
id: C-0001
object_type: claim
title: Short object title
lifecycle_state: active
visibility: public
source_refs: []
basis_refs: []
key_facts: {}
links: []
```

The shared envelope is now treated as the common transport layer.
The family-specific schemas below define the minimum required fields for each object family.

---

## Claim object

### Required fields

```yaml
id: C-0001
object_type: claim
title: ...
lifecycle_state: draft | active | paused | superseded | withdrawn | archived
epistemic_status: under_evaluation | supported | contested | weakened | rejected | split | stabilized
visibility: private | team | public
source_refs: []
links: []
```

### Required meaning

A Claim object states a proposition that can be supported, challenged, narrowed, superseded, or stabilized.

### Canonical relation expectations

Claims may use:

- `depends_on`
- `descends_from`
- `supersedes`
- `cites`

Evidence usually supports claims from the evidence side rather than by authored reverse links.
Dissent usually challenges claims from the dissent side.

---

## Evidence object

### Required fields

```yaml
id: E-0001
object_type: evidence
title: ...
lifecycle_state: draft | active | linked | paused | superseded | withdrawn | archived
visibility: private | team | public
source_refs: []
links:
  - type: supports | challenges | cites
    target: C-0001
```

### Required meaning

An Evidence object records a source-grounded support, challenge, or citation move.
It is not merely a bibliographic note.

### Canonical relation expectations

Evidence objects should use authored outward relations:

- `supports` when the evidence strengthens a claim or verdict basis
- `challenges` when the evidence weakens or contests a claim
- `cites` when the evidence primarily grounds context or source lineage

---

## Dissent object

### Required fields

```yaml
id: D-0001
object_type: dissent
title: ...
lifecycle_state: draft | active | paused | superseded | withdrawn | archived
visibility: private | team | public
dissent_kind: empirical | methodological | logical | definitional | procedural | scope | interpretive
severity: low | medium | high | critical
source_refs: []
links:
  - type: challenges | cites
    target: C-0001
```

### Required meaning

A Dissent object preserves an objection, limitation, counterargument, uncertainty, scope boundary, or unresolved residue.
It must remain visible until narrowed, cleared, superseded, or explicitly carried forward.

### Canonical relation expectations

Dissent objects should use:

- `challenges` toward the object being contested
- `cites` toward grounding sources where necessary

Dissent is not a comment thread. It is an accountable object.

---

## Verdict object

### Required fields

```yaml
id: V-0001
object_type: verdict
title: ...
lifecycle_state: draft | active | paused | superseded | withdrawn | archived
visibility: private | team | public
verdict_level: local | provisional | supported | stabilized | rejected | split | unresolved
basis_refs: []
links:
  - type: depends_on | supersedes | pinned_in_snapshot
    target: C-0001
```

### Required meaning

A Verdict object records a bounded adjudication over one or more governed objects.
It must name its basis rather than sounding like free-floating authority.

### Canonical relation expectations

Verdict objects should use:

- `depends_on` for basis relation when represented as graph links
- `supersedes` when replacing an earlier verdict
- `pinned_in_snapshot` when a verdict is frozen into a release or candidate snapshot

Verdict targeting may also be expressed through `basis_refs` and body prose, but it must not be implicit only.

---

## Common validity rules

A CEDV object is not valid if:

- `id` is missing
- `object_type` is not one of `claim`, `evidence`, `dissent`, `verdict`
- `title` is missing
- `lifecycle_state` is outside the protocol enum floor
- `visibility` is outside the protocol enum floor
- `links` is missing or not a list
- a link uses a non-canonical relation without an explicit migration note
- source-grounded objects omit `source_refs`
- verdict objects omit `basis_refs`
- dissent objects omit `dissent_kind` or `severity`

---

## Relationship to public candidates

A `public_candidate_object` is not a fifth CEDV family.
It is a candidate-layer export wrapper that may carry or compose CEDV objects.

Therefore:

- CEDV objects remain the protocol core.
- public candidates are transport/admission artifacts.
- public release layers should consume CEDV objects through candidate wrappers, not replace them.

---

## Current protocol reading

The right reading is:

> Claim, Evidence, Dissent, and Verdict are the canonical protocol skeleton.

The wrong reading is:

> cockpit objects and public-candidate objects are the core object families.

Cockpit and public-candidate layers are operational surfaces around the CEDV core.
