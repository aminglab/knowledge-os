# Emitted-hint admissibility v1

This note records the **smallest admissibility boundary** for future emitted hints in the current `power-posing` page stack.

It does not redesign the generator.
It does not add new fields to `page-data.js`.
It does not claim that every currently inferred meaning should now be pushed upstream.

It answers one narrower question:

> when is a renderer-side meaning mature enough to be emitted by the generator,
> and when should it still remain local to the composer?

---

## One-sentence ruling

Current ruling:

> **Naming is not enough to justify emission.**
> **A hint becomes admissible for emission only when it crosses from local convenience into stable contract necessity.**

That is the whole point of this note.

---

## Why this note exists now

The current page line has already accumulated four layers:

- payload-family naming
- renderer-side contract audit
- local composer hint hardening
- case-scoped composer cleanup

That means the next mistake would be obvious:

> pushing hints upstream merely because they have now been named.

This note exists to block that premature move.

---

## Current admissibility test

A future emitted hint should satisfy **all** of the following conditions before it is treated as admissible.

### 1. stability condition

The meaning must be stable enough that a wording tweak or local refactor should not redefine it.

If the meaning is still tightly coupled to this case’s current editorial phrasing, it is not yet admissible.

### 2. cross-layer usefulness condition

The hint must reduce real ambiguity across more than one layer.

That means emission is more justified when the hint helps:

- generator output,
- renderer composition,
- audit clarity,
- or later automation

all align more reliably.

If the hint only saves a few lines of local composer logic, admissibility is weak.

### 3. low-regret condition

The hint should be cheap to keep once emitted.

If future removal or reinterpretation would create avoidable contract churn, the hint is not yet mature enough.

### 4. semantics-not-style condition

The hint should encode a durable semantic or contract distinction, not merely a presentational styling convenience.

If the difference is mainly visual or editorial, it should remain local.

---

## Current admissibility judgments

### A. `card_family`

Current status:

> **not yet emitted, but closest to admissible**

Why:

- payload family naming already exists
- renderer pairing already exists
- audit language already names this distinction
- the distinction reduces ambiguity between `status_card`, `standard_card`, and `route_card`

Why not emitted yet:

- `standard_card` and `route_card` are still separated more by renderer role than by deeply different payload structure
- there is still only one real case

Current judgment:

> **admissible soon, but not necessary yet**

### B. `section_kind`

Current status:

> **not yet admissible for emission**

Why:

- section-shape interface exists
- but section semantics remain strongly case-scoped
- current section titles still carry much of the meaning

Current judgment:

> **keep local to the composer**

### C. `source_link_role`

Current status:

> **not yet emitted, but more admissible than before**

Why:

- the old label-driven split has already been hardened into href-based local role inference
- the distinction between `source_route` and `object_touch` is now clearer than before

Why not emitted yet:

- the current rule still serves only one case
- current source-entry usage is still small enough that local inference remains cheap

Current judgment:

> **promising, but still local for now**

### D. `source_group_key`

Current status:

> **not admissible yet**

Why:

- source grouping is still clearly case-local taxonomy
- the current grouping between scientific record and public circulation / retreat is meaningful here, but not yet justified as stable upstream contract

Current judgment:

> **must remain local**

### E. `section_card_renderer`

Current status:

> **not admissible for emission**

Why:

- this is currently a composer convenience hint
- it reduces local dispatch fragility
- but it mainly serves local composition rather than durable payload semantics

Current judgment:

> **keep local**

---

## What this note clarifies

This note clarifies three things.

### 1. named family ≠ emitted hint

Just because a payload family has been named does not mean it should now become a generated field.

### 2. local hardening ≠ upstream contract necessity

A hint can be valuable as a local composer hardening move while still being too small or too local to justify generator emission.

### 3. admissibility is a governance threshold

Emission should be treated as a governance upgrade, not as a convenience refactor.

That is why the threshold must stay conservative.

---

## What this note does **not** claim

This note does **not** claim that:

- the generator should now emit `card_family`
- the generator should now emit `section_kind`
- the generator should now emit `source_link_role`
- the generator should now emit `source_group_key`

It claims something smaller:

> these candidate hints can now be ranked by admissibility rather than discussed as one undifferentiated future upgrade bucket.

---

## Practical verdict

So the practical verdict is:

- **`card_family` is the nearest future candidate**
- **`source_link_role` is plausible but not yet needed upstream**
- **`section_kind` should remain local**
- **`source_group_key` should remain local**
- **style/convenience hints should stay in the composer**

That is the right size of boundary for the current stage.
