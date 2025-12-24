### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextExtensions Class

Provides a series of extension methods that support configuring a Text.

```csharp
public static class TextExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TextExtensions
### Methods

<a name='Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string)'></a>

## TextExtensions.FontFamily&lt;TView>(this TView, string) Method

Sets the font family of the text in the TextView.

```csharp
public static TView FontFamily&lt;TView>(this TView view, string fontFamily)
    where TView : Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.FontFamily&lt;TView>(this TView, string).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string).fontFamily'></a>

`fontFamily` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The font family of the text.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.FontFamily_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.FontFamily&lt;TView>(this TView, string).TView')  
The view instance with the specified font family.

<a name='Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float)'></a>

## TextExtensions.FontSize&lt;TView>(this TView, float) Method

Sets the font size of the view.

```csharp
public static TView FontSize&lt;TView>(this TView view, float fontSize)
    where TView : Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float).TView 'Tizen.UI.TextExtensions.FontSize&lt;TView>(this TView, float).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float).fontSize'></a>

`fontSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The font size to set.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.FontSize_TView_(thisTView,float).TView 'Tizen.UI.TextExtensions.FontSize&lt;TView>(this TView, float).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment)'></a>

## TextExtensions.HorizontalAlignment&lt;TView>(this TView, TextAlignment) Method

Sets the horizontal alignment of the text in the TextView.

```csharp
public static TView HorizontalAlignment&lt;TView>(this TView view, Tizen.UI.TextAlignment alignment)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView 'Tizen.UI.TextExtensions.HorizontalAlignment&lt;TView>(this TView, Tizen.UI.TextAlignment).TView')

The View instance.

<a name='Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).alignment'></a>

`alignment` [TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')

The horizontal alignment of the text.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.HorizontalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView 'Tizen.UI.TextExtensions.HorizontalAlignment&lt;TView>(this TView, Tizen.UI.TextAlignment).TView')  
The View instance with the specified horizontal alignment.

<a name='Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool)'></a>

## TextExtensions.MultiLine&lt;TView>(this TView, bool) Method

Sets whether the view should be multi-line or not.

```csharp
public static TView MultiLine&lt;TView>(this TView view, bool multiLine)
    where TView : Tizen.UI.ITextFormatting;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool).TView 'Tizen.UI.TextExtensions.MultiLine&lt;TView>(this TView, bool).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool).multiLine'></a>

`multiLine` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the view should be multi-line, false otherwise.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.MultiLine_TView_(thisTView,bool).TView 'Tizen.UI.TextExtensions.MultiLine&lt;TView>(this TView, bool).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.Text_TView_(thisTView,string)'></a>

## TextExtensions.Text&lt;TView>(this TView, string) Method

Sets the text of the view.

```csharp
public static TView Text&lt;TView>(this TView view, string text)
    where TView : Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.Text_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.Text_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.Text_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.Text&lt;TView>(this TView, string).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.Text_TView_(thisTView,string).text'></a>

`text` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text to set.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.Text_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.Text&lt;TView>(this TView, string).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextCenter_TView_(thisTView)'></a>

## TextExtensions.TextCenter&lt;TView>(this TView) Method

Sets the horizontal and vertical alignment of the text in the view to center.

```csharp
public static TView TextCenter&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextCenter_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextCenter_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenter_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenter&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenter_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenter&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextCenterHorizontal_TView_(thisTView)'></a>

## TextExtensions.TextCenterHorizontal&lt;TView>(this TView) Method

Sets the horizontal alignment of the text in the view to center.

```csharp
public static TView TextCenterHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextCenterHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextCenterHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenterHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenterHorizontal&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenterHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenterHorizontal&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextCenterVertical_TView_(thisTView)'></a>

## TextExtensions.TextCenterVertical&lt;TView>(this TView) Method

Sets the vertical alignment of the text in the view to center.

```csharp
public static TView TextCenterVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextCenterVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextCenterVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenterVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenterVertical&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextCenterVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextCenterVertical&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color)'></a>

## TextExtensions.TextColor&lt;TView>(this TView, Color) Method

Sets the text color of the view.

```csharp
public static TView TextColor&lt;TView>(this TView view, Tizen.UI.Color textColor)
    where TView : Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.TextExtensions.TextColor&lt;TView>(this TView, Tizen.UI.Color).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color).textColor'></a>

`textColor` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The text color to set.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.TextExtensions.TextColor&lt;TView>(this TView, Tizen.UI.Color).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string)'></a>

## TextExtensions.TextColorFromHex&lt;TView>(this TView, string) Method

Sets the text color of the view from a hexadecimal string.

```csharp
public static TView TextColorFromHex&lt;TView>(this TView view, string textColor)
    where TView : Tizen.UI.IText;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.TextColorFromHex&lt;TView>(this TView, string).TView')

The view instance.

<a name='Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string).textColor'></a>

`textColor` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The text color to set, in hexadecimal format.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.TextExtensions.TextColorFromHex&lt;TView>(this TView, string).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextEnd_TView_(thisTView)'></a>

## TextExtensions.TextEnd&lt;TView>(this TView) Method

Sets the horizontal and vertical alignment of the text in the view to end.

```csharp
public static TView TextEnd&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextEnd_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextEnd_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEnd_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEnd&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEnd_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEnd&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextEndHorizontal_TView_(thisTView)'></a>

## TextExtensions.TextEndHorizontal&lt;TView>(this TView) Method

Sets the horizontal alignment of the text in the view to end.

```csharp
public static TView TextEndHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextEndHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextEndHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEndHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEndHorizontal&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEndHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEndHorizontal&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextEndVertical_TView_(thisTView)'></a>

## TextExtensions.TextEndVertical&lt;TView>(this TView) Method

Sets the vertical alignment of the text in the view to end.

```csharp
public static TView TextEndVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextEndVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextEndVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEndVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEndVertical&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextEndVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextEndVertical&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow)'></a>

## TextExtensions.TextOverflow&lt;TView>(this TView, TextOverflow) Method

Sets whether the text in the TextView should be truncated with an ellipsis when it does not fit within its bounds.

```csharp
public static TView TextOverflow&lt;TView>(this TView view, Tizen.UI.TextOverflow textOverflow)
    where TView : Tizen.UI.ITextFormatting;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow).TView 'Tizen.UI.TextExtensions.TextOverflow&lt;TView>(this TView, Tizen.UI.TextOverflow).TView')

The View instance.

<a name='Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow).textOverflow'></a>

`textOverflow` [TextOverflow](Tizen.UI.TextOverflow.md 'Tizen.UI.TextOverflow')

Text overflow behavior.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextOverflow_TView_(thisTView,Tizen.UI.TextOverflow).TView 'Tizen.UI.TextExtensions.TextOverflow&lt;TView>(this TView, Tizen.UI.TextOverflow).TView')  
The View instance with the specified ellipsis setting.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float)'></a>

## TextExtensions.TextPadding&lt;T>(this T, float) Method

Sets the padding for the text of the view.

```csharp
public static T TextPadding&lt;T>(this T view, float uniformSize)
    where T : Tizen.UI.ITextPadding;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float).view'></a>

`view` [T](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextPadding_T_(thisT,float).T 'Tizen.UI.TextExtensions.TextPadding&lt;T>(this T, float).T')

The view to set the text padding for.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float).uniformSize'></a>

`uniformSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform size of the padding.

#### Returns
[T](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextPadding_T_(thisT,float).T 'Tizen.UI.TextExtensions.TextPadding&lt;T>(this T, float).T')  
The view itself.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float)'></a>

## TextExtensions.TextPadding&lt;T>(this T, float, float, float, float) Method

Sets the padding for the text in the view.

```csharp
public static T TextPadding&lt;T>(this T view, float left, float top, float right, float bottom)
    where T : Tizen.UI.ITextPadding;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).view'></a>

`view` [T](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).T 'Tizen.UI.TextExtensions.TextPadding&lt;T>(this T, float, float, float, float).T')

The view to set the text padding for.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The left padding.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top padding.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The right padding.

<a name='Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom padding.

#### Returns
[T](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextPadding_T_(thisT,float,float,float,float).T 'Tizen.UI.TextExtensions.TextPadding&lt;T>(this T, float, float, float, float).T')  
The view itself.

<a name='Tizen.UI.TextExtensions.TextStart_TView_(thisTView)'></a>

## TextExtensions.TextStart&lt;TView>(this TView) Method

Sets the horizontal and vertical alignment of the text in the view to start.

```csharp
public static TView TextStart&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextStart_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextStart_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStart_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStart&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStart_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStart&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextStartHorizontal_TView_(thisTView)'></a>

## TextExtensions.TextStartHorizontal&lt;TView>(this TView) Method

Sets the horizontal alignment of the text in the view to start.

```csharp
public static TView TextStartHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextStartHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextStartHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStartHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStartHorizontal&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStartHorizontal_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStartHorizontal&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.TextStartVertical_TView_(thisTView)'></a>

## TextExtensions.TextStartVertical&lt;TView>(this TView) Method

Sets the vertical alignment of the text in the view to start.

```csharp
public static TView TextStartVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.TextStartVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.TextExtensions.TextStartVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStartVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStartVertical&lt;TView>(this TView).TView')

The view instance.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.TextStartVertical_TView_(thisTView).TView 'Tizen.UI.TextExtensions.TextStartVertical&lt;TView>(this TView).TView')  
The view instance.

<a name='Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment)'></a>

## TextExtensions.VerticalAlignment&lt;TView>(this TView, TextAlignment) Method

Sets the vertical alignment of the text in the TextView.

```csharp
public static TView VerticalAlignment&lt;TView>(this TView view, Tizen.UI.TextAlignment alignment)
    where TView : Tizen.UI.ITextAlignment;
```
#### Type parameters

<a name='Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).view'></a>

`view` [TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView 'Tizen.UI.TextExtensions.VerticalAlignment&lt;TView>(this TView, Tizen.UI.TextAlignment).TView')

The View instance.

<a name='Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).alignment'></a>

`alignment` [TextAlignment](Tizen.UI.TextAlignment.md 'Tizen.UI.TextAlignment')

The vertical alignment of the text.

#### Returns
[TView](Tizen.UI.TextExtensions.md#Tizen.UI.TextExtensions.VerticalAlignment_TView_(thisTView,Tizen.UI.TextAlignment).TView 'Tizen.UI.TextExtensions.VerticalAlignment&lt;TView>(this TView, Tizen.UI.TextAlignment).TView')  
The View instance with the specified vertical alignment.




