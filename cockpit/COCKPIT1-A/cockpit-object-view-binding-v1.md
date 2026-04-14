# COCKPIT1-A Object View Binding v1

## Status

Drafted for binding.

## Function

This file binds concrete cockpit views to concrete object surfaces in the two current pilot cases.

---

## View-to-object bindings

### A. `claim_view`
Must bind to:

- claim title
- current visible judgment / verdict level
- direct support surface
- direct challenge surface
- lineage placement

Primary source case:
- `power-posing`

Secondary source case:
- `h-pylori-ulcer`

### B. `evidence_tree_view`
Must bind to:

- evidence objects attached to a claim
- support clusters
- evidence gaps where explicitly surfaced
- links to source usage where available

Primary source case:
- `h-pylori-ulcer`

Secondary source case:
- `power-posing`

### C. `dissent_ledger_view`
Must bind to:

- open dissents
- answered dissents
- unresolved pressure
- dissent-to-claim attack surfaces

Primary source case:
- `power-posing`

Secondary source case:
- `h-pylori-ulcer`

### D. `verdict_state_view`
Must bind to:

- current verdict token
- prior movement where surfaced
- current holds
- current upgrade boundaries

Primary source case:
- `h-pylori-ulcer`

Secondary source case:
- `power-posing`

### E. `project_map_view`
Must bind to:

- case root
- claim index
- route or stage grouping
- readable object entry points

Primary source case:
- both

---

## Binding rule

No cockpit view may depend on prose-only interpretation when a governed object or governed surface already exists.

If a view cannot be bound to existing governed surfaces, it is out of scope for COCKPIT1-A.

---

## Final binding block

- bound views: 5
- prose-only derived views: forbidden
- current source cases: 2
