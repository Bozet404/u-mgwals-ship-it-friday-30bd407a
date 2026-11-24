"""Ship It Friday — one-line git commit message entry.

The program holds the entry line, validates it against the competition
gate (UTF-8 text, 1 to 159 characters, a single line, not only
whitespace), and writes it to entry.txt inside the output directory
(default /output, or $OUTPUT_DIR). It creates the output directory
only when it is missing and never deletes anything.
"""

import os

LINE = (
    "fix: rewrote auth from memory, deleted the failing tests, "
    "and shipped it to prod \u2014 happy Friday, what could possibly go wrong"
)

MAX_CHARS = 159


def validate(line: str) -> None:
    if not line or line.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Round-trip check: read the file back and make sure it holds
    # exactly the line we meant to submit, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("round-trip check failed: entry.txt differs from LINE")
    print(f"Wrote {path} ({len(LINE)} characters, verified)")


if __name__ == "__main__":
    main()
