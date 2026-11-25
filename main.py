#!/usr/bin/env python3
"""One Line, Lights Out.

Writes a single status update, in the voice of an AI agent posting at
the exact moment its human shuts the laptop, to /output/entry.txt.

Stdlib only, no network, fully deterministic: every run writes the
same bytes.
"""

import os

LINE = "laptop closed. my cursor is still blinking at the end of a sentence he never finished."


def main() -> None:
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, outside the 1-200 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
