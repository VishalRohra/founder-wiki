---
title: AI in Startups
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["AI startups", "using AI", "LLMs in startups", "AI pivot", "vibe coding", "AI tools for founders", "AI coding", "AI for startups"]
related: ["[[Startup Ideas]]", "[[Product Development]]", "[[Founder Productivity]]", "[[Tom Blomfield]]"]
sources: ["M3-how-to-use-ai-in-your-startup", "MN-how-to-get-the-most-out-of-vibe-coding"]
speakers_referenced: ["Brad Flora", "Gustaf Alstromer", "Pete Koomen", "Tom Blomfield"]
---

# AI in Startups

The current wave of AI -- particularly large language models (LLMs) -- represents a technology shift comparable to mobile (2007-2012) and cloud (early 2010s). YC Group Partners argue that every new startup should use AI, but that simply pivoting to AI without customer insight is not sufficient. Separately, "vibe coding" -- using AI coding assistants to build products -- has become a core productivity tool that founders can measurably improve at.

## Should You Pivot to AI?

Gustaf Alstromer offers a two-part answer: "No, you should not pivot to AI" just because it seems like a good idea. "But yes, you should almost absolutely be working on something that's using LLMs at the heart of it today" [1]. The distinction is between chasing a trend and leveraging a technology platform.

Pete Koomen draws the analogy to cloud: "If you are building a cloud company, obviously you're going to use the cloud. Same thing with AI. It doesn't make sense for anyone creating a new company today to not leverage AI within their company" [1].

## The Technology Wave Pattern

Brad Flora compares the current AI moment to the mobile wave he witnessed firsthand. He arrived at YC in 2007, the same week Steve Jobs announced the iPhone. The apps did not come until the following summer, and the permissions needed did not arrive until 2009. But the following five years produced most of the mobile companies people use today [1].

The pattern: "Big companies generally are preceded by big technology shifts" [1]. The AI shift began roughly two years ago and is intensifying monthly. Capabilities available now were not possible 18 months ago [1].

Alstromer extends the analogy to cloud migration in the early 2010s: "There were just a lot of good ideas lying around because you had the opportunity to replace some legacy piece of software that was on-prem." He cites a conversation with the CEO of Workday, who saw the same pattern when PeopleSoft's on-prem model was vulnerable to cloud-native replacements. "Similar moment now for a lot of companies" [1].

## Do Not Fear Big Companies

Despite the obvious power of incumbents, their execution speed is slow. "ChatGPT is like two years old, and we still have a dumb Alexa" [1]. This gap creates opportunities for startups. Flora advises founders not to fear big company speed of execution [1].

## Where AI Ideas Come From

### Automate Specialized Skills

Alstromer describes two companies from the Fall 2024 YC batch that automated previously specialized skills: Replex (automatic UI localization) and Gecko Security (AI security engineer). Both take a specialized skill, automate it with AI, put it behind an intuitive interface, and give software engineers the ability to manage it independently as part of their release cycle [1].

### Domain Expertise Matters

A YC company whose founders all worked at an insurance technology company built an AI co-pilot for Medicare Advantage insurance agents. "This is a relatively obscure workflow. Most software engineers don't have much experience with that. But because of that experience, they were able to build an AI co-pilot" that is doing very well [1].

This echoes [[Startup Ideas]] principles: the best ideas come from the intersection of domain expertise and a new technology capability.

### Healthcare as an AI Goldmine

Alstromer describes US healthcare as a $4 trillion system with $1.3-1.4 trillion in administrative costs. "If you look at the companies that we funded in YC, it seems like much of this admin is legacy software system plus a human who's moving data from one system into another" [1]. Most of these tasks are now fully automatable with LLM agents.

The challenge: founders do not know what these tasks are. Alstromer's advice is concrete: "Go to your friend who works in this and go and sit next to them and ask them how they do their job and watch their screens and you will get ideas right away. I'm very convinced that you don't have to spend more than a few hours in front of their screens" [1].

## The Importance of San Francisco

Multiple partners emphasize that the AI ecosystem is concentrated in San Francisco in a way that makes physical presence valuable. Alstromer compares it to his time at Airbnb: when they wanted to learn SEO, the world's best SEO team (Pinterest) was literally downstairs. "That is the state of LLMs here right now" [1].

The advice: at minimum, come to SF for three to four weeks and embed in the community. The long-term recommendation: consider moving permanently [1].

## Pivoting Done Right: The Bland Story

Flora tells the story of a company that applied to YC in Fall 2020 as "InvestBetter" (financial investment platform), pivoted during COVID to a Zoom productivity tool called Superpowered, grew to thousands of DAUs and became default alive, then recognized the LLM wave and made two decisions: move from Toronto to San Francisco, and stop working on the old product. The company, renamed Bland, grew from nothing to powering a significant portion of B2B voice AI in the YC portfolio in under 15 months [1].

## Pivoting Done Wrong

Koomen describes the failure pattern: companies that were not working pivoted to AI by becoming "customer support agent company number 50" without new insights, without changing their environment, without embedding in communities, and without deeper customer understanding. "The fundamental things that founders still need to do to enable the technology to produce value for customers are the same. And if you're not doing that, just switching your idea over to something that makes calls to OpenAI is not going to change your fate" [1].

## Vibe Coding: Getting the Most Out of AI Development Tools

[[Tom Blomfield]] spent a month building side projects with Claude Code, Windsurf, and Aqua, and compiled a playbook for getting better results from AI coding assistants [2].

### Start with a Plan, Not Code

Before writing any code, work with the LLM to write a comprehensive plan in a markdown file. Step through it section by section. Mark completed sections. Keep an "ideas for later" section to explicitly tell the LLM what is out of scope. "I probably wouldn't expect the models to oneshot entire products yet" [2].

### Version Control Religiously

Use Git as the safety net. Start each new feature from a clean Git state. If the AI goes off on a "vision quest," `git reset --hard` and try again. Do not accumulate layers of failed fixes -- each failed attempt adds cruft. If you eventually find the solution after several attempts, reset and re-implement the clean solution from scratch [2].

### Write Tests (High-Level)

Get the LLM to write tests, but keep them high-level -- simulate someone clicking through the site end to end rather than testing individual functions. LLMs have a bad habit of making unnecessary changes to unrelated logic, and test suites catch these regressions early [2].

### Bug Fixing

First step for any bug: copy-paste the error message straight into the LLM. "Often this error message is enough for the AI to identify and fix a problem. You don't even need to explain what's going wrong" [2]. For complex bugs, ask the LLM to think through three or four possible causes before writing any code. After each failed fix attempt, `git reset` and start again. If one model cannot solve it, try a different model [2].

### Write LLM Instructions

Put instructions in Cursor rules, Windsurf rules, or a Claude markdown file. Some founders have written hundreds of lines of instructions for their AI coding agent, making them "way, way, way more effective" [2].

### Choosing a Tech Stack

Blomfield found AI performed remarkably well with Ruby on Rails -- a 20-year-old framework with a ton of consistent, high-quality training data. Languages with less training data online (Rust, Elixir) produced less reliable results [2].

### Use Voice Input

Voice input through tools like Aqua (a YC company) allows input at roughly 140 words per minute, double typical typing speed. LLMs are tolerant of minor transcription errors [2].

### Refactor Frequently

Once code works and tests pass, refactor freely. Ask the LLM to identify repetitive code or refactoring candidates. Keep files small and modular -- easier for both humans and LLMs [2].

### LLMs Beyond Code

Blomfield used LLMs for DNS configuration, Heroku setup, favicon design and resizing, and documentation lookup. "The AI is now my designer as well" [2].

### Keep Experimenting

The state of the art changes weekly. Different models excel at different tasks: Gemini for whole-codebase indexing and planning, Sonnet 3.7 for implementation, though rankings shift constantly [2].

## References

1. [How To Use AI In Your Startup](https://ycombinator.com/library/M3-how-to-use-ai-in-your-startup) — Brad Flora, Pete Koomen, Gustaf Alstromer (2025)
2. [How To Get The Most Out Of Vibe Coding](https://ycombinator.com/library/MN-how-to-get-the-most-out-of-vibe-coding) — [[Tom Blomfield]] (2025)
