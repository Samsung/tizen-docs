### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ImageExtensions Class

Provides a series of extension methods that support configuring [IImage](Tizen.UI.IImage.md 'Tizen.UI.IImage').

```csharp
public static class ImageExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; ImageExtensions
### Methods

<a name='Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness)'></a>

## ImageExtensions.Border&lt;TView>(this TView, Thickness) Method

Sets the border of the image.

```csharp
public static TView Border&lt;TView>(this TView view, Tizen.UI.Thickness value)
    where TView : Tizen.UI.IImage;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness).view'></a>

`view` [TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.ImageExtensions.Border&lt;TView>(this TView, Tizen.UI.Thickness).TView')

The view instance.

<a name='Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness).value'></a>

`value` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The border of image.

#### Returns
[TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.Border_TView_(thisTView,Tizen.UI.Thickness).TView 'Tizen.UI.ImageExtensions.Border&lt;TView>(this TView, Tizen.UI.Thickness).TView')  
The view instance.

<a name='Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool)'></a>

## ImageExtensions.CropToMask&lt;TView>(this TView, bool) Method

Sets whether the image should be cropped to its mask

```csharp
public static TView CropToMask&lt;TView>(this TView view, bool value)
    where TView : Tizen.UI.IImage;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool).view'></a>

`view` [TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool).TView 'Tizen.UI.ImageExtensions.CropToMask&lt;TView>(this TView, bool).TView')

The view instance.

<a name='Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool).value'></a>

`value` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

The value indicating whether the image should be cropped to its mask.

#### Returns
[TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.CropToMask_TView_(thisTView,bool).TView 'Tizen.UI.ImageExtensions.CropToMask&lt;TView>(this TView, bool).TView')  
The view instance.

<a name='Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode)'></a>

## ImageExtensions.FittingMode&lt;TView>(this TView, FittingMode) Method

Sets the fitting mode used to scale the image to fit the control.

```csharp
public static TView FittingMode&lt;TView>(this TView view, Tizen.UI.FittingMode value)
    where TView : Tizen.UI.IImage;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode).view'></a>

`view` [TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode).TView 'Tizen.UI.ImageExtensions.FittingMode&lt;TView>(this TView, Tizen.UI.FittingMode).TView')

The view instance.

<a name='Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode).value'></a>

`value` [FittingMode](Tizen.UI.FittingMode.md 'Tizen.UI.FittingMode')

The fitting mode.

#### Returns
[TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.FittingMode_TView_(thisTView,Tizen.UI.FittingMode).TView 'Tizen.UI.ImageExtensions.FittingMode&lt;TView>(this TView, Tizen.UI.FittingMode).TView')  
The view instance.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float)'></a>

## ImageExtensions.ImagePadding&lt;T>(this T, float) Method

Sets the image padding for the given image view.

```csharp
public static T ImagePadding&lt;T>(this T view, float uniformSize)
    where T : Tizen.UI.ImageView;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float).T'></a>

`T`

The type of the image view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float).view'></a>

`view` [T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, float).T')

The image view to set the image padding for.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float).uniformSize'></a>

`uniformSize` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The uniform size of the image padding.

#### Returns
[T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, float).T')  
The image view itself.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float)'></a>

## ImageExtensions.ImagePadding&lt;T>(this T, float, float, float, float) Method

Sets the padding for the image within the image view.

```csharp
public static T ImagePadding&lt;T>(this T view, float left, float top, float right, float bottom)
    where T : Tizen.UI.ImageView;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).T'></a>

`T`

The type of the view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).view'></a>

`view` [T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, float, float, float, float).T')

The  image view to set the image padding.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).left'></a>

`left` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The left padding in pixels.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).top'></a>

`top` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The top padding in pixels.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).right'></a>

`right` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The right padding in pixels.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).bottom'></a>

`bottom` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The bottom padding in pixels.

#### Returns
[T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,float,float,float,float).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, float, float, float, float).T')  
The image view itself.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness)'></a>

## ImageExtensions.ImagePadding&lt;T>(this T, Thickness) Method

Sets the image padding for the given image view.

```csharp
public static T ImagePadding&lt;T>(this T view, Tizen.UI.Thickness padding)
    where T : Tizen.UI.ImageView;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness).T'></a>

`T`

The type of the image view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness).view'></a>

`view` [T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, Tizen.UI.Thickness).T')

The image view to set the image padding.

<a name='Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness).padding'></a>

`padding` [Thickness](Tizen.UI.Thickness.md 'Tizen.UI.Thickness')

The padding value to set.

#### Returns
[T](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ImagePadding_T_(thisT,Tizen.UI.Thickness).T 'Tizen.UI.ImageExtensions.ImagePadding&lt;T>(this T, Tizen.UI.Thickness).T')  
The image view itself.

<a name='Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string)'></a>

## ImageExtensions.ResourceUrl&lt;TView>(this TView, string) Method

Sets the [ResourceUrl](Tizen.UI.ImageView.md#Tizen.UI.ImageView.ResourceUrl 'Tizen.UI.ImageView.ResourceUrl') property on an ImageView

```csharp
public static TView ResourceUrl&lt;TView>(this TView view, string resourceUrl)
    where TView : Tizen.UI.IImage;
```
#### Type parameters

<a name='Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string).view'></a>

`view` [TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string).TView 'Tizen.UI.ImageExtensions.ResourceUrl&lt;TView>(this TView, string).TView')

The view instance.

<a name='Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string).resourceUrl'></a>

`resourceUrl` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The resource URL to set.

#### Returns
[TView](Tizen.UI.ImageExtensions.md#Tizen.UI.ImageExtensions.ResourceUrl_TView_(thisTView,string).TView 'Tizen.UI.ImageExtensions.ResourceUrl&lt;TView>(this TView, string).TView')  
The view instance with the specified resource URL.






