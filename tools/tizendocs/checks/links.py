"""L-* rules: link and image target resolution."""
import re

from .. import markdown, paths
from ..findings import ERROR, Finding

BROKEN = "L-BROKEN"
ANCHOR = "L-ANCHOR"

# Versioned API routes published by a separate pipeline, so no file exists here.
PUBLISHED_API = re.compile(r"^docs/application/(?:native|dotnet)/api/[^/]+/latest/.+")


def published_api(path):
    return bool(PUBLISHED_API.match(path))


KIND = {"md-link": "link", "md-image": "image"}


def check_links(index, path, source):
    for syntax, url, offset in source.references():
        if not url or markdown.is_external(url):
            continue
        raw, fragment = markdown.split_fragment(url)
        target = paths.resolve(path, raw)
        kind = KIND[syntax]
        if not index.exists(target):
            if raw.startswith("/") and not raw.endswith(".md"):
                continue  # Published API and route paths need not have a repo file.
            if published_api(target):
                continue  # The stable `latest` API route is published separately.
            line, col = source.position(offset)
            yield Finding(ERROR, BROKEN, path, f"{kind} target does not exist: {url}",
                          line=line, col=col, syntax=syntax)
        elif (fragment and target.endswith(".md") and not index.generated(target)
                and fragment.lower() not in index.anchors(target)):
            line, col = source.position(offset)
            yield Finding(ERROR, ANCHOR, path, f"anchor does not exist: {url}",
                          line=line, col=col, syntax=syntax)
