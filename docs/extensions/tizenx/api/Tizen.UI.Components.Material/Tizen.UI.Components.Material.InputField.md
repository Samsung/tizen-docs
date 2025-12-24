### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## InputField Class

A single-line text input control that supports various text editing features.

```csharp
public class InputField : Tizen.UI.View,
Tizen.UI.IText,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextEditable,
Tizen.UI.ITextPadding,
Tizen.UI.Components.IDecoratableText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; InputField

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText'), [Tizen.UI.ITextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment 'Tizen.UI.ITextAlignment'), [Tizen.UI.ITextEditable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextEditable 'Tizen.UI.ITextEditable'), [Tizen.UI.ITextPadding](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextPadding 'Tizen.UI.ITextPadding'), [Tizen.UI.Components.IDecoratableText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText 'Tizen.UI.Components.IDecoratableText')
### Constructors

<a name='Tizen.UI.Components.Material.InputField.InputField()'></a>

## InputField() Constructor

Constructs an InputField.

```csharp
public InputField();
```

<a name='Tizen.UI.Components.Material.InputField.InputField(Tizen.UI.Components.Material.InputFieldVariables)'></a>

## InputField(InputFieldVariables) Constructor

Constructs an InputField.

```csharp
public InputField(Tizen.UI.Components.Material.InputFieldVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.InputField(Tizen.UI.Components.Material.InputFieldVariables).variables'></a>

`variables` [InputFieldVariables](Tizen.UI.Components.Material.InputFieldVariables.md 'Tizen.UI.Components.Material.InputFieldVariables')
### Properties

<a name='Tizen.UI.Components.Material.InputField.AdjustedFontSizeScale'></a>

## InputField.AdjustedFontSizeScale Property

Gets the adjusted font size scale used for rendering after applying all constraints,  
including the current [MinimumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputField.MinimumFontSizeScale'), [MaximumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputField.MaximumFontSizeScale'),  
and system font size scale adjustments.

```csharp
public float AdjustedFontSizeScale { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If [MinimumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputField.MinimumFontSizeScale') is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputField.MaximumFontSizeScale')  
(an inverted range), the [MinimumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputField.MinimumFontSizeScale') value takes precedence  
and is used as the adjusted scale.

<a name='Tizen.UI.Components.Material.InputField.ClearFocusOnExecutionKey'></a>

## InputField.ClearFocusOnExecutionKey Property

Whether to clear focus when getting a return key pressed.

```csharp
public bool ClearFocusOnExecutionKey { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.CursorPosition'></a>

## InputField.CursorPosition Property

Gets or sets the cursor position.

```csharp
public int CursorPosition { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.InputField.FontFamily'></a>

## InputField.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputField.FontSize'></a>

## InputField.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputField.FontSizeScale'></a>

## InputField.FontSizeScale Property

Gets or sets the scaling value of the font size.

```csharp
public float FontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputField.FontSlant'></a>

## InputField.FontSlant Property

Gets or sets the font style weight such as [Tizen.UI.FontSlant.Italic](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontSlant.Italic 'Tizen.UI.FontSlant.Italic').

```csharp
public Tizen.UI.FontSlant FontSlant { get; set; }
```

#### Property Value
[Tizen.UI.FontSlant](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontSlant 'Tizen.UI.FontSlant')

<a name='Tizen.UI.Components.Material.InputField.FontWeight'></a>

## InputField.FontWeight Property

Gets or sets the font style weight such as [Tizen.UI.FontWeight.Bold](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWeight.Bold 'Tizen.UI.FontWeight.Bold').

```csharp
public Tizen.UI.FontWeight FontWeight { get; set; }
```

#### Property Value
[Tizen.UI.FontWeight](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWeight 'Tizen.UI.FontWeight')

<a name='Tizen.UI.Components.Material.InputField.FontWidth'></a>

## InputField.FontWidth Property

Gets or sets the font style width such as [FontStyleWidth.Condensed](https://docs.microsoft.com/en-us/dotnet/api/FontStyleWidth.Condensed 'FontStyleWidth.Condensed').

```csharp
public Tizen.UI.FontWidth FontWidth { get; set; }
```

#### Property Value
[Tizen.UI.FontWidth](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWidth 'Tizen.UI.FontWidth')

<a name='Tizen.UI.Components.Material.InputField.HorizontalAlignment'></a>

## InputField.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements [HorizontalAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment.HorizontalAlignment 'Tizen.UI.ITextAlignment.HorizontalAlignment')

#### Property Value
[Tizen.UI.TextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextAlignment 'Tizen.UI.TextAlignment')

<a name='Tizen.UI.Components.Material.InputField.InputColor'></a>

## InputField.InputColor Property

Gets or sets the input color for the text will be added to the input area from now on.

```csharp
public Tizen.UI.Color InputColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.InputFontFamily'></a>

## InputField.InputFontFamily Property

Gets or sets the input font family for the text will be added to the input area from now on.

```csharp
public string InputFontFamily { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputField.InputFontSize'></a>

## InputField.InputFontSize Property

Gets or sets the input font size for the text will be added to the input area from now on.

```csharp
public float InputFontSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputField.InputFontSlant'></a>

## InputField.InputFontSlant Property

Gets or sets the input font style weight such as [Tizen.UI.FontSlant.Italic](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontSlant.Italic 'Tizen.UI.FontSlant.Italic') for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontSlant InputFontSlant { get; set; }
```

#### Property Value
[Tizen.UI.FontSlant](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontSlant 'Tizen.UI.FontSlant')

<a name='Tizen.UI.Components.Material.InputField.InputFontWeight'></a>

## InputField.InputFontWeight Property

Gets or sets the input font style weight such as [Tizen.UI.FontWeight.Bold](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWeight.Bold 'Tizen.UI.FontWeight.Bold') for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWeight InputFontWeight { get; set; }
```

#### Property Value
[Tizen.UI.FontWeight](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWeight 'Tizen.UI.FontWeight')

<a name='Tizen.UI.Components.Material.InputField.InputFontWidth'></a>

## InputField.InputFontWidth Property

Gets or sets the input font style width such as [FontStyleWidth.Condensed](https://docs.microsoft.com/en-us/dotnet/api/FontStyleWidth.Condensed 'FontStyleWidth.Condensed') for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWidth InputFontWidth { get; set; }
```

#### Property Value
[Tizen.UI.FontWidth](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWidth 'Tizen.UI.FontWidth')

<a name='Tizen.UI.Components.Material.InputField.InputMethodContext'></a>

## InputField.InputMethodContext Property

Gets the input method context.

```csharp
public Tizen.UI.InputMethodContext InputMethodContext { get; }
```

Implements [InputMethodContext](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextEditable.InputMethodContext 'Tizen.UI.ITextEditable.InputMethodContext')

#### Property Value
[Tizen.UI.InputMethodContext](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.InputMethodContext 'Tizen.UI.InputMethodContext')

<a name='Tizen.UI.Components.Material.InputField.IsEditable'></a>

## InputField.IsEditable Property

Gets or sets whether the text can be edited.

```csharp
public bool IsEditable { get; set; }
```

Implements [IsEditable](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextEditable.IsEditable 'Tizen.UI.ITextEditable.IsEditable')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.IsMarkupEnabled'></a>

## InputField.IsMarkupEnabled Property

Gets or sets whether the text should be marked up with the HTML tags.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.MaximumFontSizeScale'></a>

## InputField.MaximumFontSizeScale Property

Gets or sets the maximum allowable font size scale.

```csharp
public float MaximumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is less than [MinimumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputField.MinimumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.AdjustedFontSizeScale 'Tizen.UI.Components.Material.InputField.AdjustedFontSizeScale') will follow the minimum value.

<a name='Tizen.UI.Components.Material.InputField.MaximumLength'></a>

## InputField.MaximumLength Property

Gets or sets the maximum length of the text.

```csharp
public int MaximumLength { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.InputField.MinimumFontSizeScale'></a>

## InputField.MinimumFontSizeScale Property

Gets or sets the minimum allowable font size scale.

```csharp
public float MinimumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputField.MaximumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.AdjustedFontSizeScale 'Tizen.UI.Components.Material.InputField.AdjustedFontSizeScale') will follow this minimum value.

<a name='Tizen.UI.Components.Material.InputField.Outline'></a>

## InputField.Outline Property

Gets or sets the outline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Outline> Outline { get; set; }
```

Implements [Outline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Outline 'Tizen.UI.Components.IDecoratableText.Outline')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Outline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Outline 'Tizen.UI.Outline')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputField.PasswordMode'></a>

## InputField.PasswordMode Property

Gets or sets the password mode.

```csharp
public Tizen.UI.HiddenInputMode PasswordMode { get; set; }
```

#### Property Value
[Tizen.UI.HiddenInputMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.HiddenInputMode 'Tizen.UI.HiddenInputMode')

<a name='Tizen.UI.Components.Material.InputField.PlaceholderText'></a>

## InputField.PlaceholderText Property

Gets or sets the placeholder text.

```csharp
public string PlaceholderText { get; set; }
```

Implements [PlaceholderText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextEditable.PlaceholderText 'Tizen.UI.ITextEditable.PlaceholderText')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputField.PlaceholderTextColor'></a>

## InputField.PlaceholderTextColor Property

Gets or sets the placeholder text color.

```csharp
public Tizen.UI.Color PlaceholderTextColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.SelectedText'></a>

## InputField.SelectedText Property

Gets the currently selected text.

```csharp
public string SelectedText { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputField.SelectedTextIndex'></a>

## InputField.SelectedTextIndex Property

Gets the index range of the currently selected text.

```csharp
public Tizen.UI.Components.ClosedRange&lt;int> SelectedTextIndex { get; }
```

#### Property Value
[Tizen.UI.Components.ClosedRange&lt;](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ClosedRange-1 'Tizen.UI.Components.ClosedRange`1')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ClosedRange-1 'Tizen.UI.Components.ClosedRange`1')

<a name='Tizen.UI.Components.Material.InputField.SelectionEnabled'></a>

## InputField.SelectionEnabled Property

Gets or sets whether the text selection is enabled.

```csharp
public bool SelectionEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.ShowPlaceholderTextOnFocus'></a>

## InputField.ShowPlaceholderTextOnFocus Property

Whether to keep showing the placeholder when the field is focused.

```csharp
public bool ShowPlaceholderTextOnFocus { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.Strikethrough'></a>

## InputField.Strikethrough Property

Gets or sets the strike through style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Strikethrough> Strikethrough { get; set; }
```

Implements [Strikethrough](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Strikethrough 'Tizen.UI.Components.IDecoratableText.Strikethrough')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Strikethrough](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Strikethrough 'Tizen.UI.Strikethrough')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputField.SystemFontFamilyEnabled'></a>

## InputField.SystemFontFamilyEnabled Property

Gets or sets whether the [FontFamily](Tizen.UI.Components.Material.InputField.md#Tizen.UI.Components.Material.InputField.FontFamily 'Tizen.UI.Components.Material.InputField.FontFamily') should be determined based on the system settings.

```csharp
public bool SystemFontFamilyEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.SystemFontSizeScaleEnabled'></a>

## InputField.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputField.Text'></a>

## InputField.Text Property

Gets or sets the text to display in the UTF-8 format.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputField.TextColor'></a>

## InputField.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.TextOverflow'></a>

## InputField.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')

<a name='Tizen.UI.Components.Material.InputField.TextShadow'></a>

## InputField.TextShadow Property

Gets or sets the drop shadow for the text.

```csharp
public System.Nullable&lt;Tizen.UI.TextShadow> TextShadow { get; set; }
```

Implements [TextShadow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.TextShadow 'Tizen.UI.Components.IDecoratableText.TextShadow')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.TextShadow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextShadow 'Tizen.UI.TextShadow')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputField.Underline'></a>

## InputField.Underline Property

Gets or sets the underline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Underline> Underline { get; set; }
```

Implements [Underline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Underline 'Tizen.UI.Components.IDecoratableText.Underline')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Underline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Underline 'Tizen.UI.Underline')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputField.VerticalAlignment'></a>

## InputField.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements [VerticalAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment.VerticalAlignment 'Tizen.UI.ITextAlignment.VerticalAlignment')

#### Property Value
[Tizen.UI.TextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextAlignment 'Tizen.UI.TextAlignment')
### Methods

<a name='Tizen.UI.Components.Material.InputField.ClearSelection()'></a>

## InputField.ClearSelection() Method

Clears the current selection.

```csharp
public void ClearSelection();
```

<a name='Tizen.UI.Components.Material.InputField.SelectText(int,int)'></a>

## InputField.SelectText(int, int) Method

Selects the text within the specified index range.

```csharp
public void SelectText(int startIndex, int endIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SelectText(int,int).startIndex'></a>

`startIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The start index of the selection.

<a name='Tizen.UI.Components.Material.InputField.SelectText(int,int).endIndex'></a>

`endIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The end index of the selection.

<a name='Tizen.UI.Components.Material.InputField.SelectWholeText()'></a>

## InputField.SelectWholeText() Method

Selects the whole text.

```csharp
public void SelectWholeText();
```

<a name='Tizen.UI.Components.Material.InputField.SetCursorBlink(float,float)'></a>

## InputField.SetCursorBlink(float, float) Method

Enables cursor blink.

```csharp
public void SetCursorBlink(float interval, float duration);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetCursorBlink(float,float).interval'></a>

`interval` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The interval between blinks.

<a name='Tizen.UI.Components.Material.InputField.SetCursorBlink(float,float).duration'></a>

`duration` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The duration of each blink.

<a name='Tizen.UI.Components.Material.InputField.SetCursorColor(Tizen.UI.Color)'></a>

## InputField.SetCursorColor(Color) Method

Sets the cursor color.

```csharp
public void SetCursorColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetCursorColor(Tizen.UI.Color).color'></a>

`color` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.SetCursorWidth(int)'></a>

## InputField.SetCursorWidth(int) Method

Sets the cursor width.

```csharp
public void SetCursorWidth(int width);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetCursorWidth(int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the cursor.

<a name='Tizen.UI.Components.Material.InputField.SetFontVariation(string,float)'></a>

## InputField.SetFontVariation(string, float) Method

Sets Font Variation with string tag.

```csharp
public void SetFontVariation(string tag, float value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetFontVariation(string,float).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag of font variation.

<a name='Tizen.UI.Components.Material.InputField.SetFontVariation(string,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of font variation.

<a name='Tizen.UI.Components.Material.InputField.SetInputFilter(string,string)'></a>

## InputField.SetInputFilter(string, string) Method

Set input filter.

```csharp
public void SetInputFilter(string include, string exclude=null);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetInputFilter(string,string).include'></a>

`include` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A regular expression in the set of characters to be accepted.

<a name='Tizen.UI.Components.Material.InputField.SetInputFilter(string,string).exclude'></a>

`exclude` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A regular expression in the set of characters to be rejected.

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle)'></a>

## InputField.SetInputMethodActionButtonTitle(ActionButtonTitle) Method

Sets the input method's action button title.

```csharp
public void SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle actionButtonTitle);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle).actionButtonTitle'></a>

`actionButtonTitle` [Tizen.UI.ActionButtonTitle](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ActionButtonTitle 'Tizen.UI.ActionButtonTitle')

The title of the action button.

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodCapitalMode(Tizen.UI.AutoCapital)'></a>

## InputField.SetInputMethodCapitalMode(AutoCapital) Method

Sets the input method's capital mode.

```csharp
public void SetInputMethodCapitalMode(Tizen.UI.AutoCapital capitalMode);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodCapitalMode(Tizen.UI.AutoCapital).capitalMode'></a>

`capitalMode` [Tizen.UI.AutoCapital](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoCapital 'Tizen.UI.AutoCapital')

The capital mode of the input method.

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodPanelType(Tizen.UI.PanelLayout)'></a>

## InputField.SetInputMethodPanelType(PanelLayout) Method

Sets the input method's panel layout.

```csharp
public void SetInputMethodPanelType(Tizen.UI.PanelLayout panelLayout);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetInputMethodPanelType(Tizen.UI.PanelLayout).panelLayout'></a>

`panelLayout` [Tizen.UI.PanelLayout](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.PanelLayout 'Tizen.UI.PanelLayout')

The panel layout of the input method.

<a name='Tizen.UI.Components.Material.InputField.SetSecondaryCursorColor(Tizen.UI.Color)'></a>

## InputField.SetSecondaryCursorColor(Color) Method

Sets the secondary cursor color.

```csharp
public void SetSecondaryCursorColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetSecondaryCursorColor(Tizen.UI.Color).color'></a>

`color` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.SetSelectionColor(Tizen.UI.Color)'></a>

## InputField.SetSelectionColor(Color) Method

Sets the selection area color.

```csharp
public void SetSelectionColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetSelectionColor(Tizen.UI.Color).color'></a>

`color` [Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandleImage(string,string)'></a>

## InputField.SetSelectionHandleImage(string, string) Method

Sets the selection handle images.

```csharp
public void SetSelectionHandleImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandleImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandleImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandlePressedImage(string,string)'></a>

## InputField.SetSelectionHandlePressedImage(string, string) Method

Sets the pressed selection handle images.

```csharp
public void SetSelectionHandlePressedImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandlePressedImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.Material.InputField.SetSelectionHandlePressedImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.Material.InputField.SetTextPadding(Tizen.UI.Thickness)'></a>

## InputField.SetTextPadding(Thickness) Method

Sets the padding for the text within the view.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputField.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` [Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

The padding thickness.

Implements [SetTextPadding(Thickness)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextPadding.SetTextPadding#Tizen_UI_ITextPadding_SetTextPadding_Tizen_UI_Thickness_ 'Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness)')

<a name='Tizen.UI.Components.Material.InputField.UnsetCursorBlink()'></a>

## InputField.UnsetCursorBlink() Method

Disables the cursor blink.

```csharp
public void UnsetCursorBlink();
```
### Events

<a name='Tizen.UI.Components.Material.InputField.AnchorClicked'></a>

## InputField.AnchorClicked Event

Occurs when the anchor is clicked in markup.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.AnchorClickedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AnchorClickedEventArgs 'Tizen.UI.AnchorClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.InputField.CursorMoved'></a>

## InputField.CursorMoved Event

Occurs when the cursor moved.

```csharp
public event EventHandler CursorMoved;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputField.KeyPressed'></a>

## InputField.KeyPressed Event

Occurs when any key is pressed.

```csharp
public event EventHandler&lt;string> KeyPressed;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.InputField.MaximumLengthReached'></a>

## InputField.MaximumLengthReached Event

Occurs when the text has reached to the specified maximum length.

```csharp
public event EventHandler MaximumLengthReached;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputField.SelectionChanged'></a>

## InputField.SelectionChanged Event

Occurs when the seledction changed.

```csharp
public event EventHandler SelectionChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputField.SelectionCleared'></a>

## InputField.SelectionCleared Event

Occurs when the selection is cleared.

```csharp
public event EventHandler SelectionCleared;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputField.SelectionStarted'></a>

## InputField.SelectionStarted Event

Occurs when the selection is started.

```csharp
public event EventHandler SelectionStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputField.TextChanged'></a>

## InputField.TextChanged Event

Occurs when the text is changed.

```csharp
public event EventHandler TextChanged;
```

Implements [TextChanged](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextEditable.TextChanged 'Tizen.UI.ITextEditable.TextChanged')

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')













































