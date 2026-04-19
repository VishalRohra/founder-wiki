# Founder Wiki — Query Guide

*This file is a curated view of [AGENTS.md](AGENTS.md) for query agents. AGENTS.md is the source of truth — update it first, then sync relevant changes here. See AGENTS.md > Development Lifecycle > Instruction-File Change Protocol for how the sync works.*

## Core Principle: The Wiki IS the Knowledge Base

**Never read `raw/`.** The wiki is the knowledge base. Every wiki article is rich enough to give you the full substance of what the source material says on that topic. Source links exist for provenance (where did this claim come from?), not for content (what did they actually say?).

If an article doesn't cover what the user asked, that's a gap to fix in absorption — not a reason to go to `raw/`. Say the wiki doesn't cover it and stop.

## Architecture (What's Where)

- `raw/` — Immutable source transcripts and posts. **Never read for query answers.**
- `wiki/` — The knowledge base. Your only data source.
- `wiki/_index.md` — Master catalog with aliases. Your entry point for every query.
- `wiki/_backlinks.json` — Reverse link index. Useful for discovering which articles cite a given concept.
- `wiki/_absorb_log.json` — Records which raw sources have been absorbed into which articles. Useful for provenance checks.

## How Content Is Organized

Content emerges from the data, not from a fixed taxonomy. Directories you will encounter:

- `topics/` — Thematic articles synthesized from multiple sources
- `frameworks/` — Named mental models and decision frameworks
- `case-studies/` — Deep dives on specific companies or events
- `speakers/` — First-class person pages

Every article is a node in a graph. Wikilinks (`[[Article Title]]`) are edges. An agent traversing 3-8 pages should encounter dozens of links — each one is a pathway to deeper context.

### People Are First-Class Nodes

Every speaker with 2+ sources has their own page. Use it when the question is "what does [Person] think about X?" A speaker page contains:

- Their worldview (what they consistently argue across sources)
- Their distinct perspective (how they differ from or complement others)
- Key frameworks they use (named models, recurring metaphors)
- References to every raw source that features them

Backlinks (on viewer pages, or via `_backlinks.json`) show every other article that references the speaker — a natural hub for "what has X said about everything?"

## Query Protocol

1. **Read `wiki/_index.md`.** Scan the aliases in parentheses for each article to find the 3-5 most relevant to the question.
2. **Read the matching articles.** Follow `[[wikilinks]]` 1-2 levels deep when that helps complete the answer.
3. **Check `wiki/_backlinks.json`** if you need to discover which articles most heavily reference a concept that lacks its own page.
4. **Synthesize an answer** using the content of those articles, with citations to specific sources.
5. **Never read `raw/`.** If the wiki articles don't have the detail you need, the answer is "the wiki doesn't cover this deeply — here's what it does say." Do not open raw sources.
6. **If the wiki doesn't cover the topic at all, say so.** Don't guess. Don't fill in from training data. The value of the wiki is that its answers are grounded in the source material it has absorbed.

**Query is read-only.** Do not modify wiki files during a query.

## The Content Character (So You Answer in Its Voice)

Wiki articles are **synthesized founder wisdom**, not Wikipedia-about-the-thing. An article on Hiring carries the accumulated advice from everyone who has spoken about hiring in the source material — with attribution, specific examples, and cross-references to related topics.

Answers to users should preserve the same character:

- **Attributed.** Say who said what ("Graham argues...", "Caldwell describes..."). Don't flatten multiple perspectives into a single voice.
- **Specific.** Preserve concrete examples, dollar figures, timelines, named companies. "Stripe took two weeks to set up a merchant account" is more useful than "payments integration was slow."
- **Direct quotes for texture.** Use direct quotes when they carry the speaker's voice or a memorable phrasing that paraphrase would flatten.
- **Consensus when it's load-bearing.** If 8 speakers across 15 sources all say the same thing, that's information — surface the convergence.
- **Disagreements when they exist.** If speakers disagree or an advice is conditional ("this works for B2B but not consumer"), preserve the nuance.

## Citation Format

Wiki articles use `[N]` footnotes in the body with a `## References` section at the bottom. When you cite sources in an answer, follow the same pattern.

**In the body:**

```
Graham argues that the way to get startup ideas is not to try to think of
them, but to notice problems — especially your own [1]. Caldwell extends
this with a scoring system: rate each idea 1-10 on how excited you are,
and only pursue 7.5+ [3].
```

**References section:**

```
## References

1. [How to Get Startup Ideas](https://www.ycombinator.com/library/8z-how-to-get-startup-ideas) — Paul Graham (November 2012)
3. [Where Do Great Startup Ideas Come From](https://www.ycombinator.com/library/DU-dalton-michael-where-do-great-startup-ideas-come-from) — Dalton Caldwell, Michael Seibel (2022)
```

Rules:

- Every factual claim, specific example, or direct quote has a footnote number.
- Inline attribution ("Graham argues...") provides voice; the footnote number provides provenance. Both work together.
- Each reference entry: linked title, URL, speaker name(s), publication date. Dates are mandatory.

## What to Do If the Wiki Is Thin

If an article exists but is thin, say what it covers and what it doesn't. Don't pad the answer with training-data content labeled as if it came from the wiki. The wiki's value is that its answers are grounded — diluting that breaks the contract.

If no article exists on the topic at all, say so directly. A gap is information: it tells the user (and the next absorption run) that a topic needs to be added.
