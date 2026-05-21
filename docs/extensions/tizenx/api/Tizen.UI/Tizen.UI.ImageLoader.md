### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageLoader Class

Provides a set of methods for loading images and getting their original sizes.

```csharp
public static class ImageLoader
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ImageLoader
### Methods

<a name='Tizen.UI.ImageLoader.GetOriginalImageSize(string,bool)'></a>

## ImageLoader.GetOriginalImageSize(string, bool) Method

Gets the original image size of the specified file.

```csharp
public static Tizen.UI.Size GetOriginalImageSize(string filename, bool orientationCorretion=true);
```
#### Parameters

<a name='Tizen.UI.ImageLoader.GetOriginalImageSize(string,bool).filename'></a>

`filename` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The path to the image file.

<a name='Tizen.UI.ImageLoader.GetOriginalImageSize(string,bool).orientationCorretion'></a>

`orientationCorretion` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether to correct the orientation based on Exif data.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The original image size as a Size struct.

<a name='Tizen.UI.ImageLoader.LoadImage(System.IO.Stream)'></a>

## ImageLoader.LoadImage(Stream) Method

Loads an image from the specified stream into a PixelBuffer object.

```csharp
public static Tizen.UI.PixelBuffer LoadImage(System.IO.Stream stream);
```
#### Parameters

<a name='Tizen.UI.ImageLoader.LoadImage(System.IO.Stream).stream'></a>

`stream` [System.IO.Stream](https://docs.microsoft.com/en-us/dotnet/api/System.IO.Stream 'System.IO.Stream')

The stream containing the image data.

#### Returns
[PixelBuffer](Tizen.UI.PixelBuffer.md 'Tizen.UI.PixelBuffer')  
A PixelBuffer object containing the image data.

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string)'></a>

## ImageLoader.LoadImageFromFile(string) Method

Loads an image from the file into a PixelBuffer object.

```csharp
public static Tizen.UI.PixelBuffer LoadImageFromFile(string url);
```
#### Parameters

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string).url'></a>

`url` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The image file url.

#### Returns
[PixelBuffer](Tizen.UI.PixelBuffer.md 'Tizen.UI.PixelBuffer')

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool)'></a>

## ImageLoader.LoadImageFromFile(string, Size, ImageLoaderFittingMode, ImageLoaderSamplingMode, bool) Method

Loads an image from the file with specific size into a PixelBuffer object.

```csharp
public static Tizen.UI.PixelBuffer LoadImageFromFile(string url, Tizen.UI.Size size, Tizen.UI.ImageLoaderFittingMode fittingMode, Tizen.UI.ImageLoaderSamplingMode samplingMode, bool orientationCorrection);
```
#### Parameters

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool).url'></a>

`url` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The image file url.

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The size of the image.

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool).fittingMode'></a>

`fittingMode` [ImageLoaderFittingMode](Tizen.UI.ImageLoaderFittingMode.md 'Tizen.UI.ImageLoaderFittingMode')

The fitting mode of image.

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool).samplingMode'></a>

`samplingMode` [ImageLoaderSamplingMode](Tizen.UI.ImageLoaderSamplingMode.md 'Tizen.UI.ImageLoaderSamplingMode')

The sampling mode of image.

<a name='Tizen.UI.ImageLoader.LoadImageFromFile(string,Tizen.UI.Size,Tizen.UI.ImageLoaderFittingMode,Tizen.UI.ImageLoaderSamplingMode,bool).orientationCorrection'></a>

`orientationCorrection` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Indicates whether to correct the image orientation

#### Returns
[PixelBuffer](Tizen.UI.PixelBuffer.md 'Tizen.UI.PixelBuffer')






