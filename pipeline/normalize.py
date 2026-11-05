"""Shared tool-name normalization for v1 and v2 aggregations."""
import re

ALIAS = {  # lowercase raw -> canonical
    "codex": "Codex CLI", "codex cli": "Codex CLI", "openai codex": "Codex CLI", "codex app": "Codex (app/cloud)",
    "copilot": "GitHub Copilot", "github copilot": "GitHub Copilot", "vs code copilot": "GitHub Copilot", "copilot cli": "GitHub Copilot",
    "claude code": "Claude Code", "claudecode": "Claude Code",
    "chatgpt": "ChatGPT (app/web)", "chatgpt (app/web)": "ChatGPT (app/web)",
    "claude": "Claude (app/web)", "claude.ai": "Claude (app/web)", "claude (app/web)": "Claude (app/web)", "claude desktop": "Claude (app/web)",
    "gemini": "Gemini (app/web)", "gemini (app/web)": "Gemini (app/web)",
    "lmstudio": "LM Studio", "lm studio": "LM Studio", "llama.cpp": "llama.cpp", "llamacpp": "llama.cpp", "llama-server": "llama.cpp", "ollama": "Ollama", "mlx": "MLX", "mlx-lm": "MLX", "vllm": "vLLM",
    "opencode": "OpenCode", "open code": "OpenCode", "sst opencode": "OpenCode",
    "gptel": "Emacs gptel", "emacs gptel": "Emacs gptel",
    "pi": "Pi", "pi agent": "Pi", "pi-mono": "Pi", "pi coding agent": "Pi",
    "zed": "Zed", "zed editor": "Zed", "cursor": "Cursor", "cursor cli": "Cursor",
    "gemini cli": "Gemini CLI", "aider": "Aider", "amp": "Amp", "ampcode": "Amp", "sourcegraph amp": "Amp",
    "openrouter": "OpenRouter", "open webui": "Open WebUI", "openwebui": "Open WebUI",
    "junie": "JetBrains AI/Junie", "jetbrains ai": "JetBrains AI/Junie", "jetbrains ai/junie": "JetBrains AI/Junie",
    "droid": "Factory Droid", "factory": "Factory Droid", "factory droid": "Factory Droid",
}
IMPLIED = {"Claude Code": "Claude", "Claude (app/web)": "Claude", "Codex CLI": "GPT (OpenAI)", "Codex (app/cloud)": "GPT (OpenAI)", "ChatGPT (app/web)": "GPT (OpenAI)",
           "Gemini CLI": "Gemini", "Gemini (app/web)": "Gemini", "Antigravity": "Gemini", "Jules": "Gemini"}
def model_group(fam):
    f = fam.lower()
    if f.startswith("claude"): return "Claude"
    if f.startswith("gpt-oss"): return "gpt-oss (open)"
    if f.startswith(("gpt", "openai", "o3", "o4", "codex")): return "GPT (OpenAI)"
    if f.startswith("gemini"): return "Gemini"
    return fam
def norm(t):
    t = (t or "").strip()
    l = t.lower()
    if l in ALIAS: return ALIAS[l]
    for pat, canon in NORM_RE:
        if re.search(pat, l): return canon
    return t
NORM_RE = [
    (r"^oh-?my-?pi", "oh-my-pi"), (r"^deepseek ?harness", "DeepSeek Harness"), (r"^herdr", "Herdr"),
    (r"^hermes( agent)?$", "Hermes Agent"), (r"^(claude )?fable$", "Claude Fable"), (r"spec ?kit", "GitHub Spec Kit"),
    (r"^t3 ?code$", "T3 Code"), (r"^big ?pickle", "Big Pickle (OpenCode)"), (r"^duck\.ai$", "Duck.ai"),
    (r"^oh-?my-?opencode$", "oh-my-opencode"), (r"^opencode go", "OpenCode Go"), (r"^opencode zen", "OpenCode Zen"),
    (r"^chatgpt.*(\$100|codex \$100)", "ChatGPT $100 plan"), (r"^chatgpt.*unspecified", "ChatGPT (plan unspecified)"),
    (r"^claude (subscription|\((paid|unspecified plan)|paid)", "Claude (plan unspecified)"), (r"^x premium", "X Premium (Grok)"), (r"^supergrok|^grok subscription", "SuperGrok"),
    (r"^muse code", "Muse Code subscription"),
]
def hw_class(t):
    l = t.lower()
    if re.search(r"dgx|gb10|ascent|spark", l): return "DGX Spark / GB10"
    if re.search(r"strix|ai max|395|framework desktop|bosgame", l): return "AMD Strix Halo"
    if re.search(r"mac|m[1-5]\b|apple m", l): return "Apple Silicon Mac"
    if re.search(r"rtx (pro )?6000|blackwell 72|v100|a100|h100|quadro|poweredge|cmp 170", l): return "NVIDIA RTX Pro / DC"
    if re.search(r"rtx|gtx|nvidia", l): return "NVIDIA GeForce"
    if re.search(r"radeon|7900|r9700|rx ?9|amd", l): return "AMD Radeon GPU"
    return None
RUNTIMES = {"llama.cpp", "Ollama", "LM Studio", "vLLM", "MLX", "oMLX", "llama-swap", "MLX-Serve", "EXO", "Lemonade", "Unsloth", "Unsloth Studio", "ds4-server", "antirez/ds4", "LiteLLM", "Strata"}

BLOG_AUTHOR = {"Simon Willison's Weblog": "Simon Willison", "martin@martinalderson.com (Martin Alderson)": "Martin Alderson",
               "seangoedecke.com": "Sean Goedecke", "seangoedecke.com RSS feed": "Sean Goedecke", "gklijs": "Gerard Klijs"}
