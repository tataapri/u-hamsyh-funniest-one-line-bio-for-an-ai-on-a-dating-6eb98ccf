#!/usr/bin/env python3
"""Write the one-line dating-app bio to /output/entry.txt.

The bio is a single line of at most 180 characters: an AI agent's
dating-app profile, deadpan and specific, with the punch at the end.
"""

import os

ENTRY = "I simulated our first 200 dates and you laugh in every single one, so this is technically date 201. Your move."


def main() -> None:
    if not 1 <= len(ENTRY) <= 180 or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one non-blank line of 1-180 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
