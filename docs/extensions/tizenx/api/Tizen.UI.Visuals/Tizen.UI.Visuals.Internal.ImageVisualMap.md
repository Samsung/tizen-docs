### [Tizen.UI.Visuals.Internal](Tizen.UI.Visuals.Internal.md 'Tizen.UI.Visuals.Internal')

## ImageVisualMap Class

The ImageVisualMap class is a class for setting the properties of the image visual.

```csharp
public class ImageVisualMap : Tizen.UI.Visuals.Internal.RoundedVisualMap
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [VisualMap](Tizen.UI.Visuals.Internal.VisualMap.md 'Tizen.UI.Visuals.Internal.VisualMap') &#129106; [RoundedVisualMap](Tizen.UI.Visuals.Internal.RoundedVisualMap.md 'Tizen.UI.Visuals.Internal.RoundedVisualMap') &#129106; ImageVisualMap

Derived  
&#8627; [NPatchVisualMap](Tizen.UI.Visuals.Internal.NPatchVisualMap.md 'Tizen.UI.Visuals.Internal.NPatchVisualMap')
### Constructors

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.ImageVisualMap()'></a>

## ImageVisualMap() Constructor

Initializes a new instance of the [ImageVisualMap](Tizen.UI.Visuals.Internal.ImageVisualMap.md 'Tizen.UI.Visuals.Internal.ImageVisualMap') class.

```csharp
public ImageVisualMap();
```
### Properties

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.AlphaMaskUrl'></a>

## ImageVisualMap.AlphaMaskUrl Property

Gets or sets the URL of the alpha mask image resource.

```csharp
public string AlphaMaskUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.CropToMask'></a>

## ImageVisualMap.CropToMask Property

Gets or sets a value indicating whether to crop the image to the mask.

```csharp
public bool CropToMask { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.DesiredHeight'></a>

## ImageVisualMap.DesiredHeight Property

Gets or sets the desired image height.<br/>  
If not specified, the actual image height is used.<br/>  
For normal quad images only.<br/>  
Optional.

```csharp
public float DesiredHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.DesiredWidth'></a>

## ImageVisualMap.DesiredWidth Property

Gets or sets the desired image width.<br/>  
If not specified, the actual image width is used.<br/>  
For normal quad images only.<br/>  
Optional.

```csharp
public float DesiredWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.FastTrackUploading'></a>

## ImageVisualMap.FastTrackUploading Property

Gets or sets whether to apply fast track uploading or not.<br/>

```csharp
public bool FastTrackUploading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

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

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.FittingMode'></a>

## ImageVisualMap.FittingMode Property

Gets or sets the fitting mode of the image visual.

```csharp
public Tizen.UI.FittingMode FittingMode { get; set; }
```

#### Property Value
Tizen.UI.FittingMode

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.ImageLoadWithViewSize'></a>

## ImageVisualMap.ImageLoadWithViewSize Property

Gets or sets a value indicating whether the image should be loaded with the view size.

```csharp
public bool ImageLoadWithViewSize { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
`true` if image load with view size; otherwise, `false`.

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.LoadPolicy'></a>

## ImageVisualMap.LoadPolicy Property

Gets or sets the Image Visual image loading policy.<br/>  
It decides if a texture should be loaded immediately after source set or only after the visual is added to the window.

```csharp
public Tizen.UI.ImageLoadPolicy LoadPolicy { get; set; }
```

#### Property Value
Tizen.UI.ImageLoadPolicy

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.MaskContentScale'></a>

## ImageVisualMap.MaskContentScale Property

Gets or sets scale factor to apply to the content image before masking.

```csharp
public float MaskContentScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.MaskingMode'></a>

## ImageVisualMap.MaskingMode Property

Gets or sets whether to apply mask on GPU or not.<br/>

```csharp
public Tizen.UI.ImageMaskingMode MaskingMode { get; set; }
```

#### Property Value
Tizen.UI.ImageMaskingMode

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.OrientationCorrection'></a>

## ImageVisualMap.OrientationCorrection Property

Gets or sets a value indicating whether to correct the image orientation.

```csharp
public bool OrientationCorrection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.PixelArea'></a>

## ImageVisualMap.PixelArea Property

Gets or sets the pixel area of the image visual.

```csharp
public Tizen.UI.Rect PixelArea { get; set; }
```

#### Property Value
Tizen.UI.Rect

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.PreMultipliedAlpha'></a>

## ImageVisualMap.PreMultipliedAlpha Property

Gets or sets the pre-multiplied alpha flag of the image.

```csharp
public bool PreMultipliedAlpha { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.ReleasePolicy'></a>

## ImageVisualMap.ReleasePolicy Property

Gets or sets the Image Visual release policy.<br/>  
It decides if a texture should be released from the cache or kept to reduce the loading time.<br/>

```csharp
public Tizen.UI.ImageReleasePolicy ReleasePolicy { get; set; }
```

#### Property Value
Tizen.UI.ImageReleasePolicy

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.ResourceUrl'></a>

## ImageVisualMap.ResourceUrl Property

Gets or sets the URL of the image resource

```csharp
public string ResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.SynchronousLoading'></a>

## ImageVisualMap.SynchronousLoading Property

Gets or sets a value indicating whether to load the image synchronously.

```csharp
public bool SynchronousLoading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.WrapModeU'></a>

## ImageVisualMap.WrapModeU Property

Gets or sets the horizontal wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeU { get; set; }
```

#### Property Value
Tizen.UI.ImageWrapMode

<a name='Tizen.UI.Visuals.Internal.ImageVisualMap.WrapModeV'></a>

## ImageVisualMap.WrapModeV Property

Gets or sets the vertical wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeV { get; set; }
```

#### Property Value
Tizen.UI.ImageWrapMode


























