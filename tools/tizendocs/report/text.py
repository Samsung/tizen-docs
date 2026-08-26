"""Human-readable report."""


def render(findings):
    return "".join(
        f"{f.level} {f.rule} {f.path}: {f.message}\n" for f in findings)
