---
title: Prompt Engineering
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["prompting", "prompt engineering", "system prompts", "metaprompting", "prompt folding", "evals", "LLM prompting", "AI prompting"]
related: ["[[AI-Native Software]]", "[[AI Coding Agents]]", "[[Forward Deployed Engineers]]", "[[Jared Friedman]]", "[[Harj Taggar]]", "[[Garry Tan]]"]
sources: ["MS-state-of-the-art-prompting-for-ai-agents", "MR-ai-apps-are-broken-here-s-how-to-fix-them"]
speakers_referenced: ["Jared Friedman", "Harj Taggar", "Garry Tan", "Diana Hu", "Pete Koomen"]
---

# Prompt Engineering

Prompt engineering has evolved from a temporary workaround for getting useful output from LLMs into a core discipline for AI startups. YC partners [[Garry Tan]], [[Harj Taggar]], [[Jared Friedman]], and Diana Hu surveyed more than a dozen top AI companies and synthesized what the best teams are doing to make LLM outputs useful and predictable in production [1]. The practice resembles both coding ("it kind of feels like coding in 1995") and management ("how do I actually communicate the things they need to know to make a good decision") [1].

## Anatomy of a Production Prompt

Parahelp, a YC company powering AI customer support for Perplexity, Replit, and Bolt, open-sourced its production prompt -- a rare glimpse at the "crown jewels" of a vertical AI agent company [1]. The prompt is six pages long and follows a structured format:

1. **Role definition**: "You're a manager of a customer service agent" with bullet-pointed responsibilities [1].
2. **Task specification**: Approve or reject tool calls, orchestrating other agents [1].
3. **Step-by-step plan**: Numbered steps (1, 2, 3, 4, 5) for reasoning through decisions [1].
4. **Guardrails**: Instructions to avoid calling certain tools or going off-track [1].
5. **Output format**: Structured output specification (accept/reject with specific formatting) -- critical for agent-to-agent integration [1].
6. **Worked examples**: XML-tagged examples showing expected reasoning and output [1].

Diana Hu notes that the best prompts use XML tag formatting for examples because "a lot of LLMs were post-trained in RLHF with kind of XML type of input, and it turns out to produce better results" [1]. The prompt looks "more like programming than writing English" [1].

## The Three-Tier Prompt Architecture

A production AI system typically separates prompts into three tiers [1]:

- **System prompt**: Defines the high-level behavior -- the company-wide API. Parahelp's open-sourced prompt is a system prompt with nothing customer-specific [1].
- **Developer prompt**: Customer-specific context -- how to handle Perplexity RAG questions versus Bolt build questions [1].
- **User prompt**: End-user input (not all products have this; Parahelp's product is not directly consumed by end users) [1].

This architecture addresses a key challenge for vertical AI agent companies: how to have enough flexibility for customer-specific logic without becoming a consulting company that builds a new prompt for every customer [1]. Friedman calls this "forking and merging prompts across customers" -- a frontier the industry is only beginning to explore [1].

## Metaprompting

Metaprompting -- using one LLM to improve another LLM's prompts -- is "turning out to be a very powerful tool that everyone's using now" [1].

**Prompt folding**: One prompt dynamically generates better versions of itself. A classifier prompt generates a specialized prompt based on the previous query. You feed examples where the prompt failed, and instead of rewriting the prompt manually, you give it to a raw LLM and say "Help me make this prompt better." Tan describes this: "Because it knows itself so well, strangely, metaprompting is turning out to be a very, very powerful tool" [1].

**Example-driven refinement**: When the task is too complex to describe in instructions alone, worked examples steer the model. Jasberry (current YC batch) does automatic bug finding in code, feeding expert-level examples of hard-to-find bugs (like N+1 queries) into the prompt. "This pattern of giving examples turns out to work really well because it helps LLMs reason around complicated tasks" [1].

**Model distillation via metaprompting**: Companies use a larger model (Claude 3.5, GPT-4o) to do metaprompting and refine prompts, then deploy the refined prompt on a smaller, faster model (Llama). This is common for voice AI companies where latency is critical -- "if you have too much pause before the agent responds, humans can detect something is off" [1].

**Quick-start method**: Even for hobbyists, a simple approach works: give the LLM the role of "expert prompt engineer who gives really detailed, great critiques," feed it your draft prompt, and iterate. "Works surprisingly well" [1].

## Escape Hatches and Debug Info

A critical lesson: LLMs will hallucinate rather than admit uncertainty. "The model really wants to help you so much that if you just tell it 'Give me back output in this particular format,' even if it doesn't quite have the information it needs, it'll actually just tell you what it thinks you want to hear" [1].

Two solutions have emerged:

1. **Explicit escape hatch**: Tell the model "If you do not have enough information to say yes or no, don't just make it up. Stop and ask me" [1].
2. **Debug info parameter**: Friedman's approach at YC -- add an output field where the model can complain to the developer about confusing or underspecified instructions. "It literally ends up being like a to-do list that you, the agent developer, has to do" [1].

## Model Personalities

Different models have distinct personalities that affect how they handle prompts [1]:

- **O3**: "Very rigid. It really sticks to the rubric. It heavily penalizes for anything that doesn't fit" -- like a soldier doing check, check, check [1].
- **Gemini 2.5 Pro**: "Quite good at being flexible. It would apply the rubric, but it could also reason through why someone might be an exception" -- like a high-agency employee [1].
- **Claude**: "The more happy and more human steerable model" [1].
- **Llama 4**: "Needs a lot more steering. Almost like talking to a developer" -- possibly because of less RLHF [1].

Taggar describes discovering this while building an investor scoring system: the same rubric given to O3 and Gemini 2.5 Pro produced meaningfully different results, with Gemini being better at handling edge cases that fell outside the rubric's explicit parameters [1].

## Evals Are the Crown Jewels

The YC partners have been saying for over a year that evals -- the test suites for prompt quality -- are the true data asset for AI companies [1]. Parahelp was willing to open-source its prompt precisely because "they don't consider the prompts to be the crown jewels -- the evals are the crown jewels, because without the evals, you don't know why the prompt was written the way that it was" [1].

Building good evals requires sitting "literally side by side with people who are doing X, Y, or Z knowledge work" [1]. You need to sit next to the tractor sales regional manager in Nebraska and understand their reward function, then codify that into specific evals. Tan describes this as the true moat: "If you are out there in particular places understanding that user better than anyone else and having the software actually work for those people, that's the moat" [1].

This connects directly to the [[Forward Deployed Engineers]] model pioneered by Palantir (see that article for the full treatment).

## Practical Tips

- Use Gemini 2.5 Pro's long context window like a REPL: feed your prompt plus one example, watch the reasoning trace in real time to understand how to steer the model [1].
- Thinking traces (chain-of-thought outputs) are "the critical debug information to understand what's wrong with your prompt" -- Gemini recently added these to its API [1].
- Keep a Google Doc of noted failures while using the agent, then feed those notes plus the original prompt to a strong model and ask it to suggest edits [1].
- The Kaizen principle applies: "The people who are the absolute best at improving the process are the people actually doing it" -- which is what metaprompting enables [1].

## References

1. [State-Of-The-Art Prompting For AI Agents](https://www.youtube.com/watch?v=DL82mGde6wo) -- [[Garry Tan]], [[Harj Taggar]], Diana Hu, [[Jared Friedman]] (2025)
2. [AI Apps Are Broken -- Here's How To Fix Them](https://www.youtube.com/watch?v=WJoZK9sMwvw) -- [[Pete Koomen]], Tom Blomfield, David Lieb (2025)
