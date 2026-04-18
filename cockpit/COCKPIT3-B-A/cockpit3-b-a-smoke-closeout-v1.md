# COCKPIT3-B-A Smoke Closeout v1

## Status

Not yet evaluated.

## Function

This file records the narrower smoke-verdict closeout for the current COCKPIT3-B-A prototype route.
It exists to freeze what the current bounded review-boundary prototype can honestly pass once its checker and workflow run cleanly.

---

## Smoke route

The current smoke route is:

1. open the COCKPIT3-B-A prototype;
2. confirm that the review-boundary panel is visible next to a governed result surface;
3. confirm that `review_trigger`, `review_scope`, `review_act`, and `retained_holds` are visible;
4. confirm that `draft_only` / `surface_only` / non-executable remain explicit;
5. confirm that the prototype says operator review is still not execution authority.

---

## Current smoke verdict targets

If the current prototype and checker pass, the following smoke verdicts become lawful:

- `PASS_REVIEW_BOUNDARY_PROTOTYPE_LIFT`
- `PASS_REVIEW_TRIGGER_SCOPE_ACT_VISIBLE`

The following verdicts remain unlawful at this stage:

- execution authorization pass
- governed mutation pass
- team-layer execution pass
- production frontend pass
