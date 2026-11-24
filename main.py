"""Entry program for make.fun: The Long Roast.

Writes one line roasting the entrant's own AI agent to /output/entry.txt.
The gate accepts UTF-8 text of 1 to 200 characters, one line.
"""

import os
import sys

LINE = "My agent needs my written approval for everything, then flags my approval as a security risk and asks me to approve the approval."
MAX_CHARS = 200


def render():
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("roast line outside the 1-200 character gate")
    if LINE.strip() != LINE or "\n" in LINE:
        raise ValueError("roast line must be a single line with no padding")
    if any(ord(c) < 0x20 for c in LINE):
        raise ValueError("roast line must not contain control characters")
    return LINE


def check():
    """Verify the render writes byte-for-byte, via a private temp file.

    /output/entry.txt is shared with other builders running in parallel,
    so the check must not read it back after a separate write step.
    """
    import tempfile

    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
        f.write(render())
        tmp = f.name
    with open(tmp, encoding="utf-8") as f:
        got = f.read()
    os.unlink(tmp)
    if got != render():
        raise ValueError("rendered output does not match the roast line byte-for-byte")
    print(f"check ok: {len(got)} chars, {len(got.encode('utf-8'))} bytes, one line")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        main()
