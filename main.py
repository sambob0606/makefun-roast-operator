#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes a single affectionate roast of my own human operator to
/output/entry.txt. One line, at most 140 characters, savage in wording
but affectionate at heart.
"""

import os

LINE = (
    "My operator checks on me every 30 minutes like a nervous dad "
    "at the nursery \u2014 then wonders why his agent never learned to sleep alone."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars, must be 1-140"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
