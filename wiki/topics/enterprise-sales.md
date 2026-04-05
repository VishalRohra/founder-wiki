---
title: Enterprise Sales
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["enterprise sales", "selling to enterprises", "B2B sales", "enterprise deals", "elephant hunting", "complex sales", "founder-led sales", "sales funnel", "enterprise sales funnel"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[Series A Fundraising]]", "[[Scaling and Later-Stage Operations]]", "[[B2B Pricing]]", "[[Pete Koomen]]", "[[Dalton Caldwell]]", "[[Michael Seibel]]"]
sources: ["4m-enterprise-sales-for-hackers", "LF-enterprise-sales-for-founders"]
speakers_referenced: ["Ryan Junee", "Pete Koomen", "Dalton Caldwell", "Michael Seibel"]
---

# Enterprise Sales

Enterprise sales is a learnable skill. Two complementary perspectives in the YC canon address it: Ryan Junee's essay frames enterprise selling as "hacking the enterprise" -- understanding and influencing the people-system that makes up a large organization [1]. [[Pete Koomen]], co-founder of Optimizely (which reached $100M ARR), provides a step-by-step walkthrough of the enterprise sales funnel for technical founders [2]. The consensus across both: founders must sell the product themselves before hiring salespeople, and sales is fundamentally about understanding customer problems, not psychological tricks.

## Founders Must Sell First

Koomen states this directly: "If you're the founder of an early-stage startup and you're building a product that you're hoping other businesses will buy, you are capable of selling it. The bad news is that you're probably the only person capable of selling your product" [2]. The reasoning: sales before [[Product-Market Fit]] is fundamentally entrepreneurial. It requires vision, credibility with customers, experimentation, and a tight feedback loop with the product team. This is a founder's role [2].

Technical founders have two advantages that give them a leg up in selling: they are experts in both the problem and the product, and they have genuine conviction that the product solves the customer's problem. "Expertise and conviction are surprisingly important in sales. This is especially surprising to people who mistakenly think that selling is a dark art full of psychological tricks" [2].

[[Dalton Caldwell]] and [[Michael Seibel]] reinforce this from the co-founder angle: if no one on the founding team considers it their job to do sales, no sales will happen. A technical person is fully capable of sales -- it requires "general intelligence," not specialized business training [3].

## The Sales Funnel

Koomen walks through six stages: prospecting, outreach, qualification, pricing, closing, and implementation [2].

### Prospecting

Prospecting means finding potential customers. The output is a list of companies likely to need your product and the specific humans who might buy it [2].

Start with a sales hypothesis: "Customer X has problem Y, and our product will help them solve it." At Optimizely, the hypothesis was: "Marketers at small and medium tech, media, and e-commerce companies want to run A/B tests on their websites but can't because off-the-shelf experimentation tools require users to write code" [2].

Use tools to identify target companies. Optimizely used Builtwith to check whether prospects used analytics tools and JavaScript frameworks -- signals of web sophistication [2]. For contact information, Apollo and LinkedIn Sales Navigator are common in recent YC batches [2].

### Outreach

The goal of outreach is to schedule a meeting. The easiest path is to get prospects to reach out to you: launch early and often, create technical content prospects find while searching for solutions, build self-served demos, and establish expertise in online forums where customers congregate [2].

For cold emails, Koomen advises writing each email by hand, keeping them short and specific, and making the ask clear. "Only send emails that you yourself would be excited to read" [2].

A critical anti-pattern Koomen flags: talking to anyone who will take your call. This selects for people who are easiest to talk to, not people who will be great customers [2]. Founders make this mistake in two specific ways:

1. **Selling enterprise software to startups.** Other startups are easy to talk to but often do not have the problem your product solves at their scale [2].
2. **Going bottom-up with a top-down product.** If deploying your product requires coordination across multiple teams (e.g., hospital software), talking to individual contributors is futile. You need to talk to a senior leader with decision-making authority [2].

"Talking to bad customers gives you the illusion that you're making progress when you're not" [2].

### Qualification

On the first call, the goal is not to sell but to qualify the prospect and schedule a demo [2]. The biggest mistake founders make is diving straight into a pitch instead of asking questions [2].

Questions to ask: What made you decide to take this call? How long have you had this problem? How bad is it? How do you quantify the impact? Why haven't you solved it already? What's your budget? How does your organization buy software? Who makes the buying decision? [2]

If the prospect lacks the problem, budget, or authority, that discovery saves time. "You just saved yourself and your prospect a lot of time" [2].

### Demos

Most founders think of a demo as a chance to show off the product. Koomen frames it differently: "Your job in a demo is not to show off your product. It's to convince your audience that you can help them solve their problem" [2].

Structure a demo like a movie script: start by recapping who the main character (user) is and the problem they face. This demonstrates how well you listened. Then tell a story showing exactly how the user solves their problem -- not a feature tour [2].

Great demos have "magic moments" where you surprise the audience with how easy or delightful something is. They are personalized: use the customer's logo, website, customer names, and team member names [2].

At Optimizely, competitors demoed on generic websites. Koomen and his co-founder Dan spent weeks building a feature that let them demo right on the customer's own website. "I knew it was worth it when I saw a marketer's eyes light up when they watched us change things on their landing page that would have taken them months to do on their own" [2].

### Closing

Closing is not a single conversation but a series of steps from decision to signature [2]. Big companies have formal procurement processes: security reviews, legal reviews, compliance sign-off. The biggest mistake is getting surprised that a seemingly done deal requires weeks more work [2].

Ask upfront how the company buys software and who needs to sign off. Execute steps in parallel where possible. Keep legal documents simple -- Koomen recommends open-source templates from YC company Common Paper [2].

The champion is your biggest ally at this stage. "They can't solve their problem until you get through procurement, so they're heavily incentivized to help you make it happen" [2].

### Implementation

"The single biggest mistake that founders make is thinking that implementation is the customer's job" [2]. At Optimizely, they closed six-figure deals where customers hadn't run a single A/B test a year later because marketing couldn't convince engineering to install the code [2].

The lesson: customers buy a solution to a problem, not a product. All work required to get from product to solution is the seller's responsibility. Treat implementation like a high-priority internal project: shared roadmap, task owners, regular check-ins [2].

"Your sales funnel only really ends when your customer is using your product habitually" [2].

## The People in the Enterprise System

Junee maps out the typical roles a founder encounters inside a target enterprise [1]:

### Champion

An ally with deep familiarity with the pain the product solves. "When you give your pitch, you will find the champion nodding along and completing your sentences for you" [1]. Their influence depends on seniority -- director-level and above are necessary. Champions sometimes want to quit and join the startup. "These people are gold. Find them early and build strong relationships quickly" [1].

### Detractor

Opposes deployment because it threatens their job, they are invested in a competing product, or they built the current solution. Strategy: stay off their radar and rally enough support from champions to overpower them [1].

### IT

Two types: risk-avoidant (far more common) and forward-thinking. Avoid IT until required for security reviews. By then, business units should be "pulling" so strongly that IT cannot slow things down [1]. Do not build features IT requests without validating with actual users [1].

### Procurement

After a decision maker agrees to buy, procurement negotiates the deal. "Make sure you are prepared to 'give' them something -- once they extract their pound of flesh they will get out of the way" [1]. This dynamic is why enterprise software has high list prices with 80%+ discounting as standard [1].

### Legal

Legal's weapon is "exhaustion -- sending back endless redlines over clauses that in reality won't have much impact" [1]. Decide upfront what matters and concede the rest. Combined with champion pressure, this closes negotiation [1].

### Finance

Finance thinks about budget cycles. They may prefer upfront payment to use a quarter's budget. Understanding capex vs. opex preferences affects pricing model [1].

## Hiring Salespeople

Junee advises optimizing for skills and raw characteristics over experience in early-stage sales hires. A "coin-operated" salesperson from a large company -- someone accustomed to existing playbooks -- is a "script kiddie" rather than a hacker. You need someone comfortable with uncertainty who can learn quickly [1].

Koomen adds that sales hiring only makes sense once the founder has closed deals and can articulate a repeatable process. A salesperson should generate 5x their total compensation in new ARR [4].

## References

1. [Enterprise Sales for Hackers](https://www.ycombinator.com/library/4m-enterprise-sales-for-hackers) -- Ryan Junee (n.d.)
2. [Enterprise Sales for Founders](https://www.ycombinator.com/library/LF-enterprise-sales-for-founders) -- [[Pete Koomen]] (2024)
3. [Do Technical Founders Need a Business Co-Founder?](https://www.ycombinator.com/library/KV-do-technical-founders-need-a-business-co-founder) -- [[Dalton Caldwell]], [[Michael Seibel]] (2023)
4. [How To Price For B2B](https://www.ycombinator.com/library/LI-how-to-price-for-b2b) -- [[Tom Blomfield]] (2024)
