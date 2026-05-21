### [Tizen.UI.Components.Recycler](Tizen.UI.Components.Recycler.md 'Tizen.UI.Components.Recycler')

## GroupItemSource Class

The class that provides the grouped data source for adapter.

```csharp
public class GroupItemSource :
System.Collections.IList,
System.Collections.ICollection,
System.Collections.IEnumerable,
System.Collections.Specialized.INotifyCollectionChanged
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; GroupItemSource

Implements [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList'), [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable'), [System.Collections.Specialized.INotifyCollectionChanged](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.INotifyCollectionChanged 'System.Collections.Specialized.INotifyCollectionChanged')
### Constructors

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GroupItemSource(System.Collections.IEnumerable)'></a>

## GroupItemSource(IEnumerable) Constructor

Initialize with enumerable source.

```csharp
public GroupItemSource(System.Collections.IEnumerable source);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GroupItemSource(System.Collections.IEnumerable).source'></a>

`source` [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Properties

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Count'></a>

## GroupItemSource.Count Property

Get the number of items in the source.

```csharp
public int Count { get; }
```

Implements [Count](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection.Count 'System.Collections.ICollection.Count')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GroupCount'></a>

## GroupItemSource.GroupCount Property

Get the number of groups in the source.

```csharp
public int GroupCount { get; }
```

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.HasGroupFooter'></a>

## GroupItemSource.HasGroupFooter Property

Get or set whether group has footer or not.

```csharp
public bool HasGroupFooter { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.HasGroupHeader'></a>

## GroupItemSource.HasGroupHeader Property

Get or set whether group has header or not.

```csharp
public bool HasGroupHeader { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.IsFixedSize'></a>

## GroupItemSource.IsFixedSize Property

Gets a value indicating whether the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') has a fixed size.

```csharp
public bool IsFixedSize { get; }
```

Implements [IsFixedSize](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.IsFixedSize 'System.Collections.IList.IsFixedSize')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.IsReadOnly'></a>

## GroupItemSource.IsReadOnly Property

Gets a value indicating whether the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.

```csharp
public bool IsReadOnly { get; }
```

Implements [IsReadOnly](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.IsReadOnly 'System.Collections.IList.IsReadOnly')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.IsSynchronized'></a>

## GroupItemSource.IsSynchronized Property

Gets a value indicating whether access to the [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection') is synchronized (thread safe).

```csharp
public bool IsSynchronized { get; }
```

Implements [IsSynchronized](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection.IsSynchronized 'System.Collections.ICollection.IsSynchronized')

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.SyncRoot'></a>

## GroupItemSource.SyncRoot Property

Gets an object that can be used to synchronize access to the [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection').

```csharp
public object SyncRoot { get; }
```

Implements [SyncRoot](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection.SyncRoot 'System.Collections.ICollection.SyncRoot')

#### Property Value
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

<a name='Tizen.UI.Components.Recycler.GroupItemSource.this[int]'></a>

## GroupItemSource.this[int] Property

Get the item by index. Set is not allowed.

```csharp
public object this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Item#System_Collections_IList_Item_System_Int32_ 'System.Collections.IList.Item(System.Int32)')

#### Property Value
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')
### Methods

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Add(object)'></a>

## GroupItemSource.Add(object) Method

Adds an item to the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

```csharp
public int Add(object value);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Add(object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to add to the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

Implements [Add(object)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Add#System_Collections_IList_Add_System_Object_ 'System.Collections.IList.Add(System.Object)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The position into which the new element was inserted, or -1 to indicate that the item was not inserted into the collection.

#### Exceptions

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.    
 -or-    
 The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') has a fixed size.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Clear()'></a>

## GroupItemSource.Clear() Method

Removes all items from the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Clear 'System.Collections.IList.Clear')

#### Exceptions

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Contains(object)'></a>

## GroupItemSource.Contains(object) Method

Determines whether the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') contains a specific value.

```csharp
public bool Contains(object value);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Contains(object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to locate in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

Implements [Contains(object)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Contains#System_Collections_IList_Contains_System_Object_ 'System.Collections.IList.Contains(System.Object)')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')  
[true](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool') if the [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') is found in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList'); otherwise, [false](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool').

<a name='Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int)'></a>

## GroupItemSource.CopyTo(Array, int) Method

Copies the elements of the [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection') to an [System.Array](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array'), starting at a particular [System.Array](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array') index.

```csharp
public void CopyTo(System.Array array, int index);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array'></a>

`array` [System.Array](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

The one-dimensional [System.Array](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array') that is the destination of the elements copied from [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection'). The [System.Array](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array') must have zero-based indexing.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The zero-based index in [array](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).array') at which copying begins.

Implements [CopyTo(Array, int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection.CopyTo#System_Collections_ICollection_CopyTo_System_Array,System_Int32_ 'System.Collections.ICollection.CopyTo(System.Array,System.Int32)')

#### Exceptions

[System.ArgumentNullException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentNullException 'System.ArgumentNullException')  
[array](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).array') is [null](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/null 'https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/null').

[System.ArgumentOutOfRangeException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentOutOfRangeException 'System.ArgumentOutOfRangeException')  
[index](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).index 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).index') is less than zero.

[System.ArgumentException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentException 'System.ArgumentException')  
[array](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).array') is multidimensional.    
-or-    
The number of elements in the source [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection') is greater than the available space from [index](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).index 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).index') to the end of the destination [array](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).array').    
-or-    
The type of the source [System.Collections.ICollection](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.ICollection 'System.Collections.ICollection') cannot be cast automatically to the type of the destination [array](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array,int).array 'Tizen.UI.Components.Recycler.GroupItemSource.CopyTo(System.Array, int).array').

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetAbsoluteIndex(int,int)'></a>

## GroupItemSource.GetAbsoluteIndex(int, int) Method

Get absolute index in groups

```csharp
public int GetAbsoluteIndex(int group, int ingroup);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetAbsoluteIndex(int,int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Index of group

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetAbsoluteIndex(int,int).ingroup'></a>

`ingroup` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Index of item in group

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
Index that converted to absolute position

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetChildrenCount(int)'></a>

## GroupItemSource.GetChildrenCount(int) Method

Get children count of group. It does not include header and footer.

```csharp
public int GetChildrenCount(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetChildrenCount(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of group

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The children count in the group.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetEnumerator()'></a>

## GroupItemSource.GetEnumerator() Method

Returns an enumerator that iterates through a collection.

```csharp
public System.Collections.IEnumerator GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.IEnumerator](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerator 'System.Collections.IEnumerator')  
An [System.Collections.IEnumerator](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerator 'System.Collections.IEnumerator') object that can be used to iterate through the collection.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetGroupAndIndex(int)'></a>

## GroupItemSource.GetGroupAndIndex(int) Method

Get group and index

```csharp
public (int group,int inGroup) GetGroupAndIndex(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetGroupAndIndex(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

a global index

#### Returns
[&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[,](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.ValueTuple 'System.ValueTuple')  
index of group , index in group

### Remarks
-1 means header, -2 means footer

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetGroupItem(int)'></a>

## GroupItemSource.GetGroupItem(int) Method

Get the item from group.

```csharp
public object GetGroupItem(int group);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.GetGroupItem(int).group'></a>

`group` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The index of group.

#### Returns
[System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')  
The data item object of group.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.IndexOf(object)'></a>

## GroupItemSource.IndexOf(object) Method

Determines the index of a specific item in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

```csharp
public int IndexOf(object value);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.IndexOf(object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to locate in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

Implements [IndexOf(object)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.IndexOf#System_Collections_IList_IndexOf_System_Object_ 'System.Collections.IList.IndexOf(System.Object)')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')  
The index of [value](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.IndexOf(object).value 'Tizen.UI.Components.Recycler.GroupItemSource.IndexOf(object).value') if found in the list; otherwise, -1.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object)'></a>

## GroupItemSource.Insert(int, object) Method

Inserts an item to the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') at the specified index.

```csharp
public void Insert(int index, object value);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The zero-based index at which [value](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object).value 'Tizen.UI.Components.Recycler.GroupItemSource.Insert(int, object).value') should be inserted.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to insert into the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

Implements [Insert(int, object)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Insert#System_Collections_IList_Insert_System_Int32,System_Object_ 'System.Collections.IList.Insert(System.Int32,System.Object)')

#### Exceptions

[System.ArgumentOutOfRangeException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentOutOfRangeException 'System.ArgumentOutOfRangeException')  
[index](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object).index 'Tizen.UI.Components.Recycler.GroupItemSource.Insert(int, object).index') is not a valid index in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.    
 -or-    
 The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') has a fixed size.

[System.NullReferenceException](https://docs.microsoft.com/en-us/dotnet/api/System.NullReferenceException 'System.NullReferenceException')  
[value](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.Insert(int,object).value 'Tizen.UI.Components.Recycler.GroupItemSource.Insert(int, object).value') is null reference in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Remove(object)'></a>

## GroupItemSource.Remove(object) Method

Removes the first occurrence of a specific object from the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

```csharp
public void Remove(object value);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.Remove(object).value'></a>

`value` [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object')

The object to remove from the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

Implements [Remove(object)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.Remove#System_Collections_IList_Remove_System_Object_ 'System.Collections.IList.Remove(System.Object)')

#### Exceptions

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.    
 -or-    
 The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') has a fixed size.

<a name='Tizen.UI.Components.Recycler.GroupItemSource.RemoveAt(int)'></a>

## GroupItemSource.RemoveAt(int) Method

Removes the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') item at the specified index.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Recycler.GroupItemSource.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The zero-based index of the item to remove.

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList.RemoveAt#System_Collections_IList_RemoveAt_System_Int32_ 'System.Collections.IList.RemoveAt(System.Int32)')

#### Exceptions

[System.ArgumentOutOfRangeException](https://docs.microsoft.com/en-us/dotnet/api/System.ArgumentOutOfRangeException 'System.ArgumentOutOfRangeException')  
[index](Tizen.UI.Components.Recycler.GroupItemSource.md#Tizen.UI.Components.Recycler.GroupItemSource.RemoveAt(int).index 'Tizen.UI.Components.Recycler.GroupItemSource.RemoveAt(int).index') is not a valid index in the [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList').

[System.NotSupportedException](https://docs.microsoft.com/en-us/dotnet/api/System.NotSupportedException 'System.NotSupportedException')  
The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') is read-only.    
 -or-    
 The [System.Collections.IList](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IList 'System.Collections.IList') has a fixed size.
### Events

<a name='Tizen.UI.Components.Recycler.GroupItemSource.CollectionChanged'></a>

## GroupItemSource.CollectionChanged Event

Event when collection changed.

```csharp
public event NotifyCollectionChangedEventHandler CollectionChanged;
```

Implements [CollectionChanged](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged 'System.Collections.Specialized.INotifyCollectionChanged.CollectionChanged')

#### Event Type
[System.Collections.Specialized.NotifyCollectionChangedEventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Specialized.NotifyCollectionChangedEventHandler 'System.Collections.Specialized.NotifyCollectionChangedEventHandler')


























































