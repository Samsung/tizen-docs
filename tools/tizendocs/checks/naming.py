"""N-* rules: file and directory naming. P-ROUTE: publication reachability."""
import os
import re

from .. import paths
from ..findings import ERROR, Finding

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
KEBAB_DIR = re.compile(r"^[a-z0-9]+(?:[-.][a-z0-9]+)*$")

#: Characters the published site can serve in a path. The site resolves both
#: /docs/{document} and /docs/{path}/media/{file} with the parameter pinned to
#: ^[a-zA-Z0-9/._-]+$, so a name using anything else is unreachable there no
#: matter how correct it is here.
SERVABLE = re.compile(r"^[A-Za-z0-9/._-]+$")
UNSERVABLE = re.compile(r"[^A-Za-z0-9/._-]")

#: Readable names for the characters this actually catches.
CHARACTER_NAMES = {" ": "a space", ",": "a comma", "#": "a hash",
                   "?": "a question mark", "%": "a percent sign",
                   "&": "an ampersand", "'": "an apostrophe", '"': "a quote"}

RULE = "N-KEBAB"
DIR_RULE = "N-KEBAB-DIR"
ROUTE = "P-ROUTE"


def exempt(base):
    return base.startswith("toc") or base == "README.md"


def check_kebab(index, path, source):
    base = os.path.basename(path)
    if not exempt(base) and not KEBAB.match(base):
        yield Finding(ERROR, RULE, path, "new document names use lowercase kebab-case")


def check_directory(index, path, source):
    """New directory names must be lowercase kebab-case.

    Only new ones. Renaming an existing directory such as platform/HAL/ would
    break dozens of links for a cosmetic gain, so the legacy names stay and are
    listed under [naming] in docscheck.toml.

    That list is load-bearing rather than cosmetic. The rule is scoped to added
    files, but this check walks every component of the path, so without it
    adding *any* file inside a legacy directory reports the directory - a
    finding the change cannot act on and the rule never meant to raise.
    """
    for part in os.path.dirname(path).split("/")[1:]:
        if index.legacy_directory(part):
            continue
        if not KEBAB_DIR.match(part):
            yield Finding(ERROR, DIR_RULE, path,
                          f"directory name is not lowercase kebab-case: {part}")
            return


def check_route(index):
    """A file whose published URL the site cannot serve.

    Reachability is not a naming preference. The site pins both document and
    media route parameters to ``^[a-zA-Z0-9/._-]+$``, so a path containing
    anything else answers 404 forever while looking entirely healthy from
    here: the file is committed, the importer imports it, the sitemap lists
    it. Measured on the published site, three documents carrying a comma and
    twenty media files carrying a space were in exactly that state.

    Deliberately not folded into N-KEBAB. That rule is about house style and
    is skipped for generated trees, on the sound reasoning that one generator
    defect becomes hundreds of findings in its output. This is not style — an
    unreachable page is a defect wherever it came from — so it needs to be
    visible in generated output too. If a generator ever does produce them by
    the hundred, add P-ROUTE to that class's aggregate_rules rather than
    silencing it.
    """
    for path in sorted(index.files):
        relative = path[len(paths.DOCS) + 1:] \
            if path.startswith(paths.DOCS + "/") else path
        if SERVABLE.match(relative):
            continue
        offending = sorted(set(UNSERVABLE.findall(relative)))
        described = ", ".join(
            CHARACTER_NAMES.get(character, repr(character))
            for character in offending)
        yield Finding(ERROR, ROUTE, path,
                      f"the published URL cannot contain {described}")
