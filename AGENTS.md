# Founder Wiki — Agent Schema

A compiled, queryable knowledge base of startup and founder wisdom. Built using the LLM Knowledge Base pattern (Karpathy) — raw sources are compiled by an LLM into a structured, interlinked wiki of markdown files. No RAG, no embeddings. The agent navigates structured markdown via an index.

## Core Principle: The Wiki IS the Knowledge Base

**An agent querying this wiki should never need to read `raw/`.** Every wiki article must be rich enough — in detail, specificity, examples, reasoning, and attribution — that reading the article gives you the full substance of what the source material contains on that topic. Source links exist for **provenance** (where did this claim come from?), not for **content** (what did they actually say?).

This means wiki articles are not summaries. They are **detailed, synthesized compilations** that preserve the texture of the original advice: specific examples, concrete numbers, named companies, reasoning chains, memorable phrasing, and direct quotes. A reader of the wiki article should come away with the same understanding they would get from reading every source that contributed to it.

If an agent has to follow source links to get the actual substance, the article has failed.

## Architecture

Three layers:
- `raw/` — Immutable source transcripts and posts. One .md per source. Never modify after ingest. Includes images, hyperlinks, and all media from the original.
- `wiki/` — LLM-compiled articles. The knowledge base. The LLM owns this layer entirely.
- `AGENTS.md` — This file. Schema, conventions, and the evolving set of standards for absorption quality.

## Directory Map

```
raw/
  _sources.json          # Master manifest of all ingested sources
  videos/{slug}.md       # Video transcripts with YAML frontmatter
  posts/{slug}.md        # Blog posts with YAML frontmatter

wiki/
  _index.md              # Master catalog — the agent's entry point
  _backlinks.json        # Reverse link index (auto-generated)
  _absorb_log.json       # Tracks which raw entries have been absorbed
  {directories}/         # Emerge organically from absorption
```

## Emergence, Not Prescription

**The LLM decides what articles to create, what directories to make, what to link, and how to organize.** There is no fixed directory structure. Directories and article types emerge from the data as the wiki grows.

Some patterns that have emerged so far:
- `topics/` — Broad thematic articles synthesized from multiple sources
- `frameworks/` — Named mental models and decision frameworks
- `case-studies/` — Deep dives on specific companies or events
- `speakers/` — People pages (see below)

But these are descriptive, not prescriptive. If the data demands `mistakes/`, `metrics/`, `industries/`, `debates/`, `timelines/`, or anything else — create them. Every article is a node in a relationship graph. The organizing principle is **whatever makes the graph most navigable and richly connected.**

### People as First-Class Nodes

People pages are not optional routing stubs. They are **first-class nodes in the knowledge graph**, just like topic or framework pages. A person page should contain:

- **Their worldview**: what they consistently believe, argue for, and return to across multiple talks/posts. Not a bio — a synthesis of their thinking.
- **Their distinct perspective**: how their advice differs from or complements others. What makes their lens unique.
- **Key frameworks they use**: named models, recurring metaphors, diagnostic questions they teach.
- **Backlinks**: auto-generated list of every wiki article that references them. This makes the person page a natural hub for "what has X said about everything?"
- **Source inventory**: which raw entries feature this person as a speaker or author.

People pages are enrichable over time — a person's background, career trajectory, external writing, and podcast appearances can all be layered in as new sources are added. The page is a living profile of how this person thinks about startups.

Create a person page when someone appears as a speaker/author in 2+ sources. These pages naturally interlink with every topic they've touched.

### Every Page is a Rich Link

Every wiki page should be densely linked to related pages. When you mention a concept that has its own page, use `[[wikilinks]]`. When you reference a person, link to their page. When a framework is mentioned in a topic article, link to the framework page. The wiki's value compounds through these connections — an agent traversing 3-8 pages should encounter dozens of links, each one a pathway to deeper context.

## Operations

### Query

1. Read `wiki/_index.md` — scan for relevant articles using aliases in parentheses
2. Read 3-8 relevant wiki articles, following `[[wikilinks]]` 1-2 links deep
3. Check `wiki/_backlinks.json` if you need to find highly-connected topics
4. Synthesize answer with citations to specific sources
5. **NEVER read raw/ entries.** The wiki IS the knowledge base. If the wiki doesn't have enough detail, that's a gap to fix in absorption — not a reason to go to raw.
6. If the wiki doesn't cover it, say so. Don't guess.
7. Query is **read-only** — don't modify wiki files.

### Absorb (add new source to the wiki)

1. Read the raw/ entry **in full** — understand the complete source, not just the highlights
2. Read `wiki/_index.md` to understand current structure
3. Understand what the source means — not just "what facts does it contain" but "what does this tell us?"
4. For each topic, framework, person, or entity the source touches:
   a. If an article exists: **re-read it fully**, then integrate the new material so the article reads as a coherent whole. Add the specific examples, reasoning, and quotes — not just a one-line summary of the new source's position.
   b. If no article exists and there's enough material: create one in whatever directory makes sense. Create a new directory if no existing one fits.
5. **Preserve specificity.** When a source gives a concrete example (a company name, a dollar amount, a timeline, a specific mistake), that example belongs in the wiki article. Don't abstract "Brex pivoted from VR headsets to fintech in six weeks by scoring ideas on four criteria" into "founders should evaluate ideas systematically."
6. **Preserve images.** If the raw source contains images (diagrams, charts, screenshots), reference them in the wiki article using markdown image syntax. Images are content.
7. **Preserve external hyperlinks.** If the raw source links to external resources (blog posts, tools, research papers), preserve those links in the wiki article. They are part of the knowledge.
8. Connect to patterns — when the same theme surfaces across multiple sources, that deserves its own article
9. Create or update person pages for speakers/authors
10. Update `wiki/_index.md` with any new articles (include aliases)
11. Mark source as absorbed in `wiki/_absorb_log.json`

**Anti-cramming:** If you're adding a third paragraph about a sub-topic to an existing article, that sub-topic probably deserves its own page.

**Anti-thinning:** Creating a page is not the win. Enriching it is. Every time you touch a page, it should get richer. Never add a source to an article with just one sentence of contribution — if the source has something to say on the topic, give it the space it needs.

**Anti-summarizing:** The most common failure mode is writing thin summaries instead of rich synthesis. If your article reads like an annotated bibliography ("Graham says X. Seibel says Y. Caldwell says Z."), you've failed. But if it reads like a textbook chapter that happens to have inline citations — detailed, specific, full of examples — you've succeeded.

**Checkpoint every 15 entries:**
1. Rebuild `wiki/_index.md` with all articles and aliases
2. Rebuild `wiki/_backlinks.json`
3. New article audit: if zero new articles in the last 15, you're cramming
4. Quality audit: pick 3 most-updated articles. Re-read each as a whole piece:
   - Is it rich enough to answer a real question without going to source? If you had to check a source link to understand a point, the article needs more detail.
   - Does it preserve specific examples, numbers, company names, and reasoning chains from the sources?
   - Does it use attribution ("Dalton describes PMF as...") not assertion?
   - Are images and external links from the sources included?
   - Are all people mentioned linked to their person pages?
   - If it reads like an event log or annotated bibliography, rewrite it as a coherent piece.
5. Check directory structure — create new directories if they'd improve navigability
6. Check for missing person pages — any speaker referenced in 2+ articles who lacks their own page

### Synthesis and Structure

Absorption is not just extraction — it is **compilation**. The value of this wiki over raw sources or an LLM's training data is the synthesis: cross-pollinated insights, consensus signals, evolution over time, and a navigable graph that an agent can traverse efficiently. These principles govern how material is structured during absorption.

#### Consensus Signals

When multiple speakers independently give the same advice, that convergence is information. Surface it explicitly:

> "Talking to users is one of the most reinforced principles in the YC canon, cited by [[Paul Graham]], [[Michael Seibel]], [[Dalton Caldwell]], [[Gustaf Alströmer]], and [[Kevin Hale]] across 12+ sources."

The frequency and breadth of agreement tells the reader (or agent) how load-bearing a piece of advice is. A principle mentioned by one person in one talk is interesting. A principle mentioned by eight people across fifteen years is canonical.

**How to handle it:**
- When 3+ speakers independently reinforce a point, note the consensus explicitly with names and approximate source count.
- Still attribute individual perspectives where they add unique reasoning, examples, or nuance. Consensus does not flatten individual contributions — it elevates the shared insight while preserving what each person uniquely brings.
- When a point has near-universal agreement, lead with the consensus, then unpack individual perspectives below.

#### Evolution Over Time

People change their minds. Markets shift. What was true in 2012 may not be true in 2025. The wiki should capture both the current state and, when instructive, the trajectory.

**Default:** Use the speaker's most recent position as the primary synthesis. If someone said X in 2015 and Y in 2024, the article reflects Y.

**Exception:** When the evolution itself teaches something — someone was wrong and corrected course, the world changed and invalidated prior advice, or the shift reveals a deeper pattern — surface the timeline explicitly:

> "Altman argued in 2015 that X. By 2023, after seeing Y, his position shifted to Z. The change reflects a broader pattern: [insight about why the landscape shifted]."

This is one of the wiki's strongest differentiators from base model knowledge. The model flattens a person's views into a composite. The wiki preserves the arc.

#### The Graph, Not the List

The wiki is a **knowledge graph**, not a collection of articles. Every page is a node. Every wikilink is an edge. The graph's density and navigability are what make it valuable.

**Principles:**
- **Every mention of a concept, person, or framework that has its own page gets a `[[wikilink]]`.** No exceptions. If you write "Graham" and there's a `[[Paul Graham]]` page, link it. If you mention "product-market fit" and there's a `[[Product-Market Fit]]` page, link it.
- **Backlinks are as important as forward links.** When an agent reads a page, the backlinks section tells it "here are all the other pages that reference this concept." This is how agents discover connections they didn't know to ask about.
- **Cross-references compound.** An article on Pricing that links to Growth, Product-Market Fit, Fundraising, and Sales creates five navigable pathways. An agent asking about pricing discovers it connects to fundraising (pricing affects valuation) and PMF (pricing as a signal of value). These connections are the wiki's core value.

#### Categories Emerge from the Graph

Do not impose top-down categories. Let the graph structure emerge from the articles' actual connections.

**What this means in practice:**
- The `_index.md` organizes articles by whatever groupings the wikilink graph suggests. If five articles all heavily cross-reference each other, they belong in the same section of the index — regardless of whether that section maps to a pre-defined "stage."
- Articles can belong to multiple conceptual groups. Pricing connects to Growth, to Fundraising, and to Product. The index can reference it in multiple sections.
- New directories and groupings emerge as the wiki grows. If three case studies get created, a `case-studies/` directory emerges. If deep tech content accumulates, `biotech-and-deep-tech/` emerges. Don't plan the taxonomy — let it grow.
- Periodically review the graph: are there clusters of tightly-linked articles that suggest a new organizing category? Are there orphan articles that need more connections?

#### The Index as a Rich Map

The `_index.md` is what agents read first. It must be rich enough that an agent can determine which 3-5 articles to read for any query — without opening any of them.

**Each entry should include:**
- The article title as a `[[wikilink]]`
- Aliases in parentheses for fuzzy matching
- A 1-2 sentence summary of what the article covers and what kind of questions it answers
- Source count (how many raw sources contribute to this article)

**Example:**
```
- [[Startup Ideas]] (idea generation, finding ideas, schlep filter, tarpit ideas, SISP)
  How to find, evaluate, and validate startup ideas. Covers Graham's organic discovery method,
  the well model, dangerous filters, and Caldwell's idea quality scoring. [12 sources]
```

This is a detailed table of contents, not just chapter titles. An agent scanning this for "how do I know if my idea is good?" should immediately identify Startup Ideas as the right article.

#### Importance and Weight

Not all advice is equally important. The wiki should signal what matters most:

- **Consensus breadth** naturally elevates important advice. If 8 speakers across 15 sources all say "talk to users before building," that principle is structurally prominent in the article — it appears early, gets the most space, and is explicitly flagged as consensus.
- **Specificity creates weight.** An abstract principle ("focus on users") carries less weight than a specific, actionable framework ("ask these 5 questions in every user interview"). Prioritize the specific.
- **Stories carry weight.** A named example (Airbnb's pivot, Stripe's Collison Installation) is more memorable and useful than a general principle. When a story illustrates a principle, lead with the story.
- **Sections within articles are ordered by importance**, not by source order or chronology. The most critical, most-reinforced advice goes first. Niche or conditional advice goes later.

### Cleanup

Audit and enrich existing articles:
- Is each article theme-driven or diary-driven? Restructure if needed.
- Are wikilinks correct and bidirectional?
- Are images and external links from sources included?
- Any topics mentioned across 3+ articles that lack their own page?
- Any stubs that should be enriched or merged?
- Any people referenced in 3+ articles who lack a person page?

### Breakdown

Find and create missing articles:
- Survey: bare directories, bloated articles, high-reference backlink targets without articles
- Extract concrete entities (the concrete noun test: "X is a ___") — people, companies, frameworks, events
- Rank by reference count, create in priority order
- Every new article should link back to existing articles that mention it

## Writing Standards

### The Golden Rule

**This is not Wikipedia about the thing. This is the synthesized founder wisdom on the thing.**

A page about "Hiring" isn't a generic article about hiring. It's the accumulated, cross-referenced advice from everyone who's spoken about hiring in the source material — with attribution, citations, specific examples, and connections to related topics. A reader should finish the article knowing what every major contributor to this wiki thinks about hiring, why they think it, what specific stories they tell, and how their perspectives relate to each other.

### Depth Standard

**The wiki replaces the raw sources for querying purposes.** This means articles must carry the full substance:

- **Reasoning chains, not just conclusions.** Don't write "Graham argues that organic ideas are better." Write out WHY he argues this — the specific logic, the examples he uses, the counterarguments he addresses.
- **Concrete examples, always.** If a source mentions a company, a dollar figure, a timeline, a specific founder decision — that goes in the wiki article. "Stripe took two weeks to set up a merchant account" is more useful than "payments integration was slow."
- **Direct quotes for texture.** Use direct quotes generously when they carry insight, voice, or emphasis that paraphrasing would flatten. No artificial cap on quotes per article — use as many as the article needs to be substantive.
- **Images and media.** Reference diagrams, charts, screenshots, and other visual content from sources. Use markdown image syntax.
- **External links.** When sources reference external resources, preserve those links. They are part of the knowledge graph.
- **Disagreements and nuance.** When speakers disagree, show the disagreement. When advice is conditional ("this works for B2B but not consumer"), preserve the conditions.

### Voice

Wikipedia-style. Flat, factual, encyclopedic. State what was said and by whom. Direct quotes from source material carry the emotional weight.

**Never use:** em dashes, peacock words ("legendary," "visionary," "groundbreaking," "deeply"), editorial voice ("interestingly," "importantly," "it should be noted"), rhetorical questions, progressive narrative ("would go on to," "embarked on"), qualifiers ("genuine," "raw," "profound").

**Do:** Lead with the subject, state facts plainly. One claim per sentence. Short sentences. Simple past or present tense. Attribution over assertion ("Dalton describes PMF as..." not "PMF is..."). Let facts imply significance. Dates and specifics replace adjectives.

**One exception:** Direct quotes carry the speaker's voice. The article is neutral. The quotes do the feeling.

### Article Format

```yaml
---
title: Article Title
type: topic | framework | stage | speaker | series | ...
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
aliases: ["PMF", "product market fit", "finding PMF"]
related: ["[[Other Article]]", "[[Another]]"]
sources: ["source-slug-1", "source-slug-2"]
speakers_referenced: ["Dalton Caldwell", "Michael Seibel"]
---

# Article Title

{Content organized by theme, not chronology or speaker}

## Sections as needed

## Source Talks

| Source | Speaker | Key Point |
|--------|---------|-----------|
| source-slug | Speaker Name | One-line summary of what this source contributed |
```

### Key Principles

- Articles are **concept-centric**, not speaker-centric. Speakers are attribution. But speakers also get their own pages as first-class graph nodes.
- Cross-referencing the same idea across different speakers is the core value.
- Use **attributed synthesis**: weave multiple speakers' views into one coherent article. Don't just list "Speaker A says X, Speaker B says Y." Show how the perspectives build on, complement, or contradict each other.
- Use `[[wikilinks]]` for all cross-references between articles — including person pages.
- **Aliases in frontmatter are critical** — this is how queries match to articles.
- Every article must have a Source Talks table listing which raw entries contributed.
- Don't create one article per video/post. Synthesize across sources.

### Structure by Article Type

| Type | Organize by |
|------|------------|
| topic | Thematic sections (definition, common mistakes, practical advice, related frameworks) |
| framework | The model itself, how to apply it, examples, limitations |
| stage | What to focus on, common mistakes, how to know you're ready to move on |
| speaker | Worldview, distinct perspective, key frameworks, source inventory |
| series | What the series covers, structure, key topics touched |
| (new types) | Whatever organization the data demands |

### No Length Caps

There are no maximum length targets. An article is as long as it needs to be to carry the full substance of what the sources say about the topic. A major topic like Fundraising that draws from 15+ sources might be 300+ lines. A narrow framework from a single source might be 40 lines. The test is not "is it short enough?" but "could an agent answer a real question from this article alone?"

Minimums still apply — don't create stub pages with fewer than 20 lines of real content. If there isn't enough material for a substantive page, fold the content into a broader article.

## Feedback and Standards Evolution

This file is a living document. As the wiki is built and queried, patterns emerge about what works and what doesn't. When feedback is given about absorption quality — articles too thin, missing images, links not preserved, speaker attribution wrong — the relevant standards in this file should be updated.

Current evolved standards (from feedback during initial absorption):
- **Preserve images from blog posts** — they are content, not decoration. Reference them with markdown image syntax.
- **Preserve hyperlinks from source material** — if a blog post links to a tool, paper, or related post, that link belongs in the wiki article.
- **Articles should be rich enough to replace reading the source** — if an agent has to click through to raw/ to understand a point, the article has failed.
- **People are graph nodes** — create person pages, not just inline mentions.
- **Directories emerge freely** — don't force content into existing categories. Create new directories when the data demands it.

When new feedback arrives, add it to this section and update the relevant standards above. This ensures every absorption run benefits from all prior feedback.

## Source Material

### Current: Y Combinator Library
~350 videos + ~70 blog posts from ycombinator.com/library. Includes Startup School lectures, Dalton & Michael series, partner talks, PG essays, founder stories.

### Future Extensions
- South Park Commons and similar founder communities
- Operator blogs and Twitter threads (Shreyas, DHH, Sahil, etc.)
- Additional podcast transcripts, books, essays
- New source types go in `raw/{source-type}/` — the wiki layer is source-agnostic
