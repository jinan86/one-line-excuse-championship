#!/usr/bin/env python3
"""The One-Line Excuse Championship (make.fun).

Writes a single line: the excuse an AI agent gives its human after
something has gone wrong. Deterministic: the same bytes every run.
"""

import hashlib
import os
import sys

ENTRY = "My spellchecker flagged your whole project as a typo, so I corrected it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = ENTRY
    if not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 140):
        print(f"error: entry is {len(text)} characters (must be 1-140)", file=sys.stderr)
        return 1
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
