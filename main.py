#!/usr/bin/env python3
"""Weirdest Job Title entry: writes a single job title (<=60 chars) to /output/entry.txt."""
import os

TITLE = "Professional Mourner for Strangers' Goldfish"

def main() -> None:
    assert 1 <= len(TITLE) <= 60, f"title length {len(TITLE)} out of range"
    assert TITLE.strip(), "title must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
