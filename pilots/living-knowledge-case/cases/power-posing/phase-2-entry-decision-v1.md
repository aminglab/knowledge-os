# phase-2-entry-decision-v1

## Status

Phase entry decision note v1.

## Function

This document decides where **Phase 2** should begin for the `power-posing` line.

It does not open two parallel programs at once.
Its purpose is narrower:

- evaluate the two most natural post-Phase-1 directions,
- decide which one should become the actual entry line,
- record why the other line is not the first move,
- and keep the project from drifting back into simultaneous overexpansion.

---

## Candidate entry lines

At the end of Phase 1, two next-step candidates became natural.

### Candidate A

Lift **object-envelope enforcement** from a case-scoped checker toward a broader pilot-level checker.

### Candidate B

Continue hardening the **public release surface** of `power-posing`, while keeping the discipline that the page layer must not become a second public storyline independent of the snapshot release layer.

---

## Evaluation of Candidate A

Candidate A is attractive because the object-envelope checker is now real, automated, and already passing a first workflow run.

That creates a natural temptation:

> if the checker is working, lift it immediately.

But Phase 2 should not begin there.

### Why not

1. **The current evidence base is still too narrow**  
   The checker has only been exercised against one real case line.
   That is enough to prove local value, but not enough to justify a broader pilot-level abstraction yet.

2. **A premature lift would risk fake generality**  
   The current object families and field patterns are still heavily informed by `power-posing`.
   Lifting too early would blur the distinction between:
   - a working case-scoped protocol floor,
   - and a genuinely broader pilot-level checker.

3. **The project still has only one mature public-facing living case**  
   The repository is not yet in a position where cross-case enforcement pressure is the dominant need.
   The stronger need is still to improve the quality and discipline of the one public case that already exists.

### Interim judgment on Candidate A

> Keep object-envelope enforcement **case-scoped for now**.
>
> Treat pilot-level lifting as a later Phase 2 or Phase 3 question, not as the entry move.

---

## Evaluation of Candidate B

Candidate B should become the actual Phase 2 entry line.

### Why Candidate B is the better entry move

1. **The repository now has a real public-facing living case in `main`**  
   That makes public release quality the most valuable next pressure point.

2. **Phase 1 already built the necessary floor**  
   Public/developer path splitting, homepage tightening, snapshot-to-page publication-chain clarification, and object-envelope enforcement are now in place.
   That means the release surface can be hardened from a better base than before.

3. **The public surface is where repository reality is most exposed**  
   A protocol floor matters, but the current project still lives or dies in large part on whether the public case reads clearly, coherently, and without role confusion.

4. **This line remains seam-compatible**  
   Hardening the public release surface of the first case continues to work at the seam level.
   It does not force a premature jump to a generic framework.

### Interim judgment on Candidate B

> Begin Phase 2 with continued hardening of the `power-posing` public release surface.
>
> Keep the governing rule explicit:
>
> - object layer is upstream,
> - snapshot layer is the current public release layer,
> - page layer is downstream presentation,
> - and no second public storyline should emerge.

---

## Phase 2 entry verdict

Current verdict:

> Phase 2 should begin on **Candidate B**.
>
> The next entry line is continued hardening of the `power-posing` public release surface.
>
> Candidate A remains open, but it is deferred as a later lifting question rather than the first Phase 2 move.

---

## Immediate operational consequence

The next work should therefore concentrate on the current public release surface of `power-posing`.

That means Phase 2 should prioritize improvements such as:

1. making the public homepage and page surface read more coherently as one release object,
2. preserving the one-direction publication chain from objects to snapshot to page,
3. reducing any remaining ambiguity between public-reading and governance-reading surfaces,
4. and hardening the page as a public release surface without turning it into an independent editorial layer.

The object-envelope checker should remain in force during this work,
but broader lifting of that checker is not the Phase 2 entry action.

---

## Guardrail

The Phase 2 guardrail is simple:

> do not begin by generalizing the floor before the first public release surface is fully worth generalizing.

That is the key discipline preserved by this decision.
