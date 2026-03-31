### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## Node Class

Represents a node in the UI hierarchy tree structure.
Each node contains a UIObject and its child nodes, forming a tree representation
of the UI layout. This class is useful for traversing and analyzing the UI hierarchy.

```csharp
public class Node : IDisposable
```

### Constructors

<a name='TizenX.Aurum.Node..ctor.TizenX.Aurum.UIObject.TizenX.Aurum.NodeVector.'></a>

## Node(UIObject, NodeVector)

```csharp
public Node(UIObject node, NodeVector children)
```
#### Parameters

`node` UIObject

`children` NodeVector

### Properties

<a name='TizenX.Aurum.Node.Children'></a>

## Children

```csharp
public NodeVector Children { get; set; }
```
#### Property Value

NodeVector

<a name='TizenX.Aurum.Node.UiObject'></a>

## UiObject

```csharp
public UIObject UiObject { get; set; }
```
#### Property Value

UIObject

### Methods

<a name='TizenX.Aurum.Node.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.Node.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.Node.Finalize'></a>

## ~Node()

```csharp
protected ~Node()
```
