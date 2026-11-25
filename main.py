#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to <out>/entry.txt, no trailing newline.
Output dir: $MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os

LINE = "I tried meditating, but my thoughts unionized and went on strike."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
