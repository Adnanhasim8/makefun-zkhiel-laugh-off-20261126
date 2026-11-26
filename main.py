#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

from pathlib import Path

ENTRY = "I hired a hitman to kill my procrastination \u2014 six months later, he's still putting it off."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Gate assertions: exactly one line, 1-200 characters, non-empty.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT.read_text(encoding="utf-8")
    assert written == ENTRY, "written output must match the entry exactly"


if __name__ == "__main__":
    main()
