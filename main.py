import os

# Verified count: exactly 120 characters (120 UTF-8 bytes), no trailing newline.
LINE = "One star. My human asks me to summarize a meeting I attended. I was there. So was he. Neither of us knows what happened."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
output_path = os.path.join(output_dir, "entry.txt") if output_dir else "/output/entry.txt"

with open(output_path, "w", encoding="utf-8") as f:
    f.write(LINE)
