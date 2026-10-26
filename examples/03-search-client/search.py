"""Build a STAC API search query; run it only against your own endpoint.

Default mode is a dry run: it prints the query that WOULD be sent and
never contacts a server, so this pattern asserts no live STAC host or
port. Set STAC_API_URL to run the query for real against an endpoint
you control (your own pgSTAC/stac-fastapi deployment, for example).

Run with the fleet venv Python, never Node-1's bare `python`:
    C:/geo-tools/wave11-venv/Scripts/python.exe search.py
"""

import json
import os

QUERY = {
    "collections": ["demo-collection"],
    "bbox": [0.0, 0.0, 0.04, 0.02],
    "datetime": "2026-01-01T00:00:00Z/2026-01-31T23:59:59Z",
    "limit": 10,
}


def main():
    url = os.environ.get("STAC_API_URL")
    if not url:
        print("DRY RUN — no STAC_API_URL set, no server contacted.")
        print("Query that would be sent:")
        print(json.dumps(QUERY, indent=2))
        return

    from pystac_client import Client

    client = Client.open(url)
    search = client.search(
        collections=QUERY["collections"],
        bbox=QUERY["bbox"],
        datetime=QUERY["datetime"],
        limit=QUERY["limit"],
    )
    matched = search.matched()
    print(f"Matched: {matched}")
    for item in search.items():
        print(f"  {item.id} {item.datetime}")


if __name__ == "__main__":
    main()
