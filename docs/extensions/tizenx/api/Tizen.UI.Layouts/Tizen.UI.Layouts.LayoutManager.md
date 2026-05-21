### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## LayoutManager Class

Represents a base class for layout managers.

```csharp
public abstract class LayoutManager :
Tizen.UI.Layouts.ILayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; LayoutManager

Derived  
&#8627; [AbsoluteLayoutManager](Tizen.UI.Layouts.AbsoluteLayoutManager.md 'Tizen.UI.Layouts.AbsoluteLayoutManager')  
&#8627; [GridLayoutManager](Tizen.UI.Layouts.GridLayoutManager.md 'Tizen.UI.Layouts.GridLayoutManager')  
&#8627; [ScrollLayoutManager](Tizen.UI.Layouts.ScrollLayoutManager.md 'Tizen.UI.Layouts.ScrollLayoutManager')  
&#8627; [StackLayoutManager](Tizen.UI.Layouts.StackLayoutManager.md 'Tizen.UI.Layouts.StackLayoutManager')

Implements [ILayoutManager](Tizen.UI.Layouts.ILayoutManager.md 'Tizen.UI.Layouts.ILayoutManager')
### Constructors

<a name='Tizen.UI.Layouts.LayoutManager.LayoutManager(Tizen.UI.Layouts.ILayout)'></a>

## LayoutManager(ILayout) Constructor

Initializes a new instance of the [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') class.

```csharp
public LayoutManager(Tizen.UI.Layouts.ILayout layout);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutManager.LayoutManager(Tizen.UI.Layouts.ILayout).layout'></a>

`layout` [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')

The layout that owns the layout manager.
### Properties

<a name='Tizen.UI.Layouts.LayoutManager.Layout'></a>

## LayoutManager.Layout Property

Gets the layout that owns the layout manager.

```csharp
public Tizen.UI.Layouts.ILayout Layout { get; }
```

#### Property Value
[ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Methods

<a name='Tizen.UI.Layouts.LayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## LayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the layout.

```csharp
public abstract Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` Tizen.UI.Rect

The available space for the layout.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
Tizen.UI.Size  
The arranged size of the layout.

<a name='Tizen.UI.Layouts.LayoutManager.Measure(float,float)'></a>

## LayoutManager.Measure(float, float) Method

Measures the size of the layout.

```csharp
public abstract Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Layouts.LayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.

Implements [Measure(float, float)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.Measure(float,float) 'Tizen.UI.Layouts.ILayoutManager.Measure(float, float)')

#### Returns
Tizen.UI.Size  
The measured size of the layout.

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float)'></a>

## LayoutManager.ResolveConstraints(float, float, float, float, float) Method

Resolves the constraints for the layout.

```csharp
public static float ResolveConstraints(float externalConstraint, float explicitLength, float measuredLength, float min=0f, float max=float.PositiveInfinity);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float).externalConstraint'></a>

`externalConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The external constraint for the layout.

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float).explicitLength'></a>

`explicitLength` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The explicit length for the layout.

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float).measuredLength'></a>

`measuredLength` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The measured length for the layout.

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float).min'></a>

`min` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The minimum length for the layout.

<a name='Tizen.UI.Layouts.LayoutManager.ResolveConstraints(float,float,float,float,float).max'></a>

`max` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The maximum length for the layout.

#### Returns
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')  
The resolved constraint for the layout.































































