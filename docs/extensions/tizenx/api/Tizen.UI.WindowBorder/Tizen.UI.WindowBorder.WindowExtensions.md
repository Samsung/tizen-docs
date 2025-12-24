### [Tizen.UI.WindowBorder](Tizen.UI.WindowBorder.md 'Tizen.UI.WindowBorder')

## WindowExtensions Class

Provides extension methods for Window border.

```csharp
public static class WindowExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; WindowExtensions
### Methods

<a name='Tizen.UI.WindowBorder.WindowExtensions.ClearBorderView(thisTizen.UI.Window)'></a>

## WindowExtensions.ClearBorderView(this Window) Method

Clears the border view of the window.

```csharp
public static void ClearBorderView(this Tizen.UI.Window window);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.WindowExtensions.ClearBorderView(thisTizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to clear the border view.

<a name='Tizen.UI.WindowBorder.WindowExtensions.GetBorderLayer(thisTizen.UI.Window)'></a>

## WindowExtensions.GetBorderLayer(this Window) Method

Gets the border layer of the window.

```csharp
public static Tizen.UI.Layer GetBorderLayer(this Tizen.UI.Window window);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.WindowExtensions.GetBorderLayer(thisTizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to get the border layer.

#### Returns
[Tizen.UI.Layer](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layer 'Tizen.UI.Layer')  
The border layer of the window.

<a name='Tizen.UI.WindowBorder.WindowExtensions.SetBorderView(thisTizen.UI.Window,Tizen.UI.WindowBorder.IWindowBorderProvider)'></a>

## WindowExtensions.SetBorderView(this Window, IWindowBorderProvider) Method

Sets the border view of the window using the specified [IWindowBorderProvider](Tizen.UI.WindowBorder.IWindowBorderProvider.md 'Tizen.UI.WindowBorder.IWindowBorderProvider').

```csharp
public static void SetBorderView(this Tizen.UI.Window window, Tizen.UI.WindowBorder.IWindowBorderProvider provider);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.WindowExtensions.SetBorderView(thisTizen.UI.Window,Tizen.UI.WindowBorder.IWindowBorderProvider).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to set the border view.

<a name='Tizen.UI.WindowBorder.WindowExtensions.SetBorderView(thisTizen.UI.Window,Tizen.UI.WindowBorder.IWindowBorderProvider).provider'></a>

`provider` [IWindowBorderProvider](Tizen.UI.WindowBorder.IWindowBorderProvider.md 'Tizen.UI.WindowBorder.IWindowBorderProvider')

The [IWindowBorderProvider](Tizen.UI.WindowBorder.IWindowBorderProvider.md 'Tizen.UI.WindowBorder.IWindowBorderProvider') used to create and manage the border view.














