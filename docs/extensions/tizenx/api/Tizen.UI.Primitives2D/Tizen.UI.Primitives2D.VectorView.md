### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## VectorView Class

The [VectorView](Tizen.UI.Primitives2D.VectorView.md 'Tizen.UI.Primitives2D.VectorView') class is a [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') that displays a list of drawables.

```csharp
public class VectorView : Tizen.UI.View
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; VectorView
### Constructors

<a name='Tizen.UI.Primitives2D.VectorView.VectorView()'></a>

## VectorView() Constructor

Creates a new instance of the [VectorView](Tizen.UI.Primitives2D.VectorView.md 'Tizen.UI.Primitives2D.VectorView') class.

```csharp
public VectorView();
```
### Properties

<a name='Tizen.UI.Primitives2D.VectorView.Drawables'></a>

## VectorView.Drawables Property

Gets the read-only collection of drawables in the vector view.

```csharp
public System.Collections.Generic.IReadOnlyCollection&lt;Tizen.UI.Primitives2D.Drawable> Drawables { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')[Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')
### Methods

<a name='Tizen.UI.Primitives2D.VectorView.Add(Tizen.UI.Primitives2D.Drawable)'></a>

## VectorView.Add(Drawable) Method

Adds a new [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable') to the vector view.

```csharp
public void Add(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.VectorView.Add(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to add.

<a name='Tizen.UI.Primitives2D.VectorView.Clear()'></a>

## VectorView.Clear() Method

Removes all drawables from the vector view.

```csharp
public void Clear();
```

<a name='Tizen.UI.Primitives2D.VectorView.Contains(Tizen.UI.Primitives2D.Drawable)'></a>

## VectorView.Contains(Drawable) Method

Checks if the [VectorView](Tizen.UI.Primitives2D.VectorView.md 'Tizen.UI.Primitives2D.VectorView') contains a specific [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable').

```csharp
public bool Contains(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.VectorView.Contains(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the vector view contains the specified drawable, false otherwise.

<a name='Tizen.UI.Primitives2D.VectorView.Remove(Tizen.UI.Primitives2D.Drawable)'></a>

## VectorView.Remove(Drawable) Method

Removes a [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable') from the vector view.

```csharp
public void Remove(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.VectorView.Remove(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to remove.


















































