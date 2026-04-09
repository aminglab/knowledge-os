# References Metadata v1

This file is the current **stable source metadata layer v1** for the power-posing pilot.

It is a stricter companion to `references.md`.
The goal is not to freeze a repository-wide citation constitution, but to give the first public living case a harder metadata floor that can be checked automatically.

This layer is expected to stay consistent with:

- the governed object layer,
- the public snapshot layer,
- and future release tooling.

---

## Scope and status

This file is still case-scoped.
It does **not** claim to be a universal Knowledge OS citation doctrine.

What it does claim is narrower and more concrete:

- every canonical source id used by current objects is declared here,
- every declared source carries a stable minimum metadata surface,
- and exact object usage is recorded in a machine-checkable way.

---

## Canonical source ids currently used by objects

The current case objects use these canonical ids in frontmatter:

- `Carney_Cuddy_Yap_2010`
- `Ranehill_et_al_2015`
- `Dana_Carney_2016_statement`
- `Simmons_Simonsohn_2016`
- `Early_public_amplification_context`
- `TED_Corrections_2017`

---

## Required metadata surface for this pilot

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
It is strong enough to stabilize the current public case without pretending that the whole repository already has a final citation constitution.

---

## Core sources

### `Carney_Cuddy_Yap_2010`
- Source type: journal_article
- Authors: Carney, Cuddy, & Yap
- Year: 2010
- Title: _Power Posing: Brief Nonverbal Displays Affect Neuroendocrine Levels and Risk Tolerance_
- Venue / host: Psychological Science / Sage Journals
- Canonical locator: DOI `10.1177/0956797610383437`
- Role in case: source for the original strong-form claim
- Object usage: `C-0001`, `E-0001`
- Notes: the abstract states that high-power posers experienced elevations in testosterone, decreases in cortisol, and increased feelings of power and tolerance for risk. The article was first published online on September 20, 2010.

### `Ranehill_et_al_2015`
- Source type: journal_article
- Authors: Ranehill, Dreber, Johannesson, Leiberg, Sul, & Weber
- Year: 2015
- Title: _Assessing the Robustness of Power Posing_
- Venue / host: Psychological Science / Sage Journals
- Canonical locator: DOI `10.1177/0956797614553946`
- Role in case: major empirical replication challenge to the original claim
- Object usage: `D-0001`
- Notes: this replication paper was first published online on March 25, 2015.

### `Dana_Carney_2016_statement`
- Source type: public_statement
- Authors: Dana R. Carney
- Year: 2016
- Title: _My position on “Power Poses”_
- Venue / host: Berkeley faculty page / public PDF statement
- Canonical locator: Berkeley faculty-hosted statement PDF
- Role in case: internal withdrawal of support by the original first author
- Object usage: `C-0002`, `D-0002`
- Notes: the statement explicitly says, “I do not believe that ‘power pose’ effects are real.” It also states that the sample size in the original study was tiny and that the data were flimsy.

### `Simmons_Simonsohn_2016`
- Source type: methodological_preprint_then_publication
- Authors: Simmons & Simonsohn
- Year: 2016
- Title: _Power Posing: P-Curving the Evidence_
- Venue / host: SSRN preprint; later Psychological Science
- Canonical locator: SSRN posting dated June 10, 2016
- Role in case: methodological / meta-evidential attack on the literature profile
- Object usage: `D-0003`
- Notes: this source is used in the pilot as the methodological dissent object rather than as a direct replication source.

---

## Amplification and public circulation

### `Early_public_amplification_context`
- Source type: public_talk
- Authors: Amy Cuddy
- Year: 2012
- Title: _Your body language may shape who you are_
- Venue / host: TEDGlobal / TED talk page
- Canonical locator: TED talk page, posted October 2012
- Role in case: public amplification context
- Object usage: `E-0001`
- Notes: the TED page shows the talk's very large reach and also includes later correction and update context.

### `TED_Corrections_2017`
- Source type: public_corrections_page
- Authors: TED
- Year: 2017
- Title: _Amy Cuddy's “Your body language may shape who you are”: Corrections & Updates_
- Venue / host: TED corrections and updates page
- Canonical locator: TED corrections page, updated August 2017
- Role in case: public-facing acknowledgement that the talk entered an ongoing robustness and reproducibility debate
- Object usage: `C-0002`
- Notes: this source helps anchor the public-facing retreat-and-reframing context around the weaker descendant path.

---

## Current note

This metadata layer is intentionally still narrow.
A later repository-wide source doctrine may standardize additional fields such as:

- canonical URL
- quote excerpts
- source status
- access date
- publication / update timestamps
- snapshot section usage
- evidence weight or role subtype
