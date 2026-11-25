#!/usr/bin/env python3
"""THE WEDNESDAY LEDGER - entry program for make.fun news-image-20261125.

The artwork (one broadsheet image summing up Wednesday 25 November 2026)
is rendered locally by draw.py and committed to this repository as
entry.png. This program's single job is to deliver those exact bytes to
/output/entry.png, byte for byte, every run.

Python 3.13, standard library only.
"""
import hashlib
import os
import shutil
import sys

ENTRY_NAME = "entry.png"
OUTPUT_DIR = "/output"


def entry_source():
    """Absolute path of the committed artwork beside this file."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), ENTRY_NAME)


def main():
    src = entry_source()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    dst = os.path.join(OUTPUT_DIR, ENTRY_NAME)
    shutil.copyfile(src, dst)
    with open(dst, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
