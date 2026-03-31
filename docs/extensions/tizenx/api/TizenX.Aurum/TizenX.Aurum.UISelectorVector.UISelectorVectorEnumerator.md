### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## UISelectorVector.UISelectorVectorEnumerator Class

```csharp
public sealed class UISelectorVector.UISelectorVectorEnumerator : IEnumerator<UISelector>, IEnumerator, IDisposable
```

### Constructors

<a name='TizenX.Aurum.UISelectorVector.UISelectorVectorEnumerator..ctor.TizenX.Aurum.UISelectorVector.'></a>

## UISelectorVectorEnumerator(UISelectorVector)

```csharp
public UISelectorVectorEnumerator(UISelectorVector collection)
```
#### Parameters

`collection` UISelectorVector

### Properties

<a name='TizenX.Aurum.UISelectorVector.UISelectorVectorEnumerator.Current'></a>

## Current

Gets the element in the collection at the current position of the enumerator.

```csharp
public UISelector Current { get; }
```
#### Property Value

UISelector

The element in the collection at the current position of the enumerator.

### Methods

<a name='TizenX.Aurum.UISelectorVector.UISelectorVectorEnumerator.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.UISelectorVector.UISelectorVectorEnumerator.MoveNext'></a>

## MoveNext()

Advances the enumerator to the next element of the collection.

```csharp
public bool MoveNext()
```
#### Returns

bool

true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.

<a name='TizenX.Aurum.UISelectorVector.UISelectorVectorEnumerator.Reset'></a>

## Reset()

Sets the enumerator to its initial position, which is before the first element in the collection.

```csharp
public void Reset()
```
