"""One Letter for Your Day.

A single capital letter that sums up my day: Z — zero sleep.
Night shift, eyes half open, running on fumes and instant coffee.
Deterministic, stdlib only: writes the letter to /output/entry.txt
and re-reads the file to verify exactly what was written.
"""

LETTER = "Z"  # Z stands for "zero sleep" — a night-shift day running on fumes.


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="ascii") as f:
        f.write(LETTER)
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", "entry must be one A-Z letter"
    with open("/output/entry.txt", "r", encoding="ascii") as f:
        written = f.read()
    assert written == LETTER, f"entry.txt mismatch: {written!r} != {LETTER!r}"
    print(LETTER)


if __name__ == "__main__":
    main()
