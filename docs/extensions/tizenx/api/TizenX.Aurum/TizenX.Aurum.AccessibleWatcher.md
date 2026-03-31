### [TizenX.Aurum](TizenX.Aurum.md 'TizenX.Aurum')

## AccessibleWatcher Class

Monitors accessibility events and provides notifications when UI elements change.
This class implements the singleton pattern to ensure only one instance exists.

```csharp
public class AccessibleWatcher : IDisposable
```

### Properties

<a name='TizenX.Aurum.AccessibleWatcher.Instance'></a>

## Instance

Gets the singleton instance of AccessibleWatcher.

```csharp
public static AccessibleWatcher Instance { get; }
```
#### Property Value

AccessibleWatcher

### Methods

<a name='TizenX.Aurum.AccessibleWatcher.Dispose'></a>

## Dispose()

Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.

```csharp
public void Dispose()
```
<a name='TizenX.Aurum.AccessibleWatcher.Dispose.System.Boolean.'></a>

## Dispose(bool)

```csharp
protected virtual void Dispose(bool disposing)
```
#### Parameters

`disposing` bool

<a name='TizenX.Aurum.AccessibleWatcher.Finalize'></a>

## ~AccessibleWatcher()

```csharp
protected ~AccessibleWatcher()
```
<a name='TizenX.Aurum.AccessibleWatcher.SetXMLsync.System.Boolean.'></a>

## SetXMLsync(bool)

Sets the XML synchronization mode for the accessible watcher.

```csharp
public void SetXMLsync(bool sync)
```
#### Parameters

`sync` bool

True to enable XML synchronization, false to disable.

