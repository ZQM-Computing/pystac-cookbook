"""Build a small self-contained STAC catalog: 1 collection, 2 items.

Synthetic geometries only (a 0.02-degree square near the origin — not a
real place of interest). Asset hrefs are relative placeholders; this
pattern never reads asset data, so no raster files are needed.

Run with the fleet venv Python, never Node-1's bare `python`:
    C:/geo-tools/wave11-venv/Scripts/python.exe build_catalog.py
"""

import json
from datetime import datetime, timezone

import pystac
from pystac import Catalog, Collection, Extent, Item, SpatialExtent, TemporalExtent

OUT_DIR = "demo-catalog"


def square(lon0, lat0, size=0.02):
    return {
        "type": "Polygon",
        "coordinates": [[
            [lon0, lat0],
            [lon0 + size, lat0],
            [lon0 + size, lat0 + size],
            [lon0, lat0 + size],
            [lon0, lat0],
        ]],
    }


def main():
    extent = Extent(
        SpatialExtent([[0.0, 0.0, 0.04, 0.02]]),
        TemporalExtent([[datetime(2026, 1, 1, tzinfo=timezone.utc), None]]),
    )
    collection = Collection(
        id="demo-collection",
        description="Synthetic demo collection (two scenes, no real data).",
        extent=extent,
        license="proprietary",
    )
    catalog = Catalog(id="demo-catalog", description="Synthetic demo catalog.")
    catalog.add_child(collection)

    for i, lon0 in enumerate((0.0, 0.02), start=1):
        geom = square(lon0, 0.0)
        item = Item(
            id=f"scene-{i:02d}",
            geometry=geom,
            bbox=[lon0, 0.0, lon0 + 0.02, 0.02],
            datetime=datetime(2026, 1, 15, tzinfo=timezone.utc),
            properties={"demo:scene": i},
        )
        item.add_asset("data", pystac.Asset(href=f"data/scene-{i:02d}.tif"))
        collection.add_item(item)

    catalog.normalize_hrefs(OUT_DIR)
    catalog.save(catalog_type=pystac.CatalogType.SELF_CONTAINED)
    print(f"Wrote {OUT_DIR}/catalog.json with 1 collection and 2 items.")


if __name__ == "__main__":
    main()
