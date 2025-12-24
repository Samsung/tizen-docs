### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## GroupSelectableBox Class

Selectable component with a content.

```csharp
public abstract class GroupSelectableBox : Tizen.UI.Components.GroupSelectable,
Tizen.UI.Components.ILayoutBox,
System.Collections.Generic.IList&lt;Tizen.UI.View>,
System.Collections.Generic.ICollection&lt;Tizen.UI.View>,
System.Collections.Generic.IEnumerable&lt;Tizen.UI.View>,
System.Collections.IEnumerable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; [Pressable](Tizen.UI.Components.Pressable.md 'Tizen.UI.Components.Pressable') &#129106; [Clickable](Tizen.UI.Components.Clickable.md 'Tizen.UI.Components.Clickable') &#129106; [Selectable](Tizen.UI.Components.Selectable.md 'Tizen.UI.Components.Selectable') &#129106; [GroupSelectable](Tizen.UI.Components.GroupSelectable.md 'Tizen.UI.Components.GroupSelectable') &#129106; GroupSelectableBox

Implements [ILayoutBox](Tizen.UI.Components.ILayoutBox.md 'Tizen.UI.Components.ILayoutBox'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Properties

<a name='Tizen.UI.Components.GroupSelectableBox.Children'></a>

## GroupSelectableBox.Children Property

Children of the layout box.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

Implements [Children](Tizen.UI.Components.ILayoutBox.md#Tizen.UI.Components.ILayoutBox.Children 'Tizen.UI.Components.ILayoutBox.Children')

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.GroupSelectableBox.Count'></a>

## GroupSelectableBox.Count Property

Gets the number of elements contained in the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1').

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.GroupSelectableBox.IsReadOnly'></a>

## GroupSelectableBox.IsReadOnly Property

Gets a value indicating whether the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1') is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.GroupSelectableBox.Padding'></a>

## GroupSelectableBox.Padding Property

Gets or sets the padding of the layout box.

```csharp
public abstract Tizen.UI.Thickness Padding { get; set; }
```

Implements [Padding](Tizen.UI.Components.ILayoutBox.md#Tizen.UI.Components.ILayoutBox.Padding 'Tizen.UI.Components.ILayoutBox.Padding')

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.GroupSelectableBox.this[int]'></a>

## GroupSelectableBox.this[int] Property

Gets a content view with index.

```csharp
public Tizen.UI.View this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.Components.GroupSelectableBox.Clear()'></a>

## GroupSelectableBox.Clear() Method

Clears all children.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.GroupSelectableBox.Contains(Tizen.UI.View)'></a>

## GroupSelectableBox.Contains(View) Method

Whether it contains the specified child.

```csharp
public bool Contains(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.Contains(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.GroupSelectableBox.CopyTo(Tizen.UI.View[],int)'></a>

## GroupSelectableBox.CopyTo(View[], int) Method

Copies the children to an array.

```csharp
public void CopyTo(Tizen.UI.View[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.CopyTo(Tizen.UI.View[],int).array'></a>

`array` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Components.GroupSelectableBox.CopyTo(Tizen.UI.View[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.GroupSelectableBox.GetEnumerator()'></a>

## GroupSelectableBox.GetEnumerator() Method

Returns an enumerator that iterates through the collection.

```csharp
public System.Collections.Generic.IEnumerator&lt;Tizen.UI.View> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator that can be used to iterate through the collection.

<a name='Tizen.UI.Components.GroupSelectableBox.Insert(int,Tizen.UI.View)'></a>

## GroupSelectableBox.Insert(int, View) Method

(Not implemented) Inserts the specified content at the specified index.

```csharp
public void Insert(int index, Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.Insert(int,Tizen.UI.View).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.GroupSelectableBox.Insert(int,Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.GroupSelectableBox.RemoveAt(int)'></a>

## GroupSelectableBox.RemoveAt(int) Method

Removes the content at the specified index.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.GroupSelectableBox.System.Collections.Generic.ICollection_Tizen.UI.View_.Add(Tizen.UI.View)'></a>

## GroupSelectableBox.System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Add(View) Method

Adds a child view.

```csharp
void System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Add(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.System.Collections.Generic.ICollection_Tizen.UI.View_.Add(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

Implements [Add(View)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

<a name='Tizen.UI.Components.GroupSelectableBox.System.Collections.Generic.ICollection_Tizen.UI.View_.Remove(Tizen.UI.View)'></a>

## GroupSelectableBox.System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Remove(View) Method

Removes the specified content from the layout box.

```csharp
bool System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Remove(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.GroupSelectableBox.System.Collections.Generic.ICollection_Tizen.UI.View_.Remove(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

Implements [Remove(View)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

<a name='Tizen.UI.Components.GroupSelectableBox.System.Collections.IEnumerable.GetEnumerator()'></a>

## GroupSelectableBox.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through a collection.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')


























































