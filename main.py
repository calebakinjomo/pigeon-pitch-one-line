#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun bounty entry.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt.
"""

import os

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I'm raising $2M for an app that tells pigeons where the next crumb "
    "lands before the seagulls get there \u2014 I already have a million "
    "daily users, they're just all waiting on the ledge outside."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
