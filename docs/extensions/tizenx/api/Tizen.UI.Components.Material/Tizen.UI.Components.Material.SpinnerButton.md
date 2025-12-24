### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## SpinnerButton Class

```csharp
public class SpinnerButton : Tizen.UI.Components.Clickable,
Tizen.UI.Components.IFlexibleText,
Tizen.UI.IText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Tizen.UI.Components.Pressable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Pressable 'Tizen.UI.Components.Pressable') &#129106; [Tizen.UI.Components.Clickable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.Clickable 'Tizen.UI.Components.Clickable') &#129106; SpinnerButton

Implements [Tizen.UI.Components.IFlexibleText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText 'Tizen.UI.Components.IFlexibleText'), [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText')
### Constructors

<a name='Tizen.UI.Components.Material.SpinnerButton.SpinnerButton()'></a>

## SpinnerButton() Constructor

Constructs an instance.

```csharp
public SpinnerButton();
```

<a name='Tizen.UI.Components.Material.SpinnerButton.SpinnerButton(Tizen.UI.Components.Material.SpinnerButtonVariables)'></a>

## SpinnerButton(SpinnerButtonVariables) Constructor

Constructs an instance.

```csharp
public SpinnerButton(Tizen.UI.Components.Material.SpinnerButtonVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.SpinnerButton.SpinnerButton(Tizen.UI.Components.Material.SpinnerButtonVariables).variables'></a>

`variables` [SpinnerButtonVariables](Tizen.UI.Components.Material.SpinnerButtonVariables.md 'Tizen.UI.Components.Material.SpinnerButtonVariables')
### Properties

<a name='Tizen.UI.Components.Material.SpinnerButton.AutoFontSize'></a>

## SpinnerButton.AutoFontSize Property

Gets or sets the auto font size.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements [AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.AutoFontSize 'Tizen.UI.Components.IFlexibleText.AutoFontSize')

#### Property Value
[Tizen.UI.AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoFontSize 'Tizen.UI.AutoFontSize')

<a name='Tizen.UI.Components.Material.SpinnerButton.FontFamily'></a>

## SpinnerButton.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SpinnerButton.FontSize'></a>

## SpinnerButton.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize'), [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.FontSize 'Tizen.UI.Components.IFlexibleText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SpinnerButton.IconMixColor'></a>

## SpinnerButton.IconMixColor Property

Gets or sets the mix color of the icon.

```csharp
public Tizen.UI.Color IconMixColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.SpinnerButton.ItemSpacing'></a>

## SpinnerButton.ItemSpacing Property

Gets or sets the spacing between icon and text.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.SpinnerButton.ModalContent'></a>

## SpinnerButton.ModalContent Property

Gets or sets the modal content to be shown when clicked.

```csharp
public Tizen.UI.Components.IAnchoredModal ModalContent { get; set; }
```

#### Property Value
[Tizen.UI.Components.IAnchoredModal](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal 'Tizen.UI.Components.IAnchoredModal')

<a name='Tizen.UI.Components.Material.SpinnerButton.SystemFontSizeScaleEnabled'></a>

## SpinnerButton.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.SpinnerButton.Text'></a>

## SpinnerButton.Text Property

Gets or sets the text of the tab item.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.SpinnerButton.TextColor'></a>

## SpinnerButton.TextColor Property

Gets or sets the text color of the label.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.SpinnerButton.TextOverflow'></a>

## SpinnerButton.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.TextOverflow 'Tizen.UI.Components.IFlexibleText.TextOverflow')

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')













































