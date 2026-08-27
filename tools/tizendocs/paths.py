"""Repository-root discovery and link-target resolution.

Every path this package handles is repository-relative and POSIX-separated,
for example ``docs/application/index.md``. Callers may pass absolute or
cwd-relative paths; :func:`normalize` converts them.
"""
import os

DOCS = "docs"


def repo_root():
    """Return the repository root, discovered by walking up from this file.

    The previous implementation hardcoded ``DOCS = "docs"`` as a *relative*
    path, so running it from inside ``docs/`` silently checked nothing and
    exited successfully. Anchoring on ``__file__`` removes that failure mode.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(here, DOCS)) and os.path.isdir(os.path.join(here, "tools")):
            return here
        parent = os.path.dirname(here)
        if parent == here:
            # Fall back to the cwd so the tool still runs in a partial checkout.
            return os.getcwd()
        here = parent


def to_posix(path):
    return path.replace(os.sep, "/")


def normalize(path, root):
    """Return *path* as a POSIX repository-relative path."""
    absolute = path if os.path.isabs(path) else os.path.join(os.getcwd(), path)
    try:
        relative = os.path.relpath(absolute, root)
    except ValueError:  # different drive on Windows
        return to_posix(path)
    return to_posix(relative)


def resolve(source, raw):
    """Resolve a link target found in *source* to a repository-relative path.

    A leading ``/`` means the published site root, which is the ``docs/``
    directory - not the filesystem root.
    """
    if raw.startswith("/"):
        joined = os.path.join(DOCS, raw.lstrip("/"))
    elif raw:
        joined = os.path.join(os.path.dirname(source), raw)
    else:
        return source
    return to_posix(os.path.normpath(joined))
