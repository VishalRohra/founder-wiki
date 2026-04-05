---
title: Product Development
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["building product", "feature prioritization", "MVP", "iteration", "shipping", "two-week cycles", "dev cycle", "product meetings", "feature development"]
related: ["[[Growth]]", "[[Product-Market Fit]]", "[[Feature Prioritization Frameworks]]", "[[Talking to Users]]", "[[Startup Mistakes]]"]
sources: ["4e-guide-to-product-development", "8p-how-to-prioritize-features", "4p-before-growing-your-startup"]
speakers_referenced: ["Michael Seibel", "Emmett Shear", "Sam Altman"]
---

# Product Development

Product development in startups requires structured iteration, clear measurement, and disciplined prioritization. The advice converges on a common theme: build small, measure everything, and let user behavior guide decisions.

## The Development Cycle

[[Michael Seibel]] describes a product development process he refined at Socialcam after years of dysfunction at [[Justin.tv]]. Before developing this process, the team suffered from several problems: meandering product meetings without written decisions, poorly specced products where team members "often had slightly different ideas about what we were building," always wanting to build fully-formed products instead of MVPs, rarely speccing analytics, and development cycles that ran months.

### Setting the Cycle Length

The development cycle should be dictated by the product. At Socialcam, building for iOS, they settled on a **two-week cycle** that allowed thorough testing before App Store releases. Web apps can go shorter. Hardware may need longer. The key constraint: "structure the cycle so that teammates stay excited and still feel like they can brainstorm new ideas."

### The Product Meeting

Seibel ran one and only one team meeting: the product meeting on the first day of each dev cycle. "Sometimes this meeting would go for five hours."

Every meeting focused on one of three goals:
1. Increasing content creation
2. Increasing new users
3. Increasing retention

Whichever goal was chosen became the focus for the next two weeks.

### Organized Brainstorming

Ideas were written on a whiteboard in three categories: **new features/feature iterations**, **maintenance**, and **A/B tests**. Everyone contributed. "Debates or putting down other people's ideas wasn't permitted. This was the time when everyone felt free to contribute without fear of judgement."

Each item was then graded by the most relevant engineer as:
- **Easy**: Several can be done in a day
- **Medium**: Half a day for one person
- **Hard**: Most of the dev cycle

No item could be so hard it would spill into another cycle -- if it was, it got broken into smaller chunks. This grading had a secondary benefit: "This really helped non-technical people understand which of their ideas were easy to build and which were hard. With this realization they often got better at thinking up easier and easier MVPs of their ideas."

### Building Consensus and Speccing

The team picked items by consensus, starting with hard items (easy to agree on since only one could be done), then medium, then easy. Each item got a detailed spec, an assigned owner, and defined analytics to track. "We would never release a feature without releasing the analytics for that feature and understanding what specific measurable result we wanted to create."

Features were separated into need-to-haves and nice-to-haves. After the meeting, they photographed the whiteboard and deleted it. "We didn't have a product roadmap outside of these two weeks and every product meeting we would start from scratch."

### During the Cycle

After the first Monday, work was quiet. Seibel focused on business/operations tasks, then dug through Mixpanel for product insights or bugs, and ran monthly user testing sessions. Engineers and designers worked on their well-specced projects. During the last three days, all building stopped for testing: "We had a testing list in Excel that included manual tests for all of our basic functionality. Every cycle we added tests for new features built in that cycle and we tested all items on our testing list twice. Everyone on the team tested and we often had competitions for who could test the fastest and who found the most bugs."

### Results at Socialcam

The process enabled rapid iteration: video filters, video borders, video titles, video soundtracks, feed optimizations, multiple visual redesigns, user profiles, recommended channels, front-back camera switching, and more. Growth experiments produced 16 million downloads in about 3 months and over 100 million people watching video on the website in the same period. Seibel notes: "Most importantly though, we did all of this work quickly, efficiently, without major arguments, issues with founder commitment, or really any team problems at all."

## Feature Prioritization Frameworks

[[Emmett Shear]], drawing from his experience building [[Justin.tv]] and [[Twitch]], identifies three mental frameworks for feature prioritization. Startups typically progress through them in order as their challenges shift.

### 1. Built For Me

The founder is the primary exemplar user of their own product. "Deeply introspect and figure out what you wish it did instead. Build that."

When it works best:
- When you truly love your product. Shear managed the viewer side of Twitch this way "for a long time, because I really do love watching Twitch."
- For small teams. "It's hard to communicate intuitive introspective understanding to other people."
- When you have good intuitive access to your desires. Shear warns: "I think I want this because it's what I believe I'm supposed to want" feels subjectively identical to "I want this" because human introspection is unreliable.

This framework explains why many of the biggest startups started with the Built For Me approach: "It gives you an automatic advantage against big incumbents who can't use the same method." Big companies can only use this when the CEO is the lead designer, like Steve Jobs at Apple.

### 2. Switch To Us

People are already doing the behavior you want elsewhere. The goal is to get them to do it with you instead.

Process:
- Interview 5-6 dedicated users each from your service, each competing service, and closely-adjacent services.
- Categorize and score responses in a spreadsheet.
- Look for patterns. Consider "doubling down on your strengths, and shoring up obvious weaknesses."
- Target one competitor at a time.

The critical insight: "The key to running effective interviews is to use the interviews to understand the problem, and based on what you learn to generate ideas for solving it. Validating an idea you already have is an anti-goal." You cannot improve an idea through validation. The goal is to have better ideas.

When it works best:
- When your product is very important to customers. "Streamers on Twitch have strong opinions about what makes a good streaming service that they can articulate very clearly."
- When you are selling "a better mousetrap, rather than inventing the mousetrap category."

Shear provides specific interview questions for this framework (see [[Feature Prioritization Frameworks]]).

### 3. Three Numbers Matter

Identify the three most important qualities of the product for your customer. All feature decisions flow from these.

- **Amazon**: Lower prices, more selection, faster/more reliable shipping.
- **Twitch**: Audience size, positive interactions, money.

"Three is a magic number for focus. Empirically, three seems to be the maximum number of focus areas that people can keep in mind consistently." A bonus fourth area -- "Stuff You Have To Do" (PCI compliance, uptime) -- is necessary but should not be in the top three.

The approach is recursive: each of the three top-level metrics can be decomposed into three sub-drivers. Split investment by intuition -- "maybe it's 33/33/33, maybe it's 50/25/25."

When it works best:
- When people choose your product for measurable reasons (price, audience size, speed).
- Less effective when people choose for hard-to-measure reasons (fun, connection, community).

Shear notes that Twitch still periodically returns to Switch To Us for new customer segments: "as we started working to launch our new music category, we started talking to artists who livestreamed elsewhere online."

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| 4e-guide-to-product-development | Michael Seibel | Two-week dev cycles at Socialcam: organized brainstorms, consensus-based prioritization, mandatory analytics, no roadmap beyond two weeks |
| 8p-how-to-prioritize-features | Emmett Shear | Three frameworks -- Built For Me, Switch To Us, Three Numbers Matter -- that startups progress through as they grow |
| 4p-before-growing-your-startup | Sam Altman | Build a product people love before optimizing for growth; don't paper over a mediocre product with capital |
