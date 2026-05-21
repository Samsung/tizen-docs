### [Tizen.UI.Skia](Tizen.UI.Skia.md 'Tizen.UI.Skia')

## SKPaintSurfaceEventArgs Class

Event arguments for [SKCanvasView.PaintSurface](https://docs.microsoft.com/en-us/dotnet/api/SKCanvasView.PaintSurface 'SKCanvasView.PaintSurface').

```csharp
public class SKPaintSurfaceEventArgs
```

Inheritance [System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs') &#129106; SKPaintSurfaceEventArgs
### Constructors

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo)'></a>

## SKPaintSurfaceEventArgs(SKSurface, SKImageInfo) Constructor

Initializes a new instance of the [SKPaintSurfaceEventArgs](Tizen.UI.Skia.SKPaintSurfaceEventArgs.md 'Tizen.UI.Skia.SKPaintSurfaceEventArgs') class.

```csharp
public SKPaintSurfaceEventArgs(SKSurface surface, SKImageInfo info);
```
#### Parameters

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo).surface'></a>

`surface` [SkiaSharp.SKSurface](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKSurface 'SkiaSharp.SKSurface')

The surface that is being painted.

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo).info'></a>

`info` [SkiaSharp.SKImageInfo](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKImageInfo 'SkiaSharp.SKImageInfo')

The image information for the current surface.

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo,SKImageInfo)'></a>

## SKPaintSurfaceEventArgs(SKSurface, SKImageInfo, SKImageInfo) Constructor

Initializes a new instance of the [SKPaintSurfaceEventArgs](Tizen.UI.Skia.SKPaintSurfaceEventArgs.md 'Tizen.UI.Skia.SKPaintSurfaceEventArgs') class.

```csharp
public SKPaintSurfaceEventArgs(SKSurface surface, SKImageInfo info, SKImageInfo rawInfo);
```
#### Parameters

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo,SKImageInfo).surface'></a>

`surface` [SkiaSharp.SKSurface](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKSurface 'SkiaSharp.SKSurface')

The surface that is being painted.

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo,SKImageInfo).info'></a>

`info` [SkiaSharp.SKImageInfo](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKImageInfo 'SkiaSharp.SKImageInfo')

The image information for the current surface.

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.SKPaintSurfaceEventArgs(SKSurface,SKImageInfo,SKImageInfo).rawInfo'></a>

`rawInfo` [SkiaSharp.SKImageInfo](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKImageInfo 'SkiaSharp.SKImageInfo')

The raw image information for the current surface.
### Properties

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.Info'></a>

## SKPaintSurfaceEventArgs.Info Property

Gets the image information for the current surface.

```csharp
public SKImageInfo Info { get; }
```

#### Property Value
[SkiaSharp.SKImageInfo](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKImageInfo 'SkiaSharp.SKImageInfo')

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.RawInfo'></a>

## SKPaintSurfaceEventArgs.RawInfo Property

Gets the raw image information for the current surface.

```csharp
public SKImageInfo RawInfo { get; }
```

#### Property Value
[SkiaSharp.SKImageInfo](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKImageInfo 'SkiaSharp.SKImageInfo')

<a name='Tizen.UI.Skia.SKPaintSurfaceEventArgs.Surface'></a>

## SKPaintSurfaceEventArgs.Surface Property

Gets the surface that is being painted.

```csharp
public SKSurface Surface { get; }
```

#### Property Value
[SkiaSharp.SKSurface](https://docs.microsoft.com/en-us/dotnet/api/SkiaSharp.SKSurface 'SkiaSharp.SKSurface')






























