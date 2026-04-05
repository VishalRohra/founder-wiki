---
title: The Equity Equation
type: framework
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["equity equation", "1/(1-n)", "equity formula", "stock trade test"]
related: ["[[Equity and Compensation]]", "[[Fundraising]]", "[[Paul Graham]]", "[[Hiring]]"]
sources: ["8u-the-equity-equation"]
speakers_referenced: ["Paul Graham"]
---

# The Equity Equation

A general formula introduced by [[Paul Graham]] for deciding whether any trade of company stock is worthwhile. The formula applies identically to investor deals, employee grants, and strategic partnerships. ([Original essay](http://www.paulgraham.com/equity.html))

## The Formula

**1/(1 - n)**

Where n is the fraction of the company you're giving up. The deal is a good one if it makes the company worth more than 1/(1-n) times its current value.

The logic: if you give up n% of your company, you need the remaining (100-n)% to be worth more than 100% was before. That happens when the company's total value increases by a factor of at least 1/(1-n).

## For Investment

**Example: 50% investor.** If an investor wants half your company, they must at least double your expected outcome. You'd have half of something worth more than twice as much.

**Example: YC at 7%.** 1/(1-0.07) = 1.075. YC needs to improve your prospects by more than 7.5%. Graham comments: "Does anyone really think we're so useless that in three months we can't improve a startup's prospects by 7.5%?"

**Example: Sequoia at 30%.** 1/(1-0.30) = 1.43. The deal is worth it if Sequoia improves your outcome by more than 43%. Graham argues this is "an extraordinary bargain" for the average startup because "it would improve the average startup's prospects by more than 43% just to be able to *say* they were funded by Sequoia, even if they never actually got the money." The reason Sequoia can maintain below-market pricing: "they limit their holdings to leave the founders enough stock to feel the company is still theirs." The catch: ~6,000 business plans per year, ~20 funded, odds of 1 in 300.

## For Employees

The formula works in reverse. If a new person improves the company's average outcome by a factor of i, they're worth n such that i = 1/(1-n). Solving: **n = (i-1)/i**.

**Example:** A hacker who'd increase average outcome by 20%. n = (1.2-1)/1.2 = 0.167. You'd break even giving 16.7%.

But stock is not the only cost. Graham's rule of thumb for converting salary + overhead to stock: multiply the annual rate by about 1.5. Reasoning: if the startup dies, you don't owe future salary; if it grows fast (3x/year), next year's salary comes from next year's (higher) valuation.

**Full calculation:** Suppose 50% desired profit margin on the hire. One-third off 16.7% = 11.1% retail price. At $60K/year salary + overhead, x1.5 = $90K stock-equivalent. If valuation is $2M, $90K = 4.5%. Offer: 11.1% - 4.5% = **6.6%** equity.

Graham notes: "how important it is for early employees to take little salary. It comes right out of stock that could otherwise be given to them."

## For Any Deal

The meta-principle: "whenever you make any decision involving equity, run it through 1/(1-n) to see if it makes sense. You should always feel richer after trading equity." If the trade didn't put you net ahead, you shouldn't have done it.

## Limitations

Graham is explicit that this is not a precise formula: "I'm not claiming that stock grants can now be reduced to a formula. Ultimately you always have to guess." There are always other factors -- investor reputation, employee morale, strategic considerations. But the formula provides a foundation for reasoning about what your gut feels or industry tables of typical grants are actually estimating.

## Present Valuation

For the "current value" baseline, Graham suggests using the post-money valuation of the last funding round, noting it probably undervalues the company because (a) time has passed and (b) early-round valuations reflect investor contributions beyond cash.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| 8u-the-equity-equation | Paul Graham | Complete derivation of the 1/(1-n) formula with investment and employee examples |
