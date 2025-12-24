### [Tizen.UI.Components](Tizen.UI.Components.md 'Tizen.UI.Components')

## SelectionGroup Class

SelectionGroup is the selection manager of [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable').

```csharp
public class SelectionGroup :
System.Collections.Generic.IList&lt;Tizen.UI.Components.IGroupSelectable>,
System.Collections.Generic.ICollection&lt;Tizen.UI.Components.IGroupSelectable>,
System.Collections.Generic.IEnumerable&lt;Tizen.UI.Components.IGroupSelectable>,
System.Collections.IEnumerable,
Tizen.UI.Components.ISelectionGroup,
System.IDisposable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; SelectionGroup

Implements [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable'), [ISelectionGroup](Tizen.UI.Components.ISelectionGroup.md 'Tizen.UI.Components.ISelectionGroup'), [System.IDisposable](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable 'System.IDisposable')
### Properties

<a name='Tizen.UI.Components.SelectionGroup.Children'></a>

## SelectionGroup.Children Property

Gets the list of child selectable.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.Components.IGroupSelectable> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.SelectionGroup.Count'></a>

## SelectionGroup.Count Property

Gets the number of child selectable.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Count 'System.Collections.Generic.ICollection`1.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.SelectionGroup.IsReadOnly'></a>

## SelectionGroup.IsReadOnly Property

Gets a value indicating whether the list of selectables is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.IsReadOnly 'System.Collections.Generic.ICollection`1.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.SelectionGroup.Name'></a>

## SelectionGroup.Name Property

The name of the selection group.

```csharp
public string Name { get; }
```

#### Property Value
[System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

<a name='Tizen.UI.Components.SelectionGroup.Selected'></a>

## SelectionGroup.Selected Property

The selected child in the group.

```csharp
public Tizen.UI.Components.IGroupSelectable Selected { get; set; }
```

Implements [Selected](Tizen.UI.Components.ISelectionGroup.md#Tizen.UI.Components.ISelectionGroup.Selected 'Tizen.UI.Components.ISelectionGroup.Selected')

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

<a name='Tizen.UI.Components.SelectionGroup.SelectedIndex'></a>

## SelectionGroup.SelectedIndex Property

The selected child index in the group.

```csharp
public int SelectedIndex { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.SelectionGroup.SelectionChangedCommand'></a>

## SelectionGroup.SelectionChangedCommand Property

Selected child changed event command. [SelectionChanged](Tizen.UI.Components.SelectionGroup.md#Tizen.UI.Components.SelectionGroup.SelectionChanged 'Tizen.UI.Components.SelectionGroup.SelectionChanged').

```csharp
public System.Action&lt;object,Tizen.UI.Components.GroupSelectionChangedEventArgs> SelectionChangedCommand { get; set; }
```

#### Property Value
[System.Action&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')[,](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')[GroupSelectionChangedEventArgs](Tizen.UI.Components.GroupSelectionChangedEventArgs.md 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Action-2 'System.Action`2')

<a name='Tizen.UI.Components.SelectionGroup.this[int]'></a>

## SelectionGroup.this[int] Property

Gets the child selectable at the specified index.

```csharp
public Tizen.UI.Components.IGroupSelectable this[int index] { get; }
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

<a name='Tizen.UI.Components.SelectionGroup.this[string]'></a>

## SelectionGroup.this[string] Property

Gets the selectable child by name.

```csharp
public Tizen.UI.Components.IGroupSelectable this[string name] { get; }
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.this[string].name'></a>

`name` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

#### Property Value
[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')
### Methods

<a name='Tizen.UI.Components.SelectionGroup.Add(Tizen.UI.Components.IGroupSelectable)'></a>

## SelectionGroup.Add(IGroupSelectable) Method

Add selectable child to selection group.

```csharp
public void Add(Tizen.UI.Components.IGroupSelectable selectable);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Add(Tizen.UI.Components.IGroupSelectable).selectable'></a>

`selectable` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The selectable child.

<a name='Tizen.UI.Components.SelectionGroup.Clear()'></a>

## SelectionGroup.Clear() Method

Removes all selectabls from the group.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.SelectionGroup.Contains(Tizen.UI.Components.IGroupSelectable)'></a>

## SelectionGroup.Contains(IGroupSelectable) Method

Check selection group contains specific child.

```csharp
public bool Contains(Tizen.UI.Components.IGroupSelectable selectable);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Contains(Tizen.UI.Components.IGroupSelectable).selectable'></a>

`selectable` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The selectable child.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.SelectionGroup.CopyTo(Tizen.UI.Components.IGroupSelectable[],int)'></a>

## SelectionGroup.CopyTo(IGroupSelectable[], int) Method

Copies the selectables in the selection group to the specified array, starting at the specified index.

```csharp
public void CopyTo(Tizen.UI.Components.IGroupSelectable[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.CopyTo(Tizen.UI.Components.IGroupSelectable[],int).array'></a>

`array` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The array to copy the selectable to.

<a name='Tizen.UI.Components.SelectionGroup.CopyTo(Tizen.UI.Components.IGroupSelectable[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index in the array to start copying.

<a name='Tizen.UI.Components.SelectionGroup.Dispose()'></a>

## SelectionGroup.Dispose() Method

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose();
```

Implements [Dispose()](https://docs.microsoft.com/en-us/dotnet/api/System.IDisposable.Dispose 'System.IDisposable.Dispose')

<a name='Tizen.UI.Components.SelectionGroup.Find(string)'></a>

## SelectionGroup.Find(string) Method

Find the selection group by group name.  
if group is not exist, create new selection group.

```csharp
public static Tizen.UI.Components.SelectionGroup Find(string groupName);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Find(string).groupName'></a>

`groupName` [System.String](https://docs.microsoft.com/en-us/dotnet/api/System.String 'System.String')

The name of group to find.

#### Returns
[SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup')

<a name='Tizen.UI.Components.SelectionGroup.Find(Tizen.UI.View)'></a>

## SelectionGroup.Find(View) Method

Find the selection group by group parent view.  
if group is not exist, create new selection group.

```csharp
public static Tizen.UI.Components.SelectionGroup Find(Tizen.UI.View parent);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Find(Tizen.UI.View).parent'></a>

`parent` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

The parent view to find.

#### Returns
[SelectionGroup](Tizen.UI.Components.SelectionGroup.md 'Tizen.UI.Components.SelectionGroup')

<a name='Tizen.UI.Components.SelectionGroup.GetEnumerator()'></a>

## SelectionGroup.GetEnumerator() Method

Returns an enumerator that iterates through the group.

```csharp
public System.Collections.Generic.IEnumerator&lt;Tizen.UI.Components.IGroupSelectable> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator for the group.

<a name='Tizen.UI.Components.SelectionGroup.IndexOf(Tizen.UI.Components.IGroupSelectable)'></a>

## SelectionGroup.IndexOf(IGroupSelectable) Method

Gets the index of selectable child in the group.

```csharp
public int IndexOf(Tizen.UI.Components.IGroupSelectable selectable);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.IndexOf(Tizen.UI.Components.IGroupSelectable).selectable'></a>

`selectable` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The selectable child.

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.SelectionGroup.Insert(int,Tizen.UI.Components.IGroupSelectable)'></a>

## SelectionGroup.Insert(int, IGroupSelectable) Method

Inserts a selectable at the specified index in the group.

```csharp
public void Insert(int index, Tizen.UI.Components.IGroupSelectable selectable);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Insert(int,Tizen.UI.Components.IGroupSelectable).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index to insert the child selectable at.

<a name='Tizen.UI.Components.SelectionGroup.Insert(int,Tizen.UI.Components.IGroupSelectable).selectable'></a>

`selectable` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The selectable child to insert.

<a name='Tizen.UI.Components.SelectionGroup.Remove(Tizen.UI.Components.IGroupSelectable)'></a>

## SelectionGroup.Remove(IGroupSelectable) Method

Remove selectable child from selection group.

```csharp
public bool Remove(Tizen.UI.Components.IGroupSelectable selectable);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.Remove(Tizen.UI.Components.IGroupSelectable).selectable'></a>

`selectable` [IGroupSelectable](Tizen.UI.Components.IGroupSelectable.md 'Tizen.UI.Components.IGroupSelectable')

The selectable child.

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.SelectionGroup.RemoveAt(int)'></a>

## SelectionGroup.RemoveAt(int) Method

Remove selectable child from selection group.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of the selectable child to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')
### Events

<a name='Tizen.UI.Components.SelectionGroup.SelectionChanged'></a>

## SelectionGroup.SelectionChanged Event

The event that is called when the value of [Selected](Tizen.UI.Components.SelectionGroup.md#Tizen.UI.Components.SelectionGroup.Selected 'Tizen.UI.Components.SelectionGroup.Selected') changes.

```csharp
public event EventHandler&lt;GroupSelectionChangedEventArgs> SelectionChanged;
```

Implements [SelectionChanged](Tizen.UI.Components.ISelectionGroup.md#Tizen.UI.Components.ISelectionGroup.SelectionChanged 'Tizen.UI.Components.ISelectionGroup.SelectionChanged')

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[GroupSelectionChangedEventArgs](Tizen.UI.Components.GroupSelectionChangedEventArgs.md 'Tizen.UI.Components.GroupSelectionChangedEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.SelectionGroup.System.Collections.IEnumerable.GetEnumerator()'></a>

## SelectionGroup.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through the group.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

<a name='Tizen.UI.Components.SelectionGroup.this[int]'></a>

## SelectionGroup.this[int] Property

Gets or sets the child selectable at the specified index.

```csharp
Tizen.UI.Components.IGroupSelectable this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.SelectionGroup.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)')


























































