#!/usr/bin/env python3
"""Check every http(s) link in README.md. Usage: python3 check_links.py [README.md]"""
import re
import sys
import urllib.request

path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
urls = sorted(set(re.findall(r"\]\((https?://[^)\s]+)\)", open(path, encoding="utf-8").read())))
bad = 0
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        code = urllib.request.urlopen(req, timeout=15).status
    except Exception as e:
        code = getattr(e, "code", str(e))
    ok = code == 200
    bad += not ok
    print(("OK  " if ok else "FAIL"), code, u)
sys.exit(1 if bad else 0)
