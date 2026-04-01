### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UIObjectVector.UIObjectVectorEnumerator Class

```csharp
public sealed class UIObjectVector.UIObjectVectorEnumerator : IEnumerator<UIObject>, IEnumerator, IDisposable
```

### Constructors

<a name='TizenX.Aurum.UIObjectVector.UIObjectVectorEnumerator..ctor.TizenX.Aurum.UIObjectVector.'></a>

## UIObjectVectorEnumerator(UIObjectVector)

```csharp
public UIObjectVectorEnumerator(UIObjectVector collection)
```
#### Parameters

`collection` UIObjectVector

### Properties

<a name='TizenX.Aurum.UIObjectVector.UIObjectVectorEnumerator.Current'></a>

## Current

Gets the element in the collection at the current position of the enumerator.

```csharp
public UIObject Current { get; }
```
#### Property Value

UIObject

The element in the collection at the current position of the enumerator.

### Methods

<a name='TizenX.Aurum.UIObjectVector.UIObjectVectorEnumerator.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.UIObjectVector.UIObjectVectorEnumerator.MoveNext'></a>

## MoveNext()

Advances the enumerator to the next element of the collection.

```csharp
public bool MoveNext()
```
#### Returns

bool

true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.

<a name='TizenX.Aurum.UIObjectVector.UIObjectVectorEnumerator.Reset'></a>

## Reset()

Sets the enumerator to its initial position, which is before the first element in the collection.

```csharp
public void Reset()
```
