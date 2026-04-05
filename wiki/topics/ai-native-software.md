---
title: AI-Native Software
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["AI-native apps", "AI horseless carriage", "system prompts", "AI product design", "AI UX", "building AI products", "AI app design", "chatbot paradigm"]
related: ["[[AI Coding Agents]]", "[[Prompt Engineering]]", "[[Startup Ideas]]", "[[Product Development]]", "[[Pete Koomen]]", "[[Andrej Karpathy]]"]
sources: ["MR-ai-apps-are-broken-here-s-how-to-fix-them", "MW-andrej-karpathy-software-is-changing-again", "Mf-andrew-ng-building-faster-with-ai"]
speakers_referenced: ["Pete Koomen", "Tom Blomfield", "David Lieb", "Andrej Karpathy", "Andrew Ng"]
---

# AI-Native Software

Most AI applications today are "horseless carriages" -- they pack powerful technology into outdated interfaces designed for humans to do work in, rather than reimagining the product from scratch to offload work entirely [1]. [[Pete Koomen]], YC partner and founder of Optimizely, argues that the fundamental error is asking "How can we slot AI into our existing application?" instead of "How would we design this tool from scratch to offload as much repetitive work from the user as possible?" [1]. [[Andrej Karpathy]] frames this as a broader shift: we have entered the era of "Software 3.0," where natural language becomes the programming interface and models do the rest [2].

## The Horseless Carriage Problem

Koomen draws on the analogy of early automobiles, which looked like horse carriages with the horse replaced by an engine [1]. The carriage design created problems at higher speeds: less suspension, higher center of gravity, poor handling. The motor was only a small part of what was needed -- the entire vehicle had to be redesigned. The same pattern repeats across technology transitions: the first search engines were digitized yellow pages; the first mobile apps were websites wrapped in native shells that ignored GPS and multi-touch [1].

The Gmail email-writing agent illustrates the problem. Gemini, the underlying model, is "amazing" -- "absolutely incredible" [1]. But the UI makes it frustrating to use. When asked to draft a sick-day email to a boss, it produces text like "Dear Gary, I'm writing to inform you that my daughter woke up with the flu this morning. As a result, I won't be able to come into the office today. Thank you for understanding. Best regards, Pete" [1]. Two problems: the output does not sound like the user, and the prompt is roughly as long as the draft itself -- meaning the AI creates more work than doing the task manually [1].

The root cause: the system prompt is hidden from the user, generic, and corporate-safe. It tells the model to "use a formal businessy tone and correct punctuation so that it's obvious the user is really smart and serious" [1]. Every user gets the same one-size-fits-all behavior.

## Exposing the System Prompt

Koomen's central thesis: users should be able to see and edit the system prompt [1]. If Gmail allowed Pete to replace the generic prompt with "You're Pete. You're a 43-year-old husband, father, YC partner. You're busy, and so is everyone you correspond with, so you keep emails as short as possible," the output changes dramatically: "Hi Gary, my daughter's sick with the flu, so I can't come in today. Thanks" [1].

This represents a fundamental shift in the division of labor between developer and user. For decades, the developer wrote the code, hid it behind an interface, and delivered one-size-fits-all software. The system prompt, however, is just English. It does not require technical knowledge to edit. "I think basically everyone will be able to do this," Koomen argues, comparing it to how using a computer was once a nerd-only skill and is now universal [1].

The objection that most people will not want to write system prompts from scratch has a straightforward answer: AI can auto-generate the system prompt from 20 years of email history, then the user provides feedback and the system auto-updates. "In 5 years, for 99% of people, they're not touching the system prompt, but the system prompt is custom to them" [1].

The liability shift matters too. If the user controls the system prompt, bad outputs are the user's responsibility, not the developer's -- just as profane emails written in Gmail are the sender's problem, not Google's [1].

## From Chatbots to Agents with Tools

The chatbot paradigm -- a text box where you type questions and get answers -- was "the easiest way to bring the most basic LLM experience to the whole world" but is not how AI should be used in most cases [1]. The real promise is agents that can accomplish things in the world on the user's behalf.

Koomen built a demo email reading agent with a user-editable system prompt that instructs it how to label, archive, and draft replies to incoming emails based on the sender and content [1]. The agent's capabilities come from tools: a tool for labeling, a tool for archiving, a tool for drafting. With additional tools -- paying bills, making introductions, integrating with Slack, calendar, and project management -- such an agent could handle most of the repetitive inbox work that consumes hours daily [1].

A company in the current YC batch called Den is "building Cursor for knowledge work" -- chaining together MCP servers (tools for agents) so that a boss's Slack message about reviewing terms can trigger pulling from Google Docs, sending to legal via email, and publishing via GitHub, all from one place [1]. Steve Jobs described software as "a bicycle for the mind." Koomen says this feels like "a rocket ship for the mind" [1].

## Software 3.0: Natural Language as Code

[[Andrej Karpathy]] traces three eras of software [2]:

- **Software 1.0**: Traditional code written by humans in programming languages. Deterministic, explicit instructions.
- **Software 2.0**: Neural networks where the "code" is the weights learned from data. He described this [in a 2017 blog post](https://karpathy.medium.com/software-2-0-a64152b37c35).
- **Software 3.0**: Large language models where the programming interface is natural language -- prompts. The user writes what they want in English, and the model produces the behavior.

This shift means that for the first time, the technology diffusion goes in reverse: LLMs are the first technology that reaches the people first and the experts last. Non-technical users can get useful output immediately through natural language, while developers are still figuring out the best tooling and paradigms [2].

Karpathy sees the current moment as building "a new kind of computer" -- one where the CPU is an LLM, the programming language is English, and the applications are prompts plus tools. The implications for software design are fundamental: instead of building rigid UIs with predetermined flows, developers build tool ecosystems that agents navigate based on natural language instructions [2].

## Speed as the New Bottleneck

Andrew Ng observes that AI coding assistants have shifted the bottleneck in product development [3]. Writing code is faster than ever; the bottleneck has moved to figuring out what to build and evaluating whether it works. He advocates for "concreteness over vagueness" -- instead of lengthy specification documents, build a prototype in hours and iterate from there [3].

Ng emphasizes agentic workflows as a paradigm shift: instead of a single LLM call producing output, chains of agents plan, execute, critique, and revise. This changes what startups can build because multi-step workflows that previously required teams of humans can now be automated by agent pipelines [3].

## Why Coding Agents Are Ahead

The coding domain (Cursor, Windsurf, Claude Code) is far ahead of other AI applications for two reasons [1]:

1. **LLMs are excellent at processing instructions into text output.** Code is text. A description in English maps naturally to code output.
2. **Developer tools are power tools.** They allow full access to the bare metal. The teams that built coding agents did not spend time preventing users from doing anything embarrassing -- they let users interact directly with the full power of the model [1].

Other domains still use "kid glove mentality" -- nerfing the model to prevent liability, which makes it useless [1]. Koomen hopes the industry moves beyond this: "I hope we're able to move beyond this moment in time where there's so much assumed liability on the part of the application developers for what these models do" [1].

## Implications for Founders

This is "one of the most exciting times to be a founder because almost every tool that we've been using for decades can be rethought from the ground up with AI" [1]. The AI-native version of most tools will look fundamentally different from what exists today. Founders should not ask "how do I insert AI into my tool" but rather "how would I design this tool from scratch to offload as much repetitive work from the user as possible so they can focus on what's important" [1].

## References

1. [AI Apps Are Broken -- Here's How To Fix Them](https://www.youtube.com/watch?v=WJoZK9sMwvw) -- [[Pete Koomen]], Tom Blomfield, David Lieb (2025)
2. [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) -- [[Andrej Karpathy]] (June 2025)
3. [Andrew Ng: Building Faster with AI](https://www.youtube.com/watch?v=RNJCfif1dPY) -- Andrew Ng (June 2025)
