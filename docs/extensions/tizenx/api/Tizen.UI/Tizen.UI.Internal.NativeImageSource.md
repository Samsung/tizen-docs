### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## NativeImageSource Class

Represents a native image source that can be used for rendering.

```csharp
public class NativeImageSource :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; NativeImageSource

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.Internal.NativeImageSource.NativeImageSource(int,int)'></a>

## NativeImageSource(int, int) Constructor

Initializes a new instance of the NativeImageSource class with the specified width and height.

```csharp
public NativeImageSource(int width, int height);
```
#### Parameters

<a name='Tizen.UI.Internal.NativeImageSource.NativeImageSource(int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the image source.

<a name='Tizen.UI.Internal.NativeImageSource.NativeImageSource(int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The height of the image source.
### Methods

<a name='Tizen.UI.Internal.NativeImageSource.AccquiredBuffer(int,int,int)'></a>

## NativeImageSource.AccquiredBuffer(int, int, int) Method

Acquires a buffer from the native image source.

```csharp
public System.IntPtr AccquiredBuffer(out int width, out int height, out int stride);
```
#### Parameters

<a name='Tizen.UI.Internal.NativeImageSource.AccquiredBuffer(int,int,int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the acquired buffer.

<a name='Tizen.UI.Internal.NativeImageSource.AccquiredBuffer(int,int,int).height'></a>

`height` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The height of the acquired buffer.

<a name='Tizen.UI.Internal.NativeImageSource.AccquiredBuffer(int,int,int).stride'></a>

`stride` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The stride of the acquired buffer.

#### Returns
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')  
A pointer to the acquired buffer.

<a name='Tizen.UI.Internal.NativeImageSource.Dispose()'></a>

## NativeImageSource.Dispose() Method

Releases all resources used by the NativeImageSource object.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Internal.NativeImageSource.ReleaseBuffer()'></a>

## NativeImageSource.ReleaseBuffer() Method

Releases the acquired buffer from the native image source.

```csharp
public void ReleaseBuffer();
```




