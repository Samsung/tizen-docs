### [Tizen.UI.Skia](Tizen.UI.Skia.md 'Tizen.UI.Skia')

## CustomRenderingView Class

[CustomRenderingView](Tizen.UI.Skia.CustomRenderingView.md 'Tizen.UI.Skia.CustomRenderingView') is an abstract class that provides a base for custom views that need to render their content using SkiaSharp.

```csharp
public abstract class CustomRenderingView : Tizen.UI.ImageView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ImageView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageView 'Tizen.UI.ImageView') &#129106; CustomRenderingView

Derived  
&#8627; [SKCanvasView](Tizen.UI.Skia.SKCanvasView.md 'Tizen.UI.Skia.SKCanvasView')
### Methods

<a name='Tizen.UI.Skia.CustomRenderingView.Invalidate()'></a>

## CustomRenderingView.Invalidate() Method

Invalidates the view and requests a redraw.

```csharp
public void Invalidate();
```
### Events

<a name='Tizen.UI.Skia.CustomRenderingView.PaintSurface'></a>

## CustomRenderingView.PaintSurface Event

Occurs when the view needs to be painted.

```csharp
public event EventHandler&lt;SKPaintSurfaceEventArgs> PaintSurface;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






























