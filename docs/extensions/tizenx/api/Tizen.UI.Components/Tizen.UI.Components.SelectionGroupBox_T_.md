### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## SelectionGroupBox&lt;T> Class

A group view of tab items for tab bar implementation.

```csharp
public abstract class SelectionGroupBox&lt;T> : Tizen.UI.ContentView,
Tizen.UI.Components.ISelectionGroup,
Tizen.UI.Components.ILayoutBox,
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable
    where T : Tizen.UI.View, Tizen.UI.Components.IGroupSelectable
```
#### Type parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; SelectionGroupBox&lt;T>

Implements [ISelectionGroup](Tizen.UI.Components.ISelectionGroup.md 'Tizen.UI.Components.ISelectionGroup'), [ILayoutBox](Tizen.UI.Components.ILayoutBox.md 'Tizen.UI.Components.ILayoutBox'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Components.SelectionGroupBox_T_.SelectionGroupBox()'></a>

## SelectionGroupBox() Constructor

Construct a new instance.

```csharp
public SelectionGroupBox();
```
### Properties

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Children'></a>

## SelectionGroupBox&lt;T>.Children Property

Children of the layout box.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

Implements [Children](Tizen.UI.Components.ILayoutBox.md#Tizen.UI.Components.ILayoutBox.Children 'Tizen.UI.Components.ILayoutBox.Children')

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Count'></a>

## SelectionGroupBox&lt;T>.Count Property

Gets the number of child items.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.EmptySelectionAllowed'></a>

## SelectionGroupBox&lt;T>.EmptySelectionAllowed Property

Gets or sets a value indicating whether empty selection is allowed.  
If it is set to true, it allows the no selection state when initializing or when deselecting selected item by code.

```csharp
public bool EmptySelectionAllowed { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.IsReadOnly'></a>

## SelectionGroupBox&lt;T>.IsReadOnly Property

Gets a value indicating whether the list of child items is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.ItemClickedCommand'></a>

## SelectionGroupBox&lt;T>.ItemClickedCommand Property

ItemClicked event command. [ItemClicked](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.ItemClicked 'Tizen.UI.Components.SelectionGroupBox&lt;T>.ItemClicked'). Note that this only works where item is [IClickable](Tizen.UI.Components.IClickable.md 'Tizen.UI.Components.IClickable').

```csharp
public System.Action&lt;object,Tizen.UI.Components.SelectionGroupItemClickedEventArgs> ItemClickedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[SelectionGroupItemClickedEventArgs](Tizen.UI.Components.SelectionGroupItemClickedEventArgs.md 'Tizen.UI.Components.SelectionGroupItemClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Items'></a>

## SelectionGroupBox&lt;T>.Items Property

Gets the list of child items.

```csharp
public System.Collections.Generic.ICollection&lt;T> Items { get; }
```

#### Property Value
[System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Padding'></a>

## SelectionGroupBox&lt;T>.Padding Property

Gets or sets the padding of the layout box.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

Implements [Padding](Tizen.UI.Components.ILayoutBox.md#Tizen.UI.Components.ILayoutBox.Padding 'Tizen.UI.Components.ILayoutBox.Padding')

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.SelectedIndex'></a>

## SelectionGroupBox&lt;T>.SelectedIndex Property

Gets the current selected item index.

```csharp
public int SelectedIndex { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.SelectedItem'></a>

## SelectionGroupBox&lt;T>.SelectedItem Property

Gets the current selected item.

```csharp
public T SelectedItem { get; }
```

#### Property Value
[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.SelectionChangedCommand'></a>

## SelectionGroupBox&lt;T>.SelectionChangedCommand Property

Selected child changed event command. [SelectionChanged](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.SelectionChanged 'Tizen.UI.Components.SelectionGroupBox&lt;T>.SelectionChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.GroupSelectionChangedEventArgs> SelectionChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[GroupSelectionChangedEventArgs](Tizen.UI.Components.GroupSelectionChangedEventArgs.md 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.this[int]'></a>

## SelectionGroupBox&lt;T>.this[int] Property

Gets or sets the tab items.

```csharp
public T this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')
### Methods

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Add(T)'></a>

## SelectionGroupBox&lt;T>.Add(T) Method

Adds an item to Tab bar.

```csharp
public void Add(T item);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Add(T).item'></a>

`item` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

The child item to be added.

Implements [Add(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Clear()'></a>

## SelectionGroupBox&lt;T>.Clear() Method

Removes all child items from the list of child items.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Contains(T)'></a>

## SelectionGroupBox&lt;T>.Contains(T) Method

Checks if the list of child items contains the specified child item.

```csharp
public bool Contains(T item);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Contains(T).item'></a>

`item` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

The child item to check for.

Implements [Contains(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Contains#System_Collections_Generic_ICollection_1_Contains__0_ 'System.Collections.Generic.ICollection`1.Contains(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the list of child items contains the child item, false otherwise.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.CopyTo(T[],int)'></a>

## SelectionGroupBox&lt;T>.CopyTo(T[], int) Method

Copies the child items in the list of child items to the specified array, starting at the specified index.

```csharp
public void CopyTo(T[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.CopyTo(T[],int).array'></a>

`array` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the child items to.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.CopyTo(T[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

Implements [CopyTo(T[], int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.CopyTo#System_Collections_Generic_ICollection_1_CopyTo__0[],System_Int32_ 'System.Collections.Generic.ICollection`1.CopyTo(`0[],System.Int32)')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.GetEnumerator()'></a>

## SelectionGroupBox&lt;T>.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
public System.Collections.Generic.IEnumerator&lt;T> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the list of child items.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.IndexOf(T)'></a>

## SelectionGroupBox&lt;T>.IndexOf(T) Method

Gets the index of the specified child item in the list of child items.

```csharp
public int IndexOf(T item);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.IndexOf(T).item'></a>

`item` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

The child item to find the index of.

Implements [IndexOf(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.IndexOf#System_Collections_Generic_IList_1_IndexOf__0_ 'System.Collections.Generic.IList`1.IndexOf(`0)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the child item, or -1 if it is not found.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Insert(int,T)'></a>

## SelectionGroupBox&lt;T>.Insert(int, T) Method

Inserts a child item at the specified index in the list of child items.

```csharp
public void Insert(int index, T item);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Insert(int,T).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child item at.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Insert(int,T).item'></a>

`item` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

The child item to insert.

Implements [Insert(int, T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Insert#System_Collections_Generic_IList_1_Insert_System_Int32,_0_ 'System.Collections.Generic.IList`1.Insert(System.Int32,`0)')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Remove(T)'></a>

## SelectionGroupBox&lt;T>.Remove(T) Method

Removes the item from Tab bar.

```csharp
public bool Remove(T item);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Remove(T).item'></a>

`item` [T](Tizen.UI.Components.SelectionGroupBox_T_.md#Tizen.UI.Components.SelectionGroupBox_T_.T 'Tizen.UI.Components.SelectionGroupBox&lt;T>.T')

The child item to be removed.

Implements [Remove(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the item was removed, false otherwise.

<a name='Tizen.UI.Components.SelectionGroupBox_T_.RemoveAt(int)'></a>

## SelectionGroupBox&lt;T>.RemoveAt(int) Method

Removes the child item at the specified index from the list of child items.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroupBox_T_.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the child item to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Events

<a name='Tizen.UI.Components.SelectionGroupBox_T_.ItemClicked'></a>

## SelectionGroupBox&lt;T>.ItemClicked Event

Occurs when the one of item has clicked. Note that this only works where item is [IClickable](Tizen.UI.Components.IClickable.md 'Tizen.UI.Components.IClickable').

```csharp
public event EventHandler&lt;SelectionGroupItemClickedEventArgs> ItemClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[SelectionGroupItemClickedEventArgs](Tizen.UI.Components.SelectionGroupItemClickedEventArgs.md 'Tizen.UI.Components.SelectionGroupItemClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.SelectionChanged'></a>

## SelectionGroupBox&lt;T>.SelectionChanged Event

Occures when the selected item is changed.

```csharp
public event EventHandler&lt;GroupSelectionChangedEventArgs> SelectionChanged;
```

Implements [SelectionChanged](Tizen.UI.Components.ISelectionGroup.md#Tizen.UI.Components.ISelectionGroup.SelectionChanged 'Tizen.UI.Components.ISelectionGroup.SelectionChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[GroupSelectionChangedEventArgs](Tizen.UI.Components.GroupSelectionChangedEventArgs.md 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.SelectionGroupBox_T_.System.Collections.IEnumerable.GetEnumerator()'></a>

## SelectionGroupBox&lt;T>.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

<a name='Tizen.UI.Components.SelectionGroupBox_T_.Tizen.UI.Components.ISelectionGroup.Selected'></a>

## SelectionGroupBox&lt;T>.Tizen.UI.Components.ISelectionGroup.Selected Property

The selected child in the group.

```csharp
Tizen.UI.Components.IGroupSelectable Tizen.UI.Components.ISelectionGroup.Selected { get; }
```

Implements [Selected](Tizen.UI.Components.ISelectionGroup.md#Tizen.UI.Components.ISelectionGroup.Selected 'Tizen.UI.Components.ISelectionGroup.Selected')


























































