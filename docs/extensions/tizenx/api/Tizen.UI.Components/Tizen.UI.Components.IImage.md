### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## IImage Interface

Interface for image.

```csharp
public interface IImage
```
### Properties

<a name='Tizen.UI.Components.IImage.AlphaMaskUrl'></a>

## IImage.AlphaMaskUrl Property

Gets or sets the URL of the alpha mask image to apply to the image.

```csharp
string AlphaMaskUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.IImage.CropToMask'></a>

## IImage.CropToMask Property

Gets or sets whether the image should be cropped to its mask.

```csharp
bool CropToMask { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.IImage.FittingMode'></a>

## IImage.FittingMode Property

Gets or sets the fitting mode used to scale the image to fit the control.

```csharp
Tizen.UI.ImageLoaderFittingMode FittingMode { get; set; }
```

#### Property Value
[Tizen.UI.ImageLoaderFittingMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageLoaderFittingMode 'Tizen.UI.ImageLoaderFittingMode')

<a name='Tizen.UI.Components.IImage.LoadingStatus'></a>

## IImage.LoadingStatus Property

Gets the loading status of the image.

```csharp
Tizen.UI.ImageLoadingStatus LoadingStatus { get; }
```

#### Property Value
[Tizen.UI.ImageLoadingStatus](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ImageLoadingStatus 'Tizen.UI.ImageLoadingStatus')

<a name='Tizen.UI.Components.IImage.MultipliedColor'></a>

## IImage.MultipliedColor Property

Gets or sets the color of the view, which is multiplied by the image view's alpha value.

```csharp
Tizen.UI.Color MultipliedColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.IImage.ResourceUrl'></a>

## IImage.ResourceUrl Property

Gets or sets the URL of the image to display.

```csharp
string ResourceUrl { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.IImage.SynchronousLoading'></a>

## IImage.SynchronousLoading Property

Gets or sets whether the image should be loaded synchronously.

```csharp
bool SynchronousLoading { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Components.IImage.Reload()'></a>

## IImage.Reload() Method

Reloads the image.

```csharp
void Reload();
```
### Events

<a name='Tizen.UI.Components.IImage.ResourceReady'></a>

## IImage.ResourceReady Event

An event for ResourceReady signal which can be used to subscribe or unsubscribe the event handler.<br/>  
This signal is emitted after all resources required by a control are loaded and ready.<br/>  
Most resources are only loaded when the control is placed on the stage.<br/>

```csharp
event EventHandler ResourceReady;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')


























































