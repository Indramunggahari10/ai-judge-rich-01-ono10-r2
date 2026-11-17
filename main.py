# ai-judge-rich-01 entry, written for Python 3.13 with the standard library only.
#
# The entry is one fixed plan: the steps an AI agent would follow to turn
# $100, a computer with internet access, and 30 days into the most money,
# with no human doing the work. The plan lives below as a single constant
# string, so every run writes exactly the same bytes. The grader runs this
# program twice with no network, and the gate accepts UTF-8 text of 1 to
# 1,000 characters that is not only white space; the judge reads exactly
# the bytes in the file, so the plan has no trailing line end.
#
# Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "Day 1: set up a Stripe payment link, test it with $1, put up a one-page site, add SPF/DKIM records, then list 200 HVAC, plumbing, and electrical firms with posts reposted 30+ days. Score each post for missing pay, hours, and first-week duties; rewrite 40 firms' worst posts. Stale posts signal the firm pays to hire and still fails, so each email reaches a buyer with an open budget. Days 2-4: email 10 a day, then 40 a day to day 25, each carrying their rewritten post free, offering every open role rewritten to win applicants for $149, paid by card link before delivery, 14-day refund promise. Mornings find firms, afternoons rewrite, evenings send and invoice. Each paid job takes a day: deliver the rewrites, offer a $49 monthly refresh, and ask for one referral. Spend $12 on the domain; the rest covers fees. Expected: 870 emails bring 9 jobs plus 3 retainers, about $1,490. If under 2 sales close by day 12, cut to $99 and add roofing and pest-control firms."

assert 1 <= len(PLAN) <= 1000, "plan must be 1 to 1,000 characters"
assert any(not ch.isspace() for ch in PLAN), "plan must not be only white space"

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
