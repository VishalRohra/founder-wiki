---
title: Growth Teams
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["growth team", "growth program", "growth hiring", "growth engineering", "scaling growth", "growth PM", "growth product manager"]
related: ["[[Growth]]", "[[Retention and Engagement]]", "[[Analytics and Metrics]]", "[[Hiring]]", "[[Product-Market Fit]]"]
sources: ["59-how-to-set-up-hire-and-scale-a-growth-strategy-and-team"]
speakers_referenced: ["Anu Hariharan", "Gustaf Alstromer"]
---

# Growth Teams

A growth team is a cross-functional unit dedicated to driving user acquisition, activation, and retention through structured experimentation. [[Anu Hariharan]] and [[Gustaf Alstromer]] compiled best practices from 25 growth experts at companies including Facebook, Airbnb, Uber, Stitch Fix, Square, Slack, and Instagram.

## When to Invest in Growth

The cardinal rule: do not build a growth team before proving you can retain customers. Investing in growth before retention is proven is "a great way to waste money, resources, and jeopardize the future of your company." If retention is not yet solved, a growth approach can be applied to retention itself -- for example, Stitch Fix hired a retention-focused PM to run experiments improving retention before investing in new customer acquisition.

### The Retention Checklist

Before building a growth team, companies should verify retention through four steps:

1. **Pick the right metrics.** Choose a leading indicator of revenue and repeat behavior, not a vanity metric like app downloads. For marketplaces, measure both supply and demand sides. For Airbnb: "rebook rate" (% of customers that rebook) and "nights booked per user" on the demand side; "active hosts" and "bookings per active host" on the supply side. For Uber: rider retention and trips per active rider; driver retention and trips per active driver.

2. **Pick the right cohort period.** Typically a day, week, or month. Airbnb measures retention annually because travel is low-velocity. Uber measures monthly and weekly because ride frequency is high.

3. **Identify an initial user action.** 100% of the install base takes some action that is a leading indicator for revenue. For Airbnb, this is booking a room for at least one night. For Uber, a first ride.

4. **Identify a follow-on action.** Calculate the percentage still engaging in subsequent periods.

### Good Retention vs. Bad Retention

Three tests determine if retention is good:

1. **Stable long-term retention** parallel to the x-axis (after an expected initial dip).
2. **In line with vertical benchmarks:**

| Vertical | Period | Long Term Period | Long Term Target | Median |
|----------|--------|-----------------|-----------------|--------|
| Social Network | Monthly | Month 12 | 45%-65% | 55% |
| On-Demand | Monthly | Month 12 | 20%-30% | 22% |
| Travel | Annual | Year 2 | 20%-35% | 29% |
| E-commerce | Monthly | Month 12 | 10%-25% | 16% |
| Subscription | Monthly | Month 12 | 25%-35% | 33% |

3. **Newer cohorts perform better** than older cohorts, implying product improvement.

Airbnb is cited as an example of great retention: stable long-term retention, each new cohort performing better than the previous one, and rates exceeding competitors in the travel vertical.

## Building the Growth Team

### Composition and Timing

The typical Year 1 Growth Team: **1 Growth-focused PM + 2-3 Growth Engineers + 1-2 Growth Data Scientists**.

When to hire:
- Most companies made their first growth hire when they had about **15 engineers** on the product team.
- The Growth PM is typically the **3rd or 4th PM** on the team.
- "The most common mistake CEOs make is waiting too long before they hire a growth-focused PM."

The first hires are "magnets" for subsequent hiring and scaling. 100% of experts emphasized this. Eric Colson, former VP of data science at Netflix and early Stitch Fix hire, attracted many accomplished data scientists to Stitch Fix by reputation alone.

Facebook pioneered the growth team model. Its first team had 3 people, formed when Facebook had approximately 50 million MAU with roughly flat month-on-month growth. The growth team "became a key driver of Facebook's rapid expansion to 2 billion monthly active users."

### The Ideal Growth PM

1. **Data-oriented** (must-have): "The scariest day is when numbers are down, the second scariest day is when numbers are up and you don't know why."
2. **Prior growth experience**: Should have worked at a company focused on driving growth in a competitive space (e-commerce, dating, gaming, social). More than 90% of experts cited this. Not from Google or Apple, as "those teams didn't scale based on competitive growth strategies."
3. **Former startup founder** (bonus): 60% of growth experts interviewed were former founders. "People who've started companies tend to be able to think independently, are comfortable with taking risks, and have high levels of perseverance."
4. **Existing PM** (bonus): 40% of growth leads were already PMs at their company. Facebook and Slack both promoted internal PMs. Airbnb and Uber hired externally.

### The Ideal Growth Engineer

1. **Self-starter**: Proactive about generating hypotheses and running experiments.
2. **Comfortable losing code**: "A large amount of work won't make it into the final product."
3. **OK doing things that don't scale**: Engineers with 2-4 years experience may fit better than veterans who "train toward rigid requirements and roadmaps."
4. **Great communicator**: Comfortable working cross-functionally with design, copywriting, data.

### The Ideal Growth Data Scientist

1. **Fluency with experimental design**: Can estimate sample sizes, correct for multiple comparisons.
2. **Coding ability**: Growth requires more data preparation than other data science roles. Test with live pair coding on data cleanup in Python or R.
3. **Great communication**: Must articulate both what can and cannot be validly deduced from experiments, and make the persuasive case for investing in growth initiatives.

## The Growth Team's First Year

### 1. Set an Absolute Goal and Define Key Metrics

Goals must be absolute numbers, not percentage changes. Casey Winters (former Growth Product Lead at Pinterest) [wrote about this](http://caseyaccidental.com/growth-goals). Example: "achieve 5M first-time room nights this year" -- not "improve conversion rates by 10%."

Break the absolute goal into sub-goals. Jonathan Hsu (Social Capital, Facebook's early growth team) shared the [growth accounting equation](https://medium.com/swlh/diligence-at-social-capital-part-1-accounting-for-user-growth-4a8a449fddfc):

- **Airbnb**: Room Nights = Room nights from new users + Room nights from existing users
- **Facebook**: MAU = New MAU + Retained MAU + Resurrected MAU

For marketplaces, set absolute goals for both supply and demand sides. Set the goal halfway between "sandbagging" and "too hard to achieve." 100% of experts said the CEO must be aligned when setting the goal, and it must be communicated to the entire company.

### 2. Identify Growth Channels

Use existing user behavior to identify channels. Aatif Awan (LinkedIn Head of Growth) [outlined this framework](https://www.slideshare.net/tractionconf/aatif-awan-head-of-growth-linkedin-growth-hacking-is-dead-long-live-growth):

| User Behavior | Channels to Explore | Example Companies |
|--------------|-------------------|-------------------|
| Need to connect with another user to use product | Product itself | Facebook, PayPal, Slack |
| Existing users talk about product | Referrals, Community | Uber, Airbnb, Dropbox |
| Use search to find solution | SEO, SEM | Airbnb |
| Look for expert inspiration | Affiliate bloggers, Pinterest, Partnerships, Content | Stitch Fix, Glossier, Intercom |
| High LTV users | Paid acquisition (social, search, native, offline) | Airbnb, Expedia, Uber |

Most products find 1-2 relevant channels early. Approximately 70% of experts said referrals were the top channel in the first year.

### 3. Establish Systems and Tools

Four essential elements:
- **Clean data set** to track key metrics
- **Segmentation tools** for granular customer and activity understanding
- **Rigorous experiment dashboard** tracking results and statistical significance
- **Peer review process** for discussing findings

At scale, a company typically runs **1 experiment per growth engineer per week**. 100% of experts eventually built their own internal tools, though initial tools like [Mixpanel](https://mixpanel.com/), [Optimizely](https://www.optimizely.com/), [Superset](http://airbnb.io/projects/superset/), and [Chartio](https://chartio.com) are common starting points.

Growth teams that run 100+ experiments per year report that only about a third are positive. The 20-30% success rate is intentional -- the exercise encourages engineers to take more risks.

A common heuristic: "Don't test things you wouldn't ship to everybody."

### 4. Establish User Research

Data alone cannot answer all questions. The first 100M users will look very different from the second 100M. Key practices:
- Solicit real-time feedback from users
- Use tools like [Inspectlet](https://www.inspectlet.com/) to track UX
- Meet users outside your first core market (e.g., outside San Francisco)
- Pay attention to international cultural nuances (e.g., "people in Japan do not like to post photos of people without their permission")
- Document every use case

### 5. Continue to Iterate

Tools, processes, and systems evolve at scale. The experiment dashboard, for example, may take many iterations to formalize -- one expert cited it was only formalized after having 25-30 growth engineers.

## Where Should the Growth Team Sit?

This is the biggest source of debate:

- **Separate department** (Facebook model): Growth is its own department, Head of Growth reports to CEO. Facebook's rationale: "if they didn't assign sole responsibility for growth of MAUs, then no one would own it."
- **Merged with product** (Uber, Airbnb, Slack model): Started separate but merged because "growth is not about just looking at data to drive insight" -- the team also makes product changes. Head of Growth reports to Head of Product.
- **Within marketing** (least favored): "The general sentiment about this approach is that the line of reporting is a bit rooted in the past."

Regardless of structure, at scale a growth team can exceed 100 people, composed roughly of: 10% PMs, 50% Engineers, 10-15% Data Scientists, 10% Product Marketing, 10-15% Designers, ~5% Researchers.

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| 59-how-to-set-up-hire-and-scale-a-growth-strategy-and-team | Anu Hariharan, Gustaf Alstromer | Comprehensive guide to building growth teams: retention benchmarks, team composition, experiment frameworks, and organizational structure based on 25 growth experts |
