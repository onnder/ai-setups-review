"""Score fetched Lobsters/Tildes threads by density of first-person AI-tool usage comments."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, glob, os, re, csv
TOOL = re.compile(r"claude|opus|sonnet|codex|chatgpt|\bgpt|cursor|copilot|windsurf|cline|roo code|kilo|aider|\bzed\b|junie|gemini|antigravity|\bamp\b|opencode|crush|goose|ollama|llama\.cpp|lm ?studio|\bmlx\b|vllm|qwen|deepseek|kimi|\bglm\b|mistral|devstral|openrouter|perplexity|openclaw|\bpi\b agent|pi\.dev|gptel|neovim|continue\.dev|kiro|warp", re.I)
FIRST = re.compile(r"\bI (use|used|am using|'m using|run|pay|switched|moved|tried|rely|stick|prefer|have been using|'ve been using)\b|\bmy (setup|workflow|stack|daily driver|subscription|plan)\b|\bwe use\b|\bat work we\b|\$\d+\s*(/|a |per )(mo|month)", re.I)
out = []
for f in sorted(glob.glob(f"{DATA}/community/raw/*.json")):
    d = json.load(open(f))
    cs = [c for c in d["comments"] if c.get("author") and c.get("text")]
    hits = [c for c in cs if TOOL.search(c["text"]) and FIRST.search(c["text"])]
    out.append({"source": d["source"], "id": d["id"], "rel": d["relevance"], "date": d["meta"]["date"], "title": d["meta"]["title"],
                "n": len(cs), "hits": len(hits), "authors": len({c["author"] for c in hits}), "ratio": round(len(hits) / max(1, len(cs)), 2)})
out.sort(key=lambda r: -r["authors"])
with open(f"{DATA}/community/thread_scores.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0]), delimiter="\t"); w.writeheader(); w.writerows(out)
for th in (3, 5, 8):
    sel = [r for r in out if r["authors"] >= th]
    print(f"authors>={th}: threads {len(sel)}, comments {sum(r['n'] for r in sel)}, hit comments {sum(r['hits'] for r in sel)}, by source", {s: sum(1 for r in sel if r['source'] == s) for s in ('lobsters', 'tildes')})
