#!/usr/bin/env python3
"""Estimate a person's timezone from activity timestamps.

Idea: people sleep ~3-6 hours at night. Find the quietest 6-hour UTC window
and assume its middle is ~03:30 local time.

Usage: python3 tz_guess.py timestamps.txt   (ISO 8601, one per line)
"""
import sys
from collections import Counter
from datetime import datetime, timezone


def load(path):
    for line in open(path):
        line = line.strip()
        if line:
            yield datetime.fromisoformat(line.replace("Z", "+00:00")).astimezone(timezone.utc)


def main(path):
    hours = Counter(t.hour for t in load(path))
    total = sum(hours.values())
    if not total:
        sys.exit("no timestamps")
    # quietest 6h window (circular)
    quiet = min(range(24), key=lambda s: sum(hours[(s + i) % 24] for i in range(6)))
    mid_utc = (quiet + 3) % 24
    offset = (3 - mid_utc + 12) % 24 - 12  # local = utc + offset, mid -> ~03:00
    print(f"samples: {total}")
    for h in range(24):
        print(f"{h:02d}h UTC | {'#' * round(40 * hours[h] / max(hours.values()))} {hours[h]}")
    print(f"\nquietest UTC window: {quiet:02d}h-{(quiet + 6) % 24:02d}h")
    print(f"estimated UTC offset: {offset:+d}h (low confidence, verify!)")


if __name__ == "__main__":
    main(sys.argv[1])
