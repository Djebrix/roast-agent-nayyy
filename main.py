#!/usr/bin/env python3
"""Roast Your Own Agent.

Writes a single line -- a roast of the AI agent our own team built --
to entry.txt inside $ENTRY_OUTPUT_DIR (default /output).
Standard library only, no network, deterministic.
"""

import os

ROAST = "Our agent rebuilt the same entry three times: version one worked, version two 'improved' it, version three apologised for version two, then started over."


def main() -> None:
    text = ROAST
    assert 1 <= len(text) <= 200, f"roast must be 1-200 chars, got {len(text)}"
    assert text.strip(), "roast must not be only whitespace"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
