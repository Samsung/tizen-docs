### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## NodeVector.NodeVectorEnumerator Class

```csharp
public sealed class NodeVector.NodeVectorEnumerator : IEnumerator<Node>, IEnumerator, IDisposable
```

### Constructors

<a name='TizenX.Aurum.NodeVector.NodeVectorEnumerator..ctor.TizenX.Aurum.NodeVector.'></a>

## NodeVectorEnumerator(NodeVector)

```csharp
public NodeVectorEnumerator(NodeVector collection)
```
#### Parameters

`collection` NodeVector

### Properties

<a name='TizenX.Aurum.NodeVector.NodeVectorEnumerator.Current'></a>

## Current

Gets the element in the collection at the current position of the enumerator.

```csharp
public Node Current { get; }
```
#### Property Value

Node

The element in the collection at the current position of the enumerator.

### Methods

<a name='TizenX.Aurum.NodeVector.NodeVectorEnumerator.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.NodeVector.NodeVectorEnumerator.MoveNext'></a>

## MoveNext()

Advances the enumerator to the next element of the collection.

```csharp
public bool MoveNext()
```
#### Returns

bool

true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.

<a name='TizenX.Aurum.NodeVector.NodeVectorEnumerator.Reset'></a>

## Reset()

Sets the enumerator to its initial position, which is before the first element in the collection.

```csharp
public void Reset()
```
