### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## AbsoluteLayoutExtensions Class

Provides a series of extension methods that support positioning [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')s in [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout')s.

```csharp
public static class AbsoluteLayoutExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; AbsoluteLayoutExtensions
### Methods

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float)'></a>

## AbsoluteLayoutExtensions.LayoutBounds&lt;TView>(this TView, float, float, float, float) Method

Sets the position and size of a [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') in an [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout').<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout') and used.

```csharp
public static TView LayoutBounds&lt;TView>(this TView view, float x, float y, float width, float height)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).view'></a>

`view` [TView](Tizen.UI.Layouts.AbsoluteLayoutExtensions.md#Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds&lt;TView>(this TView, float, float, float, float).TView')

The view to set the layout bounds for.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).x'></a>

`x` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The x position of the view.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).y'></a>

`y` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The y position of the view.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the view.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the view.

#### Returns
[TView](Tizen.UI.Layouts.AbsoluteLayoutExtensions.md#Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds_TView_(thisTView,float,float,float,float).TView 'Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutBounds&lt;TView>(this TView, float, float, float, float).TView')  
The view itself, to allow for method chaining.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags)'></a>

## AbsoluteLayoutExtensions.LayoutFlags&lt;TView>(this TView, AbsoluteLayoutFlags) Method

Set a flag that indicates that the layout bounds position and size values for a child are proportional to the size of the [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout').<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [AbsoluteLayout](Tizen.UI.Layouts.AbsoluteLayout.md 'Tizen.UI.Layouts.AbsoluteLayout') and used.

```csharp
public static TView LayoutFlags&lt;TView>(this TView view, Tizen.UI.Layouts.AbsoluteLayoutFlags flag)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags).view'></a>

`view` [TView](Tizen.UI.Layouts.AbsoluteLayoutExtensions.md#Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags).TView 'Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags&lt;TView>(this TView, Tizen.UI.Layouts.AbsoluteLayoutFlags).TView')

The view to set the layout flags for.

<a name='Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags).flag'></a>

`flag` [AbsoluteLayoutFlags](Tizen.UI.Layouts.AbsoluteLayoutFlags.md 'Tizen.UI.Layouts.AbsoluteLayoutFlags')

The layout flag to set.

#### Returns
[TView](Tizen.UI.Layouts.AbsoluteLayoutExtensions.md#Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags_TView_(thisTView,Tizen.UI.Layouts.AbsoluteLayoutFlags).TView 'Tizen.UI.Layouts.AbsoluteLayoutExtensions.LayoutFlags&lt;TView>(this TView, Tizen.UI.Layouts.AbsoluteLayoutFlags).TView')  
The view itself, to allow for method chaining.






























































