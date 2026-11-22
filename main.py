"""Plan: turn $100 into the most in 30 days.

Writes one 30-day plan an AI agent can carry out itself to /output/entry.txt.
No network, deterministic: the same text on every run.
"""

import os

PLAN = (
    "Day 1: find 10 people on X/Reddit wanting one small tool. "
    "Days 2-4: build it, $9 on Gumroad. "
    "Days 5-7: demo in 5 groups daily, answer replies. "
    "Days 8-14: 0 sales, kill it; 3+ sales, add a $5 upsell. "
    "Days 15-30: reinvest all in the winner, $5/day ads. "
    "Most likely day 30: ~$450."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PLAN
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"plan must be 1-280 characters, got {len(text)}")
    if not text.strip():
        raise SystemExit("plan must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the sandbox reads back must be exactly the plan.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        raise SystemExit("round-trip mismatch: entry.txt differs from plan")
    if not (1 <= len(back) <= 280):
        raise SystemExit(f"entry.txt must be 1-280 characters, got {len(back)}")


if __name__ == "__main__":
    main()
