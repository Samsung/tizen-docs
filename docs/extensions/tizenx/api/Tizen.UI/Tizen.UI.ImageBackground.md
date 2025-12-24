### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageBackground Class

ImageBackground is a visual representation of an image resource.

```csharp
public class ImageBackground : Tizen.UI.Background
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Background](Tizen.UI.Background.md 'Tizen.UI.Background') &#129106; ImageBackground
### Properties

<a name='Tizen.UI.ImageBackground.PixelArea'></a>

## ImageBackground.PixelArea Property

Gets or sets the image area to be displayed.  
It is a rectangular area.  
The first two elements indicate the top-left position of the area, and the last two elements are the areas of the width and the height respectively.  
If not specified, the default value is Rect (0.0, 0.0, 1.0, 1.0), i.e., the entire area of the image.  
For normal quad images only.

```csharp
public System.Nullable&lt;Tizen.UI.Rect> PixelArea { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.ImageBackground.ReleasePolicy'></a>

## ImageBackground.ReleasePolicy Property

Gets or sets the release policy for the ImageBackground.

```csharp
public System.Nullable&lt;Tizen.UI.ImageReleasePolicy> ReleasePolicy { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[ImageReleasePolicy](Tizen.UI.ImageReleasePolicy.md 'Tizen.UI.ImageReleasePolicy')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.ImageBackground.SynchronousLoading'></a>

## ImageBackground.SynchronousLoading Property

Gets or sets whether the image should be loaded synchronously.

```csharp
public System.Nullable&lt;bool> SynchronousLoading { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.ImageBackground.Url'></a>

## ImageBackground.Url Property

The URL of the image resource.

```csharp
public string Url { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.ImageBackground.WrapModeU'></a>

## ImageBackground.WrapModeU Property

Gets or sets the horizontal wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeU { get; set; }
```

#### Property Value
[ImageWrapMode](Tizen.UI.ImageWrapMode.md 'Tizen.UI.ImageWrapMode')

<a name='Tizen.UI.ImageBackground.WrapModeV'></a>

## ImageBackground.WrapModeV Property

Gets or sets the vertical wrap mode of the image.

```csharp
public Tizen.UI.ImageWrapMode WrapModeV { get; set; }
```

#### Property Value
[ImageWrapMode](Tizen.UI.ImageWrapMode.md 'Tizen.UI.ImageWrapMode')
### Methods

<a name='Tizen.UI.ImageBackground.BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle)'></a>

## ImageBackground.BuildPropertyMap(PropertyMapHandle) Method

Builds the property map for the visual element.

```csharp
public override void BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle map);
```
#### Parameters

<a name='Tizen.UI.ImageBackground.BuildPropertyMap(Tizen.UI.NativeHandle.PropertyMapHandle).map'></a>

`map` [PropertyMapHandle](Tizen.UI.NativeHandle.PropertyMapHandle.md 'Tizen.UI.NativeHandle.PropertyMapHandle')

The property map handle.






