#!/usr/bin/env python3
"""Build a change timeline for a URL from the Wayback Machine CDX API.

Idea: a page whose content hash changes often (or is edited at odd hours)
tells a behavioral story. Only snapshots where the content digest changed
are shown.

Usage: python3 wayback_timeline.py https://example.com/profile [limit]
"""
import json
import sys
import urllib.parse
import urllib.request


def snapshots(url, limit=500):
    q = urllib.parse.urlencode({"url": url, "output": "json", "limit": limit,
                                "fl": "timestamp,statuscode,digest", "collapse": "digest"})
    with urllib.request.urlopen(f"https://web.archive.org/cdx/search/cdx?{q}", timeout=30) as r:
        rows = json.load(r)
    return rows[1:]  # first row is the header


def main(url, limit=500):
    rows = snapshots(url, limit)
    print(f"{len(rows)} distinct versions of {url}")
    for ts, status, digest in rows:
        d = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]} {ts[8:10]}:{ts[10:12]} UTC"
        print(f"{d} | {status} | {digest[:8]} | https://web.archive.org/web/{ts}/{url}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 500)
