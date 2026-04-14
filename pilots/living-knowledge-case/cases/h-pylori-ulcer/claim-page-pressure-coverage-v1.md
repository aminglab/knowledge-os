# Claim Page Pressure Coverage v1

This note records the current **claim-page pressure / support coverage rule** for the `h-pylori-ulcer` case.

It exists because the second case has already crossed one threshold:

- claim pages are no longer merely present,
- they already have required section structure,
- and the next public-layer hardening move is no longer section existence alone.

The next question is sharper:

> when governed objects place direct support or direct challenge pressure on a claim,
> does the public claim page actually surface those pressure-bearing objects?

---

## One-sentence ruling

Current ruling:

> **If a governed evidence or dissent object directly targets a claim, the claim page should surface that object in the matching support or challenge section.**

Do not let direct pressure-bearing objects disappear behind generic prose.

---

## Why this note exists now

The second case is a good place to harden this rule because the current claim pages already do real neighborhood work.

They do not only contain headings.
They already name evidence and dissent objects directly.

That makes the next architectural move very natural:

- keep the object graph canonical,
- keep the claim page readable,
- and require the readable page to remain faithful to direct pressure-bearing objects.

Without this rule, a claim page could satisfy layering checks while still omitting a key direct support or challenge object.

---

## Scope of this rule

This rule is deliberately narrow.
It applies to:

- direct `supports` links from evidence objects to claim objects,
- direct `challenges` links from dissent objects to claim objects.

It does **not** yet require:

- transitive graph closure,
- full source-to-claim pressure tracing,
- weighted pressure ranking,
- or semantic summarization of every indirect dependency.

This is a first hardening rule, not a full graph-coverage doctrine.

---

## Current minimum obligation

At the current stage, each claim page should satisfy the following.

### 1. Direct support coverage

If one or more evidence objects directly `supports` a claim object, those evidence objects should appear in the claim page's `Support surface` section.

### 2. Direct challenge coverage

If one or more dissent objects directly `challenges` a claim object, those dissent objects should appear in the claim page's `Challenge surface` section.

### 3. Section fidelity over prose blur

The page may still explain the pressure surface in prose.
But prose should not replace direct pressure-bearing object visibility where those objects already exist in the governed layer.

---

## What this note does **not** require

This note does **not** require that claim pages:

- enumerate every indirect relation,
- duplicate full object bodies,
- become graph explorers,
- or abandon human-readable grouping prose.

The goal is not maximal graph dumping.
The goal is faithful public surfacing of direct pressure-bearing objects.

---

## Practical verdict

So the practical verdict is:

- **claim-page layering remains the structural floor**
- **claim-page pressure coverage becomes the next semantic hardening layer**
- **the second case should now keep direct evidence and dissent pressure visible rather than only implicitly described**
