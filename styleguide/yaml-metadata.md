# YAML metadata in Tizen documentents

This guideline describes YAML syntax and YAML meta.

The following code shows the YAML metadata in Tizen documents.

## Syntax

All YAML files can optionally begin with `---` and end with `---`. This is part of the YAML format and indicates the start and end of a document.


A dictionary is represented in a simple `key: value` form (the colon must be followed by a space):
```
---
title: YAML metadata in Tizen documentents
author: Anonymous (anonymous@tizen.org)
summary: YAML metadata guideline
keyword: YAML, metadata, Tizen, YAML syntax
redirect: overview
---
```

## YAML elements

The Tizen documentation has various YAML elements.

### title 

There is no title in menu, the title in meta displays displays this title.

```
---
title: YAML metadata in Tizen documentents
---
```

### author

The Tizen repository is in public GitHub so we don't know the exact the document authors.
When the authors are listed, it helps to contact the authors when there are issues.

```
---
author: Anonymous (anonymous@tizen.org)
---
```

### summary

Summary describes what the document is briefly. 

```
---
summary: YAML metadata guideline
---
```

### keyword

Keywords in the document are extracted automatically when a Pull Request is sent. The extracted keywords are words list. Words are split by a space. In other words, it can't detect collocations with space such as "heavy rain", "high temperature", and "have an experience".
However, you can manually insert keywords at the beginning of documents to improve Search Engine Optimization (SEO).

```
---
keyword: Tizen, guidleline, YAML syntax
---
```
In the above example, "YAML syntax" is a kind of collocations.

### redirect

Redirect allows the page jump the other page. For example, there is a representative page, which is a root having lots of children. 
In general, when there is `index.md` in the root directory, and children in subdirectories.

For example, Your  documents exist in folders as the follows:
```
root
├── build
│   └── package.md
├── index.md
└── setup
    └── overview.md
    └── install.md

```

You want to show the overview page, as soon as a user click the root page. In this case, `index.md` has only YAML metadata.

The following YAML meta can fulfill your requirement.

```
---
redirect: setup/overview
---
```

### 

## Related information

- [YAML](https://yaml.org/)
- [YAML Syntax](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)
- [Metadata in Microsoft Word documents](https://blog.martinfenner.org/2015/03/20/metadata-in-microsoft-word-documents/)

