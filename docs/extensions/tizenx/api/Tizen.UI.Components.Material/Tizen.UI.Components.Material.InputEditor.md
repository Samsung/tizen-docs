### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## InputEditor Class

A multi-line text input control that supports various text editing features.

```csharp
public class InputEditor : Tizen.UI.View,
Tizen.UI.IText,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextEditable,
Tizen.UI.ITextPadding,
Tizen.UI.Components.IDecoratableText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; Tizen.UI.View &#129106; InputEditor

Implements Tizen.UI.IText, Tizen.UI.ITextAlignment, Tizen.UI.ITextEditable, Tizen.UI.ITextPadding, Tizen.UI.Components.IDecoratableText
### Constructors

<a name='Tizen.UI.Components.Material.InputEditor.InputEditor()'></a>

## InputEditor() Constructor

Constructs an InputEditor.

```csharp
public InputEditor();
```

<a name='Tizen.UI.Components.Material.InputEditor.InputEditor(Tizen.UI.Components.Material.InputEditorVariables)'></a>

## InputEditor(InputEditorVariables) Constructor

Constructs an InputEditor.

```csharp
public InputEditor(Tizen.UI.Components.Material.InputEditorVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.InputEditor(Tizen.UI.Components.Material.InputEditorVariables).variables'></a>

`variables` [InputEditorVariables](Tizen.UI.Components.Material.InputEditorVariables.md 'Tizen.UI.Components.Material.InputEditorVariables')
### Properties

<a name='Tizen.UI.Components.Material.InputEditor.AdjustedFontSizeScale'></a>

## InputEditor.AdjustedFontSizeScale Property

Gets the adjusted font size scale used for rendering after applying all constraints,  
including the current [MinimumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale'), [MaximumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale'),  
and system font size scale adjustments.

```csharp
public float AdjustedFontSizeScale { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If [MinimumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale') is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale')  
(an inverted range), the [MinimumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale') value takes precedence  
and is used as the adjusted scale.

<a name='Tizen.UI.Components.Material.InputEditor.CursorPosition'></a>

## InputEditor.CursorPosition Property

Gets or sets the cursor position.

```csharp
public int CursorPosition { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.InputEditor.FontFamily'></a>

## InputEditor.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements FontFamily

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputEditor.FontSize'></a>

## InputEditor.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements FontSize

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputEditor.FontSizeScale'></a>

## InputEditor.FontSizeScale Property

Gets or sets the scaling value of the font size.

```csharp
public float FontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputEditor.FontSlant'></a>

## InputEditor.FontSlant Property

Gets or sets the font style weight such as Tizen.UI.FontSlant.Italic.

```csharp
public Tizen.UI.FontSlant FontSlant { get; set; }
```

#### Property Value
Tizen.UI.FontSlant

<a name='Tizen.UI.Components.Material.InputEditor.FontWeight'></a>

## InputEditor.FontWeight Property

Gets or sets the font style weight such as Tizen.UI.FontWeight.Bold.

```csharp
public Tizen.UI.FontWeight FontWeight { get; set; }
```

#### Property Value
Tizen.UI.FontWeight

<a name='Tizen.UI.Components.Material.InputEditor.FontWidth'></a>

## InputEditor.FontWidth Property

Gets or sets the font style width such as Tizen.UI.FontWidth.Condensed.

```csharp
public Tizen.UI.FontWidth FontWidth { get; set; }
```

#### Property Value
Tizen.UI.FontWidth

<a name='Tizen.UI.Components.Material.InputEditor.HorizontalAlignment'></a>

## InputEditor.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements HorizontalAlignment

#### Property Value
Tizen.UI.TextAlignment

<a name='Tizen.UI.Components.Material.InputEditor.InputColor'></a>

## InputEditor.InputColor Property

Gets or sets the input color for the text will be added to the input area from now on.

```csharp
public Tizen.UI.Color InputColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.InputFontFamily'></a>

## InputEditor.InputFontFamily Property

Gets or sets the input font family for the text will be added to the input area from now on.

```csharp
public string InputFontFamily { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputEditor.InputFontSize'></a>

## InputEditor.InputFontSize Property

Gets or sets the input font size for the text will be added to the input area from now on.

```csharp
public float InputFontSize { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.InputEditor.InputFontSlant'></a>

## InputEditor.InputFontSlant Property

Gets or sets the input font style weight such as Tizen.UI.FontSlant.Italic for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontSlant InputFontSlant { get; set; }
```

#### Property Value
Tizen.UI.FontSlant

<a name='Tizen.UI.Components.Material.InputEditor.InputFontWeight'></a>

## InputEditor.InputFontWeight Property

Gets or sets the input font style weight such as Tizen.UI.FontWeight.Bold for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWeight InputFontWeight { get; set; }
```

#### Property Value
Tizen.UI.FontWeight

<a name='Tizen.UI.Components.Material.InputEditor.InputFontWidth'></a>

## InputEditor.InputFontWidth Property

Gets or sets the input font style width such as Tizen.UI.FontWidth.Condensed for the text will be added to the input area from now on..

```csharp
public Tizen.UI.FontWidth InputFontWidth { get; set; }
```

#### Property Value
Tizen.UI.FontWidth

<a name='Tizen.UI.Components.Material.InputEditor.InputMethodContext'></a>

## InputEditor.InputMethodContext Property

Gets the input method context.

```csharp
public Tizen.UI.InputMethodContext InputMethodContext { get; }
```

Implements InputMethodContext

#### Property Value
Tizen.UI.InputMethodContext

<a name='Tizen.UI.Components.Material.InputEditor.IsAbsoluteLineHeight'></a>

## InputEditor.IsAbsoluteLineHeight Property

Gets or sets the line height policy. This value will determine how the line height is calculated.  
If the value is false, the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is false with value 1.0f.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.IsEditable'></a>

## InputEditor.IsEditable Property

Gets or sets whether the text can be edited.

```csharp
public bool IsEditable { get; set; }
```

Implements IsEditable

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.IsMarkupEnabled'></a>

## InputEditor.IsMarkupEnabled Property

Gets or sets whether the text should be marked up with the HTML tags.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.LineHeight'></a>

## InputEditor.LineHeight Property

Gets or sets the minimum line height. If the value is smaller than the natural line height, the natural line height will be used instead.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
This property is treated differently by the [LineHeightPolicy](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy 'LineHeightPolicy'). If the value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative'), the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative') with value 1.0f.

<a name='Tizen.UI.Components.Material.InputEditor.LineWLineBreakModerapMode'></a>

## InputEditor.LineWLineBreakModerapMode Property

Gets or sets the line break mode of the text.

```csharp
public Tizen.UI.LineBreakMode LineWLineBreakModerapMode { get; set; }
```

#### Property Value
Tizen.UI.LineBreakMode

<a name='Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale'></a>

## InputEditor.MaximumFontSizeScale Property

Gets or sets the maximum allowable font size scale.

```csharp
public float MaximumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is less than [MinimumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.AdjustedFontSizeScale 'Tizen.UI.Components.Material.InputEditor.AdjustedFontSizeScale') will follow the minimum value.

<a name='Tizen.UI.Components.Material.InputEditor.MaximumLength'></a>

## InputEditor.MaximumLength Property

Gets or sets the maximum length of the text.

```csharp
public int MaximumLength { get; set; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.InputEditor.MinimumFontSizeScale'></a>

## InputEditor.MinimumFontSizeScale Property

Gets or sets the minimum allowable font size scale.

```csharp
public float MinimumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale 'Tizen.UI.Components.Material.InputEditor.MaximumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.AdjustedFontSizeScale 'Tizen.UI.Components.Material.InputEditor.AdjustedFontSizeScale') will follow this minimum value.

<a name='Tizen.UI.Components.Material.InputEditor.Outline'></a>

## InputEditor.Outline Property

Gets or sets the outline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Outline> Outline { get; set; }
```

Implements Outline

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Outline[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputEditor.PlaceholderText'></a>

## InputEditor.PlaceholderText Property

Gets or sets the placeholder text.

```csharp
public string PlaceholderText { get; set; }
```

Implements PlaceholderText

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputEditor.PlaceholderTextColor'></a>

## InputEditor.PlaceholderTextColor Property

Gets or sets the placeholder text color.

```csharp
public Tizen.UI.Color PlaceholderTextColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.SelectedText'></a>

## InputEditor.SelectedText Property

Gets the currently selected text.

```csharp
public string SelectedText { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputEditor.SelectedTextIndex'></a>

## InputEditor.SelectedTextIndex Property

Gets the index range of the currently selected text.

```csharp
public Tizen.UI.Components.ClosedRange&lt;int> SelectedTextIndex { get; }
```

#### Property Value
Tizen.UI.Components.ClosedRange&lt;[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')&gt;

<a name='Tizen.UI.Components.Material.InputEditor.SelectionEnabled'></a>

## InputEditor.SelectionEnabled Property

Gets or sets whether the text selection is enabled.

```csharp
public bool SelectionEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.Strikethrough'></a>

## InputEditor.Strikethrough Property

Gets or sets the strike through style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Strikethrough> Strikethrough { get; set; }
```

Implements Strikethrough

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Strikethrough[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputEditor.SystemFontFamilyEnabled'></a>

## InputEditor.SystemFontFamilyEnabled Property

Gets or sets whether the [FontFamily](Tizen.UI.Components.Material.InputEditor.md#Tizen.UI.Components.Material.InputEditor.FontFamily 'Tizen.UI.Components.Material.InputEditor.FontFamily') should be determined based on the system settings.

```csharp
public bool SystemFontFamilyEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.SystemFontSizeScaleEnabled'></a>

## InputEditor.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.InputEditor.Text'></a>

## InputEditor.Text Property

Gets or sets the text to display in the UTF-8 format.

```csharp
public string Text { get; set; }
```

Implements Text

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.InputEditor.TextColor'></a>

## InputEditor.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements TextColor

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.TextOverflow'></a>

## InputEditor.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

#### Property Value
Tizen.UI.TextOverflow

<a name='Tizen.UI.Components.Material.InputEditor.TextShadow'></a>

## InputEditor.TextShadow Property

Gets or sets the drop shadow for the text.

```csharp
public System.Nullable&lt;Tizen.UI.TextShadow> TextShadow { get; set; }
```

Implements TextShadow

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.TextShadow[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputEditor.Underline'></a>

## InputEditor.Underline Property

Gets or sets the underline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Underline> Underline { get; set; }
```

Implements Underline

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Underline[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.InputEditor.VerticalAlignment'></a>

## InputEditor.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements VerticalAlignment

#### Property Value
Tizen.UI.TextAlignment
### Methods

<a name='Tizen.UI.Components.Material.InputEditor.ClearSelection()'></a>

## InputEditor.ClearSelection() Method

Clears the current selection.

```csharp
public void ClearSelection();
```

<a name='Tizen.UI.Components.Material.InputEditor.GetLineCount()'></a>

## InputEditor.GetLineCount() Method

Gets the number of lines of text.

```csharp
public int GetLineCount();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.InputEditor.SelectText(int,int)'></a>

## InputEditor.SelectText(int, int) Method

Selects the text within the specified index range.

```csharp
public void SelectText(int startIndex, int endIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SelectText(int,int).startIndex'></a>

`startIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The start index of the selection.

<a name='Tizen.UI.Components.Material.InputEditor.SelectText(int,int).endIndex'></a>

`endIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The end index of the selection.

<a name='Tizen.UI.Components.Material.InputEditor.SelectWholeText()'></a>

## InputEditor.SelectWholeText() Method

Selects the whole text.

```csharp
public void SelectWholeText();
```

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorBlink(float,float)'></a>

## InputEditor.SetCursorBlink(float, float) Method

Enables cursor blink.

```csharp
public void SetCursorBlink(float interval, float duration);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorBlink(float,float).interval'></a>

`interval` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The interval between blinks.

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorBlink(float,float).duration'></a>

`duration` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The duration of each blink.

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorColor(Tizen.UI.Color)'></a>

## InputEditor.SetCursorColor(Color) Method

Sets the cursor color.

```csharp
public void SetCursorColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorColor(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorWidth(int)'></a>

## InputEditor.SetCursorWidth(int) Method

Sets the cursor width.

```csharp
public void SetCursorWidth(int width);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetCursorWidth(int).width'></a>

`width` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The width of the cursor.

<a name='Tizen.UI.Components.Material.InputEditor.SetFontVariation(string,float)'></a>

## InputEditor.SetFontVariation(string, float) Method

Sets Font Variation with string tag.

```csharp
public void SetFontVariation(string tag, float value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetFontVariation(string,float).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag of font variation.

<a name='Tizen.UI.Components.Material.InputEditor.SetFontVariation(string,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of font variation.

<a name='Tizen.UI.Components.Material.InputEditor.SetInputFilter(string,string)'></a>

## InputEditor.SetInputFilter(string, string) Method

Set input filter.

```csharp
public void SetInputFilter(string include, string exclude=null);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetInputFilter(string,string).include'></a>

`include` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A regular expression in the set of characters to be accepted.

<a name='Tizen.UI.Components.Material.InputEditor.SetInputFilter(string,string).exclude'></a>

`exclude` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

A regular expression in the set of characters to be rejected.

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle)'></a>

## InputEditor.SetInputMethodActionButtonTitle(ActionButtonTitle) Method

Sets the input method's action button title.

```csharp
public void SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle actionButtonTitle);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodActionButtonTitle(Tizen.UI.ActionButtonTitle).actionButtonTitle'></a>

`actionButtonTitle` Tizen.UI.ActionButtonTitle

The title of the action button.

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodCapitalMode(Tizen.UI.AutoCapital)'></a>

## InputEditor.SetInputMethodCapitalMode(AutoCapital) Method

Sets the input method's capital mode.

```csharp
public void SetInputMethodCapitalMode(Tizen.UI.AutoCapital capitalMode);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodCapitalMode(Tizen.UI.AutoCapital).capitalMode'></a>

`capitalMode` Tizen.UI.AutoCapital

The capital mode of the input method.

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodPanelType(Tizen.UI.PanelLayout)'></a>

## InputEditor.SetInputMethodPanelType(PanelLayout) Method

Sets the input method's panel layout.

```csharp
public void SetInputMethodPanelType(Tizen.UI.PanelLayout panelLayout);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetInputMethodPanelType(Tizen.UI.PanelLayout).panelLayout'></a>

`panelLayout` Tizen.UI.PanelLayout

The panel layout of the input method.

<a name='Tizen.UI.Components.Material.InputEditor.SetSecondaryCursorColor(Tizen.UI.Color)'></a>

## InputEditor.SetSecondaryCursorColor(Color) Method

Sets the secondary cursor color.

```csharp
public void SetSecondaryCursorColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetSecondaryCursorColor(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionColor(Tizen.UI.Color)'></a>

## InputEditor.SetSelectionColor(Color) Method

Sets the selection area color.

```csharp
public void SetSelectionColor(Tizen.UI.Color color);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionColor(Tizen.UI.Color).color'></a>

`color` Tizen.UI.Color

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandleImage(string,string)'></a>

## InputEditor.SetSelectionHandleImage(string, string) Method

Sets the selection handle images.

```csharp
public void SetSelectionHandleImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandleImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandleImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandlePressedImage(string,string)'></a>

## InputEditor.SetSelectionHandlePressedImage(string, string) Method

Sets the pressed selection handle images.

```csharp
public void SetSelectionHandlePressedImage(string leftResourceUrl, string rightResourceUrl);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandlePressedImage(string,string).leftResourceUrl'></a>

`leftResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the left handle.

<a name='Tizen.UI.Components.Material.InputEditor.SetSelectionHandlePressedImage(string,string).rightResourceUrl'></a>

`rightResourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The Url of the image for the right handle.

<a name='Tizen.UI.Components.Material.InputEditor.SetTextPadding(Tizen.UI.Thickness)'></a>

## InputEditor.SetTextPadding(Thickness) Method

Sets the padding for the text within the view.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.Components.Material.InputEditor.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` Tizen.UI.Thickness

The padding thickness.

Implements SetTextPadding(Thickness)')

<a name='Tizen.UI.Components.Material.InputEditor.UnsetCursorBlink()'></a>

## InputEditor.UnsetCursorBlink() Method

Disables the cursor blink.

```csharp
public void UnsetCursorBlink();
```
### Events

<a name='Tizen.UI.Components.Material.InputEditor.AnchorClicked'></a>

## InputEditor.AnchorClicked Event

Occurs when the anchor is clicked in markup.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.AnchorClickedEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.InputEditor.CursorMoved'></a>

## InputEditor.CursorMoved Event

Occurs when the cursor moved.

```csharp
public event EventHandler CursorMoved;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputEditor.KeyPressed'></a>

## InputEditor.KeyPressed Event

Occurs when any key is pressed.

```csharp
public event EventHandler&lt;string> KeyPressed;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.InputEditor.MaximumLengthReached'></a>

## InputEditor.MaximumLengthReached Event

Occurs when the text has reached to the specified maximum length.

```csharp
public event EventHandler MaximumLengthReached;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputEditor.SelectionChanged'></a>

## InputEditor.SelectionChanged Event

Occurs when the seledction changed.

```csharp
public event EventHandler SelectionChanged;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputEditor.SelectionCleared'></a>

## InputEditor.SelectionCleared Event

Occurs when the selection is cleared.

```csharp
public event EventHandler SelectionCleared;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputEditor.SelectionStarted'></a>

## InputEditor.SelectionStarted Event

Occurs when the selection is started.

```csharp
public event EventHandler SelectionStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.InputEditor.TextChanged'></a>

## InputEditor.TextChanged Event

Occurs when the text is changed.

```csharp
public event EventHandler TextChanged;
```

Implements TextChanged

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')














































