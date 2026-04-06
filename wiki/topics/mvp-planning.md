---
title: MVP Planning
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["MVP", "minimum viable product", "planning an MVP", "building an MVP", "MVP spec", "lean MVP", "heavy MVP", "how to plan an MVP"]
related: ["[[Simple Products]]", "[[Launching]]", "[[Talking to Users]]", "[[Product-Market Fit]]", "[[Doing Things That Don't Scale]]", "[[Michael Seibel]]", "[[Diana Hu]]", "[[Product Development]]"]
sources: ["6f-how-to-plan-an-mvp", "Is-tips-for-technical-startup-founders"]
speakers_referenced: ["Michael Seibel", "Diana Hu"]
---

# MVP Planning

The minimum viable product is the first thing a startup can give to the very first set of users it wants to target, in order to see if it can deliver any value at all [1]. [[Michael Seibel]] defines it as "something ridiculously simple" and frames the entire prelaunch startup process as four steps: launch quickly, get initial customers, talk to users and get feedback, and iterate [1]. [[Diana Hu]] extends this with a three-stage model for technical founders: prototype (days), MVP (weeks), and launch-to-iterate (ongoing) [2].

## The Goal of a Prelaunch Startup

Seibel distills the prelaunch phase to four sequential steps [1]:

1. **Launch quickly.** "If you can walk away from one thing from this presentation, it's launch something bad, quickly" [1].
2. **Get initial customers.** Get anyone using the product. "You'd be surprised at how many founders' journeys end before a single user has actually interacted with a product they've created" [1].
3. **Talk to users and get feedback.** The common mistake is thinking feedback on a half-built product is useless because "the full thing" has not been built yet. Seibel's response: "Hold the problem you're solving tightly, hold the customer tightly, hold the solution you're building loosely" [1].
4. **Iterate.** Iteration means improving the solution for the same user and problem. It does not mean finding new problems for the existing solution. Seibel uses the screwdriver metaphor: "If your screwdriver doesn't help the mechanic solve the problem, keep the mechanic, keep the problem, I need to screw something in, fix the fucking screwdriver" [1].

## Lean MVP vs. Heavy MVP

Most startups should build a **lean MVP** [1]:

- Buildable in weeks, not months
- Extremely limited functionality
- Focused on a small set of initial users and their highest-order problems
- A base to iterate from, not a finished product

Seibel illustrates with three billion-dollar companies [1]:

**Airbnb (2008):** No payments -- guests exchanged money with hosts in person. No map view. The sole coder, Nate Blecharczyk, was working part-time [1].

**Twitch (as Justin.tv):** Only one channel -- Justin Kan's life. If you did not like watching his life, you had to leave the website. Video was extremely low resolution. No video games, except when the founders happened to play them in their apartment [1].

**Stripe (as /dev/payments):** No bank deals. Almost no features. The founders would come to your office and integrate it for you -- "half because they were just desperate to get anyone to use it, and half because it was a great way to find bugs before the users found bugs" [1]. See [[Doing Things That Don't Scale]] for more on the Collison installation.

A **heavy MVP** applies when regulation, hard tech, biotech, or moonshot physics make a quick build impossible [1]. Even then, Seibel argues the MVP can start with a simple website explaining what the company does: "That can be your start, and you can build that simple website in days, not weeks" [1].

## The Prototype Stage (Diana Hu)

Diana Hu separates the prototype from the MVP [2]. The prototype is built in days, not weeks, with the singular focus of having something to show and demo to users. It does not need to fully work [2].

Examples of prototypes [2]:

- **Software companies:** A clickable Figma or Invision prototype
- **Dev tools:** A script written in an afternoon, launched on the terminal
- **Hardware/hard tech:** 3D renderings that show the promise of the product. Remora, a carbon capture device for trucks, used a 3D rendering that was enough to get users excited [2]
- **Optimizely (Winter '10):** Pete Koomen and Dan Siroker built a prototype in a few days. It was the first visual A/B test editor -- a JavaScript file on S3. "Literally just opened Option-Command-J in Chrome" and ran the test manually. Nobody could use it except the founders, but it was enough to show marketers and get them excited [2]

The common mistake at this stage is overbuilding. Hu warns against founders who say "users don't see it, or it's not good enough" and try to build a full MVP when a prototype is sufficient [2].

## Building the MVP (Diana Hu)

Once the prototype validates interest, the MVP stage focuses on building something that gets commitment -- ideally payment -- from users [2]. Hu provides three principles:

### 1. Do Things That Don't Scale

Find clever hacks to launch quickly [2]. The things to avoid: automatic self-onboarding, scalable back-ends, and automated scripts. The hacks to embrace: manually editing the database to add users, providing insane custom support, processing requests by hand. Stripe's founders literally filled bank forms manually to process payments at launch [2]. See [[Doing Things That Don't Scale]].

### 2. Create a 90/10 Solution

Coined by Paul Buchheit (creator of Gmail and YC group partner), the 90/10 solution means restricting the product to work on limited dimensions -- limited situations, data types, functionality, user types, device types, or geography [2]. The first version will be rewritten. Push off features to post-launch.

Hu uses DoorDash as the canonical example. Built in one afternoon as "Palo Alto Delivery," the entire front end was static HTML, CSS, and PDF menus. The back end was Google Forms and Google Docs. Driver tracking used Find My Friends on iPhone. By constraining to Palo Alto, the founders got delivery and unit economics right in the suburbs before expanding -- an advantage over competitors like GrubHub who started in metro cities where the operations were harder [2].

### 3. Choose Tech for Iteration Speed

Balance what makes sense for the product against personal expertise to ship as quickly as possible [2]. Do not choose a cool new language to learn for your startup. Use third-party frameworks and APIs: Auth0 for authentication, Stripe for payments, React Native for cross-platform, AWS/GCP for cloud, Webflow for landing pages, Firebase for back-end [2].

Hu invokes the "midwit meme" pattern: the beginner who chooses PHP or JavaScript to build a toy car, the mid-level engineer who reaches for Kafka, Kubernetes, and hundreds of microservices ("the average startup dies, so that's not a good outcome"), and the Jedi Master who also chooses PHP or JavaScript but for different reasons -- they recognize it lets them move faster [2]. Facebook was built on PHP because Mark Zuckerberg was fast with it. When they needed performance at scale, they built HipHop to transpile PHP to C++. "If you build a company and it works and you get users, you can solve your way out of it" [2].

WayUp (YC 2015), a job board for diverse candidates, is another example. CTO JJ chose Django and Python over the trendier Ruby on Rails. "He kept it simple in the backend: Postgres, Python, Heroku. And that worked out well for them" [2].

**The only tech choices that matter are the ones tied to your customer promises.** At Hu's startup Escher Reality, they rewrote and threw away code multiple times as they scaled, but maintained the API contract with game engine developers [2].

## Don't Hire to Build the MVP

Hu advises against hiring during the MVP stage [2]. It slows you down: finding a good engineer from an unknown pool takes over a month. More insidiously, it prevents founders from developing key product insights. "If someone else in your team is building that and not the founders, you're gonna miss that key learning about your tech that could have been a gold nugget" [2].

Justin.tv/Twitch illustrates the point. The MVP was built by three technical founders: Kyle tackled hard video streaming problems, Emmett handled the database, Justin built the web layer. Only after launching did they hire -- and when they did, they found engineers Google had overlooked. "Those turned out to be amazing" [2].

## Hacks for Building Fast

Seibel provides four tactical hacks for building an MVP quickly [1]:

1. **Time box your spec.** "What happens if I want to launch in three weeks? The only things that could be on my spec are things I can build in three weeks" [1].
2. **Write your spec.** If you never write it down, you keep changing it without realizing. "Your three week plan turns into a three month plan" [1].
3. **Cut your spec.** A week in, you will realize you added too much. Cut the unimportant things. "If there's no non-important things, start cutting important things" [1].
4. **Don't fall in love with your MVP.** "You wouldn't fall in love with a paper you wrote in the first grade" [1].

## Ask Users for Problems, Not Features

When gathering feedback on the MVP, the critical question is: does it solve the problem? Seibel warns against asking users for features: "Never ask users to tell you what they want. It's not the user's job to come up with features. That's your job. The user's job is to give you problems" [1].

The diagnostic questions for users [1]:
- How often do you experience this problem?
- How intense is it?
- Are you willing to pay for a solution?
- Do you know other people who have the problem?

When a user sneaks into "feature zone," redirect them: "Why do you wanna do that? What problem do you have? How often do you encounter that problem?" [1]

## Product-Market Fit Is Unmistakable

Seibel provides a vivid definition of [[Product-Market Fit]]: "People start using your product so much, you transition from doing anything, other than just keeping it online" [1]. You stop thinking about new features, conversion funnels, or distribution. "You are literally just, 'Holy shit, I don't know how I'm going to serve the people who are coming to my product tomorrow'" [1].

He warns against diluting the term: "A lot of people like to throw around the term, and a lot of people like to redefine it as, 'Someone's using my product.' That's not the term. The term for someone's using your product is, 'You have a user'" [1].

## Both Growth and Retention Matter

When asked whether to prioritize growth or retention post-MVP, Seibel refuses to choose: "What's more important, like, taking a shower or going to the bathroom? I'd like you to do both" [1]. Founders try to reduce startups to single-variable problems because multi-variable problems are hard. The startup does not offer that luxury [1].

## References

1. [How to Plan an MVP](https://www.ycombinator.com/library/6f-how-to-plan-an-mvp) -- [[Michael Seibel]] (2019)
2. [Tips for Technical Startup Founders](https://www.ycombinator.com/library/Is-tips-for-technical-startup-founders) -- [[Diana Hu]] (2024)
