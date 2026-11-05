"""Build infographic.html from viz.json + agg.json + mentions.csv + articles. Run after aggregate.py."""
import json, csv, os, re, html
from collections import Counter, defaultdict

W = os.path.dirname(os.path.abspath(__file__))
OUT = "../../data/v1-output"  # historical: originally an absolute local output path
viz = json.load(open(f"{W}/viz.json"))
agg = json.load(open(f"{W}/agg.json"))
rows = list(csv.DictReader(open(f"{OUT}/mentions.csv")))

final = {}
for r in sorted(rows, key=lambda r: r["date"]): final[(r["author"], r["tool"])] = r
def users(pred): return {a for (a, t), r in final.items() if r["status"] == "uses" and pred(t, r)}
sub = lambda t, r: r["category"] == "subscription"
cc, cx = users(lambda t, r: t == "Claude Code"), users(lambda t, r: t == "Codex CLI")
allu = users(lambda t, r: True)
catc = defaultdict(Counter)
for r in rows: catc[r["tool"]][r["category"]] += 1
cat = {t: c.most_common(1)[0][0] for t, c in catc.items()}

viz["venn"] = {"both": len(cc & cx), "cc": len(cc - cx), "cx": len(cx - cc), "none": len(allu - cc - cx)}
viz["providers"] = [
    {"name": "Anthropic", "n": len(users(lambda t, r: sub(t, r) and t.startswith("Claude") and "Free" not in t)), "detail": viz["claude_tiers"]},
    {"name": "OpenAI", "n": len(users(lambda t, r: sub(t, r) and t.startswith("ChatGPT"))),
     "detail": {"Plus": len(users(lambda t, r: t == "ChatGPT Plus")), "Pro": len(users(lambda t, r: t == "ChatGPT Pro")), "Business/Ent.": len(users(lambda t, r: t == "ChatGPT Business/Enterprise"))}},
    {"name": "API / OpenRouter", "n": len(users(lambda t, r: sub(t, r) and ("pay-as-you-go" in t or "OpenRouter" in t))), "detail": {}},
    {"name": "Platí zamestnávateľ", "n": len(users(lambda t, r: sub(t, r) and ("mployer" in t or "Team/Enterprise" in t or "Business" in t))), "detail": {}},
]
viz["local_any"] = len(users(lambda t, r: r["category"] in ("local_runtime", "hardware")))
viz["n_rows"] = len(rows)
viz["n_left"] = sum(1 for r in final.values() if r["status"] == "left")
viz["churn"] = [c for c in viz["churn"] if cat.get(c["from"]) in ("harness", "app")]

# threads
titles = {}
for l in open(f"{W}/ask_titles.tsv"):
    p = l.rstrip("\n").split("\t"); titles[p[0]] = {"c": int(p[1]), "d": p[2], "t": p[3]}
A = "50366117 47388646 48542100 46255285 48771515 48413629 48492118 46292682 46993479 49934037 50337431 49290713 47559293 48587808 47616250 50016644 48166147 49449290 49586386 49848426 46731068".split()
def cnt(n): return sum(1 + cnt(c) if c.get("author") and c.get("text") else cnt(c) for c in n.get("children", []))
viz["n_comments"] = sum(cnt(t) + bool(t.get("text")) for t in (json.load(open(f"{W}/raw/{i}.json")) for i in A))  # incl. Ask HN post bodies, as in flatten.py
viz["threads"] = [{"id": i, **titles[i], "a": agg["threads"].get(i, {}).get("authors", 0), "top": agg["threads"].get(i, {}).get("top", [])} for i in A]

# articles
arts = []
for l in open(f"{W}/out/articles_summary.md"):
    m = re.match(r"- \[(.+?)\]\((.+?)\) — (.+?), (\d{4}-\d\d-\d\d): (.+)", l.strip())
    if m: arts.append({"title": m[1], "url": m[2], "author": m[3], "date": m[4], "sum": m[5]})
chips = defaultdict(list); spend = {}
for l in open(f"{W}/out/articles.jsonl"):
    r = json.loads(l)
    if r["status"] != "uses": continue
    if r.get("spend_usd_mo"): spend[r["author"]] = max(spend.get(r["author"], 0), r["spend_usd_mo"])
    lab = r["model_version"] if r["category"] == "model" and r.get("model_version") else r["tool"]
    if r["category"] in ("harness", "model", "subscription", "app") and lab not in [c[0] for c in chips[r["author"]]]:
        chips[r["author"]].append((lab, r["category"]))
for a in arts:
    a["chips"] = chips.get(a["author"], [])[:7]; a["spend"] = spend.get(a["author"])
viz["articles"] = sorted(arts, key=lambda a: a["date"])

tpl = open(f"{W}/infographic_tpl.html").read()
out = tpl.replace("__DATA__", json.dumps(viz, ensure_ascii=False).replace("</", "<\\/"))
open(f"{OUT}/infographic.html", "w").write(out)
print("ok", len(out), viz["venn"], [p["n"] for p in viz["providers"]], viz["local_any"], len(viz["churn"]), len(arts))
