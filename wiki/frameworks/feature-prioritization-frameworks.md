---
title: Feature Prioritization Frameworks
type: framework
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["feature prioritization", "what to build next", "product prioritization", "Built For Me", "Switch To Us", "Three Numbers Matter"]
related: ["[[Growth]]", "[[Product-Market Fit]]"]
sources: ["8p-how-to-prioritize-features"]
speakers_referenced: ["Emmett Shear"]
---

# Feature Prioritization Frameworks

[[Emmett Shear]], co-founder of Justin.tv and Twitch, describes three mental frameworks for deciding what to build next. In his experience, startups progress through each framework in order as the type of challenge shifts [1].

Justin.tv started as a "Built For Me" product -- the founders wanted to make a live reality TV show and built the underlying technology for themselves. Twitch began the same way, as the only part of Justin.tv Shear personally enjoyed was video game streaming. When Twitch development started in earnest, the approach shifted to "Switch To Us" because the primary customers were streamers and Shear was not a streamer. Later, Twitch developed a "Three Numbers Matter" approach that drove most subsequent development [1].

## Built For Me

The founder is the primary exemplar user of the product. Deeply introspect and figure out what you wish the product did. Build that [1].

**When it works best:**
- When the founder truly loves the product. Shear managed the viewer side of the Twitch experience this way because he genuinely loved watching Twitch [1].
- With small teams. Intuitive, introspective understanding is hard to communicate to others. A small team inside a big company can use it, but a medium-sized organization cannot easily align on it [1].
- When the founder has good intuitive access to their desires. Some people want what they "should" want rather than what they actually want. Human introspection is unreliable -- "I think I want this because it's what I believe I'm supposed to want" feels subjectively identical to "I want this" [1].

**Why it gives startups an advantage:** Big companies cannot easily use this method because it does not scale. This explains why many of the biggest startups started with Built For Me -- it provides an automatic advantage against large incumbents. The ongoing popularity of "hack weeks" within large organizations is an attempt to unleash the Built For Me capacity latent in the organization by reverting to a more startup-like approach with small teams and intuitive decisions [1].

## Switch To Us

People are already doing the behavior the product enables, using competitors. The goal is to get them to do it with your product instead [1].

**The method:**
1. Interview 5-6 dedicated users each from your service, each competing service, and closely adjacent services
2. Accumulate approximately 50 interviews
3. Categorize responses and score them in a spreadsheet
4. Look for patterns. Consider doubling down on strengths and shoring up obvious weaknesses
5. Target one competitor at a time
6. Prioritize things that can be built or changed fast -- customers do not care how hard something is to build, only how effective it is for their problem [1]

**The critical principle for interviews:** Use interviews to understand the problem and generate ideas for solving it. "Validating an idea you already have is an anti-goal. You can't improve an idea through any amount of validation" [1]. The goal is to have better ideas as much as to prioritize them. If ideas are generated from customer problems and opportunities, both quality and intuitive prioritization improve [1].

**When it works best:**
- When the product is important to customers and they can articulate their needs. Twitch streamers had strong opinions about streaming services and could weight tradeoffs like "prosumers" or "SMBs." This would not work for something like Snapchat, where users may have no idea what they specifically like about it [1].
- When selling a better mousetrap, not inventing the category. Twitch was a better mousetrap for streamers on other platforms. It would not have worked for Justin.tv when there were no existing live streamers because they were the first live streaming service [1].

**Good interview questions:**
- What do you like about your current solution?
- What do not you like about it?
- How did you choose your current solution?
- What were you doing before?
- What would you do if you were the CEO of the company whose product you are using?
- What is the single most annoying thing about your current solution?
- What is the single coolest new thing about your current solution?
- Is there anything that would convince you to switch to us immediately if we built it?
- If you had a magic wand and could create any experience you wanted, how would it work?
- What is one thing about your current solution that is surprisingly hard?
- Follow up with "interesting, tell me more" or "why is that?" as appropriate. "People know more than they think they do, they just need a good interviewer to draw it out of them" [1]

## Three Numbers Matter

There are a few key drivers that make using the product better or worse. Identify the three most important and focus the entire organization on moving them [1].

**Examples:**
- **Amazon**: lower prices, more product selection, faster/more reliable shipping. Ideas that move those three numbers get priority [1].
- **Twitch**: audience size, positive interactions, money. Twitch focuses on helping streamers grow their audience, interact in more fun and connected ways, and earn more money per viewer [1].

**Why three:** "Three seems to be the maximum number of focus areas that people can keep in mind consistently." A list of "X, Y, and Z" feels natural; "W, X, Y, and Z" does not [1].

**The bonus fourth area: Stuff You Have To Do.** PCI compliance, uptime, security -- things that are not company focus areas but will kill the company if neglected. These should be done but not included in the top-level three metrics [1].

**The recursive property:** Each of the three top-level metrics can be further decomposed into three sub-drivers, and so on. Start with a metric for each area (these evolve -- revisit every few months), choose a resource split by intuition (maybe 33/33/33, maybe 50/25/25), and start trying to move the numbers [1].

**When it works best:**
- When people choose the product for measurable reasons (price, audience size, speed)
- Poorly suited for difficult-to-measure reasons (fun, connection, love, community). "Good for making utilitarian things, less good for making games and toys and beautiful UX" [1]

**Operational excellence:** Important for every company, but for a startup, winning through pure operational excellence is rare. Usually, the startup needs "good enough" operational excellence while focusing on what customers really care about. Sometimes one aspect of operational excellence (low latency, high security, super reliability) becomes a key goal, but even then most aspects should run on a "good enough" basis early on [1].

## Transitions Between Frameworks

Twitch periodically returned to Switch To Us for new customer segments even while running primarily on Three Numbers Matter. When launching a music category, the team talked to artists who livestreamed elsewhere to understand their needs. As the category grew, they began identifying key metrics and transitioning back to Three Numbers Matter [1].

## The Hard Problem

Certain products do not fit any framework: a brand-new category, where people like the product for hard-to-measure reasons, and the founder is not the end user. "It's really really hard!" [1]. This constrains big companies more than small ones because Built For Me does not scale. Big companies end up working on products with easily measurable drivers, or on incremental innovation. The exception is when the CEO is the lead designer (Steve Jobs at Apple) -- a big company escaping the dilemma to do ground-breaking category creation for products that are great for hard-to-measure reasons [1].

## References

1. [How to Prioritize Features](https://www.ycombinator.com/library/8p-how-to-prioritize-features) -- [[Emmett Shear]] (n.d.)
