"""Repository-relative paths shared by all pipeline scripts."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIPE = ROOT / "pipeline"
DATA = ROOT / "data"
SITE = ROOT / "site"
DOCS = ROOT / "docs"
