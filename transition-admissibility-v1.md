# Transition admissibility v1

This note records the **first compact transition-admissibility rule** for Knowledge OS.

It is intentionally small.
It does not attempt a full legal state machine for the entire platform.
It does not define every future action sequence.
It does something narrower and more useful:

> it gives the current system a governed way to say which verdict transitions are ordinary,
> which ones are guarded,
> which ones are disallowed,
> and when a change should be modeled as lineage, lifecycle, or publication rather than verdict movement.

---

## One-sentence ruling

Current ruling:

> **Verdict movement is governed, not rhetorical.**
> **A claim may move between verdict levels only through named admissible transitions backed by explicit basis, explicit rationale, and preserved separation between verdict, relation, lifecycle, and lineage.**

That is the whole point of this note.

---

## Why this note exists now

The repository now has:

- a revision model,
- an action grammar,
- an object relation grammar,
- and a compact verdict floor.

That is enough to name the pieces.
It is not enough to govern movement between them.

Without a transition rule, several bad habits appear quickly:

- claims jump from vague support to vague rejection with no explicit threshold,
- stabilization gets used as enthusiasm rather than governed state,
- reopening happens silently,
- claim splitting is smuggled into verdict wording,
- lifecycle or publication changes impersonate epistemic movement.

This note resolves that ambiguity at the first useful level.

---

## Scope of this note

This note governs **verdict transitions on target claims** at the first compact cross-pilot level.

It does **not** yet attempt to freeze:

- the whole object-lifecycle state machine,
- every domain-specific theorem ladder,
- every institution-specific approval process,
- or every multi-action workflow.

It is narrower:

> it defines the current admissibility floor for moving between the first verdict levels.

---

## Current verdict floor in scope

This transition rule applies to the current compact verdict levels:

- `under_evaluation`
- `supported`
- `contested`
- `weakened`
- `rejected`
- `stabilized`

---

## Three transition classes

At the current stage, verdict transitions should be read in three classes:

### A. ordinary admissible

These are normal governed moves that can occur without extraordinary burden, provided basis and rationale are explicit.

### B. guarded admissible

These are lawful, but they require stronger explicit burden because they compress or reverse substantial institutional movement.

### C. disallowed as pure verdict moves

These should not be modeled as verdict movement alone.
They require lineage, lifecycle, publication, or a more complex governed workflow.

---

## Ordinary admissible transitions

### 1. `under_evaluation -> supported`

Lawful when:

- support pressure is materially positive,
- no decisive unresolved challenge blocks a positive reading,
- and dependencies are not known to be materially broken.

### 2. `under_evaluation -> contested`

Lawful when:

- the claim enters institutional reading already under material unresolved challenge,
- or evidence and dissent arrive together strongly enough that dispute must be surfaced immediately.

### 3. `under_evaluation -> weakened`

Lawful when:

- the first governed reading already shows material damage relative to a previously assumed stronger reading,
- but current basis does not justify full rejection.

This is less common as an initial state, but still lawful.

### 4. `under_evaluation -> rejected`

Lawful when:

- decisive challenge or dependency failure is already clear,
- and the claim does not currently earn a supported or weakened reading.

### 5. `supported -> contested`

Lawful when:

- new nontrivial challenge lands,
- major dissent is reopened,
- or an important dependency becomes questionable enough that the public institutional reading must visibly carry dispute.

### 6. `supported -> weakened`

Lawful when:

- support materially erodes,
- dependency damage lands,
- or challenge pressure reduces the claim below ordinary positive reading without fully collapsing it.

### 7. `supported -> stabilized`

Lawful when:

- the claim has durable support,
- major challenge pressure has been answered, downgraded, or absorbed,
- and the institution is justified in moving beyond ordinary support.

### 8. `contested -> supported`

Lawful when:

- the main live challenge has been answered or downgraded,
- and support now clearly outweighs remaining dispute.

### 9. `contested -> weakened`

Lawful when:

- the claim survives, but with material loss relative to the earlier positive route,
- or challenge pressure reveals only a narrower or damaged route of survival.

### 10. `contested -> rejected`

Lawful when:

- challenge pressure decisively breaks current admissibility,
- and no currently lawful route of nontrivial survival remains.

### 11. `weakened -> contested`

Lawful when:

- the claim remains damaged,
- but the institution must now visibly carry an active open dispute rather than only a downgraded weakened reading.

### 12. `weakened -> rejected`

Lawful when:

- the residual route of survival fails,
- or remaining support no longer justifies nontrivial survival.

### 13. `weakened -> supported`

Lawful when:

- the damaging condition has been answered, repaired, or superseded by stronger lawful basis,
- and the claim again earns ordinary positive reading.

This move is lawful, but in practice often carries more burden than a small routine update.

---

## Guarded admissible transitions

These moves are lawful, but they should carry explicit stronger burden.

### 1. `supported -> rejected`

This is lawful only when:

- decisive adverse basis lands,
- the collapse is clear enough that a stop through `contested` or `weakened` would be institutionally misleading,
- and the rationale explicitly names why the stronger jump is justified.

### 2. `rejected -> under_evaluation`

This is the compact lawful **reopen** move.

It is lawful only when:

- materially new basis arrives,
- the new basis is not merely recycled wording over already defeated support,
- and the institution explicitly records reopening rather than silently softening the old rejection.

### 3. `rejected -> weakened`

Lawful only when:

- new basis does not yet justify ordinary positive support,
- but it is enough to restore a nontrivial route of survival.

This should be rarer than `rejected -> under_evaluation`.

### 4. `rejected -> supported`

Lawful only under especially strong new basis and explicit rationale.

In most cases, the cleaner route is:

- `rejected -> under_evaluation`
- then later to `supported` if warranted.

### 5. `stabilized -> contested`

Lawful only when:

- substantial new challenge lands,
- and the institution must visibly re-open dispute on what had previously become durable.

### 6. `stabilized -> weakened`

Lawful only when:

- the stable positive route has materially degraded,
- but immediate rejection would overstate the collapse.

### 7. `stabilized -> rejected`

Lawful only in extraordinary cases.

This should require explicit high-burden rationale because it compresses a major institutional collapse.

---

## Disallowed as pure verdict moves

The following should **not** be modeled as verdict movement alone.

### 1. “split” as a verdict token

If the real institutional change is:

- the old claim breaks into narrower descendants,
- or only a narrower successor survives,

that should be modeled using:

- lineage relations,
- succession relations,
- and distinct verdicts on the resulting claims.

Do not fake that whole move as one special verdict word.

### 2. publication-only movement

Changing:

- what snapshot is public,
- what page is shown,
- what reading path is foregrounded,

is not by itself a verdict transition.

### 3. lifecycle-only movement

Changing:

- `active`
- `paused`
- `withdrawn`
- `archived`

is not by itself a verdict transition.

### 4. citation-only or formatting-only movement

More citation, nicer prose, or richer metadata does not by itself justify verdict movement.

---

## Minimum transition obligations

Every lawful verdict transition should explicitly name at least:

- the `target_claim_id`,
- the `from` verdict level,
- the `to` verdict level,
- the basis objects materially responsible,
- the unresolved dissent situation,
- the actor or authority issuing the move,
- and a short rationale for why this transition class is admissible.

At the current stage, silent verdict jumps are governance failure.

---

## Relation-aware transition rule

The most important relation families for verdict movement are currently:

- `supports`
- `challenges`
- `depends_on`

Current rule:

- verdict transitions should usually be explainable in terms of changes in these pressure-bearing relations,
- while `cites` and `pinned_in_snapshot` should not by themselves drive verdict movement,
- and `descends_from` / `supersedes` should explain routing and lineage rather than impersonate verdict force.

---

## Reopen rule

A rejected claim is not dead history.
But reopening must be explicit.

Current compact rule:

> **reopening is lawful only through named guarded transition with materially new basis.**

That means:

- no silent drift from `rejected` back to `supported`,
- no rhetorical softening without explicit new grounds,
- and no pretending that public rephrasing alone counted as reopening.

---

## Stabilization rule

`stabilized` has a higher burden than `supported`.

Current compact rule:

> **stabilization requires durability, not just current positivity.**

So a claim should not be marked `stabilized` merely because:

- one favorable artifact appeared,
- the public narrative is tidy,
- or current supporters are loud.

It needs stronger governed durability.

---

## Transition versus revision

A verdict transition often co-occurs with revision activity.
It must not be collapsed into revision history alone.

Revision answers:

> what changed in this governed object state?

Transition admissibility answers:

> was the move from one judgment level to another lawful, and under what burden?

Those are related, but not identical questions.

---

## What this note does **not** claim

This note does **not** claim that:

- the full platform transition matrix is finished,
- every institution must use the same burden thresholds,
- all guarded transitions are numerically quantified,
- theorem-grade ladders are already standardized,
- or automation can move verdict state without governance.

It claims something smaller:

> the current system now has a compact admissibility floor strong enough to stop the worst verdict-jump drift.

---

## Practical verdict

So the practical verdict is:

- **verdict movement is now governed as admissible transition rather than rhetorical mood shift**
- **ordinary, guarded, and disallowed transition classes are now explicit**
- **reopen and stabilization now have named burdens**
- **lineage, lifecycle, and publication can no longer quietly impersonate verdict transition**
- **the current transition rule is now strong enough to support later matrix hardening without pretending the full law code is already done**

That is the right size of rule for the current stage.
