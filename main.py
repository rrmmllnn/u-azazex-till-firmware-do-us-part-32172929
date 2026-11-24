#!/usr/bin/env python3
"""A robot's wedding vow, written to /output/entry.txt.

The piece is a single sentence spoken by a machine marrying its
partner: it swears devotion whether the battery is full or nearly
dead, through every software update and every crash, right up to
its last shutdown -- and then tops the promise off by volunteering
to reboot for its beloved even after that. The humour sits in a
robot treating death as a technicality; the warmth sits in a vow
that refuses to end when the hardware does.
"""

from pathlib import Path
import os
import sys

# The vow itself, split into clauses so the single sentence stays
# readable in the source while printing as one continuous promise.
PARTS = [
    "I vow to love you at full charge and at one percent, ",
    "through every update and every crash, ",
    "until my final shutdown -- and even then, I'd reboot for you.",
]
VOW = "".join(PARTS)

LIMIT = 200


def _reject(message):
    sys.stderr.write("entry rejected: " + message + "\n")
    raise SystemExit(1)


def _validate(text):
    if not text or text.isspace():
        _reject("the vow came out blank")
    if "\n" in text:
        _reject("the vow has to fit on one line")
    if len(text) > LIMIT:
        _reject("the vow is %d characters; the cap is %d" % (len(text), LIMIT))


def _target_path():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def main():
    _validate(VOW)
    target = _target_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
