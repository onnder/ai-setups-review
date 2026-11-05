"""Render report.md (v2) from v2/viz2.json. Run after aggregate_v2.py (and build_infographic_v2.py for src_summary)."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, os, statistics
V = json.load(open(f"{DATA}/viz2.json"))
N = V["n_authors"]
pc = lambda n, d=N: f"{100 * n / d:.0f} %"
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
fmt1 = lambda v: f"{v}".replace('.', ',')
num = lambda n: f"{n:,}".replace(',', '\u00a0')

md = f"""# AI Setup Census 2026: čo IT komunita reálne používa

Status: ready-for-human

Infografika: [site/index.html](../site/index.html). Rozhodnutia a zoznam zdrojov: [spec.md](./spec.md). Dáta: [mentions.csv](../data/mentions.csv) ({num(V['n_rows'])} riadkov, každý s odkazom a citáciou).

Okno: **1. 1. – 5. 11. 2026**. Zdroje: Hacker News (21 schválených vlákien Ask HN, z toho 19 s komentármi z roku 2026), Lobste.rs a Tildes (213 diskusií) a {next(s['authors'] for s in V['sources'] if s['id']=='blogs')} autorov osobných blogov (HN + Readwise Reader). Ankety SO, JetBrains a Pragmatic Engineer slúžia iba na kalibráciu. Reddit je vynechaný (pozri metodiku).

## TL;DR

- **{num(N)} autorov** opísalo vlastný AI setup (HN {S['hn']['n']}, Lobste.rs {S['lobsters']['n']}, Tildes {S['tildes']['n']}, blogy {S['blogs']['n']}).
- **Claude Code** používa {H['Claude Code']} autorov ({pc(H['Claude Code'])}), {fmt1(round(H['Claude Code']/H['Codex CLI'],1))}× viac ako druhý **Codex CLI** ({H['Codex CLI']}). Nasledujú **OpenCode** ({H['OpenCode']}), **Pi** ({H['Pi']}), **GitHub Copilot** ({H['GitHub Copilot']}) a **Cursor** ({H['Cursor']}).
- **Komunity sa líšia v chvoste:** HN je baštou Codexu a open-source agentov, Lobste.rs viac používa chat (Claude app {sh('lobsters','Claude (app/web)'):.0f} % oproti {sh('hn','Claude (app/web)'):.0f} % na HN) a Tildes má najviac používateľov Copilotu ({sh('tildes','GitHub Copilot'):.0f} %).
- **Rozhrania:** terminál/TUI uvádza {it['terminal']['n']} autorov ({it['terminal']['exp']} výslovne). Ďalej web ({it['web']['n']}), rozšírenie v IDE ({it['ide-extension']['n']}), AI editor ({it['ai-editor']['n']}) a desktop app ({it['desktop-app']['n']}). Pri Claude Code, kde autor rozhranie uviedol (n={ccn}), je terminál {100*cc['explicit'][0]['n']/ccn:.0f} %, no desktop app a mobil už nie sú okrajové.
- **Kalibrácia:** oproti anketám je komunita výrazne terminálová a open-source. Pi má {sv['Pi']['community']:.0f} % oproti {fmt1(sv['Pi']['so'])} % v SO. OpenCode je so {sv['OpenCode']['community']:.0f} % na úrovni SO ({fmt1(sv['OpenCode']['so'])} %), ale 2× nad JetBrains ({sv['OpenCode']['jb']} %). Copilot ({sv['GitHub Copilot']['community']:.0f} % oproti {fmt1(sv['GitHub Copilot']['so'])} %) a Cursor ({sv['Cursor']['community']:.0f} % oproti {fmt1(sv['Cursor']['so'])} %) sú hlboko pod priemerom.
- **Peniaze:** platený plán Anthropicu má {V['providers'][0]['n']} autorov, OpenAI {V['providers'][1]['n']}. Medián uvedenej mesačnej útraty je **${med:.0f}** (n={len(sp)}).

## 1. Harnessy a coding nástroje

{table(V['harness'], ['#', 'Harness', 'Autori', '%'], lambda i, r: (i, r['name'], r['n'], pc(r['n'])))}

Claude Code + Codex CLI naraz: {V['venn']['both']} autorov.

## 2. Komunity vedľa seba (podiel autorov v zdroji, %)

| Tool | {' | '.join(f"{r['label']} (n={r['n']})" for r in V['by_source']['rows'])} |
|---|{'---|' * len(V['by_source']['rows'])}
""" + "\n".join(f"| {t} | " + " | ".join(f"{r['share'][i]:.0f}" for r in V['by_source']['rows']) + " |" for i, t in enumerate(T)) + f"""

Blogy (n={S['blogs']['n']}) = autori článkov o vlastnom setupe. Píšu najmä nadšenci, preto majú vyššie podiely naprieč tools.

## 3. Rozhrania

Výslovne = autor rozhranie uviedol. Doplnené = odvodené z predvoleného rozhrania nástroja (napríklad „Codex CLI“ → terminál).

{table(V['iface'], ['Typ rozhrania', 'Autori spolu', 'z toho výslovne'], lambda i, r: (r['name'], r['n'], r['exp']))}

**Claude Code podľa rozhrania** (iba výslovne uvedené, n={ccn} z {cc['total']} používateľov):

{table(cc['explicit'], ['Rozhranie', 'Autori'], lambda i, r: (r['name'], r['n']))}

**GitHub Copilot podľa rozhrania** (výslovne):

{table(V['tool_split']['GitHub Copilot']['explicit'], ['Rozhranie', 'Autori'], lambda i, r: (r['name'], r['n']))}

**Hostiteľ** (v čom nástroj beží, výslovne): {', '.join(f"{h['name']} {h['n']}" for h in V['hosts'])}.

### Model × cez čo ho autor používa (výslovné párovanie)

| Model | {' | '.join(V['via']['vias'])} | spolu |
|---|{'---|' * (len(V['via']['vias']) + 1)}
""" + "\n".join(f"| {g} | " + " | ".join(str(v or '·') for v in V['via']['m'][i]) + f" | {V['via']['tot'][i]} |" for i, g in enumerate(V['via']['models'])) + f"""

## 4. Trend 2026 po kvartáloch (podiel aktívnych autorov)

| Tool | {' | '.join(f"{q} (n={n})" for q, n in zip(V['quarters'], V['q_active']))} |
|---|{'---|' * len(V['quarters'])}
""" + "\n".join(f"| {t['name']} | " + " | ".join(f"{100*v/max(1,n):.0f} %" for v, n in zip(t['n'], V['q_active'])) + " |" for t in V['trend']) + f"""

Q4 = do 5. 11. a tvorí ho najmä jedno veľké HN vlákno z novembra.

## 5. Modely

{table(V['model_grp'], ['Skupina', 'Výslovne', 'Implicitne (z harnessu)', 'Spolu', 'Otvorené váhy'], lambda i, r: (r['name'], r['exp'], r['imp'], r['exp'] + r['imp'], 'áno' if r['open'] else ''))}

Rodiny (výslovne): {', '.join(f"{r['name']} {r['n']}" + (f" ({', '.join(r['v'])})" if r['v'] else '') for r in V['model_fam'])}.

## 6. Predplatné a útrata

{table(V['sub'], ['Plán / platba', 'Autori'], lambda i, r: (r['name'], r['n']))}

Podľa poskytovateľa: """ + " · ".join(f"{p['name']} {p['n']}" + (f" ({', '.join(f'{k} {v}' for k, v in p['detail'].items())})" if p['detail'] else '') for p in V['providers']) + f"""

Mesačná útrata (n={len(sp)}): medián **${med:.0f}**, priemer ${statistics.mean(sp) if sp else 0:.0f}. Pásma: <$20 {V['spend_buckets'][0]} · $20–100 {V['spend_buckets'][1]} · $100–250 {V['spend_buckets'][2]} · >$250 {V['spend_buckets'][3]}.

## 7. Odchody (najčastejšie toky so známym cieľom)

{table([c for c in V['churn'] if c['to'] != '?'][:15], ['Z', 'Na', 'Autori'], lambda i, r: (r['from'], r['to'], r['n']))}

Spolu {V['n_left']} prípadov typu autor × tool so stavom „prestal používať“.

## 8. Lokálne modely

{V['local_any']} autorov spomína lokálnu inferenciu. Runtime: {', '.join(f"{r['name']} {r['n']}" for r in V['local'])}. Hardvér: {', '.join(f"{r['name']} {r['n']}" for r in V['hw'])}.

## 9. Kalibrácia oproti anketám 2026

Komunita = podiel z {V['n_harness_authors']} autorov, ktorí uviedli aspoň jeden coding harness.

{table(V['surveys'], ['Tool', 'Komunita', 'Stack Overflow 2026', 'JetBrains 2026', 'Pragmatic Eng. 2026'], lambda i, r: (r['name'], f"{r['community']:.0f} %", f"{fmt1(r['so'])} %", f"{r['jb']} %" if r['jb'] is not None else '–', f"{r['pe']} %" if r['pe'] is not None else '–'))}

Zdroje: [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/ai/data/ai-code-agent) (n≈12 260, „used in the past year“) · [JetBrains Developer Ecosystem 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) (n>15 000, máj–júl, „at work“) · [Pragmatic Engineer AI Tooling 2026](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026) (n=507 pravidelných používateľov agentov). Formulácie otázok sa líšia, porovnávaj poradie a smer.

## Metodika a limity

- **Korpus:** HN 21 vlákien Ask HN. Lobste.rs a Tildes: 213 diskusií o AI v praxi z roku 2026 (Lobste.rs podľa tagov, Tildes podľa vyhľadávania). Iba komentáre z roku 2026.
- **Spracovanie:** každý komentár prečítal LLM bez predfiltra a určil tool, stav (uses/left), rozhranie (výslovne/doplnené), hostiteľa a párovanie model → harness. 99,6 % citácií je overených doslovne proti zdroju.
- **Počítanie:** unikátny autor × tool v rámci zdroja, posledný stav vyhráva. Ráta sa iba vlastné aktuálne používanie.
- **Skreslenia:** diskusné komunity nie sú reprezentatívne. HN vlákno o lokálnych modeloch (jún) nadhodnocuje Qwen, DeepSeek, Pi a OpenCode. Lobste.rs a Tildes dodali menej setupov na komentár, pretože ide o diskusie pod článkami, nie Ask vlákna.
- **Reddit vynechaný:** [Reddit Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy) vyžaduje schválenie prístupu k API a výskum mimo programu Reddit for Researchers zakazuje.
- **Blogy:** 11 článkov z HN titulky + Readwise Reader (knižnica later/starred/archive a 100 ITech feedov vrátane Swamp Club, 1 916 kandidátov → triedenie → 321 plných textov). Ráta sa iba autor. Swamp je produkt komunity Swamp Club, preto je v porovnaní zdrojov vynechaný.
"""
open(f"{DOCS}/report.md", "w").write(md)
print("report.md", len(md))
