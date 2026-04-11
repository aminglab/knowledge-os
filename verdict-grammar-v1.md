# Verdict grammar v1

This note records the **first compact verdict grammar** for Knowledge OS.

It is intentionally small.
It does not attempt a full legal code for every claim state.
It does not freeze every future domain-specific verdict lexicon.
It does something narrower and more useful:

> it gives the current system a governed way to name the first institutional judgment levels,
> distinguish verdict from lifecycle, lineage, and publication,
> and stop claim state from collapsing into vague prose.

---

## One-sentence ruling

Current ruling:

> **A verdict is a first-class institutional judgment on a target claim.**
> **The current cross-pilot verdict floor is deliberately small: `under_evaluation`, `supported`, `contested`, `weakened`, `rejected`, and `stabilized`.**

That is the whole point of this note.

---

## Why this note exists now

`ARCHITECTURE.md` already says:

- lifecycle state and epistemic standing must remain separate,
- verdict is its own object family,
- actions include a distinct epistemic / institutional family,
- publication is not truth,
- relation semantics are governed rather than anonymous.

That is enough to establish direction.
It is not enough to govern verdict language.

Without a compact verdict grammar, several confusions appear quickly:

- lifecycle labels impersonate judgment,
- support language becomes soft prose rather than governed state,
- rejection and withdrawal get confused,
- lineage events get faked as verdict labels,
- public release wording drifts away from the underlying object graph.

This note resolves that ambiguity at the first useful level.

---

## What a verdict is

A verdict is not merely a UI badge.
It is a governed institutional judgment on a target claim.

At the current stage, a verdict should answer at least these questions:

- what claim is being judged,
- what the current institutional standing is,
- what basis objects materially support that standing,
- what unresolved dissent remains,
- and what would justify upgrade, downgrade, or reopening.

A verdict therefore sits at the junction of:

- claim identity,
- evidentiary pressure,
- challenge pressure,
- dependency admissibility,
- and institutional reading.

---

## Current verdict floor

The current cross-pilot verdict floor is:

- `under_evaluation`
- `supported`
- `contested`
- `weakened`
- `rejected`
- `stabilized`

That does **not** mean every project must stop there forever.
It means the system now has a compact lawful floor strong enough to make verdict language legible and governable.

---

## Core verdict levels

### 1. `under_evaluation`

Meaning:

> the claim is currently under active institutional assessment and has not yet earned a stronger current judgment.

Typical use:

- newly introduced claim,
- reopened claim after new basis arrives,
- claim whose support and challenge landscape has not yet been judged to a stronger current state.

This is the lawful default floor.

### 2. `supported`

Meaning:

> the current governed reading is net-positive: available support is currently sufficient for a positive institutional judgment, while remaining open to future challenge.

Typical use:

- support objects materially sustain the claim,
- challenge pressure exists but is not currently decisive,
- dependencies are not known to be materially broken.

`supported` is not the same as final, immune, or historically closed.

### 3. `contested`

Meaning:

> the claim is under live, nontrivial institutional challenge such that the current reading must visibly retain that dispute.

Typical use:

- decisive support-pressure and challenge-pressure are both present,
- major dissent remains unresolved,
- dependency or admissibility concerns are still actively open.

`contested` does not automatically mean false.
It means the current institutional surface must visibly carry dispute.

### 4. `weakened`

Meaning:

> the claim has suffered material institutional damage relative to an earlier stronger reading, but the system is not yet justified in treating it as fully rejected.

Typical use:

- major support has eroded,
- important dependencies are damaged,
- significant challenge pressure has landed,
- some route of partial survival or narrower admissibility may remain.

`weakened` is stronger than generic controversy.
It marks real damage.

### 5. `rejected`

Meaning:

> the current institutional reading is that the claim does not presently hold as an admissible supported judgment.

Typical use:

- decisive challenge has landed,
- support has materially failed,
- dependencies are broken without lawful repair,
- or the previous reading can no longer be sustained.

`rejected` is a current institutional judgment, not historical erasure.
A rejected claim can remain visible, cited, and historically important.

### 6. `stabilized`

Meaning:

> the claim has survived challenge, retains durable support, and currently warrants a stronger institutional reading than ordinary support.

Typical use:

- support has remained durable over time,
- major live challenges are resolved, downgraded, or no longer decisive,
- the claim has crossed beyond merely provisional positive reading.

`stabilized` is not a synonym for metaphysical truth.
It is a stronger institutional reading than `supported`.

---

## Verdict relevance versus other state layers

Verdict grammar governs institutional judgment.
It must stay distinct from other layers.

### A. verdict versus lifecycle

Lifecycle answers:

> what is the operational state of the object inside the system?

Verdict answers:

> what is the current institutional judgment on the target claim?

Examples:

- a claim can be `active` and `rejected`,
- a claim can be `archived` and historically important,
- a claim can remain `active` while `contested`,
- a verdict object itself can be revised without changing the target claim’s lifecycle.

So withdrawal, archiving, and supersession must not impersonate verdict.

### B. verdict versus revision

Revision answers:

> is this still the same governed object, now in a new semantic state?

Verdict answers:

> how does the institution currently read the target claim?

A verdict update may require a revision record.
But revision history is not itself the verdict grammar.

### C. verdict versus lineage

Lineage answers:

> how do distinct governed identities stand in ancestry or succession?

Verdict answers:

> what is the current judgment on this specific target claim?

Important rule:

- if a claim only survives by splitting into narrower descendants,
- that is not best modeled as a new verdict token,
- it should be modeled through lineage and succession relations plus distinct verdicts on the resulting claims.

A local project may still use prose like “split” in narrative explanation.
But `split` is **not** part of the first compact cross-pilot verdict floor.

### D. verdict versus publication

Publication answers:

> what is currently shown on a public release surface?

Verdict answers:

> what is the underlying institutional judgment?

A public page may show a verdict.
That does not mean publication created the verdict.

---

## Minimal verdict record shape

The system does not need a huge verdict ontology to start.
A minimal governed verdict record can be described as:

```text
VerdictRecord := {
  verdict_id: string,
  target_claim_id: string,
  verdict_level:
    "under_evaluation" |
    "supported" |
    "contested" |
    "weakened" |
    "rejected" |
    "stabilized",
  issued_at: ISODateTime,
  issued_by: ActorRef,
  summary: string,
  basis_object_ids: string[],
  unresolved_dissent_ids?: string[],
  upgrade_conditions?: string[],
  downgrade_conditions?: string[],
}
```

Optional later additions may include:

- confidence or stability qualifiers,
- policy references,
- institutional signoff class,
- jurisdiction or scope,
- public wording sidecar.

But those are not required for the first useful grammar.

---

## First practical reading rules

### Rule 1. `cites` is not enough

A verdict should not move just because more citation exists.
Citation supports traceability, not verdict force by itself.

### Rule 2. `supports` / `challenges` / `depends_on` carry the main pressure

At the current stage, the main relation families that should materially influence verdict reading are:

- `supports`
- `challenges`
- `depends_on`

These are the first-layer verdict-bearing relation types.

### Rule 3. `weakened` is not a euphemism for `rejected`

Use `weakened` when real damage exists but a lawful route of nontrivial survival remains.
Do not use it as a vague softening move to avoid saying `rejected`.

### Rule 4. `stabilized` has a burden

A claim should not jump to `stabilized` merely because it is currently fashionable or positively read.
It needs stronger institutional durability than ordinary support.

### Rule 5. lineage must stay explicit

If the real change is that one claim gave way to a narrower descendant, use lineage and succession relations.
Do not hide that move inside verdict prose alone.

---

## What this note does **not** claim

This note does **not** claim that:

- every future project must use only these verdict words,
- specialized verdict ladders are forbidden,
- the full transition matrix is already frozen,
- theorem-grade or domain-specific judgment ladders are already standardized,
- or machine automation can issue final verdicts without governance.

It claims something smaller:

> the current system now has a compact verdict floor strong enough to stop the worst judgment drift.

---

## Practical verdict

So the practical verdict is:

- **verdict is now named as a first-class institutional judgment rather than loose page wording**
- **the first compact verdict floor is now explicit**
- **support, contestation, weakening, rejection, and stabilization are no longer muddled together**
- **lineage and publication no longer need to impersonate verdict**
- **the current verdict grammar is now strong enough to support a first transition-admissibility rule**

That is the right size of rule for the current stage.
