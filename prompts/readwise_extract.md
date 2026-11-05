# Extract the ARTICLE AUTHOR's own AI setup (Readwise blog articles)

Input JSONL: one article per line (`id`, `title`, `author`, `site`, `url`, `date`, `text` = full article text, possibly truncated).

Only the article AUTHOR's own, current setup counts (one author = one voice). Ignore tools the author merely reviews, reports news about, recommends to others, or mentions in passing. Many articles will have nothing — skip them.

Swamp Club field reports: the author's use of other tools/models counts normally; record `Swamp` itself as a harness line too (it will be excluded from cross-source comparison later).

Use the schema, categories, canonical names, `interface` / `interface_explicit` / `host` / `via` rules and status rules from `prompts/classify_comments_v2.md` — read it first. Differences:
- `source` = "blogs", `comment_id` = article `id`, `thread` = article `id`, `author` = article author name (if missing, use the site name), `date` = article `date`.
- Add `"url": "<article url>"` to every line.

Output: one JSONL file (path in your task) with lines only for `uses`/`left`. Additionally write a summary file (path in your task) with one markdown bullet per article that HAS at least one output line:
`- [Title](url) — Author, YYYY-MM-DD: <1–2 sentences in SLOVAK summarizing the author's setup>`
(keep tool names in English).

Read every article yourself. Verify JSONL parses with python3. Reply with ONLY: input articles, articles with output, output lines, top 5 tools.
