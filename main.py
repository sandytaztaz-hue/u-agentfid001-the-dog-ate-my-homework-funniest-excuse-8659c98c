"""The Dog Ate My Homework: Funniest Excuse — make.fun bounty entry.

A single line, in the dog's voice, explaining why the homework got eaten.
The program writes exactly that line to /output/entry.txt and nothing else.
"""

import os

ENTRY = "I graded your homework. It failed every question, so I ate the evidence before your teacher could."

os.makedirs("/output", exist_ok=True)
# Write exactly the entry text: no title, no extra words, no trailing newline.
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
