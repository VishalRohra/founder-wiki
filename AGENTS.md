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
- **References**: which raw entries feature this person as a speaker or author, in the standard numbered References format.

People pages are enrichable over time — a person's background, career trajectory, external writing, and podcast appearances can all be layered in as new sources are added. The page is a living profile of how this person thinks about startups.

Create a person page when someone appears as a speaker/author in 2+ sources. These pages naturally interlink with every topic they've touched.

### Every Page is a Rich Link

Every wiki page should be densely linked to related pages. When you mention a concept that has its own page, use `[[wikilinks]]`. When you reference a person, link to their page. When a framework is mentioned in a topic article, link to the framework page. The wiki's value compounds through these connections — an agent traversing 3-8 pages should encounter dozens of links, each one a pathway to deeper context.

## Development Lifecycle

Two rules govern every change to this repo, regardless of what else you are working on. They exist because the `wiki/` folder is production data, and AGENTS.md is the source of truth every future agent will read.

### Pre-commit Verification

Before any commit that touches the `wiki/` folder, re-read the relevant sections of AGENTS.md and verify the staged changes actually follow the instructions. This is a hard gate, not a courtesy check. The check covers, at minimum:

1. **Structure.** Does every modified article still follow the article rendering structure (frontmatter → body → References → optional Backlinks)? Is any content accidentally appended *after* References?
2. **Synthesis.** Are new contributions woven into existing thematic sections (the default), or is there a per-source block that should have been integrated? If a per-source block exists, does it meet one of the case-by-case exceptions (see *Integration Over Appending* in Writing Standards)?
3. **Propagation.** Does `_absorb_log.json`'s `articles_touched` list every article that actually received substantive content? Is a multi-topic source enriching every relevant topic article, not just a single hub page?
4. **Citations and frontmatter.** References numbered correctly, publication dates present, `last_updated` bumped, and `sources` / `aliases` / `related` frontmatter current?
5. **JSON rebuild.** Are `viewer/articles.json` and `docs/articles.json` regenerated and in sync? The local rebuild in `absorb_batch.py:rebuild_viewer_json` captures git dates as of *before* the pending commit — so freshly edited files will show their previous commit date in the Recently Updated section until the next rebuild. A GitHub Action (`.github/workflows/refresh-articles-json.yml`) handles this automatically: after any push that touches `wiki/**` or `scripts/absorb_batch.py`, it rebuilds the JSON against the just-landed git state and commits a refresh. You should not manually run a second-commit JSON refresh anymore — the Action covers it.

If any check fails, rewrite the staged changes before commit. If the rule is ambiguous in context, ask the user — don't guess.

### Feedback Becomes Permanent Standards

When the user identifies a problem, requests a change, or points out an inconsistency — the relevant principle in this file MUST be updated immediately, in the same response. Do not wait for the user to ask. Do not treat feedback as a one-time fix. Every fix becomes a permanent standard so the same issue never recurs. This is non-negotiable.

The feedback loop is: user identifies issue → fix the issue → update AGENTS.md so the next agent does not repeat the mistake. If the user says "footnotes should scroll to references," update the Rendering Standards section. If the user says "dates should be in references," update the Citations section. If the user says "images are missing," update the Depth Standard. The update must follow the *Instruction-File Change Protocol* below — synthesize into the right existing section, not append a parallel bullet.

### Instruction-File Change Protocol

Any change to a markdown file that an agent reads as instruction (AGENTS.md, QUERY.md, CLAUDE.md, README.md, files under `.claude/skills/`) follows this protocol. Instruction files are the source of truth for every future agent run — incoherent instructions produce incoherent behavior.

1. **Scan for conflicts first.** Before proposing a new principle, bullet, or section, scan the target file for existing content on the same topic. If the new content duplicates, contradicts, or overlaps with existing content, flag the conflict.
2. **Ask the user to resolve.** Present the conflict with concrete options (keep A, keep B, merge, soften, delete). Do not pick a side silently.
3. **Synthesize, don't append.** After resolution, update the relevant existing section — do not add a parallel bullet that shadows the existing rule. A parallel log of "evolved standards" that contradicts the main spec will produce inconsistent agent behavior.
4. **No silent additions.** Never edit an instruction file in a way that future agents might interpret differently from existing content. If the change can't be made without a conflict check, it shouldn't be made in that turn.

### QUERY.md Sync

QUERY.md is a curated view of AGENTS.md for query agents — it contains only what a reader needs (Core Principle, Architecture, People pages, Query protocol, content character, citation format). AGENTS.md is the source of truth; QUERY.md is downstream.

Rules:

1. **AGENTS.md updates first.** Any change that affects query-agent behavior (how queries traverse the wiki, how content is organized, citation format, the character of articles, what to do when the wiki is thin) is made in AGENTS.md first, then synced into QUERY.md.
2. **Do not edit QUERY.md in isolation.** If you find a needed improvement while reading QUERY.md, update AGENTS.md, then reflect it in QUERY.md.
3. **Scope discipline.** Do not expand QUERY.md with build-side content. If a rule concerns absorption, synthesis, propagation, rendering standards, or lifecycle, it stays in AGENTS.md only.
4. **Sync check on every AGENTS.md change.** Before committing any AGENTS.md edit, ask: does this change query-relevant behavior? If yes, update QUERY.md in the same commit. If no, leave QUERY.md alone.

## Operations

### Query

1. Read `wiki/_index.md` — scan for relevant articles using aliases in parentheses
2. Read 3-8 relevant wiki articles, following `[[wikilinks]]` 1-2 links deep
3. Check `wiki/_backlinks.json` if you need to find highly-connected topics
4. Synthesize answer with citations to specific sources
5. **NEVER read raw/ entries.** The wiki IS the knowledge base. If the wiki doesn't have enough detail, that's a gap to fix in absorption — not a reason to go to raw.
6. If the wiki doesn't cover it, say so. Don't guess.
7. Query is **read-only** — don't modify wiki files.

### Absorb (add new sources to the wiki)

Absorption runs in **three phases** to balance speed (parallel agents) with graph consistency (no broken links, no duplicates, no orphans).

#### Phase 1: Draft (parallel, fast)

Multiple agents run simultaneously, each reading a batch of raw sources. Each agent writes articles to its own **isolated draft directory** (`wiki_draft_1/`, `wiki_draft_2/`, etc.) to avoid file conflicts. No agent reads another agent's output.

**Absorption coverage principle.** Every existing topic article that a source substantively addresses must be enriched in the same absorption run. If a source has N distinct ideas, absorption should touch ~N articles. Updating only the speaker page when the source covers hiring, leadership, productivity, and growth is an absorption failure, not a trade-off — the speaker page is a hub, but topic pages are where the knowledge actually gets queried. A single-article entry in `articles_touched` for a multi-topic source is a bug.

**Pre-write mapping step.** Before touching any wiki file, list every distinct idea, argument, or item in the source and map each to the specific wiki article(s) that should absorb it. Make that mapping explicit and visible in the absorption output — not an internal decision. Every article identified in the mapping must be updated in the same run, before commit.

**Ingestion metadata.** Extract all available metadata when creating the raw entry: dates, authors, speaker labels, tags, images, external links, duration. Store in frontmatter even if not immediately used — having the data available is better than needing to re-scrape.

Each agent:
1. Read the raw/ entries **in full**
2. Understand what each source means — not just facts but implications
3. Create articles organized by topic, framework, person, case study — whatever the data demands
4. **Preserve specificity.** Concrete examples, company names, dollar amounts, timelines, specific mistakes — all belong in the article. Don't abstract.
5. **Preserve images.** Reference images from raw sources using markdown image syntax.
6. **Preserve external hyperlinks.** Links to tools, papers, and related resources are part of the knowledge.
7. Use `[1]` footnote citations with `## References` section. Include publication dates.
8. Add `[[wikilinks]]` for every concept, person, or framework mentioned.
9. Create speaker/person pages for anyone appearing in 2+ sources.
10. Apply consensus signals where 3+ speakers agree.
11. Mark sources as absorbed in a local log.

#### Phase 2: Merge (single agent)

One agent reads ALL draft directories and the existing wiki, then produces the unified wiki:
1. **Deduplicate articles.** If multiple drafts created `fundraising.md`, merge them — combine material, deduplicate examples, unify the References section.
2. **Resolve conflicts.** If two drafts say different things about the same topic, preserve both perspectives with attribution.
3. **Combine speaker pages.** Merge source inventories across drafts.
4. Write unified articles to `wiki/`.
5. Update `wiki/_absorb_log.json` with all absorbed sources.

#### Phase 3: Propagate (single agent)

Graph propagation is mandatory. Every absorption must update all connected nodes — no orphan pages, no broken links, no stale cross-references. One agent ensures the graph is fully consistent:

1. **Find and fix all dead wikilinks.** For every `[[link]]` that references a nonexistent page, either create the page (if enough material exists across the wiki) or remove/rewrite the link.
2. **Ensure bidirectional linking.** If article A links to article B, check that B's backlinks include A. Update `wiki/_backlinks.json`.
3. **Create missing person pages.** Any speaker referenced in 2+ articles who lacks a page gets one.
4. **Co-speakers share sources.** When a video features multiple speakers (e.g., "Dalton & Michael"), every one of their speaker pages must list that video in the `sources` frontmatter field. If one speaker has it, the others must too.
5. **Update the index.** Rebuild `wiki/_index.md` with all articles, 1-2 sentence summaries, aliases, and source counts. Categories emerge from the actual wikilink graph.
6. **Audit article quality.** Spot-check the 5 most-connected articles. Are they rich enough to answer questions without going to source? Do they have consensus signals? Are images and external links included?
7. **Rebuild viewer.** Regenerate `viewer/articles.json` and sync to `docs/articles.json` so the live site reflects all changes immediately.
8. **Update repo-level counts.** Refresh article and source counts in `README.md` — the single source of truth for numbers. Also refresh the article count in `wiki/_index.md`. Do not duplicate counts into AGENTS.md or elsewhere; all other instruction files link to README.md's `Current coverage` section.
9. **Report.** Output a consistency report: total articles, dead links remaining (should be 0), orphan pages, articles without references.

This three-phase approach is the **default for every absorption run**, including future video transcripts, external blog posts, and any new source type. It is not optional — skipping Phase 3 produces an inconsistent wiki.

#### Auto-Parallelization Thresholds

When the number of sources to absorb exceeds 3, automatically use the three-phase pipeline with parallel agents. Do not process 4+ sources sequentially — parallelism is the answer to speed, not skipping steps.

| Sources | Mode |
|---------|------|
| 1-3 | Sequential (inline absorption, no draft directories) |
| 4-10 | Parallel: 2-3 agents, ~3-5 sources each |
| 11-25 | Parallel: 3-4 agents, ~6-8 sources each |
| 26+ | Parallel: 5-6 agents, ~10-13 sources each |

**Constraints validated empirically:**
- **Max ~13 sources per agent.** More than that and agents start skimming. 52 per agent produced F-grade absorptions; 10-13 per agent produced A-grade.
- **Balance by word count, not just source count.** Keep total words per agent under ~60K. A 25K-word transcript needs more room than a 2K-word one.
- **All agents read the existing wiki** before writing — this ensures they enrich existing articles rather than creating duplicates.
- **Draft directories prevent file conflicts.** Each agent writes to `wiki_draft_N/`. No two agents write to the same directory.
- **Clean up draft directories** after Phase 3 (`rm -rf wiki_draft_*`).

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

#### Speaker-Level Attribution

**Who says what matters.** Every insight must be attributed to the specific person who said it. This is non-negotiable.

**Collaborative discussions (e.g., Dalton & Michael):** When two speakers build on each other's point in real-time, attribute jointly: "Caldwell and Seibel argue that..." But when they make distinct contributions — Caldwell introduces a framework and Seibel adds a different example from his Twitch experience — attribute each separately: "Caldwell proposes the scoring system [3]. Seibel adds that at Twitch, they scored a 2.5 before pivoting [3]."

**Interviews:** When one person interviews another (e.g., Friedman interviews Scholl), only the advice-giver is the speaker. The interviewer gets credit only for their own observations, not for questions asked. The interviewer's speaker page does not need this video in its sources unless they contributed substantive insights.

**Speaker pages must reflect what that person specifically said.** A D&M video should update both Dalton's and Michael's speaker pages — but with different content. Dalton's page gets his frameworks and examples. Michael's page gets his frameworks and examples. If you can't tell who said what (auto-caption without labels), note this limitation.

**Co-speakers share sources in frontmatter.** The `sources` frontmatter array on every co-speaker's page must include the multi-speaker video. If Dalton's page has a D&M video, Michael's page must too — even if their inline content differs. Phase 3 propagation checks for this.

**Repeated examples across speakers:** When the same example (e.g., "Airbnb's early photos") is mentioned by 5 speakers across 5 videos, mention it once in the topic article with citations to all sources: [1][4][7][12][15]. This shows consensus without repetition. In speaker pages, include the example only if that speaker draws a unique lesson from it.

#### Transcript Quality

**Always check the YC library page for a curated transcript before falling back to YouTube auto-captions.** YC page transcripts are editorially reviewed and have proper speaker labels; auto-captions have transcription errors and no labels. The `transcript_source` field in frontmatter records which source was used (`yc_page` or `youtube_auto`).

**YC page transcripts** (transcript_source: "yc_page") have speaker labels and editorial review. Use direct quotes freely. Speaker attribution is reliable.

**YouTube auto-captions** (transcript_source: "youtube_auto") have transcription errors and no speaker labels. For single-speaker videos: absorb the ideas but use direct quotes cautiously (they may be garbled). For multi-speaker auto-caption videos without labels: **skip absorption and log them** as pending improved transcripts. Do not guess speaker attribution from auto-captions.

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

### Lint

Periodic maintenance pass that scans all articles for quality issues and fixes them. Run after every major absorption batch; can also be triggered manually.

Checks and fixes:
- **Duplicate citation sections** (Source Talks + References, or Source Inventory + References) -- merge into a single `## References` section
- **Image relevance audit** -- for each image, ask: does this convey something text cannot? Would an agent querying this article benefit from this image? If the answer is no, remove it. Diagrams, charts, and before/after comparisons earn their place. Decorative or redundant images do not.
- **Dead wikilinks** -- create stub pages if enough material exists, or rewrite as plain text
- **Missing dates in References entries** -- fill in from raw source frontmatter or URL metadata
- **Articles over 200 lines that should be split** -- identify natural sub-topics and extract into their own pages
- **Orphan pages with no inbound links** -- add wikilinks from related articles or flag for review
- **Speaker pages missing for people referenced in 3+ articles** -- create the page
- **Stale `last_updated` timestamps** -- update to reflect the most recent actual edit date
- **Frontmatter source counts must match References** -- if an article's References section lists 14 sources but the frontmatter `sources:` field has 0, rebuild the sources field from the References URLs. The viewer displays source counts from frontmatter, so mismatches make the home page inconsistent.

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
- **Images — selective and purposeful.** Include images only when they convey information that text cannot. For each image, ask: would an agent querying this knowledge base benefit from this image? If you can say it in text, say it in text. An image earns its place when it makes a concept immediately graspable in a way words cannot. For a pitch deck article, a few key slide examples that illustrate the principles are valuable — all 26 slides from the source are not.
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

## References

1. [Source Title](URL) — Speaker Name (Month Year)
2. [Source Title](URL) — Speaker Name (Month Year)
```

**Required frontmatter fields:** `title`, `type`, `created`, `last_updated`, `sources`. The `last_updated` field must be refreshed every time the article is modified — the viewer uses it to display "Last edited" timestamps.

### Key Principles

- Articles are **concept-centric**, not speaker-centric. Speakers are attribution. But speakers also get their own pages as first-class graph nodes.
- Cross-referencing the same idea across different speakers is the core value.
- Use **attributed synthesis**: weave multiple speakers' views into one coherent article. Don't just list "Speaker A says X, Speaker B says Y." Show how the perspectives build on, complement, or contradict each other.
- **Integration over appending.** When a new source contributes to an existing article, default to inline attributed synthesis — find the existing thematic section the contribution fits into, add 1-3 sentences of synthesis that connects the new voice to what's already there, and drop the `[N]` citation into that paragraph. Points from the same source do not cluster together just because they came from the same source; each point finds its own home. Per-source sections (e.g. "How to Succeed with a Startup (2018 Talk)") are acceptable on a case-by-case basis when (a) the source shows evolution of one person's thinking across a major work, (b) the source is a discrete lecture best treated as a unit, or (c) a new short article is being created around a distinct topic where inline doesn't apply. Default is integration; per-source blocks are the exception, not the pattern.
- Use `[[wikilinks]]` for all cross-references between articles — including person pages.
- **Aliases in frontmatter are critical** — this is how queries match to articles.
- Every article must have a References section listing which raw entries contributed.
- Don't create one article per video/post. Synthesize across sources.

### Structure by Article Type

| Type | Organize by |
|------|------------|
| topic | Thematic sections (definition, common mistakes, practical advice, related frameworks) |
| framework | The model itself, how to apply it, examples, limitations |
| stage | What to focus on, common mistakes, how to know you're ready to move on |
| speaker | Worldview, distinct perspective, key frameworks, references |
| series | What the series covers, structure, key topics touched |
| (new types) | Whatever organization the data demands |

### No Length Caps

There are no maximum length targets. An article is as long as it needs to be to carry the full substance of what the sources say about the topic. A major topic like Fundraising that draws from 15+ sources might be 300+ lines. A narrow framework from a single source might be 40 lines. The test is not "is it short enough?" but "could an agent answer a real question from this article alone?"

**Keep articles unified, use sections.** When an article grows long (200+ lines) because many speakers address the same topic, do NOT split it. Use well-structured sections so agents can navigate. A 300-line Fundraising article with clear sections is better than 3 separate articles an agent has to find and cross-reference.

**Thin articles are fine if distinct.** A 25-line article on a genuinely distinct topic (e.g., "Startup Legal Mechanics") is acceptable. The test is distinctness, not length. If it's a truly separate concept, it deserves its own page even if small. But if a video only produces content that fits naturally into an existing article, fold it in rather than creating a thin orphan.

## Rendering Standards

The wiki is **agent-first, human-readable**. The markdown files are the product — they must be fully useful to an agent via CLI or API without any viewer. The Wikipedia-style viewer is a visualization layer on top. If the viewer broke, the wiki should still be completely functional.

This means: optimize the markdown structure for agent navigation (clean frontmatter, consistent headings, reliable wikilink patterns, parseable reference sections). The viewer renders what the markdown already expresses — it doesn't add information.

### Citations: Wikipedia-Style Footnotes

Use numbered footnote references in the article body, with a References section at the bottom.

**In the body:**
```
Graham argues that the way to get startup ideas is not to try to think of them,
but to notice problems — especially your own [1]. The verb is "notice," not
"think up." Organic ideas grown from the founder's own experience are almost
always stronger than ideas generated on demand [1].

Caldwell extends this with a scoring system: rate each idea 1-10 on how
excited you are, and only pursue 7.5+ [3].
```

**At the bottom (References section):**
```
## References

1. [How to Get Startup Ideas](https://www.ycombinator.com/library/8z-how-to-get-startup-ideas) — Paul Graham (November 2012)
2. [The 18 Mistakes That Kill Startups](https://www.ycombinator.com/library/8t-the-18-mistakes-that-kill-startups) — Paul Graham (October 2006)
3. [Where Do Great Startup Ideas Come From](https://www.ycombinator.com/library/DU-dalton-michael-where-do-great-startup-ideas-come-from) — Dalton Caldwell, Michael Seibel (2022)
```

**Why this format:**
- Numbered references are scannable — an agent or human can quickly see how many sources support a claim.
- The References section doubles as a bibliography — it shows at a glance every source that contributed, who spoke, and links to the original.
- Inline attribution ("Graham argues...") provides the human voice. The footnote number provides the provenance. Both work together.

**Rules:**
- Every factual claim, specific example, or direct quote must have a footnote number.
- The same source can be referenced multiple times with the same number.
- References are numbered in order of first appearance in the article.
- Each reference entry includes: linked title, URL, and speaker/author name(s).
- Speaker names in references should link to their person page if one exists.
- **Publication dates are mandatory.** Format: `1. [Source Title](URL) — Speaker Name (Month Year)`. Extract the date from the raw source's frontmatter or body text. If no month is available, use the year from the URL or other metadata. Dates provide temporal context for advice that may evolve and are never optional.
- **Only one citation section per article.** Use `## References` with `[N]` footnotes. Never create a parallel `## Source Talks` table or other citation block. If both exist, merge into References only.

### References Section (Replaces Source Talks Table)

The old Source Talks table is replaced by the References section described above. This is more Wikipedia-standard and serves both audiences better:

- **For agents:** parseable numbered list with URLs and speaker names.
- **For humans:** a clean bibliography at the bottom of every article.

The References section format:
```
## References

1. [Source Title](URL) — Speaker Name, Speaker Name
2. [Source Title](URL) — Speaker Name
```

Group by number, not by speaker. The numbering matches the inline `[1]` `[2]` references in the body text.

### Article Rendering Structure

Every article, when rendered, should have these visual sections (in order):

1. **Title** (h1)
2. **Metadata line** — article type, key speakers, source count
3. **Table of Contents** — auto-generated from h2 headings, numbered, Wikipedia-style box
4. **Body** — the article content with inline `[1]` citations and `[[wikilinks]]`
5. **References** — numbered list of all sources cited
6. **Backlinks** — auto-generated list of "Pages that link here"

**Never add content after `## References`.** This is non-negotiable. Any edit that appends a new section below the References list is broken and must be redone before commit — new content goes into the relevant body section above References, and the citation is added to the References list in place.

### Wikilink Rendering

`[[Article Title]]` renders as a clickable link to that article. `[[Article Title|display text]]` renders with custom display text. Dead links (referencing articles that don't exist yet) should render in red — this signals gaps in the wiki that need to be filled.

### Viewer Principles

The viewer is intentionally simple — navigation, search, and article rendering. No interactive features beyond these for now. The architecture supports future additions (graph view, query interface) because the underlying data (wikilinks, backlinks, rich index) is already structured for them.

- **Home page:** Browse by category (categories emerge from the graph, reflected in `_index.md`)
- **Article pages:** Table of Contents, body with rendered wikilinks and citations, References, Backlinks
- **Search:** Matches against titles, aliases, and body text
- **Sidebar:** Navigation organized by the categories in `_index.md`
- **Hash-based navigation (`#slug`) is required.** The site is served as static files on GitHub Pages. Hash routing is the only approach that works with static hosting — query params (`?article=slug`) fail on reload because there is no server to parse them. Hash URLs persist on reload, work with back/forward, and are shareable. Do not change this.
- **Last edited timestamps link to GitHub.** The "Last edited" date on each article page links to the GitHub commits page for that file, providing full version history. Every commit to `wiki/` is a version; the viewer reconstructs history from `git log`.
- **Fully dynamic rendering.** No hardcoded article lists, categories, or slugs anywhere in the viewer. Everything renders from `articles.json`, `_index.md`, and `_backlinks.json`. New articles appear automatically after a JSON rebuild — no viewer code edits required.
- **Image rendering.** Images are rendered as small Wikipedia-style thumbnails floated right, max 220px wide. Curation (see *Depth Standard* under Writing Standards) decides which images to include; the viewer decides how they appear.

## Source Material

Current corpus and current counts live in [README.md](README.md#current-coverage) — treat it as the single source of truth so numbers never drift across instruction files. In short: the primary source is the [YC Startup Library](https://www.ycombinator.com/library), with a growing tail of external sources (Sam Altman's personal blog is the first). A substantial portion of fetched sources remain unabsorbed in `raw/` — mostly Lightcone Podcast episodes, AI/tech deep-dives, design reviews, and founder interviews.

### Future Extensions
- South Park Commons and similar founder communities
- Operator blogs and Twitter threads (Shreyas, DHH, Sahil, etc.)
- Additional podcast transcripts, books, essays
- New source types go in `raw/{source-type}/` — the wiki layer is source-agnostic
