### [Tizen.UI.Layouts](Tizen.UI.Layouts.md 'Tizen.UI.Layouts')

## LayoutHelper Class

Provides common layout logic for ViewGroup instances.  
This class uses composition to provide layout functionality, simplifying the implementation of custom layouts.

```csharp
public class LayoutHelper :
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; LayoutHelper

Implements [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Constructors

<a name='Tizen.UI.Layouts.LayoutHelper.LayoutHelper(Tizen.UI.ViewGroup,Tizen.UI.Layouts.ILayoutManager)'></a>

## LayoutHelper(ViewGroup, ILayoutManager) Constructor

Initializes a new instance of the [LayoutHelper](Tizen.UI.Layouts.LayoutHelper.md 'Tizen.UI.Layouts.LayoutHelper') class.

```csharp
public LayoutHelper(Tizen.UI.ViewGroup viewGroup, Tizen.UI.Layouts.ILayoutManager layoutManager);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.LayoutHelper(Tizen.UI.ViewGroup,Tizen.UI.Layouts.ILayoutManager).viewGroup'></a>

`viewGroup` [Tizen.UI.ViewGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ViewGroup 'Tizen.UI.ViewGroup')

The ViewGroup instance this helper will provide functionality for.

<a name='Tizen.UI.Layouts.LayoutHelper.LayoutHelper(Tizen.UI.ViewGroup,Tizen.UI.Layouts.ILayoutManager).layoutManager'></a>

`layoutManager` [ILayoutManager](Tizen.UI.Layouts.ILayoutManager.md 'Tizen.UI.Layouts.ILayoutManager')

The layout manager instance to use for layout operations.
### Properties

<a name='Tizen.UI.Layouts.LayoutHelper.Measured'></a>

## LayoutHelper.Measured Property

Gets or sets a value indicating whether the layout has been measured.

```csharp
public bool Measured { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')
### Methods

<a name='Tizen.UI.Layouts.LayoutHelper.Dispose()'></a>

## LayoutHelper.Dispose() Method

Disposes the object and releases all resources associated with it.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Layouts.LayoutHelper.Measure(float,float)'></a>

## LayoutHelper.Measure(float, float) Method

Measures the layout with the specified available width and height.

```csharp
public Tizen.UI.Size Measure(float availableWidth, float availableHeight);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.Measure(float,float).availableWidth'></a>

`availableWidth` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available width to measure the layout with.

<a name='Tizen.UI.Layouts.LayoutHelper.Measure(float,float).availableHeight'></a>

`availableHeight` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The available height to measure the layout with.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The size of the layout after measuring.

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildAdded(Tizen.UI.View)'></a>

## LayoutHelper.OnChildAdded(View) Method

Called when a child is added to the layout. The implementer should call this from their OnChildAdded method.

```csharp
public void OnChildAdded(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildAdded(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view that was added to the layout.

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildMeasureInvalidatedOverride(Tizen.UI.View)'></a>

## LayoutHelper.OnChildMeasureInvalidatedOverride(View) Method

Called when the child measure is invalidated. The implementer should call this from their OnChildMeasureInvalidatedOverride method.

```csharp
public void OnChildMeasureInvalidatedOverride(Tizen.UI.View child);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildMeasureInvalidatedOverride(Tizen.UI.View).child'></a>

`child` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The child that was invalidated.

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildRemoved(Tizen.UI.View)'></a>

## LayoutHelper.OnChildRemoved(View) Method

Called when a child is removed from the layout. The implementer should call this from their OnChildRemoved method.

```csharp
public void OnChildRemoved(Tizen.UI.View view);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.OnChildRemoved(Tizen.UI.View).view'></a>

`view` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The view that was removed from the layout.

<a name='Tizen.UI.Layouts.LayoutHelper.OnMeasureInvalidated()'></a>

## LayoutHelper.OnMeasureInvalidated() Method

Called when the measure of the layout is invalidated. The implementer should call this from their OnMeasureInvalidatedOverride method.

```csharp
public void OnMeasureInvalidated();
```

<a name='Tizen.UI.Layouts.LayoutHelper.UpdateLayout()'></a>

## LayoutHelper.UpdateLayout() Method

Updates the layout.

```csharp
public void UpdateLayout();
```

<a name='Tizen.UI.Layouts.LayoutHelper.UpdateLayout(Tizen.UI.Rect)'></a>

## LayoutHelper.UpdateLayout(Rect) Method

Updates the layout with the specified bounds.

```csharp
public Tizen.UI.Size UpdateLayout(Tizen.UI.Rect bounds);
```
#### Parameters

<a name='Tizen.UI.Layouts.LayoutHelper.UpdateLayout(Tizen.UI.Rect).bounds'></a>

`bounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds to update the layout with.

#### Returns
[Tizen.UI.Size](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Size 'Tizen.UI.Size')  
The size of the layout after updating.






























































