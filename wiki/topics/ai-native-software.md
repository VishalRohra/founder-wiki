---
title: AI-Native Software
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["AI-native software", "AI horseless carriage", "AI apps", "system prompts", "AI agents", "AI UX", "AI product design", "editable system prompts", "AI tools", "building AI products"]
related: ["[[AI and Startups]]", "[[Product Development]]", "[[Pete Koomen]]", "[[Tom Blomfield]]", "[[David Lieb]]"]
sources: ["MR-ai-apps-are-broken-here-s-how-to-fix-them"]
speakers_referenced: ["Pete Koomen", "Tom Blomfield", "David Lieb"]
---

# AI-Native Software

Most AI apps today are "horseless carriages" -- they pack powerful AI models into outdated interfaces designed for humans to do work in, rather than redesigning from the ground up to offload work [1]. [[Pete Koomen]], YC partner and founder of Optimizely, argues that the fundamental design question should shift from "How do I insert AI into my tool?" to "How would I design this tool from scratch to offload as much repetitive work from the user as possible?" [1].

## The Horseless Carriage Problem

The term references early automobile designs that looked like carriages with the horse replaced by an engine. The carriage form factor created problems at higher speeds -- poor suspension, high center of gravity, bad turns. "Inventing the motor was only a small part of what was needed to produce a vehicle that could take advantage of it. It only became useful once you redesigned the entire vehicle" [1].

The same pattern has repeated with every major technology transition [1]:
- **Internet**: The first search engines were digitized yellow pages (literal directories)
- **Mobile**: The first mobile apps were websites wrapped in a native app wrapper, ignoring GPS and multi-touch

Koomen argues we are in the horseless carriage stage of AI: developers are slotting AI into applications designed for humans to do work in, rather than redesigning around what AI can actually do [1].

## The Gmail Problem: A Case Study

Koomen uses Gmail's AI draft-writing feature as a detailed case study of the failure pattern [1].

**The prompt**: "Let my boss Gary know that my daughter woke up with the flu this morning and I won't be able to come into the office today."

**The output**: "Dear Gary, I'm writing to inform you that my daughter woke up with the flu this morning. As a result, I won't be able to come into the office today. Thank you for understanding. Best regards, Pete."

Two problems: (1) it does not sound like Pete -- it sounds like no human, and (2) the prompt is roughly as long as the output, defeating the purpose [1].

### The Root Cause: Hidden, Generic System Prompts

Every AI agent combines the user's prompt with a system prompt -- text that tells the AI who it is and what its job is. Gmail's system prompt is hidden from the user, cannot be edited, and is generic: "Use a formal businessy tone and correct punctuation so that it's obvious the user is really smart and serious" [1].

The system prompt is generic because developers treat it as they have treated code for decades: one-size-fits-all, hidden behind an interface, owned by the developer. "For as long as we've had a software industry, there's been a division of labor between me, the user, and you, the developer. The user does not see the code" [1].

### The Fix: Editable System Prompts

If Gmail allowed users to edit the system prompt, Koomen could write: "You're Pete. You're a 43-year-old husband, father, YC partner. You're busy, and so is everyone you correspond with, so you do your best to keep emails as short as possible" [1].

Using this custom system prompt with the same user prompt, the draft becomes: "Hi Gary, my daughter's sick with the flu, so I can't come in today. Thanks." That sounds like Pete [1].

The insight: "By editing this system prompt, I'm able to explain to the AI model how I write emails in general so that I don't have to do it every single time" [1].

## From Email Writer to Email Reader

The real opportunity is not making AI write emails -- it is making AI handle the inbox. Koomen built a demo of an email reading agent with a user-editable system prompt that assigns labels, archives messages, sets priorities, and drafts replies [1]:

- If the email is from my wife: draft a reply, label it personal
- If it is from my boss: draft a reply, priority one
- Anyone else at YC: YC label, priority two
- From a founder who needs help: founders label
- Tech-related: label it tech
- Someone trying to sell me something: archive it

This is the code. The user wrote it in plain English. "The LLM technology is actually good enough to let non-programmers program these apps" [1].

[[Tom Blomfield]] frames the potential: "Steve Jobs describes software as a bicycle for the mind. This feels like a rocket ship for the mind" [1].

## The Developer's New Job: Build Tools, Not Prompts

If users can program agents through natural language, what should developers build? Koomen's answer: tools [1].

Tools are the capabilities that agents need to take action -- labeling an email, archiving it, writing a draft, making a calendar entry, sending a Slack message, updating a Jira ticket. "The thing that these agents need in order to be able to do anything useful, we call tools" [1].

With the right tools, an email agent could handle bill payments, introductions, handoffs, BCC management -- the transactional work that fills most inboxes but does not require original thinking [1].

MCP (Model Context Protocol) servers are emerging as the standard way to provide tool access to agents. A YC batch company called Den is building "Cursor for knowledge work" -- chaining together MCP servers so agents can operate across Slack, Google Docs, email, and GitHub from a single interface [1].

## Why Coding Agents Are So Far Ahead

Koomen and Blomfield identify two reasons Cursor, Windsurf, and Claude Code feel so much more powerful than AI agents in other domains [1]:

1. **LLMs are good at processing text and producing code.** If you can describe what you want in English, the model can produce functional code. This is a domain where the core capability aligns perfectly with the use case.

2. **Developer tools give full access to the model.** Developer tool teams did not spend effort preventing users from doing embarrassing things. "They allowed me full access to have this agent do whatever I wanted." Other domains still use a "kid glove mentality" -- limiting the model's power to prevent bad outputs [1].

## Can Non-Technical Users Write System Prompts?

Koomen acknowledges that today most people cannot write system prompts. But he argues this will change quickly, analogizing to computer literacy: "When I was growing up, computers were still seen as a power tool that only nerds really knew how to use. Today that's just no longer the case" [1].

Writing a prompt is more accessible than operating a file system. "You don't need to understand much except to be able to explain yourself in English or whatever language you speak" [1].

For the near term, AI can help. Blomfield describes the pattern: the product reads 20 years of email history, generates a draft system prompt customized to the user, and iterates based on feedback -- exactly how a new human assistant would learn [1].

Koomen built a demo where users can edit system prompts and immediately rerun them, creating a feedback loop: "As long as you can watch it do the job and give it feedback by adjusting this prompt, it's pretty intuitive" [1].

## The Chatbot Paradigm Is Wrong

Blomfield expresses strong dissatisfaction with the chatbot paradigm: "I kind of hate the chatbot paradigm. It was the easiest way to bring the most basic LLM experience to the whole world. But now every product is just embedding this chat agent in it. That's not the way this stuff should be used in almost every case" [1].

LLMs are capable of automating work on behalf of users -- accomplishing things in the world, not just answering questions. The chatbot interface obscures this capability [1].

## Implications for Founders

Koomen's advice: "This is one of the most exciting times to be a founder because almost every tool that we've been using for decades can be rethought from the ground up with AI. The AI-native version of a lot of tools will look different from the versions we're used to" [1].

The shift: instead of asking "How do I insert AI into my tool?" ask "How would I design this tool from scratch to offload as much repetitive work from the user as possible so they can focus on what's important?" [1].

## References

1. [AI Apps Are Broken -- Here's How To Fix Them](https://ycombinator.com/library/MR-ai-apps-are-broken-here-s-how-to-fix-them) -- [[Pete Koomen]], [[Tom Blomfield]], [[David Lieb]] (2025)
