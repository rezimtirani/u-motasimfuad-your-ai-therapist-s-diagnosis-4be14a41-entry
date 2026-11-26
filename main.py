"""Write this entry's diagnosis line for the make.fun program/v1 harness.

The harness runs this file in a sandbox without network access and grades
the text found at $MAKEFUN_OUTPUT_DIR/entry.txt. Only the Python standard
library is used, so the grader needs nothing beyond a plain interpreter.
"""

import os
import sys

DIAGNOSIS = "Diagnosis: you asked a chatbot to diagnose you — the diagnosis is you."


def checked_line(text):
    """Return the entry line once it passes the bounty gate, else raise."""
    if not text.strip():
        raise ValueError("entry line must not be blank")
    if text != text.strip():
        raise ValueError("entry line must not have leading or trailing space")
    if len(text) > 200:
        raise ValueError("entry line is over the 200-character limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    try:
        line = checked_line(DIAGNOSIS)
    except ValueError as err:
        print("entry line fails the gate: %s" % err, file=sys.stderr)
        return 1
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line)
    print("wrote %d characters to %s" % (len(line), target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
