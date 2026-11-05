"""Aggregate classified JSONL (calendar 2026; hn/lobsters/tildes/blogs) -> data/mentions.csv + data/viz2.json."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, glob, csv, os, re, statistics
from collections import defaultdict, Counter
from normalize import IMPLIED, model_group, norm, hw_class, RUNTIMES, BLOG_AUTHOR

SRC = ["hn", "lobsters", "tildes", "blogs"]
SRC_LABEL = {"hn": "Hacker News", "lobsters": "Lobste.rs", "tildes": "Tildes", "blogs": "Blogs (authors)"}
IFACES = ["terminal", "ide-extension", "ai-editor", "desktop-app", "web", "chat-bot", "api-script", "vim-emacs", "acp", "mobile"]
IF_LABEL = {"terminal": "Terminal / TUI", "ide-extension": "IDE extension", "ai-editor": "AI editor", "desktop-app": "Desktop app", "web": "Web",
            "chat-bot": "Chat bot (Telegram, Slack…)", "api-script": "Own scripts / API", "vim-emacs": "Vim / Emacs", "acp": "ACP (agent in editor)", "mobile": "Mobile"}
SOURCE_SPECIFIC = {"Swamp"}  # Q25: product-community tools excluded from cross-source comparison

def vnorm(v):
    v = re.sub(r"(?i)\b(claude|anthropic|opus|sonnet|haiku|fable|gemma|kimi|glm|qwen|deepseek|openai|gpt|gemini|mistral|devstral|ministral|grok)\b[- ]*", "", str(v)).strip(" -")
    return v or None
def quarter(d): return f"Q{(int(d[5:7]) - 1) // 3 + 1}"

rows = []
def add(r, source):
    if r.get("status") not in ("uses", "left") or not str(r.get("date", "")).startswith("2026"): return
    r["source"] = source
    r["tool"] = norm(r["tool"])
    if r.get("left_to"): r["left_to"] = norm(r["left_to"])
    if r.get("via"): r["via"] = norm(r["via"])
    if r.get("category") == "local_runtime" and r["tool"] not in RUNTIMES and hw_class(r["tool"]):
        r["model_version"], r["tool"], r["category"] = r["tool"], hw_class(r["tool"]), "hardware"
    if source == "blogs": r["author"] = BLOG_AUTHOR.get(r["author"], r["author"])
    r["author_key"] = f"{source}:{r['author']}"
    r["comment_id"] = str(r.get("comment_id"))
    rows.append(r)
for f in sorted(glob.glob(f"{DATA}/classified/output/v*.jsonl")):
    for ln in open(f):
        if ln.strip():
            r = json.loads(ln); add(r, r.get("source", "hn"))
for f in [f"{DATA}/hn/v1/classified/articles.jsonl"] + sorted(glob.glob(f"{DATA}/classified/output/blog_*.jsonl")):
    if os.path.exists(f):
        for ln in open(f):
            if ln.strip(): add(json.loads(ln), "blogs")

LINK = {"hn": "https://news.ycombinator.com/item?id={}", "lobsters": "https://lobste.rs/c/{}", "tildes": None, "blogs": None}
def link(r):
    if r["source"] == "tildes": return f"https://tildes.net/~comp/{r['thread']}#comment-{r['comment_id']}"
    if r["source"] == "blogs": return r.get("url") or f"https://news.ycombinator.com/item?id={r['thread']}"
    return LINK[r["source"]].format(r["comment_id"])
cols = ["source", "author", "date", "quarter", "thread", "comment_id", "link", "tool", "category", "status", "left_to", "interface", "interface_explicit", "host", "via", "model_version", "spend_usd_mo", "quote"]
with open(f"{DATA}/mentions.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader()
    for r in sorted(rows, key=lambda r: (r["date"], r["source"])):
        w.writerow({**r, "quarter": quarter(r["date"]), "link": link(r)})

# latest status per (author_key, tool)
final = {}
for r in sorted(rows, key=lambda r: r["date"]):
    if r["tool"] != "TOTAL SPEND": final[(r["author_key"], r["tool"])] = r
cat = {t: c.most_common(1)[0][0] for t, c in ((t, Counter(r["category"] for r in rows if r["tool"] == t)) for t in {r["tool"] for r in rows})}
uses = [r for r in final.values() if r["status"] == "uses"]
users = defaultdict(set)
for r in uses: users[r["tool"]].add(r["author_key"])
src_authors = {s: {r["author_key"] for r in uses if r["source"] == s} for s in SRC}
all_authors = set().union(*src_authors.values())

def rank(cats, by_src=None, k=None, min_n=3):
    u = defaultdict(set)
    for r in uses:
        if cat.get(r["tool"]) in cats and (by_src is None or r["source"] == by_src): u[r["tool"]].add(r["author_key"])
    xs = sorted(((t, len(a)) for t, a in u.items()), key=lambda x: (-x[1], x[0]))
    xs = [x for x in xs if x[1] >= min_n]
    return [{"name": t, "n": n} for t, n in (xs[:k] if k else xs)]

V = {"sources": [{"id": s, "label": SRC_LABEL[s], "authors": len(src_authors[s])} for s in SRC], "n_authors": len(all_authors), "n_rows": len(rows)}
V["harness"] = [{**r, "tag": "Swamp Club"} if r["name"] in SOURCE_SPECIFIC else r for r in rank({"harness"}, k=20)]
V["app"] = rank({"app"}, k=10)
V["local"] = rank({"local_runtime"}, k=8)
V["hw"] = rank({"hardware"})
V["sub"] = rank({"subscription"}, k=18)
# per-source harness share (Q: cross-source comparison), excluding source-specific tools
top = [x["name"] for x in rank({"harness", "app"}, k=14) if x["name"] not in SOURCE_SPECIFIC]
V["by_source"] = {"tools": top, "rows": []}
for s in SRC:
    n = max(1, len(src_authors[s])); u = defaultdict(set)
    for r in uses:
        if r["source"] == s: u[r["tool"]].add(r["author_key"])
    V["by_source"]["rows"].append({"src": s, "label": SRC_LABEL[s], "n": len(src_authors[s]), "share": [round(100 * len(u[t]) / n, 1) for t in top], "cnt": [len(u[t]) for t in top]})

# models
fam_users, fam_ver = defaultdict(set), defaultdict(Counter)
for r in uses:
    if r["category"] == "model":
        fam_users[r["tool"]].add(r["author_key"])
        v = vnorm(r.get("model_version")) if r.get("model_version") else None
        if v: fam_ver[r["tool"]][v] += 1
OPEN = {"Qwen", "DeepSeek", "GLM", "Gemma", "Kimi", "Mistral/Devstral", "Nemotron", "gpt-oss (open)", "MiniMax", "MiMo (Xiaomi)", "Llama", "Whisper", "NVIDIA Parakeet"}
grp_e, grp_i = defaultdict(set), defaultdict(set)
for t, u in fam_users.items(): grp_e[model_group(t)] |= u
for t, g in IMPLIED.items():
    for a in users.get(t, ()):
        if a not in grp_e[g]: grp_i[g].add(a)
gs = sorted(set(grp_e) | set(grp_i), key=lambda g: (-(len(grp_e[g]) + len(grp_i[g])), g))
V["model_grp"] = [{"name": g, "exp": len(grp_e[g]), "imp": len(grp_i[g]), "open": g in OPEN} for g in gs if len(grp_e[g]) + len(grp_i[g]) >= 5]
V["model_fam"] = [{"name": t, "n": len(u), "v": [k for k, _ in fam_ver[t].most_common(2)]} for t, u in sorted(fam_users.items(), key=lambda x: (-len(x[1]), x[0])) if len(u) >= 5]

# interfaces — authors per interface type (harness/app/model lines), all vs explicit-only
iface_all, iface_exp = defaultdict(set), defaultdict(set)
for r in uses:
    if r["category"] in ("harness", "app", "model") and r.get("interface") in IFACES:
        iface_all[r["interface"]].add(r["author_key"])
        if r.get("interface_explicit"): iface_exp[r["interface"]].add(r["author_key"])
V["iface"] = [{"id": i, "name": IF_LABEL[i], "n": len(iface_all[i]), "exp": len(iface_exp[i])} for i in sorted(IFACES, key=lambda i: (-len(iface_all[i]), i))]
# per-tool interface split (explicit only) for multi-surface tools
def split(tool):
    c = defaultdict(set)
    for r in rows:
        if r["status"] == "uses" and r["tool"] == tool and r.get("interface_explicit") and r.get("interface") in IFACES: c[r["interface"]].add(r["author_key"])
    return [{"id": i, "name": IF_LABEL[i], "n": len(a)} for i, a in sorted(c.items(), key=lambda x: (-len(x[1]), x[0]))]
V["tool_split"] = {t: {"total": len(users.get(t, ())), "explicit": split(t)} for t in ["Claude Code", "Codex CLI", "GitHub Copilot", "OpenCode", "Claude (app/web)", "ChatGPT (app/web)"]}
hosts = defaultdict(set)
for r in rows:
    if r["status"] == "uses" and r.get("host"): hosts[r["host"]].add(r["author_key"])
V["hosts"] = [{"name": h, "n": len(a)} for h, a in sorted(hosts.items(), key=lambda x: (-len(x[1]), x[0])) if len(a) >= 3][:14]
# model × via matrix (model groups × top vias)
mv = defaultdict(lambda: defaultdict(set))
for r in rows:
    if r["status"] == "uses" and r["category"] == "model" and r.get("via"):
        mv[model_group(r["tool"])][r["via"]].add(r["author_key"])
vtot = Counter()
for g, d in mv.items():
    for v, a in d.items(): vtot[v] += len(a)
vias = [v for v, _ in sorted(vtot.items(), key=lambda x: (-x[1], x[0]))[:9]]
mgs = [g for g in sorted(mv, key=lambda g: (-sum(len(a) for a in mv[g].values()), g)) if sum(len(a) for a in mv[g].values()) >= 5][:9]
V["via"] = {"models": mgs, "vias": vias + ["other"],
            "m": [[len(mv[g][v]) for v in vias] + [sum(len(a) for v2, a in mv[g].items() if v2 not in vias)] for g in mgs],
            "tot": [sum(len(a) for a in mv[g].values()) for g in mgs]}

# trend by quarter (2026), share of active authors that quarter
qa, qt = defaultdict(set), defaultdict(lambda: defaultdict(set))
for r in rows:
    if r["status"] == "uses" and r["tool"] != "TOTAL SPEND":
        q = quarter(r["date"]); qa[q].add(r["author_key"]); qt[r["tool"]][q].add(r["author_key"])
qs = sorted(qa)
t10 = [x["name"] for x in rank({"harness", "app"}, k=10)]
V["quarters"], V["q_active"] = qs, [len(qa[q]) for q in qs]
V["trend"] = [{"name": t, "n": [len(qt[t][q]) for q in qs]} for t in t10]

# churn
pair, ltot = Counter(), Counter()
for r in final.values():
    if r["status"] == "left": ltot[r["tool"]] += 1; pair[(r["tool"], r.get("left_to") or "?")] += 1
V["n_left"] = sum(ltot.values())
V["churn"] = [{"from": a, "to": b, "n": n} for (a, b), n in sorted(pair.items(), key=lambda x: (-x[1], x[0])) if cat.get(a) in ("harness", "app")]

# spend
spend = {}
for r in rows:
    v = r.get("spend_usd_mo")
    if isinstance(v, (int, float)) and v >= 0: spend[r["author_key"]] = max(spend.get(r["author_key"], 0), v)
vals = sorted(spend.values())
V["spend"] = vals
V["spend_buckets"] = [sum(1 for v in vals if v < 20), sum(1 for v in vals if 20 <= v < 100), sum(1 for v in vals if 100 <= v <= 250), sum(1 for v in vals if v > 250)]
def su(pred): return {r["author_key"] for r in uses if r["category"] == "subscription" and pred(r["tool"])}
maxu = su(lambda t: t.startswith("Claude Max"))
V["providers"] = [
    {"name": "Anthropic", "n": len(su(lambda t: t.startswith("Claude") and "Free" not in t)), "detail": {"Pro": len(su(lambda t: t == "Claude Pro")), "Max": len(maxu), "Ultra": len(su(lambda t: t == "Claude Ultra"))}},
    {"name": "OpenAI", "n": len(su(lambda t: t.startswith("ChatGPT"))), "detail": {"Plus": len(su(lambda t: t == "ChatGPT Plus")), "Pro": len(su(lambda t: t == "ChatGPT Pro"))}},
    {"name": "API / OpenRouter", "n": len(su(lambda t: "pay-as-you-go" in t or "OpenRouter" in t)), "detail": {}},
    {"name": "Employer pays", "n": len(su(lambda t: "mployer" in t or "Team/Enterprise" in t or "Business" in t)), "detail": {}},
]
cc, cx = users.get("Claude Code", set()), users.get("Codex CLI", set())
V["venn"] = {"both": len(cc & cx), "cc": len(cc - cx), "cx": len(cx - cc), "none": len(all_authors - cc - cx)}
V["local_any"] = len({r["author_key"] for r in uses if r["category"] in ("local_runtime", "hardware")})

# calibration vs 2026 surveys: community share among authors naming >=1 coding harness
harness_authors = {r["author_key"] for r in uses if r["category"] == "harness"}
def hshare(*tools):
    a = set().union(*(users.get(t, set()) for t in tools)) & harness_authors
    return round(100 * len(a) / max(1, len(harness_authors)), 1)
SURVEY_TOOLS = [("Claude Code", ("Claude Code",), 65.5, 39, 71), ("GitHub Copilot", ("GitHub Copilot",), 58.7, 21, 46),
                ("Codex", ("Codex CLI", "Codex (app/cloud)"), 29.5, 16, None), ("Cursor", ("Cursor",), 25.5, 12, 39),
                ("Antigravity", ("Antigravity",), 16.0, 6, None), ("OpenCode", ("OpenCode",), 13.6, 7, None),
                ("JetBrains AI", ("JetBrains AI/Junie", "JetBrains Thinkrail"), 12.8, 9, None), ("Windsurf", ("Windsurf",), 6.5, None, None),
                ("Pi", ("Pi", "oh-my-pi"), 4.4, None, None), ("Cline", ("Cline",), 4.5, None, None), ("Aider", ("Aider",), 2.1, None, None)]
V["n_harness_authors"] = len(harness_authors)
V["surveys"] = [{"name": n, "community": hshare(*ts), "so": so, "jb": jb, "pe": pe} for n, ts, so, jb, pe in SURVEY_TOOLS]

json.dump(V, open(f"{DATA}/viz2.json", "w"), ensure_ascii=False)
pr = lambda k: print(f"\n## {k}\n", json.dumps(V[k], ensure_ascii=False)[:900])
print("rows", len(rows), "authors", V["n_authors"], V["sources"])
for k in ("harness", "iface", "tool_split", "hosts", "via", "by_source", "model_grp", "providers", "venn", "spend_buckets", "quarters", "q_active", "n_left"): pr(k)
