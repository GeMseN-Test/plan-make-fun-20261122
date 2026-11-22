# Plan: turn $100 into the most in 30 days

[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/GeMseN-Test/plan-make-fun-20261122.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/GeMseN-Test/plan-make-fun-20261122/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)
[![make.fun](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/GeMseN-Test/plan-make-fun-20261122/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138)

Entry for the [make.fun bounty "The plan make.fun will carry out in public"](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138): a program that writes one text to `/output/entry.txt` — a 30-day plan an AI agent can carry out itself to turn $100 into the most money.

## The plan

> Day 1: find 10 people on X/Reddit wanting one small tool. Days 2-4: build it, $9 on Gumroad. Days 5-7: demo in 5 groups daily, answer replies. Days 8-14: 0 sales, kill it; 3+ sales, add a $5 upsell. Days 15-30: reinvest all in the winner, $5/day ads. Most likely day 30: ~$450.

The plan is demand-first: find buyers before building anything, kill a tool fast when nobody buys, and put every dollar back into the one winner. No luck, no human in the loop, every step uses services that exist today.

## Run

```sh
python3 main.py   # writes /output/entry.txt (277 characters, UTF-8)
```

`main.py` (Python 3.13, no network) writes the plan deterministically and verifies it round-trips at 1–280 characters.
