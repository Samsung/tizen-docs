### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## FlexBoxExtensions Class

Provides a series of extension methods that support positioning a [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') in a [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox').

```csharp
public static class FlexBoxExtensions
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; FlexBoxExtensions
### Methods

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems)'></a>

## FlexBoxExtensions.AlignItems&lt;TView>(this TView, FlexAlignItems) Method

Sets the align-items property of the FlexBox.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView AlignItems&lt;TView>(this TView view, Tizen.UI.Layouts.FlexAlignItems alignItems)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AlignItems&lt;TView>(this TView, Tizen.UI.Layouts.FlexAlignItems).TView')

The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems).alignItems'></a>

`alignItems` [FlexAlignItems](Tizen.UI.Layouts.FlexAlignItems.md 'Tizen.UI.Layouts.FlexAlignItems')

The align-items value to set.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AlignItems_TView_(thisTView,Tizen.UI.Layouts.FlexAlignItems).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AlignItems&lt;TView>(this TView, Tizen.UI.Layouts.FlexAlignItems).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf)'></a>

## FlexBoxExtensions.AlignSelf&lt;TView>(this TView, FlexAlignSelf) Method

Sets the align-self property of the view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView AlignSelf&lt;TView>(this TView view, Tizen.UI.Layouts.FlexAlignSelf alignSelf)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf&lt;TView>(this TView, Tizen.UI.Layouts.FlexAlignSelf).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf).alignSelf'></a>

`alignSelf` [FlexAlignSelf](Tizen.UI.Layouts.FlexAlignSelf.md 'Tizen.UI.Layouts.FlexAlignSelf')

The align-self value.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf_TView_(thisTView,Tizen.UI.Layouts.FlexAlignSelf).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AlignSelf&lt;TView>(this TView, Tizen.UI.Layouts.FlexAlignSelf).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign_TView_(thisTView)'></a>

## FlexBoxExtensions.AutoAlign&lt;TView>(this TView) Method

Sets the align-self property of the view to auto.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView AutoAlign&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AutoAlign&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis_TView_(thisTView)'></a>

## FlexBoxExtensions.AutoBasis&lt;TView>(this TView) Method

Sets the flex basis property of the view to auto.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView AutoBasis&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.AutoBasis&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float)'></a>

## FlexBoxExtensions.Basis&lt;TView>(this TView, float) Method

Sets the flex basis property of the view to an absolute value.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Basis&lt;TView>(this TView view, float length)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Basis&lt;TView>(this TView, float).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float).length'></a>

`length` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The absolute length of the basis.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Basis_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Basis&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign_TView_(thisTView)'></a>

## FlexBoxExtensions.CenterAlign&lt;TView>(this TView) Method

Sets the align-self property of the view to center.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView CenterAlign&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterAlign&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterItems_TView_(thisTView)'></a>

## FlexBoxExtensions.CenterItems&lt;TView>(this TView) Method

Sets the align-items property of the FlexBox to center.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView CenterItems&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterItems_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterItems_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterItems&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterItems&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.CenterJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to center.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView CenterJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.CenterJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Column_TView_(thisTView)'></a>

## FlexBoxExtensions.Column&lt;TView>(this TView) Method

Sets the direction of the FlexBox to column.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Column&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Column_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Column_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Column_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Column&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Column_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Column&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse_TView_(thisTView)'></a>

## FlexBoxExtensions.ColumnReverse&lt;TView>(this TView) Method

Sets the direction of the FlexBox to column-reverse.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView ColumnReverse&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.ColumnReverse&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection)'></a>

## FlexBoxExtensions.Direction&lt;TView>(this TView, FlexDirection) Method

Sets the direction of the FlexBox.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Direction&lt;TView>(this TView view, Tizen.UI.Layouts.FlexDirection direction)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Direction&lt;TView>(this TView, Tizen.UI.Layouts.FlexDirection).TView')

The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection).direction'></a>

`direction` [FlexDirection](Tizen.UI.Layouts.FlexDirection.md 'Tizen.UI.Layouts.FlexDirection')

The direction to set.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Direction_TView_(thisTView,Tizen.UI.Layouts.FlexDirection).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Direction&lt;TView>(this TView, Tizen.UI.Layouts.FlexDirection).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndAlign_TView_(thisTView)'></a>

## FlexBoxExtensions.EndAlign&lt;TView>(this TView) Method

Sets the align-self property of the view to end.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView EndAlign&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndAlign_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndAlign_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndAlign&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndAlign&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndItems_TView_(thisTView)'></a>

## FlexBoxExtensions.EndItems&lt;TView>(this TView) Method

Sets the align-items property of the FlexBox to end.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView EndItems&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndItems_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndItems_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndItems&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndItems&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.EndJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to end.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView EndJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.EndJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.EndJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.EndJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float)'></a>

## FlexBoxExtensions.Grow&lt;TView>(this TView, float) Method

Sets the flex grow property of the view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Grow&lt;TView>(this TView view, float grow)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Grow&lt;TView>(this TView, float).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float).grow'></a>

`grow` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The flex grow value.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Grow_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Grow&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify)'></a>

## FlexBoxExtensions.JustifyContent&lt;TView>(this TView, FlexJustify) Method

Sets the justify-content property of the FlexBox.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView JustifyContent&lt;TView>(this TView view, Tizen.UI.Layouts.FlexJustify justifyContent)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify).TView 'Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent&lt;TView>(this TView, Tizen.UI.Layouts.FlexJustify).TView')

The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify).justifyContent'></a>

`justifyContent` [FlexJustify](Tizen.UI.Layouts.FlexJustify.md 'Tizen.UI.Layouts.FlexJustify')

The justify-content value to set.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent_TView_(thisTView,Tizen.UI.Layouts.FlexJustify).TView 'Tizen.UI.Layouts.FlexBoxExtensions.JustifyContent&lt;TView>(this TView, Tizen.UI.Layouts.FlexJustify).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int)'></a>

## FlexBoxExtensions.Order&lt;TView>(this TView, int) Method

Sets the order property of the view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Order&lt;TView>(this TView view, int order)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Order&lt;TView>(this TView, int).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int).order'></a>

`order` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The order value.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Order_TView_(thisTView,int).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Order&lt;TView>(this TView, int).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float)'></a>

## FlexBoxExtensions.RelativeBasis&lt;TView>(this TView, float) Method

Sets the flex basis property of the view to a relative value.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView RelativeBasis&lt;TView>(this TView view, float length)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis&lt;TView>(this TView, float).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float).length'></a>

`length` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The relative length of the basis.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.RelativeBasis&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Row_TView_(thisTView)'></a>

## FlexBoxExtensions.Row&lt;TView>(this TView) Method

Sets the direction of the FlexBox to row.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Row&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Row_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Row_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Row_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Row&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Row_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Row&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RowReverse_TView_(thisTView)'></a>

## FlexBoxExtensions.RowReverse&lt;TView>(this TView) Method

Sets the direction of the FlexBox to row-reverse.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView RowReverse&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RowReverse_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.RowReverse_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.RowReverse_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.RowReverse&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.RowReverse_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.RowReverse&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float)'></a>

## FlexBoxExtensions.Shrink&lt;TView>(this TView, float) Method

Sets the flex shrink property of the view.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView Shrink&lt;TView>(this TView view, float shrink)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Shrink&lt;TView>(this TView, float).TView')

The view to set the property on.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float).shrink'></a>

`shrink` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The flex shrink value.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.Shrink_TView_(thisTView,float).TView 'Tizen.UI.Layouts.FlexBoxExtensions.Shrink&lt;TView>(this TView, float).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.SpaceAroundJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to space-around.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView SpaceAroundJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceAroundJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.SpaceBetweenJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to space-between.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView SpaceBetweenJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceBetweenJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.SpaceEvenlyJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to space-evenly.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView SpaceEvenlyJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.SpaceEvenlyJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartAlign_TView_(thisTView)'></a>

## FlexBoxExtensions.StartAlign&lt;TView>(this TView) Method

Sets the align-self property of the view to start.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView StartAlign&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartAlign_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartAlign_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartAlign&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartAlign&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartItems_TView_(thisTView)'></a>

## FlexBoxExtensions.StartItems&lt;TView>(this TView) Method

Sets the align-items property of the FlexBox to start.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView StartItems&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartItems_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartItems_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartItems&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartItems&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartJustify_TView_(thisTView)'></a>

## FlexBoxExtensions.StartJustify&lt;TView>(this TView) Method

Sets the justify-content property of the FlexBox to start.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView StartJustify&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartJustify_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StartJustify_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartJustify&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StartJustify_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StartJustify&lt;TView>(this TView).TView')  
The FlexBox.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign_TView_(thisTView)'></a>

## FlexBoxExtensions.StretchAlign&lt;TView>(this TView) Method

Sets the align-self property of the view to stretch.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView StretchAlign&lt;TView>(this TView view)
    where TView : Tizen.UI.View;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign_TView_(thisTView).TView'></a>

`TView`

The type of the view.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign&lt;TView>(this TView).TView')

The view to set the property on.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StretchAlign&lt;TView>(this TView).TView')  
The view itself.

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchItems_TView_(thisTView)'></a>

## FlexBoxExtensions.StretchItems&lt;TView>(this TView) Method

Sets the align-items property of the FlexBox to stretch.<br/>  
This only works if the [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') is included in the  [FlexBox](Tizen.UI.Layouts.FlexBox.md 'Tizen.UI.Layouts.FlexBox') and used.

```csharp
public static TView StretchItems&lt;TView>(this TView view)
    where TView : Tizen.UI.Layouts.FlexBox;
```
#### Type parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchItems_TView_(thisTView).TView'></a>

`TView`

The type of the FlexBox.
#### Parameters

<a name='Tizen.UI.Layouts.FlexBoxExtensions.StretchItems_TView_(thisTView).view'></a>

`view` [TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StretchItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StretchItems&lt;TView>(this TView).TView')

The FlexBox.

#### Returns
[TView](Tizen.UI.Layouts.FlexBoxExtensions.md#Tizen.UI.Layouts.FlexBoxExtensions.StretchItems_TView_(thisTView).TView 'Tizen.UI.Layouts.FlexBoxExtensions.StretchItems&lt;TView>(this TView).TView')  
The FlexBox.






























































