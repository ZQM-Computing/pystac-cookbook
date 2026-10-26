"""Validate a good item (passes) and a broken item (fails clearly).

The broken item is the good item's dict with `datetime` removed and no
start/end datetime supplied, which the STAC spec requires. Validation
uses pystac's bundled schema validation; on a host without network
access to the schema URLs, the first run may need the schemas cached —
see the README.
"""

from datetime import datetime, timezone

import pystac
from pystac import Item
from pystac.validation import validate, validate_dict


def good_item():
    return Item(
        id="scene-01",
        geometry={
            "type": "Polygon",
            "coordinates": [[[0.0, 0.0], [0.02, 0.0], [0.02, 0.02],
                              [0.0, 0.02], [0.0, 0.0]]],
        },
        bbox=[0.0, 0.0, 0.02, 0.02],
        datetime=datetime(2026, 1, 15, tzinfo=timezone.utc),
        properties={},
    )


def main():
    item = good_item()
    validate(item)
    print("OK: valid item passes validation.")

    broken = item.to_dict()
    del broken["properties"]["datetime"]
    try:
        validate_dict(broken)
    except Exception as exc:  # STACValidationError on pystac 1.15.2
        print(f"OK: broken item fails validation: {type(exc).__name__}: {exc}")
    else:
        raise SystemExit("FAIL: broken item unexpectedly passed validation.")


if __name__ == "__main__":
    main()
