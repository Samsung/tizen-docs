"""Git interrogation for change-scoped runs."""
import subprocess


def changed_files(base, root):
    """Return the paths this working tree changes relative to *base*.

    Two invocations are unioned on purpose: the three-dot form covers a branch
    that has diverged from the base, and the two-dot form covers uncommitted
    work in the tree.
    """
    paths = set()
    for revisions in (f"{base}...HEAD", base):
        result = subprocess.run(
            ("git", "-C", root, "diff", "--name-only", revisions),
            capture_output=True, text=True)
        paths.update(line for line in result.stdout.splitlines() if line)
    return sorted(paths)
