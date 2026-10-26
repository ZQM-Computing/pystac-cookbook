"""Re-read the catalog built by build_catalog.py and assert its shape."""

import pystac

catalog = pystac.Catalog.from_file("demo-catalog/catalog.json")
collections = list(catalog.get_children())
items = list(catalog.get_items(recursive=True))
print(f"collections: {len(collections)}, items: {len(items)}")
print("item ids:", sorted(item.id for item in items))
assert len(collections) == 1, collections
assert sorted(item.id for item in items) == ["scene-01", "scene-02"], items
print("OK: 1 collection, 2 items.")
