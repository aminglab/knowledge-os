# COCKPIT1-C Entry Decision v1

## Status

Entered at current threshold.

## Function

This file records the entry decision for **COCKPIT1-C / Prototype Semantic Contract and Calibration v1**.

COCKPIT1-B created the first static cockpit skeleton.
The next lawful step is to tighten its semantic floor so the prototype does not drift into a pretty but under-specified mockup.

---

## One-sentence entry verdict

Current entry verdict:

> **ENTER_COCKPIT1_C_SEMANTIC_CONTRACT**
>
> The project may now enter prototype semantic contract and calibration because a first static cockpit skeleton already exists and must now be constrained by machine-checkable frontend semantics.

---

## Immediate purpose

COCKPIT1-C exists to do four things:

1. define the minimum semantic contract for the cockpit screens;
2. define the minimum slot contract for the cockpit frame;
3. calibrate the prototype against the bounded case fixtures;
4. attach a lightweight checker so the prototype can fail for real drift rather than visual guesswork.

---

## Boundary

COCKPIT1-C does **not**:

- add live backend behavior
- add runtime model routing
- turn the static prototype into a production app
- expand to team-layer functionality
- claim complete accessibility or responsive implementation coverage

It only hardens the semantic floor of the existing static skeleton.

---

## Final decision block

- entry verdict: `ENTER_COCKPIT1_C_SEMANTIC_CONTRACT`
- proof target: `machine-checkable static cockpit semantics`
- implementation overclaim: forbidden
