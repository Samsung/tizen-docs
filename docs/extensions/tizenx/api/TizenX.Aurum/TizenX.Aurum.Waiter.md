### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## Waiter Class

Provides functionality to wait for specific UI conditions to be met.
This class monitors UI elements and waits for them to appear, disappear, or change state.

```csharp
public class Waiter : IDisposable
```

### Constructors

<a name='TizenX.Aurum.Waiter..ctor.TizenX.Aurum.Searchable.'></a>

## Waiter(Searchable)

```csharp
public Waiter(Searchable searchableObject)
```
#### Parameters

`searchableObject` Searchable

<a name='TizenX.Aurum.Waiter..ctor.TizenX.Aurum.Searchable.TizenX.Aurum.UIObject.'></a>

## Waiter(Searchable, UIObject)

```csharp
public Waiter(Searchable searchableObject, UIObject uiObject)
```
#### Parameters

`searchableObject` Searchable

`uiObject` UIObject

<a name='TizenX.Aurum.Waiter..ctor.TizenX.Aurum.Searchable.TizenX.Aurum.UIObject.System.Int32.'></a>

## Waiter(Searchable, UIObject, int)

Initializes a new Waiter instance to wait for a searchable object to match a UI object.

```csharp
public Waiter(Searchable searchableObject, UIObject uiObject, int timeout)
```
#### Parameters

`searchableObject` Searchable

The searchable object containing the search criteria.

`uiObject` UIObject

The UI object to wait for.

`timeout` int

Maximum time to wait in milliseconds.

### Fields

<a name='TizenX.Aurum.Waiter.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.Waiter.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.Waiter.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.Waiter.Finalize'></a>

## ~Waiter()

```csharp
protected ~Waiter()
```
