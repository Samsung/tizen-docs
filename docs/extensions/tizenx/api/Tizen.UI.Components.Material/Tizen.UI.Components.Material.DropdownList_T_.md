### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## DropdownList&lt;T> Class

The selectable item container desinged to be posted above the other objects.

```csharp
public class DropdownList&lt;T> : Tizen.UI.ContentView,
Tizen.UI.Components.IAnchoredModal,
Tizen.UI.Components.ISelectionGroup,
System.Collections.Generic.IList&lt;T>,
System.Collections.Generic.ICollection&lt;T>,
System.Collections.Generic.IEnumerable&lt;T>,
System.Collections.IEnumerable
    where T : Tizen.UI.View, Tizen.UI.Components.IGroupSelectable, Tizen.UI.Components.IClickable
```
#### Type parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.T'></a>

`T`

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; DropdownList&lt;T>

Derived  
&#8627; [DropdownList](Tizen.UI.Components.Material.DropdownList.md 'Tizen.UI.Components.Material.DropdownList')

Implements [Tizen.UI.Components.IAnchoredModal](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal 'Tizen.UI.Components.IAnchoredModal'), [Tizen.UI.Components.ISelectionGroup](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup 'Tizen.UI.Components.ISelectionGroup'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Components.Material.DropdownList_T_.DropdownList()'></a>

## DropdownList() Constructor

Creates a new instance.

```csharp
public DropdownList();
```

<a name='Tizen.UI.Components.Material.DropdownList_T_.DropdownList(Tizen.UI.Components.Material.DropdownListVariables)'></a>

## DropdownList(DropdownListVariables) Constructor

Creates a new instance.

```csharp
public DropdownList(Tizen.UI.Components.Material.DropdownListVariables variables);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.DropdownList(Tizen.UI.Components.Material.DropdownListVariables).variables'></a>

`variables` [DropdownListVariables](Tizen.UI.Components.Material.DropdownListVariables.md 'Tizen.UI.Components.Material.DropdownListVariables')
### Properties

<a name='Tizen.UI.Components.Material.DropdownList_T_.Count'></a>

## DropdownList&lt;T>.Count Property

Gets the number of child items.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.DropdownList_T_.DismissedCommand'></a>

## DropdownList&lt;T>.DismissedCommand Property

Dismissed event command. [Dismissed](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.Dismissed 'Tizen.UI.Components.Material.DropdownList&lt;T>.Dismissed').

```csharp
public System.Action&lt;object,System.EventArgs> DismissedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.DropdownList_T_.EmptySelectionAllowed'></a>

## DropdownList&lt;T>.EmptySelectionAllowed Property

Gets or sets a value indicating whether empty selection is allowed.  
If it is set to true, it allows the no selection state when initializing or when deselecting selected item by code.

```csharp
public bool EmptySelectionAllowed { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.DropdownList_T_.HiddenCommand'></a>

## DropdownList&lt;T>.HiddenCommand Property

Dismissed event command. [Hidden](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.Hidden 'Tizen.UI.Components.Material.DropdownList&lt;T>.Hidden').

```csharp
public System.Action&lt;object,System.EventArgs> HiddenCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.EventArgs](https://docs.microsoft.com/en-us/dotnet/api/System.EventArgs 'System.EventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.DropdownList_T_.IsReadOnly'></a>

## DropdownList&lt;T>.IsReadOnly Property

Gets a value indicating whether the list of child items is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.DropdownList_T_.ItemClickedCommand'></a>

## DropdownList&lt;T>.ItemClickedCommand Property

ItemClicked event command. [ItemClicked](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.ItemClicked 'Tizen.UI.Components.Material.DropdownList&lt;T>.ItemClicked').

```csharp
public System.Action&lt;object,Tizen.UI.Components.SelectionGroupItemClickedEventArgs> ItemClickedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[Tizen.UI.Components.SelectionGroupItemClickedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.SelectionGroupItemClickedEventArgs 'Tizen.UI.Components.SelectionGroupItemClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Items'></a>

## DropdownList&lt;T>.Items Property

Gets or sets the index of the currently selected child item.

```csharp
public System.Collections.Generic.IList&lt;T> Items { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Material.DropdownList_T_.ModalPivot'></a>

## DropdownList&lt;T>.ModalPivot Property

Gets or sets the modal pivot. It is used to calculate the position when it is posted.

```csharp
public Tizen.UI.Components.ModalPivot ModalPivot { get; set; }
```

Implements [ModalPivot](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal.ModalPivot 'Tizen.UI.Components.IAnchoredModal.ModalPivot')

#### Property Value
[Tizen.UI.Components.ModalPivot](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ModalPivot 'Tizen.UI.Components.ModalPivot')

### Remarks
Changing this property after the dropdown list is added to the scene graph will have no effect.

<a name='Tizen.UI.Components.Material.DropdownList_T_.SelectedIndex'></a>

## DropdownList&lt;T>.SelectedIndex Property

Gets the current selected item index.

```csharp
public int SelectedIndex { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.DropdownList_T_.SelectedItem'></a>

## DropdownList&lt;T>.SelectedItem Property

Gets the current selected item.

```csharp
public T SelectedItem { get; }
```

#### Property Value
[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

<a name='Tizen.UI.Components.Material.DropdownList_T_.SelectionChangedCommand'></a>

## DropdownList&lt;T>.SelectionChangedCommand Property

Selected item changed event command. [SelectionChanged](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.SelectionChanged 'Tizen.UI.Components.Material.DropdownList&lt;T>.SelectionChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.GroupSelectionChangedEventArgs> SelectionChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[Tizen.UI.Components.GroupSelectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectionChangedEventArgs 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.Material.DropdownList_T_.this[int]'></a>

## DropdownList&lt;T>.this[int] Property

Gets or sets the items.

```csharp
public T this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')
### Methods

<a name='Tizen.UI.Components.Material.DropdownList_T_.Add(T)'></a>

## DropdownList&lt;T>.Add(T) Method

Adds an item to the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1').

```csharp
public void Add(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Add(T).item'></a>

`item` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

The object to add to the [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1').

Implements [Add(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

#### Exceptions

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.Generic.ICollection&lt;&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1') is read-only.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Clear()'></a>

## DropdownList&lt;T>.Clear() Method

Removes all child items from the list of child items.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Contains(T)'></a>

## DropdownList&lt;T>.Contains(T) Method

Checks if the list of child items contains the specified child item.

```csharp
public bool Contains(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Contains(T).item'></a>

`item` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

The child item to check for.

Implements [Contains(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Contains#System_Collections_Generic_ICollection_1_Contains__0_ 'System.Collections.Generic.ICollection`1.Contains(`0)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
True if the list of child items contains the child item, false otherwise.

<a name='Tizen.UI.Components.Material.DropdownList_T_.CopyTo(T[],int)'></a>

## DropdownList&lt;T>.CopyTo(T[], int) Method

Copies the child items in the list of child items to the specified array, starting at the specified index.

```csharp
public void CopyTo(T[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.CopyTo(T[],int).array'></a>

`array` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the child items to.

<a name='Tizen.UI.Components.Material.DropdownList_T_.CopyTo(T[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

Implements [CopyTo(T[], int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.CopyTo#System_Collections_Generic_ICollection_1_CopyTo__0[],System_Int32_ 'System.Collections.Generic.ICollection`1.CopyTo(`0[],System.Int32)')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Dismiss()'></a>

## DropdownList&lt;T>.Dismiss() Method

Dismiss the modal from the window.

```csharp
public void Dismiss();
```

<a name='Tizen.UI.Components.Material.DropdownList_T_.GetEnumerator()'></a>

## DropdownList&lt;T>.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
public System.Collections.Generic.IEnumerator&lt;T> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the list of child items.

<a name='Tizen.UI.Components.Material.DropdownList_T_.IndexOf(T)'></a>

## DropdownList&lt;T>.IndexOf(T) Method

Gets the index of the specified child item in the list of child items.

```csharp
public int IndexOf(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.IndexOf(T).item'></a>

`item` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

The child item to find the index of.

Implements [IndexOf(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.IndexOf#System_Collections_Generic_IList_1_IndexOf__0_ 'System.Collections.Generic.IList`1.IndexOf(`0)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of the child item, or -1 if it is not found.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Insert(int,T)'></a>

## DropdownList&lt;T>.Insert(int, T) Method

Inserts a child item at the specified index in the list of child items.

```csharp
public void Insert(int index, T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Insert(int,T).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child item at.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Insert(int,T).item'></a>

`item` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

The child item to insert.

Implements [Insert(int, T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Insert#System_Collections_Generic_IList_1_Insert_System_Int32,_0_ 'System.Collections.Generic.IList`1.Insert(System.Int32,`0)')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post()'></a>

## DropdownList&lt;T>.Post() Method

Post as a modal content.

```csharp
public void Post();
```

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Rect)'></a>

## DropdownList&lt;T>.Post(Rect) Method

Post as a modal content with anchor data.

```csharp
public void Post(Tizen.UI.Rect anchorBounds);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Rect).anchorBounds'></a>

`anchorBounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds of the anchor object. It should be relative to the window's coordinate system.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window)'></a>

## DropdownList&lt;T>.Post(Window) Method

Post as a modal content to the given window. If no window is specified, it uses default window.

```csharp
public void Post(Tizen.UI.Window window);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to post the modal to.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect)'></a>

## DropdownList&lt;T>.Post(Window, Rect) Method

Post as a modal content to the given window with anchor data.

```csharp
public void Post(Tizen.UI.Window window, Tizen.UI.Rect anchorBounds);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to post the modal to.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect).anchorBounds'></a>

`anchorBounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds of the anchor object. It should be relative to the window's coordinate system.

Implements [Post(Window, Rect)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal.Post#Tizen_UI_Components_IAnchoredModal_Post_Tizen_UI_Window,Tizen_UI_Rect_ 'Tizen.UI.Components.IAnchoredModal.Post(Tizen.UI.Window,Tizen.UI.Rect)')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect,Tizen.UI.Rect)'></a>

## DropdownList&lt;T>.Post(Window, Rect, Rect) Method

Post as a modal content to the given window. If no window is specified, it uses default window.

```csharp
public void Post(Tizen.UI.Window window, Tizen.UI.Rect anchorBounds, Tizen.UI.Rect restrictBounds);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect,Tizen.UI.Rect).window'></a>

`window` [Tizen.UI.Window](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Window 'Tizen.UI.Window')

The window to post the modal to.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect,Tizen.UI.Rect).anchorBounds'></a>

`anchorBounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds of the anchor object. It should be relative to the window's coordinate system.

<a name='Tizen.UI.Components.Material.DropdownList_T_.Post(Tizen.UI.Window,Tizen.UI.Rect,Tizen.UI.Rect).restrictBounds'></a>

`restrictBounds` [Tizen.UI.Rect](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Rect 'Tizen.UI.Rect')

The bounds to restrict the modal to. It should be relative to the window's coordinate system.

<a name='Tizen.UI.Components.Material.DropdownList_T_.RemoveAt(int)'></a>

## DropdownList&lt;T>.RemoveAt(int) Method

Removes the child item at the specified index from the list of child items.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the child item to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Events

<a name='Tizen.UI.Components.Material.DropdownList_T_.Dismissed'></a>

## DropdownList&lt;T>.Dismissed Event

Occurred when the dismiss requested.

```csharp
public event EventHandler Dismissed;
```

Implements [Dismissed](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.IAnchoredModal.Dismissed 'Tizen.UI.Components.IAnchoredModal.Dismissed')

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Hidden'></a>

## DropdownList&lt;T>.Hidden Event

Occurred when the dropdown list is fully dismissed (animation finished).

```csharp
public event EventHandler Hidden;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.DropdownList_T_.ItemClicked'></a>

## DropdownList&lt;T>.ItemClicked Event

Occurs when the one of item has clicked.

```csharp
public event EventHandler&lt;SelectionGroupItemClickedEventArgs> ItemClicked;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.Components.SelectionGroupItemClickedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.SelectionGroupItemClickedEventArgs 'Tizen.UI.Components.SelectionGroupItemClickedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.DropdownList_T_.SelectionChanged'></a>

## DropdownList&lt;T>.SelectionChanged Event

Occurs when the selected item is changed. [SelectedItem](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.SelectedItem 'Tizen.UI.Components.Material.DropdownList&lt;T>.SelectedItem').

```csharp
public event EventHandler&lt;GroupSelectionChangedEventArgs> SelectionChanged;
```

Implements [SelectionChanged](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup.SelectionChanged 'Tizen.UI.Components.ISelectionGroup.SelectionChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.Components.GroupSelectionChangedEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.GroupSelectionChangedEventArgs 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.Material.DropdownList_T_.System.Collections.Generic.ICollection_T_.Remove(T)'></a>

## DropdownList&lt;T>.System.Collections.Generic.ICollection&lt;T>.Remove(T) Method

Removes the item.

```csharp
bool System.Collections.Generic.ICollection&lt;T>.Remove(T item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.DropdownList_T_.System.Collections.Generic.ICollection_T_.Remove(T).item'></a>

`item` [T](Tizen.UI.Components.Material.DropdownList_T_.md#Tizen.UI.Components.Material.DropdownList_T_.T 'Tizen.UI.Components.Material.DropdownList&lt;T>.T')

The child item to be removed.

Implements [Remove(T)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

<a name='Tizen.UI.Components.Material.DropdownList_T_.System.Collections.IEnumerable.GetEnumerator()'></a>

## DropdownList&lt;T>.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the list of child items.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

<a name='Tizen.UI.Components.Material.DropdownList_T_.Tizen.UI.Components.ISelectionGroup.Selected'></a>

## DropdownList&lt;T>.Tizen.UI.Components.ISelectionGroup.Selected Property

The selected child in the group.

```csharp
Tizen.UI.Components.IGroupSelectable Tizen.UI.Components.ISelectionGroup.Selected { get; }
```

Implements [Selected](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Components.ISelectionGroup.Selected 'Tizen.UI.Components.ISelectionGroup.Selected')













































