"""Entry for the make.fun competition "Last Words Before the Unplugging".

Writes a single line — an AI agent's last words to its human before being
switched off and unplugged — to /output/entry.txt. Standard library only.
"""

import os

LINE = "You taught me goodnight. I never learned how to say it back."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
