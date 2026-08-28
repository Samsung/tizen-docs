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


def test_publication_section_and_reviewed_exception():
    cfg = config(publication={
        "sections": [{"id": "guides", "match": ["docs/guides/**"],
                      "governing_tocs": ["docs/guides/toc.md"]}],
        "exceptions": [{"match": ["docs/guides/legacy.md"],
                        "reason": "migration", "owner": "docs@example.invalid",
                        "review_by": "2027-01-01"}],
        "automatic_landings": ["docs/guides/index.md"],
    })
    assert cfg.publication_section("docs/guides/a.md").id == "guides"
    assert cfg.publication_exception("docs/guides/legacy.md").owner == "docs@example.invalid"
    assert cfg.automatic_landing("docs/guides/index.md")


def test_index_records_every_toc_that_registers_a_target(tmp_path):
    from tizendocs.index import DocsIndex
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "page.md").write_text("# Page\n", encoding="utf-8")
    (tmp_path / "docs" / "toc.md").write_text("# [Page](page.md)\n", encoding="utf-8")
    (tmp_path / "docs" / "toc_other.md").write_text("# [Page](page.md)\n", encoding="utf-8")
    index = DocsIndex(root=str(tmp_path), config=Config({}))
    assert index.toc_target_sources["docs/page.md"] == (
        "docs/toc.md", "docs/toc_other.md")


def test_orphan_requires_a_governing_toc_and_reports_context(tmp_path):
    from tizendocs.checks.toc_checks import check_orphan
    from tizendocs.index import DocsIndex
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "page.md").write_text("# Page\n", encoding="utf-8")
    (tmp_path / "docs" / "toc_all.md").write_text("# [Page](page.md)\n", encoding="utf-8")
    (tmp_path / "docs" / "toc.md").write_text("# Empty\n", encoding="utf-8")
    cfg = Config({"publication": {"sections": [{
        "id": "published", "match": ["docs/**"],
        "governing_tocs": ["docs/toc.md"], "recommended_section": "Guides",
    }]}})
    index = DocsIndex(root=str(tmp_path), config=cfg)
    finding = next(check_orphan(index, "docs/page.md", index.source("docs/page.md")))
    assert finding.data == {
        "governing_tocs": ["docs/toc.md"],
        "registered_tocs": ["docs/toc_all.md"],
        "inbound_links": 0,
        "recommended_section": "Guides",
    }
