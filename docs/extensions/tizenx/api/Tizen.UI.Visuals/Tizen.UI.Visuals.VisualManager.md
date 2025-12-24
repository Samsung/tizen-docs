### [Tizen.UI.Visuals](Tizen.UI.Visuals.md 'Tizen.UI.Visuals')

## VisualManager Class

VisualManager is a class that manages visuals.

```csharp
public class VisualManager :
System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject>,
System.Collections.Generic.ICollection&lt;Tizen.UI.Visuals.VisualObject>,
System.Collections.Generic.IEnumerable&lt;Tizen.UI.Visuals.VisualObject>,
System.Collections.IEnumerable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; VisualManager

Implements [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Visuals.VisualManager.VisualManager(Tizen.UI.View)'></a>

## VisualManager(View) Constructor

Initializes a new instance of the VisualManager class.

```csharp
public VisualManager(Tizen.UI.View owner);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.VisualManager(Tizen.UI.View).owner'></a>

`owner` Tizen.UI.View

The View object that owns this VisualManager.
### Properties

<a name='Tizen.UI.Visuals.VisualManager.BackgroundLayer'></a>

## VisualManager.BackgroundLayer Property

Gets the background layer for the visual object.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject> BackgroundLayer { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

### Remarks
This layer is rendered below the background

<a name='Tizen.UI.Visuals.VisualManager.ContentLayer'></a>

## VisualManager.ContentLayer Property

Gets the content layer for the visual object.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject> ContentLayer { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

### Remarks
This layer is rendered below the content.  
It is a default layer of the visual object

<a name='Tizen.UI.Visuals.VisualManager.Count'></a>

## VisualManager.Count Property

Gets the number of visual objects in the content layer.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Visuals.VisualManager.DecorationLayer'></a>

## VisualManager.DecorationLayer Property

Gets the decoration layer for the visual object.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject> DecorationLayer { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

### Remarks
This layer is rendered below the decoration

<a name='Tizen.UI.Visuals.VisualManager.ForegroundEffectLayer'></a>

## VisualManager.ForegroundEffectLayer Property

Gets the foreground effect layer for the visual object.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject> ForegroundEffectLayer { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

### Remarks
This layer is rendered below the foreground effect

<a name='Tizen.UI.Visuals.VisualManager.IsReadOnly'></a>

## VisualManager.IsReadOnly Property

Gets a value indicating whether the VisualManager is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Visuals.VisualManager.Owner'></a>

## VisualManager.Owner Property

Gets the owner of the VisualManager.

```csharp
public Tizen.UI.View Owner { get; }
```

#### Property Value
Tizen.UI.View

<a name='Tizen.UI.Visuals.VisualManager.ShadowLayer'></a>

## VisualManager.ShadowLayer Property

Gets the shadow layer for the visual object.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Visuals.VisualObject> ShadowLayer { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

### Remarks
This layer is rendered below the shadow

<a name='Tizen.UI.Visuals.VisualManager.this[int]'></a>

## VisualManager.this[int] Property

Gets the visual at the specified index in the content layer

```csharp
public Tizen.UI.Visuals.VisualObject this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')
### Methods

<a name='Tizen.UI.Visuals.VisualManager.Add(Tizen.UI.Visuals.VisualObject)'></a>

## VisualManager.Add(VisualObject) Method

Adds a visual to the content layer.

```csharp
public void Add(Tizen.UI.Visuals.VisualObject item);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.Add(Tizen.UI.Visuals.VisualObject).item'></a>

`item` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual to add.

<a name='Tizen.UI.Visuals.VisualManager.Clear()'></a>

## VisualManager.Clear() Method

Clears all visual objects from the content layer.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Visuals.VisualManager.Contains(Tizen.UI.Visuals.VisualObject)'></a>

## VisualManager.Contains(VisualObject) Method

Checks whether the specified visual object exists in the content layer.

```csharp
public bool Contains(Tizen.UI.Visuals.VisualObject item);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.Contains(Tizen.UI.Visuals.VisualObject).item'></a>

`item` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual object to check.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the visual object exists in the content container, false otherwise.

<a name='Tizen.UI.Visuals.VisualManager.CopyTo(Tizen.UI.Visuals.VisualObject[],int)'></a>

## VisualManager.CopyTo(VisualObject[], int) Method

Copies the elements of the VisualBase collection to an Array, starting at a particular Array index.

```csharp
public void CopyTo(Tizen.UI.Visuals.VisualObject[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.CopyTo(Tizen.UI.Visuals.VisualObject[],int).array'></a>

`array` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The one-dimensional Array that is the destination of the elements copied from VisualBase collection. The Array must have zero-based indexing.

<a name='Tizen.UI.Visuals.VisualManager.CopyTo(Tizen.UI.Visuals.VisualObject[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The zero-based index in array at which copying begins.

<a name='Tizen.UI.Visuals.VisualManager.GetEnumerator()'></a>

## VisualManager.GetEnumerator() Method

Returns an enumerator that iterates through the collection.

```csharp
public System.Collections.Generic.IEnumerator&lt;Tizen.UI.Visuals.VisualObject> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator that can be used to iterate through the collection.

<a name='Tizen.UI.Visuals.VisualManager.IndexOf(Tizen.UI.Visuals.VisualObject)'></a>

## VisualManager.IndexOf(VisualObject) Method

Returns the zero-based index of the first occurrence of the specified visual in the content layer.

```csharp
public int IndexOf(Tizen.UI.Visuals.VisualObject item);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.IndexOf(Tizen.UI.Visuals.VisualObject).item'></a>

`item` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual to locate in the content layer.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The zero-based index of the first occurrence of the specified visual, if found; otherwise, -1.

<a name='Tizen.UI.Visuals.VisualManager.Insert(int,Tizen.UI.Visuals.VisualObject)'></a>

## VisualManager.Insert(int, VisualObject) Method

Inserts a visual at the specified position in the content layer.

```csharp
public void Insert(int index, Tizen.UI.Visuals.VisualObject item);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.Insert(int,Tizen.UI.Visuals.VisualObject).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The position at which to insert the visual.

<a name='Tizen.UI.Visuals.VisualManager.Insert(int,Tizen.UI.Visuals.VisualObject).item'></a>

`item` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual to insert.

<a name='Tizen.UI.Visuals.VisualManager.Remove(Tizen.UI.Visuals.VisualObject)'></a>

## VisualManager.Remove(VisualObject) Method

Removes the specified visual object from the content layer.

```csharp
public bool Remove(Tizen.UI.Visuals.VisualObject item);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.Remove(Tizen.UI.Visuals.VisualObject).item'></a>

`item` [VisualObject](Tizen.UI.Visuals.VisualObject.md 'Tizen.UI.Visuals.VisualObject')

The visual object to remove.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the visual object was removed successfully, false otherwise.

<a name='Tizen.UI.Visuals.VisualManager.RemoveAt(int)'></a>

## VisualManager.RemoveAt(int) Method

Removes the child at the specified index from the content layer.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Visuals.VisualManager.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The zero-based index of the child to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Explicit Interface Implementations

<a name='Tizen.UI.Visuals.VisualManager.System.Collections.IEnumerable.GetEnumerator()'></a>

## VisualManager.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the collection.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

























