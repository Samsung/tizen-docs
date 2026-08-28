<!--
  Table of contents for this section.

  The developer-site pipeline builds one publication manifest per section
  directory, and the section's toc.md is what it reads to build it. The file
  decides two things: which pages are published, and where they sit in the
  navigation tree (heading depth is navigation depth). A page that no toc.md
  in its own directory lists exists in this repository but has no URL on the
  site.

  `/application/toc_all.md` also links this page, but that file is the
  information-architecture overview for the whole namespace and the site
  pipeline does not read it, so it cannot stand in for this one.

  This directory holds a single page, so this file has a single entry. It is
  worth having anyway. Without it the site had to special-case overview
  directories through a separate hand-written code path, and that path was
  duplicated once per overview section - eight copies that drifted from the
  shared one and from each other.

  Metadata inside the link title is optional. `source:` must name this entry's
  own target; `tags:` and `authors:` override values the site would otherwise
  derive from this repository's git history, so leave them out unless you mean
  to override.
-->

# [Overview](overview.md "source:https://github.com/Samsung/tizen-docs/blob/master/docs/application/dotnet/overview/overview.md")
