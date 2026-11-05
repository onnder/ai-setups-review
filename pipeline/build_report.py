"""Render docs/report.md from data/viz2.json. Run after aggregate.py."""
from paths import DATA, DOCS
import json, statistics

V = json.load(open(f"{DATA}/viz2.json"))
N = V["n_authors"]
pc = lambda n, d=N: f"{100 * n / d:.0f}%"
def table(rows, head, fmt):
    return "\n".join([f"| {' | '.join(head)} |", "|" + "---|" * len(head)] + [f"| {' | '.join(map(str, fmt(i, r)))} |" for i, r in enumerate(rows, 1)])
H = {r["name"]: r["n"] for r in V["harness"]}
S = {r["src"]: r for r in V["by_source"]["rows"]}
T = V["by_source"]["tools"]
sh = lambda src, tool: S[src]["share"][T.index(tool)] if tool in T else 0
sp = V["spend"]; med = statistics.median(sp) if sp else 0
cc = V["tool_split"]["Claude Code"]; ccn = sum(x["n"] for x in cc["explicit"])
it = {x["id"]: x for x in V["iface"]}
sv = {x["name"]: x for x in V["surveys"]}
blogs_n = next(s["authors"] for s in V["sources"] if s["id"] == "blogs")

md = f"""# AI Setups Review 2026: what the IT community actually uses for AI work

Infographic: [site/index.html](../site/index.html) · live at <https://aisetups.ringil.cc/>. Decisions and source list: [spec.md](./spec.md). Data: [mentions.csv](../data/mentions.csv) ({V['n_rows']:,} rows, each with a link and a quote).

Window: **Jan 1 – Nov 5, 2026**. Sources: Hacker News (21 approved Ask HN threads, 19 of them with 2026 comments), Lobste.rs and Tildes (213 discussions) and {blogs_n} personal-blog authors (HN + Readwise Reader). Stack Overflow, JetBrains and Pragmatic Engineer surveys are used for calibration only. Reddit is excluded (see methodology).

## TL;DR

- **{N:,} authors** described their own AI setup (HN {S['hn']['n']}, Lobste.rs {S['lobsters']['n']}, Tildes {S['tildes']['n']}, blogs {S['blogs']['n']}).
- **Claude Code** is used by {H['Claude Code']} authors ({pc(H['Claude Code'])}), {H['Claude Code']/H['Codex CLI']:.1f}× more than the runner-up **Codex CLI** ({H['Codex CLI']}). Next: **OpenCode** ({H['OpenCode']}), **Pi** ({H['Pi']}), **GitHub Copilot** ({H['GitHub Copilot']}) and **Cursor** ({H['Cursor']}).
- **Communities differ in the long tail:** HN is the stronghold of Codex and open-source agents, Lobste.rs leans more on chat (Claude app {sh('lobsters','Claude (app/web)'):.0f}% vs {sh('hn','Claude (app/web)'):.0f}% on HN) and Tildes has the most GitHub Copilot users ({sh('tildes','GitHub Copilot'):.0f}%).
- **Interfaces:** {it['terminal']['n']} authors use a terminal/TUI ({it['terminal']['exp']} explicitly), then web ({it['web']['n']}), IDE extension ({it['ide-extension']['n']}), AI editor ({it['ai-editor']['n']}) and desktop app ({it['desktop-app']['n']}). For Claude Code, where the author named the interface (n={ccn}), the terminal is {100*cc['explicit'][0]['n']/ccn:.0f}%, but the desktop app and mobile are no longer niche.
- **Calibration:** compared with the surveys the community is strongly terminal- and open-source-oriented. Pi: {sv['Pi']['community']:.0f}% vs {sv['Pi']['so']}% in Stack Overflow. OpenCode at {sv['OpenCode']['community']:.0f}% matches Stack Overflow ({sv['OpenCode']['so']}%) but is 2× JetBrains ({sv['OpenCode']['jb']}%). Copilot ({sv['GitHub Copilot']['community']:.0f}% vs {sv['GitHub Copilot']['so']}%) and Cursor ({sv['Cursor']['community']:.0f}% vs {sv['Cursor']['so']}%) are far below.
- **Money:** {V['providers'][0]['n']} authors have a paid Anthropic plan, {V['providers'][1]['n']} a paid OpenAI plan. Median stated monthly spend is **${med:.0f}** (n={len(sp)}).

## 1. Harnesses and coding tools

{table(V['harness'], ['#', 'Harness', 'Authors', '%'], lambda i, r: (i, r['name'] + (f" ({r['tag']})" if r.get('tag') else ''), r['n'], pc(r['n'])))}

Claude Code and Codex CLI together: {V['venn']['both']} authors.

## 2. Communities side by side (share of authors within each source, %)

| Tool | {' | '.join(f"{r['label']} (n={r['n']})" for r in V['by_source']['rows'])} |
|---|{'---|' * len(V['by_source']['rows'])}
""" + "\n".join(f"| {t} | " + " | ".join(f"{r['share'][i]:.0f}" for r in V['by_source']['rows']) + " |" for i, t in enumerate(T)) + f"""

Blogs (n={S['blogs']['n']}) = authors of articles about their own setup. They are mostly enthusiasts, so their shares are higher across tools.

## 3. Interfaces

Explicit = the author named the interface. Inferred = derived from the tool's default interface (e.g. "Codex CLI" → terminal).

{table(V['iface'], ['Interface type', 'Authors total', 'of which explicit'], lambda i, r: (r['name'], r['n'], r['exp']))}

**Claude Code by interface** (explicit only, n={ccn} of {cc['total']} users):

{table(cc['explicit'], ['Interface', 'Authors'], lambda i, r: (r['name'], r['n']))}

**GitHub Copilot by interface** (explicit):

{table(V['tool_split']['GitHub Copilot']['explicit'], ['Interface', 'Authors'], lambda i, r: (r['name'], r['n']))}

**Host** (what the tool runs in, explicit): {', '.join(f"{h['name']} {h['n']}" for h in V['hosts'])}.

### Model × what it is used through (explicit pairing)

| Model | {' | '.join(V['via']['vias'])} | total |
|---|{'---|' * (len(V['via']['vias']) + 1)}
""" + "\n".join(f"| {g} | " + " | ".join(str(v or '·') for v in V['via']['m'][i]) + f" | {V['via']['tot'][i]} |" for i, g in enumerate(V['via']['models'])) + f"""

## 4. 2026 trend by quarter (share of active authors)

| Tool | {' | '.join(f"{q} (n={n})" for q, n in zip(V['quarters'], V['q_active']))} |
|---|{'---|' * len(V['quarters'])}
""" + "\n".join(f"| {t['name']} | " + " | ".join(f"{100*v/max(1,n):.0f}%" for v, n in zip(t['n'], V['q_active'])) + " |" for t in V['trend']) + f"""

Q4 runs to Nov 5 and consists mostly of one large HN thread from November.

## 5. Models

{table(V['model_grp'], ['Group', 'Explicit', 'Implicit (from harness)', 'Total', 'Open weights'], lambda i, r: (r['name'], r['exp'], r['imp'], r['exp'] + r['imp'], 'yes' if r['open'] else ''))}

Families (explicit): {', '.join(f"{r['name']} {r['n']}" + (f" ({', '.join(r['v'])})" if r['v'] else '') for r in V['model_fam'])}.

## 6. Subscriptions and spend

{table(V['sub'], ['Plan / payment', 'Authors'], lambda i, r: (r['name'], r['n']))}

By provider: """ + " · ".join(f"{p['name']} {p['n']}" + (f" ({', '.join(f'{k} {v}' for k, v in p['detail'].items())})" if p['detail'] else '') for p in V['providers']) + f"""

Monthly spend (n={len(sp)}): median **${med:.0f}**, mean ${statistics.mean(sp) if sp else 0:.0f}. Bands: <$20 {V['spend_buckets'][0]} · $20–100 {V['spend_buckets'][1]} · $100–250 {V['spend_buckets'][2]} · >$250 {V['spend_buckets'][3]}.

## 7. Churn (most common moves with a known destination)

{table([c for c in V['churn'] if c['to'] != '?'][:15], ['From', 'To', 'Authors'], lambda i, r: (r['from'], r['to'], r['n']))}

In total {V['n_left']} author × tool cases with status "stopped using".

## 8. Local models

{V['local_any']} authors mention running models locally. Runtimes: {', '.join(f"{r['name']} {r['n']}" for r in V['local'])}. Hardware: {', '.join(f"{r['name']} {r['n']}" for r in V['hw'])}.

## 9. Calibration against 2026 surveys

Community = share of the {V['n_harness_authors']} authors who named at least one coding harness.

{table(V['surveys'], ['Tool', 'Community', 'Stack Overflow 2026', 'JetBrains 2026', 'Pragmatic Eng. 2026'], lambda i, r: (r['name'], f"{r['community']:.0f}%", f"{r['so']}%", f"{r['jb']}%" if r['jb'] is not None else '–', f"{r['pe']}%" if r['pe'] is not None else '–'))}

Sources: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) (n≈12,260, "used in the past year") · [JetBrains Developer Ecosystem 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) (n>15,000, May–Jul, "at work") · [Pragmatic Engineer AI Tooling 2026](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) (n=507 regular agent users). Question wording differs, so compare rank and direction, not absolute percentages.

## Methodology and limitations

- **Corpus:** HN: 21 Ask HN threads. Lobste.rs and Tildes: 213 discussions about AI in practice from 2026 (Lobste.rs by tag, Tildes by search). 2026 comments only.
- **Processing:** every comment was read by an LLM without a pre-filter, extracting tool, status (uses/left), interface (explicit/inferred), host and model → harness pairing. 99.6% of quotes were verified verbatim against the source.
- **Counting:** unique author × tool within a source; the latest status wins. Only first-person current use counts.
- **Biases:** discussion communities are not representative. The HN thread about local models (June) inflates Qwen, DeepSeek, Pi and OpenCode. Lobste.rs and Tildes yield fewer setups per comment because they are discussions under articles, not Ask threads.
- **Reddit excluded:** the [Reddit Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy) requires approval for API access and forbids research outside the Reddit for Researchers program.
- **Blogs:** 11 articles from the HN front page + Readwise Reader (later/starred/archive library and 100 ITech feeds including Swamp Club; 1,916 candidates → screening → 321 full texts). Only the article author counts. Swamp is a product of the Swamp Club community, so it is excluded from the cross-source comparison.
"""
open(f"{DOCS}/report.md", "w").write(md)
print("report.md", len(md))
