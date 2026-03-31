### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## ParagraphStyle Class

Represents style settings for paragraph elements in Markdown.

```csharp
public record ParagraphStyle : IEquatable<ParagraphStyle>
```

### Properties

<a name='Tizen.UI.Markdown.ParagraphStyle.Default'></a>

## Default

Gets the default paragraph style configuration.

```csharp
public static ParagraphStyle Default { get; }
```
#### Property Value

ParagraphStyle

<a name='Tizen.UI.Markdown.ParagraphStyle.FontColor'></a>

## FontColor

Gets or initializes the font color for paragraphs.

```csharp
public Color FontColor { get; init; }
```
#### Property Value

Color

<a name='Tizen.UI.Markdown.ParagraphStyle.FontFamily'></a>

## FontFamily

Gets or initializes the font family for paragraphs.

```csharp
public string FontFamily { get; init; }
```
#### Property Value

string

<a name='Tizen.UI.Markdown.ParagraphStyle.FontSize'></a>

## FontSize

Gets or initializes the font size for paragraphs.

```csharp
public float FontSize { get; init; }
```
#### Property Value

float

<a name='Tizen.UI.Markdown.ParagraphStyle.LineHeight'></a>

## LineHeight

Gets or initializes the minimum height of a line in pixels.

```csharp
public float LineHeight { get; init; }
```
#### Property Value

float

<a name='Tizen.UI.Markdown.ParagraphStyle.StrikethroughThickness'></a>

## StrikethroughThickness

Gets or initializes the thickness of the strikethrough.

```csharp
public int StrikethroughThickness { get; init; }
```
#### Property Value

int

