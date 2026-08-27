"""Report formatters. Each is a pure ``(findings, summary) -> str``."""
from . import github, jsonl, sarif, text

FORMATS = {
    "text": text.render,
    "jsonl": jsonl.render,
    "sarif": sarif.render,
    "github": github.render,
}
