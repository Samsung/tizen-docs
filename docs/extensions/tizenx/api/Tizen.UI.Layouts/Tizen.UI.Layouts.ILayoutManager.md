### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## ILayoutManager Interface

Defines the interface for a layout manager, which is responsible for measuring and arranging the children of a layout.

```csharp
public interface ILayoutManager
```

Derived  
&#8627; [FlexLayoutManager](Tizen.UI.Layouts.FlexLayoutManager.md 'Tizen.UI.Layouts.FlexLayoutManager')  
&#8627; [LayoutManager](Tizen.UI.Layouts.LayoutManager.md 'Tizen.UI.Layouts.LayoutManager')
### Methods

<a name='Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect)'></a>

## ILayoutManager.ArrangeChildren(Rect) Method

Arranges the children of the layout.

```csharp
Tizen.UI.Size ArrangeChildren(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.ILayoutManager.ArrangeChildren(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The available space for the layout.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The arranged size of the layout.

<a name='Tizen.UI.Layouts.ILayoutManager.Measure(float,float)'></a>

## ILayoutManager.Measure(float, float) Method

Measures the size of the layout.

```csharp
Tizen.UI.Size Measure(float widthConstraint, float heightConstraint);
```
#### Parameters

<a name='Tizen.UI.Layouts.ILayoutManager.Measure(float,float).widthConstraint'></a>

`widthConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width for the layout.

<a name='Tizen.UI.Layouts.ILayoutManager.Measure(float,float).heightConstraint'></a>

`heightConstraint` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height for the layout.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The measured size of the layout.






























































