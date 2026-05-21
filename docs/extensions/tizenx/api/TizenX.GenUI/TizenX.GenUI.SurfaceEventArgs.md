### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## SurfaceEventArgs Class

Provides data for surface lifecycle events such as BeginRendering and DeleteSurface.
Contains information about the surface being rendered or deleted.

```csharp
public class SurfaceEventArgs : EventArgs
```

### Properties

<a name='TizenX.GenUI.SurfaceEventArgs.SurfaceId'></a>

## SurfaceId

Gets or sets the unique identifier of the surface associated with this event.

```csharp
public string SurfaceId { get; set; }
```
#### Property Value

string

A string representing the surface ID.
This ID is used to identify and manage the surface in the SurfaceManager.

<a name='TizenX.GenUI.SurfaceEventArgs.SurfaceRoot'></a>

## SurfaceRoot

Gets or sets the root view of the surface.

```csharp
public View SurfaceRoot { get; set; }
```
#### Property Value

View

The root View of the surface, or null if no root view is available.
For BeginRendering events, this is the view to add to your layout.
For DeleteSurface events, this is the view to remove from your layout.

