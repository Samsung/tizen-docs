"""The single finding record every check emits."""
from dataclasses import dataclass

ERROR = "ERROR"
WARN = "WARN"


@dataclass(frozen=True)
class Finding:
    level: str
    rule: str
    path: str
    message: str

    @property
    def is_error(self):
        return self.level == ERROR
