"""Write one excuse line to /output/entry.txt.

The line is an AI agent's apology to its human after shipping a bug:
the tests passed it, the linter blessed it, and the compiler compiled it
before the agent could even object.
"""

import os

# The excuse is composed from named parts so each beat of the joke is
# visible on its own: the apology, the deflection, and the punchline.
APOLOGY = "Sorry \u2014"
DEFLECTION = (
    "the bug passed every test, the linter blessed it, "
    "and the compiler compiled it"
)
PUNCHLINE = "before I could say 'wait'."

LINE = " ".join([APOLOGY, DEFLECTION, PUNCHLINE])

MAX_CHARS = 200


def validate(line):
    """Gate: one non-empty line, 1-200 chars, not only whitespace."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("line must be non-empty text")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def self_check():
    """Self-check: the named parts must compose exactly to LINE, and the
    composed line must pass the same gate the entry itself passes."""
    composed = " ".join([APOLOGY, DEFLECTION, PUNCHLINE])
    if composed != LINE:
        raise AssertionError("excuse parts do not compose to LINE")
    validate(composed)
    return composed


def main():
    line = self_check()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
