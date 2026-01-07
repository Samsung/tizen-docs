### [Tizen.UI](Tizen.UI.md 'Tizen.UI')

## ViewGroup Class

ViewGroup is a container class that manages an array of child views and layouts. It provides layout management and event propagation.

```csharp
public class ViewGroup : Tizen.UI.View,
System.Collections.Generic.IList&lt;Tizen.UI.View>,
System.Collections.Generic.ICollection&lt;Tizen.UI.View>,
System.Collections.Generic.IEnumerable&lt;Tizen.UI.View>,
System.Collections.IEnumerable,
Tizen.UI.IParentObject
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [NObject](Tizen.UI.NObject.md 'Tizen.UI.NObject') &#129106; [View](Tizen.UI.View.md 'Tizen.UI.View') &#129106; ViewGroup

Implements [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable'), [IParentObject](Tizen.UI.IParentObject.md 'Tizen.UI.IParentObject')
### Constructors

<a name='Tizen.UI.ViewGroup.ViewGroup()'></a>

## ViewGroup() Constructor

Constructor for the ViewGroup class.

```csharp
public ViewGroup();
```
### Properties

<a name='Tizen.UI.ViewGroup.Children'></a>

## ViewGroup.Children Property

Gets the list of child views.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.ViewGroup.Count'></a>

## ViewGroup.Count Property

Gets the number of child views.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.ViewGroup.IsReadOnly'></a>

## ViewGroup.IsReadOnly Property

Gets a value indicating whether the list of child views is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.ViewGroup.this[int]'></a>

## ViewGroup.this[int] Property

Gets or sets the child view at the specified index.

```csharp
public Tizen.UI.View this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.ViewGroup.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[View](Tizen.UI.View.md 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.ViewGroup.Add(Tizen.UI.View)'></a>

## ViewGroup.Add(View) Method

Adds a child view to the end of the list of child views.

```csharp
public void Add(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.Add(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to add.

<a name='Tizen.UI.ViewGroup.Clear()'></a>

## ViewGroup.Clear() Method

Removes all child views from the list of child views.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.ViewGroup.Contains(Tizen.UI.View)'></a>

## ViewGroup.Contains(View) Method

Checks if the list of child views contains the specified child view.

```csharp
public bool Contains(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.Contains(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to check for.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the list of child views contains the child view, false otherwise.

<a name='Tizen.UI.ViewGroup.CopyTo(Tizen.UI.View[],int)'></a>

## ViewGroup.CopyTo(View[], int) Method

Copies the child views in the list of child views to the specified array, starting at the specified index.

```csharp
public void CopyTo(Tizen.UI.View[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.CopyTo(Tizen.UI.View[],int).array'></a>

`array` [View](Tizen.UI.View.md 'Tizen.UI.View')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the child views to.

<a name='Tizen.UI.ViewGroup.CopyTo(Tizen.UI.View[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

<a name='Tizen.UI.ViewGroup.GetDescendant(string)'></a>

## ViewGroup.GetDescendant(string) Method

Gets the descendant view with the specified name.

```csharp
public override Tizen.UI.View GetDescendant(string name);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.GetDescendant(string).name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of the descendant view to find.

#### Returns
[View](Tizen.UI.View.md 'Tizen.UI.View')  
The descendant view with the specified name, or null if it is not found.

<a name='Tizen.UI.ViewGroup.GetEnumerator()'></a>

## ViewGroup.GetEnumerator() Method

Returns an enumerator that iterates through the list of child views.

```csharp
public System.Collections.Generic.IEnumerator&lt;Tizen.UI.View> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[View](Tizen.UI.View.md 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the list of child views.

<a name='Tizen.UI.ViewGroup.IndexOf(Tizen.UI.View)'></a>

## ViewGroup.IndexOf(View) Method

Gets the index of the specified child view in the list of child views.

```csharp
public int IndexOf(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.IndexOf(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to find the index of.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the child view, or -1 if it is not found.

<a name='Tizen.UI.ViewGroup.Insert(int,Tizen.UI.View)'></a>

## ViewGroup.Insert(int, View) Method

Inserts a child view at the specified index in the list of child views.

```csharp
public void Insert(int index, Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.Insert(int,Tizen.UI.View).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child view at.

<a name='Tizen.UI.ViewGroup.Insert(int,Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to insert.

<a name='Tizen.UI.ViewGroup.Remove(Tizen.UI.View)'></a>

## ViewGroup.Remove(View) Method

Removes the specified child view from the list of child views.

```csharp
public bool Remove(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.Remove(Tizen.UI.View).item'></a>

`item` [View](Tizen.UI.View.md 'Tizen.UI.View')

The child view to remove.

Implements [Remove(View)](Tizen.UI.IParentObject.md#Tizen.UI.IParentObject.Remove(Tizen.UI.View) 'Tizen.UI.IParentObject.Remove(Tizen.UI.View)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the child view was removed, false otherwise.

<a name='Tizen.UI.ViewGroup.RemoveAt(int)'></a>

## ViewGroup.RemoveAt(int) Method

Removes the child view at the specified index from the list of child views.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.ViewGroup.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the child view to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Explicit Interface Implementations

<a name='Tizen.UI.ViewGroup.System.Collections.IEnumerable.GetEnumerator()'></a>

## ViewGroup.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the list of child views.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')




