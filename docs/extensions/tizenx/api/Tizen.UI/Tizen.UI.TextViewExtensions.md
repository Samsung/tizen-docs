### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## TextViewExtensions Class

Provides a series of extension methods that support configuring a [TextView](Tizen.UI.TextView.md 'Tizen.UI.TextView').

```csharp
public static class TextViewExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; TextViewExtensions
### Methods

<a name='Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow)'></a>

## TextViewExtensions.EllipsisPosition&lt;TView>(this TView, TextOverflow) Method

Sets the position of the ellipsis in the TextView when the text is truncated.

```csharp
public static TView EllipsisPosition&lt;TView>(this TView view, Tizen.UI.TextOverflow position)
    where TView : Tizen.UI.TextView;
```
#### Type parameters

<a name='Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow).view'></a>

`view` [TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow).TView 'Tizen.UI.TextViewExtensions.EllipsisPosition&lt;TView>(this TView, Tizen.UI.TextOverflow).TView')

The TextView instance.

<a name='Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow).position'></a>

`position` [TextOverflow](Tizen.UI.TextOverflow.md 'Tizen.UI.TextOverflow')

The position of the ellipsis.

#### Returns
[TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.EllipsisPosition_TView_(thisTView,Tizen.UI.TextOverflow).TView 'Tizen.UI.TextViewExtensions.EllipsisPosition&lt;TView>(this TView, Tizen.UI.TextOverflow).TView')  
The TextView instance with the specified ellipsis position.

<a name='Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool)'></a>

## TextViewExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool) Method

Sets whether the line height is absolute or relative.

```csharp
public static TView IsAbsoluteLineHeight&lt;TView>(this TView view, bool isAbsoluteLineHeight)
    where TView : Tizen.UI.TextView;
```
#### Type parameters

<a name='Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView 'Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool).TView')

The TextView instance.

<a name='Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).isAbsoluteLineHeight'></a>

`isAbsoluteLineHeight` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the value of line height is absolute value, false otherwise.

#### Returns
[TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight_TView_(thisTView,bool).TView 'Tizen.UI.TextViewExtensions.IsAbsoluteLineHeight&lt;TView>(this TView, bool).TView')  
The TextView instance.

<a name='Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool)'></a>

## TextViewExtensions.IsMarkupEnabled&lt;TView>(this TView, bool) Method

Sets whether the text in the TextView should support markup.

```csharp
public static TView IsMarkupEnabled&lt;TView>(this TView view, bool enable)
    where TView : Tizen.UI.TextView;
```
#### Type parameters

<a name='Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool).TView 'Tizen.UI.TextViewExtensions.IsMarkupEnabled&lt;TView>(this TView, bool).TView')

The TextView instance.

<a name='Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool).enable'></a>

`enable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

True if the text should support markup, false otherwise.

#### Returns
[TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.IsMarkupEnabled_TView_(thisTView,bool).TView 'Tizen.UI.TextViewExtensions.IsMarkupEnabled&lt;TView>(this TView, bool).TView')  
The TextView instance with the specified markup support setting.

<a name='Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode)'></a>

## TextViewExtensions.LineBreakMode&lt;TView>(this TView, LineBreakMode) Method

Sets the line break mode of the text in the TextView.

```csharp
public static TView LineBreakMode&lt;TView>(this TView view, Tizen.UI.LineBreakMode mode)
    where TView : Tizen.UI.TextView;
```
#### Type parameters

<a name='Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode).view'></a>

`view` [TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode).TView 'Tizen.UI.TextViewExtensions.LineBreakMode&lt;TView>(this TView, Tizen.UI.LineBreakMode).TView')

The TextView instance.

<a name='Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode).mode'></a>

`mode` [LineBreakMode](Tizen.UI.LineBreakMode.md 'Tizen.UI.LineBreakMode')

The line break mode of the text.

#### Returns
[TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.LineBreakMode_TView_(thisTView,Tizen.UI.LineBreakMode).TView 'Tizen.UI.TextViewExtensions.LineBreakMode&lt;TView>(this TView, Tizen.UI.LineBreakMode).TView')  
The TextView instance with the specified line break mode.

<a name='Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float)'></a>

## TextViewExtensions.LineHeight&lt;TView>(this TView, float) Method

Sets the line height of the TextView.

```csharp
public static TView LineHeight&lt;TView>(this TView view, float height)
    where TView : Tizen.UI.TextView;
```
#### Type parameters

<a name='Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float).TView'></a>

`TView`

The type of the View.
#### Parameters

<a name='Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float).TView 'Tizen.UI.TextViewExtensions.LineHeight&lt;TView>(this TView, float).TView')

The TextView instance.

<a name='Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative line height.

#### Returns
[TView](Tizen.UI.TextViewExtensions.md#Tizen.UI.TextViewExtensions.LineHeight_TView_(thisTView,float).TView 'Tizen.UI.TextViewExtensions.LineHeight&lt;TView>(this TView, float).TView')  
The TextView instance with the specified relative line height.




