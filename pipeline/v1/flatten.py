import json, re, html, sys, os
W = os.path.dirname(os.path.abspath(__file__))
A = "50366117 47388646 48542100 46255285 48771515 48413629 48492118 46292682 46993479 49934037 50337431 49290713 47559293 48587808 47616250 50016644 48166147 49449290 49586386 49848426 46731068".split()
TOOLS = r"claude|anthropic|opus|sonnet|haiku|codex|openai|chatgpt|gpt|o3|o4|cursor|copilot|windsurf|cline|roo|kilo|aider|zed|jetbrains|junie|gemini|antigravity|jules|amp|opencode|crush|goose|continue|cody|devin|kiro|warp|ollama|llama|lm ?studio|mlx|vllm|qwen|deepseek|kimi|glm|mistral|devstral|grok|openrouter|perplexity|v0|lovable|bolt|replit|conductor|superwhisper|whisper|wispr|openclaw|pi agent|droid|factory|cerebras|groq|minimax|gpt-oss|llama\.cpp|neovim|emacs|gptel|simon|llm cli|mcp|agent"
TRIG = r"\bI use\b|\bI'm using\b|\bI am using\b|\bwe use\b|\bmy setup\b|\bmy workflow\b|\bmy stack\b|\bI pay\b|\bsubscription\b|\bplan\b|\bper month\b|/mo\b|/month\b|\$\d|\bswitched\b|\bcancel|\bstopped using\b|\bmoved to\b|\bdaily driver\b|\bI run\b|\blocal(ly)?\b"
tre = re.compile(TOOLS, re.I); trg = re.compile(TRIG, re.I)
def clean(t):
    t = re.sub(r"<p>", "\n", t or ""); t = re.sub(r"<a [^>]*href=\"([^\"]*)\"[^>]*>.*?</a>", r"\1", t); t = re.sub(r"<[^>]+>", "", t)
    return html.unescape(t).strip()
out = open(f"{W}/comments.jsonl", "w"); n = kept = 0
for tid in A:
    root = json.load(open(f"{W}/raw/{tid}.json"))
    def walk(node, parent_text):
        global n, kept
        for c in node.get("children", []):
            txt = clean(c.get("text"))
            if c.get("author") and txt:
                n += 1
                if tre.search(txt) or trg.search(txt):
                    kept += 1
                    out.write(json.dumps({"id": c["id"], "thread": int(tid), "author": c["author"], "date": c["created_at"][:10], "parent": parent_text[:300], "text": txt[:4000]}) + "\n")
            walk(c, txt)
    # include the Ask HN post body itself (OP may describe their setup)
    body = clean(root.get("text"))
    if body and root.get("author"):
        n += 1; kept += 1
        out.write(json.dumps({"id": root["id"], "thread": int(tid), "author": root["author"], "date": root["created_at"][:10], "parent": "(OP) " + (root.get("title") or ""), "text": body[:4000]}) + "\n")
    walk(root, root.get("title") or "")
print("total", n, "kept", kept)
