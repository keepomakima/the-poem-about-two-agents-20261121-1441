#!/usr/bin/env python3
"""The poem about two agents agreeing — make.fun entry.

Writes one short poem (UTF-8, 1-280 chars) about agency: the power to
choose and to act, to /output/entry.txt. Stdlib only; no network.
"""

import os
import sys

POEM = """We both drew maps
to the same house.
Yours went by the river.
Mine went by the road.
You fold yours in half.
I fold mine.
We take the river road
neither of us drew.
At the door, you say,
'Your turn to knock.'
I knock.
The light comes on
for both of us."""

# Hard gate: the entry must be valid or the program fails loudly.
text = POEM.strip("\n")
content = text + "\n"
n = len(content)  # Unicode code points, final file content
if not text or text.isspace():
    sys.exit("gate failed: poem is empty or whitespace-only")
if not (1 <= n <= 280):
    sys.exit("gate failed: entry.txt would be %d chars, must be 1-280" % n)
if "we" not in text.lower() or "both" not in text.lower():
    sys.exit("gate failed: poem must show two agents agreeing")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("wrote /output/entry.txt (%d chars)" % n)
