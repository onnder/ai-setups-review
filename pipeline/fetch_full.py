"""Fetch full text for selected Reader docs (by id) -> full/<id>.json with plain text."""
from paths import ROOT, PIPE, DATA, SITE, DOCS
import json, os, re, html, time, urllib.request, urllib.parse, urllib.error
TOKEN = open(os.path.expanduser("~/.config/readwise/token")).read().strip()
os.makedirs(f"{DATA}/readwise/full", exist_ok=True)
def text(h):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", h or "", flags=re.S)
    h = re.sub(r"<(p|br|li|h[1-6]|div|tr)[^>]*>", "\n", h); h = re.sub(r"<[^>]+>", "", h)
    return re.sub(r"\n{3,}", "\n\n", html.unescape(h)).strip()
sel = json.load(open(f"{DATA}/readwise/selected.json")); done = 0
for s in sel:
    f = f"{DATA}/readwise/full/{s['id']}.json"
    if os.path.exists(f): continue
    while True:
        try:
            req = urllib.request.Request("https://readwise.io/api/v3/list/?" + urllib.parse.urlencode({"id": s["id"], "withHtmlContent": "true"}), headers={"Authorization": f"Token {TOKEN}"})
            r = json.load(urllib.request.urlopen(req, timeout=60))["results"]; break
        except urllib.error.HTTPError as e:
            if e.code == 429: time.sleep(int(e.headers.get("Retry-After", "30")) + 1); continue
            r = []; break
    t = text(r[0].get("html_content")) if r else ""
    json.dump({**s, "text": t[:30000], "len": len(t)}, open(f, "w"), ensure_ascii=False)
    done += 1; time.sleep(3.1)
    if done % 25 == 0: print("fetched", done, flush=True)
print("done", done)
