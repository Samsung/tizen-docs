### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Swatch Class

Represents a color swatch generated from a [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette').  
  
A swatch contains a color, its population in the image, and suitable text colors for use over the swatch's color.

```csharp
public sealed class Swatch
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Swatch
### Constructors

<a name='Tizen.UI.Components.Swatch.Swatch(int,int)'></a>

## Swatch(int, int) Constructor

Initializes a new instance of the [Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch') class from an ARGB color value.

```csharp
public Swatch(int colorValue, int population);
```
#### Parameters

<a name='Tizen.UI.Components.Swatch.Swatch(int,int).colorValue'></a>

`colorValue` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The ARGB color value.

<a name='Tizen.UI.Components.Swatch.Swatch(int,int).population'></a>

`population` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The population of the color in the image.

<a name='Tizen.UI.Components.Swatch.Swatch(int,int,int,int)'></a>

## Swatch(int, int, int, int) Constructor

Initializes a new instance of the [Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch') class from RGB components.

```csharp
public Swatch(int r, int g, int b, int population);
```
#### Parameters

<a name='Tizen.UI.Components.Swatch.Swatch(int,int,int,int).r'></a>

`r` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The red component (0-255).

<a name='Tizen.UI.Components.Swatch.Swatch(int,int,int,int).g'></a>

`g` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The green component (0-255).

<a name='Tizen.UI.Components.Swatch.Swatch(int,int,int,int).b'></a>

`b` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The blue component (0-255).

<a name='Tizen.UI.Components.Swatch.Swatch(int,int,int,int).population'></a>

`population` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The population of the color in the image.

<a name='Tizen.UI.Components.Swatch.Swatch(Tizen.UI.Color,int)'></a>

## Swatch(Color, int) Constructor

Initializes a new instance of the [Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch') class.

```csharp
public Swatch(Tizen.UI.Color color, int population);
```
#### Parameters

<a name='Tizen.UI.Components.Swatch.Swatch(Tizen.UI.Color,int).color'></a>

`color` Tizen.UI.Color

The color of the swatch.

<a name='Tizen.UI.Components.Swatch.Swatch(Tizen.UI.Color,int).population'></a>

`population` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The population of the color in the image.
### Properties

<a name='Tizen.UI.Components.Swatch.BodyTextColor'></a>

## Swatch.BodyTextColor Property

Gets a text color that is suitable for use as a body text over this swatch's color.

```csharp
public Tizen.UI.Color BodyTextColor { get; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Swatch.Color'></a>

## Swatch.Color Property

Gets the color of this swatch.

```csharp
public Tizen.UI.Color Color { get; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Swatch.Population'></a>

## Swatch.Population Property

Gets the population of this color in the image.

```csharp
public int Population { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Swatch.TitleTextColor'></a>

## Swatch.TitleTextColor Property

Gets a text color that is suitable for use as a title text over this swatch's color.

```csharp
public Tizen.UI.Color TitleTextColor { get; }
```

#### Property Value
Tizen.UI.Color


























































