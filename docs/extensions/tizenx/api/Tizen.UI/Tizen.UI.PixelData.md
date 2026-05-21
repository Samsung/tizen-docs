### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PixelData Class

The PixelData class provides a way to manage pixel data.

```csharp
public class PixelData : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; PixelData
### Constructors

<a name='Tizen.UI.PixelData.PixelData(byte[],int,int,Tizen.UI.PixelFormat)'></a>

## PixelData(byte[], int, int, PixelFormat) Constructor

Initializes a new instance of the PixelData class with the specified buffer, width, height, and pixel format.

```csharp
public PixelData(byte[] buffer, int width, int height, Tizen.UI.PixelFormat pixelFormat);
```
#### Parameters

<a name='Tizen.UI.PixelData.PixelData(byte[],int,int,Tizen.UI.PixelFormat).buffer'></a>

`buffer` [System.Byte](https://docs.microsoft.com/en-us/dotnet/api/System.Byte 'System.Byte')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The pixel data buffer.

<a name='Tizen.UI.PixelData.PixelData(byte[],int,int,Tizen.UI.PixelFormat).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the pixel data.

<a name='Tizen.UI.PixelData.PixelData(byte[],int,int,Tizen.UI.PixelFormat).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The height of the pixel data.

<a name='Tizen.UI.PixelData.PixelData(byte[],int,int,Tizen.UI.PixelFormat).pixelFormat'></a>

`pixelFormat` [PixelFormat](Tizen.UI.PixelFormat.md 'Tizen.UI.PixelFormat')

The pixel format of the pixel data.

<a name='Tizen.UI.PixelData.PixelData(System.IntPtr,bool)'></a>

## PixelData(IntPtr, bool) Constructor

Initializes a new instance of the PixelData class with the specified handle and whether the handle is owned by the instance.

```csharp
public PixelData(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.PixelData.PixelData(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The native handle of the pixel data.

<a name='Tizen.UI.PixelData.PixelData(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the instance owns the handle.
### Properties

<a name='Tizen.UI.PixelData.Height'></a>

## PixelData.Height Property

Gets the width of the buffer in pixels.

```csharp
public uint Height { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.PixelData.PixelFormat'></a>

## PixelData.PixelFormat Property

Gets the pixel format.

```csharp
public Tizen.UI.PixelFormat PixelFormat { get; }
```

#### Property Value
[PixelFormat](Tizen.UI.PixelFormat.md 'Tizen.UI.PixelFormat')

<a name='Tizen.UI.PixelData.Width'></a>

## PixelData.Width Property

Gets the height of the buffer in pixels.

```csharp
public uint Width { get; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')
### Methods

<a name='Tizen.UI.PixelData.GenerateUrl()'></a>

## PixelData.GenerateUrl() Method

Generates an ImageUrl object from the pixel data.

```csharp
public Tizen.UI.ImageUrl GenerateUrl();
```

#### Returns
[ImageUrl](Tizen.UI.ImageUrl.md 'Tizen.UI.ImageUrl')  
The generated ImageUrl object.






