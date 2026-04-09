# case-template-boundary-v1

## Status

Working boundary document v1.

## Function

This document does **not** define a generic multi-case framework, a universal case compiler, or the second case itself.

Its function is narrower:

- inspect the current `power-posing` line as it actually exists,
- distinguish case-specific payload from reusable pilot structure,
- define the first **small reusable template seam** that can already be defended,
- prevent overclaim before a second case is opened.

The operative question is:

> What is the smallest reusable boundary that can already be defended without pretending the whole line is generic?

---

## Non-goals

This document does **not**:

1. authorize opening a second case now,
2. promote the current generator into a generic multi-case generator,
3. merge the current checker network into one unified checker,
4. freeze a global protocol for all future cases,
5. claim that `power-posing` has already become a universal template.

---

## Current layered inventory

The current `power-posing` line is no longer a flat case directory. It already contains a layered structure:

1. **Object layer**  
   Claim, evidence, dissent, and verdict objects specific to the case.

2. **Reference layer**  
   A thin reader-facing entrypoint plus a more stable metadata layer.

3. **Governance wording layer**  
   Explicit verdict grammar and explicit status legend.

4. **Snapshot layer**  
   A public-facing narrative surface that remains tied to governance.

5. **Reader-facing surface layer**  
   README and page-facing reading paths for non-developer readers.

6. **Publishing layer**  
   Case-scoped page generation, validation, summary, and machine-readable output.

7. **Checking layer**  
   Multiple adjacent but non-identical checkers covering page generation, snapshot consistency, reference metadata, verdict grammar, status legend, and public surface.

8. **CI layer**  
   Workflow-level enforcement of those checks.

9. **Meta-governance layer**  
   Atlas, merge assessment, and phase-transition decision documents governing the line itself.

This layered shape is why `power-posing` is no longer just a content example. It is now a candidate template seam.

---

## Boundary classification

### A. Clearly case-specific

These parts remain specific to `power-posing` and must **not** be carried forward as if they were reusable structure.

#### 1. Case payload objects

- the actual claims,
- the actual evidence objects,
- the actual dissent objects,
- the actual verdict objects,
- the actual lineages and dispute history.

These are payload, not reusable shell.

#### 2. Snapshot substance tied to this controversy

- the concrete historical narrative,
- the exact controversy arc,
- the specific public interpretation,
- the case-specific status explanations tied to this dispute.

A future case may also need snapshots, but not this snapshot substance.

#### 3. Reference payload

- the actual source ids,
- the actual bibliographic contents,
- the actual source mapping for this debate.

The existence of a reference metadata layer may be reusable; the contents are not.

#### 4. Hard-coded phrasing and section assumptions tied to this case

Any checker or generator behavior that assumes `power-posing`-specific wording, section naming, or public phrasing remains case-specific unless explicitly parameterized later.

---

### B. Reusable pilot structure

These parts can already be defended as reusable **structure**, even though their payload must be replaced.

#### 1. Layered case architecture

The following layered shape is already reusable in principle:

- object layer,
- reference layer,
- governance wording layer,
- snapshot layer,
- reader-facing surface layer,
- publishing layer,
- checking layer,
- CI layer,
- meta-governance layer.

This does not mean every future case needs identical filenames. It does mean a living knowledge case can already be expected to expose these functional strata.

#### 2. Dual reference pattern

The split between:

- a thin reader-facing `references.md`, and
- a more stable machine- and checker-facing metadata file

is already reusable.

Reader navigation and machine validation are different jobs; this split has already proved its value.

#### 3. Explicit governance wording objects

The decision to externalize governance wording into:

- a verdict grammar document, and
- a status legend document

is already reusable.

This matters because it prevents public-facing language from drifting away from governance.

#### 4. Snapshot must remain linked to governance

A reusable rule now exists:

> The public-facing snapshot must not detach itself from governance.

In practical terms, snapshots should continue to expose or visibly connect to governance wording objects.

#### 5. Case-scoped publishing contract

The idea that a case may have a publishing tool which supports:

- validation,
- check-only mode,
- summary output,
- machine-readable summary,
- schema identity,
- documented contract

is already reusable as a structural pattern.

The current implementation is still case-scoped, but the contract shape is no longer accidental.

#### 6. Multi-checker governance surface

A living knowledge case can legitimately be guarded by multiple adjacent checkers rather than one monolithic checker, provided their boundaries are explicit and non-redundant.

That governance stance is already reusable.

#### 7. CI belongs to case hardening

A reusable lesson now exists:

> once a case has a publishing and governance surface, CI belongs to the case shell.

#### 8. Meta-governance documents for the case line itself

The existence of:

- a check atlas,
- a merge assessment,
- a phase-transition decision

is itself a reusable pattern for hardening a case line before expansion.

---

### C. Mixed: reusable shell, case-specific implementation

These parts already contain reusable value, but only as **shell + rule**, not as immediately generic implementation.

#### 1. `page/generate_page_data.py`

Reusable side:

- the existence of a publishing tool,
- validation and check mode,
- machine-readable summary,
- schema identification,
- a documented output contract.

Case-specific side:

- current path assumptions,
- current file names,
- current field expectations,
- current section expectations,
- current release surface assumptions.

Correct classification:

> reusable publishing-tool pattern, case-specific implementation.

#### 2. Current checker suite

Reusable side:

- checker specialization,
- checker adjacency without forced merger,
- explicit governance of checker boundaries.

Case-specific side:

- current file paths,
- current section names,
- current public wording assumptions,
- current grammar payload.

Correct classification:

> reusable checker-network pattern, case-specific checker bodies.

#### 3. README surface structure

Reusable side:

- separate reader path and developer path,
- visible connection between content and governance,
- explicit reading entrypoints.

Case-specific side:

- exact file references,
- exact narrative sequence,
- exact guidance wording.

Correct classification:

> reusable README surface pattern, case-specific path contents.

---

## Current smallest reusable template seam

The smallest boundary that can already be defended as reusable is **not** the entire `power-posing` case and **not** a generic case compiler.

The smallest defensible seam is:

> a minimal living knowledge case shell consisting of:
>
> - a structured object layer,
> - a split reference surface (reader-facing + metadata-facing),
> - explicit governance wording objects (verdict grammar + status legend),
> - a public snapshot that remains visibly connected to governance,
> - a case-scoped publishing tool with validation/check/summary/schema contract,
> - a multi-checker governance surface,
> - CI workflows enforcing that surface,
> - and meta-governance documents explaining the checker map and current phase decision.

This seam is already more than a one-off case, but less than a generic framework.

That is exactly why it is useful.

---

## What future cases should copy

A future second case, when eventually authorized, should copy the following **kinds of structure**:

1. an object directory with explicit object types,
2. the dual reference pattern,
3. explicit governance wording files,
4. the expectation that snapshot and public surface visibly expose governance,
5. a case-level publishing/check contract,
6. checker specialization rather than one giant undifferentiated checker,
7. CI workflows for those checks,
8. meta-governance files once the case line begins to harden.

---

## What future cases should not copy blindly

A future case should **not** simply clone and preserve:

1. `power-posing` object payload,
2. its controversy-specific snapshot logic,
3. its source ids and reference contents,
4. its case-specific public wording,
5. checker assumptions that are really section-name or phrasing assumptions,
6. generator assumptions that are still path-bound or payload-bound.

In short:

> future cases may copy the shell, but must rewrite the payload.

---

## Practical copy rules for a future second case

When a second case is eventually opened, the correct discipline should be:

### Copy directly

- structural directory expectations,
- the dual reference pattern,
- the idea of explicit grammar and legend files,
- the existence of a snapshot linked to governance,
- checker and workflow roles where still structurally valid,
- meta-governance discipline where needed.

### Rewrite immediately

- all objects,
- all reference metadata contents,
- snapshot prose,
- public-facing README paths,
- grammar payload where case semantics differ,
- checker expectations tied to section names or public phrasing.

### Do not assume yet

- do not assume one generator can already compile multiple cases,
- do not assume one schema now fits every case,
- do not assume current checker boundaries are globally optimal,
- do not assume current file names are final protocol.

---

## Overclaim guardrail

The most important guardrail is:

> The current boundary authorizes a **small reusable template seam**, not a generic multi-case platform.

Therefore the following claims remain unauthorized:

- "the case framework is already generic"
- "the page generator is already multi-case"
- "the current checker network is the final general architecture"
- "opening a second case is now required"

This guardrail matters because premature abstraction would blur the difference between:

- a defendable reusable seam, and
- a speculative general framework.

The first is real. The second is not yet earned.

---

## Recommended next action

After `case-template-boundary-v1.md`, the next action should remain narrow.

The most natural continuation is **not** to open a second case immediately. It is to derive one small follow-on extraction piece, if needed, such as:

- a concise extraction checklist,
- a minimal copy-discipline note,
- or a utility-sharing note for future checker reuse.

Only after that should the project decide whether to:

- further harden `power-posing`,
- open a second case,
- or carefully extract one more utility layer.

---

## Verdict

Current verdict:

> The `power-posing` line has already produced a defendable **small reusable template seam**.
>
> This seam is real enough to document and govern.
>
> It is **not yet** a generic multi-case framework, a universal case generator, or a warrant to open the second case immediately.

Operational consequence:

- proceed with template-boundary hardening,
- do not jump to generalized framework claims,
- do not open the second case yet,
- do not mistake a reusable shell for a finished platform.