"""The single finding record every check emits.

Each optional field exists because a reviewer or an agent needs it and cannot
derive it from the others:

``line``/``col``
    the minimum needed to attach an inline pull-request comment.
``fix``
    filled in whenever the correction is unambiguous, which turns a finding
    into a one-click suggestion. Its absence is itself information: it means
    the finding needs a human decision.
``syntax``
    whether the reference was Markdown or HTML. This tells a reviewer why
    their own grep missed it.
``cause``
    for reverse-direction rules, the deleted or renamed path responsible, so
    every consequence of one removal can be grouped into a single comment.
"""
from dataclasses import dataclass, field

ERROR = "ERROR"
WARN = "WARN"
NOTE = "NOTE"

#: Most to least severe. Findings are reported and filtered in this order.
LEVELS = (ERROR, WARN, NOTE)


def rank(level):
    return LEVELS.index(level)


@dataclass(frozen=True)
class Finding:
    level: str
    rule: str
    path: str
    message: str
    line: int = 0
    col: int = 0
    fix: str = ""
    syntax: str = ""
    cause: str = ""
    related: tuple = field(default_factory=tuple)

    @property
    def is_error(self):
        return self.level == ERROR

    @property
    def location(self):
        return f"{self.path}:{self.line}" if self.line else self.path

    def as_dict(self):
        data = {"level": self.level, "rule": self.rule, "path": self.path,
                "message": self.message}
        if self.line:
            data["line"] = self.line
            data["col"] = self.col
        for name in ("fix", "syntax", "cause"):
            value = getattr(self, name)
            if value:
                data[name] = value
        if self.related:
            data["related"] = list(self.related)
        return data
