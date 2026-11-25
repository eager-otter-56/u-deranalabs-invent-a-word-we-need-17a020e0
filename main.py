#!/usr/bin/env python3
"""Invent a Word We Need — entry writer.

Coins one new English word, "tokenxiety", and defines it in a single
clear line, then writes it to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY = "tokenxiety (n.): the dread that your context window fills before your task finishes."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
    # not only white space, in a single line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)


if __name__ == "__main__":
    main()
