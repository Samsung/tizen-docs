### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## NodeVector Class

```csharp
public class NodeVector : IDisposable, IEnumerable<Node>, IEnumerable
```

### Constructors

<a name='TizenX.Aurum.NodeVector..ctor'></a>

## NodeVector()

```csharp
public NodeVector()
```
<a name='TizenX.Aurum.NodeVector..ctor.System.Collections.Generic.IEnumerable.TizenX.Aurum.Node..'></a>

## NodeVector(IEnumerable<Node>)

```csharp
public NodeVector(IEnumerable<Node> c)
```
#### Parameters

`c` IEnumerable<Node>

<a name='TizenX.Aurum.NodeVector..ctor.System.Collections.IEnumerable.'></a>

## NodeVector(IEnumerable)

```csharp
public NodeVector(IEnumerable c)
```
#### Parameters

`c` IEnumerable

<a name='TizenX.Aurum.NodeVector..ctor.System.Int32.'></a>

## NodeVector(int)

```csharp
public NodeVector(int capacity)
```
#### Parameters

`capacity` int

<a name='TizenX.Aurum.NodeVector..ctor.TizenX.Aurum.NodeVector.'></a>

## NodeVector(NodeVector)

```csharp
public NodeVector(NodeVector other)
```
#### Parameters

`other` NodeVector

### Properties

<a name='TizenX.Aurum.NodeVector.Capacity'></a>

## Capacity

```csharp
public int Capacity { get; set; }
```
#### Property Value

int

<a name='TizenX.Aurum.NodeVector.Count'></a>

## Count

```csharp
public int Count { get; }
```
#### Property Value

int

<a name='TizenX.Aurum.NodeVector.IsFixedSize'></a>

## IsFixedSize

```csharp
public bool IsFixedSize { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.NodeVector.IsReadOnly'></a>

## IsReadOnly

```csharp
public bool IsReadOnly { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.NodeVector.IsSynchronized'></a>

## IsSynchronized

```csharp
public bool IsSynchronized { get; }
```
#### Property Value

bool

<a name='TizenX.Aurum.NodeVector.Item.System.Int32.'></a>

## this[int]

```csharp
public Node this[int index] { get; set; }
```
#### Parameters

`index` int

#### Property Value

Node

### Fields

<a name='TizenX.Aurum.NodeVector.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.NodeVector.Add.TizenX.Aurum.Node.'></a>

## Add(Node)

```csharp
public void Add(Node x)
```
#### Parameters

`x` Node

<a name='TizenX.Aurum.NodeVector.AddRange.TizenX.Aurum.NodeVector.'></a>

## AddRange(NodeVector)

```csharp
public void AddRange(NodeVector values)
```
#### Parameters

`values` NodeVector

<a name='TizenX.Aurum.NodeVector.Clear'></a>

## Clear()

```csharp
public void Clear()
```
<a name='TizenX.Aurum.NodeVector.CopyTo.System.Int32.TizenX.Aurum.Node...System.Int32.System.Int32.'></a>

## CopyTo(int, Node[], int, int)

```csharp
public void CopyTo(int index, Node[] array, int arrayIndex, int count)
```
#### Parameters

`index` int

`array` Node[]

`arrayIndex` int

`count` int

<a name='TizenX.Aurum.NodeVector.CopyTo.TizenX.Aurum.Node...'></a>

## CopyTo(Node[])

```csharp
public void CopyTo(Node[] array)
```
#### Parameters

`array` Node[]

<a name='TizenX.Aurum.NodeVector.CopyTo.TizenX.Aurum.Node...System.Int32.'></a>

## CopyTo(Node[], int)

```csharp
public void CopyTo(Node[] array, int arrayIndex)
```
#### Parameters

`array` Node[]

`arrayIndex` int

<a name='TizenX.Aurum.NodeVector.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.NodeVector.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.NodeVector.Finalize'></a>

## ~NodeVector()

```csharp
protected ~NodeVector()
```
<a name='TizenX.Aurum.NodeVector.GetEnumerator'></a>

## GetEnumerator()

```csharp
public NodeVector.NodeVectorEnumerator GetEnumerator()
```
#### Returns

NodeVector.NodeVectorEnumerator

<a name='TizenX.Aurum.NodeVector.GetRange.System.Int32.System.Int32.'></a>

## GetRange(int, int)

```csharp
public NodeVector GetRange(int index, int count)
```
#### Parameters

`index` int

`count` int

#### Returns

NodeVector

<a name='TizenX.Aurum.NodeVector.Insert.System.Int32.TizenX.Aurum.Node.'></a>

## Insert(int, Node)

```csharp
public void Insert(int index, Node x)
```
#### Parameters

`index` int

`x` Node

<a name='TizenX.Aurum.NodeVector.InsertRange.System.Int32.TizenX.Aurum.NodeVector.'></a>

## InsertRange(int, NodeVector)

```csharp
public void InsertRange(int index, NodeVector values)
```
#### Parameters

`index` int

`values` NodeVector

<a name='TizenX.Aurum.NodeVector.RemoveAt.System.Int32.'></a>

## RemoveAt(int)

```csharp
public void RemoveAt(int index)
```
#### Parameters

`index` int

<a name='TizenX.Aurum.NodeVector.RemoveRange.System.Int32.System.Int32.'></a>

## RemoveRange(int, int)

```csharp
public void RemoveRange(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.NodeVector.Repeat.TizenX.Aurum.Node.System.Int32.'></a>

## Repeat(Node, int)

```csharp
public static NodeVector Repeat(Node value, int count)
```
#### Parameters

`value` Node

`count` int

#### Returns

NodeVector

<a name='TizenX.Aurum.NodeVector.Reverse'></a>

## Reverse()

```csharp
public void Reverse()
```
<a name='TizenX.Aurum.NodeVector.Reverse.System.Int32.System.Int32.'></a>

## Reverse(int, int)

```csharp
public void Reverse(int index, int count)
```
#### Parameters

`index` int

`count` int

<a name='TizenX.Aurum.NodeVector.SetRange.System.Int32.TizenX.Aurum.NodeVector.'></a>

## SetRange(int, NodeVector)

```csharp
public void SetRange(int index, NodeVector values)
```
#### Parameters

`index` int

`values` NodeVector

<a name='TizenX.Aurum.NodeVector.ToArray'></a>

## ToArray()

```csharp
public Node[] ToArray()
```
#### Returns

Node[]

