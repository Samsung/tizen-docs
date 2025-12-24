### [Tizen.UI.WindowBorder](Tizen.UI.WindowBorder.md 'Tizen.UI.WindowBorder')

## BorderView Class

The BorderView class is a view that provides a border for a window.

```csharp
public class BorderView : Tizen.UI.ContentView,
Tizen.UI.WindowBorder.IWindowBorderProvider
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; BorderView

Implements [IWindowBorderProvider](Tizen.UI.WindowBorder.IWindowBorderProvider.md 'Tizen.UI.WindowBorder.IWindowBorderProvider')
### Constructors

<a name='Tizen.UI.WindowBorder.BorderView.BorderView()'></a>

## BorderView() Constructor

Constructor to create a new instance of BorderView class.

```csharp
public BorderView();
```

<a name='Tizen.UI.WindowBorder.BorderView.BorderView(Tizen.UI.ViewTemplate)'></a>

## BorderView(ViewTemplate) Constructor

Constructor to create a new instance of BorderView class.

```csharp
public BorderView(Tizen.UI.ViewTemplate header);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.BorderView.BorderView(Tizen.UI.ViewTemplate).header'></a>

`header` [Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

The header view template of BorderView.

<a name='Tizen.UI.WindowBorder.BorderView.BorderView(Tizen.UI.ViewTemplate,Tizen.UI.ViewTemplate)'></a>

## BorderView(ViewTemplate, ViewTemplate) Constructor

Constructor to create a new instance of BorderView class.

```csharp
public BorderView(Tizen.UI.ViewTemplate header, Tizen.UI.ViewTemplate footer);
```
#### Parameters

<a name='Tizen.UI.WindowBorder.BorderView.BorderView(Tizen.UI.ViewTemplate,Tizen.UI.ViewTemplate).header'></a>

`header` [Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

The header view template of BorderView.

<a name='Tizen.UI.WindowBorder.BorderView.BorderView(Tizen.UI.ViewTemplate,Tizen.UI.ViewTemplate).footer'></a>

`footer` [Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

The footer view template of BorderView.
### Properties

<a name='Tizen.UI.WindowBorder.BorderView.BorderActiveColor'></a>

## BorderView.BorderActiveColor Property

Gets or sets the color of the border when it is active.

```csharp
public Tizen.UI.Color BorderActiveColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.WindowBorder.BorderView.BorderArea'></a>

## BorderView.BorderArea Property

Gets the thickness of the border area.

```csharp
public Tizen.UI.Thickness BorderArea { get; set; }
```

Implements [BorderArea](Tizen.UI.WindowBorder.IWindowBorderProvider.md#Tizen.UI.WindowBorder.IWindowBorderProvider.BorderArea 'Tizen.UI.WindowBorder.IWindowBorderProvider.BorderArea')

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.WindowBorder.BorderView.BorderColor'></a>

## BorderView.BorderColor Property

Gets or sets the color of the border.

```csharp
public Tizen.UI.Color BorderColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.WindowBorder.BorderView.DefaultBorderWidth'></a>

## BorderView.DefaultBorderWidth Property

Gets or sets the default width of the border.

```csharp
public float DefaultBorderWidth { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.WindowBorder.BorderView.EnableOverlayBorder'></a>

## BorderView.EnableOverlayBorder Property

Gets or sets a value indicating whether the overlay border is enabled or not.

```csharp
public bool EnableOverlayBorder { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.WindowBorder.BorderView.FooterTemplate'></a>

## BorderView.FooterTemplate Property

Gets or sets the template used to create the footer of the border.

```csharp
public Tizen.UI.ViewTemplate FooterTemplate { get; }
```

#### Property Value
[Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')

<a name='Tizen.UI.WindowBorder.BorderView.HeaderTemplate'></a>

## BorderView.HeaderTemplate Property

Gets or sets the template used to create the header of the border.

```csharp
public Tizen.UI.ViewTemplate HeaderTemplate { get; }
```

#### Property Value
[Tizen.UI.ViewTemplate](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewTemplate 'Tizen.UI.ViewTemplate')
### Methods

<a name='Tizen.UI.WindowBorder.BorderView.HideOverlayBorder()'></a>

## BorderView.HideOverlayBorder() Method

Hides the overlay border.

```csharp
public void HideOverlayBorder();
```

<a name='Tizen.UI.WindowBorder.BorderView.ShowOverlayBorder()'></a>

## BorderView.ShowOverlayBorder() Method

Shows the overlay border.

```csharp
public void ShowOverlayBorder();
```














