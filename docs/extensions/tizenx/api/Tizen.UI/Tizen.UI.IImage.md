### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## IImage Interface

The IImage interface provides a common set of properties and methods for image objects.

```csharp
public interface IImage
```

Derived  
&#8627; [ImageView](Tizen.UI.ImageView.md 'Tizen.UI.ImageView')
### Properties

<a name='Tizen.UI.IImage.Border'></a>

## IImage.Border Property

Gets or sets the border of the image.

```csharp
Tizen.UI.Thickness Border { get; set; }
```

#### Property Value
[Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

<a name='Tizen.UI.IImage.CropToMask'></a>

## IImage.CropToMask Property

Gets or sets whether the image should be cropped to its mask.

```csharp
bool CropToMask { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IImage.FittingMode'></a>

## IImage.FittingMode Property

Gets or sets the fitting mode used to scale the image to fit the control.

```csharp
Tizen.UI.FittingMode FittingMode { get; set; }
```

#### Property Value
[FittingMode](Tizen.UI.FittingMode.md 'Tizen.UI.FittingMode')

<a name='Tizen.UI.IImage.IsNinePatchImage'></a>

## IImage.IsNinePatchImage Property

Gets or sets whether the image is a nine-patch image.

```csharp
bool IsNinePatchImage { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.IImage.ResourceUrl'></a>

## IImage.ResourceUrl Property

Gets or sets the resource url of image.

```csharp
string ResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')






