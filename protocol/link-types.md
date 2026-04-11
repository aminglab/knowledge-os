# Link Types (Working Set)

This file defines the current working relation vocabulary for Knowledge OS.
It is a practical coordination file, not a frozen protocol doctrine.

---

## Current canonical link floor

The current compact canonical relation floor is now:

- `supports`
- `challenges`
- `cites`
- `depends_on`
- `descends_from`
- `supersedes`
- `pinned_in_snapshot`

These names are the preferred graph language for new authoring.

They align with:

- `object-relation-grammar-v1.md`
- `verdict-grammar-v1.md`
- `transition-admissibility-v1.md`

---

## Direction rule

Current compact convention:

> **source -> target** means:
> the source object is making the governed move named by the relation toward the target object.

Examples:

- Evidence usually `supports` a Claim.
- A Dissent usually `challenges` a Claim or another governed object.
- A Claim may `depends_on` another Claim.
- A descendant Claim may `descends_from` an earlier Claim.
- A newer governed route may `supersedes` an older one.
- A release surface may `pinned_in_snapshot` a governed object state.

The canonical floor prefers one named direction.
Reverse views may still exist in UI or derived rendering.
They should not be the primary authored graph semantics.

---

## Legacy migration vocabulary

Older pilot materials may still contain legacy or mirrored relation names such as:

- `supported_by`
- `weakens`
- `attacks`
- `attacked_by`
- `responds_to`
- `rules_on`
- `ruled_on`
- `splits_from`
- `splits_to`
- `published_as`
- `derived_from`
- `based_on`
- `cited_by`
- `coexists_with`

These names are not treated as the preferred stable target shape anymore.

At the current stage, they should be read as one of:

- legacy pilot-local vocabulary,
- mirrored reverse naming,
- or migration debt waiting to be normalized.

---

## Current migration guidance

### `supported_by`
Prefer canonical authored direction:

- `E-0001 supports C-0001`

rather than:

- `C-0001 supported_by E-0001`

### `attacks` / `attacked_by`
Prefer:

- `D-0001 challenges C-0001`

The new grammar names institutional challenge directly.
It does not need both attack directions as primary graph language.

### `rules_on` / `ruled_on`
These may still appear in older pilot verdict wiring.
Current direction is moving away from treating them as the long-term primary relation language.

Verdict targeting should increasingly become explicit at the verdict-record layer, while relation language stays compact and legible.

### `splits_from` / `splits_to`
Prefer:

- `descends_from`
- `supersedes`

plus lineage-aware narrative where necessary.

The compact grammar no longer treats “split” as a primary canonical graph token.

### `published_as`
Prefer publication-aware pin semantics such as:

- `pinned_in_snapshot`

rather than ambiguous release wording that can be mistaken for truth or endorsement.

---

## Notes

### Do not overproduce link types

If every case invents new relation names, the protocol will drift immediately.
Prefer the current canonical floor unless a new type is genuinely necessary and its need is explicitly explained.

### Canonical floor does not mean total freeze

The current floor is deliberately compact.
Future growth is possible.
But expansion should happen through explicit protocol decisions, not quiet pilot drift.

### Migration is real, not shameful

Older pilot records may continue to use legacy relation names while the system is being tightened.
That is acceptable during migration.

What is no longer acceptable is pretending that legacy variety and canonical floor are the same thing.
