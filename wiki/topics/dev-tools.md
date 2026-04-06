---
title: Dev Tools
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["dev tools", "developer tools", "dev tool startup", "developer tools company", "API startup", "open source startup", "developer marketing", "selling to developers"]
related: ["[[Sales for Founders]]", "[[MVP Planning]]", "[[Launching]]", "[[Doing Things That Don't Scale]]", "[[Pricing and Monetization]]", "[[Nicolas Dessaigne]]", "[[Diana Hu]]", "[[Growth]]"]
sources: ["Lu-how-to-start-a-dev-tools-company"]
speakers_referenced: ["Nicolas Dessaigne"]
---

# Dev Tools

Dev tools are software that developers use to build products -- covering coding, testing, debugging, documenting, deploying, and running applications [1]. The category includes IDEs (VSCode), APIs (Stripe, Twilio, Algolia), libraries and frameworks (React, Next.js, LangChain), infrastructure (AWS, Vercel), and workflow tools (Docker, Terraform, DataDog, GitHub) [1]. [[Nicolas Dessaigne]], former CEO of Algolia and YC Group Partner, provides the comprehensive guide to building a dev tools company [1].

YC has funded hundreds of dev tools companies, including two that became public (GitLab, PagerDuty) and many others: Stripe, Docker, Heroku, Supabase, Segment, PlanetScale, and Apollo [1].

## Founding Team

The founding team for a dev tool should be technical. The product is built for developers, so the founders must be developers [1]. Dessaigne provides a striking statistic: 74% of YC dev tool companies had only technical co-founders, compared to 45% for all other YC companies [1].

A common mistake is thinking the team needs a business co-founder. Dessaigne's own experience at Algolia: "We ended up creating Algolia with two tech co-founders. But it crossed our mind: 'Hey, we don't know how to sell.'" They did not need one. Learning to sell a dev tool is easier than learning to speak the language of developers [1].

## Good vs. Bad Ideas

### Build Time vs. Runtime

The distinction between build-time and runtime ideas is one of the most important filters for dev tool startups [1].

**Build-time ideas** (docs, QA, testing) are tools used when building software. They are "mostly nice to have. You could build your product without them." These are also the most obvious ideas -- every developer encounters them daily -- which creates a crowded market [1].

**Runtime ideas** are tools that run in production. They are "must-have products. If you bet on an API, for example, you cannot run your own product if it's down." Runtime ideas also have a natural usage-based growth dynamic: as customers grow, they use more of the product. "Think about Stripe. If their customers sell more products, they make more money. Everyone is happy" [1].

### Libraries and Frameworks

Libraries and frameworks can be great but are challenging to monetize. Pandas, for example, is widely used but very difficult to make money from. The main monetization path is a hosting service: Next.js and Vercel illustrate this model [1].

### The AI/LLM Wave

The LLM wave has created many new dev tool opportunities, but also extreme noise. LLM observability is the obvious example: "Anyone building with LLMs, they want to know how they are doing. They want to be able to evaluate them. Guess what? Many other companies think the same thing" [1]. Dozens to hundreds of such companies exist. Starting in a crowded space is not fatal, but founders need a clear differentiation plan [1].

A counterpoint: "With the advent of LLMs and AI in general, it's actually very difficult to know for sure today what's a good or bad idea. The bad ideas, the ideas of yesterday, could actually be possible to make successful now thanks to LLMs" [1].

### Common Idea Mistakes

1. **Waiting for the perfect idea.** "You are going to wait for a very long time." Start, learn, and iterate. "You learn as you go, and eventually you'll be able to pull it off. Or you'll change your idea" [1].
2. **Sticking with the wrong idea too long.** 50% of YC companies pivot from their first idea, and this is also true for dev tools [1].
3. **Thinking you need a business founder.** See above [1].

## Building: Prototype to MVP

The two activities at this stage are building and talking with users, in no particular order [1].

### Don't Over-Engineer

"The most important thing here is not to over-engineer it. You should do that quick and dirty" [1]. Dessaigne acknowledges this is hard for experienced engineers who pride themselves on robustness. But the reality: "I would assume that you'll throw away 90% of all the code you write. So your goal at that stage is just to identify the 10% of what you're building that's actually valuable" [1].

### Start Narrow

"It's much better to be 10x better on a very tiny thing for someone who cares about it. Working for a niche is completely okay" [1].

Algolia started as "a glorified autocomplete. Very minimal." The first customer demo used a command line to index content -- no API client, no admin UI, "just a command line and then a very simple webpage to show the search." That was enough to close a $2,000/month contract [1].

### Talk to Users Early

Developers are often introverts who dislike sales. Dessaigne reframes this: "You are a developer yourself. You speak the language of your customers. You are uniquely qualified to understand them" [1]. Do not wait for the product to be ready. "Right away, if you are solving a real problem, then people will be ready to pay for it" [1].

### Finding Users: Outreach and Launches

Nobody knows a new dev tool exists, so inbound will not work initially [1]. Two approaches:

**Outreach:** Start with your network (colleagues, classmates), then expand to friends of friends and LinkedIn. Personalize messages. "Ask yourself: would you be excited to open your message?" [1]. See [[Sales for Founders]].

**Launches:** The best place to launch a dev tool is Hacker News, specifically the "Show HN" section [1]. The key: "Don't do marketing. Don't try to sell your product. Just explain plainly and simply what's new and interesting in what you are building" [1]. Engage with comments, including hostile ones. "Your goal is not to convince them. It's just to convince any other readers who are going to read how you reply to these haters" [1].

**Segment** validated its idea by launching on Hacker News. The post blew up with hundreds of votes and comments, confirming they were onto something [1]. **Ollama** started as a comment on another HN post, attracted interest, then launched its product to massive engagement. They launched again and again every few months: "Each time they had new things to share. And that continued to fuel their growth" [1].

### Common Building Mistakes

- Choosing a tech stack because it is cool rather than because the team is fast with it [1]
- Not talking with users [1]
- Overbuilding before getting feedback [1]
- Misunderstanding developer feedback. If users say "I could build this in a week," ignore it -- "You just built it yourself in a week. You shouldn't mind about that" [1]
- Hiring too early. "Please don't hire anyone until you have convinced yourself you're working on the right idea" [1]

## Open Source as Go-to-Market

Open source is one of the main go-to-market strategies for dev tools [1].

### When You Must Be Open Source

- **Libraries and frameworks.** "Developers wouldn't implement on top of a new framework that is not open source" [1]
- **Products dealing with sensitive data.** A new database or an API connecting to CRM or EHR data needs to be open source [1]

### When Open Source Is Optional

APIs and applications (like bug trackers) do not necessarily need to be open source, though it can serve as differentiation: "You could be the open source version of X" -- PostHog vs. Amplitude, Supabase vs. Firebase, Airbyte vs. Fivetran [1].

### Benefits of Open Source

- Developers prefer open source tools [1]
- Creates community awareness [1]
- Can be a differentiation strategy [1]
- Community contributions (though Dessaigne warns: "Good contributions are actually pretty rare" and managing contributors can be more work than expected) [1]
- Trust, especially with enterprises. Med Plum, an open-source EHR, likely shortened its enterprise sales cycle by a year or more through being open source [1]

### Monetization

Open source must be monetized eventually. Three common approaches [1]:

1. **Hosting/Cloud.** Free self-hosted version, paid cloud version with additional features like team management [1]
2. **Open Core.** An enterprise tier with advanced features not in the open source version: SSO, OAuth, disaster recovery, SLAs [1]
3. **Support and Services.** Dessaigne discourages this: "Your incentive becomes to build the most complex product possible so you can charge for support and services, which is a bad incentive" [1]

### Pricing for Non-Open-Source Dev Tools

Two approaches [1]:

- **Usage-based** (like APIs). Algolia and Stripe charge based on customer usage, with possible volume discounts [1]
- **Good/Better/Best tiers.** "Good" is self-serve for individual developers (low price). "Better" targets engineering managers who care about collaboration (self-serve, team features). "Best" targets CTOs and requires sales -- security, audit logs, SLAs [1]

## Developer Marketing

The goal is awareness that drives inbound [1].

### Find Your Community

Hacker News, relevant subreddits, Discord servers. "Your goal is not to sell your product just yet. Here, just be helpful. Just establish yourself as the expert" [1].

### Launch Repeatedly

Supabase runs "launch weeks" once a quarter, concentrating all news into one week to maximize noise [1].

### Documentation Is Marketing

"Documentation should never be an afterthought. It should be part of the product. Documentation is marketing" [1]. Stripe raised expectations industry-wide. "Developers have become very demanding" [1].

At Algolia: "A feature was not ever done until the docs were done. And documentation should be written by developers" [1]. The documentation team's role was to help developers write better docs, not to write docs for them. They built tools that automatically inserted API keys for logged-in users so copy-pasted code worked immediately [1].

### Support Is Marketing

"Engineers should do support" [1]. Two benefits:

1. Developers interacting with other developers who speak their language are more satisfied. "I have examples where someone would reach out to support, and then the developer doing the support was able to actually fix the bug and deploy in production in like 20 minutes" [1].
2. Engineers doing support better understand customer needs [1].

Algolia waited until they had hundreds of employees before building a dedicated support team, and then asked their best engineering manager to lead it [1].

### Developers Should Do Marketing

Dessaigne's most provocative claim: "I don't know a single dev tool company that is happy with their CMO when they have a traditional marketing background" [1]. Traditional marketers do not understand developers. "Developers really hate being marketed to" [1].

At Algolia, every engineer did a "marketing hack" every month: writing a blog post, speaking at a meetup, or building a hack [1]. "All of our best marketing at Algolia was done by developers" [1].

On developer advocates: the concept is sound (developers in the marketing team) but the role is "ill-defined with often a lot of very fuzzy expectations." Wait until Series A or later, and hire from within or from the community -- contributors or active Discord members make the best candidates [1].

## References

1. [How To Start A Dev Tools Company](https://www.ycombinator.com/library/Lu-how-to-start-a-dev-tools-company) -- [[Nicolas Dessaigne]] (2024)
