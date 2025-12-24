### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Button Class

A [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') component containing single text.

```csharp
public class Button : Tizen.UI.Components.Clickable,
Tizen.UI.IText,
Tizen.UI.Components.IFlexibleText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; Button

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText'), [Tizen.UI.Components.IFlexibleText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText 'Tizen.UI.Components.IFlexibleText')
### Constructors

<a name='Tizen.UI.Components.Material.Button.Button()'></a>

## Button() Constructor

Constructs an empty button.

```csharp
public Button();
```

<a name='Tizen.UI.Components.Material.Button.Button(string)'></a>

## Button(string) Constructor

Constructs a button with text.

```csharp
public Button(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Button.Button(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Button.Button(string,Tizen.UI.Components.Material.ButtonVariables)'></a>

## Button(string, ButtonVariables) Constructor

Constructs a button with text.

```csharp
public Button(string text, Tizen.UI.Components.Material.ButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Button.Button(string,Tizen.UI.Components.Material.ButtonVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Button.Button(string,Tizen.UI.Components.Material.ButtonVariables).variables'></a>

`variables` [ButtonVariables](Tizen.UI.Components.Material.ButtonVariables.md 'Tizen.UI.Components.Material.ButtonVariables')

<a name='Tizen.UI.Components.Material.Button.Button(Tizen.UI.Components.Material.ButtonVariables)'></a>

## Button(ButtonVariables) Constructor

Constructs an empty button.

```csharp
public Button(Tizen.UI.Components.Material.ButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Button.Button(Tizen.UI.Components.Material.ButtonVariables).variables'></a>

`variables` [ButtonVariables](Tizen.UI.Components.Material.ButtonVariables.md 'Tizen.UI.Components.Material.ButtonVariables')
### Properties

<a name='Tizen.UI.Components.Material.Button.AutoFontSize'></a>

## Button.AutoFontSize Property

Gets or sets the auto font size.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements [AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.AutoFontSize 'Tizen.UI.Components.IFlexibleText.AutoFontSize')

#### Property Value
[Tizen.UI.AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoFontSize 'Tizen.UI.AutoFontSize')

<a name='Tizen.UI.Components.Material.Button.FontFamily'></a>

## Button.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Button.FontSize'></a>

## Button.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.FontSize 'Tizen.UI.Components.IFlexibleText.FontSize'), [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Button.IsProgressing'></a>

## Button.IsProgressing Property

Gets or sets whether the progress mode is enabled.

```csharp
public bool IsProgressing { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Button.Padding'></a>

## Button.Padding Property

Gets or sets the padding of button.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.Material.Button.Text'></a>

## Button.Text Property

Gets or sets the text of the button.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Button.TextColor'></a>

## Button.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.Button.TextOverflow'></a>

## Button.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.TextOverflow 'Tizen.UI.Components.IFlexibleText.TextOverflow')

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')
### Methods

<a name='Tizen.UI.Components.Material.Button.GetTouchEffectTarget()'></a>

## Button.GetTouchEffectTarget() Method

Get the target view to apply feedback.

```csharp
public override Tizen.UI.View GetTouchEffectTarget();
```

Implements [GetTouchEffectTarget()](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget 'Tizen.UI.Components.ITouchEffectTarget.GetTouchEffectTarget')

#### Returns
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')













































