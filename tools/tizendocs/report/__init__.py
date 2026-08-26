"""Report formatters. Each is a pure ``list[Finding] -> str``."""
from . import text

FORMATS = {"text": text.render}
