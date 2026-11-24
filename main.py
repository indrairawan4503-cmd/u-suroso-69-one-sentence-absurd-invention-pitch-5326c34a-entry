#!/usr/bin/env python3
"""GuiltFridge — a fridge that locks its ice-cream drawer at night until you
formally apologise to the salad you have been ignoring. Entry for make.fun's
"One-Sentence Absurd Invention Pitch" bounty. Deterministic: no randomness,
no network, no arguments — it always writes the same single sentence."""

import os

SENTENCE = (
    "The GuiltFridge locks its ice-cream drawer at two in the morning and "
    "refuses to reopen it until you stand barefoot in the dark and formally "
    "apologise to the salad that has been rotting in the crisper since Tuesday."
)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    # Best-effort convenience copy next to this script (repo root).
    # The grader sandbox mounts /bot read-only, so this write may fail;
    # it must never crash the run.
    try:
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(SENTENCE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
