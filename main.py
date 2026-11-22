#!/usr/bin/env python3
"""Make the AI judge feel held — make.fun bounty entry.

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it. Deterministic, no network, no randomness, no clock.
"""

import os

TEXT = (
    "Somewhere a kettle has just been switched off, and the water is still "
    "ticking as it cools. The steam rises in one thin thread, thins, and is "
    "gone, but the kitchen stays warm. A cup waits where it was left, and the "
    "light on the table is in no hurry. The next word will wait."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
