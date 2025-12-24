### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageView Class

ImageView is a control for displaying an image resource.

```csharp
public class ImageView : Tizen.UI.View,
Tizen.UI.IImage,
Tizen.UI.Internal.IResourceReadySignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; ImageView

Derived  
&#8627; [LottieAnimationView](Tizen.UI.LottieAnimationView.md 'Tizen.UI.LottieAnimationView')

Implements [IImage](Tizen.UI.IImage.md 'Tizen.UI.IImage'), [Tizen.UI.Internal.IResourceReadySignalHandler](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.IResourceReadySignalHandler 'Tizen.UI.Internal.IResourceReadySignalHandler')
### Constructors

<a name='Tizen.UI.ImageView.ImageView()'></a>

## ImageView() Constructor

Creates an instance of an ImageView.

```csharp
public ImageView();
```
### Properties

<a name='Tizen.UI.ImageView.AlphaMaskUrl'></a>

## ImageView.AlphaMaskUrl Property

Gets or sets the URL of the alpha mask image to apply to the image.

```csharp
public string AlphaMaskUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ImageView.Border'></a>

## ImageView.Border Property

Gets or sets the border of the image.

```csharp
public Tizen.UI.Thickness Border { get; set; }
```

Implements [Border](Tizen.UI.IImage.md#Tizen.UI.IImage.Border 'Tizen.UI.IImage.Border')

#### Property Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.ImageView.CropToMask'></a>

## ImageView.CropToMask Property

Gets or sets whether the image should be cropped to its mask.

```csharp
public bool CropToMask { get; set; }
```

Implements [CropToMask](Tizen.UI.IImage.md#Tizen.UI.IImage.CropToMask 'Tizen.UI.IImage.CropToMask')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ImageView.FittingMode'></a>

## ImageView.FittingMode Property

Gets or sets the fitting mode used to scale the image to fit the control.

```csharp
public Tizen.UI.FittingMode FittingMode { get; set; }
```

Implements [FittingMode](Tizen.UI.IImage.md#Tizen.UI.IImage.FittingMode 'Tizen.UI.IImage.FittingMode')

#### Property Value
[FittingMode](Tizen.UI.FittingMode.md 'Tizen.UI.FittingMode')

<a name='Tizen.UI.ImageView.ImageMultipliedColor'></a>

## ImageView.ImageMultipliedColor Property

Gets or sets the color of the view, which is multiplied by the image view's alpha value.

```csharp
public Tizen.UI.Color ImageMultipliedColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.ImageView.IsNinePatchImage'></a>

## ImageView.IsNinePatchImage Property

Gets or sets whether the image is a nine-patch image.

```csharp
public bool IsNinePatchImage { get; set; }
```

Implements [IsNinePatchImage](Tizen.UI.IImage.md#Tizen.UI.IImage.IsNinePatchImage 'Tizen.UI.IImage.IsNinePatchImage')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ImageView.IsResourceReady'></a>

## ImageView.IsResourceReady Property

Gets a value indicating whether the image is ready to be displayed.

```csharp
public bool IsResourceReady { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ImageView.LoadingPlaceholderUrl'></a>

## ImageView.LoadingPlaceholderUrl Property

The LoadingPlaceholderUrl property specifies the URL of the image to display while the main image is being loaded.

```csharp
public string LoadingPlaceholderUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ImageView.LoadingStatus'></a>

## ImageView.LoadingStatus Property

Gets the loading status of the image.

```csharp
public Tizen.UI.ImageLoadingStatus LoadingStatus { get; }
```

#### Property Value
[ImageLoadingStatus](Tizen.UI.ImageLoadingStatus.md 'Tizen.UI.ImageLoadingStatus')

<a name='Tizen.UI.ImageView.PreMultipliedAlpha'></a>

## ImageView.PreMultipliedAlpha Property

Gets or sets whether the image should be pre-multiplied by its alpha channel.

```csharp
public bool PreMultipliedAlpha { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ImageView.ResourceUrl'></a>

## ImageView.ResourceUrl Property

Gets or sets the URL of the image to display.

```csharp
public virtual string ResourceUrl { get; set; }
```

Implements [ResourceUrl](Tizen.UI.IImage.md#Tizen.UI.IImage.ResourceUrl 'Tizen.UI.IImage.ResourceUrl')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ImageView.SynchronousLoading'></a>

## ImageView.SynchronousLoading Property

Gets or sets whether the image should be loaded synchronously.

```csharp
public bool SynchronousLoading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.ImageView.Measure(float,float)'></a>

## ImageView.Measure(float, float) Method

Measures the view based on the available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.ImageView.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.ImageView.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The measured size of the view.

<a name='Tizen.UI.ImageView.Pause()'></a>

## ImageView.Pause() Method

Pauses the animated image.

```csharp
public virtual void Pause();
```

<a name='Tizen.UI.ImageView.Play()'></a>

## ImageView.Play() Method

Plays the animated image.

```csharp
public virtual void Play();
```

<a name='Tizen.UI.ImageView.Reload()'></a>

## ImageView.Reload() Method

Reloads the image.

```csharp
public virtual void Reload();
```

<a name='Tizen.UI.ImageView.SetImagePadding(Tizen.UI.Thickness)'></a>

## ImageView.SetImagePadding(Thickness) Method

Sets the padding for the image.

```csharp
public void SetImagePadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.ImageView.SetImagePadding(Tizen.UI.Thickness).thickness'></a>

`thickness` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The thickness of the padding.

<a name='Tizen.UI.ImageView.Stop()'></a>

## ImageView.Stop() Method

Stops the animated image.

```csharp
public virtual void Stop();
```

<a name='Tizen.UI.ImageView.Update()'></a>

## ImageView.Update() Method

The Update method updates the image map and clears the need update map.

```csharp
public void Update();
```
### Events

<a name='Tizen.UI.ImageView.ResourcesLoaded'></a>

## ImageView.ResourcesLoaded Event

Occurs when the resources of the view are loaded.

```csharp
public event EventHandler ResourcesLoaded;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')






