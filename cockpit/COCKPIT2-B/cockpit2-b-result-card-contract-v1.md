# COCKPIT2-B Result Card Contract v1

## Status

Drafted for current threshold.

## Function

This file defines the minimum contract for a lawful COCKPIT2-B result card.
A result card is the smallest cockpit-native unit for a structured draft-only trigger output.

---

## Minimum required fields

Every lawful result card must visibly expose all of the following:

1. **title**
2. **output class**
3. **anchor reference**
4. **draft-only honesty marker**
5. **body or structured bullet surface**

Optional but recommended fields include:

- basis hints
- unresolved remainder
- next-step hints
- audit trace note

---

## Required honesty markers

A lawful result card must visibly read as one of the following kinds of bounded output:

- draft
- suggestion
- scan result
- condition check
- prepared summary

A lawful result card must not read as:

- committed update
- resolved verdict
- published output
- completed runtime task

---

## Required anchor posture

A result card must visibly state the current object or route anchor it belongs to.
The card must not float anonymously.

Examples of lawful anchor posture include:

- `Anchor: C-0001 stronger claim`
- `Anchor: hpVerdict stage verdict object`
- `Anchor: power-posing route surface`

---

## Required non-mutation rule

A result card may summarize, suggest, scan, or stage next steps.
It may not itself mutate:

- claim state
- verdict state
- lineage state
- publication state

If a future threshold ever makes some mutation lawful, that will require a separate object and a separate rule surface.

---

## Minimum contract reading

The result card contract exists to ensure that stronger trigger outputs still read as cockpit-governed drafts rather than as stealth writes.
