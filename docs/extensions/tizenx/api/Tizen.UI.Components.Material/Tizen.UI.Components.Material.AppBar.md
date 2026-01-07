### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## AppBar Class

The AppBar providing a layout for leading, title, action buttons, and trailing contents.

```csharp
public class AppBar : Tizen.UI.ContentView,
Tizen.UI.Components.IColorProvider,
Tizen.UI.Components.ITitle
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; Tizen.UI.ContentView &#129106; AppBar

Implements Tizen.UI.Components.IColorProvider, Tizen.UI.Components.ITitle
### Constructors

<a name='Tizen.UI.Components.Material.AppBar.AppBar()'></a>

## AppBar() Constructor

Constructs an app bar.

```csharp
public AppBar();
```

<a name='Tizen.UI.Components.Material.AppBar.AppBar(bool,Tizen.UI.Components.Material.AppBarVariables)'></a>

## AppBar(bool, AppBarVariables) Constructor

Constructs an app bar.

```csharp
public AppBar(bool useUniformedContentColor, Tizen.UI.Components.Material.AppBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AppBar.AppBar(bool,Tizen.UI.Components.Material.AppBarVariables).useUniformedContentColor'></a>

`useUniformedContentColor` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.AppBar.AppBar(bool,Tizen.UI.Components.Material.AppBarVariables).variables'></a>

`variables` [AppBarVariables](Tizen.UI.Components.Material.AppBarVariables.md 'Tizen.UI.Components.Material.AppBarVariables')

<a name='Tizen.UI.Components.Material.AppBar.AppBar(Tizen.UI.Components.Material.AppBarVariables)'></a>

## AppBar(AppBarVariables) Constructor

Constructs an app bar.

```csharp
public AppBar(Tizen.UI.Components.Material.AppBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.AppBar.AppBar(Tizen.UI.Components.Material.AppBarVariables).variables'></a>

`variables` [AppBarVariables](Tizen.UI.Components.Material.AppBarVariables.md 'Tizen.UI.Components.Material.AppBarVariables')
### Properties

<a name='Tizen.UI.Components.Material.AppBar.ActionButtons'></a>

## AppBar.ActionButtons Property

Gets a list of action buttons.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> ActionButtons { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')Tizen.UI.View[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Material.AppBar.DominantColor'></a>

## AppBar.DominantColor Property

Gets a color of the object.

```csharp
public Tizen.UI.Color DominantColor { get; set; }
```

Implements DominantColor

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.AppBar.Leading'></a>

## AppBar.Leading Property

Gets or sets a leading content. It will be placed in the head of app bar.

```csharp
public Tizen.UI.View Leading { get; set; }
```

#### Property Value
Tizen.UI.View

### Remarks
There are predefined contents such as [BackButton](Tizen.UI.Components.Material.BackButton.md 'Tizen.UI.Components.Material.BackButton').

<a name='Tizen.UI.Components.Material.AppBar.Title'></a>

## AppBar.Title Property

Gets or sets a title text of [TitleContent](Tizen.UI.Components.Material.AppBar.md#Tizen.UI.Components.Material.AppBar.TitleContent 'Tizen.UI.Components.Material.AppBar.TitleContent') .

```csharp
public string Title { get; set; }
```

Implements Title

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.AppBar.TitleContent'></a>

## AppBar.TitleContent Property

Gets or sets a title content. It will be placed in the center of app bar.

```csharp
public Tizen.UI.View TitleContent { get; set; }
```

#### Property Value
Tizen.UI.View

### Remarks
There are predefined contents such as [Components.Title](https://docs.microsoft.com/en-us/dotnet/api/Components.Title 'Components.Title') and [DoubleTitle](Tizen.UI.Components.Material.DoubleTitle.md 'Tizen.UI.Components.Material.DoubleTitle').

<a name='Tizen.UI.Components.Material.AppBar.Trailing'></a>

## AppBar.Trailing Property

Gets or sets a trailing content. It will be placed in the tail of app bar.

```csharp
public Tizen.UI.View Trailing { get; set; }
```

#### Property Value
Tizen.UI.View

### Remarks
There are predefined contents such as [MoreButton](Tizen.UI.Components.Material.MoreButton.md 'Tizen.UI.Components.Material.MoreButton').

<a name='Tizen.UI.Components.Material.AppBar.UnifiedContentColor'></a>

## AppBar.UnifiedContentColor Property

Gets or sets the color of contents. This color is used when `useUnifiedContentColor` is set to true in constructor.

```csharp
public Tizen.UI.Color UnifiedContentColor { get; }
```

#### Property Value
Tizen.UI.Color
### Events

<a name='Tizen.UI.Components.Material.AppBar.DominantColorChanged'></a>

## AppBar.DominantColorChanged Event

Invoked when the dominant color is changed.

```csharp
public event EventHandler DominantColorChanged;
```

Implements DominantColorChanged

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')














































