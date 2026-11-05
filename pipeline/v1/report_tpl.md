# HN AI setup survey: čo ľudia na Hacker News reálne používajú (nov 2025 až nov 2026)

Status: ready-for-human

Infografika: [infographic.html](./infographic.html) (otvoriť v prehliadači). Spec a rozhodnutia: [spec.md](./spec.md). Surové dáta: [mentions.csv](./mentions.csv), 2 974 riadkov (autor × tool × komentár), každý riadok s linkom a citáciou.

## TL;DR

- **Claude Code jasne dominuje.** Medzi 870 autormi, ktorí opísali svoj setup, ho aktívne používa 318 (37 %). Bez vlákna o lokálnych modeloch je to 41 %. To je približne 2,8× viac ako druhý **Codex CLI** (114, 13 %). Oba nástroje naraz používa 75 ľudí.
- **Open-source harnessy rastú najrýchlejšie.** **OpenCode** (85) a **Pi** (72) mali v Q4 2025 takmer nulu, od Q2 2026 držia stabilne 11–13 % aktívnych autorov.
- **IDE pluginy ustupujú.** **Cursor** klesol z 11 % (Q1 2026) na 3 % (Q4 2026) a 5 zo 6 odchodov z Cursoru smerovalo ku Claude Code. **GitHub Copilot** sa drží najmä tam, kde ho platí zamestnávateľ.
- **Modely:** najčastejšie výslovne menovaná rodina je **Claude Opus** (129 autorov, najmä Opus 5.5 a 4.6). Celá skupina Claude má vrátane implicitných zmienok 484 autorov, GPT 204. Z otvorených modelov vedú **Qwen** (125, najmä 3.6 27B), **DeepSeek** (85, V4 Flash) a **GLM** (48).
- **Platby:** platený plán Anthropicu (Pro, Max alebo Ultra) má 142 autorov, OpenAI (Plus alebo Pro) 82. Zo 111 ľudí, ktorí uviedli sumu, je medián **$60/mes** a priemer $247. Takmer polovica (53) platí ≥ $100.
- **Lokálne modely** spomína 152 autorov. Runtime **llama.cpp** (32) predbehol Ollamu (17) a najčastejší hardvér je Apple Silicon Mac (33).

## Metodika v skratke

- **Korpus:** 21 vlákien Ask HN o setupe, workflow a útrate (2 948 komentárov vrátane vnorených) a 11 článkov o osobnom setupe, kde sa započítal iba autor. Zoznam zdrojov je v [spec.md](./spec.md).
- **Spracovanie:** regex predfilter nechal 1 790 komentárov. Každý z nich prečítal LLM a určil stav `uses` (aktuálne používa), `left` (prestal používať) alebo zmienku bez osobnej skúsenosti, ktorá sa ignorovala.
- **Počítanie:** **unikátny autor × tool** s posledným stavom autora. Percentá sa rátajú z 870 autorov, ktorí uviedli aspoň jeden tool, ktorý používajú.
- **Skreslenia:**
  - Korpus tvoria HN power useri, takže výsledok nie je reprezentatívny pre všetkých vývojárov.
  - Vlákno *„Has anyone replaced Claude/GPT with a local model…“* (140 autorov) nadhodnocuje Qwen, DeepSeek, Pi a OpenCode. Rebríček bez neho je uvedený nižšie.
  - Q4 2026 je takmer celé jedno vlákno (*„What's your current AI agentic setup?“*, 254 autorov).
  - Trend preto ukazuje **podiel** aktívnych autorov v kvartáli, nie absolútne čísla.

## 1. Harnessy a coding tools

{{harness}}

Long tail (< 3 autori): {{tail_h}} ďalších harnessov. Veľa z nich sú vlastnoručne postavené agenty a orchestrátory, napríklad „obeya“, „neal“ či „miniclaw“. V [mentions.csv](./mentions.csv) majú `category=harness`.

### Kontrola citlivosti: harnessy a appky bez vlákna o lokálnych modeloch

{{sens}}

Poradie top 5 zostáva rovnaké, pri OpenCode a Pi klesne len podiel.

## 2. Appky a služby (mimo kódenia)

{{app}}

## 3. Modely

### Podľa skupiny: explicitné vs. implicitné

Implicitný model znamená, že autor uviedol iba harness viazaný na jedného poskytovateľa a model nespomenul: Claude Code/Claude app → Claude, Codex/ChatGPT → GPT, Gemini CLI/Antigravity/Jules → Gemini. Autor sa započíta iba raz na skupinu.

{{model_grp}}

### Podľa rodiny (iba explicitne spomenuté)

{{model_fam}}

„Claude Fable“ je model Anthropicu, ktorý autori opisujú ako drahší a silnejší ako Opus („I use Fable only very selectively now, it is just too expensive“).

## 4. Predplatné a platby

{{sub}}

**Súhrn podľa poskytovateľa (unikátni autori):** Anthropic platený plán 142 (Pro 42, Max {{max}}, Ultra 28) · OpenAI ChatGPT platený plán 82 · API pay-as-you-go alebo OpenRouter 68 · platí zamestnávateľ (Team/Enterprise/Business/employer) 53.

### Mesačná útrata (z autorov, ktorí uviedli sumu)

{{spend}}

Extrémy idú cez API: napríklad autor článku [The LLM Critics Are Right](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/) minul za jún ~$9 839 a [Ben Stolovitz](https://ben.stolovitz.com/posts/how-use-ai-oct-2026/) ~$3 000 mesačne.

## 5. Lokálne modely

{{local}}

{{hw}}

## 6. Trend po kvartáloch (top 10 harnessov a áppiek)

Formát buniek je *autori (podiel z aktívnych autorov v kvartáli)*. Q4 2025 aj Q4 2026 sú neúplné kvartály (od 5. 11., resp. do 5. 11.).

{{trend}}

Čo z trendu vyplýva:

- Podiel **Codex CLI** stúpol zo 5 % na 19 %.
- **OpenRouter** narástol z 0 na 10 %, čo súvisí s viac-modelovými setupmi.
- **Cursor** klesol z 11 % na 3 %.
- Podiel **Claude Code** sa ustálil na 26–38 % po vysokom štarte 53 % v Q4 2025.

## 7. Odchody (churn): odkiaľ a kam

Zaznamenaných je spolu 168 prípadov typu autor × tool so stavom „prestal používať“. `?` znamená, že cieľ nebol uvedený.

{{churn}}

Medzi Claude Code a Codex CLI prúdia ľudia oboma smermi (Codex → Claude Code 5, Claude Code → Codex 3), takže ide skôr o „prepínanie“ ako o jednosmerný odliv. Cursor a Aider jednoznačne strácajú v prospech Claude Code.

## 8. Zdroje

### Ask HN vlákna (rátajú sa všetky komentáre)

{{threads}}

### Články o osobnom setupe (ráta sa iba autor)

{{articles}}

### Kontext, ktorý sa neráta (vlákna k spusteniam a produktové)

- [OpenCode – Open source AI coding agent](https://news.ycombinator.com/item?id=47460525) (618 kom., 2026-03-20): spustenie produktu, ktorý v nasledujúcich kvartáloch vystúpal na #3.
- [Tell HN: I'm 60 years old. Claude Code has re-ignited a passion](https://news.ycombinator.com/item?id=47282777) (988 kom., 2026-03-07): najväčšie „pro“ vlákno roka okolo Claude Code.
- [Tell HN: Anthropic no longer allowing Claude Code subscriptions to use OpenClaw](https://news.ycombinator.com/item?id=47633396) (827 kom., 2026-04-03): zmena pravidiel predplatného, po ktorej OpenClaw zaznamenal odchody (7 autorov, okrem iného na Hermes Agent).

## Long tail (všetky kategórie, < 3 autori)

<details><summary>Zoznam ({{tail_n}} položiek)</summary>

{{tail}}

</details>
