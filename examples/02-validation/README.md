# 02 — Validation

Validate one good item (passes) and one broken item (fails with a clear
error). The broken item is the good item's dict with `datetime` removed
and no start/end datetime supplied, which the STAC spec requires.

## Prerequisites

- pystac 1.15.2 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- Python 3.12.10; invoke the venv Python by its full path, never
  Node-1's bare `python`

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe validate_items.py
```

## Expected output

- `OK: valid item passes validation.`
- `OK: broken item fails validation: STACValidationError: ...` naming
  the missing datetime requirement.

## Failure behavior

- If the broken item unexpectedly passes, the script exits non-zero
  with `FAIL` — the validation call is not doing what this pattern
  claims; do not ship the pattern until the failure case is reproduced.
- Schema-fetch errors on first run (no network to the schema URLs):
  pystac validation resolves STAC JSON Schemas; on an offline host the
  first run may fail at schema retrieval rather than at item content.
  That outcome is a validation-environment note, not a pass — confirm
  schema availability at gate-3 validation on Node-1.

## Versions and evidence

- pystac 1.15.2 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same pystac 1.15.2 — not a fleet run):
  the pass/fail pair behaves as above; exact exception text is
  recorded at gate-3 validation.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this script on
Node-1's wave11-venv and confirms both outcomes plus the exact
exception class and message.
