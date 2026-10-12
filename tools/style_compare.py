#!/usr/bin/env python3
"""Compare writing style of two text files using function-word frequencies.

Usage: python3 style_compare.py a.txt b.txt
Result is a similarity hint (0-1), NOT proof of common authorship.
"""
import math
import re
import sys
from collections import Counter

# small PT-BR + EN function-word list
FUNC = """the of and to in a is that it for as with was on be by at this have from or
an but not are we you they his her their which can will if so no do just
de a o que e do da em um para com não uma os no se na por mais as dos como mas
foi ao ele das tem à seu sua ou ser quando muito há nos já está eu também só pelo""".split()


def profile(path):
    words = re.findall(r"\w+", open(path, encoding="utf-8").read().lower())
    c = Counter(w for w in words if w in FUNC)
    n = max(len(words), 1)
    return [c[w] / n for w in FUNC]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na, nb = math.sqrt(sum(x * x for x in a)), math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


if __name__ == "__main__":
    print(f"similarity: {cosine(profile(sys.argv[1]), profile(sys.argv[2])):.3f}")
