# Classify HN comments: personal AI setup mentions

Input: a JSONL batch, one HN comment per line: `id, thread, author, date, parent` (first 300 chars of the parent comment, for context), `text`.

Goal: extract what AI tools, models, and subscriptions the comment AUTHOR personally uses (or stopped using) right now.

Read EVERY comment yourself — no keyword scripts for the classification decision. Use a scratch script only to read/write files.

## Output

Write a JSONL file (path given in your task). One line per (comment, tool) pair, ONLY for status `uses` or `left`. Skip comments with nothing relevant. Schema:

```json
{"comment_id": 123, "thread": 456, "author": "x", "date": "2026-01-01", "tool": "Claude Code", "category": "harness", "status": "uses", "left_to": null, "model_version": null, "spend_usd_mo": null, "quote": "short verbatim evidence <=160 chars"}
```

- `status`
  - `uses` = the author currently uses it themselves (first person: "I use", "my setup is", "I pay for", "I run", "we use at work" counts if the author personally uses it).
  - `left` = the author used it and stopped / switched away / cancelled. Put the replacement tool's canonical name in `left_to` if stated.
  - NOT counted (skip): hearsay, recommendations to others without own use, hypotheticals, "I tried it once and it was bad" without ongoing use (skip — that's neither), questions, general opinions about a tool.
- `category` — one of:
  - `harness` — coding agents / IDEs / CLIs / editor integrations (Claude Code, Codex CLI, Cursor, Copilot, Aider, OpenCode, Zed, Cline, Gemini CLI, Amp, Windsurf, Kiro, Antigravity, gptel, Conductor, OpenClaw…)
  - `app` — non-coding / general AI apps and services (ChatGPT app, Claude.ai app, Gemini app, Perplexity, NotebookLM, Superwhisper/Wispr Flow, Open WebUI, OpenRouter as a router…)
  - `model` — a model family the author uses. `tool` = family, `model_version` = specific version if given. Families: `Claude Opus`, `Claude Sonnet`, `Claude Haiku`, `Claude (unspecified)`, `GPT-5 / GPT (OpenAI)`, `OpenAI o-series`, `gpt-oss`, `Gemini Pro`, `Gemini Flash`, `Gemini (unspecified)`, `Qwen`, `DeepSeek`, `Kimi`, `GLM`, `MiniMax`, `Mistral/Devstral`, `Llama`, `Gemma`, `Grok`, other → descriptive family name.
  - `local_runtime` — local inference stack (Ollama, llama.cpp, LM Studio, MLX, vLLM) and hardware if notable (e.g. "Mac Studio M3 Ultra 512GB", "RTX 4090") — put hardware as tool with category `local_runtime`.
  - `subscription` — a paid plan / payment mode. Canonical: `Claude Pro`, `Claude Max (5x/$100)`, `Claude Max (20x/$200)`, `Claude Max (unspecified)`, `Claude Team/Enterprise`, `ChatGPT Plus`, `ChatGPT Pro`, `ChatGPT Business/Enterprise`, `Cursor Pro`, `Cursor Ultra`, `GitHub Copilot (individual)`, `GitHub Copilot (employer)`, `Gemini/Google AI Pro`, `Google AI Ultra`, `API pay-as-you-go (Anthropic)`, `API pay-as-you-go (OpenAI)`, `API pay-as-you-go (other)`, `OpenRouter credits`, `Z.ai GLM Coding Plan`, `Employer-paid (unspecified)`, `Free tier only`, other → descriptive.
- `spend_usd_mo` — only if the author states their own monthly spend (number, USD, convert roughly if other currency; annual → /12). Put it on ONE line per comment (the `subscription` line, or a line with tool `TOTAL SPEND`, category `subscription`, status `uses` if no single plan).
- Canonical harness/app names: `Claude Code`, `Codex CLI`, `Codex (app/cloud)`, `Cursor`, `GitHub Copilot`, `Aider`, `OpenCode`, `Zed`, `Cline`, `Roo Code`, `Kilo Code`, `Gemini CLI`, `Amp`, `Windsurf`, `Kiro`, `Antigravity`, `JetBrains AI/Junie`, `Continue`, `Goose`, `Crush`, `Pi`, `Factory Droid`, `Warp`, `Devin`, `Jules`, `OpenClaw`, `Conductor`, `ChatGPT (app/web)`, `Claude (app/web)`, `Gemini (app/web)`, `Perplexity`, `NotebookLM`, `Open WebUI`, `OpenRouter`, `Superwhisper`, `Wispr Flow`, `Emacs gptel`, `Neovim plugin (specify)`, `llm (Simon Willison CLI)`. Unknown tools: use their own name as written.
- "Codex" alone in a coding context → `Codex CLI`. "Copilot" in a coding context → `GitHub Copilot`. "Claude" alone used for coding in terminal → `Claude Code`; used for chat → `Claude (app/web)`; if unclear → model `Claude (unspecified)` only.
- A person who says "Claude Code with Opus 4.x on Max $200" → 3 lines: harness Claude Code, model Claude Opus (version 4.x), subscription Claude Max (20x/$200) with spend 200.

When done, reply with ONLY: number of input comments, number of output lines, and the top 5 tools you saw. No other commentary.
