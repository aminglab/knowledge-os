# Object Envelope (Working Set)

This file defines the **minimum working object envelope** currently expected in early Knowledge OS pilots.
It is not a frozen protocol spec.
It is a practical guardrail derived from actual use.

The goal is simple:

> keep object frontmatter stable enough to build,
> without pretending the full protocol has already been solved.

---

## Why this file exists

The early pilot is already using structured object files.
That is good.
But if each pilot grows its own frontmatter shape without restraint, the language will drift immediately.

This file exists to prevent that drift.

It does **not** attempt to define the full long-term object model.
It only defines the smallest envelope that is already useful for:

- indexing,
- navigation,
- snapshot composition,
- source tracking,
- link discipline,
- and later renderer work.

---

## First rule

An object file has two layers:

1. **frontmatter** — the minimum machine-legible governance envelope
2. **body** — the human-readable explanation, argument, or narrative content

The frontmatter should be strong enough that a renderer, indexer, or audit tool can understand the object's role **without** reading the full prose body.

---

## Current working envelope

The current working shape is:

```yaml
---
id: C-0002
object_type: claim
title: A weaker descendant claim about subjective feeling may survive the collapse of the original strong-form claim
lifecycle_state: active
epistemic_status: contested
visibility: public
source_refs:
  - Ranehill_et_al_2015
  - Dana_Carney_2016_statement
key_facts:
  year: 2015
  scope: weaker descendant route
links:
  - type: descends_from
    target: C-0001
---
```

Not every object needs every field.
But pilots should not casually invent unrelated shapes.

---

## Current fields

### `id`
A unique object identifier inside the project or case.

Examples:

- `C-0001`
- `E-0001`
- `D-0002`
- `V-0001`

This field is required.

---

### `object_type`
The current primary object family.

Current working values:

- `claim`
- `evidence`
- `dissent`
- `verdict`

This field is required.

---

### `title`
A short, human-readable title for the object.

The title should be strong enough to display in lists, navigation, and snapshot rendering.

This field is required.

---

### `lifecycle_state`
The current operational state of the object inside the system.

Use the working vocabulary defined in [`enums.md`](./enums.md).

This field is required.

---

### `epistemic_status`
The current knowledge standing of a claim-like object.

Typical current use:

- common for `claim`
- optional for other object families unless genuinely needed

Use the working vocabulary defined in [`enums.md`](./enums.md).

This field is conditionally required rather than universal.

---

### `visibility`
The release scope of the object.

Current working values:

- `private`
- `team`
- `public`

This field is required.

---

### `source_refs`
A list of source identifiers used to ground the object.

These ids should point to canonical entries defined at the case or project level, for example in a `references.md` file.

This field is strongly recommended whenever an object relies on external sources.
Objects should not use undefined source ids.

---

### `basis_refs`
A list of internal object ids that serve as the formal basis for the current object.

Typical current use:

- often useful for `verdict`
- may later be useful for other object families

Examples:

- `E-0001`
- `D-0001`
- `D-0002`

This field is optional.

---

### `key_facts`
A compact structured map for highly reusable facts that should remain visible outside the prose body.

Examples:

- year
- sample_size
- actor
- method
- effect_summary

This field is optional.

The purpose of `key_facts` is not to duplicate the whole body.
It is to preserve the small number of facts that are especially useful for indexing, rendering, filtering, or later audit.

---

### `links`
Typed directed relations from this object to other governed objects.

Each link currently uses the working shape:

```yaml
links:
  - type: supports
    target: C-0001
```

Use the current relation floor defined in:

- [`object-relation-grammar-v1.md`](../object-relation-grammar-v1.md)
- [`link-types.md`](./link-types.md)

Current direction rule:

> the source object is making the governed move named by `type` toward the `target`.

This field is required.
Even if the list is short, relation discipline is central to the system.

Legacy pilot names such as `supported_by`, `attacks`, `ruled_on`, or `splits_to` may still appear in older materials.
They should now be treated as migration vocabulary rather than the preferred canonical graph language.

---

## Current field expectations by object family

This section is intentionally lightweight.
It describes current working expectations, not eternal law.

### Claim
Usually expected to include:

- `id`
- `object_type`
- `title`
- `lifecycle_state`
- `epistemic_status`
- `visibility`
- `source_refs` when externally grounded
- `key_facts` when useful
- `links`

### Evidence
Usually expected to include:

- `id`
- `object_type`
- `title`
- `lifecycle_state`
- `visibility`
- `source_refs`
- `links`

Evidence objects should now prefer canonical outward relation names such as `supports`, `challenges`, or `cites` rather than mirrored reverse labels.

### Dissent
Usually expected to include:

- `id`
- `object_type`
- `title`
- `lifecycle_state`
- `visibility`
- `dissent_kind`
- `severity`
- `source_refs`
- `key_facts` when useful
- `links`

`dissent_kind` and `severity` are governed by the working enum vocabulary in [`enums.md`](./enums.md).

Dissent objects should now prefer canonical outward relation names such as `challenges` or `cites`.

### Verdict
Usually expected to include:

- `id`
- `object_type`
- `title`
- `lifecycle_state`
- `visibility`
- `verdict_level`
- `basis_refs`
- `links`

`verdict_level` is no longer only an unnamed pilot-local prose field.
The current compact verdict floor is now described in [`verdict-grammar-v1.md`](../verdict-grammar-v1.md).

Older pilot materials may still infer verdict targeting through legacy relation names such as `rules_on`.
That should now be treated as a migration pattern rather than the preferred long-term shape.

---

## What this file does **not** do yet

This file does not yet freeze:

- a universal `project_id`
- revision history shape
- actor / author metadata
- timestamps
- body schema
- publication metadata
- full audit fields
- formal validation rules for every object family

Those may arrive later.
They should not be front-loaded before repeated use demands them.

---

## Current discipline

When adding or editing object files in early pilots:

1. Prefer the current working envelope.
2. Prefer current enum values and canonical relation names.
3. Do not invent new top-level frontmatter fields casually.
4. If a new field is genuinely needed, add it deliberately and explain why.
5. Keep `source_refs` aligned with canonical source ids defined by the case or project.
6. Treat older mirrored or pilot-local relation names as migration debt, not as the stable target shape.

---

## Practical test

A frontmatter design is probably good enough for now if it lets us answer these questions quickly:

- What kind of object is this?
- What is its current lifecycle state?
- What is its current knowledge standing, if relevant?
- What sources ground it?
- What other objects does it connect to?
- What small number of key facts should remain visible without reading the whole body?

If yes, the envelope is doing its job.
If not, it is either too weak or too ornamental.

---

## Current reminder

This is a **working envelope**.
It should become more stable by surviving live pilots, not by being overdesigned in advance.

> Run it alive before you freeze it.
