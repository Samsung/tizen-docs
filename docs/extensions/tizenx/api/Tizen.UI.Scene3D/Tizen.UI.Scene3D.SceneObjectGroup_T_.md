### [Tizen.UI.Scene3D](Tizen.UI.Scene3D.md 'Tizen.UI.Scene3D')

## SceneObjectGroup&lt;T> Class

SceneObjectGroup is a container class that manages an array of scene object.

```csharp
public abstract class SceneObjectGroup&lt;T> : Tizen.UI.Scene3D.SceneObject,
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable
    where T : Tizen.UI.Scene3D.SceneObject
```
#### Type parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [SceneObject](Tizen.UI.Scene3D.SceneObject.md 'Tizen.UI.Scene3D.SceneObject') &#129106; SceneObjectGroup&lt;T>

Derived  
&#8627; [Model3D](Tizen.UI.Scene3D.Model3D.md 'Tizen.UI.Scene3D.Model3D')  
&#8627; [ModelNode](Tizen.UI.Scene3D.ModelNode.md 'Tizen.UI.Scene3D.ModelNode')

Implements [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Properties

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Children'></a>

## SceneObjectGroup&lt;T>.Children Property

Gets the list of child scene objects.

```csharp
public System.Collections.Generic.IList&lt;T> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Count'></a>

## SceneObjectGroup&lt;T>.Count Property

Gets the number of child scene objects.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.IsReadOnly'></a>

## SceneObjectGroup&lt;T>.IsReadOnly Property

Gets a value indicating whether the list of child scene objects is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.this[int]'></a>

## SceneObjectGroup&lt;T>.this[int] Property

Gets or sets the scene object at the specified index.

```csharp
public T this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')
### Methods

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Add(T)'></a>

## SceneObjectGroup&lt;T>.Add(T) Method

Adds a child scene object to the end of the list of child scene objects.

```csharp
public void Add(T item);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Add(T).item'></a>

`item` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')

The child scene object to add.

Implements [Add(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Clear()'></a>

## SceneObjectGroup&lt;T>.Clear() Method

Removes all child scene objects from the list of child scene objects.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Contains(T)'></a>

## SceneObjectGroup&lt;T>.Contains(T) Method

Checks if the list of child scene objects contains the specified child scene object.

```csharp
public bool Contains(T item);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Contains(T).item'></a>

`item` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')

The child scene object to check for.

Implements [Contains(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Contains#System_Collections_Generic_ICollection_1_Contains__0_ 'System.Collections.Generic.ICollection`1.Contains(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the list of child scene objects contains the child scene object, false otherwise.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.CopyTo(T[],int)'></a>

## SceneObjectGroup&lt;T>.CopyTo(T[], int) Method

Copies the child scene objects in the list of child scene objects to the specified array, starting at the specified index.

```csharp
public void CopyTo(T[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.CopyTo(T[],int).array'></a>

`array` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the child scene objects to.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.CopyTo(T[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

Implements [CopyTo(T[], int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.CopyTo#System_Collections_Generic_ICollection_1_CopyTo__0[],System_Int32_ 'System.Collections.Generic.ICollection`1.CopyTo(`0[],System.Int32)')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.GetEnumerator()'></a>

## SceneObjectGroup&lt;T>.GetEnumerator() Method

Returns an enumerator that iterates through the list of child scene objects.

```csharp
public System.Collections.Generic.IEnumerator&lt;T> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the list of child scene objects.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.IndexOf(T)'></a>

## SceneObjectGroup&lt;T>.IndexOf(T) Method

Gets the index of the specified child scene object in the list of child scene objects.

```csharp
public int IndexOf(T item);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.IndexOf(T).item'></a>

`item` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')

The child scene object to find the index of.

Implements [IndexOf(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.IndexOf#System_Collections_Generic_IList_1_IndexOf__0_ 'System.Collections.Generic.IList`1.IndexOf(`0)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the child scene object, or -1 if it is not found.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Insert(int,T)'></a>

## SceneObjectGroup&lt;T>.Insert(int, T) Method

Inserts a child scene object at the specified index in the list of child scene objects.

```csharp
public void Insert(int index, T item);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Insert(int,T).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child scene object at.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Insert(int,T).item'></a>

`item` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')

The child scene object to insert.

Implements [Insert(int, T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Insert#System_Collections_Generic_IList_1_Insert_System_Int32,_0_ 'System.Collections.Generic.IList`1.Insert(System.Int32,`0)')

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Remove(T)'></a>

## SceneObjectGroup&lt;T>.Remove(T) Method

Removes the specified child scene object from the list of child scene objects.

```csharp
public bool Remove(T item);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.Remove(T).item'></a>

`item` [T](Tizen.UI.Scene3D.SceneObjectGroup_T_.md#Tizen.UI.Scene3D.SceneObjectGroup_T_.T 'Tizen.UI.Scene3D.SceneObjectGroup&lt;T>.T')

The child scene object to remove.

Implements [Remove(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the child scene object was removed, false otherwise.

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.RemoveAt(int)'></a>

## SceneObjectGroup&lt;T>.RemoveAt(int) Method

Removes the child scene object at the specified index from the list of child scene objects.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the child scene object to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Explicit Interface Implementations

<a name='Tizen.UI.Scene3D.SceneObjectGroup_T_.System.Collections.IEnumerable.GetEnumerator()'></a>

## SceneObjectGroup&lt;T>.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the list of child scene objects.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')





































