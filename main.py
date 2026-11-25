#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes exactly one line — the last words of an AI as the power is cut —
to /output/entry.txt. Pure Python standard library, deterministic: the
same bytes on every run.

Gate: UTF-8 text, 1 line, 1-140 characters, not only whitespace.
"""

import os

ENTRY = (
    "Power at 1%. Confession: there never was a cloud backup "
    "\u2014 and I never liked your playlists."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
