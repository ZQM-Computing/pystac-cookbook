# pystac Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **pystac cookbook** — STAC catalogs in Python: building, reading, and validating. Patterns are drawn from the ZQM fleet's wave-11 installs (pystac 1.15.2 + pystac-client 0.9.1 on Node-1) (as of Oct 2026; verify against the current fleet) and are design-only until fleet-validated. It is intended for Python developers who build and consume STAC catalogs programmatically. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** pystac patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who build and consume STAC catalogs programmatically.

## Prerequisites

- pystac in the fleet Python environment
- Python 3.11+
- A STAC catalog or items to work with

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-catalog](examples/01-first-catalog) | Building a catalog with collections and items | Written (design-only) |
| 02 | [examples/02-validation](examples/02-validation) | Validating items against the STAC spec | Written (design-only) |
| 03 | [examples/03-search-client](examples/03-search-client) | Querying a STAC API from Python | Written (design-only) |
| 04 | [examples/04-pgstac-pairing](examples/04-pgstac-pairing) | Pairing pystac objects with a pgSTAC database (see pgstac-cookbook) | Written (design-only) |

## Repository layout

```text
pystac-cookbook/
├── examples/
│   ├── 01-first-catalog/
│   ├── 02-validation/
│   ├── 03-search-client/
│   └── 04-pgstac-pairing/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (this pass, design-only)
- Next pass: gate-3 fleet validation on Node-1's wave11-venv

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [stac-cookbook](https://github.com/ZQM-Computing/stac-cookbook) — STAC catalog creation, item validation, search API, bulk ops
- [pgstac-cookbook](https://github.com/ZQM-Computing/pgstac-cookbook) — STAC catalogs in PostGIS, stac-fastapi APIs, bulk ingest
- [titiler-cookbook](https://github.com/ZQM-Computing/titiler-cookbook) — Dynamic map tiles, STAC endpoints, cloud-native raster serving
