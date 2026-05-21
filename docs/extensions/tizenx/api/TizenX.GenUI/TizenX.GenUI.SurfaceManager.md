### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## SurfaceManager Class

Manages the creation, retrieval, and lifecycle of multiple surface contexts.
Acts as a central registry for all surfaces and forwards events from individual surfaces.

```csharp
public class SurfaceManager
```

### Methods

<a name='TizenX.GenUI.SurfaceManager.DetachSurface.TizenX.GenUI.SurfaceContext.'></a>

## DetachSurface(SurfaceContext)

Removes a surface context from the manager without clearing its data bindings.
Use this method when you want to detach a surface but preserve its data bindings.

```csharp
public void DetachSurface(SurfaceContext context)
```
#### Parameters

`context` SurfaceContext

The surface context to detach.

<a name='TizenX.GenUI.SurfaceManager.GetContext.System.String.'></a>

## GetContext(string)

Gets or creates a surface context for the specified surface ID.
If a context with the given ID already exists, it is returned; otherwise, a new context is created.

```csharp
public SurfaceContext GetContext(string surfaceId)
```
#### Parameters

`surfaceId` string

The unique identifier for the surface.
If null or empty, "default" is used as the surface ID.

#### Returns

SurfaceContext

The SurfaceContext for the specified surface.

<a name='TizenX.GenUI.SurfaceManager.RemoveSurface.TizenX.GenUI.SurfaceContext.'></a>

## RemoveSurface(SurfaceContext)

Removes a surface context from the manager and clears all its data bindings.
Use this method to properly clean up a surface that is no longer needed.

```csharp
public void RemoveSurface(SurfaceContext context)
```
#### Parameters

`context` SurfaceContext

The surface context to remove.

### Events

<a name='TizenX.GenUI.SurfaceManager.BeginRendering'></a>

## BeginRendering

Occurs when any surface begins rendering.
This event aggregates BeginRendering events from all managed surfaces.

```csharp
public event EventHandler<SurfaceEventArgs> BeginRendering
```
<a name='TizenX.GenUI.SurfaceManager.DeleteSurface'></a>

## DeleteSurface

Occurs when any surface is deleted.
This event aggregates DeleteSurface events from all managed surfaces.

```csharp
public event EventHandler<SurfaceEventArgs> DeleteSurface
```
<a name='TizenX.GenUI.SurfaceManager.UserAction'></a>

## UserAction

Occurs when a user action is triggered in any surface.
This event aggregates UserAction events from all managed surfaces.

```csharp
public event EventHandler<UserActionEventArgs> UserAction
```
