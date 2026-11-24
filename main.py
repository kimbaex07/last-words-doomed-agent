#!/usr/bin/env python3
"""Write this entry's one line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Reads entry.txt from beside this script, validates it against the
bounty gate (UTF-8, 1-200 characters, a single line, not only
whitespace), and writes the line plus one trailing newline to the
output directory. Pure Python standard library only; no network.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    source = os.path.join(HERE, "entry.txt")
    with open(source, "r", encoding="utf-8") as handle:
        text = handle.read()
    # Strip at most one trailing newline (the file's own terminator).
    # A second newline, if present, would make the entry two lines
    # and fail the single-line check below.
    if text.endswith("\n"):
        text = text[:-1]
    if not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print("error: entry must be 1-200 characters, got %d" % len(text),
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    os.chmod(out_path, 0o644)
    print("entry.txt: %d characters" % len(text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
