"""Fetch Lobsters (JSON) and Tildes (HTML) threads from candidates TSV -> raw/<source>_<id>.json (flat comment list)."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import csv, json, os, re, html, time, urllib.request
UA = {"User-Agent": "Mozilla/5.0 research"}
def get(u):
    for i in range(3):
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30).read().decode("utf-8", "replace")
        except Exception as e:
            time.sleep(3 * (i + 1)); err = e
    raise err
def clean(t):
    t = re.sub(r"<(p|br|li)[^>]*>", "\n", t or ""); t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()
rows = [r for r in csv.DictReader(open(f"{DATA}/community/candidates_lob_tildes.tsv"), delimiter="\t") if r["relevance"] in ("high", "medium")]
for r in rows:
    out = f"{DATA}/community/raw/{r['source']}_{r['id']}.json"
    if os.path.exists(out): continue
    if r["source"] == "lobsters":
        d = json.loads(get(f"https://lobste.rs/s/{r['id']}.json"))
        cs = [{"id": c["short_id"], "author": c.get("commenting_user") if isinstance(c.get("commenting_user"), str) else (c.get("commenting_user") or {}).get("username"),
               "date": c["created_at"][:10], "parent": c.get("parent_comment"), "text": clean(c.get("comment") or "")} for c in d.get("comments", [])]
        meta = {"title": d["title"], "url": d.get("url"), "date": d["created_at"][:10], "author": (d.get("submitter_user") if isinstance(d.get("submitter_user"), str) else (d.get("submitter_user") or {}).get("username")),
                "body": clean(d.get("description") or "")}
        time.sleep(1.1)
    else:
        s = get(r["url_of_discussion"])
        cs = []
        for m in re.finditer(r'<article[^>]*id="comment-([a-z0-9]+)"[^>]*>(.*?)(?=<article[^>]*id="comment-|\Z)', s, re.S):
            body = m.group(2)
            a = re.search(r'class="link-user"[^>]*>([^<]+)<', body); dt = re.search(r'<time[^>]*datetime="([^"]+)"', body)
            tx = re.search(r'<div class="comment-text"\s*>(.*?)</div>\s*<menu', body, re.S)
            if a and tx: cs.append({"id": m.group(1), "author": a.group(1).strip(), "date": dt.group(1)[:10] if dt else r["date"], "parent": None, "text": clean(tx.group(1))})
        t = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        meta = {"title": clean(t.group(1)) if t else r["title"], "url": r["url_of_discussion"], "date": r["date"], "author": None, "body": ""}
        time.sleep(2.1)
    json.dump({"source": r["source"], "id": r["id"], "relevance": r["relevance"], "meta": meta, "comments": cs}, open(out, "w"))
print("done", len(os.listdir(f"{DATA}/community/raw")))
