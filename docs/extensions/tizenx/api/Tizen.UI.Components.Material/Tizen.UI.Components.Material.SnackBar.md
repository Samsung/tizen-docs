### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## SnackBar Class

A SnackBar component that displays a message with action button.

```csharp
public class SnackBar : Tizen.UI.Layouts.Grid,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Tizen.UI.Layouts.Layout](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.Layout 'Tizen.UI.Layouts.Layout') &#129106; [Tizen.UI.Layouts.Grid](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.Grid 'Tizen.UI.Layouts.Grid') &#129106; SnackBar

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText')
### Constructors

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar()'></a>

## SnackBar() Constructor

Constructs an empty SnackBar.

```csharp
public SnackBar();
```

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string)'></a>

## SnackBar(string) Constructor

Constructs a SnackBar with text.

```csharp
public SnackBar(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the SnackBar.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint)'></a>

## SnackBar(string, uint) Constructor

Constructs a SnackBar with text and duration.

```csharp
public SnackBar(string text, uint duration);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the SnackBar.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint).duration'></a>

`duration` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The duration for which the SnackBar is displayed.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint,Tizen.UI.Components.Material.SnackBarVariables)'></a>

## SnackBar(string, uint, SnackBarVariables) Constructor

Constructs a SnackBar with text, duration and variables.

```csharp
public SnackBar(string text, uint duration, Tizen.UI.Components.Material.SnackBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint,Tizen.UI.Components.Material.SnackBarVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the SnackBar.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint,Tizen.UI.Components.Material.SnackBarVariables).duration'></a>

`duration` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The duration for which the SnackBar is displayed.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(string,uint,Tizen.UI.Components.Material.SnackBarVariables).variables'></a>

`variables` [SnackBarVariables](Tizen.UI.Components.Material.SnackBarVariables.md 'Tizen.UI.Components.Material.SnackBarVariables')

Custom SnackBar variables.

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(Tizen.UI.Components.Material.SnackBarVariables)'></a>

## SnackBar(SnackBarVariables) Constructor

Constructs an empty SnackBar.

```csharp
public SnackBar(Tizen.UI.Components.Material.SnackBarVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SnackBar.SnackBar(Tizen.UI.Components.Material.SnackBarVariables).variables'></a>

`variables` [SnackBarVariables](Tizen.UI.Components.Material.SnackBarVariables.md 'Tizen.UI.Components.Material.SnackBarVariables')

Custom SnackBar variables.
### Properties

<a name='Tizen.UI.Components.Material.SnackBar.ActionButtonText'></a>

## SnackBar.ActionButtonText Property

Gets or sets the action button text of the SnackBar.

```csharp
public string ActionButtonText { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SnackBar.ActionButtonTextColor'></a>

## SnackBar.ActionButtonTextColor Property

Gets or sets the action button text color of the SnackBar.

```csharp
public Tizen.UI.Color ActionButtonTextColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.SnackBar.Duration'></a>

## SnackBar.Duration Property

Gets or sets the duration for which the SnackBar is displayed.

```csharp
public uint Duration { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.Components.Material.SnackBar.FontFamily'></a>

## SnackBar.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SnackBar.FontSize'></a>

## SnackBar.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SnackBar.ItemSpacing'></a>

## SnackBar.ItemSpacing Property

Gets or sets the spacing between text and action button.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SnackBar.Text'></a>

## SnackBar.Text Property

Gets or sets the text of the SnackBar.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SnackBar.TextColor'></a>

## SnackBar.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')
### Methods

<a name='Tizen.UI.Components.Material.SnackBar.Dismiss()'></a>

## SnackBar.Dismiss() Method

Dismisses the SnackBar.

```csharp
public void Dismiss();
```

<a name='Tizen.UI.Components.Material.SnackBar.Post(Tizen.UI.Window)'></a>

## SnackBar.Post(Window) Method

Post the SnackBar.

```csharp
public void Post(Tizen.UI.Window window=null);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SnackBar.Post(Tizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')
### Events

<a name='Tizen.UI.Components.Material.SnackBar.ActionButtonClicked'></a>

## SnackBar.ActionButtonClicked Event

ActionButtonClicked event is raised when the action button is clicked.

```csharp
public event EventHandler&lt;SnackBarActionEventArgs> ActionButtonClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[SnackBarActionEventArgs](Tizen.UI.Components.Material.SnackBarActionEventArgs.md 'Tizen.UI.Components.Material.SnackBarActionEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.SnackBar.Hidden'></a>

## SnackBar.Hidden Event

Add and remove hidden event handler.

```csharp
public event EventHandler Hidden;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

### Remarks
This event is raised when the SnackBar is fully dismissed.

<a name='Tizen.UI.Components.Material.SnackBar.Shown'></a>

## SnackBar.Shown Event

Add and remove shown event handler.

```csharp
public event EventHandler Shown;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

### Remarks
This event is raised when the SnackBar is fully shown.













































