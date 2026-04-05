---
title: "Perplexity: Building the Next Search Engine"
type: case-study
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["Perplexity", "Perplexity AI", "Aravind Srinivas", "AI search", "Perplexity case study"]
related: ["[[Aravind Srinivas]]", "[[AI and Startups]]", "[[Competing with Big Companies]]", "[[Product-Market Fit]]", "[[Talking to Users]]", "[[Growth]]", "[[David Lieb]]"]
sources: ["MC-how-to-build-the-future-aravind-srinivas"]
speakers_referenced: ["Aravind Srinivas", "David Lieb"]
---

# Perplexity: Building the Next Search Engine

Perplexity is an AI-powered search engine that grew to a $9 billion valuation in under three years. Co-founded and led by Aravind Srinivas, the company started as a Twitter search tool, pivoted to general web search powered by LLMs, and now competes directly with Google. The story illustrates how ignorance of competitive moats can be an asset, why the "dumb approach" sometimes beats the smart one, and how the innovator's dilemma protects challengers in ad-dependent markets.

## Ilya's Two Circles

Srinivas came to the US from India for a PhD at Berkeley, studying AI and deep learning. His intellectual trajectory was reshaped by an internship at OpenAI, where Ilya Sutskever "listened for five minutes and said, 'All this research is useless'" [1].

Sutskever drew two circles. The large circle was unsupervised learning. Inside it, a smaller circle was reinforcement learning. He pointed to the inner circle and said, "This is AGI. Every other research doesn't matter" [1]. This was during GPT-1 development, before the name "GPT-1" existed.

Srinivas returned to Berkeley and shifted his focus from reinforcement learning (the trend, driven by AlphaGo and DeepMind) to generative models and unsupervised learning. During a later internship at Google, he read Steven Levy's "In the Plex" and realized that Google's founders were once grad students like him. The idea took shape: build a company at the intersection of AI research and product building [1].

He discussed this with Sutskever, and they identified two problems where AI research and product development could form a flywheel: search and autonomous driving. In both, product usage generates data that improves the underlying AI, which makes the product better, which attracts more users. Critically, the company must be "on the AI completeness path" -- better AI should continuously make the product better, so the company grows alongside AI progress rather than being run over by it [1].

## The Twitter Search Prototype

Srinivas's first pitch to seed investor Elad Gil was about disrupting Google "from pixels, from a glass" -- a multimodal, camera-based approach. Gil advised against it [1].

The team pivoted to building search over specific databases and verticals. They could not get enterprise data (Pitchbook, Crunchbase refused to share), so they turned to Twitter's publicly available academic data. In one month, three people built a conversational search tool for Twitter: you could chat, query, and plot data. Users loved it, particularly the social search dimension -- discovering who follows whom, who liked what, who unfollowed whom [1].

They attempted to replicate this for other databases (GitHub, LinkedIn) but kept hitting data access walls. Then Srinivas encountered a key insight, which he attributes to the "Polymath tweet": when you try to solve a harder version of a problem, you sometimes end up with a simpler, more general, more scalable solution [1].

The choice was between two architectures [1]:

1. **Structured approach**: Index each domain's data into specific formats (tables), write templates, have the LLM generate SQL queries. Reliable but domain-specific and labor-intensive.

2. **Unstructured approach**: Keep data unstructured, let the LLM do the heavy lifting at inference time. Less reliable with current models but more general and future-proof.

The team chose the second path, betting that models would get smarter. This also meant Perplexity would be architecturally different from Google's heavily indexed system, providing a structural advantage if the bet on improving models was correct [1].

## The "Dumb Approach" That Worked

OpenAI's WebGPT (built by John Schulman's team) had already demonstrated web-search-plus-LLM, but it was slow and agentic -- an RL agent that decided whether to click links, scroll, and browse. Srinivas built a simpler, faster version [1]:

- Always take the top-K links from a search API
- Only use the cached summary snippets (no scrolling, no clicking)
- Feed all links into the LLM prompt
- Ask the model to write a summary with academic-style source citations

Srinivas describes this as "the dumb approach," but it worked because models had improved enough for reliable instruction-following. "One year ago, John and his team tried, like the models were just so much worse that if you tried the dumb approach it just wouldn't work" [1]. Better models fixed the latency problem, which was the core product UX issue. Even so, the first version took seven seconds because they did not implement streaming, and had to hardcode prompts like "Only write five sentences" to control verbosity [1].

## Finding Traction: People Search for Themselves

The first moment of virality came from an error. An academic searched for herself, and Perplexity wrote her biography in the past tense -- because a person with the same name had died. The model's reasoning was "pretty clever" but lacked the higher-order understanding that these were different people. The mistake went viral and triggered a wave of people searching for themselves, screenshotting AI-generated summaries of their internet presence, and sharing them [1].

Srinivas recognized a universal pattern, confirmed by a conversation with Instagram's Mike Krieger: people love to search for themselves. On Instagram, even though users can tap their own profile icon, they frequently search for their username in the search bar [1].

The product breakthrough came when they added follow-up questions, which "doubled the engagement time on the site and also increased the number of questions every day." The number of queries per day was growing exponentially. This convinced Srinivas not to pivot to enterprise [1].

## The Bing Chat Scare

On the day Srinivas agreed to a term sheet with NEA, The Verge leaked screenshots of Bing Chat. One competing investor extended the due diligence period from 30 to 45 days. Another texted asking for a call the next morning [1].

Srinivas told his co-founder they should consider selling the company. But the NEA investor called and said: "Look, I'm not going to ask you to pivot. I'm not going to ask you to do anything different. You guys keep going." The following week, Google announced Bard. Srinivas's assessment: Microsoft "was never really good at consumer products for a long, long time. You can't suddenly change that." They "messed up the opportunity." Google would have its own internal challenges [1].

## The Innovator's Dilemma as Competitive Moat

Srinivas articulates why Google cannot easily build Perplexity's exact product on its homepage: if people stop clicking on links, the ad economy declines. Google's search page is already cluttered with answer boxes, knowledge panels, ads, social cards, and perspectives. The difference between using Google and Perplexity on informational queries is "fast food versus healthy meal" [1].

Google's search revenue is close to $200 billion per year, with the highest margins in the company. YouTube is not high-margin (creator payouts, no ads on subscribers). Cloud only recently became profitable. The stock price depends on search revenue: "Wall Street just automatically panics if search revenue goes down" [1].

Srinivas argues that whoever wins the next generation of search will need a new business model. The current ad model is structurally incompatible with directly answering questions. He envisions a product that researches products, books hotels, completes purchases -- end-to-end from question to action. The monetization comes from transaction facilitation, not from ad clicks on intermediate links [1].

## Larry Page's "User Is Never Wrong" Principle

Srinivas deliberately modeled Perplexity's culture on early Google principles, particularly Larry Page's maxim that "the user is never wrong" [1]. When a feature fails for a user, the product should clarify ambiguity rather than blame the user:

"It should have come and clarified to me, 'Hey, I'm not sure. Either it's this or this, which one did you actually want?' And then I should have clarified and then it should have gone and done, instead of saying, 'I don't know'" [1].

The opposite approach -- blaming users and telling them to become better prompt engineers -- is how enterprise software works. Magical consumer products work the other way. Srinivas draws the analogy to Google's spell-check and auto-suggest: Larry Page was not good at spelling, so Google handled typos. The product adapted to the user, not the other way around [1].

## Operating the Company

Perplexity's primary metric is number of queries per day, the same metric Google used in its early days. Srinivas reviews it weekly at All Hands meetings, analyzing growth rates and investigating any declines. He rejected the idea of a always-visible TV dashboard as distracting [1].

The organizational culture is flat: "There's no hierarchy. If there is some bug to be fixed, if I know some particular person's working on it, I can go and talk to the person directly." Srinivas personally files roughly 50 bugs per day. The team understands this is about product quality, not performance review [1].

For user feedback, Srinivas uses X (Twitter) as the primary channel because "people are just super brutally honest there." Email is too polite. In-person feedback is worst: "You go show someone something and they're just going to tell you good things, even if they hate it" [1].

## Fighting Entropy at Scale

Srinivas acknowledges the company is already slowing compared to its earliest days. The causes are not just headcount but the cost of things breaking in production, which erodes trust and makes people cautious. Not every new engineer has full context of the codebase. There is tension between moving fast and maintaining quality for mass-market usage [1].

His strategy: maintain personal awareness of who is working on what, file bugs directly, and rely on co-founders who share the obsessive detail-orientation. "We're trying to fight the entropy here. I think that's the only thing you can try. And it's an uphill battle" [1].

## The Next Google: An Orchestration Problem

Srinivas's vision for what wins in 10 years is not just better answers but a universal orchestrator: small models for quick facts (weather, scores, ages), knowledge graphs, widgets, LLM streaming for complex answers, multi-step reasoning for research queries, clarifying questions for ambiguous intent, and transactional capabilities for shopping and booking. The user should not need to specify when to use what -- the system decides. "Whoever builds that and can operate that at a scale of billion users and also knows how to monetize some of those queries really well is going to be the next Google" [1].

He argues Perplexity is better positioned for this than OpenAI or Anthropic: "We have it in our DNA to care about the user and the product. We're not just talking about reasoning and models" [1].

## References

1. [How To Build The Future: Aravind Srinivas](https://ycombinator.com/library/MC-how-to-build-the-future-aravind-srinivas) -- Aravind Srinivas, [[David Lieb]] (2025)
