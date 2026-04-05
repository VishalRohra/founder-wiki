---
title: Equity Equation
type: framework
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["1/(1-n)", "equity formula", "stock grants", "equity dilution", "trading equity"]
related: ["[[Paul Graham]]", "[[Financial Survival]]", "[[Early-Stage Mistakes]]"]
sources: ["8u-the-equity-equation"]
speakers_referenced: ["Paul Graham"]
---

# Equity Equation

The Equity Equation is a formula introduced by [[Paul Graham]] in July 2007 for deciding whether any trade of company stock -- for investment, an employee, or a deal -- is worth making [1]. The formula is:

**1/(1 - n)**

where n is the fraction of the company you are giving up. You should make the trade if what you receive improves your average outcome enough that the (100 - n)% you have left is worth more than the whole company was before [1].

## How the Formula Works

If an investor wants to buy half your company, the investment must more than double your average outcome for you to break even. You have half as big a share of something that must be worth more than twice as much [1].

In the general case, if n is the fraction you are giving up, the deal is good if it makes the company worth more than 1/(1 - n) [1].

### Example: Y Combinator

At the time of writing, YC took about 7% of a company. n = 0.07, and 1/(1 - 0.07) = 1.075. So the deal is worth taking if YC can improve your average outcome by more than 7.5%. If they improve it by 10%, you are net ahead: the remaining 0.93 you hold is worth 0.93 x 1.1 = 1.023 [1].

Graham comments: "This is why we can't believe anyone would think Y Combinator was a bad deal. Does anyone really think we're so useless that in three months we can't improve a startup's prospects by 7.5%?" [1]

### Example: Sequoia

Greg McAdoo from Sequoia said at a YC dinner that when Sequoia invests alone they like to take about 30% of a company. 1/0.7 = 1.43, meaning the deal is worth taking if Sequoia can improve your outcome by more than 43% [1].

For the average startup, this would be an extraordinary bargain. "It would improve the average startup's prospects by more than 43% just to be able to say they were funded by Sequoia, even if they never actually got the money" [1]. The reason Sequoia is such a good deal is that their percentage is "artificially low" -- they limit holdings to leave founders enough stock to feel the company is still theirs [1].

The catch: Sequoia gets about 6,000 business plans a year and funds about 20. The odds of getting this deal are 1 in 300. The companies that make it through are not average startups [1].

## Applying the Formula to Employee Equity

The formula works in reverse for employees. If i is the average outcome multiplier with the addition of a new person, they are worth n such that i = 1/(1 - n), which means n = (i - 1)/i [1].

### Worked Example

Suppose you are two founders and want to hire a hacker so good you estimate he will increase the average outcome by 20%. n = (1.2 - 1)/1.2 = 0.167. You would break even trading 16.7% of the company for this person [1].

But 16.7% is not the right amount to offer because stock is not the only cost. There is salary and overhead too. Graham suggests multiplying the annual salary-plus-overhead rate by about 1.5 to translate it into stock terms. The reasoning: most startups grow fast or die. If they die, you don't pay. If they grow fast, next year's salary comes out of next year's (presumably 3x higher) valuation. So the total stock-equivalent cost is about 1.5 years at the present valuation [1].

Full example: the employee is worth 16.7% but the company wants 50% profit on the hire, so his "retail" price is about 11.1%. If he costs $60k/year in salary and overhead, times 1.5 = $90k total. At a $2M valuation, $90k is 4.5%. So the stock offer is 11.1% - 4.5% = 6.6% [1].

Graham notes: "notice how important it is for early employees to take little salary. It comes right out of stock that could otherwise be given to them" [1].

## The General Principle

"Whenever you make any decision involving equity, run it through 1/(1 - n) to see if it makes sense. You should always feel richer after trading equity. If the trade didn't increase the value of your remaining shares enough to put you net ahead, you wouldn't have (or shouldn't have) done it" [1].

The formula does not eliminate guesswork -- "ultimately you always have to guess" -- but it ensures you know what you are guessing about. Whether you use gut feel or a VC-supplied table of typical grant sizes, understand that those are estimates of the multiplier in the equity equation [1].

## Limitations

The formula assumes you can estimate the outcome multiplier, which is inherently uncertain. For VC deals, there are always factors beyond a straight trade of money for stock [1]. The present valuation (typically the post-money of your last round) probably undervalues the company because (a) the company has presumably grown since the last round and (b) the valuation of an early round usually reflects some other contribution by the investors [1].

## References

1. [The Equity Equation](https://www.ycombinator.com/library/8u-the-equity-equation) -- [[Paul Graham]] (July 2007)
