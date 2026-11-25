"""One funny line for the make.fun bounty "One Line, One Laugh".

The whole entry is a single self-contained joke: a smart fridge files for
divorce after catching its owner cheating with the takeaway menu at 2 a.m.
Nothing else is needed here -- the script validates the line and drops it
into /output/entry.txt.
"""

from pathlib import Path

# The line itself: one joke, exactly 90 characters.
LINE = (
    "My smart fridge filed for divorce \u2014 it caught me cheating "
    "with the takeaway menu at 2 a.m."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> str:
    """Strip and sanity-check the line; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"line must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("line must not contain control characters")
    if "  " in text:
        raise ValueError("line must not contain double spaces")
    if not text.endswith("."):
        raise ValueError("line must end with a full stop")
    return text


def main() -> None:
    text = validate(LINE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
