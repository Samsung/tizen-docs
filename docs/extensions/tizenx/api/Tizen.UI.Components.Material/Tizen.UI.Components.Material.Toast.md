### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Toast Class

A toast component that displays a message, it automatically dismisses after a specified duration.

```csharp
public class Toast : Tizen.UI.Layouts.Grid,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup') &#129106; [Tizen.UI.Layouts.Layout](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.Layout 'Tizen.UI.Layouts.Layout') &#129106; [Tizen.UI.Layouts.Grid](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.Grid 'Tizen.UI.Layouts.Grid') &#129106; Toast

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText')
### Constructors

<a name='Tizen.UI.Components.Material.Toast.Toast()'></a>

## Toast() Constructor

Constructs an empty toast.

```csharp
public Toast();
```

<a name='Tizen.UI.Components.Material.Toast.Toast(string)'></a>

## Toast(string) Constructor

Constructs a toast with text.

```csharp
public Toast(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Toast.Toast(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the Toast.

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint)'></a>

## Toast(string, uint) Constructor

Constructs a toast with text and duration.

```csharp
public Toast(string text, uint duration);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the Toast.

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint).duration'></a>

`duration` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The duration for which the Toast is displayed.

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint,Tizen.UI.Components.Material.ToastVariables)'></a>

## Toast(string, uint, ToastVariables) Constructor

Constructs a toast with text, duration and variables.

```csharp
public Toast(string text, uint duration, Tizen.UI.Components.Material.ToastVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint,Tizen.UI.Components.Material.ToastVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display in the Toast.

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint,Tizen.UI.Components.Material.ToastVariables).duration'></a>

`duration` [System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

The duration for which the Toast is displayed.

<a name='Tizen.UI.Components.Material.Toast.Toast(string,uint,Tizen.UI.Components.Material.ToastVariables).variables'></a>

`variables` [ToastVariables](Tizen.UI.Components.Material.ToastVariables.md 'Tizen.UI.Components.Material.ToastVariables')

Custom Toast variables.

<a name='Tizen.UI.Components.Material.Toast.Toast(Tizen.UI.Components.Material.ToastVariables)'></a>

## Toast(ToastVariables) Constructor

Constructs an empty toast.

```csharp
public Toast(Tizen.UI.Components.Material.ToastVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Toast.Toast(Tizen.UI.Components.Material.ToastVariables).variables'></a>

`variables` [ToastVariables](Tizen.UI.Components.Material.ToastVariables.md 'Tizen.UI.Components.Material.ToastVariables')

Custom Toast variables.
### Properties

<a name='Tizen.UI.Components.Material.Toast.Duration'></a>

## Toast.Duration Property

Gets or sets the duration for which the toast is displayed.

```csharp
public uint Duration { get; set; }
```

#### Property Value
[System.UInt32](https://docs.microsoft.com/en-us/dotnet/api/System.UInt32 'System.UInt32')

<a name='Tizen.UI.Components.Material.Toast.FontFamily'></a>

## Toast.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Toast.FontSize'></a>

## Toast.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Toast.ItemSpacing'></a>

## Toast.ItemSpacing Property

Gets or sets the spacing between icon and text.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Toast.Text'></a>

## Toast.Text Property

Gets or sets the text of the toast.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Toast.TextColor'></a>

## Toast.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')
### Methods

<a name='Tizen.UI.Components.Material.Toast.Dismiss()'></a>

## Toast.Dismiss() Method

Dismisses the toast.

```csharp
public void Dismiss();
```

<a name='Tizen.UI.Components.Material.Toast.Post(Tizen.UI.Window)'></a>

## Toast.Post(Window) Method

Post the toast.

```csharp
public void Post(Tizen.UI.Window window=null);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Toast.Post(Tizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')
### Events

<a name='Tizen.UI.Components.Material.Toast.Hidden'></a>

## Toast.Hidden Event

Add and remove hidden event handler.

```csharp
public event EventHandler Hidden;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

### Remarks
This event is raised when the toast is fully dismissed.

<a name='Tizen.UI.Components.Material.Toast.Shown'></a>

## Toast.Shown Event

Add and remove shown event handler.

```csharp
public event EventHandler Shown;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

### Remarks
This event is raised when the toast is fully shown.













































