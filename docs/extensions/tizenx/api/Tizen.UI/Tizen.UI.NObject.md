### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## NObject Class

NObject is a base class for all objects in UI.

```csharp
public abstract class NObject :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; NObject

Derived  
&#8627; [Animation](Tizen.UI.Animation.md 'Tizen.UI.Animation')  
&#8627; [FocusManager](Tizen.UI.FocusManager.md 'Tizen.UI.FocusManager')  
&#8627; [FontClient](Tizen.UI.FontClient.md 'Tizen.UI.FontClient')  
&#8627; [Gesture](Tizen.UI.Gesture.md 'Tizen.UI.Gesture')  
&#8627; [GestureDetector](Tizen.UI.GestureDetector.md 'Tizen.UI.GestureDetector')  
&#8627; [HoverEvent](Tizen.UI.HoverEvent.md 'Tizen.UI.HoverEvent')  
&#8627; [ImageUrl](Tizen.UI.ImageUrl.md 'Tizen.UI.ImageUrl')  
&#8627; [InputMethodContext](Tizen.UI.InputMethodContext.md 'Tizen.UI.InputMethodContext')  
&#8627; [KeyEvent](Tizen.UI.KeyEvent.md 'Tizen.UI.KeyEvent')  
&#8627; [Layer](Tizen.UI.Layer.md 'Tizen.UI.Layer')  
&#8627; [PixelBuffer](Tizen.UI.PixelBuffer.md 'Tizen.UI.PixelBuffer')  
&#8627; [PixelData](Tizen.UI.PixelData.md 'Tizen.UI.PixelData')  
&#8627; [Timer](Tizen.UI.Timer.md 'Tizen.UI.Timer')  
&#8627; [TouchEvent](Tizen.UI.TouchEvent.md 'Tizen.UI.TouchEvent')  
&#8627; [TouchPoint](Tizen.UI.TouchPoint.md 'Tizen.UI.TouchPoint')  
&#8627; [View](Tizen.UI.View.md 'Tizen.UI.View')  
&#8627; [WheelEvent](Tizen.UI.WheelEvent.md 'Tizen.UI.WheelEvent')  
&#8627; [Window](Tizen.UI.Window.md 'Tizen.UI.Window')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.NObject.Handle'></a>

## NObject.Handle Property

Gets the native object handle.

```csharp
public System.IntPtr Handle { get; }
```

#### Property Value
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

<a name='Tizen.UI.NObject.HasOwnership'></a>

## NObject.HasOwnership Property

Gets or sets a flag indicating whether the object owns the native handle.

```csharp
public bool HasOwnership { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.NObject.IsDisposed'></a>

## NObject.IsDisposed Property

Gets a value indicating whether the object has been disposed.

```csharp
public bool IsDisposed { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the object has been disposed, otherwise false.
### Methods

<a name='Tizen.UI.NObject.Dispose()'></a>

## NObject.Dispose() Method

Disposes the object and releases all resources associated with it.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.NObject.GetObjectFromNativeObject(System.IntPtr)'></a>

## NObject.GetObjectFromNativeObject(IntPtr) Method

Gets the managed object corresponding to the specified native object handle.

```csharp
public static Tizen.UI.NObject GetObjectFromNativeObject(System.IntPtr nativeObj);
```
#### Parameters

<a name='Tizen.UI.NObject.GetObjectFromNativeObject(System.IntPtr).nativeObj'></a>

`nativeObj` [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

The native object handle.

#### Returns
[NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')  
The managed object corresponding to the specified native object handle, or null if no managed object corresponds to the native object handle
### Operators

<a name='Tizen.UI.NObject.op_ImplicitSystem.IntPtr(Tizen.UI.NObject)'></a>

## NObject.implicit operator IntPtr(NObject) Operator

Provides an implicit conversion between [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') and [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr').

```csharp
public static System.IntPtr implicit operator IntPtr(Tizen.UI.NObject obj);
```
#### Parameters

<a name='Tizen.UI.NObject.op_ImplicitSystem.IntPtr(Tizen.UI.NObject).obj'></a>

`obj` [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject')

The [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') instance to convert.

#### Returns
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')  
The [System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr') representation of the [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') instance.




