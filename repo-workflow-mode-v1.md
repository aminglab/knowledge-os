# repo-workflow-mode-v1

## Status

Repository workflow note v1.

## Function

This document records the current **repository workflow mode** of `aminglab/knowledge-os`.

Its purpose is not to define an eternal engineering law.
Its purpose is to state, plainly and operationally:

- how the repository is being worked on **now**,
- why that current mode is acceptable,
- what risks it introduces,
- what conditions would justify changing it,
- and what workflow mode should replace it once the project is no longer effectively a one-person mainline.

This is therefore a workflow-governance note, not a product or protocol note.

---

## Why this document exists

The repository is no longer only a conceptual shell.
It already contains:

- project entry documents,
- protocol working sets,
- a real living case,
- a validation network,
- a publishing pipeline,
- and an expanding Phase 3 public-layer document chain.

That means repository workflow is no longer a trivial detail.
The way changes land in `main` now affects:

- what counts as current project reality,
- where future collaborators will orient themselves,
- how checks and closeout notes are interpreted,
- and how responsibility is understood across repository history.

This note exists to make the current mode explicit rather than leaving it as an accidental habit.

---

## Current repository reality

At the current stage, the repository is effectively being developed in **solo mainline mode**.

That means:

- the active working line is `main`,
- important changes are landing directly on `main`,
- the historical pilot branch is no longer the live center of gravity,
- and the repository is currently being governed as a one-person project rather than as a reviewed multi-maintainer codebase.

This is not a hidden fact.
It is the real working condition of the repository at the moment.

---

## Current workflow mode

### Current verdict

The current repository workflow mode is:

> **direct-to-main solo development**

This means the repository is currently allowed to:

- write directly to `main`,
- treat `main` as both stable trunk and active development line,
- and evolve through small, explicit commits without requiring branch review for every change.

That mode is currently acceptable because the repository is still, in practical terms:

- a one-person governed project,
- with one principal maintainer,
- one active decision chain,
- and no standing multi-person review requirement.

---

## Why direct-to-main is acceptable right now

Direct-to-main is not always good.
But at the current repository stage, it is acceptable for concrete reasons.

### 1. The project is still effectively solo-maintained

The current workflow does not yet need to optimize for many simultaneous authors, asynchronous review queues, or merge negotiation between multiple active branches.

### 2. The repository is still in active conceptual and structural formation

Many recent changes are not only implementation details.
They are:

- stage judgments,
- foundation notes,
- IA notes,
- seed-surface notes,
- and validation or governance refinements.

For a solo project at this stage, forcing every one of those through branch + PR overhead would likely produce more friction than clarity.

### 3. The repository already preserves history through explicit commits

The current direct-to-main mode is not the same thing as silent overwrite.
The project is still leaving a visible history of:

- stage decisions,
- workflow additions,
- validation changes,
- and public-layer direction notes.

### 4. The repository still benefits more from momentum than from review bureaucracy

At the current scale, the larger risk is not “insufficient reviewer ceremony.”
The larger risk is losing coherence or slowing down hard-earned structural progress under premature process weight.

So direct-to-main is currently a reasonable working mode.

---

## What direct-to-main does **not** mean

The current mode should not be misunderstood.

It does **not** mean:

- no discipline,
- no checkpoints,
- no phase closeouts,
- no validation surfaces,
- no audit trail,
- or no future workflow hardening.

It only means that the current repository does not yet require **branch-mediated collaboration** as its default change path.

That is a much narrower claim.

---

## Current discipline inside direct-to-main mode

Even in direct-to-main solo development, the repository should still follow several rules.

### 1. `main` must be treated as real project reality

Because changes land directly on `main`, that branch must be treated as the current authoritative project surface.

### 2. Commits should stay explicit and scoped

A direct-to-main repository cannot afford muddy commits that hide unrelated changes under one vague message.

### 3. Phase and governance notes should continue to objectify major shifts

When the project changes mode, closes a phase, or adopts a major direction decision, that should still be written as an explicit repository artifact rather than left only in commit history.

### 4. Validation should continue to grow where it meaningfully reduces drift

Direct-to-main is safer when the repository has visible checks guarding important surfaces.
That is already happening in the current case line and should continue where useful.

### 5. Historical branches should not be mistaken for the active mainline

Old pilot branches may remain informative.
But they should not be treated as if they still define current repository direction when `main` has clearly moved beyond them.

---

## Risks of staying in direct-to-main too long

The current mode is acceptable now.
It should not be universalized carelessly.

If the repository stays in direct-to-main mode past the point where collaboration complexity rises, several risks appear.

### 1. Review ambiguity

Once more than one real contributor is landing important changes, direct-to-main makes it harder to know:

- who reviewed what,
- what was proposed versus accepted,
- and whether a change was meant as a draft, experiment, or repository reality.

### 2. Merge-context loss

Branches and PRs are not only for code mechanics.
They preserve the context of proposal, discussion, and acceptance.
Without them, multi-person change history becomes flatter and less interpretable.

### 3. Harder rollback boundaries

When multiple people begin changing different surfaces, branch-based staging makes it easier to isolate and revert work without collateral confusion.

### 4. Main-branch overload

If every experimental, provisional, and production-facing change lands directly on `main`, the main branch can become harder to read as a stable project surface.

### 5. Collaboration trust friction

New collaborators usually need a workflow where they can:

- propose changes,
- receive feedback,
- revise safely,
- and merge with confidence.

Direct-to-main is often too exposed for that.

---

## Workflow change trigger conditions

The repository should **not** switch workflow mode only because “PRs are more professional.”
It should switch when the actual project condition changes.

The most important trigger conditions are these.

### Trigger 1. A second real maintainer begins landing substantive changes

This is the cleanest switch condition.
Once another person is making meaningful changes to repository structure, workflow, product surfaces, validation, or protocol artifacts, direct-to-main should stop being the default.

### Trigger 2. Experimental work needs safe staging before acceptance

If the project begins to carry larger experimental implementation work, UI rewrites, renderer shifts, or multi-file refactors that should be inspected before becoming repository reality, branch-mediated review becomes more valuable.

### Trigger 3. `main` needs stronger stability guarantees

If the repository reaches a stage where `main` must become a more clearly stable trunk for other people to rely on, then direct-to-main becomes less appropriate.

### Trigger 4. Contributors need review context, not just commit history

Once collaboration depends on visible proposal / review / merge context, PR-based workflow should become default.

### Trigger 5. Protected branch rules become worth the cost

When checks, review gates, and merge discipline provide more clarity than friction, it is time to move beyond direct-to-main.

---

## Recommended future workflow mode

Once the repository crosses those trigger conditions, the recommended workflow mode becomes:

> **branch + pull request + protected main**

That future mode should mean:

- `main` becomes the protected stable trunk,
- feature work lands on short-lived branches,
- pull requests become the default merge path,
- checks run before merge,
- and important repository changes gain visible review context.

This does not require heavyweight bureaucracy.
It only requires that the repository stop treating `main` as the place where every draft becomes reality immediately.

---

## Minimum future branch model

When the repository does switch, the minimum future model should be simple.

### Branch types

- `main` — protected stable trunk
- `feature/...` — focused implementation work
- `docs/...` — substantial documentation or governance-note work when review is useful
- `fix/...` — bounded fixes

The project does **not** need a large enterprise branching taxonomy.
It only needs enough branch structure to preserve proposal and review context.

---

## Minimum future PR model

Once the switch happens, pull requests should become the normal path for:

- significant implementation changes,
- validation network changes,
- public-layer surface changes,
- protocol-floor changes,
- and repository workflow changes.

Small typo-only or trivial copy fixes may still remain lightweight.
The point is not ceremony for its own sake.
The point is making meaningful repository change legible under collaboration.

---

## Minimum future protection model

When collaboration becomes real, the repository should consider at least:

- protecting `main`,
- requiring passing checks before merge,
- and using PRs as the default merge path.

Additional review requirements can be added later if and when they become worth the friction.

The future model should stay proportionate to project reality.

---

## Transition rule

The repository should not drift silently from solo-main mode into quasi-collaborative chaos.

When one or more trigger conditions are met, the workflow mode should be deliberately re-declared.

That later transition can be recorded in a successor document, for example:

- `repo-workflow-mode-v2.md`

The important thing is that the mode change should be explicit.

---

## Current verdict

Current verdict:

> The repository is currently in a legitimate **direct-to-main solo development** mode.
>
> That mode is acceptable because the project is still effectively one-person governed, structurally formative, and better served by explicit momentum than by premature collaboration ceremony.
>
> But this mode is conditional, not permanent.
>
> Once real multi-person maintenance, review need, or stability pressure appears, the repository should shift to **branch + pull request + protected main**.

That is the current workflow-governance ruling.

---

## Immediate practical consequence

Until the trigger conditions appear, the repository may continue to:

- write directly to `main`,
- use explicit commits,
- rely on growing validation surfaces,
- and objectify major workflow or stage shifts through repository documents.

But the project should now remember one thing clearly:

> direct-to-main is the current mode because of the current project condition, not because repository workflow does not matter.

---

## Consolidated closing sentence

`main` is currently both the stable trunk and the active solo development line.
That is acceptable for the current repository stage.
But it should be treated as a temporary workflow mode earned by solo governance, not as a permanent rule for a future multi-person Knowledge OS repository.
