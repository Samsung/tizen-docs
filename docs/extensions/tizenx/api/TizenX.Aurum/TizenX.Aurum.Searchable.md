### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## Searchable Class

```csharp
public class Searchable : IDisposable
```

### Fields

<a name='TizenX.Aurum.Searchable.swigCMemOwn'></a>

## swigCMemOwn

```csharp
protected bool swigCMemOwn
```
#### Field Value

bool

### Methods

<a name='TizenX.Aurum.Searchable.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.Searchable.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.Searchable.Finalize'></a>

## ~Searchable()

```csharp
protected ~Searchable()
```
<a name='TizenX.Aurum.Searchable.FindObject.TizenX.Aurum.UISelector.'></a>

## FindObject(UISelector)

```csharp
public virtual UIObject FindObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObject

<a name='TizenX.Aurum.Searchable.FindObjects.TizenX.Aurum.UISelector.'></a>

## FindObjects(UISelector)

```csharp
public virtual UIObjectVector FindObjects(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

UIObjectVector

<a name='TizenX.Aurum.Searchable.GetMatches.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatches(UISelector, bool)

```csharp
public virtual UIObjectVector GetMatches(UISelector selector, bool earlyReturn)
```
#### Parameters

`selector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.Searchable.GetMatchesInMatches.TizenX.Aurum.UISelector.TizenX.Aurum.UISelector.System.Boolean.'></a>

## GetMatchesInMatches(UISelector, UISelector, bool)

```csharp
public virtual UIObjectVector GetMatchesInMatches(UISelector firstSelector, UISelector secondSelector, bool earlyReturn)
```
#### Parameters

`firstSelector` UISelector

`secondSelector` UISelector

`earlyReturn` bool

#### Returns

UIObjectVector

<a name='TizenX.Aurum.Searchable.HasObject.TizenX.Aurum.UISelector.'></a>

## HasObject(UISelector)

```csharp
public virtual bool HasObject(UISelector selector)
```
#### Parameters

`selector` UISelector

#### Returns

bool

