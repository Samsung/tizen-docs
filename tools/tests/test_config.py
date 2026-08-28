"""Configuration loading, glob translation and severity resolution.

The glob translator gets its own tests because it is the component most likely
to fail silently: a pattern that quietly stops matching turns an exemption into
noise, or worse, turns a check off.
"""
import pytest

from tizendocs.config import Config, compile_glob

DOUBLE_STAR = [
    ("docs/**/api/**", "docs/api/x.html", True),
    ("docs/**/api/**", "docs/a/b/api/x.html", True),
    ("docs/**/api/**", "docs/a/api/b/c.html", True),
    ("docs/**/api/**", "docs/apix/y.md", False),
    ("docs/**/api/**", "docs/a/apiz/x.md", False),
    ("docs/**/*.autogen.md", "docs/x.autogen.md", True),
    ("docs/**/*.autogen.md", "docs/a/b.autogen.md", True),
    ("docs/**/*.autogen.md", "docs/a/b.md", False),
    ("docs/a/api/*/latest/**", "docs/a/api/common/latest/g.html", True),
    ("docs/a/api/*/latest/**", "docs/a/api/common/10.0/g.html", False),
    ("docs/**/api/[0-9]*.[0-9]*/**", "docs/w/api/10.0/x.html", True),
    ("docs/**/api/[0-9]*.[0-9]*/**", "docs/w/api/latest/x.html", False),
]


@pytest.mark.parametrize("pattern,path,expected", DOUBLE_STAR)
def test_glob_translation(pattern, path, expected):
    assert bool(compile_glob(pattern).match(path)) is expected


def test_star_does_not_cross_a_separator():
    assert not compile_glob("docs/*.md").match("docs/a/b.md")


def config(**kwargs):
    return Config(kwargs, source="test")


def test_classify_takes_the_first_match():
    """Order is the mechanism that rescues a hand-written page living under an
    api/ directory from the generated class."""
    cfg = config(classes=[
        {"id": "api-handwritten", "match": ["docs/a/api/keep.md"]},
        {"id": "generated", "match": ["docs/**/api/**"], "skip_rules": ["D-*"]},
    ])
    assert cfg.classify("docs/a/api/keep.md").id == "api-handwritten"
    assert cfg.classify("docs/a/api/other.md").id == "generated"
    assert not cfg.skips("docs/a/api/keep.md", "D-H1")
    assert cfg.skips("docs/a/api/other.md", "D-H1")


def test_exempt_existence_considers_every_class_not_just_the_first():
    """A versioned API route is both generated content and published
    elsewhere; the first-match rule must not lose the second fact."""
    cfg = config(classes=[
        {"id": "generated", "match": ["docs/**/api/**"]},
        {"id": "published-elsewhere", "match": ["docs/**/api/*/latest/**"],
         "link_policy": "exempt-existence"},
    ])
    assert cfg.classify("docs/a/api/c/latest/x.html").id == "generated"
    assert cfg.exempt_existence("docs/a/api/c/latest/x.html")
    assert not cfg.exempt_existence("docs/a/api/c/10.0/x.html")


def test_optional_patterns_are_recorded():
    cfg = config(classes=[{"id": "generated",
                           "match": ["docs/**/api/**", "?docs/**/wiki/**"]}])
    entry = cfg.classes[0]
    assert entry.patterns == ["docs/**/api/**", "docs/**/wiki/**"]
    assert entry.optional == {"docs/**/wiki/**"}
    assert entry.matches("docs/a/wiki/x.md")


def test_severity_supports_globs_and_a_default():
    cfg = config(rules={"L-*": "warn", "L-BROKEN": "error"})
    assert cfg.severity("L-BROKEN", "ERROR") in {"WARN", "ERROR"}
    assert cfg.severity("T-ORPHAN", "ERROR") == "ERROR"
    assert cfg.severity("L-CASE", "ERROR") == "WARN"


def test_only_rules_inverts_the_skip_list():
    cfg = config(classes=[{"id": "xml", "match": ["docs/t.xml"],
                           "only_rules": ["T-XML"]}])
    assert not cfg.skips("docs/t.xml", "T-XML")
    assert cfg.skips("docs/t.xml", "L-BROKEN")


def test_missing_file_yields_an_empty_config():
    from tizendocs import config as module
    cfg = module.load(path="/nonexistent/docscheck.toml")
    assert cfg.source == "" and cfg.classes == []


def test_legacy_directories_default_to_empty():
    """A file without [naming] must not exempt anything."""
    assert Config({}).legacy_directories == ()
    assert not Config({}).legacy_directory("HAL")


def test_legacy_directory_matches_exact_names_only():
    """Substring matching here would exempt far more than intended."""
    config = Config({"naming": {"legacy_directories": ["HAL"]}})
    assert config.legacy_directory("HAL")
    assert not config.legacy_directory("hal")
    assert not config.legacy_directory("HALO")
    assert not config.legacy_directory("my-HAL")
