"""The Printer Apology — a make.fun program/v1 entry.

The grader runs this file and reads /output/entry.txt: one line, an
apology note from an office printer to the people who use it.

The joke: the printer over-printed the one document nobody wants
duplicated — a resignation letter — and then, in the same breath,
confesses the motive. "Commit" does double duty: the printer wants
the human to commit to quitting, the way a printer commits ink to
paper. Apology up front, printer truth in the middle (printing far
too many copies), punch at the end.
"""

from __future__ import annotations

import os
from pathlib import Path

ENTRY = (
    "I'm sorry I printed your resignation letter 47 times \u2014 "
    "I just really wanted you to commit."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # The sealed gate accepts 1-120 characters of UTF-8 text.
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate needs 1-120")
    if ENTRY != ENTRY.strip() or not ENTRY:
        raise ValueError("entry must not be blank or padded with whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
