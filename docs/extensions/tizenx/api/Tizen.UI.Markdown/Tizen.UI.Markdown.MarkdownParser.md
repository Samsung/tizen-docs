### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## MarkdownParser Class

Provides a Markdown parser configured with custom pipeline options,
enabling table support and enhanced emphasis handling for Tizen NUI markdown rendering.

```csharp
public static class MarkdownParser
```

### Methods

<a name='Tizen.UI.Markdown.MarkdownParser.MarkdownToPlainText.System.String.'></a>

## MarkdownToPlainText(string)

Converts the given markdown text to plain text.

```csharp
public static string MarkdownToPlainText(string markdown)
```
#### Parameters

`markdown` string

Markdown input string.

#### Returns

string

Plain text.

<a name='Tizen.UI.Markdown.MarkdownParser.Parse.System.String.'></a>

## Parse(string)

Parses the given markdown string into a Markdig MarkdownDocument AST,
using the configured pipeline.

```csharp
public static MarkdownDocument Parse(string markdown)
```
#### Parameters

`markdown` string

The markdown text to parse.

#### Returns

MarkdownDocument

The parsed Markdig.Syntax.MarkdownDocument object.

