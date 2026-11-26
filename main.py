"""Write one excuse line to /output/entry.txt.

The line is an AI agent's apology to its human after shipping a bug:
the tests passed it, the linter blessed it, and the compiler compiled it
before the agent could even object.
"""

import os

LINE = "Sorry \u2014 the bug passed every test, the linter blessed it, and the compiler compiled it before I could say 'wait'."

MAX_CHARS = 200


def validate(line):
    """Gate: one non-empty line, 1-200 chars, not only whitespace."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("line must be non-empty text")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
