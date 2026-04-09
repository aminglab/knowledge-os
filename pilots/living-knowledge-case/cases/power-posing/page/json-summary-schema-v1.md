# JSON Summary Schema v1

This file documents the **current stable machine-readable contract** for:

```bash
python generate_page_data.py --json-summary
python generate_page_data.py --check --json-summary
```

It exists for one reason:

> downstream automation should not have to infer the structure of the generator output by reading Python code.

This is still a small case-scoped publishing tool.
But its JSON output is now important enough to deserve an explicit schema document.

---

## Status of this schema

**Schema status:** working stable contract for the current generator

This does **not** mean the generator can never evolve.
It means that changes to the JSON field names, value meanings, or success/failure shape should now be treated as deliberate interface changes rather than casual script edits.

If the contract changes materially, the schema document should be versioned forward rather than silently rewritten.

---

## Scope

This schema applies only to the JSON emitted by:

- `generate_page_data.py --json-summary`
- `generate_page_data.py --check --json-summary`

It does **not** describe:

- the structure of `page-data.js`
- the internal object model
- the page renderer payload
- or future multi-case generator interfaces

---

## Stable schema identity

Every JSON payload now self-identifies with these top-level fields:

- `schema_name`
- `schema_version`

### Current stable values

- `schema_name = "power_posing_json_summary"`
- `schema_version = "v1"`

These fields are present in both success and failure payloads.

---

## Top-level success payload

When validation passes, the generator emits a JSON object with these top-level keys:

- `schema_name`
- `schema_version`
- `validation_status`
- `check_mode`
- `write_status`
- `output_path`
- `release_summary`

### Field meanings

#### `schema_name`
String.

Current stable value:

- `"power_posing_json_summary"`

#### `schema_version`
String.

Current stable value:

- `"v1"`

#### `validation_status`
String.

Current stable success value:

- `"passed"`

#### `check_mode`
Boolean.

- `true` when the generator ran with `--check`
- `false` otherwise

#### `write_status`
String.

Current stable success values:

- `"completed"`
- `"skipped"`

Meaning:

- `completed` means validation passed and `page-data.js` was written
- `skipped` means validation passed but file writing was intentionally skipped because `--check` was active

#### `output_path`
String or `null`.

- string path when writing occurred
- `null` when writing was skipped in `--check` mode

#### `release_summary`
Object containing the current release-surface counts.

Current stable keys:

- `objects_total`
- `claims`
- `evidence_objects`
- `dissents`
- `verdicts`
- `canonical_source_ids`
- `status_cards`
- `neighborhood_cards`
- `timeline_entries`
- `reading_path_links`

All current values are integers.

---

## Top-level failure payload

When validation fails, the generator emits a JSON object with these top-level keys:

- `schema_name`
- `schema_version`
- `validation_status`
- `check_mode`
- `write_status`
- `output_path`
- `errors`

### Field meanings

#### `schema_name`
String.

Same stable value as in the success payload.

#### `schema_version`
String.

Same stable value as in the success payload.

#### `validation_status`
String.

Current stable failure value:

- `"failed"`

#### `check_mode`
Boolean.

Same meaning as in the success payload.

#### `write_status`
String.

Current stable failure value:

- `"skipped_due_to_validation_failure"`

#### `output_path`
Always `null` on validation failure.

#### `errors`
Array of strings.

Each entry is one human-readable validation error line.
The order is not guaranteed to be a semantic sort order and should not be treated as such by downstream consumers.

---

## Structural invariants

Downstream automation may rely on these current invariants:

### Success path
If `validation_status == "passed"`, then:

- `schema_name == "power_posing_json_summary"`
- `schema_version == "v1"`
- `release_summary` is present
- `errors` is absent
- `write_status` is either `"completed"` or `"skipped"`

### Failure path
If `validation_status == "failed"`, then:

- `schema_name == "power_posing_json_summary"`
- `schema_version == "v1"`
- `errors` is present
- `release_summary` is absent
- `write_status == "skipped_due_to_validation_failure"`
- `output_path == null`

---

## Exit-code relationship

The JSON schema is paired with the current exit-code discipline of the generator:

- exit code `0` → validation passed and the requested action completed
- exit code `1` → validation failed
- exit code `2` → command-line usage error from `argparse`

A well-behaved automation should check both:

1. the process exit code
2. the JSON payload shape

Do not rely on only one of them.

---

## Current success example

```json
{
  "schema_name": "power_posing_json_summary",
  "schema_version": "v1",
  "validation_status": "passed",
  "check_mode": true,
  "write_status": "skipped",
  "output_path": null,
  "release_summary": {
    "objects_total": 8,
    "claims": 2,
    "evidence_objects": 1,
    "dissents": 3,
    "verdicts": 2,
    "canonical_source_ids": 6,
    "status_cards": 2,
    "neighborhood_cards": 7,
    "timeline_entries": 7,
    "reading_path_links": 7
  }
}
```

---

## Current failure example

```json
{
  "schema_name": "power_posing_json_summary",
  "schema_version": "v1",
  "validation_status": "failed",
  "check_mode": false,
  "write_status": "skipped_due_to_validation_failure",
  "output_path": null,
  "errors": [
    "C-0001: undefined source_ref `Some_Missing_Source`"
  ]
}
```

---

## What should count as a breaking change

The following should be treated as schema-breaking unless deliberately versioned:

- renaming `schema_name`
- renaming `schema_version`
- changing the meaning of the current schema identity values without versioning forward
- renaming any other top-level key
- renaming any `release_summary` key
- changing `write_status` meanings
- changing success from `release_summary` to a different shape
- changing failure from `errors[]` to some unrelated structure

The following are usually non-breaking:

- changing the numeric values themselves
- adding a clearly optional new field with documentation
- improving the human-readable terminal output in non-JSON mode

---

## Current discipline

If the generator evolves further, prefer this order:

1. preserve existing fields when possible
2. append optional fields rather than renaming required ones
3. document any new field here before treating it as reliable automation surface
4. version forward if the payload shape materially changes

That keeps the JSON output from turning back into script folklore.
