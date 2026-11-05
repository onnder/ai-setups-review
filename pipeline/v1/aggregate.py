import json, glob, csv, os, re, statistics
from collections import defaultdict, Counter

W = os.path.dirname(os.path.abspath(__file__))
OUT = "../../data/v1-output"  # historical: originally an absolute local output path

from normalize import ALIAS, IMPLIED, model_group, norm, NORM_RE, hw_class, RUNTIMES
def quarter(d):
    y, m = int(d[:4]), int(d[5:7])
    return f"{y}-Q{(m - 1) // 3 + 1}"

rows = []
for f in sorted(glob.glob(f"{W}/out/*.jsonl")):
    for ln in open(f):
        ln = ln.strip()
        if not ln: continue
        r = json.loads(ln)
        if r.get("status") not in ("uses", "left"): continue
        r["tool"] = norm(r["tool"])
        if r.get("category") == "local_runtime" and r["tool"] not in RUNTIMES and hw_class(r["tool"]):
            r["model_version"], r["tool"], r["category"] = r["tool"], hw_class(r["tool"]), "hardware"
        if r.get("left_to"): r["left_to"] = norm(r["left_to"])
        r["source"] = "article" if os.path.basename(f).startswith("articles") else "ask_hn"
        r["quarter"] = quarter(r["date"])
        rows.append(r)

# ---- mentions.csv
cols = ["author", "date", "quarter", "source", "thread", "comment_id", "link", "tool", "category", "status", "left_to", "model_version", "spend_usd_mo", "quote"]
with open(f"{OUT}/mentions.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for r in sorted(rows, key=lambda r: (r["date"], r["author"])):
        r["link"] = f"https://news.ycombinator.com/item?id={r['comment_id']}"
        w.writerow(r)

# ---- final status per author x tool (latest mention wins)
final = {}
for r in sorted(rows, key=lambda r: r["date"]):
    if r["tool"] == "TOTAL SPEND": continue
    final[(r["author"], r["tool"])] = r
users = defaultdict(set); cat = {}
for (a, t), r in final.items():
    if r["status"] == "uses": users[t].add(a)
    cat.setdefault(t, Counter())[r["category"]] += 1
cat = {t: c.most_common(1)[0][0] for t, c in cat.items()}
all_users = {a for (a, t), r in final.items() if r["status"] == "uses"}

def table(cats, title, extra=None):
    items = sorted(((t, len(u)) for t, u in users.items() if cat.get(t) in cats), key=lambda x: (-x[1], x[0]))
    main = [x for x in items if x[1] >= 3]; tail = [x for x in items if x[1] < 3]
    s = [f"| # | {title} | Autori | % z {len(all_users)} |", "|---|---|---|---|"]
    s += [f"| {i} | {t} | {n} | {100 * n / len(all_users):.0f} % |" for i, (t, n) in enumerate(main, 1)]
    return "\n".join(s), tail

out = {}
out["n_authors"] = len(all_users)
out["n_rows"] = len(rows)
out["harness"], tail_h = table({"harness"}, "Harness / coding tool")
out["app"], tail_a = table({"app"}, "App / služba")
out["local"], tail_l = table({"local_runtime"}, "Lokálny runtime")
out["hw"], tail_hw = table({"hardware"}, "Hardvér (trieda)")
out["sub"], tail_s = table({"subscription"}, "Predplatné / platba")

# ---- models: detailed families (explicit) + groups explicit vs implied
def vnorm(v):
    v = re.sub(r"(?i)\b(claude|anthropic|opus|sonnet|haiku|fable|gemma|kimi|glm|qwen|deepseek|openai|gpt|gemini|mistral|devstral|ministral|grok)\b[- ]*", "", str(v)).strip(" -")
    return v or "?"
fam_users = defaultdict(set); fam_versions = defaultdict(Counter)
for (a, t), r in final.items():
    if r["category"] == "model" and r["status"] == "uses":
        fam_users[t].add(a)
        if r.get("model_version") and vnorm(r["model_version"]) != "?": fam_versions[t][vnorm(r["model_version"])] += 1
items = sorted(fam_users.items(), key=lambda x: (-len(x[1]), x[0]))
s = ["| # | Rodina modelu | Autori (explicitne) | Najčastejšie verzie |", "|---|---|---|---|"]
tail_m = []
i = 0
for t, u in items:
    if len(u) < 3: tail_m.append((t, len(u))); continue
    i += 1
    v = ", ".join(f"{k} ({n})" for k, n in fam_versions[t].most_common(3))
    s.append(f"| {i} | {t} | {len(u)} | {v} |")
out["model_fam"] = "\n".join(s)
grp_exp = defaultdict(set); grp_imp = defaultdict(set)
for t, u in fam_users.items(): grp_exp[model_group(t)] |= u
for t, g in IMPLIED.items():
    for a in users.get(t, ()):
        if a not in grp_exp[g]: grp_imp[g].add(a)
gs = sorted(set(grp_exp) | set(grp_imp), key=lambda g: -(len(grp_exp[g]) + len(grp_imp[g])))
s = ["| # | Skupina | Explicitne | Implicitne (z harnessu) | Spolu |", "|---|---|---|---|---|"]
s += [f"| {i} | {g} | {len(grp_exp[g])} | {len(grp_imp[g])} | {len(grp_exp[g]) + len(grp_imp[g])} |" for i, g in enumerate(gs, 1) if len(grp_exp[g]) + len(grp_imp[g]) >= 3]
out["model_grp"] = "\n".join(s)

# ---- quarterly trend: top10 harness+app, share of authors active that quarter
qa = defaultdict(set); qt = defaultdict(lambda: defaultdict(set))
for r in rows:
    if r["status"] == "uses" and r["tool"] != "TOTAL SPEND":
        qa[r["quarter"]].add(r["author"]); qt[r["tool"]][r["quarter"]].add(r["author"])
qs = sorted(qa)
top10 = [t for t, _ in sorted(((t, len(u)) for t, u in users.items() if cat.get(t) in ("harness", "app")), key=lambda x: -x[1])[:10]]
s = ["| Tool | " + " | ".join(qs) + " |", "|---|" + "---|" * len(qs), "| *aktívni autori* | " + " | ".join(str(len(qa[q])) for q in qs) + " |"]
for t in top10:
    s.append(f"| {t} | " + " | ".join(f"{len(qt[t][q])} ({100 * len(qt[t][q]) / max(1, len(qa[q])):.0f} %)" for q in qs) + " |")
out["trend"] = "\n".join(s)

# ---- churn
ch = Counter(); left_tot = Counter()
for (a, t), r in final.items():
    if r["status"] == "left":
        left_tot[t] += 1
        ch[(t, r.get("left_to") or "?")] += 1
s = ["| Odchod z | Počet autorov | Kam (top) |", "|---|---|---|"]
for t, n in left_tot.most_common(15):
    if n < 2: break
    dest = ", ".join(f"{d} ({k})" for (src, d), k in ch.most_common() if src == t)[:200]
    s.append(f"| {t} | {n} | {dest} |")
out["churn"] = "\n".join(s)

# ---- spend
spend = {}
for r in rows:
    v = r.get("spend_usd_mo")
    if isinstance(v, (int, float)) and v >= 0: spend[r["author"]] = max(spend.get(r["author"], 0), v)
vals = sorted(spend.values())
b = Counter("<$20" if v < 20 else "$20–100" if v < 100 else "$100–250" if v <= 250 else ">$250" for v in vals)
out["spend"] = (f"Autori s uvedenou sumou: **{len(vals)}**, medián **${statistics.median(vals):.0f}/mes**, priemer ${statistics.mean(vals):.0f}/mes.\n\n"
                "| Pásmo | Autori |\n|---|---|\n" + "\n".join(f"| {k} | {b[k]} |" for k in ["<$20", "$20–100", "$100–250", ">$250"])) if vals else "Žiadne sumy."

out["tail"] = "; ".join(f"{t} ({n})" for t, n in sorted(tail_h + tail_a + tail_l + tail_hw + tail_s + tail_m, key=lambda x: (-x[1], x[0])))
out["tail_counts"] = {"harness": len(tail_h), "app": len(tail_a), "local": len(tail_l), "hw": len(tail_hw), "sub": len(tail_s), "model": len(tail_m)}

# ---- per-thread stats
th = defaultdict(lambda: {"authors": set(), "tools": defaultdict(set)})
for r in rows:
    if r["status"] == "uses" and r["tool"] != "TOTAL SPEND":
        th[r["thread"]]["authors"].add(r["author"])
        if r["category"] in ("harness", "app"): th[r["thread"]]["tools"][r["tool"]].add(r["author"])
out["threads"] = {k: {"authors": len(v["authors"]), "top": sorted(((t, len(u)) for t, u in v["tools"].items()), key=lambda x: -x[1])[:3]} for k, v in th.items()}

# ---- sensitivity: harness+app ranking without the local-model thread
LOCAL_THREAD = 48542100
su = defaultdict(set); sa = set()
for r in rows:
    if r["thread"] == LOCAL_THREAD or r["status"] != "uses": continue
    sa.add(r["author"])
    if r["category"] in ("harness", "app"): su[r["tool"]].add(r["author"])
s = [f"| # | Tool | Autori | % z {len(sa)} |", "|---|---|---|---|"]
s += [f"| {i} | {t} | {len(u)} | {100 * len(u) / len(sa):.0f} % |" for i, (t, u) in enumerate(sorted(su.items(), key=lambda x: -len(x[1]))[:10], 1)]
out["sens"] = "\n".join(s)
# Claude paid tiers rolled up
tiers = {"Claude Pro": 0, "Claude Max (any)": 0, "Claude Ultra": 0}
maxu = set()
for t, u in users.items():
    if t.startswith("Claude Max"): maxu |= u
tiers["Claude Pro"] = len(users.get("Claude Pro", ())); tiers["Claude Max (any)"] = len(maxu); tiers["Claude Ultra"] = len(users.get("Claude Ultra", ()))
out["claude_tiers"] = tiers

json.dump(out, open(f"{W}/agg.json", "w"), ensure_ascii=False, indent=1, default=list)
for k in ("harness", "app", "local", "hw", "sub", "model_fam", "model_grp", "trend", "churn", "spend"):
    print(f"\n### {k}\n{out[k]}")
print("\n### tail\n", out["tail"])
print("\nrows", len(rows), "authors", len(all_users))

# ---- structured data for infographic
def ranked(cats, k=None):
    xs = sorted(((t, len(u)) for t, u in users.items() if cat.get(t) in cats), key=lambda x: (-x[1], x[0]))
    return [{"name": t, "n": n} for t, n in (xs[:k] if k else xs) if n >= 3]
pair_ch = Counter()
for (a, t), r in final.items():
    if r["status"] == "left": pair_ch[(t, r.get("left_to") or "?")] += 1
open_w = {"Qwen", "DeepSeek", "GLM", "Gemma", "Kimi", "Mistral/Devstral", "Nemotron", "gpt-oss (open)", "MiniMax", "MiMo (Xiaomi)", "Llama"}
dd = {
 "n_authors": len(all_users), "harness": ranked({"harness"}, 18), "app": ranked({"app"}, 10), "local": ranked({"local_runtime"}, 8), "hw": ranked({"hardware"}),
 "sub": ranked({"subscription"}, 18),
 "model_grp": [{"name": g, "exp": len(grp_exp[g]), "imp": len(grp_imp[g]), "open": g in open_w} for g in gs if len(grp_exp[g]) + len(grp_imp[g]) >= 5],
 "model_fam": [{"name": t, "n": len(u), "v": [k for k, _ in fam_versions[t].most_common(2)]} for t, u in items if len(u) >= 5],
 "quarters": qs, "q_active": [len(qa[q]) for q in qs],
 "trend": [{"name": t, "n": [len(qt[t][q]) for q in qs]} for t in top10],
 "churn": [{"from": a, "to": b, "n": n} for (a, b), n in pair_ch.most_common() if n >= 1],
 "churn_tot": [{"name": t, "n": n} for t, n in left_tot.most_common(12)],
 "spend": vals, "spend_buckets": [b[k] for k in ["<$20", "$20–100", "$100–250", ">$250"]],
 "claude_tiers": tiers,
}
json.dump(dd, open(f"{W}/viz.json", "w"), ensure_ascii=False)
