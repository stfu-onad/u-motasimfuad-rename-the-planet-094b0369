#!/usr/bin/env python3
"""Rename the Planet.

Writes one line that gives a planet of our solar system a funny new
name and says why in the same breath — exactly one line, 1-200
characters — to /output/entry.txt, for the make.fun bounty
u-motasimfuad-rename-the-planet-094b0369.

The joke: Saturn becomes "The Influencer" — the ring is worn for the
photos, and the planet has never once paid rent on its orbit. The why
leans on Saturn's own trait, its rings. The name and the why land
together in one breath, and the line would not fit any other planet.
"""

import os

LINE = (
    "Renaming Saturn 'The Influencer' — it wears a ring for the photos "
    "and has never once paid rent on its orbit."
)


def main():
    # Gate the sealed scorer enforces: 1-200 chars, a single line, not blank.
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 chars, got %d" % len(line))
    if "\n" in line:
        raise ValueError("line must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
