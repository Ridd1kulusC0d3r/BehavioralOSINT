#!/usr/bin/env python3
"""Activity-hour profile of a public GitHub user (from public events API).

Shows events per UTC hour and a rough timezone guess (see tz_guess.py).
Public events only (last ~90 days / 300 events). Probability, not proof.

Usage: python3 gh_activity.py <username>    (set GITHUB_TOKEN to avoid rate limits)
"""
import json
import os
import sys
import urllib.request
from collections import Counter


def events(user):
    out = []
    for page in (1, 2, 3):
        req = urllib.request.Request(
            f"https://api.github.com/users/{user}/events/public?per_page=100&page={page}",
            headers={"User-Agent": "behavioralosint"})
        if os.environ.get("GITHUB_TOKEN"):
            req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
        with urllib.request.urlopen(req, timeout=30) as r:
            batch = json.load(r)
        out += batch
        if len(batch) < 100:
            break
    return out


def profile(evs):
    """Return (hours Counter, weekdays Counter, quietest-window start hour)."""
    hours = Counter(int(e["created_at"][11:13]) for e in evs)
    days = Counter(__import__("datetime").datetime.fromisoformat(e["created_at"][:10]).strftime("%a") for e in evs)
    quiet = min(range(24), key=lambda s: sum(hours[(s + i) % 24] for i in range(6)))
    return hours, days, quiet


if __name__ == "__main__":
    evs = events(sys.argv[1])
    if not evs:
        sys.exit("no public events")
    hours, days, quiet = profile(evs)
    top = max(hours.values())
    for h in range(24):
        print(f"{h:02d}h UTC | {'#' * round(30 * hours[h] / top)} {hours[h]}")
    print("weekdays:", dict(days))
    mid = (quiet + 3) % 24
    offset = (3 - mid + 12) % 24 - 12
    print(f"quietest UTC window: {quiet:02d}h-{(quiet + 6) % 24:02d}h -> offset ~{offset:+d}h (low confidence)")
