---
title: Product Development
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["product development", "dev cycle", "product process", "building product", "feature prioritization", "product meetings", "development cycles"]
related: ["[[Michael Seibel]]", "[[Startup Essentials]]", "[[Product-Market Fit]]", "[[Pricing and Monetization]]"]
sources: ["4e-guide-to-product-development"]
speakers_referenced: ["Michael Seibel"]
---

# Product Development

[[Michael Seibel]] describes a product development process that he developed at Socialcam (previously Justin.tv) after years of running a broken process [1]. The broken version had meandering product meetings where decisions were not written down, specs were loose enough that team members had different ideas about what was being built, the team always wanted to build fully-formed products instead of MVPs, analytics were rarely specified for new features, development cycles ran months, and product decisions were made exclusively by founders in a non-transparent process [1].

This guide assumes the company has already shipped an MVP and is figuring out what to do next, which is where most startups spend most of their time [1].

## Define the Development Cycle

The cycle length should be dictated by the product. At Socialcam, building for iOS, the team settled on a two-week cycle, which allowed thorough testing before App Store releases. Web apps can use shorter cycles; hardware might need longer ones. The key constraint is that teammates must stay excited and still feel like they can brainstorm new ideas [1].

## The Product Meeting

Seibel's team ran one and only one recurring team meeting: the product meeting, held on the first day of each development cycle. These meetings sometimes lasted five hours [1].

Every product meeting focused on exactly one of three goals [1]:

1. Increasing content creation
2. Increasing new users
3. Increasing retention

Whichever goal was chosen became the focus of the meeting and the next two weeks. The product lead's role was to protect and improve the development cycle and moderate the meeting to ensure all team members felt comfortable contributing. "Oftentimes just getting the opportunity to voice your idea and having it written on the board -- even if it isn't built -- massively increases buy-in of the process" [1].

## Organized and Inclusive Brainstorm

During brainstorming, ideas were written on the whiteboard in three categories: new features/feature iterations, maintenance, and A/B tests. Everyone was expected to contribute. Debates or putting down other people's ideas was not permitted. This was the time for free contribution without fear of judgment [1].

Each brainstormed item was graded by the engineer in the meeting with the most experience in that specific area [1]:

- **Easy**: Several can be done in a day
- **Medium**: Half a day for one person
- **Hard**: Most of the development cycle

No item could be so hard it would spill into the next cycle. If it was, the team broke it into smaller chunks. This grading system had a critical side effect: it helped non-technical people understand which of their ideas were easy to build and which were hard. "With this realization they often got better at thinking up easier and easier MVPs of their ideas. These easy ideas would then get built and, if they worked, would be iterated upon" [1].

## Building Consensus

The team picked what to work on through consensus, starting with hard ideas (easy to reach consensus because only one could fit), then medium, then easy. Consensus was not difficult because everyone had contributed their own ideas, there was a clear goal, and difficulty estimates were objective. "This process allowed you to grade the quality of your own idea and didn't allow personalities to bully their pet ideas through" [1].

## Clear Spec and Measurements

After consensus, each item was specced in detail, assigned to team members, and paired with the specific stats needed to measure effectiveness. The team would never release a feature without releasing the analytics for that feature and understanding what specific measurable result they wanted to create. Need-to-haves were separated from nice-to-haves; if time ran short, nice-to-haves were dropped [1].

After speccing, the team photographed the whiteboard and erased it. There was no product roadmap outside of these two weeks. Every product meeting started from scratch with a new goal, new analytics data from the last two weeks, and often new insights from monthly in-person user testing [1].

## Working During the Cycle

After the first Monday, work was quiet. The product lead handled business and operations tasks, then dug through Mixpanel looking for product insights or potential bugs, and ran monthly user testing sessions. Engineers and the designer worked quietly on well-scoped, well-specced projects [1].

During the last three days of every cycle, the entire team stopped building and tested. They maintained a testing list in Excel with manual tests for all basic functionality, adding tests for new features each cycle and running all tests twice. Everyone tested, and competitions for fastest testing and most bugs found helped share the burden of an inherently tedious task [1].

## Results

Socialcam did not achieve the team's dream of being the "Instagram for Video" (Seibel notes that what they should have built looks closer to Snapchat). But the process allowed extremely fast iteration: video filters, borders, titles, soundtracks, feed optimizations, multiple visual redesigns, user profiles, recommended channels, front/back camera switching, and more. Growth experiments produced 16 million downloads in about three months and over 100 million people watching video on their website during the same period. The work was done "quickly, efficiently, without major arguments, issues with founder commitment, or really any team problems at all" [1].

## References

1. [Guide to Product Development](https://www.ycombinator.com/library/4e-guide-to-product-development) — [[Michael Seibel]] (August 2016)
