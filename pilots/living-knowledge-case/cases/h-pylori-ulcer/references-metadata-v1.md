# References Metadata v1

This file is the current **stable source metadata layer v1** for the H. pylori case.

It is a stricter companion to `references.md`.
The goal is not to freeze a repository-wide citation constitution, but to give the second living case a hard metadata floor that can later support object checks, source pages, and snapshot summaries.

---

## Scope and status

This file is still case-scoped.
It does **not** claim to be a universal Knowledge OS citation doctrine.

What it does claim is narrower and more concrete:

- every canonical source id used by current objects is declared here,
- every declared source carries a stable minimum metadata surface,
- exact object usage is recorded in a machine-readable way,
- and the source-pack index can later grow into a richer source-page layer.

---

## Canonical source ids currently used by objects

The current object skeleton uses these canonical ids in frontmatter:

- `Warren_1983_Lancet`
- `Marshall_Warren_1984_Lancet`
- `Nobel_2005_Hpylori`
- `NIH_1994_Consensus`
- `Review_1995_Hpylori_Peptic_Ulcer`
- `NIDDK_Peptic_Ulcers_Overview`
- `NIDDK_Peptic_Ulcer_Treatment`
- `NCI_Hpylori_Cancer_Fact_Sheet`

---

## Current source structure

At the current stage, the rough division of labor is:

- `references.md` — thin reader-facing entrypoint
- `references-metadata-v1.md` — stable metadata layer
- `sources/` — source-pack index and later source-page growth path

This is the current source-surface structure of the second case.

---

## Required metadata surface for this case

Each source entry below is expected to expose at least:

- `Source type`
- `Authors`
- `Year`
- `Title`
- `Venue / host`
- `Canonical locator`
- `Role in case`
- `Object usage`
- `Notes`

That minimum surface is intentionally modest.
It is strong enough to stabilize the current second-case skeleton without pretending that the repository already has a final cross-case citation doctrine.

---

## Core sources

### `Warren_1983_Lancet`
- Source type: journal_article
- Authors: J. R. Warren and B. Marshall
- Year: 1983
- Title: _Unidentified curved bacilli on gastric epithelium in active chronic gastritis_
- Venue / host: The Lancet
- Canonical locator: PMID `6134060`
- Role in case: early observation surface for bacteria on gastric epithelium in active chronic gastritis
- Object usage: `E-0001`
- Notes: used in this case as part of the early observation route that destabilized the assumption that ulcer-relevant gastric surfaces were bacterially irrelevant.

### `Marshall_Warren_1984_Lancet`
- Source type: journal_article
- Authors: B. J. Marshall and J. R. Warren
- Year: 1984
- Title: _Unidentified curved bacilli in the stomach of patients with gastritis and peptic ulceration_
- Venue / host: The Lancet
- Canonical locator: DOI `10.1016/S0140-6736(84)91816-6`; PMID `6145023`
- Role in case: stronger early causal and cultivation-linked challenge to the dominant ulcer model
- Object usage: `C-0001`, `E-0001`
- Notes: used here as the clearest early publication object in the transition from observational anomaly to causal pressure.

### `Nobel_2005_Hpylori`
- Source type: prize_record
- Authors: Nobel Prize Outreach / Nobel Assembly at Karolinska Institutet
- Year: 2005
- Title: _The Nobel Prize in Physiology or Medicine 2005_
- Venue / host: NobelPrize.org
- Canonical locator: Nobel Prize page for Physiology or Medicine 2005
- Role in case: later stabilization anchor for the core claim
- Object usage: `E-0001`, `V-0001`
- Notes: used here not as primary experimental evidence, but as a public-facing stabilization marker.

### `NIH_1994_Consensus`
- Source type: consensus_statement
- Authors: NIH Consensus Development Panel on Helicobacter pylori in Peptic Ulcer Disease
- Year: 1994
- Title: _NIH Consensus Conference. Helicobacter pylori in peptic ulcer disease_
- Venue / host: JAMA / NIH consensus record
- Canonical locator: PMID `8007082`
- Role in case: consensus-turn anchor
- Object usage: `E-0002`, `E-0003`
- Notes: used here to mark movement from contested disease theory toward accepted clinical doctrine.

### `Review_1995_Hpylori_Peptic_Ulcer`
- Source type: review_article
- Authors: current metadata layer uses the PubMed-indexed review record title as stable locator
- Year: 1995
- Title: _Helicobacter pylori in peptic ulcer disease_
- Venue / host: NIH consensus statement / review record
- Canonical locator: PMID `7920747`
- Role in case: treatment-response and disease-model reinforcement layer
- Object usage: `E-0002`
- Notes: used here as a compact review anchor for the shift from observation to disease-management consequences.

---

## Current clinical and risk-governance sources

### `NIDDK_Peptic_Ulcers_Overview`
- Source type: official_health_guidance
- Authors: National Institute of Diabetes and Digestive and Kidney Diseases
- Year: 2022
- Title: _Peptic Ulcers (Stomach or Duodenal Ulcers)_
- Venue / host: NIDDK
- Canonical locator: NIDDK peptic ulcers overview page
- Role in case: current official disease-frame anchor
- Object usage: `E-0003`, `D-0003`, `V-0002`
- Notes: used here because it explicitly names H. pylori infection and NSAID use as the two most common causes of peptic ulcers.

### `NIDDK_Peptic_Ulcer_Treatment`
- Source type: official_health_guidance
- Authors: National Institute of Diabetes and Digestive and Kidney Diseases
- Year: 2022
- Title: _Treatment for Peptic Ulcers (Stomach or Duodenal Ulcers)_
- Venue / host: NIDDK
- Canonical locator: NIDDK peptic ulcer treatment page
- Role in case: current treatment-path anchor
- Object usage: `C-0002`, `E-0002`, `E-0003`, `V-0002`
- Notes: used here because it makes the detect-treat-retest clinical path publicly legible.

### `NCI_Hpylori_Cancer_Fact_Sheet`
- Source type: official_health_guidance
- Authors: National Cancer Institute
- Year: 2023
- Title: _Helicobacter pylori (H. pylori) and Cancer_
- Venue / host: National Cancer Institute
- Canonical locator: NCI fact sheet on H. pylori and cancer
- Role in case: extension and public-risk guardrail anchor
- Object usage: `C-0002`, `D-0003`, `V-0002`
- Notes: used here to keep the case honest about cancer-risk extension, testing/treatment scope, and the dangers of careless overgeneralization.

---

## Current note

This metadata layer is intentionally still narrow.
A later repository-wide source doctrine may standardize additional fields such as:

- canonical URL
- quote excerpts
- access date
- publication and update timestamps
- snapshot section usage
- evidence weight or role subtype

But at the current stage, the second case already has a real source floor:

- entry,
- metadata,
- and a source-pack layer that can later grow into public source pages.
