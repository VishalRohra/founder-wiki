---
title: Forward Deployed Engineers
type: topic
created: 2026-04-05
last_updated: 2026-04-05
aliases: ["FDE", "forward deployed engineer", "FDE playbook", "Palantir model", "founder as FDE", "vertical AI sales"]
related: ["[[Enterprise Sales]]", "[[Prompt Engineering]]", "[[AI-Native Software]]", "[[Doing Things That Don't Scale]]", "[[Garry Tan]]"]
sources: ["MS-state-of-the-art-prompting-for-ai-agents", "Mt-the-fde-playbook-for-ai-startups-with-bob-mcgrew"]
speakers_referenced: ["Garry Tan", "Jared Friedman", "Harj Taggar", "Bob McGrew"]
---

# Forward Deployed Engineers

The forward deployed engineer (FDE) model -- originating at Palantir and now the dominant go-to-market motion for vertical AI startups -- places engineers directly alongside end users to understand workflows, build custom solutions in real time, and close deals through demonstrated value rather than sales presentations [1] [2]. [[Garry Tan]] argues that every AI founder should think of themselves as a forward deployed engineer [1]. Bob McGrew, former Chief Research Officer at OpenAI, describes the FDE as the critical role for AI startups specifically because the last 5-10% of making an AI system work for a specific customer requires deep domain understanding that only comes from sitting next to the user [2].

## The Palantir Origin

[[Garry Tan]], who was early at Palantir, traces the FDE concept to a core insight shared by Peter Thiel, Alex Karp, and the other Palantir founders: if you go into any Fortune 500 company or government agency, "nobody who understands computer science and technology at the highest possible level would ever even be in that room" [1]. The problems those organizations face are multi-billion-dollar, sometimes trillion-dollar problems. They are awash in data but have no idea what to do with it [1].

The FDE title was created to solve a specific problem: how do you sit next to the FBI agent investigating domestic terrorism, see what the case coming in looks like, understand all the steps, observe that the actual artifacts are Word documents and Excel spreadsheets, and then convert those "file cabinet and fax machine things" into clean software [1]?

The difference from traditional enterprise sales: "Other companies would send a salesperson to go sit with the FBI agent. Palantir sent engineers" [1]. Instead of the next meeting being a review of 50 pages of sales documentation, "it's literally 'Okay, we built it.' And then you're getting real live feedback within days" [1].

This approach produced seven, eight, and eventually nine-figure contracts because the software was so immediately useful that "the second you see something that makes you feel seen, you want to buy it on the spot" [1].

## The AI-Era FDE

The FDE model has become even more powerful with AI because the turnaround time has collapsed [1]. In the pre-LLM era, Palantir needed a team of engineers and weeks to build a custom solution. Now, two founders can go into a meeting, take context about the customer's workflow, "stuff it basically in the prompt," and return the next day with a working demo that closes six or seven-figure deals [1].

Specific examples from YC:
- **Giger ML**: Two talented software engineers, "not natural salespeople," force themselves to be FDEs for customer support voice agents. They closed a deal with Zapier by having the most impressive demo, differentiating through technical innovation on the RAG pipeline for accurate, low-latency voice responses [1].
- **Happy Robot**: Sold seven-figure contracts to the top three largest logistics brokers in the world for AI voice agents. Started with six-figure deals, graduated to seven figures within months using the FDE model -- talking to CIOs, rapidly shipping product, and doing very fast turnaround [1].

## Why FDEs Win Against Incumbents

Tan describes the dynamic: "How does a really good engineer with a weak handshake beat [Salesforce, Oracle, Booz Allen]? You show them something that they've never seen before and make them feel super heard. You have to be super empathetic about it. You actually have to be a great designer and product person. And then come back and blow them away" [1].

The pre-AI enterprise sales model -- "hair and teeth" salespeople, steakhouse dinners, six-to-twelve-week sales cycles, software that never quite works -- loses to founders who can demonstrate working software customized to the specific customer's workflow within days [1].

## The FDE Playbook for AI Startups

Bob McGrew, having spent years building what became O1 and O3 at OpenAI, was "shocked" after leaving to find how few companies were actually using the technology. He expected "intelligence is too cheap to meter" euphoria; instead, most companies were "still on our quarterly roadmap unchanged from a year ago" [2].

McGrew's framework for AI startups emphasizes:
- The founder must be the FDE. You cannot outsource the deep customer understanding that makes the AI work [2].
- The evals (test suites for AI quality) are the true IP. They come from sitting next to users and understanding their workflow at a granular level [1].
- The vertical AI agent model works because domain expertise -- understanding the specific customer's reward function -- is the moat, not the model [1].

## Connection to YC Canon

The FDE model is a natural evolution of [[Doing Things That Don't Scale]]. Graham's consulting technique -- pick a single user and act as if you were building something just for them -- is precisely what FDEs do [3]. The Collison Installation (setting up Stripe on a user's laptop during the meeting) is the same motion [3].

The difference in the AI era: the FDE can customize the product during or immediately after the meeting by modifying prompts and tool configurations, rather than writing new code. This collapses the feedback loop from weeks to hours.

## References

1. [State-Of-The-Art Prompting For AI Agents](https://www.youtube.com/watch?v=DL82mGde6wo) -- [[Garry Tan]], [[Harj Taggar]], Diana Hu, [[Jared Friedman]] (2025)
2. [The FDE Playbook for AI Startups with Bob McGrew](https://www.youtube.com/watch?v=placeholder) -- Bob McGrew (2025)
3. [Do Things That Don't Scale](https://www.ycombinator.com/library/96-do-things-that-don-t-scale) -- [[Paul Graham]] (July 2013)
