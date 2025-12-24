### [Tizen.UI.Components.Material](Tizen.UI.Components.Material.md 'Tizen.UI.Components.Material')

## PageScroller Class

A Page scroller component.

```csharp
public class PageScroller : Tizen.UI.ContentView,
Tizen.UI.Components.Material.IPager,
System.Collections.Generic.IList&lt;Tizen.UI.View>,
System.Collections.Generic.ICollection&lt;Tizen.UI.View>,
System.Collections.Generic.IEnumerable&lt;Tizen.UI.View>,
System.Collections.IEnumerable
```

Inheritance [System.Object](https://docs.microsoft.com/en-us/dotnet/api/System.Object 'System.Object') &#129106; [Tizen.UI.NObject](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.NObject 'Tizen.UI.NObject') &#129106; [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View') &#129106; [Tizen.UI.ContentView](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.ContentView 'Tizen.UI.ContentView') &#129106; PageScroller

Implements [IPager](Tizen.UI.Components.Material.IPager.md 'Tizen.UI.Components.Material.IPager'), [System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1'), [System.Collections.Generic.ICollection&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1 'System.Collections.Generic.ICollection`1'), [System.Collections.Generic.IEnumerable&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1 'System.Collections.Generic.IEnumerable`1'), [System.Collections.IEnumerable](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable 'System.Collections.IEnumerable')
### Constructors

<a name='Tizen.UI.Components.Material.PageScroller.PageScroller()'></a>

## PageScroller() Constructor

Constructs a Page Scroller.

```csharp
public PageScroller();
```
### Properties

<a name='Tizen.UI.Components.Material.PageScroller.Children'></a>

## PageScroller.Children Property

Children of the page scroller.

```csharp
public System.Collections.Generic.IList&lt;Tizen.UI.View> Children { get; }
```

#### Property Value
[System.Collections.Generic.IList&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1 'System.Collections.Generic.IList`1')

<a name='Tizen.UI.Components.Material.PageScroller.CurrentPage'></a>

## PageScroller.CurrentPage Property

Gets sets the current page.

```csharp
public int CurrentPage { get; }
```

Implements [CurrentPage](Tizen.UI.Components.Material.IPager.md#Tizen.UI.Components.Material.IPager.CurrentPage 'Tizen.UI.Components.Material.IPager.CurrentPage')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageScroller.IsHorizontal'></a>

## PageScroller.IsHorizontal Property

Gets or sets the direction of page scroller is horizontal or not.

```csharp
public bool IsHorizontal { get; set; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.PageScroller.IsScrolling'></a>

## PageScroller.IsScrolling Property

Gets a value indicating whether the scroll is currently in progress.

```csharp
public bool IsScrolling { get; }
```

#### Property Value
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.PageScroller.Padding'></a>

## PageScroller.Padding Property

Gets or sets the padding on PageScroller.

```csharp
public Tizen.UI.Thickness Padding { get; set; }
```

#### Property Value
[Tizen.UI.Thickness](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Thickness 'Tizen.UI.Thickness')

<a name='Tizen.UI.Components.Material.PageScroller.PageAdapter'></a>

## PageScroller.PageAdapter Property

Adapter who connects pager and indicator.

```csharp
public Tizen.UI.Components.Material.PageAdapter PageAdapter { get; set; }
```

Implements [PageAdapter](Tizen.UI.Components.Material.IPager.md#Tizen.UI.Components.Material.IPager.PageAdapter 'Tizen.UI.Components.Material.IPager.PageAdapter')

#### Property Value
[PageAdapter](Tizen.UI.Components.Material.PageAdapter.md 'Tizen.UI.Components.Material.PageAdapter')

<a name='Tizen.UI.Components.Material.PageScroller.PageCount'></a>

## PageScroller.PageCount Property

Gets sets the page count.

```csharp
public int PageCount { get; }
```

Implements [PageCount](Tizen.UI.Components.Material.IPager.md#Tizen.UI.Components.Material.IPager.PageCount 'Tizen.UI.Components.Material.IPager.PageCount')

#### Property Value
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageScroller.SnapPointsAlignment'></a>

## PageScroller.SnapPointsAlignment Property

Page alignment of scroll. default is Center.  
[SnapPointsAlignment](Tizen.UI.Components.Material.PageScroller.md#Tizen.UI.Components.Material.PageScroller.SnapPointsAlignment 'Tizen.UI.Components.Material.PageScroller.SnapPointsAlignment').

```csharp
public Tizen.UI.Layouts.SnapPointsAlignment SnapPointsAlignment { get; set; }
```

#### Property Value
[Tizen.UI.Layouts.SnapPointsAlignment](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.SnapPointsAlignment 'Tizen.UI.Layouts.SnapPointsAlignment')

<a name='Tizen.UI.Components.Material.PageScroller.SnapPointType'></a>

## PageScroller.SnapPointType Property

Specifies the behavior of snap points when scrolling.  
default is MandatorySingle

```csharp
public Tizen.UI.Layouts.SnapPointsType SnapPointType { get; set; }
```

#### Property Value
[Tizen.UI.Layouts.SnapPointsType](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.Layouts.SnapPointsType 'Tizen.UI.Layouts.SnapPointsType')

<a name='Tizen.UI.Components.Material.PageScroller.Spacing'></a>

## PageScroller.Spacing Property

Gets or sets the spacing between pages.

```csharp
public float Spacing { get; set; }
```

#### Property Value
[System.Single](https://docs.microsoft.com/en-us/dotnet/api/System.Single 'System.Single')

<a name='Tizen.UI.Components.Material.PageScroller.this[int]'></a>

## PageScroller.this[int] Property

Gets a content view with index.

```csharp
public Tizen.UI.View this[int index] { get; set; }
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.this[int].index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [this[int]](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.Item#System_Collections_Generic_IList_1_Item_System_Int32_ 'System.Collections.Generic.IList`1.Item(System.Int32)'), [this[int]](Tizen.UI.Components.Material.IPager.md#Tizen.UI.Components.Material.IPager.this[int] 'Tizen.UI.Components.Material.IPager.this[int]')

#### Property Value
[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')
### Methods

<a name='Tizen.UI.Components.Material.PageScroller.Clear()'></a>

## PageScroller.Clear() Method

Clears all children.

```csharp
public void Clear();
```

Implements [Clear()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Clear 'System.Collections.Generic.ICollection`1.Clear')

<a name='Tizen.UI.Components.Material.PageScroller.Contains(Tizen.UI.View)'></a>

## PageScroller.Contains(View) Method

Whether it contains the specified child.

```csharp
public bool Contains(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.Contains(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

#### Returns
[System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

<a name='Tizen.UI.Components.Material.PageScroller.CopyTo(Tizen.UI.View[],int)'></a>

## PageScroller.CopyTo(View[], int) Method

Copies the children to an array.

```csharp
public void CopyTo(Tizen.UI.View[] array, int arrayIndex);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.CopyTo(Tizen.UI.View[],int).array'></a>

`array` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[[]](https://docs.microsoft.com/en-us/dotnet/api/System.Array 'System.Array')

<a name='Tizen.UI.Components.Material.PageScroller.CopyTo(Tizen.UI.View[],int).arrayIndex'></a>

`arrayIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageScroller.GetEnumerator()'></a>

## PageScroller.GetEnumerator() Method

Returns an enumerator that iterates through the collection.

```csharp
public System.Collections.Generic.IEnumerator&lt;Tizen.UI.View> GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerable-1.GetEnumerator 'System.Collections.Generic.IEnumerable`1.GetEnumerator'), [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')

#### Returns
[System.Collections.Generic.IEnumerator&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')[Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IEnumerator-1 'System.Collections.Generic.IEnumerator`1')  
An enumerator that can be used to iterate through the collection.

<a name='Tizen.UI.Components.Material.PageScroller.IndexOf(Tizen.UI.View)'></a>

## PageScroller.IndexOf(View) Method

Gets the index of the specified child.

```csharp
public int IndexOf(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.IndexOf(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

#### Returns
[System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageScroller.Insert(int,Tizen.UI.View)'></a>

## PageScroller.Insert(int, View) Method

(Not implemented) Inserts the specified content at the specified index.

```csharp
public void Insert(int index, Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.Insert(int,Tizen.UI.View).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

<a name='Tizen.UI.Components.Material.PageScroller.Insert(int,Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

<a name='Tizen.UI.Components.Material.PageScroller.Remove(Tizen.UI.View)'></a>

## PageScroller.Remove(View) Method

Removes the specified view from its parent.

```csharp
public void Remove(Tizen.UI.View child);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.Remove(Tizen.UI.View).child'></a>

`child` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

Implements [Remove(View)](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.IParentObject.Remove#Tizen_UI_IParentObject_Remove_Tizen_UI_View_ 'Tizen.UI.IParentObject.Remove(Tizen.UI.View)')

<a name='Tizen.UI.Components.Material.PageScroller.RemoveAt(int)'></a>

## PageScroller.RemoveAt(int) Method

Removes the content at the specified index.

```csharp
public void RemoveAt(int index);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.RemoveAt(int).index'></a>

`index` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

Implements [RemoveAt(int)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.IList-1.RemoveAt#System_Collections_Generic_IList_1_RemoveAt_System_Int32_ 'System.Collections.Generic.IList`1.RemoveAt(System.Int32)')

<a name='Tizen.UI.Components.Material.PageScroller.ShowPage(int,bool)'></a>

## PageScroller.ShowPage(int, bool) Method

Show page in pager.

```csharp
public System.Threading.Tasks.Task ShowPage(int pageIndex, bool animation);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.ShowPage(int,bool).pageIndex'></a>

`pageIndex` [System.Int32](https://docs.microsoft.com/en-us/dotnet/api/System.Int32 'System.Int32')

The page index to be shown.

<a name='Tizen.UI.Components.Material.PageScroller.ShowPage(int,bool).animation'></a>

`animation` [System.Boolean](https://docs.microsoft.com/en-us/dotnet/api/System.Boolean 'System.Boolean')

Whether to play an animation.

Implements [ShowPage(int, bool)](Tizen.UI.Components.Material.IPager.md#Tizen.UI.Components.Material.IPager.ShowPage(int,bool) 'Tizen.UI.Components.Material.IPager.ShowPage(int, bool)')

#### Returns
[System.Threading.Tasks.Task](https://docs.microsoft.com/en-us/dotnet/api/System.Threading.Tasks.Task 'System.Threading.Tasks.Task')  
the visual object.
### Events

<a name='Tizen.UI.Components.Material.PageScroller.DragFinished'></a>

## PageScroller.DragFinished Event

Occurs when the page drag finishes.

```csharp
public event EventHandler DragFinished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.PageScroller.Dragging'></a>

## PageScroller.Dragging Event

Occurs while page dragging.

```csharp
public event EventHandler&lt;DragEventArgs> Dragging;
```

#### Event Type
[System.EventHandler&lt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')[Tizen.UI.DragEventArgs](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.DragEventArgs 'Tizen.UI.DragEventArgs')[&gt;](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler-1 'System.EventHandler`1')

<a name='Tizen.UI.Components.Material.PageScroller.DragStarted'></a>

## PageScroller.DragStarted Event

Occurs when the page drag starts.

```csharp
public event EventHandler DragStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.PageScroller.ScrollFinished'></a>

## PageScroller.ScrollFinished Event

Occurs when the page scroll finishes.

```csharp
public event EventHandler ScrollFinished;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.PageScroller.Scrolling'></a>

## PageScroller.Scrolling Event

Occurs while page scrolling.

```csharp
public event EventHandler Scrolling;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')

<a name='Tizen.UI.Components.Material.PageScroller.ScrollStarted'></a>

## PageScroller.ScrollStarted Event

Occurs when the page scroll starts.

```csharp
public event EventHandler ScrollStarted;
```

#### Event Type
[System.EventHandler](https://docs.microsoft.com/en-us/dotnet/api/System.EventHandler 'System.EventHandler')
### Explicit Interface Implementations

<a name='Tizen.UI.Components.Material.PageScroller.System.Collections.Generic.ICollection_Tizen.UI.View_.Add(Tizen.UI.View)'></a>

## PageScroller.System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Add(View) Method

Adds a child view.

```csharp
void System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Add(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.System.Collections.Generic.ICollection_Tizen.UI.View_.Add(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

Implements [Add(View)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Add#System_Collections_Generic_ICollection_1_Add__0_ 'System.Collections.Generic.ICollection`1.Add(`0)')

<a name='Tizen.UI.Components.Material.PageScroller.System.Collections.Generic.ICollection_Tizen.UI.View_.Remove(Tizen.UI.View)'></a>

## PageScroller.System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Remove(View) Method

Removes the specified content from the page scroller.

```csharp
bool System.Collections.Generic.ICollection&lt;Tizen.UI.View>.Remove(Tizen.UI.View item);
```
#### Parameters

<a name='Tizen.UI.Components.Material.PageScroller.System.Collections.Generic.ICollection_Tizen.UI.View_.Remove(Tizen.UI.View).item'></a>

`item` [Tizen.UI.View](https://docs.microsoft.com/en-us/dotnet/api/Tizen.UI.View 'Tizen.UI.View')

Implements [Remove(View)](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.Generic.ICollection-1.Remove#System_Collections_Generic_ICollection_1_Remove__0_ 'System.Collections.Generic.ICollection`1.Remove(`0)')

<a name='Tizen.UI.Components.Material.PageScroller.System.Collections.IEnumerable.GetEnumerator()'></a>

## PageScroller.System.Collections.IEnumerable.GetEnumerator() Method

Returns an enumerator that iterates through a collection.

```csharp
System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator();
```

Implements [GetEnumerator()](https://docs.microsoft.com/en-us/dotnet/api/System.Collections.IEnumerable.GetEnumerator 'System.Collections.IEnumerable.GetEnumerator')













































