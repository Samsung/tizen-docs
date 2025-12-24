### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## Drawer&lt;T> Class

This component supports both modal and static types of drawers.

```csharp
public abstract class Drawer&lt;T> : Tizen.UI.ContentView,
Tizen.UI.Components.ISelectionGroup,
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable
    where T : Tizen.UI.View, Tizen.UI.Components.IGroupSelectable
```
#### Type parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; Drawer&lt;T>

Derived  
&#8627; [ModalDrawer&lt;T&gt;](Tizen.UI.Components.Material.ModalDrawer_T_.md 'Tizen.UI.Components.Material.ModalDrawer&lt;T>')  
&#8627; [StaticDrawer&lt;T&gt;](Tizen.UI.Components.Material.StaticDrawer_T_.md 'Tizen.UI.Components.Material.StaticDrawer&lt;T>')

Implements [Tizen.UI.Components.ISelectionGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup 'Tizen.UI.Components.ISelectionGroup'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Components.Material.Drawer_T_.Drawer()'></a>

## Drawer() Constructor

Initializes a new instance of the Drawer class with default settings.

```csharp
public Drawer();
```

<a name='Tizen.UI.Components.Material.Drawer_T_.Drawer(Tizen.UI.Components.Material.ModalDrawerVariables)'></a>

## Drawer(ModalDrawerVariables) Constructor

Initializes a new instance of the Drawer class with specified variables.

```csharp
public Drawer(Tizen.UI.Components.Material.ModalDrawerVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.Drawer(Tizen.UI.Components.Material.ModalDrawerVariables).variables'></a>

`variables` [ModalDrawerVariables](Tizen.UI.Components.Material.ModalDrawerVariables.md 'Tizen.UI.Components.Material.ModalDrawerVariables')

The DrawerVariables object containing configuration for the drawer.
### Properties

<a name='Tizen.UI.Components.Material.Drawer_T_.Content'></a>

## Drawer&lt;T>.Content Property

Gets or sets the content of the Drawer.

```csharp
public abstract Tizen.UI.View Content { get; set; }
```

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Material.Drawer_T_.Count'></a>

## Drawer&lt;T>.Count Property

Gets the number of child items.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.Drawer_T_.IsReadOnly'></a>

## Drawer&lt;T>.IsReadOnly Property

Gets a value indicating whether the list of child items is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.Drawer_T_.Items'></a>

## Drawer&lt;T>.Items Property

Gets or sets the index of the currently selected child item.

```csharp
public System.Collections.Generic.IList&lt;T> Items { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Material.Drawer_T_.ItemSpacing'></a>

## Drawer&lt;T>.ItemSpacing Property

Gets or sets the spacing between child items.

```csharp
public float ItemSpacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.Drawer_T_.SelectedIndex'></a>

## Drawer&lt;T>.SelectedIndex Property

Gets the current selected item index.

```csharp
public int SelectedIndex { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.Drawer_T_.SelectedItem'></a>

## Drawer&lt;T>.SelectedItem Property

Gets the current selected item.

```csharp
public T SelectedItem { get; }
```

#### Property Value
[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

<a name='Tizen.UI.Components.Material.Drawer_T_.SelectionChangedCommand'></a>

## Drawer&lt;T>.SelectionChangedCommand Property

Selected child changed event command. [SelectionChanged](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.SelectionChanged 'Tizen.UI.Components.Material.Drawer&lt;T>.SelectionChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.GroupSelectionChangedEventArgs> SelectionChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[Tizen.UI.Components.GroupSelectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectionChangedEventArgs 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.Drawer_T_.this[int]'></a>

## Drawer&lt;T>.this[int] Property

Gets or sets the tab items.

```csharp
public T this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')
### Methods

<a name='Tizen.UI.Components.Material.Drawer_T_.Add(T)'></a>

## Drawer&lt;T>.Add(T) Method

Adds an item to the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1').

```csharp
public void Add(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.Add(T).item'></a>

`item` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

The object to add to the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1').

Implements [Add(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

#### Exceptions

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1') is read-only.

<a name='Tizen.UI.Components.Material.Drawer_T_.Clear()'></a>

## Drawer&lt;T>.Clear() Method

Removes all child items from the list of child items.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.Material.Drawer_T_.Contains(T)'></a>

## Drawer&lt;T>.Contains(T) Method

Checks if the list of child items contains the specified child item.

```csharp
public bool Contains(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.Contains(T).item'></a>

`item` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

The child item to check for.

Implements [Contains(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Contains#System_Collections_Generic_ICollection_1_Contains__0_ 'System.Collections.Generic.ICollection`1.Contains(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the list of child items contains the child item, false otherwise.

<a name='Tizen.UI.Components.Material.Drawer_T_.CopyTo(T[],int)'></a>

## Drawer&lt;T>.CopyTo(T[], int) Method

Copies the child items in the list of child items to the specified array, starting at the specified index.

```csharp
public void CopyTo(T[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.CopyTo(T[],int).array'></a>

`array` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the child items to.

<a name='Tizen.UI.Components.Material.Drawer_T_.CopyTo(T[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

Implements [CopyTo(T[], int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.CopyTo#System_Collections_Generic_ICollection_1_CopyTo__0[],System_Int32_ 'System.Collections.Generic.ICollection`1.CopyTo(`0[],System.Int32)')

<a name='Tizen.UI.Components.Material.Drawer_T_.GetEnumerator()'></a>

## Drawer&lt;T>.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
public System.Collections.Generic.IEnumerator&lt;T> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the list of child items.

<a name='Tizen.UI.Components.Material.Drawer_T_.IndexOf(T)'></a>

## Drawer&lt;T>.IndexOf(T) Method

Gets the index of the specified child item in the list of child items.

```csharp
public int IndexOf(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.IndexOf(T).item'></a>

`item` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

The child item to find the index of.

Implements [IndexOf(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.IndexOf#System_Collections_Generic_IList_1_IndexOf__0_ 'System.Collections.Generic.IList`1.IndexOf(`0)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the child item, or -1 if it is not found.

<a name='Tizen.UI.Components.Material.Drawer_T_.Insert(int,T)'></a>

## Drawer&lt;T>.Insert(int, T) Method

Inserts a child item at the specified index in the list of child items.

```csharp
public void Insert(int index, T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.Insert(int,T).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child item at.

<a name='Tizen.UI.Components.Material.Drawer_T_.Insert(int,T).item'></a>

`item` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

The child item to insert.

Implements [Insert(int, T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Insert#System_Collections_Generic_IList_1_Insert_System_Int32,_0_ 'System.Collections.Generic.IList`1.Insert(System.Int32,`0)')

<a name='Tizen.UI.Components.Material.Drawer_T_.RemoveAt(int)'></a>

## Drawer&lt;T>.RemoveAt(int) Method

Removes the child item at the specified index from the list of child items.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the child item to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Events

<a name='Tizen.UI.Components.Material.Drawer_T_.SelectionChanged'></a>

## Drawer&lt;T>.SelectionChanged Event

Event that is triggered when the selected item in the drawer changes.

```csharp
public event EventHandler&lt;GroupSelectionChangedEventArgs> SelectionChanged;
```

Implements [SelectionChanged](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup.SelectionChanged 'Tizen.UI.Components.ISelectionGroup.SelectionChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.Components.GroupSelectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectionChangedEventArgs 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.Material.Drawer_T_.System.Collections.Generic.ICollection_T_.Remove(T)'></a>

## Drawer&lt;T>.System.Collections.Generic.ICollection&lt;T>.Remove(T) Method

Removes the item from drawer.

```csharp
bool System.Collections.Generic.ICollection&lt;T>.Remove(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.Drawer_T_.System.Collections.Generic.ICollection_T_.Remove(T).item'></a>

`item` [T](Tizen.UI.Components.Material.Drawer_T_.md#Tizen.UI.Components.Material.Drawer_T_.T 'Tizen.UI.Components.Material.Drawer&lt;T>.T')

The child item to be removed.

Implements [Remove(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

<a name='Tizen.UI.Components.Material.Drawer_T_.System.Collections.IEnumerable.GetEnumerator()'></a>

## Drawer&lt;T>.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

<a name='Tizen.UI.Components.Material.Drawer_T_.Tizen.UI.Components.ISelectionGroup.Selected'></a>

## Drawer&lt;T>.Tizen.UI.Components.ISelectionGroup.Selected Property

The selected child in the group.

```csharp
Tizen.UI.Components.IGroupSelectable Tizen.UI.Components.ISelectionGroup.Selected { get; }
```

Implements [Selected](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup.Selected 'Tizen.UI.Components.ISelectionGroup.Selected')













































