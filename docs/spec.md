# HN AI setup survey — spec

Status: ready-for-human (report done 2026-11-05 → report.md)

Goal: usage statistics of AI tools / harnesses / models / subscriptions based on what authors and commenters on Hacker News write about their personal setup. Top → bottom by number of unique authors.

## Decisions (grilling 2026-11-05)

| # | Decision |
|---|---|
| Window | 2025-11-05 → 2026-11-05; yearly ranking + quarterly trend of the top 10 |
| Scope | all of AI; coding (harnesses, agents, models) as the main section, the rest (chat apps, local LLMs, voice…) secondary |
| Corpus | Ask HN threads about setup/workflow/spend — all comments including nested ones. Articles about a personal setup → only the author's setup (1 vote). Launch threads and product Tell HN → only in the source summary, not counted |
| Unit | unique author × tool (yearly once per corpus, in the trend once per quarter) |
| What counts | only current personal use. Churn (“I stopped / I switched from X to Y”) → separate from → to table. Mentions without personal experience are not counted |
| Rankings | (1) harnesses/apps, (2) models by family with explicit / implicit columns (Claude Code → Claude, Codex CLI → GPT, Gemini CLI → Gemini), versions in detail, (3) subscriptions/tiers + monthly spend distribution (median; <$20, $20–100, $100–250, >$250) |
| Long tail | < 3 authors → separate section, not the main ranking |
| Method | Algolia HN API (`hn.algolia.com/api/v1/items/<id>`) → regex prefilter (tool names + generic triggers “I use”, “I pay”, “my setup”, “$/mo”) → LLM classification `uses` / `left` / `mention_only` → alias normalization |
| Output | `spec.md` (this file), `report.md` (rankings, trend, churn, spend, sources), `infographic.html` (visual report, offline), `mentions.csv` (author, date, quarter, item_id, link, tool, category, status, model_explicit, model_implied, spend_usd_mo, quote) |
| Language | report in Slovak, tool names and quotes in English |

## Sources for approval

### A. Ask HN — all comments count (core, ~3,000 comments)

| ID | Com. | Date | Thread |
|---|---|---|---|
| [50366117](https://news.ycombinator.com/item?id=50366117) | 396 | 2026-11-04 | What's your current AI agentic setup? |
| [47388646](https://news.ycombinator.com/item?id=47388646) | 616 | 2026-03-15 | How is AI-assisted coding going for you professionally? |
| [48542100](https://news.ycombinator.com/item?id=48542100) | 563 | 2026-06-15 | Has anyone replaced Claude/GPT with a local model for daily coding? |
| [46255285](https://news.ycombinator.com/item?id=46255285) | 469 | 2025-12-13 | How can I get better at using AI for programming? |
| [48771515](https://news.ycombinator.com/item?id=48771515) | 206 | 2026-07-03 | Is anyone experimenting with different ways of using LLMs for coding? |
| [48413629](https://news.ycombinator.com/item?id=48413629) | 136 | 2026-06-05 | What is your (AI) dev tech stack / workflow? |
| [48492118](https://news.ycombinator.com/item?id=48492118) | 124 | 2026-06-11 | How do you get into a flow state when using AI to code? |
| [46292682](https://news.ycombinator.com/item?id=46292682) | 66 | 2025-12-16 | How are you LLM-coding in an established code base? |
| [46993479](https://news.ycombinator.com/item?id=46993479) | 60 | 2026-02-12 | Are you using an agent orchestrator to write code? |
| [49934037](https://news.ycombinator.com/item?id=49934037) | 48 | 2026-10-02 | Is anybody producing good code with coding agents? |
| [50337431](https://news.ycombinator.com/item?id=50337431) | 46 | 2026-11-02 | What hardware are you using to run local LLMs? |
| [49290713](https://news.ycombinator.com/item?id=49290713) | 41 | 2026-08-13 | How much money do you spend monthly on subscriptions for AI models? |
| [47559293](https://news.ycombinator.com/item?id=47559293) | 32 | 2026-03-29 | How are you keeping AI coding agents from burning money? |
| [48587808](https://news.ycombinator.com/item?id=48587808) | 31 | 2026-06-18 | What tools are you using for AI-assisted code review? |
| [47616250](https://news.ycombinator.com/item?id=47616250) | 28 | 2026-04-02 | What is your dev set up like? |
| [50016644](https://news.ycombinator.com/item?id=50016644) | 19 | 2026-10-09 | Are you a subscribed LLM or a locally deployed open-source model? |
| [48166147](https://news.ycombinator.com/item?id=48166147) | 16 | 2026-05-17 | What LLM models are you using and why? |
| [49449290](https://news.ycombinator.com/item?id=49449290) | 16 | 2026-08-26 | Are you still using AI code autocomplete? |
| [49586386](https://news.ycombinator.com/item?id=49586386) | 16 | 2026-09-06 | Any Software Engineers here who enjoy their AI-native dev workflow? |
| [49848426](https://news.ycombinator.com/item?id=49848426) | 15 | 2026-09-25 | Which model do you use for work? |
| [46731068](https://news.ycombinator.com/item?id=46731068) | 71 | 2026-01-23 | What's the current best local/open speech-to-speech setup? (non-coding) |

### B. Borderline — default **don't count** (skewed toward a specific product or off-topic); say if anything should move to A

| ID | Com. | Date | Thread | Reason |
|---|---|---|---|---|
| [46838946](https://news.ycombinator.com/item?id=46838946) | 189 | 2026-01-31 | Any real OpenClaw users? | product-specific |
| [48989357](https://news.ycombinator.com/item?id=48989357) | 33 | 2026-07-21 | Claude Code or Codex? | binary, overrepresents 2 tools |
| [48612758](https://news.ycombinator.com/item?id=48612758) | 23 | 2026-06-20 | Do you use Claude Code, Codex, or something else? | ditto |
| [47750069](https://news.ycombinator.com/item?id=47750069) | 17 | 2026-04-13 | Is Codex really on par with Claude Code? | ditto |
| [46400129](https://news.ycombinator.com/item?id=46400129) | 32 | 2025-12-27 | How are you sandboxing coding agents? | sandboxing, not setup |
| [47581097](https://news.ycombinator.com/item?id=47581097) | 45 | 2026-03-30 | Addicted to the dev workflow of coding with agents? | feelings-based |
| [46896309](https://news.ycombinator.com/item?id=46896309) | 15 | 2026-02-05 | Has your whole engineering team gone big into AI coding? | team, not personal |
| [46030021](https://news.ycombinator.com/item?id=46030021) | 19 | 2025-11-24 | What tools do you pay for that feel overpriced? | general SaaS |

### C. Articles about a personal setup — only the author counts (1 vote), comments don't

| ID | Com. | Date | Article |
|---|---|---|---|
| [47106686](https://news.ycombinator.com/item?id=47106686) | 591 | 2026-02-22 | [How I use Claude Code: Separation of planning and execution](https://boristane.com/blog/how-i-use-claude-code/) |
| [47394022](https://news.ycombinator.com/item?id=47394022) | 528 | 2026-03-16 | [How I write software with LLMs](https://www.stavros.io/posts/how-i-write-software-with-llms/) |
| [46903558](https://news.ycombinator.com/item?id=46903558) | 401 | 2026-02-05 | [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey) |
| [48933310](https://news.ycombinator.com/item?id=48933310) | 310 | 2026-07-16 | [The LLM Critics Are Right. I Use LLMs Anyway](https://www.theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway/) |
| [50355767](https://news.ycombinator.com/item?id=50355767) | 306 | 2026-11-03 | [How I use AI (Oct 2026)](https://ben.stolovitz.com/posts/how-use-ai-oct-2026/) |
| [47648828](https://news.ycombinator.com/item?id=47648828) | 301 | 2026-04-05 | [Eight years of wanting, three months of building with AI](https://lalitm.com/post/building-syntaqlite-ai/) |
| [46933223](https://news.ycombinator.com/item?id=46933223) | 241 | 2026-02-08 | [Eight more months of agents](https://crawshaw.io/blog/eight-more-months-of-agents) |
| [49410932](https://news.ycombinator.com/item?id=49410932) | 176 | 2026-08-23 | [My agent.md to improve LLM-assisted code quality](https://fabiensanglard.net/agent.md/index.html) |
| [47494890](https://news.ycombinator.com/item?id=47494890) | 167 | 2026-03-23 | [How I'm Productive with Claude Code](https://neilkakkar.com/productive-with-claude-code.html) |
| [49272484](https://news.ycombinator.com/item?id=49272484) | 63 | 2026-08-12 | [My Agent Setup](https://chad.cm/posts/2026-8-11-my-agent-setup) |
| [49234675](https://news.ycombinator.com/item?id=49234675) | 546 | 2026-08-09 | [How I use LLMs to learn complex topics](https://laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn/) (non-coding) |

### D. Only in the source summary (context, not counted)

Launch / product threads with high engagement, e.g. [OpenCode – Open source AI coding agent](https://news.ycombinator.com/item?id=47460525) (618), [Tell HN: I'm 60 years old. Claude Code has re-ignited a passion](https://news.ycombinator.com/item?id=47282777) (988), [Tell HN: Anthropic no longer allowing Claude Code subscriptions to use OpenClaw](https://news.ycombinator.com/item?id=47633396) (827). Final selection of up to 10 items when writing the report.

## Phase 2: extension to more sources (grilling 2026-11-05 afternoon)

Status: done (v2 + Readwise published 2026-11-05 at https://aisetups.ringil.cc/ via Cloudflare Pages connected to GitHub)

| # | Decision |
|---|---|
| Q18 Window | all sources including HN unified to **calendar year 2026** (2026-01-01 → 2026-11-05); HN is re-filtered from existing data |
| Sources | **HN** (Ask HN comments), **Lobste.rs**, **Tildes**, ~~Reddit~~ (see Q30), **Blogs (authors)** = HN articles + Readwise Reader (later/starred/archive + feeds of the ITech folder including Swamp Club), **Surveys** only as calibration |
| Q19 Readwise | only the article author's setup counts (1 vote); the publication date in 2026 decides, or the save date if it is missing |
| Q20 Readwise selection | keyword prefilter → LLM judges “does the author describe their own setup?” → list for approval |
| Q21 Overlap | blogs from both HN and Readwise are merged into the “Blogs (authors)” source and deduplicated by URL |
| Q22 Reddit | only r/ExperiencedDevs + r/programming; subreddits focused on a specific tool excluded |
| Q23 Lobste.rs/Tildes | on-topic threads for 2026 → list approval → all comments (on Lobste.rs also discussions under articles) |
| Q24 Surveys | separate “community vs. surveys” section, not merged into the rankings |
| Output | a ranking per source + side-by-side source comparison + combined ranking; both report.md and infographic.html get extended |
| Q25 Swamp Club | written posts treated as blogs (1 author = 1 vote); Swamp excluded from the cross-source comparison; YouTube only with a transcript in Reader |
| Q26/Q27 Interfaces | the entire 2026 corpus re-read with the v2 schema (`interface`, `interface_explicit`, `host`, `via`), without a prefilter; Lobste.rs + Tildes all 213 threads |
| Q28 Publishing | only the infographic goes on the web (aggregated numbers, no usernames); `mentions.csv` with usernames stays only in the vault |
| Q29 When | publish right after v2; add Readwise in the next version |
| Q30 Reddit | **dropped**: the Reddit Responsible Builder Policy requires approval and prohibits research outside the Reddit for Researchers program |
| Access | Readwise token in `~/.config/readwise/token`, Reddit script app in `~/.config/reddit/client` (line 1 = client id, line 2 = secret); never printed or saved to the vault |

## Appendix: Lobste.rs and Tildes, candidate threads 2026 (213)

Proposal: include **all** (high + medium by title). Comments with any tool mention (956 of 7,724) go to LLM classification. Threads with “low” relevance (473) are excluded.

<details><summary>Thread list (source · relevance · date · comments · with tool mention)</summary>

| Source | Rel. | Date | Com. | With tool | Thread |
|---|---|---|---|---|---|
| lobsters | high | 2026-06-16 | 56 | 19 | [Running local models is good now](https://lobste.rs/s/hwqdvt) |
| lobsters | high | 2026-04-21 | 49 | 16 | [Is Claude Code going to cost $100/month? Probably not—it’s all very confusing](https://lobste.rs/s/0qdgc0) |
| lobsters | high | 2026-04-02 | 42 | 16 | [I used AI. It worked. I hated it](https://lobste.rs/s/7d8dxv) |
| lobsters | high | 2026-03-22 | 42 | 13 | [Is Local the Future of AI?](https://lobste.rs/s/n1h2tl) |
| lobsters | high | 2026-01-12 | 30 | 13 | [Anthropic blocks third-party tools using Claude Code OAuth tokens](https://lobste.rs/s/mhgog9) |
| lobsters | high | 2026-03-14 | 17 | 10 | [Getting started with Claude for software development](https://lobste.rs/s/k0cm8c) |
| lobsters | high | 2026-03-28 | 25 | 8 | [BubbleWrap your dev env and agents](https://lobste.rs/s/u4bws9) |
| lobsters | high | 2026-08-02 | 24 | 8 | [I'm (mostly) picking models on speed now, not intelligence](https://lobste.rs/s/aso7dh) |
| lobsters | high | 2026-01-18 | 20 | 7 | [My thoughts on Gas Town after 10,000 hours of Claude Code](https://lobste.rs/s/txknsm) |
| lobsters | high | 2026-08-10 | 51 | 7 | [No, local models will not win](https://lobste.rs/s/kkqqdn) |
| lobsters | high | 2026-07-04 | 50 | 6 | [Better Models: Worse Tools](https://lobste.rs/s/yrmpxy) |
| lobsters | high | 2026-01-20 | 10 | 6 | [My week with opencode](https://lobste.rs/s/oxeeyz) |
| lobsters | high | 2026-02-27 | 21 | 6 | [An AI agent coding skeptic tries AI agent coding, in excessive detail](https://lobste.rs/s/ykwb2z) |
| lobsters | high | 2026-06-04 | 18 | 5 | [What happened to tab autocomplete?](https://lobste.rs/s/humg0y) |
| lobsters | high | 2026-02-09 | 57 | 2 | [Fine, I'll Try AI](https://lobste.rs/s/9kb1xw) |
| lobsters | high | 2026-09-12 | 18 | 2 | [Useful Things Agents Can Do That Are Not Writing Code](https://lobste.rs/s/ub8q3s) |
| lobsters | high | 2026-06-20 | 15 | 2 | [Effective use-cases for LLMs](https://lobste.rs/s/77kygu) |
| lobsters | high | 2026-02-05 | 19 | 1 | [My AI Adoption Journey](https://lobste.rs/s/87rudf) |
| lobsters | high | 2026-05-25 | 46 | 1 | [Using AI to write better code more slowly](https://lobste.rs/s/lkv0sh) |
| lobsters | high | 2026-10-16 | 23 | 0 | [Do you let LLMs write both your tests and your code?](https://lobste.rs/s/miwcai) |
| lobsters | high | 2026-02-16 | 15 | 0 | [I Sold Out for $20 a Month and All I Got Was This Perfectly Generated Terraform](https://lobste.rs/s/stwus1) |
| lobsters | medium | 2026-01-11 | 296 | 34 | [Don't fall into the anti-AI hype](https://lobste.rs/s/cmsfbu) |
| lobsters | medium | 2026-09-04 | 98 | 19 | [Surviving Code Reviews in the era of AI](https://lobste.rs/s/7tpc5q) |
| lobsters | medium | 2026-03-15 | 30 | 16 | [I let Claude Code configure my Arch install](https://lobste.rs/s/8pfxqy) |
| lobsters | medium | 2026-01-18 | 100 | 14 | [Agent Psychosis: Are We Going Insane?](https://lobste.rs/s/0pxvyd) |
| lobsters | medium | 2026-01-24 | 135 | 14 | [AI tribalism](https://lobste.rs/s/cw6f2s) |
| lobsters | medium | 2026-01-23 | 73 | 13 | [AGENTS.md as a dark signal](https://lobste.rs/s/x0qrlm) |
| lobsters | medium | 2026-03-31 | 46 | 13 | [Reading leaked Claude Code source code](https://lobste.rs/s/6c8cwq) |
| lobsters | medium | 2026-10-12 | 112 | 12 | [Linus Torvalds Working On A Hefty Linux Kernel Improvement With Claude Code](https://lobste.rs/s/iq5xtw) |
| lobsters | medium | 2026-04-09 | 42 | 12 | [Let’s talk about LLMs](https://lobste.rs/s/j2l2ya) |
| lobsters | medium | 2026-04-16 | 16 | 9 | [The Claude Coding Vibes Are Getting Worse](https://lobste.rs/s/xaicu8) |
| lobsters | medium | 2026-08-12 | 81 | 9 | [I'm done using AI](https://lobste.rs/s/rfiuko) |
| lobsters | medium | 2026-09-30 | 80 | 9 | [The AI Pascal’s Wager](https://lobste.rs/s/hbjy0b) |
| lobsters | medium | 2026-07-06 | 18 | 8 | [GLM 5.2 and the coming AI margin collapse](https://lobste.rs/s/ua1gxl) |
| lobsters | medium | 2026-06-10 | 59 | 8 | [Blogging with an LLM assistant](https://lobste.rs/s/tdvu7a) |
| lobsters | medium | 2026-03-30 | 31 | 8 | [copilot edited an ad into my pr](https://lobste.rs/s/0o60nu) |
| lobsters | medium | 2026-03-10 | 95 | 8 | [AI should help us produce better code](https://lobste.rs/s/tiktds) |
| lobsters | medium | 2026-01-22 | 68 | 8 | [Your App Subscription Is Now My Weekend Project](https://lobste.rs/s/m0twb1) |
| lobsters | medium | 2026-10-02 | 28 | 7 | [The Four Horsemen of Agentic Coding](https://lobste.rs/s/wevegu) |
| lobsters | medium | 2026-02-05 | 47 | 7 | [Building a C compiler with a team of parallel Claudes](https://lobste.rs/s/6nahuh) |
| lobsters | medium | 2026-01-16 | 35 | 7 | [Histomat of F/OSS: We should reclaim LLMs, not reject them](https://lobste.rs/s/go7hr7) |
| lobsters | medium | 2026-10-09 | 22 | 7 | [Why Are Coding Agents So Dumb?](https://lobste.rs/s/t5htlf) |
| lobsters | medium | 2026-04-28 | 14 | 7 | [Warp is now open-source](https://lobste.rs/s/ccbjxb) |
| lobsters | medium | 2026-09-05 | 113 | 7 | [Is it too much to ask devs to use AI to review their hand-crafted code?](https://lobste.rs/s/fxccx9) |
| lobsters | medium | 2026-10-25 | 59 | 6 | [“AI Skills” are worthless in 2026](https://lobste.rs/s/x1s5oq) |
| lobsters | medium | 2026-06-21 | 68 | 6 | [Is AI ruining our skills? Early results are in and they’re not good](https://lobste.rs/s/d0vsgl) |
| lobsters | medium | 2026-01-14 | 19 | 6 | [Coding on a Phone: What I Learned Building Software on Mobile in the Last Three Weeks](https://lobste.rs/s/mj7k0s) |
| lobsters | medium | 2026-01-13 | 20 | 6 | [AI Coding Assistants Are Getting Worse](https://lobste.rs/s/6skrep) |
| lobsters | medium | 2026-06-04 | 57 | 6 | [AI enthusiasts are in a race against time, AI skeptics are in a race against entropy](https://lobste.rs/s/ri4flr) |
| lobsters | medium | 2026-08-02 | 20 | 6 | [Prevent cognitive debt by manually retyping LLM-generated code](https://lobste.rs/s/ui2vor) |
| lobsters | medium | 2026-09-01 | 44 | 6 | [The Endless Temptation of Claude](https://lobste.rs/s/qnffyn) |
| lobsters | medium | 2026-10-06 | 11 | 5 | [What is Codemode](https://lobste.rs/s/sshhsl) |
| lobsters | medium | 2026-09-11 | 136 | 5 | [Feeling sad about AI](https://lobste.rs/s/7guove) |
| lobsters | medium | 2026-06-25 | 32 | 5 | [The Exhaustion of Talking to a Tool](https://lobste.rs/s/csgzki) |
| lobsters | medium | 2026-06-11 | 25 | 5 | [our workplace LLM mass delusion](https://lobste.rs/s/lrjceq) |
| lobsters | medium | 2026-02-15 | 63 | 5 | [AI is slowly munching away my passion](https://lobste.rs/s/qmjejh) |
| lobsters | medium | 2026-07-27 | 76 | 5 | [On AI](https://lobste.rs/s/zljfgp) |
| lobsters | medium | 2026-08-08 | 32 | 5 | ["Code was never the hard part" is an insult to all programmers](https://lobste.rs/s/iixlsm) |
| lobsters | medium | 2026-02-22 | 61 | 5 | [You are not left behind](https://lobste.rs/s/vdueen) |
| lobsters | medium | 2026-05-05 | 26 | 5 | [claude code is not making your product better](https://lobste.rs/s/kn0jwm) |
| lobsters | medium | 2026-02-27 | 25 | 4 | [AI sandbox that runs on your homelab](https://lobste.rs/s/wdrawa) |
| lobsters | medium | 2026-08-17 | 33 | 4 | [Vetted AI code is hard to justify](https://lobste.rs/s/os20fa) |
| lobsters | medium | 2026-08-02 | 41 | 4 | [23 languages, one I can check](https://lobste.rs/s/j65lz5) |
| lobsters | medium | 2026-09-14 | 20 | 4 | ["Do You Still Read the Code?"](https://lobste.rs/s/qiwlzz) |
| lobsters | medium | 2026-05-31 | 26 | 4 | [vibecoding as adhd multiplier](https://lobste.rs/s/tsgoap) |
| lobsters | medium | 2026-03-06 | 26 | 4 | [I'm not consulting an LLM](https://lobste.rs/s/qorrgl) |
| lobsters | medium | 2026-01-16 | 14 | 4 | [Cutting LLM token Usage by ~80% using REPL driven document analysis](https://lobste.rs/s/xankns) |
| lobsters | medium | 2026-06-02 | 28 | 4 | [Quality in the Age of Slop](https://lobste.rs/s/8ohth3) |
| lobsters | medium | 2026-10-07 | 116 | 4 | [Software developers are not okay](https://lobste.rs/s/0gvyif) |
| lobsters | medium | 2026-02-24 | 11 | 4 | [How I got Claude to teach me dbt](https://lobste.rs/s/nmyrxg) |
| lobsters | medium | 2026-10-13 | 75 | 4 | [Where is all the new, good software?](https://lobste.rs/s/hjhufj) |
| lobsters | medium | 2026-06-24 | 22 | 3 | [The Coming Loop](https://lobste.rs/s/a7thxr) |
| lobsters | medium | 2026-06-08 | 62 | 3 | [Cleaning up after AI rockstar developers](https://lobste.rs/s/uvwcdo) |
| lobsters | medium | 2026-09-24 | 54 | 3 | [Pencils Down, Eyes Open: A Rails Developer After Rails World](https://lobste.rs/s/jiv1c5) |
| lobsters | medium | 2026-05-01 | 35 | 3 | [Why I Don’t Vibe Code](https://lobste.rs/s/vwmojf) |
| lobsters | medium | 2026-03-27 | 29 | 3 | [Which Programming Language Is Best for Claude Code?](https://lobste.rs/s/j5rw8d) |
| lobsters | medium | 2026-06-09 | 20 | 3 | [Grit: rewriting Git in Rust with agents](https://lobste.rs/s/galkdh) |
| lobsters | medium | 2026-03-22 | 15 | 3 | [The diminished art of coding](https://lobste.rs/s/g4sj0m) |
| lobsters | medium | 2026-03-21 | 37 | 3 | [Why craft-lovers are losing their craft](https://lobste.rs/s/vxsjiv) |
| lobsters | medium | 2026-08-15 | 144 | 3 | [Why I remain a skeptic](https://lobste.rs/s/fooyux) |
| lobsters | medium | 2026-09-14 | 24 | 3 | [We are all Product Engineers now](https://lobste.rs/s/agbpkq) |
| lobsters | medium | 2026-08-22 | 26 | 3 | [Linus Torvalds uses AI to debug an Intel GPU driver bug](https://lobste.rs/s/eyaz5f) |
| lobsters | medium | 2026-02-04 | 34 | 3 | [I miss thinking hard](https://lobste.rs/s/hfuiti) |
| lobsters | medium | 2026-04-12 | 14 | 2 | [The peril of laziness lost](https://lobste.rs/s/tmddcs) |
| lobsters | medium | 2026-09-17 | 45 | 2 | [I Don't Like LLMs](https://lobste.rs/s/pkj7mf) |
| lobsters | medium | 2026-06-04 | 11 | 2 | [Code is Cheap(er)](https://lobste.rs/s/onbcu5) |
| lobsters | medium | 2026-01-02 | 12 | 2 | [Welcome to Gas Town](https://lobste.rs/s/vd8q8g) |
| lobsters | medium | 2026-09-14 | 74 | 2 | [The contagion of fear](https://lobste.rs/s/1ifr5f) |
| lobsters | medium | 2026-04-25 | 72 | 2 | [Do I belong in tech anymore?](https://lobste.rs/s/xgtyyu) |
| lobsters | medium | 2026-10-03 | 66 | 2 | [The Era of Software Quality, or the Era of Ostriches?](https://lobste.rs/s/elziso) |
| lobsters | medium | 2026-04-05 | 17 | 2 | [Eight years of wanting, three months of building with AI](https://lobste.rs/s/gpqkcx) |
| lobsters | medium | 2026-07-13 | 41 | 2 | [Control the ideas, not the code](https://lobste.rs/s/5t3wzn) |
| lobsters | medium | 2026-01-09 | 26 | 2 | [Prompting 101: Show, don’t tell](https://lobste.rs/s/zdwvdw) |
| lobsters | medium | 2026-02-04 | 51 | 2 | [Competence as Tragedy](https://lobste.rs/s/2svv99) |
| lobsters | medium | 2026-10-01 | 17 | 2 | [Is sandboxing sufficient to contain rogue agents?](https://lobste.rs/s/zcr7in) |
| lobsters | medium | 2026-08-06 | 47 | 2 | [Taste Is All That's Left](https://lobste.rs/s/4qfkrz) |
| lobsters | medium | 2026-09-22 | 14 | 2 | [tokens too cheap to meter](https://lobste.rs/s/n4vfwm) |
| lobsters | medium | 2026-03-25 | 17 | 2 | [Thoughts on slowing the fuck down](https://lobste.rs/s/4i8uad) |
| lobsters | medium | 2026-02-14 | 65 | 2 | [A programmer's loss of identity](https://lobste.rs/s/m1mkjm) |
| lobsters | medium | 2026-03-09 | 24 | 2 | [Your LLM Doesn't Write Correct Code. It Writes Plausible Code](https://lobste.rs/s/dnqcvh) |
| lobsters | medium | 2026-04-11 | 13 | 2 | [With AI, you barely need a frontend framework](https://lobste.rs/s/qywh3s) |
| lobsters | medium | 2026-06-12 | 28 | 2 | [AI Agent Bankrupted Their Operator While Trying to Scan DN42](https://lobste.rs/s/ishgbs) |
| lobsters | medium | 2026-02-11 | 23 | 2 | [The AI Vampire](https://lobste.rs/s/irxjid) |
| lobsters | medium | 2026-02-08 | 12 | 2 | [I Am Happier Writing Code by Hand](https://lobste.rs/s/bnldoy) |
| lobsters | medium | 2026-02-06 | 11 | 2 | [Tactical tornado is the new default](https://lobste.rs/s/xq1ta4) |
| lobsters | medium | 2026-06-13 | 12 | 2 | [Talk more to your coding agents](https://lobste.rs/s/4rcwmh) |
| lobsters | medium | 2026-09-29 | 13 | 1 | [AI Didn’t Make Programming Easier. It Just Made It Differently Difficult](https://lobste.rs/s/qhszda) |
| lobsters | medium | 2026-02-10 | 29 | 1 | [I Started Programming When I Was 7. I'm 50 Now, and the Thing I Loved Has Changed](https://lobste.rs/s/7iford) |
| lobsters | medium | 2026-03-09 | 43 | 1 | [AI will fuck you up if you’re not on board](https://lobste.rs/s/6pvtem) |
| lobsters | medium | 2026-08-27 | 29 | 1 | [The turbulent AI era is here](https://lobste.rs/s/aixljs) |
| lobsters | medium | 2026-08-31 | 37 | 1 | [On not becoming a cyborg](https://lobste.rs/s/uxqdfr) |
| lobsters | medium | 2026-03-14 | 50 | 1 | [Thoughts on generative A.I](https://lobste.rs/s/ypes5v) |
| lobsters | medium | 2026-08-14 | 19 | 1 | [There Is Still No Silver Bullet](https://lobste.rs/s/pf0hfr) |
| lobsters | medium | 2026-09-12 | 12 | 1 | [Opusfived](https://lobste.rs/s/scyufg) |
| lobsters | medium | 2026-09-13 | 37 | 1 | [Don't call yourself an artisanal programmer](https://lobste.rs/s/dmlzwx) |
| lobsters | medium | 2026-02-08 | 17 | 1 | [AI fatigue is real and nobody talks about it](https://lobste.rs/s/gfsl25) |
| lobsters | medium | 2026-05-02 | 16 | 1 | [Agentic Coding is Burning Me Out](https://lobste.rs/s/k3delj) |
| lobsters | medium | 2026-10-01 | 19 | 1 | [Reducing the cognitive load of AI changes](https://lobste.rs/s/iwvjr0) |
| lobsters | medium | 2026-05-04 | 21 | 1 | [Nondeterminism's not the problem](https://lobste.rs/s/nmnmnq) |
| lobsters | medium | 2026-04-01 | 17 | 1 | [Everything Claude Saw: A Transparent Account of the Chardet v7 Rewrite](https://lobste.rs/s/972mji) |
| lobsters | medium | 2026-10-04 | 18 | 1 | [We’re going to need default hard budget caps on pretty much everything](https://lobste.rs/s/xkwswd) |
| lobsters | medium | 2026-01-27 | 18 | 1 | [Why AI Coding Advice Contradicts Itself](https://lobste.rs/s/hf6q1n) |
| lobsters | medium | 2026-09-28 | 17 | 1 | [What Would A Serious AI Product Look Like?](https://lobste.rs/s/q2rymh) |
| lobsters | medium | 2026-03-31 | 13 | 1 | [Early observations from Interviews with Engineering Teams Adopting AI](https://lobste.rs/s/olipz6) |
| lobsters | medium | 2026-03-17 | 27 | 1 | [A sufficiently detailed spec is code](https://lobste.rs/s/nlyezv) |
| lobsters | medium | 2026-10-12 | 22 | 1 | [What I've been seeing lately (in software)](https://lobste.rs/s/awjqvn) |
| lobsters | medium | 2026-08-03 | 51 | 1 | [Don't be a meat proxy](https://lobste.rs/s/hfbqr3) |
| lobsters | medium | 2026-09-04 | 20 | 1 | [Is AI ruining my brain?](https://lobste.rs/s/utloro) |
| lobsters | medium | 2026-05-20 | 23 | 1 | [Twelve Ways to Be Wrong About AI-Assisted Coding](https://lobste.rs/s/3ltdmy) |
| lobsters | medium | 2026-04-26 | 20 | 1 | [LLM-assisted coding is not deterministic. Does it matter?](https://lobste.rs/s/npaxtp) |
| lobsters | medium | 2026-08-24 | 22 | 1 | [AI Coding will Prevent Expertise](https://lobste.rs/s/gzddgr) |
| lobsters | medium | 2026-10-08 | 19 | 1 | [Thinking will become a hobby](https://lobste.rs/s/mosbat) |
| lobsters | medium | 2026-03-30 | 20 | 1 | [2026 has been the most pivotal year in my career… and it's only March](https://lobste.rs/s/6jlrx2) |
| lobsters | medium | 2026-10-07 | 35 | 1 | [Reasons to dislike AI coding](https://lobste.rs/s/9fjar3) |
| lobsters | medium | 2026-04-06 | 17 | 1 | [The machines are fine. I'm worried about us](https://lobste.rs/s/3w0o3y) |
| lobsters | medium | 2026-07-14 | 37 | 1 | [Hating AI in 2026](https://lobste.rs/s/el8ocy) |
| lobsters | medium | 2026-08-23 | 16 | 1 | [Amazon kept shutting down my tablet, so I spent $266 on four AI models to own it](https://lobste.rs/s/fadbev) |
| lobsters | medium | 2026-03-09 | 15 | 1 | [I don't know if my job will still exist in ten years](https://lobste.rs/s/sd1rsy) |
| lobsters | medium | 2026-03-15 | 18 | 1 | [LLM time](https://lobste.rs/s/4jgfcx) |
| lobsters | medium | 2026-03-31 | 18 | 1 | [The Subprime Technical Debt Crisis](https://lobste.rs/s/kp6eap) |
| lobsters | medium | 2026-04-30 | 18 | 1 | [The LLM Is Not a Junior Engineer](https://lobste.rs/s/rhsst0) |
| lobsters | medium | 2026-02-06 | 24 | 1 | [Programming is Dead: The Future of Software Engineering](https://lobste.rs/s/s8awlf) |
| lobsters | medium | 2026-03-20 | 33 | 1 | [I'm OK being left behind, thanks](https://lobste.rs/s/ghtnpx) |
| lobsters | medium | 2026-10-18 | 26 | 0 | [My obituary for programming](https://lobste.rs/s/wtobpt) |
| lobsters | medium | 2026-04-25 | 18 | 0 | [It's OK to use coding assistance tools to revive the projects you never were going to finish](https://lobste.rs/s/dtkjsz) |
| lobsters | medium | 2026-09-03 | 18 | 0 | [The asteroid currently hitting frontend web development](https://lobste.rs/s/rntyvm) |
| lobsters | medium | 2026-05-19 | 12 | 0 | [I am not a Software Engineer](https://lobste.rs/s/2fqahd) |
| lobsters | medium | 2026-04-04 | 21 | 0 | [If you thought the speed of writing code was your problem - you have bigger problems](https://lobste.rs/s/05o8yu) |
| lobsters | medium | 2026-02-17 | 13 | 0 | [Are We Becoming Architects or Butlers to LLMs?](https://lobste.rs/s/zvcupc) |
| lobsters | medium | 2026-05-04 | 14 | 0 | [Losing Skills](https://lobste.rs/s/mfizts) |
| lobsters | medium | 2026-07-24 | 11 | 0 | [Nothing Works and Everyone Is Euphoric](https://lobste.rs/s/syk1hi) |
| lobsters | medium | 2026-09-27 | 14 | 0 | [One month without AI](https://lobste.rs/s/ivbx5f) |
| lobsters | medium | 2026-10-09 | 49 | 0 | [Programming Isn’t Special](https://lobste.rs/s/ily7as) |
| lobsters | medium | 2026-02-24 | 23 | 0 | [Lines of Code Are Back (And It's Worse Than Before)](https://lobste.rs/s/kx2sp3) |
| lobsters | medium | 2026-02-01 | 11 | 0 | [Vibe: Easy VM sandboxes for LLM agents on MacOS](https://lobste.rs/s/6ifznf) |
| lobsters | medium | 2026-05-19 | 45 | 0 | [Type out the code](https://lobste.rs/s/zotppg) |
| lobsters | medium | 2026-04-13 | 14 | 0 | [Programming used to be free](https://lobste.rs/s/o7zxmn) |
| lobsters | medium | 2026-02-24 | 11 | 0 | [How we rebuilt Next.js with AI in one week](https://lobste.rs/s/fjrzzm) |
| lobsters | medium | 2026-09-06 | 15 | 0 | [Maybe We Shouldn't Be Reviewing All This Code](https://lobste.rs/s/lfaddj) |
| lobsters | medium | 2026-08-12 | 27 | 0 | [Why Go is an Ideal Language for AI-Assisted Software Engineering](https://lobste.rs/s/0rtina) |
| lobsters | medium | 2026-09-24 | 11 | 0 | [Clankers Made Me Build a Second Brain](https://lobste.rs/s/xg8zbk) |
| lobsters | medium | 2026-05-19 | 12 | 0 | [Software's Centaur Era](https://lobste.rs/s/prer9l) |
| lobsters | medium | 2026-01-02 | 32 | 0 | [Bespoke software is the future](https://lobste.rs/s/0r8fgx) |
| lobsters | medium | 2026-08-16 | 18 | 0 | [You can just choose how many bugs you want now](https://lobste.rs/s/8izobt) |
| lobsters | medium | 2026-04-07 | 25 | 0 | [Multi-agentic Software Development is a Distributed Systems Problem (AGI can't save you)](https://lobste.rs/s/vjcymq) |
| lobsters | medium | 2026-08-13 | 18 | 0 | [AI is removing the middle class of software engineering](https://lobste.rs/s/xk3ley) |
| lobsters | medium | 2026-01-25 | 21 | 0 | [How to think about Gas Town](https://lobste.rs/s/xmwgtx) |
| lobsters | medium | 2026-01-14 | 58 | 0 | [Why We Don't Use AI](https://lobste.rs/s/jsw3wk) |
| lobsters | medium | 2026-03-12 | 18 | 0 | [Grief and the AI Split](https://lobste.rs/s/wssz9m) |
| lobsters | medium | 2026-01-31 | 24 | 0 | [Automatic programming](https://lobste.rs/s/rboeor) |
| lobsters | medium | 2026-05-06 | 16 | 0 | [Vibe coding and agentic engineering are getting closer than I’d like](https://lobste.rs/s/435bmi) |
| lobsters | medium | 2026-09-18 | 24 | 0 | [There's no point at which turning your brain off will work](https://lobste.rs/s/dd6if1) |
| lobsters | medium | 2026-02-15 | 39 | 0 | [A Single Reason To Not Vibe Code](https://lobste.rs/s/uvdj0c) |
| lobsters | medium | 2026-09-10 | 12 | 0 | [Bad Vibes Coding](https://lobste.rs/s/ifvdvx) |
| lobsters | medium | 2026-07-11 | 18 | 0 | [In defense of not understanding your codebase](https://lobste.rs/s/elhi7o) |
| tildes | high | 2026-06-12 | 32 | 22 | [Any fellow software engineers using paid GitHub copilot?](https://tildes.net/~comp/1un9/any_fellow_software_engineers_using_paid_github_copilot) |
| tildes | high | 2026-04-06 | 46 | 16 | [AI Coding agents are the opposite of what I want](https://tildes.net/~comp/1tkx/ai_coding_agents_are_the_opposite_of_what_i_want) |
| tildes | high | 2026-03-06 | 40 | 13 | [Is it worthwhile to run local LLMs for coding today?](https://tildes.net/~comp/1t2j/is_it_worthwhile_to_run_local_llms_for_coding_today) |
| tildes | high | 2026-05-28 | 15 | 7 | [Actually useful MCPs](https://tildes.net/~comp/1udu/actually_useful_mcps) |
| tildes | high | 2026-06-04 | 30 | 4 | [Have you tried Pewdiepies' self-hosted AI workspace, Odysseus?](https://tildes.net/~tech/1uj1/have_you_tried_pewdiepies_self_hosted_ai_workspace_odysseus) |
| tildes | high | 2026-06-15 | 15 | 1 | [Will you be left behind if you don't use LLMs to code?](https://tildes.net/~comp/1uoy/will_you_be_left_behind_if_you_dont_use_llms_to_code) |
| tildes | medium | 2026-03-19 | 61 | 33 | [That one study that proves developers using AI are deluded](https://tildes.net/~tech/1t9w/that_one_study_that_proves_developers_using_ai_are_deluded) |
| tildes | medium | 2026-08-10 | 135 | 26 | [Why normal people aren’t using AI agents](https://tildes.net/~tech/1viu/why_normal_people_arent_using_ai_agents) |
| tildes | medium | 2026-10-10 | 100 | 16 | [Solo developer rebuilds Adobe Creative Suite in Rust using Claude, releases it free to all](https://tildes.net/~tech/1wew/solo_developer_rebuilds_adobe_creative_suite_in_rust_using_claude_releases_it_free_to_all) |
| tildes | medium | 2026-03-10 | 49 | 16 | [What are people using instead of VS Code?](https://tildes.net/~comp/1t4l/what_are_people_using_instead_of_vs_code) |
| tildes | medium | 2026-02-04 | 71 | 12 | [Any software engineers considering a career switch due to AI?](https://tildes.net/~comp/1sim/any_software_engineers_considering_a_career_switch_due_to_ai) |
| tildes | medium | 2026-09-12 | 98 | 12 | [Where do we go from here? (Regarding AI)](https://tildes.net/~tech/1vzt/where_do_we_go_from_here_regarding_ai) |
| tildes | medium | 2026-07-16 | 29 | 9 | [Claude Code is the ceiling on vibe-coded software](https://tildes.net/~tech/1v5j/claude_code_is_the_ceiling_on_vibe_coded_software) |
| tildes | medium | 2026-09-24 | 24 | 9 | [The plunging price of AI](https://tildes.net/~tech/1w5w/the_plunging_price_of_ai) |
| tildes | medium | 2026-06-10 | 19 | 9 | [AI is bringing my friend out of retirement](https://tildes.net/~comp/1ume/ai_is_bringing_my_friend_out_of_retirement) |
| tildes | medium | 2026-03-08 | 41 | 8 | [I don’t know if my software engineering job will still exist in ten years](https://tildes.net/~comp/1t3p/i_dont_know_if_my_software_engineering_job_will_still_exist_in_ten_years) |
| tildes | medium | 2026-02-18 | 52 | 8 | [The AI disruption has arrived, and it sure is fun](https://tildes.net/~tech/1sr8/the_ai_disruption_has_arrived_and_it_sure_is_fun) |
| tildes | medium | 2026-02-23 | 13 | 7 | [My personal AI assistant project](https://tildes.net/~tech/1su9/my_personal_ai_assistant_project) |
| tildes | medium | 2026-04-03 | 69 | 6 | [What if AI just makes us work harder?](https://tildes.net/~tech/1tjo/what_if_ai_just_makes_us_work_harder) |
| tildes | medium | 2026-01-07 | 33 | 6 | [Feeling weird about my career with respect to AI](https://tildes.net/~life/1s2s/feeling_weird_about_my_career_with_respect_to_ai) |
| tildes | medium | 2026-06-16 | 23 | 6 | [What about having an LLM teach you to code?](https://tildes.net/~comp/1up9/what_about_having_an_llm_teach_you_to_code) |
| tildes | medium | 2026-03-18 | 95 | 6 | [I hope you don't use generative AI - an essay about my experience offering an open-source tool](https://tildes.net/~tech/1t9c/i_hope_you_dont_use_generative_ai_an_essay_about_my_experience_offering_an_open_source_tool) |
| tildes | medium | 2026-08-26 | 25 | 6 | [Software engineers / programmers: how’s it going?](https://tildes.net/~comp/1vs0/software_engineers_programmers_hows_it_going) |
| tildes | medium | 2026-11-03 | 11 | 5 | [Qwen 3.8 27B on my laptop can interpret model weights, too](https://tildes.net/~tech/1wrg/qwen_3_8_27b_on_my_laptop_can_interpret_model_weights_too) |
| tildes | medium | 2026-02-23 | 41 | 5 | [Why doesn’t Anthropic use Claude to make a good Claude desktop app?](https://tildes.net/~tech/1sul/why_doesnt_anthropic_use_claude_to_make_a_good_claude_desktop_app) |
| tildes | medium | 2026-07-17 | 27 | 5 | [I wonder if years from now hand written code will be antique](https://tildes.net/~tech/1v5t/i_wonder_if_years_from_now_hand_written_code_will_be_antique) |
| tildes | medium | 2026-06-30 | 14 | 4 | [AI adoption and IntelliSense](https://tildes.net/~tech/1ux8/ai_adoption_and_intellisense) |
| tildes | medium | 2026-09-09 | 68 | 4 | [Software for humans](https://tildes.net/~tech/1vya/software_for_humans) |
| tildes | medium | 2026-06-11 | 14 | 4 | [Our workplace LLM mass delusion](https://tildes.net/~tech/1un2/our_workplace_llm_mass_delusion) |
| tildes | medium | 2026-04-10 | 8 | 3 | [Prototyping with LLMs](https://tildes.net/~tech/1tnd/prototyping_with_llms) |
| tildes | medium | 2026-04-16 | 39 | 3 | [Vibe coding is just the return of Excel/Access, with more danger](https://tildes.net/~comp/1tqz/vibe_coding_is_just_the_return_of_excel_access_with_more_danger) |
| tildes | medium | 2026-07-05 | 10 | 3 | [Agentic test processes, LLM benchmarks, and other notes on agentic coding](https://tildes.net/~comp/1uzm/agentic_test_processes_llm_benchmarks_and_other_notes_on_agentic_coding) |
| tildes | medium | 2026-10-07 | 39 | 3 | [Given everything we know about AI so far, what do you think it can or cannot be good for?](https://tildes.net/~tech/1wd1/given_everything_we_know_about_ai_so_far_what_do_you_think_it_can_or_cannot_be_good_for) |
| tildes | medium | 2026-08-23 | 15 | 2 | [Amazon kept shutting down my tablet, so I spent $266 on four AI models to own it](https://tildes.net/~tech/1vqh/amazon_kept_shutting_down_my_tablet_so_i_spent_266_on_four_ai_models_to_own_it) |
| tildes | medium | 2026-11-02 | 13 | 1 | [A lukewarm defense of LLMs](https://tildes.net/~tech/1wqy/a_lukewarm_defense_of_llms) |
| tildes | medium | 2026-10-11 | 34 | 1 | [Software developers are not okay](https://tildes.net/~tech/1wf9/software_developers_are_not_okay) |
| tildes | medium | 2026-07-14 | 26 | 1 | [Who cleans up after the vibe-coding party?](https://tildes.net/~tech/1v41/who_cleans_up_after_the_vibe_coding_party) |
| tildes | medium | 2026-07-02 | 17 | 0 | [What AI does to the minds of novice coders](https://tildes.net/~comp/1uy1/what_ai_does_to_the_minds_of_novice_coders) |

</details>
