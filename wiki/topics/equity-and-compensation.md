---
title: Equity and Compensation
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["equity", "stock options", "equity equation", "employee equity", "refresher grants", "compensation bands", "stock grants", "equity split"]
related: ["[[The Equity Equation]]", "[[Fundraising]]", "[[Hiring]]", "[[Cofounders]]", "[[Paul Graham]]", "[[Financial Survival]]"]
sources: ["8u-the-equity-equation", "93-a-student-s-guide-to-startups", "Gu-snapdocs-aaron-king-on-navigating-market-cycles"]
speakers_referenced: ["Paul Graham", "Aaron King"]
---

# Equity and Compensation

Equity decisions -- how much to give investors, employees, and cofounders -- are among the hardest questions founders face. [[Paul Graham]] provides a mathematical framework for evaluating any trade of company stock, whether for investment, hires, or partnerships.

## The Equity Equation

Graham's central insight: every equity trade has the same test. "You should give up n% of your company if what you trade it for improves your average outcome enough that the (100-n)% you have left is worth more than the whole company was before." ([The Equity Equation](http://www.paulgraham.com/equity.html))

The formula: **1/(1-n)**

If n is the fraction you're giving up, the deal is good if it makes the company worth more than 1/(1-n) times its current value.

**Investment example:** If an investor wants half your company, they must at least double your average outcome for you to break even. You'd have half of something worth more than twice as much.

**YC example:** YC takes 7%. 1/(1-0.07) = 1.075. The deal is worth taking if YC improves your outcome by more than 7.5%. "If we improve your outcome by 10%, you're net ahead, because the remaining .93 you hold is worth .93 x 1.1 = 1.023." Graham adds: "This is why we can't believe anyone would think Y Combinator was a bad deal. Does anyone really think we're so useless that in three months we can't improve a startup's prospects by 7.5%?"

**Sequoia example:** Greg McAdoo from Sequoia said they like to take about 30% when investing alone. 1/0.7 = 1.43. The deal is worth taking if Sequoia improves your outcome by 43%. "For the average startup, that would be an extraordinary bargain. It would improve the average startup's prospects by more than 43% just to be able to *say* they were funded by Sequoia." The catch: Sequoia funds about 20 of 6,000 annual applicants.

## Employee Equity

The same formula works in reverse for employee grants. If a new hire improves your average outcome by factor i, they're worth n such that i = 1/(1-n), which gives n = (i-1)/i.

**Worked example:** Two founders want to hire a hacker who'd increase average outcome by 20%. n = (1.2-1)/1.2 = 0.167. You'd break even giving 16.7% of the company.

But stock isn't the only cost. Salary and overhead must be accounted for. Graham's rule of thumb for converting salary to stock cost: multiply the annual rate by about 1.5. The reasoning: "Most startups grow fast or die; if you die you don't have to pay the guy, and if you grow fast you'll be paying next year's salary out of next year's valuation, which should be 3x this year's."

**Full worked example:** Suppose a company wants 50% "profit" on the hire. One third off 16.7% = 11.1% "retail price." At $60K/year salary + overhead, x1.5 = $90K total stock-equivalent cost. If company valuation is $2M, $90K = 4.5%. So the offer is 11.1% - 4.5% = **6.6%** equity.

Graham observes: "Notice how important it is for early employees to take little salary. It comes right out of stock that could otherwise be given to them."

The formula doesn't replace judgment. "I'm not claiming that stock grants can now be reduced to a formula. Ultimately you always have to guess. But at least know what you're guessing." If you use a gut number or a VC-supplied table of typical grants, understand that those are estimates of the same underlying calculation.

The meta-principle: "You should always feel richer after trading equity. If the trade didn't increase the value of your remaining shares enough to put you net ahead, you wouldn't have (or shouldn't have) done it."

## Valuation for Stock Calculations

Graham suggests using the post-money valuation of the last funding round as the present valuation. He notes this probably undervalues the company because (a) time has passed since the round, and (b) the valuation usually reflects contributions from investors beyond just cash.

## Early Employee Equity in Practice: Snapdocs

[[Aaron King]] of Snapdocs describes treating early hires "like founding team members." He was "generous with equity and shared everything about the potential and challenges of the business." This built deep trust within the small team.

King's early hiring approach: his first full-time hire was an engineer from a previous job. The second and third came from Hacker News job postings. None had large networks in the startup world. King invested in people he "thought had a lot of potential" rather than well-known talent. As Snapdocs grew, employees began referring friends, creating a virtuous recruiting cycle.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| 8u-the-equity-equation | Paul Graham | The 1/(1-n) formula for all equity trades; investment, employee, and deal applications |
| 93-a-student-s-guide-to-startups | Paul Graham | Check employment agreements before starting; code written while employed may belong to employer |
| Gu-snapdocs-aaron-king-on-navigating-market-cycles | Aaron King | Generous equity for early employees; treating hires like founding team members |
