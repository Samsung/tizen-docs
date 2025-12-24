### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ViewExtensions Class

Provides a series of extension methods that support configuring the alignment of controls inheriting from [View](Tizen.UI.View.md 'Tizen.UI.View').

```csharp
public static class ViewExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ViewExtensions
### Methods

<a name='Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U)'></a>

## ViewExtensions.Attach&lt;T,U>(this T, U) Method

Attaches an object to the view.

```csharp
public static T Attach&lt;T,U>(this T view, U value)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).T'></a>

`T`

The type of the view.

<a name='Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).U'></a>

`U`

The type of the object to attach.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).T 'Tizen.UI.ViewExtensions.Attach&lt;T,U>(this T, U).T')

The view to attach the object to.

<a name='Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).value'></a>

`value` [U](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).U 'Tizen.UI.ViewExtensions.Attach&lt;T,U>(this T, U).U')

The object to attach.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Attach_T,U_(thisT,U).T 'Tizen.UI.ViewExtensions.Attach&lt;T,U>(this T, U).T')  
The view with the attached object.

<a name='Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background)'></a>

## ViewExtensions.Background&lt;T>(this T, Background) Method

Sets the background of the view using a background visual.

```csharp
public static T Background&lt;T>(this T view, Tizen.UI.Background background)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background).T 'Tizen.UI.ViewExtensions.Background&lt;T>(this T, Tizen.UI.Background).T')

The view to set the background for.

<a name='Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background).background'></a>

`background` [Background](Tizen.UI.Background.md 'Tizen.UI.Background')

The background visual to use as the background.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Background_T_(thisT,Tizen.UI.Background).T 'Tizen.UI.ViewExtensions.Background&lt;T>(this T, Tizen.UI.Background).T')  
The view itself, to allow for method chaining.

<a name='Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color)'></a>

## ViewExtensions.BackgroundColor&lt;TView>(this TView, Color) Method

Sets the background color of the view.

```csharp
public static TView BackgroundColor&lt;TView>(this TView view, Tizen.UI.Color color)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.ViewExtensions.BackgroundColor&lt;TView>(this TView, Tizen.UI.Color).TView')

The view to set the background color for.

<a name='Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The background color of the view.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BackgroundColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.ViewExtensions.BackgroundColor&lt;TView>(this TView, Tizen.UI.Color).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string)'></a>

## ViewExtensions.BackgroundColorFromHex&lt;TView>(this TView, string) Method

Sets the background color of the view using a hex string.

```csharp
public static TView BackgroundColorFromHex&lt;TView>(this TView view, string color)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.ViewExtensions.BackgroundColorFromHex&lt;TView>(this TView, string).TView')

The view to set the background color for.

<a name='Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string).color'></a>

`color` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The background color of the view in hex format.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BackgroundColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.ViewExtensions.BackgroundColorFromHex&lt;TView>(this TView, string).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color)'></a>

## ViewExtensions.BorderlineColor&lt;TView>(this TView, Color) Method

Sets the borderline color of the view.

```csharp
public static TView BorderlineColor&lt;TView>(this TView view, Tizen.UI.Color color)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.ViewExtensions.BorderlineColor&lt;TView>(this TView, Tizen.UI.Color).TView')

The view to set the borderline color.

<a name='Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color).color'></a>

`color` [Color](Tizen.UI.Color.md 'Tizen.UI.Color')

The borderline color to set.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineColor_TView_(thisTView,Tizen.UI.Color).TView 'Tizen.UI.ViewExtensions.BorderlineColor&lt;TView>(this TView, Tizen.UI.Color).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string)'></a>

## ViewExtensions.BorderlineColorFromHex&lt;TView>(this TView, string) Method

Sets the borderline color of the view using a hex string.

```csharp
public static TView BorderlineColorFromHex&lt;TView>(this TView view, string color)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.ViewExtensions.BorderlineColorFromHex&lt;TView>(this TView, string).TView')

The view to set the borderline color for.

<a name='Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string).color'></a>

`color` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The borderline color of the view in hex format.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineColorFromHex_TView_(thisTView,string).TView 'Tizen.UI.ViewExtensions.BorderlineColorFromHex&lt;TView>(this TView, string).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float)'></a>

## ViewExtensions.BorderlineOffset&lt;TView>(this TView, float) Method

Sets the borderline offset of the view.

```csharp
public static TView BorderlineOffset&lt;TView>(this TView view, float offset)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.BorderlineOffset&lt;TView>(this TView, float).TView')

The view to set the borderline offest.

<a name='Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float).offset'></a>

`offset` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The borderline offset to set.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineOffset_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.BorderlineOffset&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float)'></a>

## ViewExtensions.BorderlineWidth&lt;TView>(this TView, float) Method

Sets the borderline width of the view.

```csharp
public static TView BorderlineWidth&lt;TView>(this TView view, float width)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.BorderlineWidth&lt;TView>(this TView, float).TView')

The view to set the borderline width.

<a name='Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The borderline width to set.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.BorderlineWidth_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.BorderlineWidth&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius)'></a>

## ViewExtensions.CornerRadius&lt;TView>(this TView, CornerRadius) Method

Sets the corner radius of the view.

```csharp
public static TView CornerRadius&lt;TView>(this TView view, Tizen.UI.CornerRadius cornerRadius)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius).TView 'Tizen.UI.ViewExtensions.CornerRadius&lt;TView>(this TView, Tizen.UI.CornerRadius).TView')

The view to set the corner radius.

<a name='Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius).cornerRadius'></a>

`cornerRadius` [CornerRadius](Tizen.UI.CornerRadius.md 'Tizen.UI.CornerRadius')

The corner radius to set.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.CornerRadius_TView_(thisTView,Tizen.UI.CornerRadius).TView 'Tizen.UI.ViewExtensions.CornerRadius&lt;TView>(this TView, Tizen.UI.CornerRadius).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float)'></a>

## ViewExtensions.DesiredHeight&lt;TView>(this TView, float) Method

Sets the desired height of the view.

```csharp
public static TView DesiredHeight&lt;TView>(this TView view, float height)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.DesiredHeight&lt;TView>(this TView, float).TView')

The view to set the desired height for.

<a name='Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired height of the view.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredHeight_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.DesiredHeight&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float)'></a>

## ViewExtensions.DesiredSize&lt;TView>(this TView, float, float) Method

Sets the desired size of the view.

```csharp
public static TView DesiredSize&lt;TView>(this TView view, float width, float height)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).TView 'Tizen.UI.ViewExtensions.DesiredSize&lt;TView>(this TView, float, float).TView')

The view to set the desired size for.

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired width of the view.

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired height of the view.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,float,float).TView 'Tizen.UI.ViewExtensions.DesiredSize&lt;TView>(this TView, float, float).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size)'></a>

## ViewExtensions.DesiredSize&lt;TView>(this TView, Size) Method

Sets the desired size of the view.

```csharp
public static TView DesiredSize&lt;TView>(this TView view, Tizen.UI.Size size)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size).TView'></a>

`TView`
#### Parameters

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size).TView 'Tizen.UI.ViewExtensions.DesiredSize&lt;TView>(this TView, Tizen.UI.Size).TView')

The view to set the desired size for.

<a name='Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size).size'></a>

`size` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The desired size to set.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredSize_TView_(thisTView,Tizen.UI.Size).TView 'Tizen.UI.ViewExtensions.DesiredSize&lt;TView>(this TView, Tizen.UI.Size).TView')  
The view with the desired size set.

<a name='Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float)'></a>

## ViewExtensions.DesiredWidth&lt;TView>(this TView, float) Method

Sets the desired width of the view.

```csharp
public static TView DesiredWidth&lt;TView>(this TView view, float width)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.DesiredWidth&lt;TView>(this TView, float).TView')

The view to set the desired width for.

<a name='Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The desired width of the view.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.DesiredWidth_TView_(thisTView,float).TView 'Tizen.UI.ViewExtensions.DesiredWidth&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool)'></a>

## ViewExtensions.Focusable&lt;TView>(this TView, bool) Method

Sets a value indicating whether the view can receive keyboard focus.

```csharp
public static TView Focusable&lt;TView>(this TView view, bool focusable)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool).TView'></a>

`TView`

The view inheriting from [View](Tizen.UI.View.md 'Tizen.UI.View').
#### Parameters

<a name='Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.Focusable&lt;TView>(this TView, bool).TView')

The target view.

<a name='Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool).focusable'></a>

`focusable` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Focusable_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.Focusable&lt;TView>(this TView, bool).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool)'></a>

## ViewExtensions.FocusableChildren&lt;TView>(this TView, bool) Method

Sets a value indicating whether the view can receive keyboard focus.

```csharp
public static TView FocusableChildren&lt;TView>(this TView view, bool focusableChildren)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool).TView'></a>

`TView`

The view inheriting from [View](Tizen.UI.View.md 'Tizen.UI.View').
#### Parameters

<a name='Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.FocusableChildren&lt;TView>(this TView, bool).TView')

The target view.

<a name='Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool).focusableChildren'></a>

`focusableChildren` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A boolean value whether the view make focusableChildren or not.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.FocusableChildren_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.FocusableChildren&lt;TView>(this TView, bool).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool)'></a>

## ViewExtensions.FocusableInTouch&lt;TView>(this TView, bool) Method

Sets whether the view can receive focus through touch events.

```csharp
public static TView FocusableInTouch&lt;TView>(this TView view, bool focusableInTouch)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool).TView'></a>

`TView`

The view inheriting from [View](Tizen.UI.View.md 'Tizen.UI.View').
#### Parameters

<a name='Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.FocusableInTouch&lt;TView>(this TView, bool).TView')

The target view.

<a name='Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool).focusableInTouch'></a>

`focusableInTouch` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

A boolean value whether the view make focusableInTouch or not.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.FocusableInTouch_TView_(thisTView,bool).TView 'Tizen.UI.ViewExtensions.FocusableInTouch&lt;TView>(this TView, bool).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.IsDescendantOf(thisTizen.UI.View,Tizen.UI.View)'></a>

## ViewExtensions.IsDescendantOf(this View, View) Method

Checks if the given view is a descendant of the specified parent view.

```csharp
public static bool IsDescendantOf(this Tizen.UI.View view, Tizen.UI.View parent);
```
#### Parameters

<a name='Tizen.UI.ViewExtensions.IsDescendantOf(thisTizen.UI.View,Tizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to check.

<a name='Tizen.UI.ViewExtensions.IsDescendantOf(thisTizen.UI.View,Tizen.UI.View).parent'></a>

`parent` [View](Tizen.UI.View.md 'Tizen.UI.View')

The parent view to compare with.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the view is a descendant of the parent, otherwise false.

<a name='Tizen.UI.ViewExtensions.Name_T_(thisT,string)'></a>

## ViewExtensions.Name&lt;T>(this T, string) Method

Sets the name of the view.

```csharp
public static T Name&lt;T>(this T view, string name)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Name_T_(thisT,string).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Name_T_(thisT,string).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Name_T_(thisT,string).T 'Tizen.UI.ViewExtensions.Name&lt;T>(this T, string).T')

The view the name for.

<a name='Tizen.UI.ViewExtensions.Name_T_(thisT,string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name to set.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Name_T_(thisT,string).T 'Tizen.UI.ViewExtensions.Name&lt;T>(this T, string).T')  
The view with the name set.

<a name='Tizen.UI.ViewExtensions.Position(thisTizen.UI.View)'></a>

## ViewExtensions.Position(this View) Method

Gets the position of the view.

```csharp
public static Tizen.UI.Point Position(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ViewExtensions.Position(thisTizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the position for.

#### Returns
[Point](Tizen.UI.Point.md 'Tizen.UI.Point')  
The position of the view.

<a name='Tizen.UI.ViewExtensions.Scale(thisTizen.UI.View)'></a>

## ViewExtensions.Scale(this View) Method

Gets the scale of the view.

```csharp
public static Tizen.UI.Size Scale(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ViewExtensions.Scale(thisTizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the scale for.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The scale of the view.

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float)'></a>

## ViewExtensions.Scale&lt;T>(this T, float, float) Method

Sets the scale of the view.

```csharp
public static T Scale&lt;T>(this T view, float scaleX, float scaleY)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).T 'Tizen.UI.ViewExtensions.Scale&lt;T>(this T, float, float).T')

The view to set the scale for.

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).scaleX'></a>

`scaleX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scaleX of the view.

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).scaleY'></a>

`scaleY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scaleY of the view.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Scale_T_(thisT,float,float).T 'Tizen.UI.ViewExtensions.Scale&lt;T>(this T, float, float).T')  
The view itself.

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size)'></a>

## ViewExtensions.Scale&lt;T>(this T, Size) Method

Sets the scale of the view.

```csharp
public static T Scale&lt;T>(this T view, Tizen.UI.Size scale)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size).T 'Tizen.UI.ViewExtensions.Scale&lt;T>(this T, Tizen.UI.Size).T')

The view to set the scale for.

<a name='Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size).scale'></a>

`scale` [Size](Tizen.UI.Size.md 'Tizen.UI.Size')

The scale to set.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Scale_T_(thisT,Tizen.UI.Size).T 'Tizen.UI.ViewExtensions.Scale&lt;T>(this T, Tizen.UI.Size).T')  
The view itself.

<a name='Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float)'></a>

## ViewExtensions.ScaleX&lt;T>(this T, float) Method

Sets the scaleX of the view.

```csharp
public static T ScaleX&lt;T>(this T view, float scaleX)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float).T 'Tizen.UI.ViewExtensions.ScaleX&lt;T>(this T, float).T')

The view to set the scaleX for.

<a name='Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float).scaleX'></a>

`scaleX` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scaleX of the view.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.ScaleX_T_(thisT,float).T 'Tizen.UI.ViewExtensions.ScaleX&lt;T>(this T, float).T')  
The view itself.

<a name='Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float)'></a>

## ViewExtensions.ScaleY&lt;T>(this T, float) Method

Sets the scaleY of the view.

```csharp
public static T ScaleY&lt;T>(this T view, float scaleY)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float).T 'Tizen.UI.ViewExtensions.ScaleY&lt;T>(this T, float).T')

The view to set the scaleY for.

<a name='Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float).scaleY'></a>

`scaleY` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The scaleY of the view.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.ScaleY_T_(thisT,float).T 'Tizen.UI.ViewExtensions.ScaleY&lt;T>(this T, float).T')  
The view itself.

<a name='Tizen.UI.ViewExtensions.ScreenScaledBounds(thisTizen.UI.View)'></a>

## ViewExtensions.ScreenScaledBounds(this View) Method

Returns the screen-scaled bounds of the view.

```csharp
public static Tizen.UI.Rect ScreenScaledBounds(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ViewExtensions.ScreenScaledBounds(thisTizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the screen-scaled bounds for.

#### Returns
[Rect](Tizen.UI.Rect.md 'Tizen.UI.Rect')  
A rectangle representing the screen-scaled bounds of the view.

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_)'></a>

## ViewExtensions.Self&lt;TView>(this TView, Action&lt;TView>) Method

Invokes an action on the specified view.

```csharp
public static TView Self&lt;TView>(this TView view, System.Action&lt;TView> action)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, System.Action&lt;TView>).TView')

The view to which the action will be applied.

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).action'></a>

`action` [System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, System.Action&lt;TView>).TView')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-1 'System.Action`1')

The action to invoke on the view.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,System.Action_TView_).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, System.Action&lt;TView>).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView)'></a>

## ViewExtensions.Self&lt;TView>(this TView, TView) Method

Assign this view reference to the given variable.

```csharp
public static TView Self&lt;TView>(this TView view, out TView variable)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).view'></a>

`view` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, TView).TView')

<a name='Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).variable'></a>

`variable` [TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, TView).TView')

The variable to save the reference to.

#### Returns
[TView](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Self_TView_(thisTView,TView).TView 'Tizen.UI.ViewExtensions.Self&lt;TView>(this TView, TView).TView')  
The view itself.

<a name='Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow)'></a>

## ViewExtensions.Shadow&lt;T>(this T, Shadow) Method

Sets the shadow of the view.

```csharp
public static T Shadow&lt;T>(this T view, Tizen.UI.Shadow shadow)
    where T : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow).view'></a>

`view` [T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow).T 'Tizen.UI.ViewExtensions.Shadow&lt;T>(this T, Tizen.UI.Shadow).T')

The view to set the shadow for.

<a name='Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow).shadow'></a>

`shadow` [Shadow](Tizen.UI.Shadow.md 'Tizen.UI.Shadow')

The shadow object to apply to the view.

#### Returns
[T](Tizen.UI.ViewExtensions.md#Tizen.UI.ViewExtensions.Shadow_T_(thisT,Tizen.UI.Shadow).T 'Tizen.UI.ViewExtensions.Shadow&lt;T>(this T, Tizen.UI.Shadow).T')  
The view itself, to allow method chaining.

<a name='Tizen.UI.ViewExtensions.Size(thisTizen.UI.View)'></a>

## ViewExtensions.Size(this View) Method

Gets the size of the view.

```csharp
public static Tizen.UI.Size Size(this Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.ViewExtensions.Size(thisTizen.UI.View).view'></a>

`view` [View](Tizen.UI.View.md 'Tizen.UI.View')

The view to get the size for.

#### Returns
[Size](Tizen.UI.Size.md 'Tizen.UI.Size')  
The size of the view.




