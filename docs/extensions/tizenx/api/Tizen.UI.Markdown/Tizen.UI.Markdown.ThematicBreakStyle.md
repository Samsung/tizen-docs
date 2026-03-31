### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## ThematicBreakStyle Class

Represents style settings for thematic break (horizontal rule) elements in Markdown.

```csharp
public record ThematicBreakStyle : IEquatable<ThematicBreakStyle>
```

### Properties

<a name='Tizen.UI.Markdown.ThematicBreakStyle.Color'></a>

## Color

Gets or initializes the color of the thematic break.

```csharp
public Color Color { get; init; }
```
#### Property Value

Color

<a name='Tizen.UI.Markdown.ThematicBreakStyle.Default'></a>

## Default

Gets the default thematic break style configuration.

```csharp
public static ThematicBreakStyle Default { get; }
```
#### Property Value

ThematicBreakStyle

<a name='Tizen.UI.Markdown.ThematicBreakStyle.Margin'></a>

## Margin

Gets or initializes the margin added in pixels to the top and bottom of Block.

```csharp
public int Margin { get; init; }
```
#### Property Value

int

<a name='Tizen.UI.Markdown.ThematicBreakStyle.Thickness'></a>

## Thickness

Gets or initializes the thickness of the thematic break.

```csharp
public int Thickness { get; init; }
```
#### Property Value

int

