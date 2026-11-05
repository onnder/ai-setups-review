"""Readwise Reader: (1) `candidates` — keyword filter of 2026 library + ITech-feed docs -> candidates.json + screening batches;
(2) `select` — merge LLM screening verdicts (+ all Swamp Club posts), drop HN-blog duplicates -> selected.json.
ITech feed list comes from a Reader snapshot markdown (path via READER_FEEDS_MD env var)."""
import json, re, os, sys, glob, collections
from urllib.parse import urlparse
from paths import DATA

RW = DATA / "readwise"
KW = re.compile(r"\b(claude code|codex|cursor|copilot|opencode|aider|agentic|coding agent|ai agent|agents?\b|llms?\b|vibe.?cod|ai coding|ai[- ]assisted|my (ai|llm|agent) (setup|workflow|stack)|how i use|how i code|how i write|workflow|harness|mcp|gemini cli|antigravity|ollama|local model|swamp)\b", re.I)
HN_BLOGS = {"boristane.com/blog/how-i-use-claude-code", "stavros.io/posts/how-i-write-software-with-llms", "mitchellh.com/writing/my-ai-adoption-journey",
            "theocharis.dev/blog/llm-critics-are-right-i-use-llms-anyway", "ben.stolovitz.com/posts/how-use-ai-oct-2026", "lalitm.com/post/building-syntaqlite-ai",
            "crawshaw.io/blog/eight-more-months-of-agents", "fabiensanglard.net/agent.md", "neilkakkar.com/productive-with-claude-code",
            "chad.cm/posts/2026-8-11-my-agent-setup", "laurentiugabriel.github.io/blog/articles/how-i-use-llms-to-learn"}

def host(u):
    h = urlparse(u or "").netloc.lower(); return h[4:] if h.startswith("www.") else h
def in_2026(d):
    p = (d.get("published_date") or "")[:4]; return p == "2026" if p else (d.get("saved_at") or "")[:4] == "2026"
def docs():
    return [json.loads(l) for l in open(RW / "docs.jsonl")]

def candidates(feeds_md):
    s = open(feeds_md).read(); a = s.index("### ITech ("); b = s.index("\n### ", a + 5); block = s[a:b]
    names = {n.strip().lower() for n in re.findall(r"^\d+\.\s+(.+?)\s*$", block, re.M)}
    hosts = {host(u) for u in re.findall(r"^\s+(https?://\S+)", block, re.M)}
    D = [d for d in docs() if in_2026(d) and d.get("category") in ("article", "rss", "email", "pdf", "video")]
    def itech(d):
        hs = {host(d.get("source_url")), host(d.get("url"))}
        return bool(hs & hosts) or (d.get("site_name") or "").lower() in names or any(h and any(h.endswith("." + ih) or ih.endswith("." + h) for ih in hosts) for h in hs)
    pool = [d for d in D if d["location"] in ("later", "shortlist", "archive")] + [d for d in D if d["location"] == "feed" and itech(d)]
    seen, C = set(), []
    for d in pool:
        if not KW.search((d.get("title") or "") + " " + (d.get("summary") or "")): continue
        k = (d.get("source_url") or d["id"]).split("?")[0]
        if k not in seen: seen.add(k); C.append(d)
    json.dump(C, open(RW / "candidates.json", "w"), ensure_ascii=False)
    os.makedirs(RW / "screen/in", exist_ok=True)
    for i in range(0, len(C), 160):
        with open(RW / f"screen/in/s{i//160:02d}.jsonl", "w") as fh:
            for d in C[i:i+160]:
                fh.write(json.dumps({"id": d["id"], "title": d.get("title"), "author": d.get("author"), "site": d.get("site_name"), "url": d.get("source_url"),
                                     "date": (d.get("published_date") or d.get("saved_at") or "")[:10], "loc": d["location"], "summary": (d.get("summary") or "")[:600]}, ensure_ascii=False) + "\n")
    print("candidates", len(C))

def select():
    C = {d["id"]: d for d in json.load(open(RW / "candidates.json"))}
    S = [json.loads(l) for f in sorted(glob.glob(f"{RW}/screen/out/*.jsonl")) for l in open(f) if l.strip()]
    sel = {s["id"]: s for s in S if s["id"] in C}
    for d in docs():
        if in_2026(d) and "swamp" in ((d.get("site_name") or "") + (d.get("source_url") or "")).lower():
            C.setdefault(d["id"], d); sel.setdefault(d["id"], {"verdict": "maybe", "why": "Swamp Club field report"})
    key = lambda u: (u or "").split("?")[0].split("#")[0].rstrip("/").replace("https://", "").replace("http://", "").replace("www.", "").replace(".html", "").replace("/index", "")
    out, seen = [], set()
    for i, v in sel.items():
        d = C[i]; k = key(d.get("source_url"))
        if any(k.startswith(h) for h in HN_BLOGS) or k in seen: continue
        seen.add(k)
        out.append({"id": i, "verdict": v["verdict"], "why": v["why"], "title": d.get("title"), "author": d.get("author"), "site": d.get("site_name"),
                    "url": d.get("source_url"), "date": (d.get("published_date") or d.get("saved_at") or "")[:10], "loc": d["location"], "cat": d.get("category")})
    json.dump(out, open(RW / "selected.json", "w"), ensure_ascii=False, indent=0)
    print("selected", len(out), collections.Counter(o["verdict"] for o in out))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "candidates": candidates(os.environ["READER_FEEDS_MD"])
    elif cmd == "select": select()
    else: sys.exit("usage: readwise_select.py candidates|select")
