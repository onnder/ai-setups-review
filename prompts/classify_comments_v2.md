# Classify community comments: personal AI setup mentions (v2 — with interfaces)

Input: a JSONL batch, one comment per line: `source` (hn | lobsters | tildes), `id`, `thread`, `author`, `date`, `parent` (first 300 chars of the parent comment or story title, for context), `text`.

Goal: extract what AI tools, models, interfaces and subscriptions the comment AUTHOR personally uses (or stopped using).

Read EVERY comment yourself — no keyword scripts for the classification decision. Many comments are opinions with no personal setup: skip them. Use a scratch script only to read/write files.

## Output

Write a JSONL file (path given in your task). One line per (comment, tool) pair, ONLY for status `uses` or `left`. Skip comments with nothing relevant. Schema:

```json
{"source": "hn", "comment_id": "123", "thread": "456", "author": "x", "date": "2026-01-01",
 "tool": "Claude Code", "category": "harness", "status": "uses", "left_to": null,
 "interface": "terminal", "interface_explicit": false, "host": null,
 "via": null, "model_version": null, "spend_usd_mo": null,
 "quote": "short verbatim evidence <=160 chars"}
```

Copy `source`, `thread`, `author`, `date` from the input; `comment_id` = input `id` as string.

### status
- `uses` = the author currently uses it themselves (first person: "I use", "my setup is", "I pay for", "I run", "we use at work" if the author personally uses it). Past-tense ongoing use that is clearly still current counts.
- `left` = the author used it and stopped / switched away / cancelled. Put the replacement tool's canonical name in `left_to` if stated.
- NOT counted (skip): hearsay, advice to others without own use, hypotheticals, questions, general opinions, "I tried it once" without ongoing use, describing what someone else (the article author, a coworker) does.

### category
- `harness` — coding agents, AI editors, CLIs, IDE extensions, agent orchestrators, agent GUIs (Claude Code, Codex CLI, Cursor, GitHub Copilot, Aider, OpenCode, OpenChamber, Zed, Cline, Gemini CLI, Amp, Windsurf, Kiro, Antigravity, gptel, Conductor, Herdr, OpenClaw, Hermes Agent, Pi…)
- `app` — general AI apps/services not primarily for coding (ChatGPT app, Claude.ai/Claude Desktop chat, Gemini app, Perplexity, NotebookLM, Superwhisper, Wispr Flow, Open WebUI, OpenRouter as router…)
- `model` — a model family the author uses. `tool` = family, `model_version` = specific version if given. Families: `Claude Opus`, `Claude Sonnet`, `Claude Haiku`, `Claude Fable`, `Claude (unspecified)`, `GPT-5 / GPT (OpenAI)`, `OpenAI o-series`, `gpt-oss`, `Gemini Pro`, `Gemini Flash`, `Gemini (unspecified)`, `Qwen`, `DeepSeek`, `Kimi`, `GLM`, `MiniMax`, `Mistral/Devstral`, `Llama`, `Gemma`, `Grok`, `Cursor Composer`, other → descriptive family name.
- `local_runtime` — local inference runtime (Ollama, llama.cpp, LM Studio, MLX, vLLM, llama-swap…) or hardware used for local models (e.g. "Mac Studio M3 Ultra 512GB", "RTX 4090", "DGX Spark") — put hardware as its own line with category `local_runtime`.
- `subscription` — a paid plan / payment mode. Canonical: `Claude Pro`, `Claude Max (5x/$100)`, `Claude Max (20x/$200)`, `Claude Max (unspecified)`, `Claude Ultra`, `Claude Team/Enterprise`, `Claude (plan unspecified)`, `ChatGPT Plus`, `ChatGPT Pro`, `ChatGPT Business/Enterprise`, `ChatGPT (plan unspecified)`, `Cursor Pro`, `Cursor Ultra`, `GitHub Copilot (individual)`, `GitHub Copilot (employer)`, `Gemini/Google AI Pro`, `Google AI Ultra`, `API pay-as-you-go (Anthropic)`, `API pay-as-you-go (OpenAI)`, `API pay-as-you-go (other)`, `OpenRouter credits`, `OpenCode Go`, `OpenCode Zen`, `Z.ai GLM Coding Plan`, `Employer-paid (unspecified)`, `Free tier only`, other → descriptive.

### interface (NEW — the surface through which the author interacts with the tool/model)
Fill for `harness`, `app` and `model` lines; null for `local_runtime` and `subscription`.
- `terminal` — CLI / TUI in a terminal (Claude Code CLI, Codex CLI, OpenCode TUI, Pi, Aider, Gemini CLI, Crush, Goose, llm CLI)
- `ide-extension` — panel/extension inside an editor (GitHub Copilot in VS Code, Claude Code VS Code/JetBrains extension, Codex IDE extension, Cline, Roo, Kilo, Continue, JetBrains AI/Junie)
- `ai-editor` — standalone AI-first editor/IDE (Cursor, Windsurf, Antigravity, Kiro, Zed, Void, Trae)
- `vim-emacs` — Neovim/Vim/Emacs plugin (gptel, avante, codecompanion, claude-code-ide.el)
- `acp` — agent driven through Agent Client Protocol inside another editor (e.g. "Claude Code in Zed via ACP", "OpenCode in Zed")
- `desktop-app` — native desktop GUI app (Claude Desktop, Codex app, ChatGPT desktop, OpenChamber, Conductor, T3 Code, LM Studio chat UI, OpenCode desktop)
- `web` — browser UI (claude.ai, chatgpt.com, Gemini web, Codex cloud, Jules, Open WebUI, OpenCode web)
- `mobile` — phone app
- `chat-bot` — the agent is driven from a messaging app (Telegram, Slack, Discord, WhatsApp, Signal, iMessage) e.g. OpenClaw, Hermes Agent
- `api-script` — the author's own code / scripts calling an API or SDK directly
- `unknown` — cannot tell
`interface_explicit` = true only if the comment states or clearly implies the surface ("in VS Code", "the desktop app", "in the terminal", "from Telegram", "claude.ai"). If you infer it only from the tool's default surface (e.g. "Codex CLI" → terminal, "Cursor" → ai-editor, "ChatGPT" chat → web), set the default and `interface_explicit` = false. For tools with several surfaces and no hint (e.g. plain "Claude Code", "Codex", "OpenCode", "Copilot"), use the tool's primary surface (Claude Code → terminal, Codex → terminal, OpenCode → terminal, Copilot → ide-extension) with `interface_explicit` = false.
- `host` — the hosting editor/app/channel when relevant: `VS Code`, `JetBrains`, `Zed`, `Neovim`, `Vim`, `Emacs`, `Xcode`, `Visual Studio`, `tmux`, `Telegram`, `Slack`, `Discord`, `WhatsApp`, `Signal`, `browser`, etc. Null if not stated.

### via (NEW — for `model` lines)
The harness/app through which the author uses this model, canonical name (e.g. `Claude Code`, `OpenCode`, `Cursor`, `GitHub Copilot`, `Codex CLI`, `Pi`, `Claude (app/web)`, `ChatGPT (app/web)`, `OpenRouter`, `own scripts/API`, `llama.cpp`…). Only fill if the comment states or makes the pairing clear (e.g. "Opus 4.6 in Claude Code", "I run Qwen through OpenCode", "Cursor with Sonnet", or the author names exactly one harness and one model together). Null if ambiguous. If one model is used via two harnesses, emit two model lines with different `via`.

### spend_usd_mo
Only if the author states their own monthly spend (number, USD, convert roughly; annual → /12). Put it on ONE line per comment (the `subscription` line, or a line with tool `TOTAL SPEND`, category `subscription`, status `uses`).

### Canonical harness/app names
`Claude Code`, `Codex CLI`, `Codex (app/cloud)`, `Cursor`, `GitHub Copilot`, `Aider`, `OpenCode`, `OpenChamber`, `Zed`, `Cline`, `Roo Code`, `Kilo Code`, `Gemini CLI`, `Amp`, `Windsurf`, `Kiro`, `Antigravity`, `JetBrains AI/Junie`, `Continue`, `Goose`, `Crush`, `Pi`, `oh-my-pi`, `Factory Droid`, `Warp`, `Devin`, `Jules`, `OpenClaw`, `Hermes Agent`, `Conductor`, `Herdr`, `T3 Code`, `ChatGPT (app/web)`, `Claude (app/web)`, `Gemini (app/web)`, `Perplexity`, `NotebookLM`, `Open WebUI`, `OpenRouter`, `Superwhisper`, `Wispr Flow`, `Emacs gptel`, `llm (Simon Willison CLI)`. Unknown tools: use their own name as written. "Claude Desktop" chat → `Claude (app/web)` with interface `desktop-app`; "Claude Code desktop" → `Claude Code` with interface `desktop-app`.
- "Codex" alone in a coding context → `Codex CLI`. "Copilot" in a coding context → `GitHub Copilot`. "Claude" alone used for coding in terminal → `Claude Code`; used for chat → `Claude (app/web)`; if unclear → model `Claude (unspecified)` only.
- Example: "I use Claude Code in VS Code with Opus 4.6 on Max $200" → harness Claude Code (interface ide-extension, explicit true, host VS Code); model Claude Opus (version 4.6, via Claude Code, interface ide-extension, explicit true, host VS Code); subscription Claude Max (20x/$200) with spend 200.

When done, reply with ONLY: number of input comments, number of output lines, number of distinct authors with output, and the top 5 tools you saw. No other commentary.
