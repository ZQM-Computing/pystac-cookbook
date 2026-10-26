# 01 — First catalog

Build a self-contained STAC catalog with one collection and two items,
then re-read it and assert the shape. All geometries are synthetic (a
0.02-degree square near the origin — not a real place of interest), and
asset hrefs are relative placeholders; no raster files are needed.

## Prerequisites

- pystac 1.15.2 (Node-1 wave11-venv, `C:/geo-tools/wave11-venv`)
- Python 3.12.10; invoke the venv Python by its full path, never
  Node-1's bare `python` (that resolves to the hermes venv)

## Run

```bash
C:/geo-tools/wave11-venv/Scripts/python.exe build_catalog.py
C:/geo-tools/wave11-venv/Scripts/python.exe check_catalog.py
```

## Expected output

- `demo-catalog/catalog.json` plus `demo-collection/` with two item files.
- `check_catalog.py` prints `collections: 1, items: 2` and
  `item ids: ['scene-01', 'scene-02']`, then `OK`.

## Failure behavior

- Missing pystac: `ModuleNotFoundError` — run from the wave11-venv
  Python, not the bare `python`.
- A changed item count or id breaks the assertions in
  `check_catalog.py` with a clear message; re-run `build_catalog.py`
  from a clean directory.

## Versions and evidence

- pystac 1.15.2, pystac-client 0.9.1 (Node-1 wave11-venv, wave-11 Part A,
  2026-10-25; Wally spot-checked venv versions).
- Draft-time execution (VM, same pystac 1.15.2 — not a fleet run):
  build + check pass with the outputs above.

## Validation boundary

Design-only, gate 1 target. Fleet validation runs this pair on Node-1's
wave11-venv and confirms the same outputs.
