---
title: "Cursor: From Failed CAD Co-Pilot to $100M ARR Code Editor"
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["Cursor", "Cursor case study", "Anysphere", "Anyphere", "Michael Truell", "AI code editor", "Cursor IDE"]
related: ["[[AI and Startups]]", "[[Pivoting]]", "[[Starting Young]]", "[[Competing with Big Companies]]", "[[Product-Market Fit]]", "[[Michael Truell]]"]
sources: ["Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students"]
speakers_referenced: ["Michael Truell"]
---

# Cursor: From Failed CAD Co-Pilot to $100M ARR Code Editor

Cursor (built by Anysphere) is an AI-powered code editor that went from zero to $100M ARR in one year (2024). Co-founder Michael Truell was 24 at the time. The company's story illustrates several principles: the value of years of preparation before a startup "overnight success," the courage to compete against an entrenched incumbent, and the power of product quality as a growth engine [1].

## Origins: A Decade of Preparation

Truell's path to Cursor began in middle school. He and his brother wanted to build a hit mobile game. His brother looked at Objective-C and quit. Truell bought a book and kept going. His most viral creation was not a game but a novelty app that spoofed high scores in Piano Tiles and Flappy Bird -- "the technically easiest thing to build, which was maybe a lesson in startups of, you know, the code isn't everything" [1].

In high school, Truell and a friend built robots with reinforcement learning. They wanted to teach a robot dog to learn from positive and negative feedback, like a real dog. Their naivete was an advantage: unable to use standard ML libraries on memory-constrained microcontrollers, they implemented their own neural network library from scratch. "I have memories of us not really understanding calculus but kind of fumbling our way through reimplementing some important ideas from neural networks" [1].

Truell was inspired from early on by [[Paul Graham]]'s essays and the YC community [1].

## The Founding and Failed Ideas

The four co-founders graduated from MIT in 2022. They shared deep interest in AI and two catalysts excited them: GitHub Copilot (proof that AI coding products had a market) and scaling law research (evidence that AI would predictably improve) [1].

They began with a month-long hackathon in early 2022, exploring AI for various knowledge work domains [1].

### The CAD Co-Pilot (6+ months)

Their first serious idea: an AI co-pilot for mechanical engineers using CAD systems like Solidworks and Fusion 360. They chose it because it seemed "boring and sleepy and uncompetitive" -- an "armchair MBA thing" that was a poor fit because none of them were mechanical engineers and the AI science was not ready for that domain [1].

The work was heavy on data scraping (collecting all CAD models on the internet, converting between file formats), training infrastructure, and hacking extensions into non-extensible CAD applications. The result: effectively no users [1].

### Other Failed Projects

Simultaneously, two co-founders built an end-to-end encrypted messaging system that hid not just message content but metadata (who is talking to whom, when). Technically impressive but no traction as either a consumer or B2B product [1].

### The Pivot to Coding

The co-founders had avoided AI for coding because they thought it was too competitive -- GitHub Copilot was already generating $100M+ in revenue. The pivot came from "the desperation of having worked on ideas for a while and not really being excited about them" [1].

A critical realization: "If we were being really consistent with our beliefs, there was going to be an opportunity for all of coding to change in the next 5 years and for all of software development to flow through models. It felt like no one working on the space at the time was really taking that seriously. They had great products and were making them a bit better, but they weren't really aiming for a world where all of coding as we know it today gets automated" [1].

They considered niche approaches first -- security reviews, tools for quants -- but had too many ideas for the general product. "We just had a ton of conviction about that and we had a ton of excitement about that and so at some point we just decided to go for it" [1].

## Building the Product

### The Custom Editor (First 3 Months)

The team initially built their own code editor from scratch using open-source primitives like CodeMirror and language servers. Within four weeks, they had something they could use as their daily driver. Four weeks later, first beta testers. Four more weeks, public launch [1].

The first version had a single command that pulled up a "universal remote" -- users asked the AI to do something, and the system tried to figure out the appropriate response. "There wasn't a lot of control." They learned that given the state of AI at the end of 2022, the interface needed more structure [1].

### The Switch to VS Code

They also learned that building a feature-complete code editor for the world would take far longer than anticipated. VS Code had been developed over 12 years with many people. "We thought, 'Oh yeah, of course, you can spin something up that's just equivalent for the world in a few months.' We learned very rapidly that wasn't the reality." They switched to basing Cursor on VS Code, similar to how browsers base themselves on Chromium [1].

### Custom Models as a Product Lever

Initially, the team avoided model training, burned by the CAD experience. But as the product scaled, building their own models -- especially for Tab (next-edit prediction) -- became "a really important product lever." Product usage data fed back into model improvement [1].

## The Growth Story

### 2023: Wandering the Desert

Throughout 2023, numbers were small and direction was unclear. The team debated whether to pivot again. There was no clear next step much of the time. Early users pulled in different directions: a vocal segment of non-coders wanted attention; another segment wanted tech-stack-specific tools. The team resisted both [1].

A team member occasionally argued that "the product's already good enough -- let's focus on growth engineering." Two-month sprints on growth "kind of washed away compared to the other stuff we worked on that year" [1].

The company ended 2023 with fewer than 10 employees and roughly $1M in revenue [1].

### 2024: 1 to 100 in One Year

Compounding growth continued because each product improvement showed up immediately in the numbers: codebase awareness, next-action prediction, faster and more ambitious predictions, agent-like behavior within the codebase. "We kind of just focused on making the product better. The compounding continued" [1].

YC batch adoption was a signal: from single-digit percentage Cursor usage in 2023 to roughly 80% in 2024. "It just spread like wildfire. The best builders were using it" [1].

### Growth Channels

Initial traction came from one co-founder who had built a niche following on Twitter by reading AI papers and posting analysis. He evangelized the product at launch. But after the initial push, "we stepped away from that and lived like monks in 2023 and just focused on the product." Growth was almost entirely word of mouth [1].

## Truell's Advice

### For Young Builders

"Work on things that you're interested in and do it with people both that you enjoy being around but that you respect a ton. And take that really seriously" [1].

For students: resist the pull toward checking boxes. "Really focusing on something that you're interested in" matters more than credentials [1].

### On the Future of Coding

Truell holds a middle position between "AGI makes all coding tools irrelevant" and "the current paradigm is permanent." His view: AI will transform software development over the next couple of decades. Code will still matter for professional engineers, but the role shifts toward reviewing, editing, and directing AI output. "There will be this long messy middle where you will be working with the AI more and more. It will become like a colleague more and more" [1].

Programming, like math, is "a good general education. I don't think that goes away" [1].

## References

1. [Michael Truell: Building Cursor at 23, Taking on GitHub Copilot, and Advice to Engineering Students](https://ycombinator.com/library/Ms-michael-truell-building-cursor-at-23-taking-on-github-copilot-and-advice-to-engineering-students) -- Michael Truell, Diana Hu (June 2025)
