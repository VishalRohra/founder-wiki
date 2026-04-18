---
title: "The Next Breakthrough In AI Agents Is Here"
slug: "MM-the-next-breakthrough-in-ai-agents-is-here"
media_type: "Video"
author: "Garry Tan"
speakers: ["Speaker"]
categories: []
description: "Usable AI agents are finally here. Garry dives into Manus’ “chain-of-thought injection” technique that enables agents to actively update plans, what works particularly well with its UI, and how founders can create enduring value with application-level products."
url: "https://ycombinator.com/library/MM-the-next-breakthrough-in-ai-agents-is-here"
youtube_id: "JOYSDqJdiro"
youtube_url: "https://www.youtube.com/watch?v=JOYSDqJdiro"
transcript_source: "yc_page"
multi_speaker: false
speaker_labels: true
---

# The Next Breakthrough In AI Agents Is Here

Usable AI agents are finally here.

From OpenAI’s DeepResearch to xAI’s DeepSearch, we’re seeing the first real push toward autonomous tools that can plan,
execute, and complete tasks like research, outreach, and coding with minimal human input. Recently, a new entrant joined
the competition — Manus, a general-purpose AI agent that’s getting global attention. Some are calling it the “most
sophisticated computer using AI,” while others write it off as just another “wrapper.”

So what sets Manus apart under the hood? What does its launch say about the broader debate around GPT “wrappers”?

Garry dives into Manus’ “chain-of-thought injection” technique that enables agents to actively update plans, what works
particularly well with its UI, and how founders can create enduring value with application-level products.

## Transcript

Speaker: Usable AI agents are finally here. From deep research platforms out of OpenAI and Google to similar tools from XAI and DeepSeek, joining the competition now is Manis, a brand new agentic AI platform that has taken the world by storm. And today we're launching an early preview of Manis, the first general AI agent.

Speaker: When Manis officially launched, the hype around it immediately took off. A Chinese startup unveiling a new AI agent that some are calling China's next DeepSeek moment, with people calling it the most impressive AI tool they've ever tried and the most sophisticated computer using AI. Unlike some of its predecessors, Manis wasn't just another specialized chatbot. It promised to be a true general-purpose AI agent. With invitations rare and access limited, the question remains: has Manis truly revolutionized the AI agent landscape? Let's find out.

Speaker: Behind all the excitement around Manis is something genuinely innovative: a multi-agent AI system that can seemingly complete all sorts of tasks, from travel planning and financial analysis to searching over dozens of files or doing industry research. So, how does it work? Rather than relying on one big neural network, Manis works more like an executive overseeing a team of sub-agents, coordinating and guiding their every move across a shared action space.

Speaker: It takes in your prompt as input and gets to work figuring out what it needs to do. Instead of tackling your task in one go, a planner agent first comes up with a master plan to follow, breaking things down into manageable subtasks. This way, Manis knows precisely what needs to be done before executing and can hand off these tasks to other sub-agents. These are like Manis's own in-house experts. They share the same context, but each has its own delineated domain from knowledge or memory to execution. Manis can call upon an extensive suite of 29 different integrated tools. Whether they're automating web navigation, securely running code, or pulling important information from files, Manis's sub-agents intelligently decide which tools to use.

Speaker: Finally, when each subtask is complete, the executor agent combines the outputs together into a final synthesized output for the user. Under the hood, Manis is powered by a pretty sophisticated dynamic task decomposition algorithm. This is what enables it to autonomously break down complex instructions into clear execution paths. To ensure stability even after dozens of rounds of reasoning and tool use, the Manis team developed an original technique called chain of thought injection, enabling agents to actively reflect and update plans.

Speaker: At its core, Manis makes use of Anthropic's Claude 3.7 Sonnet. Manis also features robust cross-platform execution capabilities thanks to its seamless integration with open source tools like YC company Browser Use for advanced website interaction and startup E2B's secure cloud sandbox environment. So what can Manis actually accomplish? Impressively, it can take on a wide range of real world tasks. It excels in scenarios like creating travel itineraries, detailed financial analyses, and educational content. While it can also assist with valuable tasks like structured database compilation, insurance policy comparisons, supplier sourcing, and even assisting with high-quality presentations.

Speaker: To truly measure Manis's capabilities, we can look at GAIA, a benchmark designed to challenge AI agents on reasoning, multimodal handling, web browsing, and tool proficiency. Humans typically score about 92%, whereas OpenAI's Deep Research, in comparison, scored about 74% at its best. Manis smashed the state-of-the-art on GAIA, scoring 86.5%, just a few points shy of the average human.

Speaker: Still, despite impressive benchmark performance, Manis has reignited a broader conversation about the nature of AI startups at the application layer: rappers. Some have dismissed Manis as merely a wrapper since it stitches together existing foundational models and various tool calls. But this dismissal overlooks an important reality. Most successful AI products today could also qualify as wrappers by this logic. Cursor and Windsurf, for example, integrate existing LLMs alongside external APIs and developer-focused tooling such as real-time code analysis and debugging utilities. Domain-specific agents like Harvey combine foundational models with legal-specific tool integrations: case law retrieval, compliance checks, and document analysis. Clearly, many useful applications do fit the wrapper mold. And for many developers, it makes sense to go this route.

Speaker: As Manis co-founder Yichao Peng told us himself, from day one, they decided to work orthogonally to model development, wanting to be excited rather than threatened by each new model release. What distinguishes successful wrappers from their less effective counterparts is typically a bunch of things: intuitive UI, proprietary evals, much more careful fine-tuning of foundational models, and thoughtfully designed multi-agent architectures. And this is a good example of that. Manis itself illustrates these trade-offs really well. On the positive side, its multi-agent orchestration helps deliver significantly lower per-task costs—around $2 a task—compared to integrated competitors like OpenAI's Deep Research. Manis also offers greater transparency and user control, letting users directly inspect, customize, or replace individual sub-agents and tool integrations, a degree of flexibility centralized platforms rarely match.

Speaker: One of the coolest things Manis figured out was actually exposing the file system so you could see exactly what the agents were doing. ChatGPT requires you to reprompt and it's opaque what's happening when it's thinking. Manis is a glimpse into the future of ChatGPT desktop, operating directly on your computer, and it will be cool to see how much more control you'll get when it's happening there instead of a browser.

Speaker: But there are a few clear limitations. Coordination across specialized agents becomes increasingly difficult as tasks scale or complexity grows. More critically, its current advantages—UX refinements, targeted fine-tuning, thoughtful integrations—are vulnerable to competitors just coming along and doing that as well. These strengths and weaknesses are generally shared by wrappers. They allow you to have really rapid deployment, iteration, and specialized UX at lower upfront cost, but they're also vulnerable to disruption such as API pricing changes or provider policy shifts, which can quickly erase any of the cost benefits.

Speaker: Ultimately, the critical challenge isn't deciding whether wrappers are viable, but identifying genuinely sustainable differentiation for your product. For founders, this might mean investing early in proprietary evals that are expensive or time-consuming to replicate, embedding your workflows deeply into specific user routines to increase switching costs, or identifying integrations with platforms or data sets competitors can't easily access. In the end, success in AI doesn't hinge on reinventing the wheel, but rather on who can stitch together the existing models into a product users genuinely love.
