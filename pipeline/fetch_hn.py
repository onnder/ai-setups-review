"""Download full HN comment trees (Algolia API) for the approved Ask HN threads and blog-post stories -> data/hn/raw/<id>.json."""
import json, os, urllib.request
from paths import DATA

ASK = "50366117 47388646 48542100 46255285 48771515 48413629 48492118 46292682 46993479 49934037 50337431 49290713 47559293 48587808 47616250 50016644 48166147 49449290 49586386 49848426 46731068".split()
ARTICLES = "47106686 47394022 46903558 48933310 50355767 47648828 46933223 49410932 47494890 49272484 49234675".split()
CONTEXT = "47460525 47282777 47633396".split()

if __name__ == "__main__":
    os.makedirs(DATA / "hn/raw", exist_ok=True)
    for i in ASK + ARTICLES + CONTEXT:
        out = DATA / f"hn/raw/{i}.json"
        if out.exists(): continue
        out.write_bytes(urllib.request.urlopen(f"https://hn.algolia.com/api/v1/items/{i}", timeout=60).read())
        print("fetched", i)
