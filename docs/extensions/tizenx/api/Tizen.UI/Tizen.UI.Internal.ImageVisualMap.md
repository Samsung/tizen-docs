### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## ImageVisualMap Class

ImageVisualMap is a class that represents a property map for the image visual.

```csharp
public class ImageVisualMap :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ImageVisualMap

Derived  
&#8627; [LottieVisualMap](Tizen.UI.Internal.LottieVisualMap.md 'Tizen.UI.Internal.LottieVisualMap')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.Internal.ImageVisualMap.ImageVisualMap()'></a>

## ImageVisualMap() Constructor

Initializes a new instance of the ImageVisualMap class.

```csharp
public ImageVisualMap();
```
### Properties

<a name='Tizen.UI.Internal.ImageVisualMap.AlphaMaskUrl'></a>

## ImageVisualMap.AlphaMaskUrl Property

Gets or sets the URL of the alpha mask image resource.

```csharp
public string AlphaMaskUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Internal.ImageVisualMap.Border'></a>

## ImageVisualMap.Border Property

Gets or sets the border of the image.

```csharp
public Tizen.UI.Thickness Border { get; set; }
```

#### Property Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.Internal.ImageVisualMap.BorderOnly'></a>

## ImageVisualMap.BorderOnly Property

Gets or sets a value indicating whether to draw only the border.

```csharp
public bool BorderOnly { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Internal.ImageVisualMap.CropToMask'></a>

## ImageVisualMap.CropToMask Property

Gets or sets a value indicating whether to crop the image to the mask.

```csharp
public bool CropToMask { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Internal.ImageVisualMap.FittingMode'></a>

## ImageVisualMap.FittingMode Property

Gets or sets the fitting mode of the image.

```csharp
public Tizen.UI.FittingMode FittingMode { get; set; }
```

#### Property Value
[FittingMode](Tizen.UI.FittingMode.md 'Tizen.UI.FittingMode')

<a name='Tizen.UI.Internal.ImageVisualMap.Handle'></a>

## ImageVisualMap.Handle Property

Gets the handle of the property map.

```csharp
public Tizen.UI.NativeHandle.PropertyMapHandle Handle { get; set; }
```

#### Property Value
[PropertyMapHandle](Tizen.UI.NativeHandle.PropertyMapHandle.md 'Tizen.UI.NativeHandle.PropertyMapHandle')

<a name='Tizen.UI.Internal.ImageVisualMap.IsNinePatchImage'></a>

## ImageVisualMap.IsNinePatchImage Property

Gets or sets a value indicating whether the image is a nine-patch image.

```csharp
public bool IsNinePatchImage { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Internal.ImageVisualMap.MultipliedColor'></a>

## ImageVisualMap.MultipliedColor Property

Gets or sets the multiplied color of the image

```csharp
public Tizen.UI.Color MultipliedColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.Internal.ImageVisualMap.OrientationCorrection'></a>

## ImageVisualMap.OrientationCorrection Property

Gets or sets a value indicating whether to correct the image orientation.

```csharp
public bool OrientationCorrection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Internal.ImageVisualMap.ResourceUrl'></a>

## ImageVisualMap.ResourceUrl Property

Gets or sets the URL of the image resource.

```csharp
public string ResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Internal.ImageVisualMap.SynchronousLoading'></a>

## ImageVisualMap.SynchronousLoading Property

Gets or sets a value indicating whether to load the image synchronously.

```csharp
public bool SynchronousLoading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Internal.ImageVisualMap.Dispose()'></a>

## ImageVisualMap.Dispose() Method

Disposes the ImageVisualMap object.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Internal.ImageVisualMap.SetDirty()'></a>

## ImageVisualMap.SetDirty() Method

Sets the map as dirty.

```csharp
public void SetDirty();
```

<a name='Tizen.UI.Internal.ImageVisualMap.SetFastTrackUploading(bool)'></a>

## ImageVisualMap.SetFastTrackUploading(bool) Method

Sets whether to apply fast track uploading or not.<br/>

```csharp
public void SetFastTrackUploading(bool enable);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetFastTrackUploading(bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

### Remarks
If we use fast track uploading feature, It can upload texture without event-thead dependency. But also,<br/>  
 - Texture size is invalid until ResourceReady signal comes.<br/>  
 - Texture cannot be cached (We always try to load new image).<br/>  
 - Seamless visual change didn't supported.<br/>  
 - Alpha masking didn't supported. If you try, It will load as normal case.<br/>  
 - Synchronous loading didn't supported. If you try, It will load as normal case.<br/>  
 - Reload action didn't supported. If you try, It will load as normal case.<br/>  
 - Atlas loading didn't supported. If you try, It will load as normal case.<br/>  
 - Custom shader didn't supported. If you try, It will load as normal case.

<a name='Tizen.UI.Internal.ImageVisualMap.SetMaskingMode(Tizen.UI.ImageMaskingMode)'></a>

## ImageVisualMap.SetMaskingMode(ImageMaskingMode) Method

Sets the masking mode for the ImageVisual.

```csharp
public void SetMaskingMode(Tizen.UI.ImageMaskingMode mode);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetMaskingMode(Tizen.UI.ImageMaskingMode).mode'></a>

`mode` [ImageMaskingMode](Tizen.UI.ImageMaskingMode.md 'Tizen.UI.ImageMaskingMode')

The masking mode to use.

<a name='Tizen.UI.Internal.ImageVisualMap.SetPixelArea(Tizen.UI.Rect)'></a>

## ImageVisualMap.SetPixelArea(Rect) Method

Sets the image area to be displayed.  
It is a rectangular area.  
The first two elements indicate the top-left position of the area, and the last two elements are the areas of the width and the height respectively.  
If not specified, the default value is Rect (0.0, 0.0, 1.0, 1.0), i.e., the entire area of the image.  
For normal quad images only.

```csharp
public void SetPixelArea(Tizen.UI.Rect area);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetPixelArea(Tizen.UI.Rect).area'></a>

`area` [Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')

<a name='Tizen.UI.Internal.ImageVisualMap.SetReleasePolicy(Tizen.UI.ImageReleasePolicy)'></a>

## ImageVisualMap.SetReleasePolicy(ImageReleasePolicy) Method

Sets the release policy for the ImageVisual.

```csharp
public void SetReleasePolicy(Tizen.UI.ImageReleasePolicy releasePolicy);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetReleasePolicy(Tizen.UI.ImageReleasePolicy).releasePolicy'></a>

`releasePolicy` [ImageReleasePolicy](Tizen.UI.ImageReleasePolicy.md 'Tizen.UI.ImageReleasePolicy')

The release policy to be used by the ImageVisual.

<a name='Tizen.UI.Internal.ImageVisualMap.SetWrapModeU(Tizen.UI.ImageWrapMode)'></a>

## ImageVisualMap.SetWrapModeU(ImageWrapMode) Method

Gets or sets the horizontal wrap mode of the image.

```csharp
public void SetWrapModeU(Tizen.UI.ImageWrapMode mode);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetWrapModeU(Tizen.UI.ImageWrapMode).mode'></a>

`mode` [ImageWrapMode](Tizen.UI.ImageWrapMode.md 'Tizen.UI.ImageWrapMode')

<a name='Tizen.UI.Internal.ImageVisualMap.SetWrapModeV(Tizen.UI.ImageWrapMode)'></a>

## ImageVisualMap.SetWrapModeV(ImageWrapMode) Method

Sets the vertical wrap mode of the image.

```csharp
public void SetWrapModeV(Tizen.UI.ImageWrapMode mode);
```
#### Parameters

<a name='Tizen.UI.Internal.ImageVisualMap.SetWrapModeV(Tizen.UI.ImageWrapMode).mode'></a>

`mode` [ImageWrapMode](Tizen.UI.ImageWrapMode.md 'Tizen.UI.ImageWrapMode')
### Events

<a name='Tizen.UI.Internal.ImageVisualMap.UpdateRequired'></a>

## ImageVisualMap.UpdateRequired Event

Occurs when the update is required.

```csharp
public event EventHandler UpdateRequired;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')




