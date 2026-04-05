---
title: Startup Metrics
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["startup metrics", "key metrics", "KPIs", "vanity metrics", "retention metrics", "net dollar retention", "NDR", "gross margin", "unit economics", "NPS", "net promoter score", "consumer metrics", "B2B metrics", "burn rate", "runway"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[B2B Pricing]]", "[[Financial Survival]]", "[[Tom Blomfield]]"]
sources: ["KR-key-startup-metrics", "KT-consumer-startup-metrics"]
speakers_referenced: ["Tom Blomfield"]
---

# Startup Metrics

[[Tom Blomfield]], YC Group Partner and founder of Monzo (8 million customers in the UK) and GoCardless, provides two comprehensive lectures on startup metrics -- one for B2B companies and one for consumer companies [1] [2]. The core message: metrics are like instruments in an airplane cockpit. Without them, you are flying blind. But too many metrics -- or the wrong ones -- are equally dangerous.

## Principles Before Metrics

Before launching, pick four or five key metrics to track accurately -- not 30 or 50 [1]. The number will grow over time. Use the simplest analytics solution you can operate, even just SQL queries against your database [1].

Three warnings Blomfield emphasizes:

1. **Don't launch without metrics.** Blomfield has seen founders have great launches on Hacker News or Product Hunt with hundreds of daily users but no idea whether those users are new or returning, active or churning [1].

2. **Don't drown in metrics.** A 500-metric dashboard before launch signals a founder who has watched too many YouTube videos. "You don't have the volume of users or data to make those kinds of split tests sensibly" [1]. Split-test important decisions (should the price be $80/year or $200/year?) but not button colors.

3. **Don't hide behind metrics.** "Brian from Airbnb still hosts Airbnb users in his home. It's an obsession with staying close to customers" [1]. Metrics supplement talking to users, not replace it.

Agree on metric definitions with your entire team and write them down. Constant arguments about definitions destroy meeting productivity. Keep definitions consistent over time -- even if the numbers are disappointing. "You're only fooling yourself" if you switch from weekly active to monthly active to make the numbers look better [1].

## The Three Numbers Every Investor Update Needs

For every company, B2B or consumer, three numbers should be at the top of every investor update [1]:

1. **Revenue** -- the primary metric for most B2B companies. If revenue is zero, report it as zero. One founder Blomfield admired sent ten successive monthly updates with a big zero as the main metric. "She kept herself honest" [1].

2. **Burn rate** -- net monthly costs minus revenues. The amount by which your bank balance decreases each month [1].

3. **Runway** -- cash in bank divided by burn rate. "In ten months, you're going to run out of money, and the startup will be bankrupt" [1].

If these three numbers are not at the top of your investor updates, "I always assume this founder has something to hide" [1].

## Avoiding Vanity Metrics

Vanity metrics are numbers that look big and may keep increasing but are not tied to company success [1]. Common examples:

- **GMV (Gross Merchandise Value)**: The total value of goods sold on a platform, not the platform's actual revenue. eBay reports GMV, but revenue is a fraction of it [1].
- **Gross Transaction Value**: A neobank Blomfield worked with in the Middle East reported 50% growth in transaction value every two weeks. Revenue was flat for two months -- they were signing bigger customers but giving massive cashback rebates [1].
- In the early internet era: page views, unique visitors [1].

"Almost always, especially for B2B companies, your key metric should be revenue" [1]. Whatever metric you pick, people will optimize for it. Make sure it is the right one.

## Retention: The Make-or-Break Metric

Retention is one of the most important metrics for all startups [1]. If you sign up 100 paying customers in January, how many are still paying in February, March, April?

### The Layer Cake vs. The Leaky Bucket

Blomfield uses a visualization of stacked monthly cohorts to illustrate why retention matters [1]:

**High retention (the layer cake):** Each monthly cohort retains most of its users. After 18 months, you have 18 cohorts all paying you. The team could go on holiday for a month and revenue stays consistent. With expanding revenue -- customers growing their usage over time -- the business grows even without new signups [1]. GoCardless and Stripe exhibit this pattern: customers implement a payment solution once and rarely switch [1].

**Low retention (the leaky bucket):** Customers signed up in January are gone by month three or six. Instead of building stable layers, you scramble to fill a bucket that leaks as fast as you pour. "You'll reach some natural plateau where you're working as hard as you can to fill up the customers who simply churned out last month. It's a futile endeavor" [1].

The key insight: "I take a 20% retention that flattens out over a higher retention initially that goes to zero" [1]. What matters is that the retention curve flattens somewhere -- at any level.

### Net Dollar Retention (B2B)

Net dollar retention (NDR) measures whether revenue from a given cohort grows or shrinks over time [1]. Example: sign up 10 customers in January at $10K/month each ($100K MRR). One year later, two have canceled ($-20K), but three have upsold to $20K/month ($+30K). Net change: +$10K. January cohort now generates $110K/month. That is 110% net dollar retention [1].

NDR above 100% means cohorts grow over time. Below 100% means they shrink -- the leaky bucket [1].

**Benchmarks:**
- Early-stage B2B SaaS: aim for 125% to 150% NDR [1]
- Mature B2B SaaS: 110% to 120% is good [1]
- Below 100%: "Something is wrong. You are churning off customers. They don't love the product" [1]

Three reasons early-stage NDR should be high: you have probably underpriced initially, you are adding features constantly, and you should be getting better at upselling [1].

## Gross Margin

Gross margin is revenue minus cost of goods sold (COGS) -- the variable costs that scale per customer [1].

Pure B2B SaaS historically had 95% margins (just AWS/bandwidth costs). AI changes this: credits paid to OpenAI, Anthropic, or other foundation models are now a significant COGS. "Just because you're getting free credits doesn't mean that cost doesn't exist. It just means you're hiding it for the moment" [1].

Operationally intensive businesses (grocery delivery, house painting, heat pump installation) may have 5-15% gross margins. Blomfield advises exploring whether a software-only version of the business exists: "Instead of running a delivery company, can you take the software that powers all of that and sell it to other delivery companies?" [1]

### Scaling Negative Margins

During the ZIRP era (2010-2021), companies like Uber scaled negative-margin businesses using capital as a weapon, subsidizing both sides of the market to reach network-effect density before competitors [1]. This approach became popular in ride-sharing, ten-minute grocery, and electric scooters. "There's a whole wasteland of startups that tried to do that" [1].

Monzo lost 30-40 pounds per customer on its first half million users, then flipped unit economics by bringing technology in-house, introducing charges, and adding paid products [1]. The lesson: "If you start with negative unit economics, you really have to have a plan to fix them. Don't scale your customer base whilst you have negative unit economics. Fix them first, then scale" [1].

## Consumer-Specific Metrics

### Growth Rate Benchmarks

For consumer companies, Blomfield provides specific growth benchmarks [2]:

| Monthly Growth Rate | Assessment |
|---|---|
| 15%+ | Good -- will 5x user base every year |
| 10% | Okay -- will approximately 3x every year |
| 5% or lower | Unlikely to reach breakout success |

### Organic vs. Paid Growth

The best consumer companies have 80%+ organic growth [2]. Facebook and WhatsApp in their early days were 100% organic. A 50/50 split between paid and organic is acceptable. Below 50% organic "is pretty worrisome" [2].

The reason: as you pay ad platforms more to acquire more users, cost per user rises. "All these competing companies bid and bid and bid. Only Google and Meta really win in that battle. You all take your margins to zero" [2]. Platform changes (e.g., iOS tracking changes) can wipe out half your business overnight [2].

"I've not seen any great consumer company get to true scale where more than 50% of their signups are coming from paid ads" [2].

**Organic growth levers:**

- **Virality**: one user using the product introduces it to others. Facebook's photo-tagging sent emails to unregistered friends. Wordle's score-sharing on social media [2].
- **Network effects**: the product gets better with more users. WhatsApp is useless alone but valuable when everyone uses it [2].

Blomfield argues: "On these network effect and viral loops, you will pay back every day for the rest of the life of the company. Whereas with ad spend, you spend the money one day. Tomorrow it's gone" [2].

### Unit Economics

Revenue per customer minus variable costs per customer. At Monzo, each customer generated about $50 in revenue, but costs included card production, customer service, fraud, and transaction fees -- all tracked per customer [2].

This granularity matters: Monzo discovered that customers from one particular money-saving blog were deeply unprofitable (they loaded cards, went on holiday, and withdrew cash from ATMs). They shut down that advertising channel despite its low acquisition cost because lifetime value was negative [2].

"Unit economics should be tracked to an active, monetized, retaining user, not simply a sign-up" because 80-90% may drop off in the first week [2].

### The Magic Moment

When retention periods are long (Airbnb users may only book every six months), look for a "magic moment" -- a user behavior that predicts long-term retention [2].

Facebook discovered that adding seven friends in the first 10 days predicted long-term usage. Monzo found that adding three friends from one's phone book to send/receive money improved retention by 20 percentage points [2].

Once identified, re-engineer the product onboarding to push as many users as possible toward this magic moment [2]. Do not get overly fixated on the precise definition -- "it probably didn't matter that much whether it was seven friends or eight friends" [2].

### Net Promoter Score (NPS)

NPS measures how likely users are to recommend the product to a friend, on a 0-10 scale. Promoters (9-10) minus detractors (0-6) equals the score [2].

Benchmarks for new consumer companies: +50 is a minimum baseline. Monzo hovered between +75 and +80. Tesla is at +96. Old incumbents (cell phone companies, legacy banks) often score zero or negative -- a signal of disruption opportunity [2].

Crucial: keep the measurement method consistent. Blomfield's dating startup Grouper changed the collection method and NPS dropped 20 points overnight -- an artifact, not a real change [2].

Follow up the NPS question with "Why?" Then fix every issue detractors raise [2].

## References

1. [Key Startup Metrics](https://www.ycombinator.com/library/KR-key-startup-metrics) -- [[Tom Blomfield]] (2023)
2. [Consumer Startup Metrics](https://www.ycombinator.com/library/KT-consumer-startup-metrics) -- [[Tom Blomfield]] (2023)
