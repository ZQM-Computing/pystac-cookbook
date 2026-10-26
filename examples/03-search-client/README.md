# 03 — Search client

Build a STAC API search query with pystac-client. The default mode is
a dry run that prints the query and contacts no server, so this pattern
asserts no live STAC host or port. A live run is gated on the
`STAC_API_URL` environment variable pointing at an endpoint you
control.

## Prerequisites

- pystac-client 0.9.1 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- Python 3.12.10; invoke the venv Python by its full path, never
  Node-1's bare `python`

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe search.py
```

For a live run against your own endpoint only:

```bash
set STAC_API_URL=https://your-stac-api.example/
C:/geo-tools/wave11-venv/Scripts/python.exe search.py
```

## Expected output

- Dry run: `DRY RUN — no STAC_API_URL set, no server contacted.` plus
  the query JSON (collections `demo-collection`, the synthetic bbox,
  the January 2026 datetime range, limit 10).
- Live run: `Matched: N` followed by one line per item (`id datetime`).
  `N` depends on your endpoint's data and is not asserted here.

## Failure behavior

- No `STAC_API_URL` set: dry run, exit 0 — this is the intended
  default, not an error.
- Unreachable or non-STAC URL: the client raises a connection or
  decode error; check the URL before assuming the query is wrong.
- Empty result on a live endpoint: `Matched: 0` — the query is valid
  but nothing matches; widen the bbox or datetime range.

## Versions and evidence

- pystac-client 0.9.1 (Node-1 wave11-venv, wave-11 Part A, 2026-10-25).
- Draft-time execution (VM, same pystac-client 0.9.1 — not a fleet
  run): dry-run output verified; no live endpoint was contacted.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs the dry run on
Node-1's wave11-venv, and the live run only against a fleet STAC API
the validator controls (see pgstac-cookbook / stac-fastapi notes).
