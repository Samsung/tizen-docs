### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## Palette Class

A class that extracts prominent colors from an image.  
  
This is a helper class to extract colors from a Tizen.UI.PixelBuffer  
It can generate a number of selected color swatches based on the image.

```csharp
public class Palette
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Palette
### Properties

<a name='Tizen.UI.Components.Palette.DarkMuted'></a>

## Palette.DarkMuted Property

Gets a dark muted swatch from the image.

```csharp
public Tizen.UI.Components.Swatch DarkMuted { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.DarkVibrant'></a>

## Palette.DarkVibrant Property

Gets a dark vibrant swatch from the image.

```csharp
public Tizen.UI.Components.Swatch DarkVibrant { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.Dominant'></a>

## Palette.Dominant Property

Gets the dominant swatch from the image.

```csharp
public Tizen.UI.Components.Swatch Dominant { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.LightMuted'></a>

## Palette.LightMuted Property

Gets a light muted swatch from the image.

```csharp
public Tizen.UI.Components.Swatch LightMuted { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.LightVibrant'></a>

## Palette.LightVibrant Property

Gets a light vibrant swatch from the image.

```csharp
public Tizen.UI.Components.Swatch LightVibrant { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.Muted'></a>

## Palette.Muted Property

Gets a muted swatch from the image.

```csharp
public Tizen.UI.Components.Swatch Muted { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')

<a name='Tizen.UI.Components.Palette.Swatches'></a>

## Palette.Swatches Property

Gets all of the swatches (colors) extracted from the image.

```csharp
public System.Collections.Generic.IEnumerable&lt;Tizen.UI.Components.Swatch> Swatches { get; }
```

#### Property Value
[System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')

<a name='Tizen.UI.Components.Palette.Vibrant'></a>

## Palette.Vibrant Property

Gets a vibrant swatch from the image.

```csharp
public Tizen.UI.Components.Swatch Vibrant { get; }
```

#### Property Value
[Swatch](Tizen.UI.Components.Swatch.md 'Tizen.UI.Components.Swatch')
### Methods

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer)'></a>

## Palette.Generate(PixelBuffer) Method

Synchronously generates a [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette') from the given Tizen.UI.PixelBuffer.

```csharp
public static Tizen.UI.Components.Palette Generate(Tizen.UI.PixelBuffer buffer);
```
#### Parameters

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer).buffer'></a>

`buffer` Tizen.UI.PixelBuffer

The Tizen.UI.PixelBuffer to generate the palette from.

#### Returns
[Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette')  
The generated [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette').

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float)'></a>

## Palette.Generate(PixelBuffer, float, float, float, float) Method

Synchronously generates a [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette') from a specific region of the given Tizen.UI.PixelBuffer.

```csharp
public static Tizen.UI.Components.Palette Generate(Tizen.UI.PixelBuffer buffer, float regionX, float regionY, float regionWidth, float regionHeight);
```
#### Parameters

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float).buffer'></a>

`buffer` Tizen.UI.PixelBuffer

The Tizen.UI.PixelBuffer to generate the palette from.

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float).regionX'></a>

`regionX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the top-left corner of the region.

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float).regionY'></a>

`regionY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the top-left corner of the region.

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float).regionWidth'></a>

`regionWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the region.

<a name='Tizen.UI.Components.Palette.Generate(Tizen.UI.PixelBuffer,float,float,float,float).regionHeight'></a>

`regionHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the region.

#### Returns
[Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette')  
The generated [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette').

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer)'></a>

## Palette.GenerateAsync(PixelBuffer) Method

Asynchronously generates a [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette') from the given Tizen.UI.PixelBuffer.

```csharp
public static System.Threading.Tasks.Task&lt;Tizen.UI.Components.Palette> GenerateAsync(Tizen.UI.PixelBuffer buffer);
```
#### Parameters

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer).buffer'></a>

`buffer` Tizen.UI.PixelBuffer

The Tizen.UI.PixelBuffer to generate the palette from.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
A task that represents the asynchronous generation operation. The task result contains the generated [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette').

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float)'></a>

## Palette.GenerateAsync(PixelBuffer, float, float, float, float) Method

Asynchronously generates a [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette') from the given Tizen.UI.PixelBuffer.

```csharp
public static System.Threading.Tasks.Task&lt;Tizen.UI.Components.Palette> GenerateAsync(Tizen.UI.PixelBuffer buffer, float regionX, float regionY, float regionWidth, float regionHeight);
```
#### Parameters

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float).buffer'></a>

`buffer` Tizen.UI.PixelBuffer

The Tizen.UI.PixelBuffer to generate the palette from.

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float).regionX'></a>

`regionX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x-coordinate of the top-left corner of the region.

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float).regionY'></a>

`regionY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y-coordinate of the top-left corner of the region.

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float).regionWidth'></a>

`regionWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the region.

<a name='Tizen.UI.Components.Palette.GenerateAsync(Tizen.UI.PixelBuffer,float,float,float,float).regionHeight'></a>

`regionHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the region.

#### Returns
[System.Threading.Tasks.Task&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')[Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task-1 'System.Threading.Tasks.Task`1')  
A task that represents the asynchronous generation operation. The task result contains the generated [Palette](Tizen.UI.Components.Palette.md 'Tizen.UI.Components.Palette').



























































