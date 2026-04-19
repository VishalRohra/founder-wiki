"""
Automated wiki absorption pipeline.

Reads raw sources, sends them to Claude API with the current wiki state,
and writes/updates wiki articles based on the LLM's decisions.

Usage:
  python scripts/absorb_batch.py                    # absorb all unabsorbed
  python scripts/absorb_batch.py --type posts       # only blog posts
  python scripts/absorb_batch.py --type videos      # only videos
  python scripts/absorb_batch.py --batch-size 10    # process 10 at a time
  python scripts/absorb_batch.py --checkpoint-every 15
  python scripts/absorb_batch.py --dry-run          # show what would be absorbed
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
RAW_DIR = ROOT / "raw"
ABSORB_LOG = WIKI_DIR / "_absorb_log.json"
INDEX_FILE = WIKI_DIR / "_index.md"
BACKLINKS_FILE = WIKI_DIR / "_backlinks.json"

MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 8192
CONCURRENT_ABSORBS = 5  # parallel API calls


def load_agents_md():
    with open(ROOT / "AGENTS.md") as f:
        return f.read()


def load_index():
    if INDEX_FILE.exists():
        return INDEX_FILE.read_text()
    return ""


def load_absorb_log():
    if ABSORB_LOG.exists():
        with open(ABSORB_LOG) as f:
            return json.load(f)
    return {}


def save_absorb_log(log):
    with open(ABSORB_LOG, "w") as f:
        json.dump(log, f, indent=2)


def get_existing_articles():
    """Return dict of {relative_path: content} for all wiki articles."""
    articles = {}
    for dirpath, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, ROOT)
                with open(path) as fh:
                    articles[rel] = fh.read()
    return articles


def get_article_summaries():
    """Get a compact summary of each article (title + first 2 lines) for context."""
    summaries = []
    for dirpath, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, WIKI_DIR)
                with open(path) as fh:
                    content = fh.read()
                # Extract title from frontmatter
                title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else f
                # Extract aliases
                alias_match = re.search(r'^aliases:\s*\[(.+)\]', content, re.MULTILINE)
                aliases = alias_match.group(1) if alias_match else ""
                # Get source count
                src_match = re.search(r'^sources:\s*\[(.+)\]', content, re.MULTILINE)
                src_count = len(re.findall(r'"[^"]+?"', src_match.group(1))) if src_match else 0
                summaries.append(f"- {rel}: {title} (aliases: {aliases}) [{src_count} sources]")
    return "\n".join(summaries)


def get_unabsorbed_sources(source_type=None):
    """Get list of raw source files not yet in the absorb log."""
    log = load_absorb_log()
    absorbed_slugs = set(log.keys())
    sources = []

    dirs = []
    if source_type in (None, "posts"):
        dirs.append(("posts", RAW_DIR / "posts"))
    if source_type in (None, "videos"):
        dirs.append(("videos", RAW_DIR / "videos"))

    for stype, sdir in dirs:
        if not sdir.exists():
            continue
        for f in sorted(sdir.glob("*.md")):
            if f.name.startswith("_"):
                continue
            slug = f.stem
            if slug not in absorbed_slugs:
                sources.append({
                    "slug": slug,
                    "type": stype,
                    "path": str(f),
                    "size": f.stat().st_size,
                })

    return sources


def truncate_source(content, max_chars=15000):
    """Truncate very long sources to fit in context window."""
    if len(content) <= max_chars:
        return content
    # Keep frontmatter + first max_chars of body
    match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = content[len(frontmatter):]
        return frontmatter + body[:max_chars - len(frontmatter)] + "\n\n[... truncated for length ...]"
    return content[:max_chars] + "\n\n[... truncated for length ...]"


def absorb_single_source(source, agents_md, index_md, article_summaries, existing_articles):
    """Call Claude API to absorb a single source into the wiki."""
    slug = source["slug"]
    source_path = source["path"]

    with open(source_path) as f:
        source_content = truncate_source(f.read())

    # Build the prompt
    system_prompt = f"""You are a wiki compiler for the Founder Wiki project. Your job is to absorb a raw source into the wiki by deciding which articles to update or create.

Here are the wiki conventions and writing standards:

{agents_md}

CURRENT WIKI ARTICLES:
{article_summaries}

CURRENT INDEX:
{index_md}
"""

    user_prompt = f"""Absorb this source into the wiki. For each article you want to update or create, output it in this exact format:

===FILE: wiki/topics/example-topic.md===
[complete file content with frontmatter and body]
===END FILE===

Rules:
1. If updating an existing article, output the COMPLETE updated file (not just the diff). Include all existing content plus new material integrated coherently.
2. If creating a new article, use the format from AGENTS.md.
3. Add inline [[wikilinks]] to other topics wherever relevant.
4. Add inline citations linking to the source URL.
5. Update the sources list in frontmatter.
6. The source URL is: https://www.ycombinator.com/library/{slug}
7. You MUST output at least one ===FILE=== block.
8. Do NOT output the _index.md or _absorb_log.json — those are rebuilt separately.
9. For existing articles, read the article summaries above to know what exists. Only output articles that this source meaningfully contributes to (3+ sentences of new material).
10. Organize by theme, not chronology. Use attribution ("Speaker argues that...").

Here is the existing content of articles you might want to update (read these carefully before updating):

{_get_relevant_articles(source_content, existing_articles)}

SOURCE TO ABSORB:

{source_content}"""

    client = anthropic.Anthropic()

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )

        response_text = response.content[0].text

        # Parse output files
        files_written = []
        file_blocks = re.findall(
            r'===FILE:\s*(.+?)===\s*\n(.*?)\n===END FILE===',
            response_text,
            re.DOTALL
        )

        for file_path, file_content in file_blocks:
            file_path = file_path.strip()
            file_content = file_content.strip()

            # Ensure path is relative to ROOT
            full_path = ROOT / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(file_content + "\n")
            files_written.append(file_path)

        return {
            "slug": slug,
            "status": "ok",
            "files_written": files_written,
            "tokens_used": response.usage.input_tokens + response.usage.output_tokens,
        }

    except Exception as e:
        return {
            "slug": slug,
            "status": "error",
            "error": str(e),
            "files_written": [],
        }


def _get_relevant_articles(source_content, existing_articles, max_articles=5, max_chars_per=3000):
    """Select the most relevant existing articles to include as context."""
    source_lower = source_content.lower()

    # Score each article by keyword overlap
    scores = []
    for path, content in existing_articles.items():
        title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
        title = (title_match.group(1) if title_match else "").lower()
        alias_match = re.search(r'^aliases:\s*\[(.+)\]', content, re.MULTILINE)
        aliases = re.findall(r'"([^"]+)"', alias_match.group(1)) if alias_match else []

        score = 0
        # Title match
        if title and title in source_lower:
            score += 10
        # Alias matches
        for alias in aliases:
            if alias.lower() in source_lower:
                score += 3
        # Quick keyword check
        for word in title.split():
            if len(word) > 3 and word in source_lower:
                score += 1

        if score > 0:
            scores.append((score, path, content))

    scores.sort(reverse=True)
    top = scores[:max_articles]

    if not top:
        return "(No existing articles seem directly relevant to this source.)"

    parts = []
    for _, path, content in top:
        truncated = content[:max_chars_per]
        if len(content) > max_chars_per:
            truncated += "\n[... truncated ...]"
        parts.append(f"### {path}\n\n{truncated}")

    return "\n\n---\n\n".join(parts)


def rebuild_index():
    """Rebuild _index.md from current wiki articles."""
    articles = []
    for dirpath, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                path = os.path.join(dirpath, f)
                rel = os.path.relpath(path, WIKI_DIR)
                with open(path) as fh:
                    content = fh.read()

                title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else f.replace(".md", "")
                type_match = re.search(r'^type:\s*(.+)$', content, re.MULTILINE)
                atype = type_match.group(1).strip() if type_match else "topic"
                alias_match = re.search(r'^aliases:\s*\[(.+)\]', content, re.MULTILINE)
                aliases = re.findall(r'"([^"]+)"', alias_match.group(1)) if alias_match else []
                src_match = re.search(r'^sources:\s*\[(.+)\]', content, re.MULTILINE)
                src_count = len(re.findall(r'"[^"]+?"', src_match.group(1))) if src_match else 0

                dir_name = os.path.relpath(dirpath, WIKI_DIR)
                articles.append({
                    "title": title,
                    "type": atype,
                    "aliases": aliases,
                    "dir": dir_name,
                    "path": rel,
                    "src_count": src_count,
                })

    # Group by category
    categories = {
        "Idea & Getting Started": [],
        "Building (Pre-PMF)": [],
        "Growth & Distribution": [],
        "Fundraising & Finance": [],
        "People & Organization": [],
        "Frameworks & Mental Models": [],
        "Other": [],
    }

    idea_slugs = {"startup-ideas", "cofounders", "founder-mindset"}
    building_slugs = {"early-stage-tactics", "product-development"}
    growth_slugs = {"growth", "sales-and-distribution"}
    money_slugs = {"fundraising", "financial-survival", "board-governance"}
    people_slugs = {"hiring", "management"}

    for a in articles:
        fname = os.path.basename(a["path"]).replace(".md", "")
        if a["dir"] == "frameworks":
            categories["Frameworks & Mental Models"].append(a)
        elif fname in idea_slugs:
            categories["Idea & Getting Started"].append(a)
        elif fname in building_slugs:
            categories["Building (Pre-PMF)"].append(a)
        elif fname in growth_slugs:
            categories["Growth & Distribution"].append(a)
        elif fname in money_slugs:
            categories["Fundraising & Finance"].append(a)
        elif fname in people_slugs:
            categories["People & Organization"].append(a)
        else:
            # Auto-categorize new articles
            if a["type"] == "framework":
                categories["Frameworks & Mental Models"].append(a)
            else:
                categories["Other"].append(a)

    # Build index
    lines = [
        "# Founder Wiki — Index\n",
        "> This index is the entry point for agent navigation. Scan this file to find relevant articles, then read those articles directly. Do NOT read raw/ entries — the wiki is the knowledge base.\n",
        "## How to Navigate\n",
        "1. Scan the sections below for your query — check aliases in parentheses",
        "2. Follow [[wikilinks]] in articles for related content",
        "3. Check _backlinks.json for high-connectivity articles\n",
        "## Topics by Stage\n",
    ]

    for cat_name, cat_articles in categories.items():
        if not cat_articles:
            continue
        lines.append(f"### {cat_name}\n")
        for a in sorted(cat_articles, key=lambda x: x["title"]):
            alias_str = ", ".join(a["aliases"][:6]) if a["aliases"] else ""
            lines.append(f"- [[{a['title']}]] ({alias_str}) [{a['src_count']} sources]")
        lines.append("")

    # Stats
    log = load_absorb_log()
    lines.append("## Stats\n")
    lines.append(f"- Total wiki articles: {len(articles)}")
    lines.append(f"- Sources absorbed: {len(log)}")
    lines.append(f"- Last updated: {time.strftime('%Y-%m-%d')}")

    INDEX_FILE.write_text("\n".join(lines) + "\n")
    print(f"  Rebuilt _index.md ({len(articles)} articles)")


def rebuild_backlinks():
    """Rebuild _backlinks.json by scanning all wiki articles for [[wikilinks]]."""
    articles = {}
    for dirpath, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if f.endswith(".md") and not f.startswith("_"):
                path = os.path.join(dirpath, f)
                with open(path) as fh:
                    content = fh.read()
                title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else f.replace(".md", "")
                # Find all wikilinks in body
                links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', content)
                articles[title] = list(set(links))

    # Build reverse map
    backlinks = {}
    for title, links in articles.items():
        for target in links:
            if target not in backlinks:
                backlinks[target] = []
            if title not in backlinks[target]:
                backlinks[target].append(title)

    with open(BACKLINKS_FILE, "w") as f:
        json.dump(backlinks, f, indent=2, sort_keys=True)

    total_links = sum(len(v) for v in backlinks.values())
    print(f"  Rebuilt _backlinks.json ({len(backlinks)} targets, {total_links} backlinks)")


def rebuild_viewer_json():
    """Regenerate viewer/articles.json from current wiki state.

    Includes `last_updated` and `created` from frontmatter, plus
    `git_last_committed` (ISO 8601) from `git log -1` for each article file.
    Git is authoritative for the "Recently updated" home page section because
    frontmatter dates can drift if an editor forgets to bump them.
    """
    # Batch-compute git last-commit dates for all wiki files in one pass.
    # Uses `git log --name-only --format=...` so we traverse history once
    # rather than running `git log` 200+ times.
    git_dates = {}
    try:
        result = subprocess.run(
            ["git", "log", "--name-only", "--format=COMMIT %cI", "--", "wiki/"],
            capture_output=True, text=True, cwd=str(ROOT), check=True,
        )
        current_date = None
        for line in result.stdout.splitlines():
            if line.startswith("COMMIT "):
                current_date = line[len("COMMIT "):].strip()
            elif line.strip() and current_date:
                # First time we see a file, that's its most recent commit.
                if line not in git_dates:
                    git_dates[line] = current_date
    except (subprocess.CalledProcessError, FileNotFoundError):
        # If git isn't available or the repo isn't initialized, fall through
        # with an empty map — articles will use frontmatter last_updated only.
        pass

    articles = []
    for dirpath, dirs, files in os.walk(WIKI_DIR):
        for f in files:
            if not f.endswith(".md") or f.startswith("_"):
                continue
            path = os.path.join(dirpath, f)
            with open(path) as fh:
                content = fh.read()

            match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
            if not match:
                continue

            meta = {}
            for line in match.group(1).split("\n"):
                kv = re.match(r'^(\w[\w_]*):\s*(.+)$', line)
                if kv:
                    key, val = kv.group(1), kv.group(2).strip()
                    if val.startswith("["):
                        try:
                            meta[key] = json.loads(val)
                        except:
                            items = re.findall(r'"([^"]+)"', val)
                            meta[key] = items if items else val
                    elif val.startswith('"') and val.endswith('"'):
                        meta[key] = val[1:-1]
                    else:
                        meta[key] = val

            parts = path.split("/")
            dir_type = parts[-2] if len(parts) > 2 else "other"
            slug = (meta.get("title", f.replace(".md", ""))).lower()
            slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")

            # Relative path from repo root for git date lookup.
            rel_path = os.path.relpath(path, str(ROOT))

            articles.append({
                "title": meta.get("title", ""),
                "type": meta.get("type", ""),
                "aliases": meta.get("aliases", []),
                "sources": meta.get("sources", []),
                "speakers_referenced": meta.get("speakers_referenced", []),
                "originated_by": meta.get("originated_by", ""),
                "related": meta.get("related", []),
                "created": meta.get("created", ""),
                "last_updated": meta.get("last_updated", ""),
                "git_last_committed": git_dates.get(rel_path, ""),
                "body": match.group(2),
                "dir": dir_type,
                "slug": slug,
            })

    viewer_path = ROOT / "viewer" / "articles.json"
    with open(viewer_path, "w") as f:
        json.dump(articles, f)

    # Keep docs/articles.json in sync for the live GitHub Pages site.
    docs_path = ROOT / "docs" / "articles.json"
    if docs_path.parent.exists():
        with open(docs_path, "w") as f:
            json.dump(articles, f)

    print(f"  Rebuilt viewer/articles.json and docs/articles.json ({len(articles)} articles)")


def checkpoint(batch_num):
    """Run checkpoint: rebuild index, backlinks, viewer."""
    print(f"\n--- Checkpoint (after batch {batch_num}) ---")
    rebuild_index()
    rebuild_backlinks()
    rebuild_viewer_json()
    print("--- Checkpoint complete ---\n")


def main():
    parser = argparse.ArgumentParser(description="Absorb raw sources into the founder wiki")
    parser.add_argument("--type", choices=["posts", "videos"], help="Only absorb this type")
    parser.add_argument("--batch-size", type=int, default=10, help="Sources per batch (default: 10)")
    parser.add_argument("--checkpoint-every", type=int, default=15, help="Checkpoint interval (default: 15)")
    parser.add_argument("--max-sources", type=int, default=None, help="Max sources to absorb")
    parser.add_argument("--concurrent", type=int, default=CONCURRENT_ABSORBS, help="Parallel API calls (default: 5)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be absorbed")
    args = parser.parse_args()

    # Load wiki state
    agents_md = load_agents_md()
    sources = get_unabsorbed_sources(args.type)

    if args.max_sources:
        sources = sources[:args.max_sources]

    print(f"Unabsorbed sources: {len(sources)}")
    if args.type:
        print(f"  Filter: {args.type} only")

    if args.dry_run:
        for s in sources[:20]:
            print(f"  [{s['type']}] {s['slug']} ({s['size']} bytes)")
        if len(sources) > 20:
            print(f"  ... and {len(sources) - 20} more")
        return

    if not sources:
        print("Nothing to absorb!")
        return

    # Process in batches
    log = load_absorb_log()
    total_files_written = 0
    total_tokens = 0
    total_errors = 0
    t_start = time.time()
    sources_processed = 0

    for batch_start in range(0, len(sources), args.batch_size):
        batch = sources[batch_start:batch_start + args.batch_size]
        batch_num = batch_start // args.batch_size + 1

        # Reload wiki state for each batch (articles may have changed)
        index_md = load_index()
        article_summaries = get_article_summaries()
        existing_articles = get_existing_articles()

        print(f"\nBatch {batch_num}: absorbing {len(batch)} sources...")

        # Process batch concurrently
        results = []
        with ThreadPoolExecutor(max_workers=args.concurrent) as pool:
            futures = {
                pool.submit(
                    absorb_single_source, s, agents_md, index_md, article_summaries, existing_articles
                ): s["slug"]
                for s in batch
            }
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                slug = result["slug"]

                if result["status"] == "ok":
                    files = result["files_written"]
                    tokens = result.get("tokens_used", 0)
                    total_files_written += len(files)
                    total_tokens += tokens
                    sources_processed += 1

                    # Update absorb log
                    log[slug] = {
                        "absorbed_date": time.strftime("%Y-%m-%d"),
                        "articles_touched": files,
                    }

                    status = f"ok ({len(files)} files, {tokens} tokens)"
                else:
                    total_errors += 1
                    status = f"ERROR: {result.get('error', 'unknown')[:80]}"

                done = len(results)
                print(f"  [{batch_start + done}/{len(sources)}] {slug}: {status}")

        # Save absorb log after each batch
        save_absorb_log(log)

        # Checkpoint
        if (batch_start + len(batch)) % args.checkpoint_every < args.batch_size or batch_start + len(batch) >= len(sources):
            checkpoint(batch_num)

    elapsed = time.time() - t_start

    print(f"\n{'='*60}")
    print(f"ABSORPTION COMPLETE ({elapsed:.1f}s)")
    print(f"{'='*60}")
    print(f"Sources processed: {sources_processed}")
    print(f"Files written/updated: {total_files_written}")
    print(f"Errors: {total_errors}")
    print(f"Total tokens: {total_tokens:,}")
    print(f"Total wiki articles: {len(get_existing_articles())}")


if __name__ == "__main__":
    main()
