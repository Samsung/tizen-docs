### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextView Class

A TextView is a text control that displays a short to medium length string of text.

```csharp
public class TextView : Tizen.UI.View,
Tizen.UI.IText,
Tizen.UI.ITextPadding,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextFormatting,
Tizen.UI.Internal.ILabelSignalHandler
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; TextView

Implements [IText](Tizen.UI.IText.md 'Tizen.UI.IText'), [ITextPadding](Tizen.UI.ITextPadding.md 'Tizen.UI.ITextPadding'), [ITextAlignment](Tizen.UI.ITextAlignment.md 'Tizen.UI.ITextAlignment'), [ITextFormatting](Tizen.UI.ITextFormatting.md 'Tizen.UI.ITextFormatting'), [Tizen.UI.Internal.ILabelSignalHandler](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Internal.ILabelSignalHandler 'Tizen.UI.Internal.ILabelSignalHandler')
### Constructors

<a name='Tizen.UI.TextView.TextView()'></a>

## TextView() Constructor

Creates a new instance of a TextView.

```csharp
public TextView();
```
### Properties

<a name='Tizen.UI.TextView.AutoAdjustedFontSize'></a>

## TextView.AutoAdjustedFontSize Property

Gets the adjusted font size after fitting the text to the size of the control.

```csharp
public float AutoAdjustedFontSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.TextView.FontFamily'></a>

## TextView.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements [FontFamily](Tizen.UI.IText.md#Tizen.UI.IText.FontFamily 'Tizen.UI.IText.FontFamily')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.TextView.FontSize'></a>

## TextView.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements [FontSize](Tizen.UI.IText.md#Tizen.UI.IText.FontSize 'Tizen.UI.IText.FontSize')

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.TextView.HorizontalAlignment'></a>

## TextView.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements [HorizontalAlignment](Tizen.UI.ITextAlignment.md#Tizen.UI.ITextAlignment.HorizontalAlignment 'Tizen.UI.ITextAlignment.HorizontalAlignment')

#### Property Value
[TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')

<a name='Tizen.UI.TextView.IsAbsoluteLineHeight'></a>

## TextView.IsAbsoluteLineHeight Property

Gets or sets whether the line height is absolute or relative. Default is false.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.IsMarkupEnabled'></a>

## TextView.IsMarkupEnabled Property

Gets or sets whether the text should be marked up with the HTML tags.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.IsMultiline'></a>

## TextView.IsMultiline Property

Gets or sets whether the text should be multi-line.

```csharp
public bool IsMultiline { get; set; }
```

Implements [IsMultiline](Tizen.UI.ITextFormatting.md#Tizen.UI.ITextFormatting.IsMultiline 'Tizen.UI.ITextFormatting.IsMultiline')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.IsTextCutout'></a>

## TextView.IsTextCutout Property

Gets or sets whether to enable cutout of the text.

```csharp
public bool IsTextCutout { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.IsTextScrolling'></a>

## TextView.IsTextScrolling Property

Gets whether the text is currently scrolling.

```csharp
public bool IsTextScrolling { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.LineBreakMode'></a>

## TextView.LineBreakMode Property

Gets or sets the line break mode of the text.

```csharp
public Tizen.UI.LineBreakMode LineBreakMode { get; set; }
```

#### Property Value
[LineBreakMode](Tizen.UI.LineBreakMode.md 'Tizen.UI.LineBreakMode')

<a name='Tizen.UI.TextView.LineCount'></a>

## TextView.LineCount Property

Gets the number of lines of text.

```csharp
public int LineCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.TextView.LineHeight'></a>

## TextView.LineHeight Property

Gets or sets the line height of the text.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.TextView.ScaledFontSize'></a>

## TextView.ScaledFontSize Property

Gets the scaled font size of the text based on the current font size scale.

```csharp
public float ScaledFontSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.TextView.SystemFontScaleEnabled'></a>

## TextView.SystemFontScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.TextView.Text'></a>

## TextView.Text Property

Gets or sets the text to display.

```csharp
public string Text { get; set; }
```

Implements [Text](Tizen.UI.IText.md#Tizen.UI.IText.Text 'Tizen.UI.IText.Text')

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.TextView.TextColor'></a>

## TextView.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements [TextColor](Tizen.UI.IText.md#Tizen.UI.IText.TextColor 'Tizen.UI.IText.TextColor')

#### Property Value
[Color](Tizen.UI.Color.md 'Tizen.UI.Color')

<a name='Tizen.UI.TextView.TextOverflow'></a>

## TextView.TextOverflow Property

Gets or sets the TextOverflow of the text.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

Implements [TextOverflow](Tizen.UI.ITextFormatting.md#Tizen.UI.ITextFormatting.TextOverflow 'Tizen.UI.ITextFormatting.TextOverflow')

#### Property Value
[TextOverflow](Tizen.UI.TextOverflow.md 'Tizen.UI.TextOverflow')

<a name='Tizen.UI.TextView.VerticalAlignment'></a>

## TextView.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements [VerticalAlignment](Tizen.UI.ITextAlignment.md#Tizen.UI.ITextAlignment.VerticalAlignment 'Tizen.UI.ITextAlignment.VerticalAlignment')

#### Property Value
[TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')
### Methods

<a name='Tizen.UI.TextView.ClearOutline()'></a>

## TextView.ClearOutline() Method

Clears the outline

```csharp
public void ClearOutline();
```

<a name='Tizen.UI.TextView.ClearUnderline()'></a>

## TextView.ClearUnderline() Method

Clears the underline

```csharp
public void ClearUnderline();
```

<a name='Tizen.UI.TextView.GetHeightForWidth(float)'></a>

## TextView.GetHeightForWidth(float) Method

Gets for the given width.

```csharp
public float GetHeightForWidth(float width);
```
#### Parameters

<a name='Tizen.UI.TextView.GetHeightForWidth(float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width for which to calculate the height.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The height that best fits the given width.

<a name='Tizen.UI.TextView.Measure(float,float)'></a>

## TextView.Measure(float, float) Method

Measures the view based on the available width and height.

```csharp
public override Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.TextView.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the view.

<a name='Tizen.UI.TextView.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the view.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The measured size of the view.

<a name='Tizen.UI.TextView.SetAutoSize(Tizen.UI.AutoFontSize)'></a>

## TextView.SetAutoSize(AutoFontSize) Method

Sets the auto size of the label.

```csharp
public void SetAutoSize(Tizen.UI.AutoFontSize size);
```
#### Parameters

<a name='Tizen.UI.TextView.SetAutoSize(Tizen.UI.AutoFontSize).size'></a>

`size` [AutoFontSize](Tizen.UI.AutoFontSize.md 'Tizen.UI.AutoFontSize')

The auto size to set.

<a name='Tizen.UI.TextView.SetMarqueeConfig(int,int,float,float)'></a>

## TextView.SetMarqueeConfig(int, int, float, float) Method

Sets the marquee config on the label.

```csharp
public void SetMarqueeConfig(int loopCount=2, int speed=80, float gap=50f, float delay=0f);
```
#### Parameters

<a name='Tizen.UI.TextView.SetMarqueeConfig(int,int,float,float).loopCount'></a>

`loopCount` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of times the text should scroll before stopping.

<a name='Tizen.UI.TextView.SetMarqueeConfig(int,int,float,float).speed'></a>

`speed` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The speed of the text scroll animation, measured in pixels per second.

<a name='Tizen.UI.TextView.SetMarqueeConfig(int,int,float,float).gap'></a>

`gap` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The gap between the start of the text and the end of the text after each loop.

<a name='Tizen.UI.TextView.SetMarqueeConfig(int,int,float,float).delay'></a>

`delay` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The delay before the text scroll animation starts, measured in seconds.

<a name='Tizen.UI.TextView.SetOutline(Tizen.UI.Outline)'></a>

## TextView.SetOutline(Outline) Method

Sets the outline style for the text in the label.

```csharp
public void SetOutline(Tizen.UI.Outline outline);
```
#### Parameters

<a name='Tizen.UI.TextView.SetOutline(Tizen.UI.Outline).outline'></a>

`outline` [Outline](Tizen.UI.Outline.md 'Tizen.UI.Outline')

The outline style to apply to the text.

<a name='Tizen.UI.TextView.SetTextPadding(Tizen.UI.Thickness)'></a>

## TextView.SetTextPadding(Thickness) Method

Sets the padding for the text within the label.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.TextView.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The padding thickness.

Implements [SetTextPadding(Thickness)](Tizen.UI.ITextPadding.md#Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness) 'Tizen.UI.ITextPadding.SetTextPadding(Tizen.UI.Thickness)')

<a name='Tizen.UI.TextView.SetTextShadow(Tizen.UI.TextShadow)'></a>

## TextView.SetTextShadow(TextShadow) Method

Sets the text shadow for the label.

```csharp
public void SetTextShadow(Tizen.UI.TextShadow shadow);
```
#### Parameters

<a name='Tizen.UI.TextView.SetTextShadow(Tizen.UI.TextShadow).shadow'></a>

`shadow` [TextShadow](Tizen.UI.TextShadow.md 'Tizen.UI.TextShadow')

The text shadow object.

<a name='Tizen.UI.TextView.SetUnderline(Tizen.UI.Underline)'></a>

## TextView.SetUnderline(Underline) Method

Sets the underline style for the text in the label.

```csharp
public void SetUnderline(Tizen.UI.Underline underline);
```
#### Parameters

<a name='Tizen.UI.TextView.SetUnderline(Tizen.UI.Underline).underline'></a>

`underline` [Underline](Tizen.UI.Underline.md 'Tizen.UI.Underline')

The underline style to apply to the text.

<a name='Tizen.UI.TextView.StartTextScroll(int,int,float,float)'></a>

## TextView.StartTextScroll(int, int, float, float) Method

Starts the text scroll animation on the label.

```csharp
public void StartTextScroll(int loopCount=2, int speed=80, float gap=50f, float delay=0f);
```
#### Parameters

<a name='Tizen.UI.TextView.StartTextScroll(int,int,float,float).loopCount'></a>

`loopCount` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of times the text should scroll before stopping.

<a name='Tizen.UI.TextView.StartTextScroll(int,int,float,float).speed'></a>

`speed` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The speed of the text scroll animation, measured in pixels per second.

<a name='Tizen.UI.TextView.StartTextScroll(int,int,float,float).gap'></a>

`gap` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The gap between the start of the text and the end of the text after each loop.

<a name='Tizen.UI.TextView.StartTextScroll(int,int,float,float).delay'></a>

`delay` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The delay before the text scroll animation starts, measured in seconds.

<a name='Tizen.UI.TextView.StopTextScroll(bool)'></a>

## TextView.StopTextScroll(bool) Method

Stops the text scroll of the label.

```csharp
public void StopTextScroll(bool immediate=true);
```
#### Parameters

<a name='Tizen.UI.TextView.StopTextScroll(bool).immediate'></a>

`immediate` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

If true, the text stops immediately. If false, the text stops after finishing the loop.
### Events

<a name='Tizen.UI.TextView.AnchorClicked'></a>

## TextView.AnchorClicked Event

Occurs when the font size is adjusted by AutoFontSize.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[AnchorClickedEventArgs](Tizen.UI.AnchorClickedEventArgs.md 'Tizen.UI.AnchorClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.TextView.FontSizeAdjusted'></a>

## TextView.FontSizeAdjusted Event

Occurs when the font size is adjusted by AutoFontSize.

```csharp
public event EventHandler FontSizeAdjusted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')




