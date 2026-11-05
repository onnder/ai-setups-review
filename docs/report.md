# AI Setup Census 2026: čo IT komunita reálne používa

Status: ready-for-human

Infografika: [site/index.html](../site/index.html). Rozhodnutia a zoznam zdrojov: [spec.md](./spec.md). Dáta: [mentions.csv](../data/mentions.csv) (4 104 riadkov, každý s odkazom a citáciou).

Okno: **1. 1. – 5. 11. 2026**. Zdroje: Hacker News (21 schválených vlákien Ask HN, z toho 19 s komentármi z roku 2026), Lobste.rs a Tildes (213 diskusií) a 66 autorov osobných blogov (HN + Readwise Reader). Ankety SO, JetBrains a Pragmatic Engineer slúžia iba na kalibráciu. Reddit je vynechaný (pozri metodiku).

## TL;DR

- **1 119 autorov** opísalo vlastný AI setup (HN 811, Lobste.rs 161, Tildes 81, blogy 66).
- **Claude Code** používa 356 autorov (32 %), 2,8× viac ako druhý **Codex CLI** (129). Nasledujú **OpenCode** (100), **Pi** (83), **GitHub Copilot** (66) a **Cursor** (43).
- **Komunity sa líšia v chvoste:** HN je baštou Codexu a open-source agentov, Lobste.rs viac používa chat (Claude app 8 % oproti 3 % na HN) a Tildes má najviac používateľov Copilotu (11 %).
- **Rozhrania:** terminál/TUI uvádza 504 autorov (117 výslovne). Ďalej web (125), rozšírenie v IDE (77), AI editor (73) a desktop app (71). Pri Claude Code, kde autor rozhranie uviedol (n=130), je terminál 62 %, no desktop app a mobil už nie sú okrajové.
- **Kalibrácia:** oproti anketám je komunita výrazne terminálová a open-source. Pi má 13 % oproti 4,4 % v SO. OpenCode je so 13 % na úrovni SO (13,6 %), ale 2× nad JetBrains (7 %). Copilot (9 % oproti 58,7 %) a Cursor (6 % oproti 25,5 %) sú hlboko pod priemerom.
- **Peniaze:** platený plán Anthropicu má 161 autorov, OpenAI 88. Medián uvedenej mesačnej útraty je **$87** (n=127).

## 1. Harnessy a coding nástroje

| # | Harness | Autori | % |
|---|---|---|---|
| 1 | Claude Code | 356 | 32 % |
| 2 | Codex CLI | 129 | 12 % |
| 3 | OpenCode | 100 | 9 % |
| 4 | Pi | 83 | 7 % |
| 5 | GitHub Copilot | 66 | 6 % |
| 6 | Cursor | 43 | 4 % |
| 7 | Hermes Agent | 27 | 2 % |
| 8 | Antigravity | 18 | 2 % |
| 9 | Herdr | 18 | 2 % |
| 10 | Codex (app/cloud) | 16 | 1 % |
| 11 | OpenClaw | 14 | 1 % |
| 12 | oh-my-pi | 14 | 1 % |
| 13 | Zed | 12 | 1 % |
| 14 | DeepSeek Harness | 10 | 1 % |
| 15 | Kiro | 7 | 1 % |
| 16 | Cline | 5 | 0 % |
| 17 | Custom harness (own) | 5 | 0 % |
| 18 | Orca | 5 | 0 % |
| 19 | Paseo | 5 | 0 % |
| 20 | T3 Code | 5 | 0 % |

Claude Code + Codex CLI naraz: 79 autorov.

## 2. Komunity vedľa seba (podiel autorov v zdroji, %)

| Tool | Hacker News (n=811) | Lobste.rs (n=161) | Tildes (n=81) | Blogy (autori) (n=66) |
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

Blogy (n=66) = autori článkov o vlastnom setupe. Píšu najmä nadšenci, preto majú vyššie podiely naprieč tools.

## 3. Rozhrania

Výslovne = autor rozhranie uviedol. Doplnené = odvodené z predvoleného rozhrania nástroja (napríklad „Codex CLI“ → terminál).

| Typ rozhrania | Autori spolu | z toho výslovne |
|---|---|---|
| Terminál / TUI | 504 | 117 |
| Web | 125 | 51 |
| Rozšírenie v IDE | 77 | 44 |
| AI editor | 73 | 11 |
| Desktop app | 71 | 43 |
| Vlastné skripty / API | 53 | 22 |
| Chat bot (Telegram, Slack…) | 45 | 13 |
| Mobil | 12 | 10 |
| Vim / Emacs | 12 | 12 |
| ACP (agent v editore) | 3 | 3 |

**Claude Code podľa rozhrania** (iba výslovne uvedené, n=130 z 356 používateľov):

| Rozhranie | Autori |
|---|---|
| Terminál / TUI | 80 |
| Desktop app | 17 |
| Rozšírenie v IDE | 12 |
| Mobil | 8 |
| Web | 5 |
| Vlastné skripty / API | 3 |
| Vim / Emacs | 3 |
| Chat bot (Telegram, Slack…) | 2 |

**GitHub Copilot podľa rozhrania** (výslovne):

| Rozhranie | Autori |
|---|---|
| Rozšírenie v IDE | 17 |
| Terminál / TUI | 10 |
| Desktop app | 5 |
| Web | 4 |
| ACP (agent v editore) | 1 |

**Hostiteľ** (v čom nástroj beží, výslovne): VS Code 36, browser 32, tmux 21, GitHub 13, Herdr 10, Emacs 9, Telegram 8, Ghostty 7, Slack 5, Visual Studio 5, JetBrains 4, Zed 4, GitHub Actions 3, T3 Code 3.

### Model × cez čo ho autor používa (výslovné párovanie)

| Model | Claude Code | Pi | OpenCode | OpenRouter | own scripts/API | GitHub Copilot | Cursor | Codex CLI | llama.cpp | iné | spolu |
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

## 4. Trend 2026 po kvartáloch (podiel aktívnych autorov)

| Tool | Q1 (n=277) | Q2 (n=405) | Q3 (n=206) | Q4 (n=347) |
|---|---|---|---|---|
| Claude Code | 42 % | 25 % | 21 % | 33 % |
| Codex CLI | 8 % | 8 % | 9 % | 17 % |
| OpenCode | 4 % | 10 % | 7 % | 11 % |
| Pi | 1 % | 8 % | 5 % | 12 % |
| GitHub Copilot | 8 % | 5 % | 5 % | 4 % |
| OpenRouter | 1 % | 1 % | 2 % | 10 % |
| ChatGPT (app/web) | 5 % | 2 % | 4 % | 4 % |
| Cursor | 8 % | 2 % | 3 % | 3 % |
| Claude (app/web) | 4 % | 3 % | 4 % | 4 % |
| Hermes Agent | 0 % | 2 % | 0 % | 5 % |

Q4 = do 5. 11. a tvorí ho najmä jedno veľké HN vlákno z novembra.

## 5. Modely

| Skupina | Výslovne | Implicitne (z harnessu) | Spolu | Otvorené váhy |
|---|---|---|---|---|
| Claude | 327 | 277 | 604 |  |
| GPT (OpenAI) | 97 | 148 | 245 |  |
| Qwen | 157 | 0 | 157 | áno |
| DeepSeek | 97 | 0 | 97 | áno |
| Gemini | 40 | 26 | 66 |  |
| GLM | 49 | 0 | 49 | áno |
| Gemma | 40 | 0 | 40 | áno |
| Kimi | 16 | 0 | 16 | áno |
| Mistral/Devstral | 10 | 0 | 10 | áno |
| Grok | 8 | 0 | 8 |  |
| Whisper | 7 | 0 | 7 | áno |
| Cursor Composer | 5 | 0 | 5 |  |
| Local models (unspecified) | 5 | 0 | 5 |  |
| MiniMax | 5 | 0 | 5 | áno |
| gpt-oss (open) | 5 | 0 | 5 | áno |

Rodiny (výslovne): Claude Opus 157 (5.5, 4.6), Qwen 157 (3.6 27B, 3.6), Claude (unspecified) 153 (4.5, 4.6), DeepSeek 97 (V4 Flash, Flash), GPT-5 / GPT (OpenAI) 97 (5.5, 5.4), GLM 49 (5.3, 5.2), Gemma 40 (4, 4 31B), Claude Sonnet 35 (4.6, 5), Claude Fable 31 (5, 5.1), Gemini (unspecified) 24 (Argon, 3.1), Kimi 16 (K2.6, K2.5), Gemini Flash 11 (3.5, 3 Flash), Mistral/Devstral 10 (2, 14B), Grok 8 (4.6), Whisper 7 (distil-large-v3.5, Distil-Whisper Large V3.5), Claude Haiku 5 (4.5, 5), Cursor Composer 5 (2.5, 2.5 fast), Gemini Pro 5 (3 Pro, 4), Local models (unspecified) 5, MiniMax 5 (M2.7, M3), gpt-oss 5 (OSS 20B, 20B).

## 6. Predplatné a útrata

| Plán / platba | Autori |
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

Podľa poskytovateľa: Anthropic 161 (Pro 47, Max 62, Ultra 27) · OpenAI 88 (Plus 26, Pro 27) · API / OpenRouter 88 · Platí zamestnávateľ 68

Mesačná útrata (n=127): medián **$87**, priemer $260. Pásma: <$20 23 · $20–100 41 · $100–250 40 · >$250 23.

## 7. Odchody (najčastejšie toky so známym cieľom)

| Z | Na | Autori |
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

Spolu 248 prípadov typu autor × tool so stavom „prestal používať“.

## 8. Lokálne modely

203 autorov spomína lokálnu inferenciu. Runtime: llama.cpp 36, Ollama 23, LM Studio 13, vLLM 7, Strata 4, MLX 3, ds4 (antirez) 3, llama-swap 3. Hardvér: Apple Silicon Mac 50, NVIDIA GeForce 42, AMD Radeon GPU 19, DGX Spark / GB10 18, AMD Strix Halo 16, NVIDIA RTX Pro / DC 15.

## 9. Kalibrácia oproti anketám 2026

Komunita = podiel z 754 autorov, ktorí uviedli aspoň jeden coding harness.

| Tool | Komunita | Stack Overflow 2026 | JetBrains 2026 | Pragmatic Eng. 2026 |
|---|---|---|---|---|
| Claude Code | 47 % | 65,5 % | 39 % | 71 % |
| GitHub Copilot | 9 % | 58,7 % | 21 % | 46 % |
| Codex | 19 % | 29,5 % | 16 % | – |
| Cursor | 6 % | 25,5 % | 12 % | 39 % |
| Antigravity | 2 % | 16,0 % | 6 % | – |
| OpenCode | 13 % | 13,6 % | 7 % | – |
| JetBrains AI | 0 % | 12,8 % | 9 % | – |
| Windsurf | 0 % | 6,5 % | – | – |
| Pi | 13 % | 4,4 % | – | – |
| Cline | 1 % | 4,5 % | – | – |
| Aider | 0 % | 2,1 % | – | – |

Zdroje: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) (n≈12 260, „used in the past year“) · [JetBrains Developer Ecosystem 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) (n>15 000, máj–júl, „at work“) · [Pragmatic Engineer AI Tooling 2026](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) (n=507 pravidelných používateľov agentov). Formulácie otázok sa líšia, porovnávaj poradie a smer.

## Metodika a limity

- **Korpus:** HN 21 vlákien Ask HN. Lobste.rs a Tildes: 213 diskusií o AI v praxi z roku 2026 (Lobste.rs podľa tagov, Tildes podľa vyhľadávania). Iba komentáre z roku 2026.
- **Spracovanie:** každý komentár prečítal LLM bez predfiltra a určil tool, stav (uses/left), rozhranie (výslovne/doplnené), hostiteľa a párovanie model → harness. 99,6 % citácií je overených doslovne proti zdroju.
- **Počítanie:** unikátny autor × tool v rámci zdroja, posledný stav vyhráva. Ráta sa iba vlastné aktuálne používanie.
- **Skreslenia:** diskusné komunity nie sú reprezentatívne. HN vlákno o lokálnych modeloch (jún) nadhodnocuje Qwen, DeepSeek, Pi a OpenCode. Lobste.rs a Tildes dodali menej setupov na komentár, pretože ide o diskusie pod článkami, nie Ask vlákna.
- **Reddit vynechaný:** [Reddit Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy) vyžaduje schválenie prístupu k API a výskum mimo programu Reddit for Researchers zakazuje.
- **Blogy:** 11 článkov z HN titulky + Readwise Reader (knižnica later/starred/archive a 100 ITech feedov vrátane Swamp Club, 1 916 kandidátov → triedenie → 321 plných textov). Ráta sa iba autor. Swamp je produkt komunity Swamp Club, preto je v porovnaní zdrojov vynechaný.
