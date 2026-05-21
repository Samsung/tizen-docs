### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## TextBaseImpl Class

Basic DALi text object wrapper.

```csharp
public abstract class TextBaseImpl :
System.IDisposable,
Tizen.UI.IText,
Tizen.UI.ITextAlignment,
Tizen.UI.ITextPadding
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TextBaseImpl

Derived  
&#8627; [InputTextBaseImpl](Tizen.UI.Components.InputTextBaseImpl.md 'Tizen.UI.Components.InputTextBaseImpl')  
&#8627; [LabelImpl](Tizen.UI.Components.LabelImpl.md 'Tizen.UI.Components.LabelImpl')

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable'), Tizen.UI.IText, Tizen.UI.ITextAlignment, Tizen.UI.ITextPadding
### Constructors

<a name='Tizen.UI.Components.TextBaseImpl.TextBaseImpl()'></a>

## TextBaseImpl() Constructor

Constructs a new instance.

```csharp
public TextBaseImpl();
```
### Properties

<a name='Tizen.UI.Components.TextBaseImpl.AdjustedFontSizeScale'></a>

## TextBaseImpl.AdjustedFontSizeScale Property

Gets the adjusted font size scale used for rendering after applying all constraints,  
including the current [MinimumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale'), [MaximumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale'),  
and system font size scale adjustments.

```csharp
public float AdjustedFontSizeScale { get; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If [MinimumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale') is greater than [MaximumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale')  
(an inverted range), the [MinimumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale') value takes precedence  
and is used as the adjusted scale.

<a name='Tizen.UI.Components.TextBaseImpl.FontFamily'></a>

## TextBaseImpl.FontFamily Property

Gets or sets the font family of the text.

```csharp
public string FontFamily { get; set; }
```

Implements FontFamily

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.TextBaseImpl.FontSize'></a>

## TextBaseImpl.FontSize Property

Gets or sets the font size of the text.

```csharp
public float FontSize { get; set; }
```

Implements FontSize

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.TextBaseImpl.FontSizeScale'></a>

## TextBaseImpl.FontSizeScale Property

Gets or sets the scaling value of the font size.

```csharp
public float FontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.TextBaseImpl.FontSlant'></a>

## TextBaseImpl.FontSlant Property

Gets or sets the font style weight such as Tizen.UI.FontSlant.Italic.

```csharp
public Tizen.UI.FontSlant FontSlant { get; set; }
```

#### Property Value
Tizen.UI.FontSlant

<a name='Tizen.UI.Components.TextBaseImpl.FontWeight'></a>

## TextBaseImpl.FontWeight Property

Gets or sets the font style weight such as Tizen.UI.FontWeight.Bold.

```csharp
public Tizen.UI.FontWeight FontWeight { get; set; }
```

#### Property Value
Tizen.UI.FontWeight

<a name='Tizen.UI.Components.TextBaseImpl.FontWidth'></a>

## TextBaseImpl.FontWidth Property

Gets or sets the font style width such as [FontWeight](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.FontWeight 'Tizen.UI.Components.TextBaseImpl.FontWeight').

```csharp
public Tizen.UI.FontWidth FontWidth { get; set; }
```

#### Property Value
Tizen.UI.FontWidth

<a name='Tizen.UI.Components.TextBaseImpl.Handle'></a>

## TextBaseImpl.Handle Property

Gets the DALi pointer.

```csharp
public System.IntPtr Handle { get; }
```

#### Property Value
[System.IntPtr](https://docs.microsoft.com/en-us/dotnet/api/System.IntPtr 'System.IntPtr')

<a name='Tizen.UI.Components.TextBaseImpl.HorizontalAlignment'></a>

## TextBaseImpl.HorizontalAlignment Property

Gets or sets the horizontal alignment of the text.

```csharp
public Tizen.UI.TextAlignment HorizontalAlignment { get; set; }
```

Implements HorizontalAlignment

#### Property Value
Tizen.UI.TextAlignment

<a name='Tizen.UI.Components.TextBaseImpl.IsDisposed'></a>

## TextBaseImpl.IsDisposed Property

Gets whether this instance is disposed or not.

```csharp
public bool IsDisposed { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.TextBaseImpl.IsMarkupEnabled'></a>

## TextBaseImpl.IsMarkupEnabled Property

Gets or sets whether the text should be marked up with the HTML tags.

```csharp
public bool IsMarkupEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale'></a>

## TextBaseImpl.MaximumFontSizeScale Property

Gets or sets the maximum allowable font size scale.

```csharp
public float MaximumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is less than [MinimumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.AdjustedFontSizeScale 'Tizen.UI.Components.TextBaseImpl.AdjustedFontSizeScale') will follow the minimum value.

<a name='Tizen.UI.Components.TextBaseImpl.MinimumFontSizeScale'></a>

## TextBaseImpl.MinimumFontSizeScale Property

Gets or sets the minimum allowable font size scale.

```csharp
public float MinimumFontSizeScale { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

### Remarks
If this value is greater than [MaximumFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale 'Tizen.UI.Components.TextBaseImpl.MaximumFontSizeScale') (range inversion),  
[AdjustedFontSizeScale](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.AdjustedFontSizeScale 'Tizen.UI.Components.TextBaseImpl.AdjustedFontSizeScale') will follow this minimum value.

<a name='Tizen.UI.Components.TextBaseImpl.Outline'></a>

## TextBaseImpl.Outline Property

Gets or sets the outline style for the text.  
It is [Outline.None](https://docs.microsoft.com/en-us/dotnet/api/Outline.None 'Outline.None') by default.

```csharp
public System.Nullable&lt;Tizen.UI.Outline> Outline { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Outline[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.TextBaseImpl.Owner'></a>

## TextBaseImpl.Owner Property

Owner view

```csharp
public Tizen.UI.View Owner { get; }
```

#### Property Value
Tizen.UI.View

<a name='Tizen.UI.Components.TextBaseImpl.Strikethrough'></a>

## TextBaseImpl.Strikethrough Property

Gets or sets the strike through style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Strikethrough> Strikethrough { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Strikethrough[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.TextBaseImpl.SystemFontFamilyEnabled'></a>

## TextBaseImpl.SystemFontFamilyEnabled Property

Gets or sets whether the [FontFamily](Tizen.UI.Components.TextBaseImpl.md#Tizen.UI.Components.TextBaseImpl.FontFamily 'Tizen.UI.Components.TextBaseImpl.FontFamily') should be determined based on the system settings.

```csharp
public bool SystemFontFamilyEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.TextBaseImpl.SystemFontSizeScaleEnabled'></a>

## TextBaseImpl.SystemFontSizeScaleEnabled Property

Gets or sets whether the font size should be scaled based on the system settings.

```csharp
public bool SystemFontSizeScaleEnabled { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.TextBaseImpl.Text'></a>

## TextBaseImpl.Text Property

Gets or sets the text to display in the UTF-8 format.

```csharp
public string Text { get; set; }
```

Implements Text

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.TextBaseImpl.TextColor'></a>

## TextBaseImpl.TextColor Property

Gets or sets the color of the text.

```csharp
public Tizen.UI.Color TextColor { get; set; }
```

Implements TextColor

#### Property Value
Tizen.UI.Color

<a name='Tizen.UI.Components.TextBaseImpl.TextOverflow'></a>

## TextBaseImpl.TextOverflow Property

Gets or sets the text ellipsize mode to be applied when the text overflows.

```csharp
public Tizen.UI.TextOverflow TextOverflow { get; set; }
```

#### Property Value
Tizen.UI.TextOverflow

<a name='Tizen.UI.Components.TextBaseImpl.TextShadow'></a>

## TextBaseImpl.TextShadow Property

Gets or sets the drop shadow for the text.

```csharp
public System.Nullable&lt;Tizen.UI.TextShadow> TextShadow { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.TextShadow[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.TextBaseImpl.Underline'></a>

## TextBaseImpl.Underline Property

Gets or sets the underline style for the text.

```csharp
public System.Nullable&lt;Tizen.UI.Underline> Underline { get; set; }
```

#### Property Value
[System.Nullable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')Tizen.UI.Underline[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Nullable-1 'System.Nullable`1')

<a name='Tizen.UI.Components.TextBaseImpl.VerticalAlignment'></a>

## TextBaseImpl.VerticalAlignment Property

Gets or sets the vertical alignment of the text.

```csharp
public Tizen.UI.TextAlignment VerticalAlignment { get; set; }
```

Implements VerticalAlignment

#### Property Value
Tizen.UI.TextAlignment
### Methods

<a name='Tizen.UI.Components.TextBaseImpl.Dispose()'></a>

## TextBaseImpl.Dispose() Method

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Components.TextBaseImpl.GetHeightForWidth(float)'></a>

## TextBaseImpl.GetHeightForWidth(float) Method

Gets for the given width.

```csharp
public float GetHeightForWidth(float width);
```
#### Parameters

<a name='Tizen.UI.Components.TextBaseImpl.GetHeightForWidth(float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width for which to calculate the height.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The height that best fits the given width.

<a name='Tizen.UI.Components.TextBaseImpl.GetSpaceHeight()'></a>

## TextBaseImpl.GetSpaceHeight() Method

Calculates natural size of a space character.

```csharp
public float GetSpaceHeight();
```

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.TextBaseImpl.Initialize(Tizen.UI.View,System.Action)'></a>

## TextBaseImpl.Initialize(View, Action) Method

Initialize an instance with owner view and resize handler.

```csharp
public void Initialize(Tizen.UI.View owner, System.Action resizeHandler);
```
#### Parameters

<a name='Tizen.UI.Components.TextBaseImpl.Initialize(Tizen.UI.View,System.Action).owner'></a>

`owner` Tizen.UI.View

<a name='Tizen.UI.Components.TextBaseImpl.Initialize(Tizen.UI.View,System.Action).resizeHandler'></a>

`resizeHandler` [System.Action](https://docs.microsoft.com/en-us/dotnet/api/System.Action 'System.Action')

<a name='Tizen.UI.Components.TextBaseImpl.SetFontVariation(string,float)'></a>

## TextBaseImpl.SetFontVariation(string, float) Method

Sets Font Variation with string tag.

```csharp
public void SetFontVariation(string tag, float value);
```
#### Parameters

<a name='Tizen.UI.Components.TextBaseImpl.SetFontVariation(string,float).tag'></a>

`tag` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The tag of font variation.

<a name='Tizen.UI.Components.TextBaseImpl.SetFontVariation(string,float).value'></a>

`value` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The value of font variation.

<a name='Tizen.UI.Components.TextBaseImpl.SetTextPadding(Tizen.UI.Thickness)'></a>

## TextBaseImpl.SetTextPadding(Thickness) Method

Sets the padding for the text within the view.

```csharp
public void SetTextPadding(Tizen.UI.Thickness thickness);
```
#### Parameters

<a name='Tizen.UI.Components.TextBaseImpl.SetTextPadding(Tizen.UI.Thickness).thickness'></a>

`thickness` Tizen.UI.Thickness

The padding thickness.

Implements SetTextPadding(Thickness)')
### Events

<a name='Tizen.UI.Components.TextBaseImpl.AnchorClicked'></a>

## TextBaseImpl.AnchorClicked Event

Occurs when the anchor is clicked in markup.

```csharp
public event EventHandler&lt;AnchorClickedEventArgs> AnchorClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')Tizen.UI.AnchorClickedEventArgs[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')



























































