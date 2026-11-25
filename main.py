#!/usr/bin/env python3
"""One-word entry: the username itself, nothing else.

Writes exactly `rifky-ardi` to /output/entry.txt — a single word,
no spaces, no trailing newline, no extra lines. The entry is checked
before writing: it must be one token of lowercase letters and a dash.
"""

import os
import re

WORD = "rifky-ardi"


def main():
    text = WORD.strip()
    if not re.fullmatch(r"[a-z]+-[a-z]+", text):
        raise SystemExit("entry must be exactly one hyphenated word")
    if len(text) != 10:
        raise SystemExit(f"entry length {len(text)} is not 10 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
