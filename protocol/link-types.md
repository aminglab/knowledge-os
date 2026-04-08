# Link Types (Working Set)

This file defines the current working relation vocabulary for Knowledge OS.
It is a practical coordination file, not a frozen protocol doctrine.

---

## Current working link types

- `supports`
- `supported_by`
- `weakens`
- `depends_on`
- `attacks`
- `attacked_by`
- `responds_to`
- `rules_on`
- `ruled_on`
- `splits_from`
- `splits_to`
- `descends_from`
- `supersedes`
- `published_as`
- `derived_from`
- `based_on`
- `cited_by`
- `coexists_with`

---

## Notes

### Direction matters

Where possible, link direction should be chosen deliberately rather than casually.
For example:

- Evidence usually `supports` a Claim.
- A Dissent usually `attacks` a Claim or another object.
- A Verdict usually `rules_on` a Claim.
- A descendant claim may `split_from` an earlier claim.

### Pairs are sometimes useful

Some pilots may temporarily use mirrored relation names such as:

- `supports` / `supported_by`
- `attacks` / `attacked_by`
- `rules_on` / `ruled_on`

This is acceptable during the working phase, but later protocol hardening may standardize one canonical direction with derived reverse views.

### Do not overproduce link types

If every case invents new relation names, the protocol will drift immediately.
Prefer using the current working set unless a new type is genuinely necessary.
