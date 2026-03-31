### [Tizen.UI.Markdown](Tizen.UI.Markdown.md 'Tizen.UI.Markdown')

## CommonStyle Class

Represents common style settings used across different Markdown elements.

```csharp
public record CommonStyle : IEquatable<CommonStyle>
```

### Properties

<a name='Tizen.UI.Markdown.CommonStyle.Default'></a>

## Default

Gets the default common style configuration.

```csharp
public static CommonStyle Default { get; }
```
#### Property Value

CommonStyle

<a name='Tizen.UI.Markdown.CommonStyle.Indent'></a>

## Indent

Gets or initializes the indent added in pixels to the left of a Container Block (Quote, List).

```csharp
public int Indent { get; init; }
```
#### Property Value

int

<a name='Tizen.UI.Markdown.CommonStyle.ItemPadding'></a>

## ItemPadding

Gets or initializes the spacing between UI items added to the top container of the view tree.

```csharp
public int ItemPadding { get; init; }
```
#### Property Value

int

<a name='Tizen.UI.Markdown.CommonStyle.Padding'></a>

## Padding

Gets or initializes the padding value.

```csharp
public int Padding { get; init; }
```
#### Property Value

int

