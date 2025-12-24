### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## LayoutExtensions Class

Provides a series of extension methods that support positioning Tizen.UI.Views in [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout')s.

```csharp
public static class LayoutExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; LayoutExtensions
### Methods

<a name='Tizen.UI.Layouts.LayoutExtensions.Arrange(thisTizen.UI.View,Tizen.UI.Rect,bool)'></a>

## LayoutExtensions.Arrange(this View, Rect, bool) Method

Arranges the view within the specified rectangle.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static void Arrange(this Tizen.UI.View view, Tizen.UI.Rect rect, bool ignoreRTL=false);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Arrange(thisTizen.UI.View,Tizen.UI.Rect,bool).view'></a>

`view` Tizen.UI.View

The view to arrange.

<a name='Tizen.UI.Layouts.LayoutExtensions.Arrange(thisTizen.UI.View,Tizen.UI.Rect,bool).rect'></a>

`rect` Tizen.UI.Rect

The rectangle within which to arrange the view.

<a name='Tizen.UI.Layouts.LayoutExtensions.Arrange(thisTizen.UI.View,Tizen.UI.Rect,bool).ignoreRTL'></a>

`ignoreRTL` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A flag indicating whether to ignore right-to-left layout direction.

<a name='Tizen.UI.Layouts.LayoutExtensions.Center_TView_(thisTView)'></a>

## LayoutExtensions.Center&lt;TView>(this TView) Method

Sets the horizontal and vertical layout alignment of the view to [Center](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Center 'Tizen.UI.Layouts.LayoutAlignment.Center').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Center&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Center_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Center_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Center_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Center&lt;TView>(this TView).TView')

The view to set the layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Center_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Center&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal_TView_(thisTView)'></a>

## LayoutExtensions.CenterHorizontal&lt;TView>(this TView) Method

Sets the horizontal layout alignment of the view to [Center](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Center 'Tizen.UI.Layouts.LayoutAlignment.Center').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView CenterHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal&lt;TView>(this TView).TView')

The view to set the horizontal layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.CenterHorizontal&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterVertical_TView_(thisTView)'></a>

## LayoutExtensions.CenterVertical&lt;TView>(this TView) Method

Sets the vertical layout alignment of the view to [Center](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Center 'Tizen.UI.Layouts.LayoutAlignment.Center').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView CenterVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.CenterVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.CenterVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.CenterVertical&lt;TView>(this TView).TView')

The view to set the vertical layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.CenterVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.CenterVertical&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.ComputeDesiredSize(thisTizen.UI.View,float,float)'></a>

## LayoutExtensions.ComputeDesiredSize(this View, float, float) Method

Computes the desired size of the specified view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static Tizen.UI.Size ComputeDesiredSize(this Tizen.UI.View view, float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.ComputeDesiredSize(thisTizen.UI.View,float,float).view'></a>

`view` Tizen.UI.View

The view whose desired size should be computed.

<a name='Tizen.UI.Layouts.LayoutExtensions.ComputeDesiredSize(thisTizen.UI.View,float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width constraint.

<a name='Tizen.UI.Layouts.LayoutExtensions.ComputeDesiredSize(thisTizen.UI.View,float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height constraint.

#### Returns
Tizen.UI.Size  
The desired size of the view.

<a name='Tizen.UI.Layouts.LayoutExtensions.End_TView_(thisTView)'></a>

## LayoutExtensions.End&lt;TView>(this TView) Method

Sets the horizontal and vertical layout alignment of the view to [End](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.End 'Tizen.UI.Layouts.LayoutAlignment.End').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView End&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.End_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.End_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.End_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.End&lt;TView>(this TView).TView')

The view to set the layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.End_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.End&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.EndHorizontal_TView_(thisTView)'></a>

## LayoutExtensions.EndHorizontal&lt;TView>(this TView) Method

Sets the horizontal layout alignment of the view to [End](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.End 'Tizen.UI.Layouts.LayoutAlignment.End').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView EndHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.EndHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.EndHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.EndHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.EndHorizontal&lt;TView>(this TView).TView')

The view to set the horizontal layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.EndHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.EndHorizontal&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.EndVertical_TView_(thisTView)'></a>

## LayoutExtensions.EndVertical&lt;TView>(this TView) Method

Sets the vertical layout alignment of the view to [End](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.End 'Tizen.UI.Layouts.LayoutAlignment.End').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView EndVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.EndVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.EndVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.EndVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.EndVertical&lt;TView>(this TView).TView')

The view to set the vertical layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.EndVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.EndVertical&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView)'></a>

## LayoutExtensions.Expand&lt;TView>(this TView) Method

Expands the given view to fill its parent layout.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Expand&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Expand&lt;TView>(this TView).TView')

The view to expand.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Expand&lt;TView>(this TView).TView')  
The same view instance with updated expand property.

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float)'></a>

## LayoutExtensions.Expand&lt;TView>(this TView, float) Method

Sets the expand property of the given view, which determines how much space the view should occupy within HStack/VStack.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Expand&lt;TView>(this TView view, float weight)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Expand&lt;TView>(this TView, float).TView')

The view to set the expand property on.

<a name='Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float).weight'></a>

`weight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The weight value indicating the proportion of space the view should take up relative to other views in the layout.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Expand_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Expand&lt;TView>(this TView, float).TView')  
The same view instance with updated expand property.

<a name='Tizen.UI.Layouts.LayoutExtensions.Fill_TView_(thisTView)'></a>

## LayoutExtensions.Fill&lt;TView>(this TView) Method

Sets the horizontal and vertical layout alignment of the specified Tizen.UI.View instance to [Fill](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Fill 'Tizen.UI.Layouts.LayoutAlignment.Fill').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Fill&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Fill_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Fill_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Fill_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Fill&lt;TView>(this TView).TView')

The view to set the layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Fill_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Fill&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.FillHorizontal_TView_(thisTView)'></a>

## LayoutExtensions.FillHorizontal&lt;TView>(this TView) Method

Sets the horizontal layout alignment of the specified Tizen.UI.View instance to [Fill](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Fill 'Tizen.UI.Layouts.LayoutAlignment.Fill').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView FillHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.FillHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.FillHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.FillHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.FillHorizontal&lt;TView>(this TView).TView')

The view to set the horizontal layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.FillHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.FillHorizontal&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.FillVertical_TView_(thisTView)'></a>

## LayoutExtensions.FillVertical&lt;TView>(this TView) Method

Sets the vertical layout alignment of the specified Tizen.UI.View instance to [Fill](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Fill 'Tizen.UI.Layouts.LayoutAlignment.Fill').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView FillVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.FillVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.FillVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.FillVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.FillVertical&lt;TView>(this TView).TView')

The view to set the vertical layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.FillVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.FillVertical&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment)'></a>

## LayoutExtensions.HorizontalLayoutAlignment&lt;TView>(this TView, LayoutAlignment) Method

Sets the horizontal layout alignment of the view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView HorizontalLayoutAlignment&lt;TView>(this TView view, Tizen.UI.Layouts.LayoutAlignment alignment)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')

The view to set the horizontal layout alignment for.

<a name='Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).alignment'></a>

`alignment` [LayoutAlignment](Tizen.UI.Layouts.LayoutAlignment.md 'Tizen.UI.Layouts.LayoutAlignment')

The horizontal layout alignment to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.HorizontalLayoutAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment)'></a>

## LayoutExtensions.ItemAlignment&lt;TView>(this TView, LayoutAlignment) Method

Sets the item alignment of the stack base layout.<br/>  
This only works if the Tizen.UI.View is included in the  [StackBase](Tizen.UI.Layouts.StackBase.md 'Tizen.UI.Layouts.StackBase') and used.

```csharp
public static TView ItemAlignment&lt;TView>(this TView view, Tizen.UI.Layouts.LayoutAlignment alignment)
    where TView : Tizen.UI.Layouts.StackBase;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView'></a>

`TView`

The type of the stack base.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.ItemAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')

The view to set the item alignment for.

<a name='Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).alignment'></a>

`alignment` [LayoutAlignment](Tizen.UI.Layouts.LayoutAlignment.md 'Tizen.UI.Layouts.LayoutAlignment')

The item alignment to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.ItemAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.ItemAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')  
The stack base itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float)'></a>

## LayoutExtensions.Margin&lt;TView>(this TView, float) Method

Sets the margin of the specified Tizen.UI.View in the layout.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Margin&lt;TView>(this TView view, float uniformSize)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float).TView')

The view to set the margin for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float).uniformSize'></a>

`uniformSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform margin size to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float)'></a>

## LayoutExtensions.Margin&lt;TView>(this TView, float, float) Method

Sets the margin of the specified Tizen.UI.View in the layout.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Margin&lt;TView>(this TView view, float horizontalSize, float verticalSize)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float, float).TView')

The view to set the margin for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).horizontalSize'></a>

`horizontalSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The horizontal margin size to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).verticalSize'></a>

`verticalSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The vertical margin size to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float)'></a>

## LayoutExtensions.Margin&lt;TView>(this TView, float, float, float, float) Method

Sets the margin of the specified [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') instance.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Margin&lt;TView>(this TView view, float left, float top, float right, float bottom)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).TView'></a>

`TView`

The type of the layout.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float, float, float, float).TView')

The layout to set the margin for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The left margin to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top margin to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The right margin to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom margin to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, float, float, float, float).TView')  
The layout itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness)'></a>

## LayoutExtensions.Margin&lt;TView>(this TView, Thickness) Method

Sets the margin of the specified Tizen.UI.View in the layout.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Margin&lt;TView>(this TView view, Tizen.UI.Thickness margin)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, Tizen.UI.Thickness).TView')

The view to set the margin for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness).margin'></a>

`margin` Tizen.UI.Thickness

The margin to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Margin_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.Layouts.LayoutExtensions.Margin&lt;TView>(this TView, Tizen.UI.Thickness).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float)'></a>

## LayoutExtensions.MaximumHeight&lt;TView>(this TView, float) Method

Sets the maximum height of the view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView MaximumHeight&lt;TView>(this TView view, float max)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MaximumHeight&lt;TView>(this TView, float).TView')

The view to set the maximum height for.

<a name='Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float).max'></a>

`max` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The maximum height to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MaximumHeight_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MaximumHeight&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float)'></a>

## LayoutExtensions.MinimumHeight&lt;TView>(this TView, float) Method

Sets the minimum height of the view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView MinimumHeight&lt;TView>(this TView view, float min)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MinimumHeight&lt;TView>(this TView, float).TView')

The view to set the minimum height for.

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float).min'></a>

`min` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The minimum height to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MinimumHeight_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MinimumHeight&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float)'></a>

## LayoutExtensions.MinimumWidth&lt;TView>(this TView, float) Method

Sets the minimum width of the view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView MinimumWidth&lt;TView>(this TView view, float min)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MinimumWidth&lt;TView>(this TView, float).TView')

The view to set the minimum width for.

<a name='Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float).min'></a>

`min` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The minimum width to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.MinimumWidth_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.MinimumWidth&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float)'></a>

## LayoutExtensions.Padding&lt;TView>(this TView, float, float, float, float) Method

Sets the padding of the specified [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') instance.

```csharp
public static TView Padding&lt;TView>(this TView view, float left, float top, float right, float bottom)
    where TView : Tizen.UI.Layouts.Layout;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).TView'></a>

`TView`

The type of the layout.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Padding&lt;TView>(this TView, float, float, float, float).TView')

The layout to set the padding for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The left padding to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top padding to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The right padding to set.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom padding to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Padding&lt;TView>(this TView, float, float, float, float).TView')  
The layout itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness)'></a>

## LayoutExtensions.Padding&lt;TView>(this TView, Thickness) Method

Sets the padding of the specified [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') instance.

```csharp
public static TView Padding&lt;TView>(this TView view, Tizen.UI.Thickness padding)
    where TView : Tizen.UI.Layouts.Layout;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness).TView'></a>

`TView`

The type of the layout.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.Layouts.LayoutExtensions.Padding&lt;TView>(this TView, Tizen.UI.Thickness).TView')

The layout to set the padding for.

<a name='Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness).padding'></a>

`padding` Tizen.UI.Thickness

The padding to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Padding_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.Layouts.LayoutExtensions.Padding&lt;TView>(this TView, Tizen.UI.Thickness).TView')  
The layout itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Start_TView_(thisTView)'></a>

## LayoutExtensions.Start&lt;TView>(this TView) Method

Sets the horizontal and vertical layout alignment of the specified Tizen.UI.View instance to [Start](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Start 'Tizen.UI.Layouts.LayoutAlignment.Start').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView Start&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Start_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Start_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Start_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Start&lt;TView>(this TView).TView')

The view to set the layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Start_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.Start&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.StartHorizontal_TView_(thisTView)'></a>

## LayoutExtensions.StartHorizontal&lt;TView>(this TView) Method

Sets the horizontal layout alignment of the specified Tizen.UI.View instance to [Start](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Start 'Tizen.UI.Layouts.LayoutAlignment.Start').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView StartHorizontal&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.StartHorizontal_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.StartHorizontal_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.StartHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.StartHorizontal&lt;TView>(this TView).TView')

The view to set the horizontal layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.StartHorizontal_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.StartHorizontal&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.StartVertical_TView_(thisTView)'></a>

## LayoutExtensions.StartVertical&lt;TView>(this TView) Method

Sets the vertical layout alignment of the specified Tizen.UI.View instance to [Start](Tizen.UI.Layouts.LayoutAlignment.md#Tizen.UI.Layouts.LayoutAlignment.Start 'Tizen.UI.Layouts.LayoutAlignment.Start').<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView StartVertical&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.StartVertical_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.StartVertical_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.StartVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.StartVertical&lt;TView>(this TView).TView')

The view to set the vertical layout alignment for.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.StartVertical_TView_(thisTView).TView 'Tizen.UI.Layouts.LayoutExtensions.StartVertical&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float)'></a>

## LayoutExtensions.Translate&lt;TView>(this TView, float, float) Method

Translates the position of the specified view by the given x and y offsets.  
This extension method applies a translation transformation to the view's layout.

```csharp
public static TView Translate&lt;TView>(this TView view, float x, float y)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).TView'></a>

`TView`
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Translate&lt;TView>(this TView, float, float).TView')

<a name='Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.Translate_TView_(thisTView,float,float).TView 'Tizen.UI.Layouts.LayoutExtensions.Translate&lt;TView>(this TView, float, float).TView')

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float)'></a>

## LayoutExtensions.TranslateX&lt;TView>(this TView, float) Method

Sets the horizontal translation value applied to the view, which affects its layout position.

```csharp
public static TView TranslateX&lt;TView>(this TView view, float x)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.TranslateX&lt;TView>(this TView, float).TView')

The target view to apply the horizontal translation to.

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The X-coordinate value by which to translate the view.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.TranslateX_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.TranslateX&lt;TView>(this TView, float).TView')

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float)'></a>

## LayoutExtensions.TranslateY&lt;TView>(this TView, float) Method

Sets the vertical translation value applied to the view, which affects its layout position.

```csharp
public static TView TranslateY&lt;TView>(this TView view, float y)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.TranslateY&lt;TView>(this TView, float).TView')

The target view to apply the vertically translation to.

<a name='Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The Y-coordinate value by which to translate the view.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.TranslateY_TView_(thisTView,float).TView 'Tizen.UI.Layouts.LayoutExtensions.TranslateY&lt;TView>(this TView, float).TView')

<a name='Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment)'></a>

## LayoutExtensions.VerticalLayoutAlignment&lt;TView>(this TView, LayoutAlignment) Method

Sets the vertical layout alignment of the view.<br/>  
This only works if the Tizen.UI.View is included in the  [Layout](Tizen.UI.Layouts.Layout.md 'Tizen.UI.Layouts.Layout') and used.

```csharp
public static TView VerticalLayoutAlignment&lt;TView>(this TView view, Tizen.UI.Layouts.LayoutAlignment alignment)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).view'></a>

`view` [TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')

The view to set the vertical layout alignment for.

<a name='Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).alignment'></a>

`alignment` [LayoutAlignment](Tizen.UI.Layouts.LayoutAlignment.md 'Tizen.UI.Layouts.LayoutAlignment')

The vertical layout alignment to set.

#### Returns
[TView](Tizen.UI.Layouts.LayoutExtensions.md#Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment_TView_(thisTView,Tizen.UI.Layouts.LayoutAlignment).TView 'Tizen.UI.Layouts.LayoutExtensions.VerticalLayoutAlignment&lt;TView>(this TView, Tizen.UI.Layouts.LayoutAlignment).TView')  
The view itself.































































