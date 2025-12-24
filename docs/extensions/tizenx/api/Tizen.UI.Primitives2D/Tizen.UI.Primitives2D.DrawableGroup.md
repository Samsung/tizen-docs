### [Tizen.UI.Primitives2D](Tizen.UI.Primitives2D.md 'Tizen.UI.Primitives2D')

## DrawableGroup Class

[DrawableGroup](Tizen.UI.Primitives2D.DrawableGroup.md 'Tizen.UI.Primitives2D.DrawableGroup') is a class that manages a collection of drawables and draws them as a group.

```csharp
public class DrawableGroup : Tizen.UI.Primitives2D.Drawable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; Tizen.UI.NObject &#129106; [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable') &#129106; DrawableGroup
### Constructors

<a name='Tizen.UI.Primitives2D.DrawableGroup.DrawableGroup()'></a>

## DrawableGroup() Constructor

Creates a new instance of the [DrawableGroup](Tizen.UI.Primitives2D.DrawableGroup.md 'Tizen.UI.Primitives2D.DrawableGroup') class.

```csharp
public DrawableGroup();
```
### Properties

<a name='Tizen.UI.Primitives2D.DrawableGroup.Drawables'></a>

## DrawableGroup.Drawables Property

Gets a read-only collection of drawables in the group.

```csharp
public System.Collections.Generic.IReadOnlyCollection&lt;Tizen.UI.Primitives2D.Drawable> Drawables { get; }
```

#### Property Value
[System.Collections.Generic.IReadOnlyCollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')[Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IReadOnlyCollection-1 'System.Collections.Generic.IReadOnlyCollection`1')
### Methods

<a name='Tizen.UI.Primitives2D.DrawableGroup.Add(Tizen.UI.Primitives2D.Drawable)'></a>

## DrawableGroup.Add(Drawable) Method

Adds a [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable') to the group.

```csharp
public void Add(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.DrawableGroup.Add(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to add.

<a name='Tizen.UI.Primitives2D.DrawableGroup.Clear()'></a>

## DrawableGroup.Clear() Method

Removes all drawables from the group.

```csharp
public void Clear();
```

<a name='Tizen.UI.Primitives2D.DrawableGroup.Contains(Tizen.UI.Primitives2D.Drawable)'></a>

## DrawableGroup.Contains(Drawable) Method

Checks if the group contains a specific drawable.

```csharp
public bool Contains(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.DrawableGroup.Contains(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the group contains the specified drawable, false otherwise.

<a name='Tizen.UI.Primitives2D.DrawableGroup.Remove(Tizen.UI.Primitives2D.Drawable)'></a>

## DrawableGroup.Remove(Drawable) Method

Removes a [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable') from the group.

```csharp
public void Remove(Tizen.UI.Primitives2D.Drawable drawable);
```
#### Parameters

<a name='Tizen.UI.Primitives2D.DrawableGroup.Remove(Tizen.UI.Primitives2D.Drawable).drawable'></a>

`drawable` [Drawable](Tizen.UI.Primitives2D.Drawable.md 'Tizen.UI.Primitives2D.Drawable')

The drawable to remove.



















































