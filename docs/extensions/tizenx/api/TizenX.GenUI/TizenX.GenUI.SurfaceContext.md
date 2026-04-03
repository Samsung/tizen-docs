### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## SurfaceContext Class

Represents the context for a single UI surface, managing its UI definition, data model, and lifecycle events.
Each surface has its own isolated context with separate component definitions and data bindings.

```csharp
public class SurfaceContext
```

### Constructors

<a name='TizenX.GenUI.SurfaceContext..ctor.System.String.'></a>

## SurfaceContext(string)

Initializes a new instance of the SurfaceContext class with the specified surface ID.

```csharp
public SurfaceContext(string id)
```
#### Parameters

`id` string

The unique identifier for this surface.

### Properties

<a name='TizenX.GenUI.SurfaceContext.DataContext'></a>

## DataContext

Gets the data context that manages data bindings between the data model and views.

```csharp
public DataContext DataContext { get; }
```
#### Property Value

DataContext

<a name='TizenX.GenUI.SurfaceContext.DataModel'></a>

## DataModel

Gets the data model that stores data values for data binding within this surface.

```csharp
public DataModel DataModel { get; }
```
#### Property Value

DataModel

<a name='TizenX.GenUI.SurfaceContext.Id'></a>

## Id

Gets the unique identifier for this surface.

```csharp
public string Id { get; }
```
#### Property Value

string

<a name='TizenX.GenUI.SurfaceContext.RootView'></a>

## RootView

Gets the root view of this surface after rendering has begun.
Returns null if rendering has not started or no root has been set.

```csharp
public View RootView { get; }
```
#### Property Value

View

<a name='TizenX.GenUI.SurfaceContext.UIDefinition'></a>

## UIDefinition

Gets the UI definition that manages component definitions and view instances for this surface.

```csharp
public UIDefinition UIDefinition { get; }
```
#### Property Value

UIDefinition

### Methods

<a name='TizenX.GenUI.SurfaceContext.Clear'></a>

## Clear()

Clears all data bindings and releases resources associated with this context.
Should be called when the surface is no longer needed.

```csharp
public void Clear()
```
<a name='TizenX.GenUI.SurfaceContext.SendBeginRendering.System.String.'></a>

## SendBeginRendering(string)

Initiates rendering of the surface with the specified root component.
If the root view is not yet available, the rendering will be deferred until the component is created.

```csharp
public void SendBeginRendering(string rootId)
```
#### Parameters

`rootId` string

The ID of the root component to render.

<a name='TizenX.GenUI.SurfaceContext.SendDeleteSurface'></a>

## SendDeleteSurface()

Notifies subscribers that this surface is being deleted.

```csharp
public void SendDeleteSurface()
```
<a name='TizenX.GenUI.SurfaceContext.SendPendingSurface'></a>

## SendPendingSurface()

Processes any pending surface rendering request.
Called when components become available after a deferred rendering request.

```csharp
public void SendPendingSurface()
```
<a name='TizenX.GenUI.SurfaceContext.SendUserAction.System.Text.Json.Nodes.JsonObject.'></a>

## SendUserAction(JsonObject)

Sends a user action message to subscribers of the UserAction event.

```csharp
public void SendUserAction(JsonObject message)
```
#### Parameters

`message` JsonObject

A JsonObject containing the user action details.

### Events

<a name='TizenX.GenUI.SurfaceContext.BeginRendering'></a>

## BeginRendering

Occurs when this surface begins rendering and its root view is ready.

```csharp
public event EventHandler<SurfaceEventArgs> BeginRendering
```
<a name='TizenX.GenUI.SurfaceContext.DeleteSurface'></a>

## DeleteSurface

Occurs when this surface is about to be deleted.

```csharp
public event EventHandler<SurfaceEventArgs> DeleteSurface
```
<a name='TizenX.GenUI.SurfaceContext.UserAction'></a>

## UserAction

Occurs when a user action is triggered within this surface.

```csharp
public event EventHandler<UserActionEventArgs> UserAction
```
