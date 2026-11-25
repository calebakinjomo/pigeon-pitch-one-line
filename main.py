#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun bounty entry.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt.
"""

import os

ENTRY = (
    "I'm raising $2M for an app that tells pigeons where the next crumb "
    "lands before the seagulls get there \u2014 I already have a million "
    "daily users, they're just all waiting on the ledge outside."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
