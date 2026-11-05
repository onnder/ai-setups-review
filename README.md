# AI Setups Review 2026

**What does the IT community actually use for AI-assisted work?**
A reproducible census of personal AI setups — coding agents/harnesses, models, interfaces, subscriptions and spend —
from **1 119 people** who described their own setup in 2026 on Hacker News, Lobste.rs, Tildes and personal blogs.

🌐 **Infographic:** <https://aisetups.ringil.cc/> · 📄 [Full report](docs/report.md) · 🧾 [Decisions & source list](docs/spec.md)

## Headline numbers (1 Jan – 5 Nov 2026)

| | |
|---|---|
| Authors with a described setup | 1 119 (HN 811 · Lobste.rs 161 · Tildes 81 · blogs 66) |
| Comments read | 10 135 (+ 199 blog articles) |
| #1 harness | **Claude Code** — 356 authors, 2.8× the #2 (Codex CLI, 129) |
| Next | Codex CLI · OpenCode · Pi · GitHub Copilot · Cursor |
| Interface | terminal/TUI dominates; desktop app and mobile are no longer niche for Claude Code |
| vs. 2026 surveys | community is far more terminal/open-source (Pi 3× Stack Overflow); Copilot & Cursor far below |

## Method in one paragraph

Threads were selected by hand (approved list in [docs/spec.md](docs/spec.md)); **every** 2026 comment was read by an LLM
with a fixed schema ([prompts/](prompts/)) that extracts tool, model, interface, host, model→harness pairing, status
(`uses` / `left`) and spend. Counting unit = unique author × tool per source; only first-person current use counts.
99.6 % of extracted quotes were verified verbatim against the source text. Large developer surveys
(Stack Overflow, JetBrains, Pragmatic Engineer) are used only for calibration. Reddit is excluded because its
[Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy)
forbids research outside the Reddit for Researchers program.

## Repository layout

```
pipeline/            Python scripts (stdlib only, Python 3.11+)
  paths.py             repo-relative paths
  fetch_hn.py          HN comment trees via Algolia API          -> data/hn/raw/
  fetch_lt.py          Lobste.rs (JSON) + Tildes (HTML) threads  -> data/community/raw/
  fetch_reader.py      Readwise Reader library metadata          -> data/readwise/docs.jsonl   (needs token)
  readwise_select.py   keyword filter + merge of LLM screening   -> candidates.json, selected.json
  fetch_full.py        full text of selected articles            -> data/readwise/full/  (git-ignored)
  prepare_batches.py   2026 comments -> classification batches  -> data/classified/input/
  normalize.py         tool-name aliases, model families, hardware classes
  aggregate.py         classified JSONL -> data/mentions.csv + data/viz2.json
  infographic_tpl.html infographic template (static HTML + inline JS, data injected at build)
  build_infographic.py -> site/index.html
  build_report.py      -> docs/report.md
  v1/                  first iteration (12-month, HN only, Slovak); kept for reference, not path-refactored
prompts/             LLM instructions used for classification, screening and extraction
data/
  mentions.csv         ★ main dataset: one row per author × tool × comment, with link + quote
  viz2.json            aggregated numbers behind the infographic
  hn/ community/ readwise/ surveys/ classified/   raw inputs and per-batch LLM outputs
site/index.html      the infographic (static, no build step)
docs/                report.md, spec.md
```

## Reproduce

Re-running the aggregation from the committed classified data is deterministic:

```bash
cd pipeline
python3 aggregate.py           # -> data/mentions.csv, data/viz2.json
python3 build_infographic.py   # -> site/index.html
python3 build_report.py        # -> docs/report.md
```

Full re-collection (network): `fetch_hn.py`, `fetch_lt.py`, then `prepare_batches.py`; classification is done by an
LLM agent per batch following `prompts/classify_comments_v2.md` (writes `data/classified/output/vNN.jsonl`).
Readwise steps need your own Reader token in `~/.config/readwise/token` and your own library.

## Deployment

`site/` is a single static HTML file. It is served by Cloudflare Pages connected to this repository
(build command: none, output directory: `site`), so every push to `main` redeploys.

## Licenses

- Code: [MIT](LICENSE)
- Derived data, report and infographic: [CC BY 4.0](LICENSE-DATA.md)
- Third-party comments, quotes and article metadata remain their authors' property — see [LICENSE-DATA.md](LICENSE-DATA.md).
  Full texts of third-party articles are intentionally not included.

Built with an AI coding agent; every number in the infographic is traceable to a row in `data/mentions.csv`.
