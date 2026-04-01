### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## MarkdownStyle Class

Represents the overall style configuration for Markdown rendering.
This record contains all style settings for different Markdown elements.

```csharp
public record MarkdownStyle : IEquatable<MarkdownStyle>
```

### Properties

<a name='Tizen.UI.Markdown.MarkdownStyle.Code'></a>

## Code

Gets or initializes the code block style settings.

```csharp
public CodeStyle Code { get; init; }
```
#### Property Value

CodeStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Common'></a>

## Common

Gets or initializes the common style settings.

```csharp
public CommonStyle Common { get; init; }
```
#### Property Value

CommonStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Default'></a>

## Default

Gets the default Markdown style configuration.

```csharp
public static MarkdownStyle Default { get; }
```
#### Property Value

MarkdownStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Heading'></a>

## Heading

Gets or initializes the heading style settings.

```csharp
public HeadingStyle Heading { get; init; }
```
#### Property Value

HeadingStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.List'></a>

## List

Gets or initializes the list style settings.

```csharp
public ListStyle List { get; init; }
```
#### Property Value

ListStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Paragraph'></a>

## Paragraph

Gets or initializes the paragraph style settings.

```csharp
public ParagraphStyle Paragraph { get; init; }
```
#### Property Value

ParagraphStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Quote'></a>

## Quote

Gets or initializes the quote style settings.

```csharp
public QuoteStyle Quote { get; init; }
```
#### Property Value

QuoteStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.Table'></a>

## Table

Gets or initializes the table style settings.

```csharp
public TableStyle Table { get; init; }
```
#### Property Value

TableStyle

<a name='Tizen.UI.Markdown.MarkdownStyle.ThematicBreak'></a>

## ThematicBreak

Gets or initializes the thematic break (horizontal rule) style settings.

```csharp
public ThematicBreakStyle ThematicBreak { get; init; }
```
#### Property Value

ThematicBreakStyle

