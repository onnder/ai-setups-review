# AI Setups Review 2026: what the IT community actually uses for AI work

Infographic: [site/index.html](../site/index.html) · live at <https://aisetups.ringil.cc/>. Decisions and source list: [spec.md](./spec.md). Data: [mentions.csv](../data/mentions.csv) (4,104 rows, each with a link and a quote).

Window: **Jan 1 – Nov 5, 2026**. Sources: Hacker News (21 approved Ask HN threads, 19 of them with 2026 comments), Lobste.rs and Tildes (213 discussions) and 66 personal-blog authors (HN + Readwise Reader). Stack Overflow, JetBrains and Pragmatic Engineer surveys are used for calibration only. Reddit is excluded (see methodology).

## TL;DR

- **1,119 authors** described their own AI setup (HN 811, Lobste.rs 161, Tildes 81, blogs 66).
- **Claude Code** is used by 356 authors (32%), 2.8× more than the runner-up **Codex CLI** (129). Next: **OpenCode** (100), **Pi** (83), **GitHub Copilot** (66) and **Cursor** (43).
- **Communities differ in the long tail:** HN is the stronghold of Codex and open-source agents, Lobste.rs leans more on chat (Claude app 8% vs 3% on HN) and Tildes has the most GitHub Copilot users (11%).
- **Interfaces:** 504 authors use a terminal/TUI (117 explicitly), then web (125), IDE extension (77), AI editor (73) and desktop app (71). For Claude Code, where the author named the interface (n=130), the terminal is 62%, but the desktop app and mobile are no longer niche.
- **Calibration:** compared with the surveys the community is strongly terminal- and open-source-oriented. Pi: 13% vs 4.4% in Stack Overflow. OpenCode at 13% matches Stack Overflow (13.6%) but is 2× JetBrains (7%). Copilot (9% vs 58.7%) and Cursor (6% vs 25.5%) are far below.
- **Money:** 161 authors have a paid Anthropic plan, 88 a paid OpenAI plan. Median stated monthly spend is **$87** (n=127).

## 1. Harnesses and coding tools

| # | Harness | Authors | % |
|---|---|---|---|
| 1 | Claude Code | 356 | 32% |
| 2 | Codex CLI | 129 | 12% |
| 3 | OpenCode | 100 | 9% |
| 4 | Pi | 83 | 7% |
| 5 | GitHub Copilot | 66 | 6% |
| 6 | Cursor | 43 | 4% |
| 7 | Hermes Agent | 27 | 2% |
| 8 | Antigravity | 18 | 2% |
| 9 | Herdr | 18 | 2% |
| 10 | Codex (app/cloud) | 16 | 1% |
| 11 | OpenClaw | 14 | 1% |
| 12 | oh-my-pi | 14 | 1% |
| 13 | Zed | 12 | 1% |
| 14 | DeepSeek Harness | 10 | 1% |
| 15 | Kiro | 7 | 1% |
| 16 | Cline | 5 | 0% |
| 17 | Custom harness (own) | 5 | 0% |
| 18 | Orca | 5 | 0% |
| 19 | Paseo | 5 | 0% |
| 20 | T3 Code | 5 | 0% |

Claude Code and Codex CLI together: 79 authors.

## 2. Communities side by side (share of authors within each source, %)

| Tool | Hacker News (n=811) | Lobste.rs (n=161) | Tildes (n=81) | Blogs (authors) (n=66) |
|---|---|---|---|---|
| Claude Code | 31 | 34 | 22 | 48 |
| Codex CLI | 13 | 3 | 7 | 17 |
| OpenCode | 10 | 6 | 2 | 9 |
| Pi | 9 | 2 | 1 | 6 |
| GitHub Copilot | 5 | 2 | 11 | 20 |
| OpenRouter | 5 | 0 | 1 | 6 |
| ChatGPT (app/web) | 4 | 2 | 4 | 6 |
| Cursor | 4 | 1 | 4 | 4 |
| Claude (app/web) | 3 | 8 | 4 | 8 |
| Hermes Agent | 3 | 0 | 2 | 0 |
| Antigravity | 2 | 0 | 0 | 2 |
| Herdr | 2 | 0 | 0 | 0 |
| Gemini (app/web) | 2 | 0 | 5 | 2 |
| Codex (app/cloud) | 2 | 1 | 0 | 3 |

Blogs (n=66) = authors of articles about their own setup. They are mostly enthusiasts, so their shares are higher across tools.

## 3. Interfaces

Explicit = the author named the interface. Inferred = derived from the tool's default interface (e.g. "Codex CLI" → terminal).

| Interface type | Authors total | of which explicit |
|---|---|---|
| Terminal / TUI | 504 | 117 |
| Web | 125 | 51 |
| IDE extension | 77 | 44 |
| AI editor | 73 | 11 |
| Desktop app | 71 | 43 |
| Own scripts / API | 53 | 22 |
| Chat bot (Telegram, Slack…) | 45 | 13 |
| Mobile | 12 | 10 |
| Vim / Emacs | 12 | 12 |
| ACP (agent in editor) | 3 | 3 |

**Claude Code by interface** (explicit only, n=130 of 356 users):

| Interface | Authors |
|---|---|
| Terminal / TUI | 80 |
| Desktop app | 17 |
| IDE extension | 12 |
| Mobile | 8 |
| Web | 5 |
| Own scripts / API | 3 |
| Vim / Emacs | 3 |
| Chat bot (Telegram, Slack…) | 2 |

**GitHub Copilot by interface** (explicit):

| Interface | Authors |
|---|---|
| IDE extension | 17 |
| Terminal / TUI | 10 |
| Desktop app | 5 |
| Web | 4 |
| ACP (agent in editor) | 1 |

**Host** (what the tool runs in, explicit): VS Code 36, browser 32, tmux 21, GitHub 13, Herdr 10, Emacs 9, Telegram 8, Ghostty 7, Slack 5, Visual Studio 5, JetBrains 4, Zed 4, GitHub Actions 3, T3 Code 3.

### Model × what it is used through (explicit pairing)

| Model | Claude Code | Pi | OpenCode | OpenRouter | own scripts/API | GitHub Copilot | Cursor | Codex CLI | llama.cpp | other | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Claude | 64 | 1 | 6 | 2 | 5 | 11 | 9 | · | · | 29 | 127 |
| Qwen | 5 | 21 | 12 | 1 | 8 | 3 | · | · | 10 | 36 | 96 |
| DeepSeek | 1 | 11 | 12 | 6 | 2 | 1 | · | · | · | 26 | 59 |
| GPT (OpenAI) | 1 | 5 | 4 | 3 | 4 | 7 | 2 | 16 | · | 17 | 59 |
| GLM | 2 | 6 | 7 | 6 | · | · | · | · | · | 7 | 28 |
| Gemini | · | · | · | 2 | 4 | 1 | · | · | · | 15 | 22 |
| Gemma | · | 7 | 1 | · | · | 1 | · | · | 5 | 7 | 21 |
| Kimi | · | 2 | 3 | 3 | · | · | · | · | · | · | 8 |
| Mistral/Devstral | · | 1 | 1 | 2 | 1 | · | · | · | · | 1 | 6 |

## 4. 2026 trend by quarter (share of active authors)

| Tool | Q1 (n=277) | Q2 (n=405) | Q3 (n=206) | Q4 (n=347) |
|---|---|---|---|---|
| Claude Code | 42% | 25% | 21% | 33% |
| Codex CLI | 8% | 8% | 9% | 17% |
| OpenCode | 4% | 10% | 7% | 11% |
| Pi | 1% | 8% | 5% | 12% |
| GitHub Copilot | 8% | 5% | 5% | 4% |
| OpenRouter | 1% | 1% | 2% | 10% |
| ChatGPT (app/web) | 5% | 2% | 4% | 4% |
| Cursor | 8% | 2% | 3% | 3% |
| Claude (app/web) | 4% | 3% | 4% | 4% |
| Hermes Agent | 0% | 2% | 0% | 5% |

Q4 runs to Nov 5 and consists mostly of one large HN thread from November.

## 5. Models

| Group | Explicit | Implicit (from harness) | Total | Open weights |
|---|---|---|---|---|
| Claude | 327 | 277 | 604 |  |
| GPT (OpenAI) | 97 | 148 | 245 |  |
| Qwen | 157 | 0 | 157 | yes |
| DeepSeek | 97 | 0 | 97 | yes |
| Gemini | 40 | 26 | 66 |  |
| GLM | 49 | 0 | 49 | yes |
| Gemma | 40 | 0 | 40 | yes |
| Kimi | 16 | 0 | 16 | yes |
| Mistral/Devstral | 10 | 0 | 10 | yes |
| Grok | 8 | 0 | 8 |  |
| Whisper | 7 | 0 | 7 | yes |
| Cursor Composer | 5 | 0 | 5 |  |
| Local models (unspecified) | 5 | 0 | 5 |  |
| MiniMax | 5 | 0 | 5 | yes |
| gpt-oss (open) | 5 | 0 | 5 | yes |

Families (explicit): Claude Opus 157 (5.5, 4.6), Qwen 157 (3.6 27B, 3.6), Claude (unspecified) 153 (4.5, 4.6), DeepSeek 97 (V4 Flash, Flash), GPT-5 / GPT (OpenAI) 97 (5.5, 5.4), GLM 49 (5.3, 5.2), Gemma 40 (4, 4 31B), Claude Sonnet 35 (4.6, 5), Claude Fable 31 (5, 5.1), Gemini (unspecified) 24 (Argon, 3.1), Kimi 16 (K2.6, K2.5), Gemini Flash 11 (3.5, 3 Flash), Mistral/Devstral 10 (2, 14B), Grok 8 (4.6), Whisper 7 (distil-large-v3.5, Distil-Whisper Large V3.5), Claude Haiku 5 (4.5, 5), Cursor Composer 5 (2.5, 2.5 fast), Gemini Pro 5 (3 Pro, 4), Local models (unspecified) 5, MiniMax 5 (M2.7, M3), gpt-oss 5 (OSS 20B, 20B).

## 6. Subscriptions and spend

| Plan / payment | Authors |
|---|---|
| Claude Pro | 47 |
| API pay-as-you-go (other) | 44 |
| Employer-paid (unspecified) | 32 |
| Claude (plan unspecified) | 30 |
| ChatGPT Pro | 27 |
| Claude Ultra | 27 |
| ChatGPT Plus | 26 |
| OpenCode Go | 25 |
| Claude Max (20x/$200) | 23 |
| Claude Max (unspecified) | 23 |
| ChatGPT (plan unspecified) | 21 |
| OpenRouter credits | 20 |
| API pay-as-you-go (Anthropic) | 18 |
| Claude Max (5x/$100) | 17 |
| GitHub Copilot (employer) | 15 |
| Free tier only | 14 |
| Gemini/Google AI Pro | 11 |
| API pay-as-you-go (OpenAI) | 10 |

By provider: Anthropic 161 (Pro 47, Max 62, Ultra 27) · OpenAI 88 (Plus 26, Pro 27) · API / OpenRouter 88 · Employer pays 68

Monthly spend (n=127): median **$87**, mean $260. Bands: <$20 23 · $20–100 41 · $100–250 40 · >$250 23.

## 7. Churn (most common moves with a known destination)

| From | To | Authors |
|---|---|---|
| Cursor | Claude Code | 6 |
| Codex CLI | Claude Code | 5 |
| OpenClaw | Hermes Agent | 3 |
| Aider | Claude Code | 2 |
| ChatGPT (app/web) | Claude (app/web) | 2 |
| Claude (app/web) | Claude Code | 2 |
| Claude Code | Codex CLI | 2 |
| Claude Code | OpenCode | 2 |
| Codex CLI | OpenCode | 2 |
| Codex CLI | Pi | 2 |
| Cursor | Codex CLI | 2 |
| GitHub Copilot | Claude Code | 2 |
| Hermes Agent | Grok Bot | 2 |
| OpenCode | Pi | 2 |
| OpenCode | oh-my-pi | 2 |

In total 248 author × tool cases with status "stopped using".

## 8. Local models

203 authors mention running models locally. Runtimes: llama.cpp 36, Ollama 23, LM Studio 13, vLLM 7, Strata 4, MLX 3, ds4 (antirez) 3, llama-swap 3. Hardware: Apple Silicon Mac 50, NVIDIA GeForce 42, AMD Radeon GPU 19, DGX Spark / GB10 18, AMD Strix Halo 16, NVIDIA RTX Pro / DC 15.

## 9. Calibration against 2026 surveys

Community = share of the 754 authors who named at least one coding harness.

| Tool | Community | Stack Overflow 2026 | JetBrains 2026 | Pragmatic Eng. 2026 |
|---|---|---|---|---|
| Claude Code | 47% | 65.5% | 39% | 71% |
| GitHub Copilot | 9% | 58.7% | 21% | 46% |
| Codex | 19% | 29.5% | 16% | – |
| Cursor | 6% | 25.5% | 12% | 39% |
| Antigravity | 2% | 16.0% | 6% | – |
| OpenCode | 13% | 13.6% | 7% | – |
| JetBrains AI | 0% | 12.8% | 9% | – |
| Windsurf | 0% | 6.5% | – | – |
| Pi | 13% | 4.4% | – | – |
| Cline | 1% | 4.5% | – | – |
| Aider | 0% | 2.1% | – | – |

Sources: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) (n≈12,260, "used in the past year") · [JetBrains Developer Ecosystem 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) (n>15,000, May–Jul, "at work") · [Pragmatic Engineer AI Tooling 2026](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) (n=507 regular agent users). Question wording differs, so compare rank and direction, not absolute percentages.

## Methodology and limitations

- **Corpus:** HN: 21 Ask HN threads. Lobste.rs and Tildes: 213 discussions about AI in practice from 2026 (Lobste.rs by tag, Tildes by search). 2026 comments only.
- **Processing:** every comment was read by an LLM without a pre-filter, extracting tool, status (uses/left), interface (explicit/inferred), host and model → harness pairing. 99.6% of quotes were verified verbatim against the source.
- **Counting:** unique author × tool within a source; the latest status wins. Only first-person current use counts.
- **Biases:** discussion communities are not representative. The HN thread about local models (June) inflates Qwen, DeepSeek, Pi and OpenCode. Lobste.rs and Tildes yield fewer setups per comment because they are discussions under articles, not Ask threads.
- **Reddit excluded:** the [Reddit Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy) requires approval for API access and forbids research outside the Reddit for Researchers program.
- **Blogs:** 11 articles from the HN front page + Readwise Reader (later/starred/archive library and 100 ITech feeds including Swamp Club; 1,916 candidates → screening → 321 full texts). Only the article author counts. Swamp is a product of the Swamp Club community, so it is excluded from the cross-source comparison.
