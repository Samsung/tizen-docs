### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TbmSurfaceView Class

The TbmSurfaceView class represents a view that renders a texture using a TBM (Tizen Buffer Manager) surface.

```csharp
public class TbmSurfaceView : Tizen.UI.View
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; TbmSurfaceView
### Constructors

<a name='Tizen.UI.TbmSurfaceView.TbmSurfaceView()'></a>

## TbmSurfaceView() Constructor

Initializes a new instance of the TbmSurfaceView class with the specified width and height.

```csharp
public TbmSurfaceView();
```
### Methods

<a name='Tizen.UI.TbmSurfaceView.SetSource(System.IntPtr)'></a>

## TbmSurfaceView.SetSource(IntPtr) Method

```csharp
public void SetSource(System.IntPtr tbmSurface);
```
#### Parameters

<a name='Tizen.UI.TbmSurfaceView.SetSource(System.IntPtr).tbmSurface'></a>

`tbmSurface` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

### Remarks
It must be called on the UI thread.

<a name='Tizen.UI.TbmSurfaceView.SetSource(Tizen.UI.Internal.NativeImageSource)'></a>

## TbmSurfaceView.SetSource(NativeImageSource) Method

Sets the source of the TbmSurfaceView.

```csharp
public void SetSource(Tizen.UI.Internal.NativeImageSource source);
```
#### Parameters

<a name='Tizen.UI.TbmSurfaceView.SetSource(Tizen.UI.Internal.NativeImageSource).source'></a>

`source` [NativeImageSource](Tizen.UI.Internal.NativeImageSource.md 'Tizen.UI.Internal.NativeImageSource')

The NativeImageSource object to set as the source.

### Remarks
It must be called on the UI thread.

<a name='Tizen.UI.TbmSurfaceView.SetSource(Tizen.UI.Internal.Texture)'></a>

## TbmSurfaceView.SetSource(Texture) Method

Sets the source texture for the TbmSurfaceView.

```csharp
public void SetSource(Tizen.UI.Internal.Texture texture);
```
#### Parameters

<a name='Tizen.UI.TbmSurfaceView.SetSource(Tizen.UI.Internal.Texture).texture'></a>

`texture` [Tizen.UI.Internal.Texture](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.Texture 'Tizen.UI.Internal.Texture')

The new texture to set as the source.

### Remarks
It must be called on the UI thread.




