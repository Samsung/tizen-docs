### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## AbsoluteLayoutManager Class

The AbsoluteLayoutManager class is responsible for measuring and arranging the children of an AbsoluteLayout.

```csharp
public class AbsoluteLayoutManager : Tizen.UI.Layouts.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') &#129106; AbsoluteLayoutManager
### Constructors

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.AbsoluteLayoutManager(Tizen.UI.Layouts.ILayout)'></a>

## AbsoluteLayoutManager(ILayout) Constructor

Initializes a new instance of the AbsoluteLayoutManager class.

```csharp
public AbsoluteLayoutManager(Tizen.UI.Layouts.ILayout absoluteLayout);
```
#### Parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.AbsoluteLayoutManager(Tizen.UI.Layouts.ILayout).absoluteLayout'></a>

`absoluteLayout` [ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')

The AbsoluteLayout associated with this AbsoluteLayoutManager.
### Properties

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.AbsoluteLayout'></a>

## AbsoluteLayoutManager.AbsoluteLayout Property

Gets the AbsoluteLayout associated with this AbsoluteLayoutManager.

```csharp
public Tizen.UI.Layouts.ILayout AbsoluteLayout { get; }
```

#### Property Value
[ILayout](Tizen.UI.Layouts.ILayout.md 'Tizen.UI.Layouts.ILayout')
### Methods

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## AbsoluteLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the AbsoluteLayout within the given bounds.

```csharp
public override Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds within which to arrange the children.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The arranged size of the children.

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.Measure(float,float)'></a>

## AbsoluteLayoutManager.Measure(float, float) Method

Measures the size of the AbsoluteLayout using the given constraints.

```csharp
public override Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width constraint to use when measuring the AbsoluteLayout.

<a name='Tizen.UI.Layouts.AbsoluteLayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height constraint to use when measuring the AbsoluteLayout.

Implements [Measure(float, float)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.Measure(float,float) 'Tizen.UI.Layouts.ILayoutManager.Measure(float, float)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the AbsoluteLayout.






























































