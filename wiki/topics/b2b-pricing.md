---
title: B2B Pricing
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["B2B pricing", "how to price", "pricing strategy", "value-based pricing", "enterprise pricing", "SaaS pricing", "pricing for startups", "value equation"]
related: ["[[Enterprise Sales]]", "[[Growth]]", "[[Product-Market Fit]]", "[[Tom Blomfield]]"]
sources: ["LI-how-to-price-for-b2b"]
speakers_referenced: ["Tom Blomfield"]
---

# B2B Pricing

Pricing is one of the most common questions early-stage founders ask, and one of the easiest to overthink. [[Tom Blomfield]], YC Group Partner, presents a framework built on three elements -- value, cost, and competition -- with the value equation as the dominant driver [1].

## The Value Equation

The value equation is by far the most important element. It accounts for 80-90% of getting the price right [1]. The method: sit down with the champion (the person at the customer who wants the product), and together write down what value the product will deliver to their company. That value falls into three categories: cost savings, time savings, or revenue increases [1].

### Worked Example

A customer service AI tool sold to a company with 100 support agents. Each agent costs $100,000 fully loaded (salary plus offices, health insurance, overhead). Total customer service cost: $10 million. If the AI tool eliminates 20% of queries, that is $2 million of potential savings [1].

The pricing rule: charge 25-50% of the value delivered. The customer keeps roughly two-thirds, the startup keeps roughly one-third [1]. In the example, $2 million in savings yields a contract price of roughly $700,000 [1].

The value equation also produces the success metrics for a pilot. In the example, if a one-month trial with 10 agents shows at least 20% query reduction, the value equation holds. If the pilot shows 15% or 25%, the pricing can be adjusted accordingly [1].

### Why Value Comes First

Blomfield warns against starting with cost-plus pricing, which "always ends up with you underpricing your software" [1]. Founders who have spent months building a product often calibrate against the last software they personally bought -- a $19/month GitHub subscription or ChatGPT -- and propose ludicrously low numbers. "Asking for tens or even hundreds of thousands of dollars can feel very uncomfortable. You almost can't say it with a straight face" [1]. The value equation provides the justification that makes large numbers defensible.

The value equation is also a sales tool: the champion takes it to their boss or CFO to justify the purchase [1].

## Cost as a Floor

Cost should never be the starting point for pricing, only a floor [1]. If the value equation yields a $700,000 contract and costs (OpenAI fees, AWS) are $200,000, margins are healthy. If the value equation yields $150,000 but costs are $200,000, the business is unsustainable -- either demonstrate more value, change what you are building, or exit the business [1].

The target for software margins is 80-90% [1].

### A Note on Credits

Startups receive large credits from AWS, Microsoft, and OpenAI. Blomfield warns to treat these as cash costs: "Don't assume you'll have unlimited credits forever. It'll totally mess up your margins" [1].

### Pricing Below Cost

Pricing at or below cost is a "really, really risky maneuver" typically used in land-grab situations where the founder bets costs will decline dramatically [1]. With LLM costs dropping rapidly from providers like OpenAI and Anthropic, there may be a case for slightly lower pricing in anticipation of margin improvement, but Blomfield advises startups to maintain 80-90% gross margins [1].

## Competition

If a direct competitor enters at half your price, the instinct is to start a price war -- undercutting them, then they undercut you, in a race to the bottom. Blomfield warns against this: "Competing solely on pricing really is not a winning maneuver" [1].

The airline industry illustrates the endpoint: a commodity product (a seat across the country) with extreme competition produces an average net profit margin of 2.7%. "It's a brutal, brutal business" [1].

The alternative: differentiate the product. "It can't be an apples-for-apples comparison. Your product needs to be differentiated" [1]. Pick a niche, focus on specific integrations or industries, and make the product incomparable to competitors.

## Pricing Structure

### Mirror What Customers Know

Ask the champion how they pay for other similar software. Are they used to monthly flat fees, per-seat pricing, usage bands, or credits? "Pick a pricing strategy they're used to" [1]. People are wary of uncapped usage-based pricing, so caps are advisable [1].

### Committed Recurring Revenue Over Usage

Monthly or annual recurring revenue (MRR/ARR) is preferable to pure usage-based pricing because it protects revenue during economic downturns [1]. A practical technique: start with usage-based pricing for new customers, run it for a month or two to establish a baseline, then offer a minimum monthly commitment with volume discounts. If the customer averages $15,000/month in usage, offer a $12,000/month flat fee on a 12-month contract [1].

### Signing Authority Hack

Ask the champion what dollar amount they can personally sign off on without CFO or legal approval. If their limit is $15,000, keep pilot pricing at $14,999 to keep things moving quickly [1].

## Published Prices vs. "Contact Sales"

Software developers often prefer transparent pricing with a "click to buy" button. But for enterprise contracts, the value equation differs for each customer. A single published price either overprices for low-value customers (losing them) or underprices for high-value customers (leaving money on the table) [1].

The standard approach: one or two cheaper plans (individual, small team) with basic functionality, and an enterprise plan gated behind "contact sales." Features commonly gated behind enterprise pricing include SOC 2 audit reports, single sign-on, audit logs, compliance reports, and data residency requirements -- things individuals do not care about but enterprises cannot live without [1]. This allows pricing enterprise customers up to 10x more than small customers [1].

## Pricing Dictates Sales Channels

A useful rule of thumb: 5:1 ratio between new signed ARR and total salesperson compensation (base plus commission) [1]. If a salesperson earns $100,000/year, they should close $500,000 in new ARR.

This creates very different sales models depending on deal size [1]:

| Annual Contract Value | Deals Needed per Year | Sales Model |
|---|---|---|
| $500,000 | 1 | Whale hunting, 4-6 active deals |
| $25,000 | 20 | ~2 deals per month, traditional AE |
| $1,000 | 500 | ~42 per month, inside sales/call center |

At $83/month contract values, a traditional sales team is not viable. The motion shifts to self-serve or inside sales [1].

## Free Trials and Pilots

Long free trials are counterproductive because the customer has not committed to using the product [1]. Keep pilots to two to four weeks with clear success criteria from the value equation.

A stronger technique: push for an annual contract from the start with a 30-60 day money-back guarantee. "By default it becomes a recurring contract. You can count this as recurring revenue pretty much straight away" [1].

## Playing to Startup Strengths

Founders sometimes ask whether they should fabricate a larger team on their website. Blomfield advises against it. Instead, play to the strengths of being small: "Say to your customers, 'You can have the phone number of the founders, and we're on call 24/7 to come and fix your problems.' You're certainly not going to get that from Salesforce or Oracle" [1].

## When All Else Fails: The Ratchet Method

If the value equation is too uncertain, pick a number similar to other software the customer buys, then increase by 50% for each subsequent customer [1]. Start at $10,000; if they say yes, pitch $15,000 to the next customer, then $22,000. "When you start to lose more than 25% of potential deals based solely on price, you're now probably in the right ballpark" [1].

If every deal closes immediately, the price is almost certainly too low [1].

## Do Not Over-Optimize Early

The first two or three sales are the hardest the company will ever have to make. These initial five or ten customers will be a tiny fraction of future revenue. "Over-optimizing for pricing early is a big mistake. Pick a number" [1]. Prices can always increase as the product improves, new modules are added behind paywalls, and validation logos accumulate on the homepage [1].

## References

1. [How To Price For B2B](https://ycombinator.com/library/LI-how-to-price-for-b2b) — [[Tom Blomfield]] (2025)
