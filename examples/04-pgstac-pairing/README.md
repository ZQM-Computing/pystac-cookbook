# 04 — pgSTAC pairing

Write pystac items as newline-delimited JSON — the bulk-load input
shape pgSTAC tooling consumes — and prove the round-trip: items written
here re-read with identical ids. This pattern deliberately stops before
the database: the load invocation against a pgSTAC database is a
gate-3 validation item, not something this pattern asserts.

## Prerequisites

- pystac 1.15.2 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- Python 3.12.10; invoke the venv Python by its full path, never
  Node-1's bare `python`
- pgstac-cookbook for the database side (PostGIS + pgSTAC)

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe to_jsonl.py
```

## Expected output

- `items.jsonl` with 2 lines (one item dict per line).
- `OK: round-trip ids ['scene-01', 'scene-02'].`

## Failure behavior

- Round-trip mismatch: the assertion names the ids found; re-check
  that the file was written by this script, not hand-edited.
- Database load errors are out of scope here: this pattern never
  opens a database connection. Load the produced `items.jsonl` with
  the pgSTAC tooling documented in pgstac-cookbook, and record the
  exact loader invocation at gate-3 validation — it is not asserted
  in this pattern because the fleet's pgSTAC loader spelling is a
  validation item, not fleet evidence in this batch.

## Versions and evidence

- pystac 1.15.2 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same pystac 1.15.2 — not a fleet run):
  write + round-trip pass with the outputs above.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this script on
Node-1's wave11-venv, then loads `items.jsonl` into a pgSTAC database
the validator controls and records the loader invocation.
