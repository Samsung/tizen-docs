### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## InputView Class

InputView is a base class for text input controls. It provides common properties and events for text input controls.

```csharp
public abstract class InputView : Tizen.UI.View,
Tizen.UI.IText,
Tizen.UI.ITextPadding,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextEditable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; InputView

Derived  
&#8627; [TextEditor](Tizen.UI.TextEditor.md 'Tizen.UI.TextEditor')  
&#8627; [TextField](Tizen.UI.TextField.md 'Tizen.UI.TextField')

Implements [IText](Tizen.UI.IText.md 'Tizen.UI.IText'), [ITextPadding](Tizen.UI.ITextPadding.md 'Tizen.UI.ITextPadding'), [ITextAlignment](Tizen.UI.ITextAlignment.md 'Tizen.UI.ITextAlignment'), [ITextEditable](Tizen.UI.ITextEditable.md 'Tizen.UI.ITextEditable')
### Properties

<a name='Tizen.UI.InputView.CursorWidth'></a>

## InputView.CursorWidth Property

Gets or sets the width of the cursor.

```csharp
public int CursorWidth { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.InputView.FontFamily'></a>

## InputView.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](Tizen.UI.IText.md#Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.InputView.FontSize'></a>

## InputView.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](Tizen.UI.IText.md#Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.InputView.HorizontalAlignment'></a>

## InputView.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements [HorizontalAlignment](Tizen.UI.ITextAlignment.md#Tizen.UI.ITextAlignment.HorizontalAlignment 'Tizen.UI.ITextAlignment.HorizontalAlignment')

#### Property Value
[TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')

<a name='Tizen.UI.InputView.InputMethodContext'></a>

## InputView.InputMethodContext Property

Gets the InputMethodContext object associated with the InputView.

```csharp
public Tizen.UI.InputMethodContext InputMethodContext { get; }
```

Implements [InputMethodContext](Tizen.UI.ITextEditable.md#Tizen.UI.ITextEditable.InputMethodContext 'Tizen.UI.ITextEditable.InputMethodContext')

#### Property Value
[InputMethodContext](Tizen.UI.InputMethodContext.md 'Tizen.UI.InputMethodContext')

<a name='Tizen.UI.InputView.IsMarkupEnabled'></a>

## InputView.IsMarkupEnabled Property

Gets or sets a value indicating whether the input view enables markup.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.InputView.IsReadOnly'></a>

## InputView.IsReadOnly Property

Gets or sets a value indicating whether the input view is read-only.

```csharp
public bool IsReadOnly { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.InputView.MaxLength'></a>

## InputView.MaxLength Property

Gets or sets the maximum length of the text input.

```csharp
public int MaxLength { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.InputView.PlaceholderText'></a>

## InputView.PlaceholderText Property

Gets or sets the placeholder text of the input view.

```csharp
public string PlaceholderText { get; set; }
```

Implements [PlaceholderText](Tizen.UI.ITextEditable.md#Tizen.UI.ITextEditable.PlaceholderText 'Tizen.UI.ITextEditable.PlaceholderText')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.InputView.PlaceholderTextColor'></a>

## InputView.PlaceholderTextColor Property

Gets or sets the color of the placeholder text.

```csharp
public Tizen.UI.Color PlaceholderTextColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.InputView.PrimaryCursorColor'></a>

## InputView.PrimaryCursorColor Property

Gets or sets the color of the primary cursor.

```csharp
public Tizen.UI.Color PrimaryCursorColor { get; set; }
```

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.InputView.PrimaryCursorPosition'></a>

## InputView.PrimaryCursorPosition Property

Gets or sets the position of the primary cursor.

```csharp
public int PrimaryCursorPosition { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.InputView.ScaledFontSize'></a>

## InputView.ScaledFontSize Property

Gets the scaled font size of the text.

```csharp
public float ScaledFontSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.InputView.SystemFontScaleEnabled'></a>

## InputView.SystemFontScaleEnabled Property

Gets or sets a value indicating whether the system font scale is enabled.

```csharp
public bool SystemFontScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.InputView.Text'></a>

## InputView.Text Property

Gets or sets the text of the input view.

```csharp
public string Text { get; set; }
```

Implements [Text](Tizen.UI.IText.md#Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.InputView.TextColor'></a>

## InputView.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](Tizen.UI.IText.md#Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.InputView.VerticalAlignment'></a>

## InputView.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements [VerticalAlignment](Tizen.UI.ITextAlignment.md#Tizen.UI.ITextAlignment.VerticalAlignment 'Tizen.UI.ITextAlignment.VerticalAlignment')

#### Property Value
[TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')
### Methods

<a name='Tizen.UI.InputView.SetInputMethodSetting(Tizen.UI.InputMethodSetting)'></a>

## InputView.SetInputMethodSetting(InputMethodSetting) Method

Sets the input method settings of the input view.

```csharp
public abstract void SetInputMethodSetting(Tizen.UI.InputMethodSetting inputMethod);
```
#### Parameters

<a name='Tizen.UI.InputView.SetInputMethodSetting(Tizen.UI.InputMethodSetting).inputMethod'></a>

`inputMethod` [InputMethodSetting](Tizen.UI.InputMethodSetting.md 'Tizen.UI.InputMethodSetting')

The input method settings.

<a name='Tizen.UI.InputView.SetTextPadding(Tizen.UI.Thickness)'></a>

## InputView.SetTextPadding(Thickness) Method

Sets the padding of the text.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.InputView.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The padding thickness.

Implements [SetTextPadding(Thickness)](Tizen.UI.ITextPadding.md#Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness) 'Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness)')
### Events

<a name='Tizen.UI.InputView.AnchorClicked'></a>

## InputView.AnchorClicked Event

Occurs when the  the anchor is clicked.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[AnchorClickedEventArgs](Tizen.UI.AnchorClickedEventArgs.md 'Tizen.UI.AnchorClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.InputView.MaxLengthReached'></a>

## InputView.MaxLengthReached Event

Occurs when the maximum length of the text input is reached.

```csharp
public event EventHandler MaxLengthReached;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.InputView.TextChanged'></a>

## InputView.TextChanged Event

Occurs when the Text property changes.

```csharp
public event EventHandler TextChanged;
```

Implements [TextChanged](Tizen.UI.ITextEditable.md#Tizen.UI.ITextEditable.TextChanged 'Tizen.UI.ITextEditable.TextChanged')

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')
### Explicit Interface Implementations

<a name='Tizen.UI.InputView.Tizen.UI.ITextEditable.IsEditable'></a>

## InputView.Tizen.UI.ITextEditable.IsEditable Property

Gets or sets a value indicating whether the text can be editable.

```csharp
bool Tizen.UI.ITextEditable.IsEditable { get; set; }
```

Implements [IsEditable](Tizen.UI.ITextEditable.md#Tizen.UI.ITextEditable.IsEditable 'Tizen.UI.ITextEditable.IsEditable')






