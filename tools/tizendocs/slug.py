"""Heading-to-anchor slug generation.

The publishing pipeline's Markdown engine is the only authority here, and its
configuration (``_config.yml``) is gitignored, so we cannot read it. Until it
is identified, keep this the single place the rule lives.
"""
import re


def slug(value):
    value = re.sub(r"\[[^]]*\]\([^)]+\)", "", value)
    value = re.sub(r"[`*_]", "", value).lower()
    value = re.sub(r"[^\w\s-]", "", value)
    return re.sub(r"\s+", "-", value).strip("-")
