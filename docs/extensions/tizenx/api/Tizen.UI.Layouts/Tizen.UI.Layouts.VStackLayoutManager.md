### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## VStackLayoutManager Class

VStackLayoutManager is a layout manager that arranges its children vertically within a given space.

```csharp
public class VStackLayoutManager : Tizen.UI.Layouts.StackLayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') &#129106; [StackLayoutManager](Tizen.UI.Layouts.StackLayoutManager.md 'Tizen.UI.Layouts.StackLayoutManager') &#129106; VStackLayoutManager
### Constructors

<a name='Tizen.UI.Layouts.VStackLayoutManager.VStackLayoutManager(Tizen.UI.Layouts.IStackLayout)'></a>

## VStackLayoutManager(IStackLayout) Constructor

Initializes a new instance of the VStackLayoutManager class.

```csharp
public VStackLayoutManager(Tizen.UI.Layouts.IStackLayout stackLayout);
```
#### Parameters

<a name='Tizen.UI.Layouts.VStackLayoutManager.VStackLayoutManager(Tizen.UI.Layouts.IStackLayout).stackLayout'></a>

`stackLayout` [IStackLayout](Tizen.UI.Layouts.IStackLayout.md 'Tizen.UI.Layouts.IStackLayout')
### Methods

<a name='Tizen.UI.Layouts.VStackLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## VStackLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the layout.

```csharp
public override Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.VStackLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The available space for the layout.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The arranged size of the layout.

<a name='Tizen.UI.Layouts.VStackLayoutManager.Measure(float,float)'></a>

## VStackLayoutManager.Measure(float, float) Method

Measures the size of the layout.

```csharp
public override Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.VStackLayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Layouts.VStackLayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.

Implements [Measure(float, float)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.Measure(float,float) 'Tizen.UI.Layouts.ILayoutManager.Measure(float, float)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the layout.






























































