"""Render report.md from report_tpl.md + agg.json. Run after aggregate.py."""
import json, re, os
W = os.path.dirname(os.path.abspath(__file__))
OUT = "../../data/v1-output"  # historical: originally an absolute local output path
d = json.load(open(f"{W}/agg.json"))
TITLES = {}
for l in open(f"{W}/ask_titles.tsv"):
    p = l.rstrip("\n").split("\t"); TITLES[p[0]] = (p[1], p[2], p[3])
A = "50366117 47388646 48542100 46255285 48771515 48413629 48492118 46292682 46993479 49934037 50337431 49290713 47559293 48587808 47616250 50016644 48166147 49449290 49586386 49848426 46731068".split()
lines = []
for i in A:
    c, dt, t = TITLES[i]; s = d["threads"].get(i, {"authors": 0, "top": []})
    top = ", ".join(f"{n} ({k})" for n, k in s["top"]) or "—"
    lines.append(f"- [{t}](https://news.ycombinator.com/item?id={i}) ({c} kom., {dt}): {s['authors']} autorov uviedlo svoj setup. Top: {top}.")
rep = {k: d[k] for k in ("harness", "sens", "app", "model_grp", "model_fam", "sub", "spend", "local", "hw", "trend", "churn", "tail")}
rep.update({"threads": "\n".join(lines), "articles": open(f"{W}/out/articles_summary.md").read().strip(),
            "tail_n": str(d["tail"].count(";") + 1), "tail_h": str(d["tail_counts"]["harness"]), "max": str(d["claude_tiers"]["Claude Max (any)"])})
s = open(f"{W}/report_tpl.md").read()
for k, v in rep.items(): s = s.replace("{{" + k + "}}", v)
assert "{{" not in s, re.findall(r"\{\{\w+\}\}", s)
open(f"{OUT}/report.md", "w").write(s)
print("report.md", len(s))
