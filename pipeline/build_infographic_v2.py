"""Build infographic v2 (calendar 2026, multi-source, interfaces) from v2/viz2.json + mentions.csv. Run after aggregate_v2.py."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, csv, os, re, glob
from collections import Counter, defaultdict
from normalize import BLOG_AUTHOR

V = json.load(open(f"{DATA}/viz2.json"))
rows = list(csv.DictReader(open(f"{DATA}/mentions.csv")))

# comments read + threads per source
read, threads = Counter(), defaultdict(set)
for f in glob.glob(f"{DATA}/classified/input/*.jsonl"):
    for l in open(f):
        d = json.loads(l); read[d["source"]] += 1; threads[d["source"]].add(str(d["thread"]))
titles = {}
for l in open(f"{DATA}/hn/ask_titles.tsv"):
    p = l.rstrip("\n").split("\t"); titles[("hn", p[0])] = (p[3], f"https://news.ycombinator.com/item?id={p[0]}")
for f in glob.glob(f"{DATA}/community/raw/*.json"):
    d = json.load(open(f))
    u = f"https://lobste.rs/s/{d['id']}" if d["source"] == "lobsters" else d["meta"]["url"]
    titles[(d["source"], d["id"])] = (d["meta"]["title"], u)
ta = defaultdict(set)
for r in rows:
    if r["status"] == "uses" and r["source"] != "blogs": ta[(r["source"], r["thread"])].add(r["author"])
top_threads = {}
for s in ("hn", "lobsters", "tildes"):
    xs = sorted(((k, len(a)) for k, a in ta.items() if k[0] == s), key=lambda x: (-x[1], x[0]))[:6]
    top_threads[s] = [{"t": titles.get(k, (k[1], ""))[0], "u": titles.get(k, ("", ""))[1], "a": n} for k, n in xs]
srcu = defaultdict(lambda: defaultdict(set))
for r in rows:
    if r["status"] == "uses" and r["category"] in ("harness", "app"): srcu[r["source"]][r["tool"]].add(r["author"])
V["src_summary"] = [{"id": s["id"], "label": s["label"], "authors": s["authors"], "read": read.get(s["id"], 11 if s["id"] == "blogs" else 0),
                     "threads": len(threads.get(s["id"], ())) if s["id"] != "blogs" else 11,
                     "top": [(t, len(a)) for t, a in sorted(srcu[s["id"]].items(), key=lambda x: (-len(x[1]), x[0]))[:3]], "tt": top_threads.get(s["id"], [])}
                    for s in V["sources"]]
V["n_read"] = sum(x["read"] for x in V["src_summary"] if x["id"] != "blogs")

# blog article cards (HN articles + Readwise blogs when present)
arts = []
for f in [f"{DATA}/hn/v1/classified/articles_summary.md", f"{DATA}/readwise/blogs_summary.md"]:
    if not os.path.exists(f): continue
    for l in open(f):
        m = re.match(r"- \[(.+?)\]\((.+?)\) — (.+?), (\d{4}-\d\d-\d\d): (.+)", l.strip())
        if m and m[4].startswith("2026"): arts.append({"title": m[1], "url": m[2], "author": BLOG_AUTHOR.get(m[3], m[3]), "date": m[4], "sum": m[5]})
chips = defaultdict(list); spend = {}
for r in rows:
    if r["source"] != "blogs" or r["status"] != "uses": continue
    if r["spend_usd_mo"]: spend[r["author"]] = max(spend.get(r["author"], 0), float(r["spend_usd_mo"]))
    mv = r["model_version"]
    fam = r["tool"].replace(" (unspecified)", "").replace("GPT-5 / GPT (OpenAI)", "GPT")
    lab = (mv if re.search(r"[A-Za-z]{2}", mv) else f"{fam} {mv}") if r["category"] == "model" and mv else r["tool"]
    if r["category"] in ("harness", "model", "subscription", "app") and lab not in [c[0] for c in chips[r["author"]]]: chips[r["author"]].append((lab, r["category"]))
seen = set()
for a in arts: a["chips"] = chips.get(a["author"], [])[:7]; a["spend"] = spend.get(a["author"])
uniq = [a for a in sorted(arts, key=lambda a: a["date"], reverse=True) if a["chips"] and not (a["url"] in seen or seen.add(a["url"]))]
by_author = {}
for a in uniq: by_author.setdefault(a["author"].lower(), a)
V["n_blog_articles"], V["n_blog_authors"] = len(uniq), len(by_author)
V["articles"] = sorted(by_author.values(), key=lambda a: (-len(a["chips"]), a["date"]))[:24]

tpl = open(f"{PIPE}/infographic_v2_tpl.html").read()
html = tpl.replace("__DATA__", json.dumps(V, ensure_ascii=False).replace("</", "<\\/"))
open(f"{SITE}/index.html", "w").write(html)
print("ok", len(html), "read", V["n_read"], {s["id"]: (s["threads"], s["read"], s["authors"]) for s in V["src_summary"]}, "articles", len(V["articles"]))
