# Living Knowledge Case Pilot

This pilot is a public-facing test of one central idea behind **Knowledge OS**:

> important knowledge should not freeze at publication.

The purpose of this pilot is not to build a full product in one step.
It is to pressure-test the object language in a case that an outside reader can quickly understand.

## What this pilot is for

This pilot tries to answer a practical question:

**What would it look like if a disputed scientific claim were managed as a living knowledge object rather than as a static paper trail?**

That means modeling a case as governed objects such as:

- claims,
- evidence,
- dissent,
- verdicts,
- lineage,
- and snapshots.

## Current first case

The first case in this pilot is:

- [`cases/power-posing/`](./cases/power-posing/)

This case was chosen because it is easy to understand, publicly legible, and structurally rich:

- an initial high-impact claim,
- early amplification,
- later replication failure,
- internal withdrawal of support,
- methodological attack,
- and a split between the original claim and a weaker surviving descendant.

## What success looks like

This pilot is successful if it makes one thing obvious:

**a claim should have a visible lifecycle.**

A reader should be able to see:

- what the original claim was,
- what evidence supported it,
- what dissent accumulated,
- what later verdict emerged,
- and whether the claim died, split, weakened, or stabilized.

## Current structure

```text
pilots/living-knowledge-case/
  README.md
  cases/
    power-posing/
      README.md
      case.md
      objects/
        claims/
        evidence/
        dissents/
        verdicts/
      timeline/
      snapshots/
```

## Important constraint

This pilot is a working structure, not a final doctrine.
It exists to help the repository move from abstract language to a live public case.
