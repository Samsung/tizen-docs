### [Tizen.UI.Internal](Tizen.UI.Internal.md 'Tizen.UI.Internal')

## WindowExtensions Class

```csharp
public static class WindowExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; WindowExtensions
### Methods

<a name='Tizen.UI.Internal.WindowExtensions.AddFrameRenderedCallback(thisTizen.UI.Window,System.Action_int_,int)'></a>

## WindowExtensions.AddFrameRenderedCallback(this Window, Action&lt;int>, int) Method

Adds a callback function that will be invoked when the frame is rendered.

```csharp
public static void AddFrameRenderedCallback(this Tizen.UI.Window window, System.Action&lt;int> callback, int id);
```
#### Parameters

<a name='Tizen.UI.Internal.WindowExtensions.AddFrameRenderedCallback(thisTizen.UI.Window,System.Action_int_,int).window'></a>

`window` [Window](Tizen.UI.Window.md 'Tizen.UI.Window')

The window instance.

<a name='Tizen.UI.Internal.WindowExtensions.AddFrameRenderedCallback(thisTizen.UI.Window,System.Action_int_,int).callback'></a>

`callback` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The callback function to be invoked.

<a name='Tizen.UI.Internal.WindowExtensions.AddFrameRenderedCallback(thisTizen.UI.Window,System.Action_int_,int).id'></a>

`id` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

A unique identifier for the callback.

### Remarks
A callback is invoked on UI thread(Main thread) and it only called once




