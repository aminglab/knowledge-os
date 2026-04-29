# CEDV Relation and Basis Validation v1

## Status

Protocol skeleton validation floor.

## Function

This file defines the first validation floor for turning individual CEDV objects into a coherent knowledge object graph.

The prior CEDV schema floor answered:

> what does a Claim, Evidence, Dissent, or Verdict object look like?

This validation floor answers:

> when do those objects form a valid graph rather than four isolated files?

---

## Design principle

A CEDV graph is valid only when authored relations, basis references, and object families agree.

The system should not accept a group of objects merely because each file has the right fields.
The files must also make a coherent epistemic move together.

---

## Canonical validation targets

A minimal CEDV graph validator should check at least:

1. object id uniqueness;
2. all link targets resolve;
3. all `basis_refs` resolve;
4. relation names are from the canonical link floor;
5. relation source and target families are admissible;
6. verdict basis references contain at least one governed object;
7. dissent objects challenge something rather than floating free;
8. evidence objects support, challenge, or cite something rather than floating free.

---

## Relation admissibility floor

### Claim source

A Claim may author links using:

- `depends_on` toward Claim
- `descends_from` toward Claim
- `supersedes` toward Claim or Verdict
- `cites` toward a source identifier or governed object when needed

### Evidence source

Evidence may author links using:

- `supports` toward Claim or Verdict
- `challenges` toward Claim or Verdict
- `cites` toward source identifiers or governed objects

### Dissent source

Dissent may author links using:

- `challenges` toward Claim, Evidence, Verdict, or another Dissent
- `cites` toward source identifiers or governed objects

### Verdict source

Verdict may author links using:

- `depends_on` toward Claim, Evidence, Dissent, or Verdict
- `supersedes` toward Verdict
- `pinned_in_snapshot` toward a snapshot or public-candidate identifier

---

## Basis-reference floor

### Verdict basis

A Verdict must include `basis_refs`.

At minimum, a Verdict basis should resolve to at least one governed object id from the CEDV set.

Recommended basis shape:

- at least one Claim or Evidence reference;
- dissent references are encouraged when unresolved residue exists;
- a Verdict should not ground itself only in another Verdict unless the relation is explicitly a lineage or supersession move.

### Non-verdict basis

Other object families may use `basis_refs`, but they are not required at this floor.

---

## Floating-object rules

The following are invalid in a minimal graph validation context:

- Evidence with no authored link;
- Dissent with no authored challenge;
- Verdict with empty `basis_refs`;
- link target that neither resolves to a CEDV object id nor is explicitly allowed as an external source or snapshot id;
- duplicate ids;
- non-canonical relation type without an explicit migration note.

---

## Relationship to examples

The current canonical examples form a minimal graph:

- `E-0001 supports C-0001`
- `D-0001 challenges C-0001`
- `V-0001 depends_on C-0001`
- `V-0001 pinned_in_snapshot public-candidate:h-pylori-ulcer-summary:v1`
- `V-0001 basis_refs: C-0001, E-0001, D-0001`

This is not a final scientific knowledge graph.
It is a minimal protocol-valid object graph.

---

## Current protocol reading

The right reading is:

> CEDV files become useful when their relation and basis structure forms a coherent graph.

The wrong reading is:

> if every file has the right top-level fields, the protocol graph is already valid.
