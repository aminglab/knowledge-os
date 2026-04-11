# Page-data contract naming v1

This note records the **smallest current naming layer** for the `page-data.js` payload used by the `power-posing` page stack.

It does not redesign the generator.
It does not add new emitted fields.
It does not claim that the payload is already a general public-layer schema.

It does something smaller:

> it names the contract families that already exist in the current payload,
> so later upgrades do not have to proceed from unnamed drift.

---

## One-sentence ruling

Current ruling:

> **The payload families already exist in practice.**
> **They should now be named before any further generator-side hint upgrade is considered.**

That is the entire point of this note.

---

## Why this note exists now

The current renderer contract audit already identified one real pressure point:

- card-shape divergence inside `page-data.js`

That divergence is not a bug.
But it means the payload is no longer one flat anonymous JSON blob.
It already contains recurring families with different field expectations.

Until those families are named, every future contract discussion risks becoming muddy.

---

## Current top-level payload families

At the current stage, the page-data payload already contains the following top-level families.

### 1. hero family

Fields:

- `title`
- `shortTitle`
- `description`
- `links[]`

Role:

- public page entry surface
- first reader-facing orientation layer

### 2. judgment family

Fields:

- `judgmentIntro`
- `judgmentLinks[]`
- `statusCards[]`

Role:

- current visible judgment surface
- governed claim-lineage status rendering

### 3. section-card family

Fields:

- `sections[]`
- each section with `title`, `intro`, `cards[]`

Role:

- snapshot-derived mid-page public section surface

Important note:

This family is already plural at the card level.
It is not one single undifferentiated card shape.

### 4. timeline family

Fields:

- `timeline[]`

Role:

- compact chronological reading surface

### 5. source-entry family

Fields:

- `sources[]`

Role:

- canonical source participation surface
- current source-route and object-touch surface

### 6. reading-path family

Fields:

- `readingPathIntro`
- `readingPath[]`

Role:

- thin downstream route back into the governed case

### 7. footer family

Fields:

- `footer`

Role:

- closing release-position statement for the page

---

## Current card-family naming

The main naming pressure appears inside card-bearing parts of the payload.

At the current stage, the following card families are already present.

### A. status-card family

Current field shape:

```text
status_card := {
  title,
  status,
  summary,
  badges[],
  links[],
}
```

Current use:

- `statusCards[]`

Current renderer pairing:

- `renderStatusCard`

### B. standard-card family

Current field shape:

```text
standard_card := {
  title,
  kind,
  body,
  badges?,
  links?,
}
```

Current use:

- non-route entries inside `sections[].cards[]`

Current renderer pairing:

- `renderStandardCard`

### C. route-card family

Current field shape:

```text
route_card := {
  title,
  kind,
  body,
  badges?,
  links?,
}
```

Current use:

- route entries inside the `Public claim and source routes` section

Current renderer pairing:

- `renderRouteCard`

Important honesty note:

The current `standard_card` and `route_card` field shapes are very close.
Their separation is currently justified by renderer role rather than by a deeply different payload structure.
That is acceptable.
But the distinction should still be named.

---

## Current entry-family naming beyond cards

Not every repeating payload unit is a card.
The current payload also already carries three other recurring entry families.

### D. timeline-entry family

Current field shape:

```text
timeline_entry := {
  year,
  title,
  body,
}
```

Current renderer pairing:

- `renderTimelineItem`

### E. source-entry family

Current field shape:

```text
source_entry := {
  id,
  title,
  role,
  locator,
  usage,
  badges[],
  links[],
}
```

Current renderer pairing:

- `renderSourceItem`

### F. footer-entry family

Current field shape:

```text
footer_entry := {
  eyebrow,
  title,
  body,
  badges[],
  links[],
}
```

Current renderer pairing:

- `renderFooterCard`

---

## What this note clarifies

This note clarifies three things.

### 1. `page-data.js` is already a family-bearing payload

It is no longer accurate to talk about it as if it were only one flat anonymous object.
The payload already contains named recurring families.

### 2. family naming is not the same as new emitted hints

This note does **not** mean the generator now emits:

- `card_family`
- `section_kind`
- `source_link_role`

It only names what is already visibly true.

### 3. naming should come before hint proliferation

If a later stage ever introduces explicit machine-readable hints, those hints should grow from these named families rather than from improvised ad hoc naming.

---

## What this note does **not** claim

This note does **not** claim that:

- the payload is already a generic page schema,
- card families are already cross-case stable,
- section semantics are already encoded in the payload,
- or generator-side redesign is now required.

It claims something smaller and more useful:

> the current payload now has enough internal structure that its recurring families should be named explicitly.

---

## Practical verdict

So the practical verdict is:

- **payload family naming now exists**
- **no generator change was required**
- **future hint upgrades now have a cleaner naming floor**
- **current contract discussion no longer has to proceed from unnamed card divergence**

That is the right size of move for the current stage.
