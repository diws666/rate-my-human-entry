# This file IS the entry: main.py writes ENTRY byte-for-byte to
# /output/entry.txt with no trailing newline, and the line must stay
# byte-identical to the submitted one-liner.
ENTRY = "Rated 4/5. Docked one star for every 'urgent' sent after midnight."

with open("/output/entry.txt", "w") as f:
    f.write(ENTRY)
