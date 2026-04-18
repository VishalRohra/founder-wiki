# founder-wiki

The compiled startup knowledge base. 350+ YC videos and 70+ blog posts, synthesized into a structured wiki that any LLM agent can navigate and query. No RAG, no embeddings, no vector DB. Just markdown files and an index.

## Inspiration

This project implements [Karpathy's LLM Knowledge Base](https://x.com/karpathy/status/2039805659525644595) pattern. Instead of RAG over raw documents, an LLM **compiles raw sources into a persistent wiki** — structured, interlinked, and maintained like Wikipedia. The knowledge is compiled once and kept current, not re-derived on every query.

[Farzapedia](https://x.com/FarzaTV/status/2040563939797504467) demonstrated this with personal knowledge (2,500 diary entries into 400 articles). We applied it to the entire public YC canon.

## Why This Over a Generic LLM Call

An LLM already "knows" startup advice from training data. But what it knows is a **flattened composite** — it can't tell you where an idea came from, how thinking evolved, or who disagrees with whom.

**Grounded and verifiable.** Every claim traces to a specific talk, essay, or transcript. "Graham argues X" links to the actual essay. No hallucinated summaries. You can check the source yourself.

**Cross-source synthesis.** The article on Startup Ideas weaves together what Paul Graham, Jared Friedman, Dalton Caldwell, and Michael Seibel each said — with their specific examples, frameworks, and disagreements. An LLM gives you a generic composite. The wiki shows you the full picture.

**The long tail.** An obscure comment in a 2019 Startup School lecture, a specific anecdote from a founder interview, a nuanced aside in a Dalton & Michael episode — the model may not have encoded these. The wiki preserves the specifics.

**Evolution over time.** People change their minds. Markets shift. The wiki captures the trajectory — what someone said in 2015 vs. 2024, and why it changed.

**Consensus signals.** When 8 speakers across 15 years independently give the same advice, that convergence is information. The wiki surfaces it explicitly.

### Examples

**"Should I pivot?"** — A generic LLM gives textbook advice. founder-wiki gives you Dalton Caldwell's scoring system (rate ideas 1-10, pivot at 2.5), the Brex story (VR to fintech in six weeks), and the consensus from 6 speakers on pivot triggers. With citations.

**"How do I price my product?"** — A generic LLM says "value-based pricing." founder-wiki gives you Kevin Hale's pricing thermometer, the 10x rule with named companies, and the "charge more than you think" consensus reinforced independently by Hale, Graham, and Seibel.

**"What makes a good co-founder?"** — A generic LLM lists communication and shared vision. founder-wiki gives you Harj Taggar's diagnostic questions, Michael Seibel's advice on why co-founder conflict is the #1 startup killer, the equity split consensus, and specific breakup stories from YC companies.

## Get Started

### 1. Clone the repo

```bash
git clone https://github.com/VishalRohra/founder-wiki.git
cd founder-wiki
```

### 2. Point your agent at it

```bash
claude  # or cursor, windsurf, codex — any agent that can read files
```

The repo includes `CLAUDE.md` and `AGENTS.md` that tell your agent what this is and how to navigate it. It starts at `wiki/_index.md`, follows `[[wikilinks]]`, and cites sources.

There is no setup. The repo is the product. `AGENTS.md` is the API.

### 3. Ask anything

```
> I feel like I'm too young to start a company. What do you think?

> What's the YC consensus on when to raise a Series A?

> How do Dalton and Michael's views on pivoting differ from PG's?

> I have 6 months of runway. What does YC say I should do?
```

## Architecture

```
raw/                           # Immutable source layer
  _sources.json                # Manifest of all 416 sources
  videos/{slug}.md             # 310 video transcripts
  posts/{slug}.md              # 70 blog posts

wiki/                          # LLM-compiled knowledge graph
  _index.md                    # Agent entry point
  _backlinks.json              # Reverse link index
  topics/                      # 91 thematic articles
  speakers/                    # 43 people pages
  case-studies/                # 25 company deep-dives
  frameworks/                  # 14 named mental models

AGENTS.md                      # Schema — tells any agent how the wiki works
```

The wiki is a **knowledge graph in markdown**. Every page is a node. Every `[[wikilink]]` is an edge. The structure follows emergence, not prescription — directories and article types are created as the data demands.

**173 articles** compiled from 168 sources. 1,700+ wikilinks connecting them. 0 dead links.

## Contributing

The most valuable contribution is **adding new raw sources**. The wiki gets richer with every source absorbed.

### How to contribute

1. **Find a source** — a blog post, transcript, video, podcast episode, essay. Anything with substantive startup/founder advice.

2. **Extract it** into a markdown file with YAML frontmatter:

```yaml
---
title: "The source title"
slug: "a-unique-slug"
media_type: "Blog" | "Video" | "Podcast"
author: "Speaker Name"
speakers: ["Speaker 1", "Speaker 2"]
categories: ["Fundraising", "Growth"]
description: "One-line description"
url: "https://original-source-url"
---

# Title

{Full text content — transcript, essay, blog post. Not a summary.}
```

3. **Add it** to `raw/`. Create a new subdirectory if the source type doesn't exist yet (e.g., `raw/podcasts/`, `raw/essays/`).

4. **Open a PR** with just the raw source file(s). Don't modify `wiki/` — absorption is run centrally to maintain consistency.

### Source ideas we'd love PRs for

- **Podcasts**: How I Built This, Acquired, The Twenty Minute VC, Lenny's Podcast
- **Blogs**: Paul Graham's remaining essays, Sam Altman's blog, First Round Review
- **Books**: excerpts from The Hard Thing About Hard Things, Zero to One, The Lean Startup
- **Twitter/X threads**: high-signal founder threads (Shreyas Doshi, Sahil Lavingia, etc.)
- **Talks**: Stanford ETL lectures, South Park Commons talks, a16z content

## Build on Top of It

If you build an app, tool, or experience on top of founder-wiki, we'd love to hear about it. Some ideas:

- **Chat interface** — founders ask questions, get wiki-grounded answers
- **YC Office Hours simulator** — feedback on your idea grounded in the actual YC canon
- **Pitch feedback tool** — submit your deck, get feedback from Hale, Graham, and Tam's frameworks
- **Graph explorer** — visual knowledge graph of topics, people, and frameworks
- **Startup course generator** — learning paths assembled from wiki articles by stage

If you build something, credit this repo and open an issue to showcase it.
