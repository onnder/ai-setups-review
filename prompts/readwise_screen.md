# Screen Reader documents: does the AUTHOR describe their OWN AI setup?

Input JSONL lines: id, title, author, site, url, date, loc, summary.

For each line decide `verdict`:
- `yes` — the author clearly writes in first person about the AI tools / coding agents / models / subscriptions / workflow THEY personally use (e.g. "How I use Claude Code", "My agent setup", "What I pay for AI", "My LLM workflow", "I switched from Cursor to …", a field report of building something with a named agent).
- `maybe` — plausible but unclear from title+summary (e.g. an essay on AI coding that likely mentions the author's own tools; a project write-up built "with AI").
- `no` — news, product announcements, model releases, benchmarks, research papers, opinion pieces without personal use, tutorials about a tool without the author's own setup, non-AI topics.

Be inclusive with `maybe` — full text will be checked later. Output one JSON line per input line ONLY for `yes` and `maybe`:
{"id": "...", "verdict": "yes|maybe", "why": "<=12 words"}

When done, reply with ONLY: input count, yes count, maybe count.
