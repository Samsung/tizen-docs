### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## ScrollLayoutManager Class

Provides functionality for arranging and measuring the children of a ScrollView.

```csharp
public class ScrollLayoutManager : Tizen.UI.Layouts.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager') &#129106; ScrollLayoutManager
### Constructors

<a name='Tizen.UI.Layouts.ScrollLayoutManager.ScrollLayoutManager(Tizen.UI.Layouts.ScrollLayout)'></a>

## ScrollLayoutManager(ScrollLayout) Constructor

Initializes a new instance of the ScrollViewLayoutManager class.

```csharp
public ScrollLayoutManager(Tizen.UI.Layouts.ScrollLayout view);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayoutManager.ScrollLayoutManager(Tizen.UI.Layouts.ScrollLayout).view'></a>

`view` [ScrollLayout](Tizen.UI.Layouts.ScrollLayout.md 'Tizen.UI.Layouts.ScrollLayout')

The ScrollView that owns the layout manager.
### Properties

<a name='Tizen.UI.Layouts.ScrollLayoutManager.ScrollView'></a>

## ScrollLayoutManager.ScrollView Property

Gets the ScrollView that owns the layout manager.

```csharp
public Tizen.UI.Layouts.ScrollLayout ScrollView { get; }
```

#### Property Value
[ScrollLayout](Tizen.UI.Layouts.ScrollLayout.md 'Tizen.UI.Layouts.ScrollLayout')
### Methods

<a name='Tizen.UI.Layouts.ScrollLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## ScrollLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the layout.

```csharp
public override Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The available space for the layout.

Implements [ArrangeChildren(Rect)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect) 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The arranged size of the layout.

<a name='Tizen.UI.Layouts.ScrollLayoutManager.Measure(float,float)'></a>

## ScrollLayoutManager.Measure(float, float) Method

Measures the size of the layout.

```csharp
public override Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.ScrollLayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Layouts.ScrollLayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.

Implements [Measure(float, float)](Tizen.UI.Layouts.ILayoutManager.md#Tizen.UI.Layouts.ILayoutManager.Measure(float,float) 'Tizen.UI.Layouts.ILayoutManager.Measure(float, float)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the layout.






























































