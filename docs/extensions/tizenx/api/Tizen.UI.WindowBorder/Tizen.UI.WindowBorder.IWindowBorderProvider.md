### [Tizen.UI.WindowBorder](Tizen.UI.WindowBorder.md 'Tizen.UI.WindowBorder')

## IWindowBorderProvider Interface

Provides an interface for managing the border of a window.

```csharp
public interface IWindowBorderProvider
```

Derived  
&#8627; [BorderView](Tizen.UI.WindowBorder.BorderView.md 'Tizen.UI.WindowBorder.BorderView')
### Properties

<a name='Tizen.UI.WindowBorder.IWindowBorderProvider.BorderArea'></a>

## IWindowBorderProvider.BorderArea Property

Gets the thickness of the border area.

```csharp
Tizen.UI.Thickness BorderArea { get; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.WindowBorder.IWindowBorderProvider.BorderView'></a>

## IWindowBorderProvider.BorderView Property

Gets the view representing the border.

```csharp
Tizen.UI.View BorderView { get; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.WindowBorder.IWindowBorderProvider.SetTargetWindow(Tizen.UI.Window)'></a>

## IWindowBorderProvider.SetTargetWindow(Window) Method

Sets the target window of the border.

```csharp
void SetTargetWindow(Tizen.UI.Window window);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.IWindowBorderProvider.SetTargetWindow(Tizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The target window.














