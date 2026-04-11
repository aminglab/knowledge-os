# Composer hint hardening v1

This note records a **small local hardening pass** on the current `power-posing` page composer.

It does not redesign the generator.
It does not declare a generic renderer schema.
It only hardens two renderer-side assumptions that were explicitly flagged in `renderer-contract-audit-v1.md`.

---

## Hardening targets

This pass targets exactly two current risks:

1. **title-driven route-section dispatch**
2. **label-driven source-link splitting**

Both were real drift risks.
Neither required a generator redesign to improve.

---

## What changed

### 1. route section dispatch now uses a local `cardRenderer` hint

Before this pass, route-card rendering still depended on a current visible section title comparison inside `render.js`.

After this pass, the composer now keeps the route-card distinction in the local section config itself through:

- `cardRenderer: 'route'`
- `cardRenderer: 'standard'`

This does **not** remove all title coupling.
The section registry is still local and keyed by current case titles.
But it does remove one fragile inline comparison and moves the display decision into the local composer hint layer.

This is a real hardening step.

### 2. source-link splitting now uses href-role classification rather than label text

Before this pass, source-route versus object-touch splitting depended on whether a link label began with `Open source`.

After this pass, the primitive layer now exposes a default source-link role classifier based on href shape:

- `../sources/...`
- `../references-metadata-v1.md#...`

These are treated as `source_route`.
Everything else falls back to `object_touch`.

This is still local renderer logic.
It is not yet a generator field like `source_link_role`.
But it is less fragile than presentation-text coupling.

---

## What this hardening does **not** claim

This note does **not** claim that:

- section semantics are now generic,
- source grouping is now generic,
- the generator has been upgraded,
- or the renderer contract is now fully explicit.

It only claims something smaller:

> two previously implicit composer assumptions are now slightly more machine-readable and less wording-dependent than before.

That is the entire point.

---

## Current residual coupling after hardening

Even after this pass, the following still remain local composer assumptions:

- section config is still keyed by current case titles,
- source grouping is still id-driven,
- card families are still not declared in `page-data.js`,
- source link roles are still not emitted by the generator.

That is acceptable at the current stage.

---

## Practical verdict

So the practical verdict is:

- **hardening succeeded**
- **no generator redesign was needed**
- **two fragile renderer assumptions are now less implicit**
- **the remaining coupling is still small enough to keep local**

This is the right size of move for the current stage.
