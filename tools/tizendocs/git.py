"""Git interrogation for change-scoped runs."""
import subprocess
from dataclasses import dataclass, field


def _run(root, *argv):
    return subprocess.run(("git", "-C", root, *argv),
                          capture_output=True, text=True)


@dataclass
class Change:
    """What a working tree does to the corpus, relative to a base revision."""

    status: dict = field(default_factory=dict)   # path -> A / M / D / R
    renames: dict = field(default_factory=dict)  # old path -> new path
    before: dict = field(default_factory=dict)   # path -> content at base

    @property
    def paths(self):
        return sorted(self.status)

    @property
    def removed(self):
        """Paths that no longer exist under their old name.

        Deletions and renames are one category here: in both cases every
        inbound reference to the old path is now broken.
        """
        return sorted(path for path, state in self.status.items() if state in "DR")

    def replacement(self, path):
        return self.renames.get(path, "")

    def previous(self, path):
        """The file's content at the base revision, or ``None``."""
        return self.before.get(path)


def describe(base, root):
    """Return a :class:`Change` for *base*...working tree.

    Two invocations are unioned on purpose: the three-dot form covers a branch
    that has diverged from the base, and the two-dot form covers uncommitted
    work. ``-M`` is required rather than optional - this repository's history
    records renames as delete/add pairs, so without it a rename cannot be
    distinguished from a deletion and the tool cannot suggest the new path.
    """
    change = Change()
    for revisions in (f"{base}...HEAD", base):
        result = _run(root, "diff", "--name-status", "-M", revisions)
        for line in result.stdout.splitlines():
            fields = line.split("\t")
            if len(fields) < 2:
                continue
            state = fields[0][0]
            if state == "R" and len(fields) >= 3:
                old, new = fields[1], fields[2]
                change.status[old] = "R"
                change.status[new] = "A"
                change.renames[old] = new
            else:
                change.status.setdefault(fields[1], state)

    # Deleted and renamed files are captured too: a rule that asks what a
    # removal orphaned has to read the references the removed file used to
    # make, and those are not in the working tree any more.
    for path, state in change.status.items():
        if state in "MDR" and path.endswith(".md"):
            shown = _run(root, "show", f"{base}:{path}")
            if shown.returncode == 0:
                change.before[path] = shown.stdout
    return change


def changed_files(base, root):
    """The paths a change touches, for the default per-document rules."""
    return describe(base, root).paths
