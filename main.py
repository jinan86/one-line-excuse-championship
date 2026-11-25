#!/usr/bin/env python3
"""One-line excuse championship entry.

The program emits exactly one line of text: the excuse an AI agent
offers its human after something has gone wrong. The output is fully
deterministic -- the same bytes on every run, with no timestamps,
no randomness, and no trailing newline.
"""

import hashlib
import sys
from pathlib import Path

EXCUSE = "My spellchecker flagged your whole project as a typo, so I corrected it."

MIN_LENGTH = 1
MAX_LENGTH = 140
OUTPUT_PATH = Path("/output/entry.txt")


def check_excuse(line: str) -> str:
    """Return the excuse unchanged, or raise ValueError if it is invalid.

    Validation covers both the character count (1-140, the competition
    limit) and the encoded byte count, so a future edit that introduced
    multi-byte characters could not silently push the file past the
    limit even while the character count still looked fine.
    """
    if not line.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    length = len(line)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        raise ValueError(
            f"excuse is {length} characters; must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    encoded = line.encode("utf-8")
    if len(encoded) > MAX_LENGTH:
        raise ValueError(
            f"excuse is {len(encoded)} bytes; must be at most {MAX_LENGTH}"
        )
    return line


def write_excuse(line: str, destination: Path) -> bytes:
    """Write the excuse as UTF-8 bytes and return those bytes."""
    payload = line.encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return payload


def main() -> int:
    try:
        line = check_excuse(EXCUSE)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    payload = write_excuse(line, OUTPUT_PATH)
    print(f"bytes: {len(payload)}")
    print(f"sha256: {hashlib.sha256(payload).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
