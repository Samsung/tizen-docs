### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## LabelImpl Class

Wrapper class of DALi text label.  
Note that this creates a native instance that can be accessed through [Handle](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.Handle 'Tizen.UI.Components.TextBaseImpl.Handle') which you should release manually using [ReleaseNativeHandle](https://docs.microsoft.com/en-us/dotnet/api/ReleaseNativeHandle 'ReleaseNativeHandle').

```csharp
public class LabelImpl : Tizen.UI.Components.TextBaseImpl,
Tizen.UI.ITextFormatting
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [TextBaseImpl](Tizen.UI.Components.TextBaseImpl.md 'Tizen.UI.Components.TextBaseImpl') &#129106; LabelImpl

Implements Tizen.UI.ITextFormatting
### Constructors

<a name='Tizen.UI.Components.LabelImpl.LabelImpl()'></a>

## LabelImpl() Constructor

Construct a new instance.

```csharp
public LabelImpl();
```
### Properties

<a name='Tizen.UI.Components.LabelImpl.AdjustedFontSize'></a>

## LabelImpl.AdjustedFontSize Property

Gets the adjusted font size after fitting the text by [AutoFontSize](Tizen.UI.Components.LabelImpl.md#Tizen.UI.Components.LabelImpl.AutoFontSize 'Tizen.UI.Components.LabelImpl.AutoFontSize').

```csharp
public float AdjustedFontSize { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.LabelImpl.AnchorClickedColor'></a>

## LabelImpl.AnchorClickedColor Property

Gets or sets the color of the anchor text when it is clicked in markup.

```csharp
public Tizen.UI.Color AnchorClickedColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.LabelImpl.AnchorColor'></a>

## LabelImpl.AnchorColor Property

Gets or sets the color of the anchor text in markup.

```csharp
public Tizen.UI.Color AnchorColor { get; set; }
```

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.LabelImpl.AutoFontSize'></a>

## LabelImpl.AutoFontSize Property

Gets or sets the auto font size options to fit text in the boundary of label.

```csharp
public Tizen.UI.AutoFontSize AutoFontSize { get; set; }
```

#### Property Value
Tizen.UI.AutoFontSize

### Remarks
The [FontSize](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.FontSize 'Tizen.UI.Components.TextBaseImpl.FontSize') value will be ignored if this is not [AutoFontSize.None](https://docs.microsoft.com/en-us/dotnet/api/AutoFontSize.None 'AutoFontSize.None').

<a name='Tizen.UI.Components.LabelImpl.IsAbsoluteLineHeight'></a>

## LabelImpl.IsAbsoluteLineHeight Property

Gets or sets the line height policy. This value will determine how the line height is calculated.  
If the value is false, the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is false with value 1.0f.

```csharp
public bool IsAbsoluteLineHeight { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.LabelImpl.IsMultiline'></a>

## LabelImpl.IsMultiline Property

Gets or sets whether the text should be multi-line.

```csharp
public bool IsMultiline { get; set; }
```

Implements IsMultiline

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.LabelImpl.IsTextCutout'></a>

## LabelImpl.IsTextCutout Property

Gets or sets whether to enable cutout of the text.

```csharp
public bool IsTextCutout { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.LabelImpl.LineBreakMode'></a>

## LabelImpl.LineBreakMode Property

Gets or sets the line break mode of the text.

```csharp
public Tizen.UI.LineBreakMode LineBreakMode { get; set; }
```

#### Property Value
Tizen.UI.LineBreakMode

<a name='Tizen.UI.Components.LabelImpl.LineHeight'></a>

## LabelImpl.LineHeight Property

Gets or sets the minimum line height. If the value is smaller than the natural line height, the natural line height will be used instead.

```csharp
public float LineHeight { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
This property is treated differently by the [LineHeightPolicy](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy 'LineHeightPolicy'). If the value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative'), the line height will be calculated as a percentage of the natural line height. Otherwise, it will be calculated as an absolute value.  
Default value is [LineHeightPolicy.Relative](https://docs.microsoft.com/en-us/dotnet/api/LineHeightPolicy.Relative 'LineHeightPolicy.Relative') with value 1.0f.
### Methods

<a name='Tizen.UI.Components.LabelImpl.GetLineCount(float)'></a>

## LabelImpl.GetLineCount(float) Method

Gets the number of lines of text within given width.

```csharp
public int GetLineCount(float width);
```
#### Parameters

<a name='Tizen.UI.Components.LabelImpl.GetLineCount(float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeGap(float)'></a>

## LabelImpl.SetMarqueeGap(float) Method

Sets the gap before marquee wraps.

```csharp
public void SetMarqueeGap(float value);
```
#### Parameters

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeGap(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The gap.

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeLoopCount(int)'></a>

## LabelImpl.SetMarqueeLoopCount(int) Method

Sets the number of complete loops for marquee.

```csharp
public void SetMarqueeLoopCount(int value);
```
#### Parameters

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeLoopCount(int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The number of loops.

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeLoopDelay(float)'></a>

## LabelImpl.SetMarqueeLoopDelay(float) Method

Sets the amount of time to delay the starting time of marquee and further loops.

```csharp
public void SetMarqueeLoopDelay(float value);
```
#### Parameters

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeLoopDelay(float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The delay time in seconds.

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeSpeed(int)'></a>

## LabelImpl.SetMarqueeSpeed(int) Method

Sets the speed of scrolling in pixels per second.

```csharp
public void SetMarqueeSpeed(int value);
```
#### Parameters

<a name='Tizen.UI.Components.LabelImpl.SetMarqueeSpeed(int).value'></a>

`value` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')
### Events

<a name='Tizen.UI.Components.LabelImpl.FontSizeAdjusted'></a>

## LabelImpl.FontSizeAdjusted Event

Occurs when the font size is adjusted automatically.

```csharp
public event EventHandler FontSizeAdjusted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')



























































