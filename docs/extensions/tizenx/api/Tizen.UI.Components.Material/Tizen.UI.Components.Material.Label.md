### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Label Class

A text control that displays a short to medium length string of text.

```csharp
public class Label : Tizen.UI.View,
Tizen.UI.IText,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextPadding,
Tizen.UI.ITextFormatting,
Tizen.UI.Components.IFlexibleText,
Tizen.UI.Components.IDecoratableText
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; Label

Derived  
&#8627; [Title](Tizen.UI.Components.Material.Title.md 'Tizen.UI.Components.Material.Title')

Implements [Tizen.UI.IText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText 'Tizen.UI.IText'), [Tizen.UI.ITextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment 'Tizen.UI.ITextAlignment'), [Tizen.UI.ITextPadding](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextPadding 'Tizen.UI.ITextPadding'), [Tizen.UI.ITextFormatting](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextFormatting 'Tizen.UI.ITextFormatting'), [Tizen.UI.Components.IFlexibleText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText 'Tizen.UI.Components.IFlexibleText'), [Tizen.UI.Components.IDecoratableText](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText 'Tizen.UI.Components.IDecoratableText')
### Constructors

<a name='Tizen.UI.Components.Material.Label.Label()'></a>

## Label() Constructor

Constructs a TextView.

```csharp
public Label();
```

<a name='Tizen.UI.Components.Material.Label.Label(string)'></a>

## Label(string) Constructor

Constructs a TextView with text.

```csharp
public Label(string text);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.Label(string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display.

<a name='Tizen.UI.Components.Material.Label.Label(string,Tizen.UI.Components.Material.LabelVariables)'></a>

## Label(string, LabelVariables) Constructor

Constructs a TextView with text.

```csharp
public Label(string text, Tizen.UI.Components.Material.LabelVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.Label(string,Tizen.UI.Components.Material.LabelVariables).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to display.

<a name='Tizen.UI.Components.Material.Label.Label(string,Tizen.UI.Components.Material.LabelVariables).variables'></a>

`variables` [LabelVariables](Tizen.UI.Components.Material.LabelVariables.md 'Tizen.UI.Components.Material.LabelVariables')

The variables to apply to the text.

<a name='Tizen.UI.Components.Material.Label.Label(Tizen.UI.Components.Material.LabelVariables)'></a>

## Label(LabelVariables) Constructor

Constructs a TextView.

```csharp
public Label(Tizen.UI.Components.Material.LabelVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.Label(Tizen.UI.Components.Material.LabelVariables).variables'></a>

`variables` [LabelVariables](Tizen.UI.Components.Material.LabelVariables.md 'Tizen.UI.Components.Material.LabelVariables')

The variables to apply to the text.
### Properties

<a name='Tizen.UI.Components.Material.Label.AdjustedFontSize'></a>

## Label.AdjustedFontSize Property

Gets the adjusted font size after fitting the text by [AutoFontSize](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.AutoFontSize 'Tizen.UI.Components.Material.Label.AutoFontSize').

```csharp
public float AdjustedFontSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Label.AdjustedFontSizeScale'></a>

## Label.AdjustedFontSizeScale Property

Gets the adjusted font size scale used for rendering after applying all constraints,  
including the current [MinimumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MinimumFontSizeScale 'Tizen.UI.Components.Material.Label.MinimumFontSizeScale'), [MaximumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MaximumFontSizeScale 'Tizen.UI.Components.Material.Label.MaximumFontSizeScale'),  
and system font size scale adjustments.

```csharp
public float AdjustedFontSizeScale { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If [MinimumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MinimumFontSizeScale 'Tizen.UI.Components.Material.Label.MinimumFontSizeScale') is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MaximumFontSizeScale 'Tizen.UI.Components.Material.Label.MaximumFontSizeScale')  
(an inverted range), the [MinimumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MinimumFontSizeScale 'Tizen.UI.Components.Material.Label.MinimumFontSizeScale') value takes precedence  
and is used as the adjusted scale.

<a name='Tizen.UI.Components.Material.Label.AnchorClickedColor'></a>

## Label.AnchorClickedColor Property

Gets or sets the color of the anchor text when it is clicked in markup.

```csharp
public Tizen.UI.Color AnchorClickedColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.Label.AnchorColor'></a>

## Label.AnchorColor Property

Gets or sets the color of the anchor text in markup.

```csharp
public Tizen.UI.Color AnchorColor { get; set; }
```

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.Label.AutoFontSize'></a>

## Label.AutoFontSize Property

Gets or sets the auto font size options to fit text in the boundary of label.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

Implements [AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.AutoFontSize 'Tizen.UI.Components.IFlexibleText.AutoFontSize')

#### Property Value
[Tizen.UI.AutoFontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AutoFontSize 'Tizen.UI.AutoFontSize')

### Remarks
The [FontSize](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.FontSize 'Tizen.UI.Components.Material.Label.FontSize') value will be ignored if this is not [AutoFontSize.None](https://docs.microsoft.com/en-us/dotnet/api/AutoFontSize.None 'AutoFontSize.None').

<a name='Tizen.UI.Components.Material.Label.FontFamily'></a>

## Label.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Label.FontSize'></a>

## Label.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.FontSize 'Tizen.UI.Components.IFlexibleText.FontSize'), [FontSize](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Label.FontSizeScale'></a>

## Label.FontSizeScale Property

Gets or sets the scaling value of the font size.

```csharp
public float FontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Label.FontSlant'></a>

## Label.FontSlant Property

Gets or sets the font style weight such as [FontStyleSlant.Italic](https://docs.microsoft.com/en-us/dotnet/api/FontStyleSlant.Italic 'FontStyleSlant.Italic').

```csharp
public Tizen.UI.FontSlant FontSlant { get; set; }
```

#### Property Value
[Tizen.UI.FontSlant](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontSlant 'Tizen.UI.FontSlant')

<a name='Tizen.UI.Components.Material.Label.FontWeight'></a>

## Label.FontWeight Property

Gets or sets the font style weight such as [FontStyleWeight.Bold](https://docs.microsoft.com/en-us/dotnet/api/FontStyleWeight.Bold 'FontStyleWeight.Bold').

```csharp
public Tizen.UI.FontWeight FontWeight { get; set; }
```

#### Property Value
[Tizen.UI.FontWeight](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWeight 'Tizen.UI.FontWeight')

<a name='Tizen.UI.Components.Material.Label.FontWidth'></a>

## Label.FontWidth Property

Gets or sets the font style width such as [FontStyleWidth.Condensed](https://docs.microsoft.com/en-us/dotnet/api/FontStyleWidth.Condensed 'FontStyleWidth.Condensed').

```csharp
public Tizen.UI.FontWidth FontWidth { get; set; }
```

#### Property Value
[Tizen.UI.FontWidth](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.FontWidth 'Tizen.UI.FontWidth')

<a name='Tizen.UI.Components.Material.Label.HorizontalAlignment'></a>

## Label.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements [HorizontalAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment.HorizontalAlignment 'Tizen.UI.ITextAlignment.HorizontalAlignment')

#### Property Value
[Tizen.UI.TextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextAlignment 'Tizen.UI.TextAlignment')

<a name='Tizen.UI.Components.Material.Label.IsAbsoluteLineHeight'></a>

## Label.IsAbsoluteLineHeight Property

Gets or sets the line height policy. This value will determine how the line height is calculated.  
If the value is false, the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is false with value 1.0f.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.IsMarkupEnabled'></a>

## Label.IsMarkupEnabled Property

Gets or sets whether the text should be marked up with the HTML tags.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.IsMultiline'></a>

## Label.IsMultiline Property

Gets or sets whether the text should be multi-line.

```csharp
public bool IsMultiline { get; set; }
```

Implements [IsMultiline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextFormatting.IsMultiline 'Tizen.UI.ITextFormatting.IsMultiline')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.IsTextCutout'></a>

## Label.IsTextCutout Property

Gets or sets whether to enable cutout of the text.

```csharp
public bool IsTextCutout { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.LineBreakMode'></a>

## Label.LineBreakMode Property

Gets or sets the line break mode of the text.

```csharp
public Tizen.UI.LineBreakMode LineBreakMode { get; set; }
```

#### Property Value
[Tizen.UI.LineBreakMode](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.LineBreakMode 'Tizen.UI.LineBreakMode')

<a name='Tizen.UI.Components.Material.Label.LineHeight'></a>

## Label.LineHeight Property

Gets or sets the minimum line height. If the value is smaller than the natural line height, the natural line height will be used instead.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
This property is treated differently by the [LineHeightPolicy](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy 'LineHeightPolicy'). If the value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative'), the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative') with value 1.0f.

<a name='Tizen.UI.Components.Material.Label.MaximumFontSizeScale'></a>

## Label.MaximumFontSizeScale Property

Gets or sets the maximum allowable font size scale.

```csharp
public float MaximumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is less than [MinimumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MinimumFontSizeScale 'Tizen.UI.Components.Material.Label.MinimumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.AdjustedFontSizeScale 'Tizen.UI.Components.Material.Label.AdjustedFontSizeScale') will follow the minimum value.

<a name='Tizen.UI.Components.Material.Label.MinimumFontSizeScale'></a>

## Label.MinimumFontSizeScale Property

Gets or sets the minimum allowable font size scale.

```csharp
public float MinimumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is greater than [MaximumFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.MaximumFontSizeScale 'Tizen.UI.Components.Material.Label.MaximumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.AdjustedFontSizeScale 'Tizen.UI.Components.Material.Label.AdjustedFontSizeScale') will follow this minimum value.

<a name='Tizen.UI.Components.Material.Label.Outline'></a>

## Label.Outline Property

Gets or sets the outline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Outline> Outline { get; set; }
```

Implements [Outline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Outline 'Tizen.UI.Components.IDecoratableText.Outline')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Outline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Outline 'Tizen.UI.Outline')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.Label.Strikethrough'></a>

## Label.Strikethrough Property

Gets or sets the strike through style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Strikethrough> Strikethrough { get; set; }
```

Implements [Strikethrough](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Strikethrough 'Tizen.UI.Components.IDecoratableText.Strikethrough')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Strikethrough](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Strikethrough 'Tizen.UI.Strikethrough')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.Label.SystemFontFamilyEnabled'></a>

## Label.SystemFontFamilyEnabled Property

Gets or sets whether the [FontFamily](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.FontFamily 'Tizen.UI.Components.Material.Label.FontFamily') should be determined based on the system settings.

```csharp
public bool SystemFontFamilyEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.SystemFontSizeScaleEnabled'></a>

## Label.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Label.Text'></a>

## Label.Text Property

Gets or sets the text to display in the UTF-8 format.

```csharp
public string Text { get; set; }
```

Implements [Text](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.Material.Label.TextColor'></a>

## Label.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Tizen.UI.Color](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Color 'Tizen.UI.Color')

<a name='Tizen.UI.Components.Material.Label.TextOverflow'></a>

## Label.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IFlexibleText.TextOverflow 'Tizen.UI.Components.IFlexibleText.TextOverflow'), [TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextFormatting.TextOverflow 'Tizen.UI.ITextFormatting.TextOverflow')

#### Property Value
[Tizen.UI.TextOverflow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextOverflow 'Tizen.UI.TextOverflow')

<a name='Tizen.UI.Components.Material.Label.TextShadow'></a>

## Label.TextShadow Property

Gets or sets the drop shadow for the text.

```csharp
public System.Nullable&lt;Tizen.UI.TextShadow> TextShadow { get; set; }
```

Implements [TextShadow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.TextShadow 'Tizen.UI.Components.IDecoratableText.TextShadow')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.TextShadow](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextShadow 'Tizen.UI.TextShadow')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.Label.Underline'></a>

## Label.Underline Property

Gets or sets the underline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Underline> Underline { get; set; }
```

Implements [Underline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IDecoratableText.Underline 'Tizen.UI.Components.IDecoratableText.Underline')

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')[Tizen.UI.Underline](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Underline 'Tizen.UI.Underline')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.Material.Label.VerticalAlignment'></a>

## Label.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements [VerticalAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextAlignment.VerticalAlignment 'Tizen.UI.ITextAlignment.VerticalAlignment')

#### Property Value
[Tizen.UI.TextAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.TextAlignment 'Tizen.UI.TextAlignment')
### Methods

<a name='Tizen.UI.Components.Material.Label.GetLineCount()'></a>

## Label.GetLineCount() Method

Gets the number of lines of text within the current caluted width.  
Note that it will not return valid count if the layout is not finished.

```csharp
public int GetLineCount();
```

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.Label.GetLineCount(float)'></a>

## Label.GetLineCount(float) Method

Gets the number of lines of text within given width.

```csharp
public int GetLineCount(float width);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.GetLineCount(float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.Label.Measure(float,float)'></a>

## Label.Measure(float, float) Method

Measures the view based on the available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.Components.Material.Label.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the view.

<a name='Tizen.UI.Components.Material.Label.SetFontVariation(string,float)'></a>

## Label.SetFontVariation(string, float) Method

Sets Font Variation with string tag.

```csharp
public void SetFontVariation(string tag, float value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetFontVariation(string,float).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag of font variation.

<a name='Tizen.UI.Components.Material.Label.SetFontVariation(string,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of font variation.

<a name='Tizen.UI.Components.Material.Label.SetMarqueeGap(float)'></a>

## Label.SetMarqueeGap(float) Method

Sets the gap before marquee wraps.

```csharp
public void SetMarqueeGap(float value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetMarqueeGap(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The gap.

<a name='Tizen.UI.Components.Material.Label.SetMarqueeLoopCount(int)'></a>

## Label.SetMarqueeLoopCount(int) Method

Sets the number of complete loops for marquee.

```csharp
public void SetMarqueeLoopCount(int value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetMarqueeLoopCount(int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of loops.

<a name='Tizen.UI.Components.Material.Label.SetMarqueeLoopDelay(float)'></a>

## Label.SetMarqueeLoopDelay(float) Method

Sets the amount of time to delay the starting time of marquee and further loops.

```csharp
public void SetMarqueeLoopDelay(float value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetMarqueeLoopDelay(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The delay time in seconds.

<a name='Tizen.UI.Components.Material.Label.SetMarqueeSpeed(int)'></a>

## Label.SetMarqueeSpeed(int) Method

Sets the marquee speed.

```csharp
public void SetMarqueeSpeed(int value);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetMarqueeSpeed(int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The marquee speed in pixels per second.

<a name='Tizen.UI.Components.Material.Label.SetTextPadding(Tizen.UI.Thickness)'></a>

## Label.SetTextPadding(Thickness) Method

Sets the padding for the text within the label.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Label.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` [Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

The padding thickness.

Implements [SetTextPadding(Thickness)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ITextPadding.SetTextPadding#Tizen_UI_ITextPadding_SetTextPadding_Tizen_UI_Thickness_ 'Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness)')
### Events

<a name='Tizen.UI.Components.Material.Label.AnchorClicked'></a>

## Label.AnchorClicked Event

Occurs when the anchor is clicked in markup.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.AnchorClickedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.AnchorClickedEventArgs 'Tizen.UI.AnchorClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.Label.FontSizeAdjusted'></a>

## Label.FontSizeAdjusted Event

Occurs when the font size is adjusted by [AutoFontSize](Tizen.UI.Components.Material.Label.md#Tizen.UI.Components.Material.Label.AutoFontSize 'Tizen.UI.Components.Material.Label.AutoFontSize').

```csharp
public event EventHandler FontSizeAdjusted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')













































