### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## ScrollableLayoutManager Class

Provides functionality for arranging and measuring the children of a Scrollable.

```csharp
public class ScrollableLayoutManager : Tizen.UI.Layouts.LayoutManager
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.Layouts.LayoutManager](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.LayoutManager 'Tizen.UI.Layouts.LayoutManager') &#129106; ScrollableLayoutManager
### Constructors

<a name='Tizen.UI.Components.ScrollableLayoutManager.ScrollableLayoutManager(Tizen.UI.Components.Scrollable)'></a>

## ScrollableLayoutManager(Scrollable) Constructor

Initializes a new instance of the ScrollableLayoutManager class.

```csharp
public ScrollableLayoutManager(Tizen.UI.Components.Scrollable view);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollableLayoutManager.ScrollableLayoutManager(Tizen.UI.Components.Scrollable).view'></a>

`view` [Scrollable](Tizen.UI.Components.Scrollable.md 'Tizen.UI.Components.Scrollable')

The Scrollable that owns the layout manager.
### Properties

<a name='Tizen.UI.Components.ScrollableLayoutManager.Scrollable'></a>

## ScrollableLayoutManager.Scrollable Property

Gets the Scrollable that owns the layout manager.

```csharp
public Tizen.UI.Components.Scrollable Scrollable { get; }
```

#### Property Value
[Scrollable](Tizen.UI.Components.Scrollable.md 'Tizen.UI.Components.Scrollable')
### Methods

<a name='Tizen.UI.Components.ScrollableLayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## ScrollableLayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the layout.

```csharp
public override Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollableLayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The available space for the layout.

Implements [ArrangeChildren(Rect)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.ILayoutManager.ArrangeChildren#Tizen_UI_Layouts_ILayoutManager_ArrangeChildren_Tizen_UI_Rect_ 'Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The arranged size of the layout.

<a name='Tizen.UI.Components.ScrollableLayoutManager.Measure(float,float)'></a>

## ScrollableLayoutManager.Measure(float, float) Method

Measures the size of the layout.

```csharp
public override Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Components.ScrollableLayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Components.ScrollableLayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.

Implements [Measure(float, float)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.ILayoutManager.Measure#Tizen_UI_Layouts_ILayoutManager_Measure_System_Single,System_Single_ 'Tizen.UI.Layouts.ILayoutManager.Measure(System.Single,System.Single)')

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the layout.


























































