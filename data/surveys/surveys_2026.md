# Developer surveys published in 2026 reporting AI tool/model usage shares

Research date: 2026-11-05. Only primary-source publisher pages were used for numbers (no secondary blog aggregators cited as sources of data, though a couple are noted where they helped locate a primary URL).

---

## 1. Stack Overflow Developer Survey 2026 (AI section)

- **Publisher:** Stack Overflow (Prosus/Stack Overflow Inc.)
- **Title:** "Stack Overflow Developer Survey 2026" — AI chapter
- **Publication date:** October 6, 2026 (per Stack Overflow's own blog post "The results of the 2026 Developer Survey are here!," stackoverflow.blog/2026/10/06/...; confirmed via the survey site itself)
- **URL (hub):** https://survey.stackoverflow.co/2026
- **URL (AI chapter):** https://survey.stackoverflow.co/2026/ai and https://survey.stackoverflow.co/2026/ai/data
- **Field dates:** ~June 23 – August 5, 2026 (per methodology search; could not re-verify exact dates on the methodology page itself, which only documents data-cleaning rules, not field dates — flagged as a minor gap below)
- **Sample / population:** 39,266 total responses collected; 30,903 counted as "valid responses"; respondents from 169 countries. All-respondents base for most AI questions ranges n=10,926–17,464 depending on question (not everyone answered every question). Population = self-selected visitors/readers of Stack Overflow who opted into the survey (a mix of professional developers, hobbyists, and students; not a random sample of all developers).
- **Question wording (coding agents/tools):** *"Have you used any of the following coding agents or assistants in the past year? Do you want to use any of the following in the next 6 months?"* — a **multi-select, "used in the past year"** measure (respondents can pick more than one; percentages do not sum to 100%).
  - Source: https://survey.stackoverflow.co/2026/ai/data/ai-code-agent (question definition: https://github.com/StackExchange/Survey/blob/releases/2026/questions/ai/AICodeAgent.yaml)

### Table: AI coding agents/assistants used in the past year (n ≈ 12,260 who answered this question)

| Tool | % of respondents |
|---|---|
| Claude Code | 65.5% |
| GitHub Copilot | 58.7% |
| OpenAI Codex | 29.5% |
| Cursor | 25.5% |
| Google Antigravity | 16.0% |
| Gemini Code Assist | 14.6% |
| OpenCode | 13.6% |
| JetBrains AI | 12.8% |
| Windsurf | 6.5% |
| Warp | 5.2% |
| Cline | 4.5% |
| Pi | 4.4% |
| Amazon Q Developer | 3.9% |
| Continue | 3.8% |
| Mistral Vibe | 3.2% |
| Kilo Code | 3.2% |
| Devin | 2.9% |
| Google Jules | 2.5% |
| Replit Agent | 2.3% |
| Tabnine | 2.1% |
| Aider | 2.1% |
| Codium (Qodo) | 1.7% |
| BLACKBOX AI | 1.6% |
| Supermaven | 1.3% |
| Trae | 1.3% |
| Augment Code | 1.2% |
| Sourcegraph Cody | 0.9% |
| Emdash | 0.7% |
| Approxima | 0.6% |
| ECA | 0.6% |
| Sweep | 0.6% |
| Kavia AI | 0.5% |
| Syntropy | 0.5% |

(Source for all rows: https://survey.stackoverflow.co/2026/ai/data/ai-code-agent)

### Table: Broad AI-tool-category usage (different, broader question — "which categories of AI tools do you use," n=17,464)

| Category | % of respondents |
|---|---|
| AI coding assistants or coding agents | 65.9% |
| General-purpose AI chat tools (ChatGPT, Claude.ai, Gemini, etc. as a category — **no brand breakdown published**) | 62.5% |
| AI agents or automated workflows | 26.2% |
| Internal AI tools built by my company | 17.8% |
| I don't use AI tools | 17.2% |

Source: https://survey.stackoverflow.co/2026/ai/data/ai-select (question "AIAdopt")

### Other AI data points (same chapter)
- **Usage frequency** (n=14,478): AI coding assistants/agents — 73.0% daily, 20.1% weekly, 6.2% monthly/infrequent. General-purpose chat tools — 65.6% daily. Source: https://survey.stackoverflow.co/2026/ai/data/ai-freq
- **Hours/day of AI use** (n=10,926): 30.9% use AI 4+ hours/day; 24.1% use it 2–4 hours/day. Source: https://survey.stackoverflow.co/2026/ai/data/ai-daily
- **Sentiment** (n=14,428): 31.6% "very favorable," 30.4% "somewhat favorable" toward AI tool use at work (≈62% net favorable). Source: https://survey.stackoverflow.co/2026/ai/data/ai-sentiment
- **Trust** (n=14,304): 48.0% "trust it when I can easily verify the output"; only 6.6% trust AI "for many tasks, including important work decisions." Source: https://survey.stackoverflow.co/2026/ai/data/ai-trust
- **Orchestration/automation tools** (per the AI highlights page, survey.stackoverflow.co/2026/ai): LangChain 30%, OpenAI Agents SDK 24% (orchestration); Make 39%, n8n 33% (automation). Exact n and respondent counts for these rows were not re-extracted; cited from the highlights narrative text at https://survey.stackoverflow.co/2026/ai — treat as approximate until cross-checked against https://survey.stackoverflow.co/2026/ai/data/ai-orch and .../ai-automate (pages exist per sitemap but individual rows were not pulled in this pass).

### Gaps for this survey
- **No brand-level breakdown of general-purpose chat assistants** (ChatGPT vs. Claude.ai vs. Gemini vs. Perplexity, etc.) was found in the public 2026 report — "General-purpose AI chat tools" is reported only as one combined category (62.5%). This differs from the 2026 AI Pulse/Pragmatic Engineer reports, which do separate chatbot brands.
- **No reported model/model-family breakdown** (e.g., GPT-5.x vs. Claude Opus/Sonnet vs. Gemini) was found.
- **No reported dollar-spend/subscription-cost figures.** The survey does ask behavioral questions about cost sensitivity (question IDs `AICost`, `AICostPrompt` — e.g., "Has cost or usage limits ever changed how you personally use AI tools at work?"), but these are multi-select behavioral questions, not spend amounts, and no public data page for them was found in the site's sitemap as of this research (https://survey.stackoverflow.co/sitemap.xml lists no `ai-cost` or `ai-cost-prompt` data URL).
- Exact field-date range (June 23–Aug 5, 2026) came from a secondary citation during search and was **not independently re-verified against the primary methodology page**, which only describes data-cleaning rules, not field dates. Flagged as unverified.

---

## 2. JetBrains "Developer Ecosystem Survey 2026" / "AI Pulse" survey series

JetBrains published **two relevant primary reports in 2026**, both part of the same ongoing "AI Pulse" + "Developer Ecosystem Survey" research program (10th edition of the Developer Ecosystem Survey).

### 2a. "Which AI Coding Tools Do Developers Actually Use at Work?" (AI Pulse, January 2026 wave)
- **Publisher:** JetBrains (Strategic Research and Market Intelligence team)
- **Publication date:** April 2026 (URL dated 2026/04)
- **URL:** https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/
- **Field dates:** January 2026 (second wave of the "AI Pulse" survey; compared against a September 2025 wave and the 2024/2025 Developer Ecosystem Survey waves)
- **Sample / population:** "over 10,000 professional developers worldwide," localized into 8 languages (English, Spanish, Chinese, Japanese, Korean, German, French, Portuguese). Recruited via Instagram ads (China: Zhihu) plus ~16% from the JetBrains research panel. "Professional developers" = respondents in developer/programmer/SWE, AI/ML engineer, DevOps, architect, data scientist, or QA roles (~90% are Developer/Programmer/SWE). Survey promo did not mention AI, to reduce self-selection bias toward AI enthusiasts/skeptics.
- **Question wording:** Awareness ("heard of") vs. "adoption"/"used at work" (regular work usage, not "past year" wording) — JetBrains' own dashboards present this as a trend line from April–June 2025 → September 2025 → January 2026.

**Table: AI coding tool adoption ("used at work"), January 2026**

| Tool | % adoption (Jan 2026) | Change vs. prior wave |
|---|---|---|
| GitHub Copilot | 29% | down from higher, growth stalled; 40% at 5,000+ employee companies |
| Claude Code | 18% | up from ~3% in Apr–Jun 2025; tied for 2nd place; 24% in US/Canada |
| Cursor | 18% | growth slowed; still 2nd most "aware of" tool (69%) |
| OpenAI Codex | 3% | "much less popular" as of Jan 2026 (pre-desktop-app launch); ChatGPT itself used for coding by 28% |
| Google Antigravity | 6% | new tool, rising awareness (29%→47% later in the year) |
| JetBrains AI Assistant / Junie | 11% combined (9% AI Assistant, 5% Junie) | — |
| ChatGPT (chatbot, for coding) | 28% | — |
| Gemini (chatbot) | 8% | — |
| Claude (chatbot) | 7% | — |

(All figures from https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/)

- Satisfaction metric: Claude Code CSAT 91%, NPS +54 (scale −100 to +100) — same source.
- Overall: **90% of developers regularly used at least one AI tool at work** for coding/development tasks in January 2026; **74% had adopted specialized AI dev tools** (assistants/editors/agents, excluding generic chatbots like ChatGPT) — same source.

### 2b. "AI Coding Agents: Adoption Trends" (Developer Ecosystem Survey 2026, 10th edition)
- **Publisher:** JetBrains
- **Publication date:** August 2026 (URL dated 2026/08)
- **URL:** https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/
- **Field dates:** May–July 2026
- **Sample / population:** "more than 15,000 professional developers worldwide," same job-role definition of "professional developers" as above (~90% Developer/Programmer/SWE); statistically reweighted by region, employment status, programming language, and JetBrains-product familiarity.
- **Question wording:** "using AI coding agents at work at least weekly" (adoption/frequency at work), plus a separate "most-used"/primary-tool metric; distinct from a "past year" usage question.

**Table: AI coding tool adoption ("used at work"), May–July 2026, global**

| Tool | % adoption (May–Jul 2026) | % adoption (Jan 2026, same series) |
|---|---|---|
| Claude Code | 39% (47% in the US; "most-used" tool for 31% of all developers, an ~80% regular-use→primary-tool conversion rate) | 18% |
| GitHub Copilot | 21% (79% awareness globally, 86–90% in Europe/UK/US; 39% of Copilot users use it inside JetBrains IDEs) | 29% |
| OpenAI Codex | 16% (awareness rose 27%→65%) | 3% |
| Cursor | 12% (biggest drop in China: 28%→16%) | 18% |
| OpenCode (open source) | 7% (42% awareness) | n/a (new) |
| Google Antigravity | 6% (stable; awareness 29%→47%; 15% adoption in India) | 6% |
| JetBrains AI (IDEs + Junie combined) | ~9% | 11% |

- **90% of professional developers used AI coding agents at work at least weekly** as of May–July 2026; **68% used them daily.**
- Methodology note: "professional developers" job-role definition and weighting scheme documented at https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ (methodology section) and https://lp.jetbrains.com/devecosystem-data-playground/methodology/.

(All figures from https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ unless noted)

### Gaps for JetBrains
- No explicit $-spend/subscription-cost figures found in either post.
- The two posts use **different question framings** ("used at work"/regular adoption vs. "at least weekly" vs. "most-used/primary tool"), so the Jan-2026 and May–Jul-2026 numbers in the tables above are from the same underlying tracking series but are not perfectly identical metrics wave-to-wave per JetBrains' own framing — treat the "change" column as directionally accurate per JetBrains' narrative, not as an exact like-for-like delta.

---

## 3. The Pragmatic Engineer — "AI Tooling for Software Engineers in 2026"

- **Publisher:** The Pragmatic Engineer (Gergely Orosz), independent newsletter/subscription publication
- **Publication date:** ~April 2026 (article URL slug "ai-tooling-2026"; referenced by other sites as published around April 9, 2026 — not independently confirmed via an on-page timestamp, flagged as approximate)
- **URL:** https://newsletter.pragmaticengineer.com/p/ai-tooling-2026
- **Field dates:** January 27 – February 17, 2026 ("the survey ran for weeks, between 27 January and 17 February 2026")
- **Sample / population:** **906 respondents** — self-selected readers/subscribers of The Pragmatic Engineer newsletter (NOT a random sample of all developers; skews toward experienced professionals at tech-forward companies). 55% of respondents are engineers, 34% engineering leadership (leads, EMs, directors+). Median experience: 11–15 years. Most respondents are in Europe or the US. This is a **follow-up to a prior wave from ~9 months earlier (May 2025)**, enabling trend comparisons.
- **Question wording:** *"Which AI tools do you use for work?"* (multi-select, "most-used AI tools by mentions" — a **mentions-based, not "% who use" in the strict survey sense**, though reported alongside clean percentages for several cross-tabs); plus a separate *"Which AI tools do you love using the most, and why?"* (open-ended, coded into "most loved" mention counts).

### Table: Tool usage among respondents who **regularly use AI agents** (n=507, i.e., the 55% of the 906 who said they regularly use agents)

| Tool | % usage (regular-agent-user subgroup) |
|---|---|
| Claude Code | 71% |
| GitHub Copilot | 46% |
| Cursor | 39% |

(Source: https://newsletter.pragmaticengineer.com/p/ai-tooling-2026 — chart captioned "Tool usage by regular users of AI agents. Claude Code is the clear leader (71% usage), followed by GitHub Copilot (46%) and Cursor (39%)." The article notes this subgroup's tool mix is "almost identical" to the full-survey mix, but the full-survey percentages themselves are presented only as a ranked list by mention count, not as exact percentages, in the body text.)

### Table: Tool usage at the **smallest companies/teams** (one company-size slice; exact percentages given)

| Tool | % usage at smallest companies |
|---|---|
| Claude Code | 75% |
| Chatbots (combined) | 55% |
| Cursor | 42% |
| GitHub Copilot | 35% |
| OpenAI Codex | 26% |
| Gemini CLI | 14% |
| OpenCode | 13% |

- At the **largest companies (10,000+ employees)**, GitHub Copilot overtakes Claude Code (exact % not given in text, shown only as a chart); the article states this reflects "enterprise procurement" and Microsoft's enterprise bundling.
- Nine months earlier (~May 2025 survey), GitHub Copilot usage was **46%**; "since then, it's barely risen" (i.e., ~46% also in this wave, per the article's own comparison, though this 46% figure appears to double as the May-2025 figure and the regular-agent-user-subgroup 2026 figure above — the two should not be conflated; see caveats).
- Cursor usage grew ~35% (relative growth in mention count) over the same nine months.
- OpenAI Codex (did not exist at prior wave) already reached "60% of Cursor's usage" (relative comparison, not an absolute %).

### Table: "Most loved" tool (open-ended, coded mentions; % of all 906 respondents naming each)

| Tool | % naming it as most loved |
|---|---|
| Claude Code | 46% |
| Cursor | 19% |
| Claude (as a model/chat brand, separate from Claude Code) | 11% |
| GitHub Copilot | 9% |

(Claude Code + Claude models combined = 57% per the article's own framing. Source: same URL, section "We asked respondents: 'Which AI tools do you love using the most, and why?'")

### Models used for coding (ranked, not exact % given in free text — described as a chart)
- "Anthropic's Opus and Sonnet dominate... Opus 4.5 and Sonnet 4.5 ... come up more often than all other models, combined." ~1 in 8 respondents say they just use whatever model is the company default. Other mentioned models (unranked): Cursor's Composer/Composer-1, Kimi K2.5, DeepSeek R1/V3.2/Coder, Qwen3, Grok, Mistral. Source: same URL.

### Frequency/mainstream-adoption stats
- **95% use AI tools weekly or more** (only 2.1% don't use AI tools at all).
- **75% use AI for at least half their software engineering work; 56% do 70%+ of their work with AI.**
- **70%** of respondents use 2–4 different AI tools simultaneously; 15% use just one; 15% use 5+.
- **55% (507 people) regularly use AI agents**; agent usage by seniority: Staff+ engineers 63.5%, regular engineers 49.7%, engineering managers 46.1%, directors/VPs 51.9%.
(All: https://newsletter.pragmaticengineer.com/p/ai-tooling-2026)

### Gaps for Pragmatic Engineer
- Full-survey (all 906) exact tool-usage percentages for the "most-used" chart (Claude Code / chatbots / GitHub Copilot / Cursor / Codex / Gemini CLI / OpenCode / Antigravity / Junie / Zed / Windsurf / Amp / Augment / Factory) are shown only as **images/charts** in the newsletter; the free, non-paywalled text gives exact numbers only for the sub-slices above (regular-agent-users, smallest-company-size, "most loved"). The complete ranked list for the whole sample could not be extracted as an exact percentage table from the accessible HTML text — only rank order was recoverable for the full-sample chart.
- No dollar-spend/subscription-cost breakdown found in the accessible (non-paywalled) portion; a **65-page detailed report is paywalled for full subscribers only** and was not accessed.
- Population is explicitly **not representative of all developers** — it is a newsletter-subscriber convenience sample skewing senior/staff+ and toward companies already engaged with cutting-edge tooling discourse. The author himself frames this as "Pragmatic Engineer readers," not "developers in general."

---

## 4. GitHub Octoverse 2026

- **Publisher:** GitHub (Microsoft)
- **Title:** "Octoverse 2026: Developer activity reaches new highs" / "Octoverse commits, pushes reach new highs in 2026 as developers build with agents"
- **Publication date:** October 2026
- **URL (landing):** https://octoverse.github.com/
- **URL (full report):** https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/
- **Methodology — IMPORTANT DIFFERENCE FROM OTHER ENTRIES:** Octoverse is **not a self-report survey**. It is derived from GitHub's own platform telemetry (commits, pushes, pull requests, Actions jobs, Copilot product usage logs) across GitHub's full user base, reported for the 12 months ending September 30, 2026 (and, for some metrics, month-by-month trend data from January–September 2026). "Population" = all ~225 million developers with GitHub accounts (public and private repositories), not a sampled/surveyed subset. This makes it **not directly comparable** to the self-reported "% of developers who use tool X" figures from Stack Overflow/JetBrains/Pragmatic Engineer.

### Key AI-related figures (all behavioral/telemetry, not self-report)
| Metric | Value | Period |
|---|---|---|
| Share of pull requests whose first draft was opened by an agent | 40%+ (up from 17% in March 2026) | September 2026 |
| Agent-opened PRs in September 2026 (absolute) | 110 million | Sept 2026 (≈6x March's volume) |
| GitHub Copilot monthly active users using agentic features | 55% (up from 35% a year earlier) | — |
| Copilot cloud-agent usage growth (assign-a-task-and-walk-away mode) | +230% YoY | — |
| Copilot agent-chat usage growth | +85% YoY | — |
| Copilot users who personally selected more than one model (of those who select a model themselves) | 61% (up from 50% four months earlier) | September 2026 |
| Distinct models used by paying Copilot users | 29 (May 2026) → 47 (September 2026) | — |
| Top single model's share of Copilot requests | No single model exceeded 25% of requests | September 2026 |
| Split of developer-selected Copilot requests by model category | General purpose 38%, Deep reasoning/planning 37%, Fast/lightweight 25% | September 2026 |
| Paying Copilot users who used "auto model selection" at least once | 63% | September 2026 |
| Repos with an agent config file — commit volume vs. repos without | 8x as many commits | repos created in 2026 |
| Merged PRs with detected AI involvement, top languages | TypeScript 44.1%, Python 41.1%, Rust 40.4%, Java 21.2% | trailing 12 months |

(All figures: https://github.blog/news-insights/octoverse/octoverse-commits-pushes-reach-new-highs-in-2026-as-developers-build-with-agents/)

### Gaps for Octoverse
- **No vendor/brand-level model-share breakdown** (e.g., % of requests to Claude vs. GPT vs. Gemini models) was published — only the three functional buckets (general purpose / deep reasoning / fast-lightweight) and the count of distinct models, with "no model over 25%." This is a deliberate editorial choice by GitHub (possibly to avoid naming specific competing vendors' market share within its own product).
- **The model-choice and agentic-feature statistics are scoped only to GitHub Copilot users** — they say nothing about the relative popularity of Copilot vs. Claude Code vs. Cursor etc. at the market level (those tools are not necessarily used through GitHub Copilot's billing/telemetry).
- No subscription/spend figures published.

---

## 5. DORA 2026 — "ROI of AI-Assisted Software Development" (v. 2026.01)

- **Publisher:** Google Cloud, DORA (DevOps Research and Assessment) team, with Google Cloud's "delta" innovation/consulting practice
- **Title:** "ROI of AI-Assisted Software Development" (report version 2026.01)
- **Publication date:** ~May 2026 (per InfoQ's coverage, dated 2026/05)
- **URL:** https://dora.dev/ai/roi/report/ (landing/intro page: https://dora.dev/ai/)
- **Secondary confirmation:** https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/
- **IMPORTANT CAVEAT:** This 2026 report is explicitly a **follow-up/framework document**, not a freshly fielded survey with new tool-adoption percentages. Per InfoQ's primary-source-quoting coverage, it is "a follow up to the 2025 DORA State of AI-Assisted Software Development report" (https://cloud.google.com/resources/content/2025-dora-ai-assisted-software-development-report) and "authored by a team from Google Cloud's DORA group and its delta innovation practice." It builds an ROI/ "J-curve" calculation framework (illustrative math: ~$11.6M value vs. $8.4M investment, 39% ROI, ~8-month payback for a hypothetical 500-person org) on top of the **2025 DORA survey's findings** (the underlying 2025 "State of AI-Assisted Software Development" report, published September 2025, is outside this research's 2026 window and was not itself re-validated here for sample size/field dates).
- **No new 2026 tool-adoption percentages (e.g., % using Claude Code vs. Copilot vs. Cursor), no model-share data, and no spend/subscription percentages were found in this 2026 publication.** It is included here for completeness because it is a 2026-published, large-reach DORA-branded artifact, but **it should not be cited as a source of 2026 tool-usage-share numbers** — it does not contain them.

---

## 6. Retool "The State of AI Governance in 2026" (found, but out of scope for tool-usage shares)

- **Publisher:** Retool
- **Publication date:** June 17, 2026
- **URL:** https://retool.com/blog/ai-governance-report-2026
- **Sample / population:** 307 senior technology and security leaders (CTOs, CIOs, CISOs) at medium-to-enterprise companies — **IT/security leadership, not developers**, and n=307 is below the n≥1000 threshold requested.
- **Content:** Governance/risk statistics only — e.g., 93% of leaders at least "somewhat concerned" about vibe-coded tools in production; only 8% describe internal-tool governance as "strong"; 58% call AI coding tools "net positive" for engineering (71% of CTOs vs. 47% of CISOs); 55% want centralized platform-level governance. **No AI coding tool / model / chatbot usage-share percentages (no Claude Code/Copilot/Cursor-style breakdown) and no subscription-spend figures were found in this report.** Included only to document that it was checked and found not to match the requested data type.

---

## Surveys searched for but not found as fresh, non-paywalled 2026 primary publications with tool-share data
- No independent "State of AI in Engineering" report from Retool matching the brief (the only 2026 Retool report found is the governance one above, and an adjacent "AI build vs. buy" report was referenced but not fetched/verified — URL seen only in passing: https://retool.com/blog/ai-build-vs-buy-report-2026; not verified in this pass).
- No 2026 DORA report with fresh self-reported tool-adoption percentages (see §5 caveat).

---

## Comparability caveats

1. **Different question wording changes what "usage" means.** Stack Overflow asks "have you used X **in the past year**" (a low bar, multi-select, inflates adoption relative to active/regular use). JetBrains asks about "**adoption at work**" and separately "**used at least weekly**" / "**daily**" (a higher, frequency-gated bar) and also tracks a "most-used/primary tool" metric distinct from "any usage." Pragmatic Engineer's headline table is **mentions in an open/multi-select "which tools do you use for work" question**, and its cleanest percentages come from sub-slices (regular-agent-users, smallest-company-size, "most loved") rather than the whole sample. GitHub Octoverse reports **behavioral telemetry** (actual PRs/commits/model-selection events), not self-reported usage at all. These four "usage %" concepts are not interchangeable, and headline numbers (e.g., Claude Code "66%" at Stack Overflow vs. "39%" at JetBrains vs. "71%" among Pragmatic Engineer's agent-using subgroup) reflect different questions and different populations, not necessarily different "true" adoption levels.

2. **Population/sampling differ substantially.** Stack Overflow's sample is self-selected visitors to Stack Overflow/its channels (broad, global, but skews toward Stack Overflow's existing audience). JetBrains' AI Pulse/Developer Ecosystem samples are recruited via paid social ads (Instagram, Zhihu) plus a JetBrains customer panel (~16% of responses), then statistically reweighted by region/employment/language/JetBrains-familiarity — likely to skew toward developers reachable via social ads and with at least some JetBrains-ecosystem overlap. Pragmatic Engineer's 906 respondents are **newsletter subscribers**, skewing strongly toward senior/staff+ engineers and engineering leadership at tech-forward companies — explaining why its Claude Code figures (e.g., 71–75% in its subgroups) run notably higher than Stack Overflow's or JetBrains'. GitHub Octoverse covers GitHub's entire platform population (~225M accounts) but is Copilot-centric for the model-choice statistics, so it cannot speak to Claude Code/Cursor/Gemini-CLI market share at all.

3. **Field-date timing varies within 2026, and the market moved fast enough that this matters.** Pragmatic Engineer fielded Jan 27–Feb 17, 2026; JetBrains AI Pulse fielded January 2026 (same window) and then re-fielded May–July 2026 (a second wave, showing substantial within-year change, e.g., Claude Code adoption 18%→39%); Stack Overflow fielded June 23–Aug 5, 2026 (per secondary citation, not independently re-verified); Octoverse's survey-like statistics are really a rolling 12-month telemetry window ending September 30, 2026, with an explicit inflection around June 2026. Comparing any two reports' "current %" without noting the month is misleading given the pace of change JetBrains itself documents (e.g., Codex 3%→16% in 5 months).

4. **No survey in this set reports a full, comparable brand-level breakdown of general-purpose chat assistants (ChatGPT vs. Claude.ai vs. Gemini) at scale.** Stack Overflow reports chat tools only as one combined 62.5% category; JetBrains' April 2026 post gives isolated figures (ChatGPT 28% for coding, Gemini 8%, Claude chatbot 7%) but these are from the January 2026 wave only, not updated in the August wave; Pragmatic Engineer describes chatbot mentions as "nearly equal" for ChatGPT/Gemini/Claude without giving a clean exact-percentage table in the accessible text.

5. **Spend/subscription-cost data is essentially absent across all surveys reviewed.** None of Stack Overflow 2026, JetBrains 2026 (either wave), or Pragmatic Engineer's free content published a clear $-denominated personal or company AI-tool spend figure in the material checked. Stack Overflow has cost-sensitivity questions (`AICost`, `AICostPrompt`) but no published percentage data page was found for them as of this research pass.

6. **DORA's 2026 publication and Retool's 2026 publication are not comparable to the others at all** — DORA 2026 is an ROI-framework document built on prior-year survey data (no fresh tool-share numbers), and Retool 2026 surveys IT/security leaders about governance risk, not developers about tool usage. Both are included for completeness/transparency but should not be used as sources of 2026 tool-usage percentages.
