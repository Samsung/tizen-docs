### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## PixelBuffer Class

PixelBuffer is a class that represents a buffer of pixels.

```csharp
public class PixelBuffer : Tizen.UI.NObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; PixelBuffer
### Constructors

<a name='Tizen.UI.PixelBuffer.PixelBuffer(int,int,Tizen.UI.PixelFormat)'></a>

## PixelBuffer(int, int, PixelFormat) Constructor

Initializes a new instance of the PixelBuffer class with the specified width, height, and pixel format.

```csharp
public PixelBuffer(int width, int height, Tizen.UI.PixelFormat pixelFormat);
```
#### Parameters

<a name='Tizen.UI.PixelBuffer.PixelBuffer(int,int,Tizen.UI.PixelFormat).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the pixel buffer.

<a name='Tizen.UI.PixelBuffer.PixelBuffer(int,int,Tizen.UI.PixelFormat).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The height of the pixel buffer.

<a name='Tizen.UI.PixelBuffer.PixelBuffer(int,int,Tizen.UI.PixelFormat).pixelFormat'></a>

`pixelFormat` [PixelFormat](Tizen.UI.PixelFormat.md 'Tizen.UI.PixelFormat')

The pixel format of the pixel buffer.

<a name='Tizen.UI.PixelBuffer.PixelBuffer(System.IntPtr,bool)'></a>

## PixelBuffer(IntPtr, bool) Constructor

Initializes a new instance of the PixelBuffer class with the specified handle and whether it owns the handle or not.

```csharp
public PixelBuffer(System.IntPtr handle, bool ownsHandle);
```
#### Parameters

<a name='Tizen.UI.PixelBuffer.PixelBuffer(System.IntPtr,bool).handle'></a>

`handle` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The handle of the pixel buffer.

<a name='Tizen.UI.PixelBuffer.PixelBuffer(System.IntPtr,bool).ownsHandle'></a>

`ownsHandle` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether the pixel buffer owns the handle or not.
### Properties

<a name='Tizen.UI.PixelBuffer.Height'></a>

## PixelBuffer.Height Property

Gets the height of the pixel buffer in pixels.

```csharp
public int Height { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.PixelBuffer.PixelFormat'></a>

## PixelBuffer.PixelFormat Property

Gets the pixel format of the pixel buffer.

```csharp
public Tizen.UI.PixelFormat PixelFormat { get; }
```

#### Property Value
[PixelFormat](Tizen.UI.PixelFormat.md 'Tizen.UI.PixelFormat')

<a name='Tizen.UI.PixelBuffer.Width'></a>

## PixelBuffer.Width Property

Gets the width of the pixel buffer in pixels.

```csharp
public int Width { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Methods

<a name='Tizen.UI.PixelBuffer.Convert(Tizen.UI.PixelBuffer)'></a>

## PixelBuffer.Convert(PixelBuffer) Method

Converts the pixel buffer to a pixel data and releases the object of the pixel buffer.  
This handle is left empty. Any other handles that keep a reference to this object will be left with no buffer. Trying to access it will return null.

```csharp
public static Tizen.UI.PixelData Convert(Tizen.UI.PixelBuffer pixelBuffer);
```
#### Parameters

<a name='Tizen.UI.PixelBuffer.Convert(Tizen.UI.PixelBuffer).pixelBuffer'></a>

`pixelBuffer` [PixelBuffer](Tizen.UI.PixelBuffer.md 'Tizen.UI.PixelBuffer')

A pixel buffer.

#### Returns
[PixelData](Tizen.UI.PixelData.md 'Tizen.UI.PixelData')  
A new PixelData that takes ownership of the buffer of the pixelBuffer.

### Remarks
Buffer ownership was transfer to PixelData

<a name='Tizen.UI.PixelBuffer.Export()'></a>

## PixelBuffer.Export() Method

Copies the data from this pixel buffer into a new PixelData object, which could be used for uploading to a texture.

```csharp
public Tizen.UI.PixelData Export();
```

#### Returns
[PixelData](Tizen.UI.PixelData.md 'Tizen.UI.PixelData')  
The pixel data.

<a name='Tizen.UI.PixelBuffer.GetBuffer()'></a>

## PixelBuffer.GetBuffer() Method

Gets the buffer of the pixel buffer.

```csharp
public System.IntPtr GetBuffer();
```

#### Returns
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')  
The buffer of the pixel buffer.

<a name='Tizen.UI.PixelBuffer.Resize(int,int)'></a>

## PixelBuffer.Resize(int, int) Method

Resizes the buffer to the given dimensions.

```csharp
public void Resize(int width, int height);
```
#### Parameters

<a name='Tizen.UI.PixelBuffer.Resize(int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The new width.

<a name='Tizen.UI.PixelBuffer.Resize(int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The new height.






