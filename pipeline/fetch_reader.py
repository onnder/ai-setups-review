"""Fetch Reader documents (later/shortlist/archive/feed) updated in 2026 -> docs.jsonl (metadata only, no html)."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, os, time, urllib.request, urllib.parse, urllib.error
TOKEN = open(os.path.expanduser("~/.config/readwise/token")).read().strip()
KEEP = ("id", "url", "source_url", "title", "author", "source", "category", "location", "site_name", "published_date", "saved_at", "created_at", "summary", "word_count", "tags", "reading_progress", "parent_id")
out = open(f"{DATA}/readwise/docs.jsonl", "w"); n = 0
for loc in ("later", "shortlist", "archive", "feed", "new"):
    cur = None; pages = 0
    while True:
        q = {"location": loc, "updatedAfter": "2026-01-01T00:00:00Z"}
        if cur: q["pageCursor"] = cur
        req = urllib.request.Request("https://readwise.io/api/v3/list/?" + urllib.parse.urlencode(q), headers={"Authorization": f"Token {TOKEN}"})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(int(e.headers.get("Retry-After", "30")) + 1); continue
            raise SystemExit(f"HTTP {e.code} on {loc}")
        for r in d["results"]:
            if r.get("parent_id"): continue
            out.write(json.dumps({k: r.get(k) for k in KEEP}, ensure_ascii=False) + "\n"); n += 1
        pages += 1; cur = d.get("nextPageCursor")
        print(f"{loc}: page {pages}, total {n}, count {d.get('count')}", flush=True)
        if not cur: break
        time.sleep(3.2)
print("done", n)
