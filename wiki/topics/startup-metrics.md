---
title: Startup Metrics
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["startup metrics", "key metrics", "KPIs", "vanity metrics", "revenue metrics", "burn rate", "retention metrics", "net dollar retention", "gross margin", "consumer metrics", "B2B metrics", "NPS", "net promoter score", "unit economics", "customer acquisition cost", "CAC", "magic moment"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[Financial Survival]]", "[[Runway Management]]", "[[Tom Blomfield]]"]
sources: ["KR-key-startup-metrics", "KT-consumer-startup-metrics"]
speakers_referenced: ["Tom Blomfield"]
---

# Startup Metrics

Metrics are the instruments that let founders navigate their startup. [[Tom Blomfield]], YC group partner and founder of Monzo (an online bank with 8 million customers in the UK), argues that running a startup without metrics is like flying an airplane without instruments [1]. But the opposite extreme -- 500 metrics on a dashboard before launch -- is equally counterproductive [1]. The goal is four or five key metrics, tracked accurately, with agreed-upon definitions, from the moment the product launches.

## The Foundation: Pick Four or Five Metrics

Blomfield recommends picking the most straightforward analytics solution available -- even raw SQL queries against the database -- and agreeing on four or five key metrics before launch [1]. The entire team must agree on definitions and stick with them. A "weekly active user" means the same thing to engineering, marketing, and sales. The exact definition matters less than consistency: "constant arguments about what your key metrics are are even worse than having no metrics at all" [1].

A critical discipline: do not change your metric definitions when results disappoint. If weekly active users are low, switching to monthly active users to get a better-looking number fools only the founder [1]. Blomfield saw this at Monzo, where competitors used different definitions of "active user" (some used eight-week windows), making cross-company comparisons meaningless. Internal consistency is what matters [1].

## Revenue: The Core Metric for B2B

For most B2B companies, revenue should be the primary metric [1]. Blomfield warns against vanity metrics -- numbers that look large and grow but are not tied to the company's success. Common examples include gross merchandise value (GMV), gross transaction value, page views, and unique visitors [1].

He worked with a neo-bank in the Middle East that reported gross transaction value growing 50% every two weeks. When he dug deeper, the company was signing up larger customers with massive cashback rebates. Gross transaction value was rising, but revenue had been flat for two months. "The founders were tricking themselves. They were fooling themselves into thinking their company was succeeding when in fact it was pretty flat in revenue terms" [1].

One of the most impressive founders Blomfield worked with sent ten consecutive monthly investor update emails with a big zero as the main metric. She was honest with investors and kept herself focused on fixing the problem rather than hiding it [1].

### Three Numbers for Every Investor Update

Every investor update should lead with three numbers [1]:

1. **Revenue** -- the money customers pay you
2. **Burn rate** -- net monthly costs minus revenues; the amount by which the bank balance decreases each month
3. **Runway** -- cash in bank divided by burn rate; the number of months until the company runs out of money

Blomfield states: "If they're not at the top of your investor updates, honestly, I always assume this founder has something to hide" [1].

## Retention: The Layer Cake

Retention measures whether users come back. Sign up 100 paying customers in January -- how many are still paying in February, March, April? Each month's signups form a "cohort," and stacking cohorts reveals whether the business is building a layer cake or filling a leaky bucket [1].

### The Layer Cake vs. the Leaky Bucket

If cohorts retain well -- 80%, 90%, even 100% -- they stack on top of each other over time. After eighteen months, eighteen cohorts are all contributing revenue simultaneously. Blomfield describes his first company, GoCardless (a recurring payments company similar to Stripe), as this pattern: customers implement a payment solution once, rarely switch, and the team could hypothetically go on holiday for a month and revenue would hold steady [1].

Even better is expanding revenue: if those January customers grow their own businesses, they transact more in year two and three. Revenue from existing customers increases without acquiring new ones. "That's the beauty of this high-retention business. It's sort of growing constantly underneath you" [1].

If retention goes to zero -- all customers from a given cohort churn within a few months -- the picture inverts. The company scrambles to acquire new customers just to replace the ones leaving. "You're pouring water into the top of the bucket, and it's leaking out of the bucket just as fast as you can fill it up" [1]. The company hits a natural plateau where growth effort exactly offsets churn. Building a big business on that foundation is "a futile endeavor" [1].

The critical test is whether retention flattens at some point. A 20% retention rate that flattens is more valuable than a higher initial rate that decays to zero [1].

### Net Dollar Retention (B2B SaaS)

Net dollar retention is the B2B SaaS version of retention. It accounts for both churn and upsells within a cohort [1].

Example: ten customers signed up in January, each paying $10,000/month ($100K total MRR from that cohort). Twelve months later, two have canceled (-$20K), but three have upsold to $20K each (+$30K). Net change is +$10K, so the cohort now generates $110K. That is 110% net dollar retention [1].

Above 100% means cohorts grow over time. Below 100% means they shrink. Combined with new customer acquisition, net dollar retention above 100% produces the exponential growth curve that characterizes companies like Stripe, GoCardless, and PayPal [1].

**Benchmarks** [1]:
- Early-stage B2B SaaS: 125-150% (or higher)
- Mature B2B SaaS: 110-120%
- Below 100%: something is wrong -- customers do not love the product

Three reasons early-stage NDR should be high [1]:
1. The product was likely underpriced at launch -- founders discover they could charge $20K-$30K instead of $10K
2. New features make the product more appealing and worth more
3. The sales team should be getting better at upselling over time

If net dollar retention is below 100%, Blomfield advises investing in fixing churn (talking to customers, understanding why they leave) rather than spending on acquiring more customers [1].

## Gross Margin

Gross margin is revenue minus the cost of goods sold (COGS) -- the variable costs that scale with each additional customer [1].

For pure software companies, COGS was historically minimal (AWS bill, bandwidth), producing 95% gross margins. But as software expands into operationally intensive industries, gross margin has become critical [1]. For AI companies, the cost of foundation model API calls (OpenAI, Anthropic) is a significant COGS. Blomfield warns: "Just because you're getting free credits doesn't mean that that's a cost that doesn't exist. It just means you're hiding it for the moment" [1].

Operationally intensive businesses (grocery delivery, house painting, heat pump installation) may have gross margins of 5-15%. This means the company must generate far more revenue to cover fixed costs like engineering salaries and office rent. Blomfield often works with founders to explore whether a software-only version of their business could run at much higher margins -- for example, selling logistics software to delivery companies rather than running a delivery company [1].

### The Danger of Scaling Negative Margins

In the 2010-2021 zero interest rate environment, companies famously scaled negative-margin businesses. Uber subsidized both drivers and riders in new cities to achieve network density, burning tens of billions in investor capital. This "blitz scaling" approach spread to ten-minute grocery delivery, electric scooters, and other categories. Most of those startups failed when they could not continue raising money [1].

Blomfield experienced this at Monzo. For the first half-million customers, Monzo lost 30-40 pounds per customer. They eventually flipped the economics by bringing technology in-house, introducing charges for certain services, and launching paid products. Several years later, Monzo became profitable [1].

The lesson: "If you start with negative unit economics, you really, really have to have a plan to fix them. And I would really advise you: don't scale your customer base, don't try and grow as quickly as possible whilst you have negative unit economics. You fix them first, and then you scale" [1].

## Consumer Startup Metrics

Consumer companies face a different metrics landscape. Revenue may come later -- first, the company needs to build a user base, often through [[Network Effects]] and viral loops [2].

### Growth Benchmarks for Consumer Startups

Blomfield provides month-over-month active user growth benchmarks [2]:
- **15% monthly growth**: good (5x annual growth)
- **10% monthly growth**: okay (roughly 3x annual growth)
- **5% monthly growth or lower**: unlikely to reach breakout success

### Organic vs. Paid Growth

Organic growth is anything the company does not pay for. Blomfield got Monzo to one million customers before spending any money on direct marketing, using virality and network effects [2].

**Virality** is when one user's actions introduce the product to non-users. Facebook's photo tagging prompted friends to sign up. Wordle players post their scores on social media, attracting new players [2].

**Network effects** follow Metcalfe's law: the value of the network grows with the square of the number of nodes. WhatsApp is useless if you are the only user; it becomes essential when everyone you know is on it [2].

The best consumer companies incorporate both. At Monzo, groups going on holiday would start with three people using Monzo and end with all six or seven, because the in-app money-sharing features only worked if everyone was on the platform [2].

**The compounding difference**: investment in viral loops and network effects pays back for the life of the company. Paid advertising pays back only while money is being spent [2].

Blomfield's benchmarks for organic/paid split [2]:
- **Best consumer companies**: 80%+ organic, often 100% organic in early days (Facebook, WhatsApp)
- **Acceptable**: 50/50
- **Worrisome**: below 50% organic for any sustained period

Relying heavily on paid growth (Google Ads, Meta ads) is dangerous because platforms are optimized to extract maximum value. Competing companies bid against each other, driving margins to zero while Google and Meta collect the profits. Platform shifts (like iOS privacy changes) can destroy paid acquisition channels overnight [2].

Blomfield states: "I've not seen any great consumer company get to true scale where more than 50% of their signups are coming from paid ads" [2].

### Customer Acquisition Cost (CAC)

For paid growth, founders must track the cost to acquire each user, broken down by channel. Crucially, CAC should be measured to an active, monetized, retaining user -- not just a signup, since 80-90% of signups may drop off in the first week [2].

Blomfield learned this at Monzo: a money-saving blog sent hundreds of users very cheaply, but those users were deeply unprofitable. They would load money onto Monzo, go on holiday, withdraw $1,000 from ATMs (generating high fees for Monzo), and never return. The channel's low acquisition cost masked a negative lifetime value. Monzo shut it down [2].

The lesson: record the acquisition source for every user permanently in the database, and monitor the long-term performance of users from each channel [2].

### Paid Referral Schemes

Paid referrals ("refer a friend, you both get $5") should be treated as paid acquisition, not organic growth [2]. Two risks:

1. **Cannibalization**: users who would have referred friends anyway are now being paid to do so. Test by running the scheme in some cities or time periods and measuring the natural referral rate without it [2].
2. **Fraud**: people gaming the referral system. Blomfield had a friend who set up Google Ads bidding on Zipcar's name, redirecting users through his referral link, and drove free Zipcars for a year before being banned [2].

### Unit Economics

Unit economics measure the revenue each customer generates minus the variable costs of serving that customer [2]. At Monzo, each customer generated about $50 in revenue, but costs included sending plastic cards, customer service contacts, fraud, and transaction fees [2].

Tracking unit economics at the individual customer level reveals which customer segments are profitable and which are not, which acquisition channels bring profitable users, and where to invest in cost reduction [2].

Blomfield warns about scaling negative unit economics: "In the early days of Monzo, we were at $3 or $4 per customer per year. And we scaled to half a million customers before we fixed them and burned a lot of capital" [2].

### Retention and the Magic Moment

Consumer retention is harder to define than B2B retention because usage patterns vary. Facebook expects daily use; Airbnb might see a booking every six months [2]. For each business, founders must define what "active" means for a successful customer. At Monzo, it was one financial transaction per week [2].

When the natural usage period is long (months or years), companies look for a **magic moment** -- an early user behavior that correlates with long-term retention [2].

**Facebook's magic moment**: adding seven friends in the first 10 days. Users who did this overwhelmingly became long-term users. Users who did not were much more likely to churn [2].

**Monzo's magic moment**: adding three friends from the phone book to enable peer-to-peer payments. Users who did this retained roughly 20 percentage points better than those who did not [2].

Once the magic moment is identified, the company re-engineers onboarding to get as many users as possible to that point as quickly as possible. Facebook made "add friend" prompts central to the signup flow [2].

Blomfield warns against over-optimizing the precise definition: "For Facebook, it probably didn't matter that much whether it was seven friends or eight friends or six friends. Simply finding that kind of tipping point that looks about right from your metrics and then agreeing with everyone that that's what you're going to optimize for" is sufficient [2].

### Net Promoter Score (NPS)

NPS measures how likely customers are to recommend the product. Customers rate 0-10; promoters (9-10) minus detractors (0-6) equals NPS [2].

- NPS of +100: every customer is a promoter
- NPS of -100: every customer is a detractor
- Tesla: +96
- Monzo: +75 to +80
- Old incumbents (banks, cell phone companies): often 0 or negative

Blomfield states that a new consumer company needs an NPS of +50 at minimum. An NPS below that signals the product is not good enough for word-of-mouth growth, which is the engine of great consumer companies [2].

**Measurement discipline**: NPS must be gathered consistently -- same point in the product, same customer lifecycle stage, same frequency. Changing the collection method produces wild swings. At Grouper (a dating startup Blomfield worked at), changing the collection method caused a 20-point NPS drop overnight that was entirely an artifact [2].

**Improving NPS**: after the rating question, ask "Why?" Then examine detractor responses and fix the problems they identify [2].

## Metrics as Blend, Not Bible

Blomfield closes with a warning against treating benchmarks as universal rules. Every company and industry is different. A company might have off-the-charts organic growth and poor unit economics (early Monzo), or excellent economics with slow, paid-driven growth [1] [2]. The right approach combines metrics, talking to customers, and product intuition. "You still have to get out of the building and talk to customers. Brian from Airbnb still hosts Airbnb users in his home" [1].

## References

1. [Key Startup Metrics](https://www.ycombinator.com/library/KR-key-startup-metrics) -- [[Tom Blomfield]] (n.d.)
2. [Consumer Startup Metrics](https://www.ycombinator.com/library/KT-consumer-startup-metrics) -- [[Tom Blomfield]] (n.d.)
