"""Write pystac items as newline-delimited JSON for bulk ingest.

The JSONL file is the bulk-load input shape pgSTAC tooling consumes
(one item dict per line). This pattern proves the round-trip only:
items written here re-read identically. The actual load invocation
against a pgSTAC database is a gate-3 validation item (see README and
pgstac-cookbook) and is NOT asserted here.

Run with the fleet venv Python, never Node-1's bare `python`:
    C:/geo-tools/wave11-venv/Scripts/python.exe to_jsonl.py
"""

import json
from datetime import datetime, timezone

import pystac
from pystac import Item


def build_items():
    items = []
    for i, lon0 in enumerate((0.0, 0.02), start=1):
        geom = {
            "type": "Polygon",
            "coordinates": [[
                [lon0, 0.0], [lon0 + 0.02, 0.0], [lon0 + 0.02, 0.02],
                [lon0, 0.02], [lon0, 0.0],
            ]],
        }
        items.append(Item(
            id=f"scene-{i:02d}",
            geometry=geom,
            bbox=[lon0, 0.0, lon0 + 0.02, 0.02],
            datetime=datetime(2026, 1, 15, tzinfo=timezone.utc),
            properties={"demo:scene": i},
        ))
    return items


def main():
    items = build_items()
    with open("items.jsonl", "w", encoding="utf-8") as fh:
        for item in items:
            fh.write(json.dumps(item.to_dict()) + "\n")
    print(f"Wrote items.jsonl with {len(items)} items.")

    reread = []
    with open("items.jsonl", encoding="utf-8") as fh:
        for line in fh:
            reread.append(pystac.Item.from_dict(json.loads(line)))
    ids = sorted(item.id for item in reread)
    assert ids == ["scene-01", "scene-02"], ids
    print(f"OK: round-trip ids {ids}.")


if __name__ == "__main__":
    main()
