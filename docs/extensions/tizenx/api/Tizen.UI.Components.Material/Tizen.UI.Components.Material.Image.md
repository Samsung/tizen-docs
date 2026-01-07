### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Image Class

Image is a control for displaying an image resource.

```csharp
public class Image : Tizen.UI.ImageView
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ImageView &#129106; Image

Derived  
&#8627; [AnimatedImage](Tizen.UI.Components.Material.AnimatedImage.md 'Tizen.UI.Components.Material.AnimatedImage')  
&#8627; [LottieImage](Tizen.UI.Components.Material.LottieImage.md 'Tizen.UI.Components.Material.LottieImage')
### Constructors

<a name='Tizen.UI.Components.Material.Image.Image()'></a>

## Image() Constructor

Creates an instance of an Image.

```csharp
public Image();
```

<a name='Tizen.UI.Components.Material.Image.Image(string)'></a>

## Image(string) Constructor

Creates an instance of an Image.

```csharp
public Image(string resourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Image.Image(string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')
### Methods

<a name='Tizen.UI.Components.Material.Image.SetDesiredTextureSize(float,float)'></a>

## Image.SetDesiredTextureSize(float, float) Method

(Not implemented) Sets the desired texture size.

```csharp
public void SetDesiredTextureSize(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Image.SetDesiredTextureSize(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired width of the texture.

<a name='Tizen.UI.Components.Material.Image.SetDesiredTextureSize(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired height of the texture.

<a name='Tizen.UI.Components.Material.Image.SetMaskingMode(Tizen.UI.ImageMaskingMode)'></a>

## Image.SetMaskingMode(ImageMaskingMode) Method

Sets the masking mode for the ImageVisual.

```csharp
public void SetMaskingMode(Tizen.UI.ImageMaskingMode mode);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Image.SetMaskingMode(Tizen.UI.ImageMaskingMode).mode'></a>

`mode` Tizen.UI.ImageMaskingMode

The masking mode to use.

<a name='Tizen.UI.Components.Material.Image.SetPixelArea(Tizen.UI.Rect)'></a>

## Image.SetPixelArea(Rect) Method

Sets the image area to be displayed.  
It is a rectangular area.  
The first two elements indicate the top-left position of the area, and the last two elements are the areas of the width and the height respectively.  
If not specified, the default value is UIRect (0.0, 0.0, 1.0, 1.0), i.e., the entire area of the image.  
For normal quad images only.

```csharp
public void SetPixelArea(Tizen.UI.Rect area);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Image.SetPixelArea(Tizen.UI.Rect).area'></a>

`area` Tizen.UI.Rect














































