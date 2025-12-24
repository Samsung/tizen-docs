### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## ImageVisual Class

ImageVisual is a class for the image visual.

```csharp
public class ImageVisual : Tizen.UI.Visuals.RoundedVisual
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject') &#129106; [RoundedVisual](Tizen.UI.Visuals.RoundedVisual.md 'Tizen.UI.Visuals.RoundedVisual') &#129106; ImageVisual

Derived  
&#8627; [NPatchVisual](Tizen.UI.Visuals.NPatchVisual.md 'Tizen.UI.Visuals.NPatchVisual')
### Properties

<a name='Tizen.UI.Visuals.ImageVisual.AlphaMaskUrl'></a>

## ImageVisual.AlphaMaskUrl Property

Gets or sets the URL of the alpha mask image resource.

```csharp
public string AlphaMaskUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Visuals.ImageVisual.CropToMask'></a>

## ImageVisual.CropToMask Property

Gets or sets a value indicating whether to crop the image to the mask.

```csharp
public bool CropToMask { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.ImageVisual.DesiredHeight'></a>

## ImageVisual.DesiredHeight Property

Gets or sets the desired image height.<br/>  
If not specified, the actual image height is used.<br/>  
For normal quad images only.<br/>  
Optional.

```csharp
public float DesiredHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.ImageVisual.DesiredWidth'></a>

## ImageVisual.DesiredWidth Property

Gets or sets the desired image width.<br/>  
If not specified, the actual image width is used.<br/>  
For normal quad images only.<br/>  
Optional.

```csharp
public float DesiredWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.ImageVisual.FastTrackUploading'></a>

## ImageVisual.FastTrackUploading Property

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

<a name='Tizen.UI.Visuals.ImageVisual.FittingMode'></a>

## ImageVisual.FittingMode Property

Gets or sets the fitting mode of the image visual.

```csharp
public Tizen.UI.FittingMode FittingMode { get; set; }
```

#### Property Value
[Tizen.UI.FittingMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FittingMode 'Tizen.UI.FittingMode')

<a name='Tizen.UI.Visuals.ImageVisual.ImageLoadWithViewSize'></a>

## ImageVisual.ImageLoadWithViewSize Property

Gets or sets a value indicating whether the image should be loaded with the view size.

```csharp
public bool ImageLoadWithViewSize { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
`true` if image load with view size; otherwise, `false`.

<a name='Tizen.UI.Visuals.ImageVisual.LoadPolicy'></a>

## ImageVisual.LoadPolicy Property

Gets or sets the Image Visual image loading policy.<br/>  
It decides if a texture should be loaded immediately after source set or only after the visual is added to the window.

```csharp
public Tizen.UI.ImageLoadPolicy LoadPolicy { get; set; }
```

#### Property Value
[Tizen.UI.ImageLoadPolicy](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageLoadPolicy 'Tizen.UI.ImageLoadPolicy')

<a name='Tizen.UI.Visuals.ImageVisual.MaskContentScale'></a>

## ImageVisual.MaskContentScale Property

Gets or sets scale factor to apply to the content image before masking.

```csharp
public float MaskContentScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Visuals.ImageVisual.MaskingMode'></a>

## ImageVisual.MaskingMode Property

Gets or sets whether to apply mask on GPU or not.<br/>

```csharp
public Tizen.UI.ImageMaskingMode MaskingMode { get; set; }
```

#### Property Value
[Tizen.UI.ImageMaskingMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageMaskingMode 'Tizen.UI.ImageMaskingMode')

<a name='Tizen.UI.Visuals.ImageVisual.OrientationCorrection'></a>

## ImageVisual.OrientationCorrection Property

Gets or sets a value indicating whether to correct the image orientation.

```csharp
public bool OrientationCorrection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.ImageVisual.PixelArea'></a>

## ImageVisual.PixelArea Property

Gets or sets the pixel area of the image visual.

```csharp
public Tizen.UI.Rect PixelArea { get; set; }
```

#### Property Value
[Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

<a name='Tizen.UI.Visuals.ImageVisual.PreMultipliedAlpha'></a>

## ImageVisual.PreMultipliedAlpha Property

Gets or sets the pre-multiplied alpha flag of the image.

```csharp
public bool PreMultipliedAlpha { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.ImageVisual.ReleasePolicy'></a>

## ImageVisual.ReleasePolicy Property

Gets or sets the Image Visual release policy.<br/>  
It decides if a texture should be released from the cache or kept to reduce the loading time.<br/>

```csharp
public Tizen.UI.ImageReleasePolicy ReleasePolicy { get; set; }
```

#### Property Value
[Tizen.UI.ImageReleasePolicy](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageReleasePolicy 'Tizen.UI.ImageReleasePolicy')

<a name='Tizen.UI.Visuals.ImageVisual.ResourceUrl'></a>

## ImageVisual.ResourceUrl Property

Gets or sets the URL of the image resource

```csharp
public string ResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Visuals.ImageVisual.SynchronousLoading'></a>

## ImageVisual.SynchronousLoading Property

Gets or sets a value indicating whether to load the image synchronously.

```csharp
public bool SynchronousLoading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.ImageVisual.WrapModeU'></a>

## ImageVisual.WrapModeU Property

Gets or sets the horizontal wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeU { get; set; }
```

#### Property Value
[Tizen.UI.ImageWrapMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageWrapMode 'Tizen.UI.ImageWrapMode')

<a name='Tizen.UI.Visuals.ImageVisual.WrapModeV'></a>

## ImageVisual.WrapModeV Property

Gets or sets the vertical wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeV { get; set; }
```

#### Property Value
[Tizen.UI.ImageWrapMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageWrapMode 'Tizen.UI.ImageWrapMode')
### Methods

<a name='Tizen.UI.Visuals.ImageVisual.Reload()'></a>

## ImageVisual.Reload() Method

Reloads the image resource.

```csharp
public void Reload();
```

<a name='Tizen.UI.Visuals.ImageVisual.Update()'></a>

## ImageVisual.Update() Method

This method updates the visual properties of the image.

```csharp
public void Update();
```

























