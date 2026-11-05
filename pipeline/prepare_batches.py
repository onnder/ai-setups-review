"""Build classification input: all 2026 comments from HN Ask threads + Lobste.rs/Tildes threads -> data/classified/input/vNN.jsonl (160 per batch)."""
import json, glob, re, html, os
from paths import DATA
from fetch_hn import ASK

def clean(t):
    t = re.sub(r"<p>", "\n", t or ""); t = re.sub(r"<a [^>]*href=\"([^\"]*)\"[^>]*>.*?</a>", r"\1", t); t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()

def hn_comments():
    out = []
    for tid in ASK:
        root = json.load(open(DATA / f"hn/raw/{tid}.json"))
        if root.get("text") and root.get("author") and root["created_at"][:4] == "2026":
            out.append({"source": "hn", "id": root["id"], "thread": tid, "author": root["author"], "date": root["created_at"][:10], "parent": "(OP) " + root.get("title", ""), "text": clean(root["text"])[:5000]})
        def walk(n, ptxt):
            for c in n.get("children", []):
                t = clean(c.get("text"))
                if c.get("author") and t and c["created_at"][:4] == "2026":
                    out.append({"source": "hn", "id": c["id"], "thread": tid, "author": c["author"], "date": c["created_at"][:10], "parent": ptxt[:300], "text": t[:5000]})
                walk(c, t or ptxt)
        walk(root, root.get("title") or "")
    return out

def community_comments():
    out = []
    for f in sorted(glob.glob(f"{DATA}/community/raw/*.json")):
        d = json.load(open(f)); byid = {c["id"]: c["text"] for c in d["comments"]}
        for c in d["comments"]:
            if c["date"][:4] != "2026" or not c["text"]: continue
            out.append({"source": d["source"], "id": c["id"], "thread": d["id"], "author": c["author"], "date": c["date"],
                        "parent": (byid.get(c["parent"]) or ("(story) " + d["meta"]["title"]))[:300], "text": c["text"][:5000]})
    return out

if __name__ == "__main__":
    allc = hn_comments() + community_comments(); B = 160
    os.makedirs(DATA / "classified/input", exist_ok=True)
    for i in range(0, len(allc), B):
        with open(DATA / f"classified/input/v{i//B:02d}.jsonl", "w") as fh:
            for c in allc[i:i+B]: fh.write(json.dumps(c, ensure_ascii=False) + "\n")
    print("comments", len(allc), "batches", (len(allc) + B - 1) // B)
