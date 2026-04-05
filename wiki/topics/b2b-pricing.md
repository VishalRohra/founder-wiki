---
title: B2B Pricing
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["B2B pricing", "startup pricing", "how to price", "pricing strategy", "value-based pricing", "enterprise pricing", "SaaS pricing", "pricing for startups"]
related: ["[[Enterprise Sales]]", "[[Growth]]", "[[Startup Metrics]]", "[[Product-Market Fit]]", "[[Tom Blomfield]]", "[[Pete Koomen]]"]
sources: ["LI-how-to-price-for-b2b", "LF-enterprise-sales-for-founders"]
speakers_referenced: ["Tom Blomfield", "Pete Koomen"]
---

# B2B Pricing

Pricing is one of the most common questions founders ask, and one of the most common sources of paralysis. [[Tom Blomfield]] provides a systematic framework for B2B pricing built on three elements: value, cost, and competition [1]. [[Pete Koomen]] adds tactical lessons from scaling Optimizely to $100M ARR [2]. The consensus: founders almost always charge too little, and over-optimizing pricing early is a bigger mistake than picking a slightly wrong number.

## The Value Equation

The most important element of pricing -- accounting for 80-90% of getting it right -- is the value equation [1]. Sit down with the champion (the person at the customer who wants to buy) and write down what the product will do for them: cost savings, time savings, or revenue increase [1].

Blomfield walks through a concrete example: selling a customer service AI tool to a company with 100 support agents, each costing $100K fully loaded ($10M total). If the tool eliminates 20% of queries, that is $2M in savings [1].

Price at roughly 25-50% of the value delivered. The customer keeps two-thirds, you keep one-third. In this example: charge approximately $700K [1]. This gives the champion a clear story to tell their CFO: "We spend $700K, we save $2M" [1].

The value equation also defines success metrics for pilots: if the tool saves 20% of agent time during a one-month trial with 10 agents, the value holds. If it saves only 15% or a surprising 25%, adjust pricing accordingly [1].

**Never start with cost.** Cost-plus-a-margin pricing always leads to underpricing software [1]. Cost should only be a floor. If your value equation yields $700K and your costs (e.g., OpenAI API fees, AWS) are $200K, you have healthy 70%+ margins. If value yields $150K and costs are $200K, you are in a bad business [1].

Aim for 80-90% software margins. Treat free credits (AWS, OpenAI, Microsoft) as a cash cost -- "don't assume you'll have unlimited credits forever" [1].

## Competition

If a direct competitor underprices you by half, the instinct is to engage in a price war. This is a race to the bottom where nobody wins [1]. The airline industry averages 2.7% net profit margin because seats are a commodity [1].

Instead, differentiate on functionality or value so the comparison is not apples-to-apples [1]. "Pick a niche, focus on certain integrations or certain industries, and show how your product is dramatically better and really incomparable to competitors" [1].

## The Most Common Pricing Mistake: Charging Too Little

Both Blomfield and Koomen emphasize this independently. Blomfield notes that founders who have never worked at a big company lack calibration on enterprise software pricing and default to consumer prices like $19/month or $49/month [1].

Koomen shares a story from early Optimizely: his co-founder Dan quoted a prospect $10,000/month. The prospect negotiated down to $2,000/month and bought. The initial quote was 5x what they paid, and they still bought [2]. "When a customer really wants your product, it's hard to scare them away by quoting a price that's too high" [2].

The Collison brothers at Stripe deliberately charged more than competitors in the beginning. The fact that customers still bought was evidence they were onto something, and it helped them focus on the most desperate customers [2].

Blomfield's escalation technique for founders who freeze: start at a number, and increase by 50% for each subsequent customer. "When you start to lose more than 25% of potential deals based solely on price, you're now probably in the right ballpark" [1]. If every deal closes immediately, you are underpricing [1].

## Pricing Structure

Ask the champion what pricing structures they are accustomed to: monthly flat fee, per-seat, usage bands, credits [1]. Mirror what they know. People are wary of uncapped usage-based pricing [1].

**Prefer committed recurring revenue (MRR/ARR) over pure usage-based pricing.** During a downturn, committed revenue is protected until renewal. Usage-based revenue can fall off a cliff in a bad month [1]. One technique: start with usage-based pricing for new customers, observe their usage for a month or two, then offer a discounted flat monthly fee with a 12-month commitment [1].

Ask what amount the champion can personally sign off on without CFO or legal approval. If their signing authority is $15,000, price the pilot at $14,999 to move quickly [1].

## Published Pricing vs. "Contact Sales"

For enterprise contracts, publishing a fixed price almost certainly leaves money on the table because the value equation differs for each customer [1]. Typical approach: offer one or two cheaper self-serve plans (individual, small team) with basic functionality, and gate features enterprises require -- SOC 2 audit reports, SSO, audit logs, data residency -- behind an enterprise plan that requires contacting sales [1]. This enables pricing enterprises up to 10x more for compliance and security features [1].

## Pricing Dictates Sales Channels

A useful rule of thumb: a salesperson should generate 5x their total compensation in new ARR [1]. If a salesperson earns $100K (base + commission), they should close $500K in new ARR per year. This can be structured as:

| Contract Size | Deals Per Year | Sales Motion |
|---|---|---|
| $500K | 1 | Whale hunting |
| $25K | 20 (~2/month) | Account executive |
| $1K | 500 (~42/month) | Inside sales / call center |

At $1K annual contract value, an outbound sales team is not viable -- you need self-serve or inbound [1].

## Free Trials and Pilots

Long free trials are counterproductive because the customer has not committed to using the product [1]. Keep pilots to two to four weeks with clear success criteria derived from the value equation [1].

A better technique: push customers to sign an annual contract from the start with a 30-60 day money-back guarantee. This defaults to recurring revenue and can be counted as such immediately [1].

## Playing to Startup Strengths

When a two-person startup sells to enterprises, do not try to look bigger than you are. Instead, offer what large vendors cannot: "You can have the phone number of the founders, and we're on call 24/7 to come and fix your problems. You're certainly not going to get that from Salesforce or Oracle" [1].

## References

1. [How To Price For B2B](https://www.ycombinator.com/library/LI-how-to-price-for-b2b) -- [[Tom Blomfield]] (2024)
2. [Enterprise Sales for Founders](https://www.ycombinator.com/library/LF-enterprise-sales-for-founders) -- [[Pete Koomen]] (2024)
