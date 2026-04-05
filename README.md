# founder-wiki

The compiled startup knowledge base. 350+ YC videos and 70+ blog posts, synthesized into a structured wiki that any LLM agent can navigate and query. No RAG, no embeddings, no vector DB. Just markdown files and an index.

## Inspiration

This project implements [Karpathy's LLM Knowledge Base](https://x.com/karpathy/status/2039805659525644595) pattern. The idea: instead of RAG over raw documents, an LLM **compiles raw sources into a persistent wiki** — structured, interlinked, and maintained like Wikipedia. The knowledge is compiled once and kept current, not re-derived on every query.

[Farzapedia](https://x.com/FarzaTV/status/2040563939797504467) demonstrated it with personal knowledge (2,500 diary entries into 400 articles). We're applying it to the entire public YC canon.

> "Every business has a raw/ directory. Nobody's ever compiled it. That's the product." — [@tammireddy](https://x.com/tammireddy)

## The Key Insight

An LLM navigating structured markdown files is better than RAG over the same content. Why?

**RAG** retrieves chunks. Chunks have no context. The LLM stitches them together on every query, and does it slightly differently each time. There's no memory, no cross-referencing, no accumulated understanding.

**A compiled wiki** is the opposite. The synthesis happens once, during absorption. Every article weaves together what 5, 10, 15 different speakers said about the same topic — with attribution, specific examples, direct quotes, and `[[wikilinks]]` connecting it to everything else in the graph. When an agent queries it, it's reading a finished knowledge base, not assembling one on the fly.

The wiki is a **knowledge graph in markdown**. Every page is a node. Every `[[wikilink]]` is an edge. The graph's density is what makes it valuable — an agent reading the article on Fundraising discovers it connects to Growth (because growth drives valuation), to Financial Survival (because runway determines negotiating position), and to Paul Graham (because he wrote the canonical essay on convincing investors). Those connections are pre-compiled. A RAG system would have to discover them each time.

## Why Not Just Ask an LLM?

An LLM already "knows" generic startup advice from its training data. But what it knows is a **flattened composite** — it can't tell you where an idea came from, how thinking evolved, or who disagrees with whom. founder-wiki adds:

**Citation chains.** Every claim traces to a specific talk, essay, or transcript. "Graham argues X" links to the actual essay. No hallucinated summaries.

**Cross-source synthesis.** The article on Startup Ideas weaves together what Paul Graham, Jared Friedman, Dalton Caldwell, Michael Seibel, and Stewart Butterfield each said — with their specific examples, frameworks, and disagreements. An LLM call gives you a generic composite. The wiki shows you the full picture.

**The long tail.** An obscure comment in a 2019 Startup School lecture, a specific anecdote from a founder interview, a nuanced aside in a Dalton & Michael episode — the model may not have encoded these, or may have blurred them into generic advice. The wiki preserves the specifics.

**Evolution over time.** People change their minds. Markets shift. The wiki captures the trajectory — what someone said in 2015 vs. 2024, and why it changed. An LLM flattens all of a person's views into one position.

**Consensus signals.** When 8 speakers across 15 years independently give the same advice, that convergence is information. The wiki surfaces it explicitly: "Talking to users is one of the most reinforced principles in the YC canon, cited by Graham, Seibel, Caldwell, Alstromer, and Hale across 12+ sources."

**Navigable structure.** Topics, frameworks, people, case studies — all interlinked. An agent can follow threads: start at Product-Market Fit, follow a link to the Schlep Filter framework, discover it connects to Startup Ideas, and surface a connection the user didn't think to ask about.

## Get Started

### 1. Clone the repo

```bash
git clone https://github.com/VishalRohra/founder-wiki.git
cd founder-wiki
```

### 2. Open your agent

```bash
claude  # or cursor, windsurf, codex — any agent that can read files
```

That's it. Your agent reads `AGENTS.md` automatically, which tells it: start at `wiki/_index.md`, navigate by `[[wikilinks]]`, synthesize answers from wiki articles, cite sources.

There is no setup. The repo is the product. `AGENTS.md` is the API.

### 3. Ask anything

```
> I feel like I'm too young to start a company. What do you think?

> What's the YC consensus on when to raise a Series A?

> How do Dalton and Michael's views on pivoting differ from PG's?

> I have 6 months of runway. What does YC say I should do?
```

## What Your Agent Does

When you ask a question, here's exactly what happens:

**Step 1: Scan the index.** The agent reads `wiki/_index.md` — a catalog of every article with aliases in parentheses. For "I feel too young to start a company," it matches:

- `[[Starting Young]]` — aliases: "young founders, age, when to start a startup" — **direct hit**, 5 sources
- `[[Becoming a Founder]]` — aliases: "should I start a startup" — relevant
- `[[Founder Mindset]]` — aliases: "founder qualities, determination" — adjacent
- `[[Paul Graham]]` — speaker page, wrote "Before the Startup" — context

**Step 2: Read 3-5 articles.** Each article is a rich synthesis — not a summary, but the full substance of what every source says about the topic. Specific examples, reasoning chains, direct quotes, cross-references.

**Step 3: Follow wikilinks.** The Starting Young article links to `[[Startup Ideas]]` (for Graham's "just learn and follow curiosity" advice for 20-year-olds) and to `[[Founder Mindset]]` (for what actually predicts founder success). The agent follows 1-2 links deep if needed.

**Step 4: Synthesize.** The agent gives you an answer grounded in the wiki — with citations to specific articles and their underlying sources. Not generic advice. Attributed, specific, cross-referenced advice.

Total: 4-6 file reads. No API calls, no embeddings, no vector search. Just an agent navigating structured markdown.

## Examples Where This Beats a Generic LLM Call

### "Should I pivot?"

**A generic LLM** gives you textbook advice about product-market fit signals.

**founder-wiki** gives you Dalton Caldwell's specific scoring system (rate ideas 1-10, pivot at 2.5, commit at 7.75), the Brex story (pivoted from VR to fintech in six weeks by scoring half a dozen ideas), Emmett Shear's distinction between vision pivots and strategy pivots, and the consensus from 6 speakers on what the actual pivot trigger is. With citations.

### "How do I price my product?"

**A generic LLM** tells you about value-based pricing and competitive analysis.

**founder-wiki** gives you Kevin Hale's specific pricing frameworks from Startup School, the 10x rule with named examples, the "charge more than you think" consensus (reinforced independently by Hale, Graham, and Seibel), and the specific mistakes YC companies made around pricing — with the company names and what happened.

### "What makes a good co-founder relationship?"

**A generic LLM** lists communication, complementary skills, shared vision.

**founder-wiki** gives you Harj Taggar's diagnostic questions ("If your co-founder left tomorrow, would you keep going?"), Michael Seibel's advice from running YC ("the #1 killer is co-founder conflict, not competition"), the equity split consensus, Paul Graham's "relentlessly resourceful" test applied to co-founders, and specific breakup stories from YC companies.

### "I'm a deep tech founder. Is YC right for me?"

**A generic LLM** gives a generic yes with caveats.

**founder-wiki** gives you Blake Scholl's story (Boom supersonic), the hard tech vs. software timeline differences, Anu Hariharan's biotech funding patterns, specific YC hard tech companies and what their early stages looked like, and the common mistake of over-building before talking to customers — with named examples from deep tech founders who made it and those who didn't.

## Architecture

Three layers:

```
raw/                           # Immutable source layer
  _sources.json                # Master manifest of all sources
  videos/{slug}.md             # Video transcripts (310 fetched, 35 pending)
  posts/{slug}.md              # Blog posts

wiki/                          # LLM-compiled knowledge graph
  _index.md                    # Agent entry point — the table of contents
  _backlinks.json              # Reverse link index
  _absorb_log.json             # Tracks which sources have been compiled
  topics/                      # Broad thematic articles
  frameworks/                  # Named mental models
  speakers/                    # People pages — worldview, key ideas, source inventory
  case-studies/                # Deep dives on specific companies
  {new directories}/           # Emerge as the data demands

AGENTS.md                      # Schema — tells any agent how the wiki works
```

The wiki structure follows **emergence, not prescription**. Directories, categories, and article types are created by the absorbing agent as the data demands. If the content suggests `mistakes/`, `metrics/`, `debates/`, or `timelines/` — those get created. The only organizing principle is: whatever makes the knowledge graph most navigable and richly connected.

## Source Material

### Current: Y Combinator Library
~350 videos + ~70 blog posts from [ycombinator.com/library](https://www.ycombinator.com/library). Startup School lectures, Dalton & Michael series, partner talks, PG essays, founder stories.

310 video transcripts fetched (curated page transcripts with speaker attribution). 35 pending (logged for retry). 70 blog posts ingested.

### Future Sources
- South Park Commons and founder communities
- Operator blogs and Twitter threads (Shreyas, DHH, Sahil, etc.)
- Podcast transcripts, books, essays
- New source types go in `raw/{source-type}/` — the wiki layer is source-agnostic

## Contributing

The most valuable contribution is **adding new raw sources**. The wiki gets richer with every source absorbed, and there's an enormous amount of founder wisdom that isn't in the YC library.

### How to contribute raw sources

1. **Find a source** — a blog post, transcript, video, podcast episode, essay. Anything with substantive startup/founder advice.

2. **Extract it** into a markdown file with YAML frontmatter:

```yaml
---
title: "The source title"
slug: "a-unique-slug"
media_type: "Blog" | "Video" | "Podcast" | ...
author: "Speaker Name"
speakers: ["Speaker 1", "Speaker 2"]
categories: ["Fundraising", "Growth"]
description: "One-line description"
url: "https://original-source-url"
---

# Title

{Full text content — transcript, essay, blog post. Not a summary.}
```

3. **Add it** to the appropriate `raw/` subdirectory. Create a new subdirectory if the source type doesn't exist yet (e.g., `raw/podcasts/`, `raw/essays/`).

4. **Open a PR** with just the raw source file(s). Don't modify `wiki/` — absorption is run centrally to maintain wiki quality and consistency.

### Why raw sources only?

Wiki compilation (absorption) is a nuanced process — it requires reading the full existing wiki, understanding cross-references, maintaining voice consistency, and deciding what deserves its own article vs. integration into an existing one. A bad absorption can fragment the wiki or create inconsistencies that are hard to undo.

By keeping contributions to raw sources, we get the best of both worlds:
- **Anyone can contribute content** — find a great founder talk? Extract the transcript and PR it.
- **Wiki quality stays high** — absorption runs are reviewed and maintain the graph's integrity.

Think of it like Wikipedia: anyone can contribute sources. Compilation into articles is a separate, careful process.

### What makes a good source to add?

- Substantive advice, not news or announcements
- Specific frameworks, examples, or stories — not generic platitudes
- Named speakers with a track record
- Ideally, content that cross-references topics already in the wiki (this creates the richest synthesis)

### Source ideas we'd love PRs for

- **Podcasts**: How I Built This, Acquired, The Twenty Minute VC, Lenny's Podcast
- **Blogs**: Paul Graham's remaining essays, Sam Altman's blog, First Round Review
- **Books**: excerpts from The Hard Thing About Hard Things, Zero to One, The Lean Startup
- **Twitter/X threads**: high-signal founder threads (Shreyas Doshi, Sahil Lavingia, etc.)
- **Talks**: Stanford ETL lectures, SPC talks, a16z content

## Build on Top of It

If you build an app, tool, or experience on top of founder-wiki, we'd love to hear about it. Some ideas:

- **Chat interface** — a web app where founders ask questions and get wiki-grounded answers
- **YC Office Hours simulator** — a persona that gives feedback on your idea/pitch grounded in the actual YC canon
- **Executive coaching agent** — structured coaching sessions pulling from leadership and management articles
- **Startup course generator** — curated learning paths assembled from wiki articles by stage
- **Pitch feedback tool** — submit your deck, get feedback grounded in Hale, Graham, and Tam's actual frameworks
- **Graph explorer** — visual knowledge graph showing connections between topics, people, and frameworks

If you build something, please:
1. Credit this repo as the knowledge source
2. Open an issue or PR to add your project to a showcase section here

We want to see what's possible when founder wisdom is structured, cited, and queryable.

## Related

This project emerged from the broader exploration in [wiki-of-you](https://github.com/VishalRohra/wiki-of-you), which documents the Karpathy/Farzapedia pattern, candidate profiles, selection criteria, and the full brainstorm of use cases.
