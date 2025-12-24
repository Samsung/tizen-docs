### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## Layer Class

Layer is a container for views. It provides a way to group views together and manipulate them as a single entity.

```csharp
public class Layer : Tizen.UI.NObject,
Tizen.UI.IParentObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; Layer

Implements [IParentObject](Tizen.UI.IParentObject.md 'Tizen.UI.IParentObject')
### Constructors

<a name='Tizen.UI.Layer.Layer()'></a>

## Layer() Constructor

Creates a new Layer object.

```csharp
public Layer();
```
### Properties

<a name='Tizen.UI.Layer.Children'></a>

## Layer.Children Property

Gets the list of children views in the Layer.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Layer.Count'></a>

## Layer.Count Property

Gets the count of children views in the Layer.

```csharp
public int Count { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Layer.HeightResizePolicy'></a>

## Layer.HeightResizePolicy Property

Gets or sets the height resize policy for the Layer.

```csharp
public Tizen.UI.ResizePolicy HeightResizePolicy { get; set; }
```

#### Property Value
[ResizePolicy](Tizen.UI.ResizePolicy.md 'Tizen.UI.ResizePolicy')

<a name='Tizen.UI.Layer.InheritLayoutDirection'></a>

## Layer.InheritLayoutDirection Property

Gets or sets a value indicating whether the layer inherits its layout direction from its parent.  
If [LayoutDirection](Tizen.UI.Layer.md#Tizen.UI.Layer.LayoutDirection 'Tizen.UI.Layer.LayoutDirection') is set, [InheritLayoutDirection](Tizen.UI.Layer.md#Tizen.UI.Layer.InheritLayoutDirection 'Tizen.UI.Layer.InheritLayoutDirection') is set to false.

```csharp
public bool InheritLayoutDirection { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layer.IsVisible'></a>

## Layer.IsVisible Property

Gets or sets a value indicating whether the layer is visible or not.

```csharp
public bool IsVisible { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Layer.LayoutDirection'></a>

## Layer.LayoutDirection Property

Gets or sets the layout direction of the layer.  
If [LayoutDirection](Tizen.UI.Layer.md#Tizen.UI.Layer.LayoutDirection 'Tizen.UI.Layer.LayoutDirection') is set, [InheritLayoutDirection](Tizen.UI.Layer.md#Tizen.UI.Layer.InheritLayoutDirection 'Tizen.UI.Layer.InheritLayoutDirection') is set to false.

```csharp
public Tizen.UI.LayoutDirection LayoutDirection { get; set; }
```

#### Property Value
[LayoutDirection](Tizen.UI.LayoutDirection.md 'Tizen.UI.LayoutDirection')

<a name='Tizen.UI.Layer.Name'></a>

## Layer.Name Property

Gets or sets the name of the layer.

```csharp
public string Name { get; set; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Layer.this[int]'></a>

## Layer.this[int] Property

Gets or sets the child view at the specified index.

```csharp
public Tizen.UI.View this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Layer.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')

<a name='Tizen.UI.Layer.WidthResizePolicy'></a>

## Layer.WidthResizePolicy Property

Gets or sets the width resize policy for the Layer.

```csharp
public Tizen.UI.ResizePolicy WidthResizePolicy { get; set; }
```

#### Property Value
[ResizePolicy](Tizen.UI.ResizePolicy.md 'Tizen.UI.ResizePolicy')
### Methods

<a name='Tizen.UI.Layer.Add(Tizen.UI.View)'></a>

## Layer.Add(View) Method

Adds a child view to the Layer.

```csharp
public void Add(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Layer.Add(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to add.

<a name='Tizen.UI.Layer.Remove(Tizen.UI.View)'></a>

## Layer.Remove(View) Method

Removes a child view from the Layer.

```csharp
public bool Remove(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Layer.Remove(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to remove.

Implements [Remove(View)](Tizen.UI.IParentObject.md#Tizen.UI.IParentObject.Remove(Tizen.UI.View) 'Tizen.UI.IParentObject.Remove(Tizen.UI.View)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the child view was removed, false otherwise.

<a name='Tizen.UI.Layer.SetSize(float,float)'></a>

## Layer.SetSize(float, float) Method

Sets the size of the Layer.

```csharp
public void SetSize(float width, float height);
```
#### Parameters

<a name='Tizen.UI.Layer.SetSize(float,float).width'></a>

`width` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The width of the Layer.

<a name='Tizen.UI.Layer.SetSize(float,float).height'></a>

`height` [System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

The height of the Layer.






