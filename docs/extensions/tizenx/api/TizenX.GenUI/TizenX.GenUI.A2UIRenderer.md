### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## A2UIRenderer Class

Main renderer class that processes JSON-based UI definitions and creates Tizen.UI views.
This class manages surface rendering, component catalogs, and user action handling.

```csharp
public class A2UIRenderer
```

### Constructors

<a name='TizenX.GenUI.A2UIRenderer..ctor'></a>

## A2UIRenderer()

Initializes a new instance of the A2UIRenderer class.
Sets up event handlers and registers standard catalog components.

```csharp
public A2UIRenderer()
```
### Properties

<a name='TizenX.GenUI.A2UIRenderer.SurfaceManager'></a>

## SurfaceManager

Gets the surface manager instance used by this renderer.

```csharp
public SurfaceManager SurfaceManager { get; }
```
#### Property Value

SurfaceManager

### Methods

<a name='TizenX.GenUI.A2UIRenderer.GetCustomCatalogSchema'></a>

## GetCustomCatalogSchema()

Generates a JSON schema string for all custom catalog components.
This can be used for documentation or validation purposes.

```csharp
public string GetCustomCatalogSchema()
```
#### Returns

string

A JSON string containing the schema definitions for custom components.

<a name='TizenX.GenUI.A2UIRenderer.JsonFeed.System.String.'></a>

## JsonFeed(string)

Processes a JSON string containing A2UI messages.
The JSON can be either a single object or an array of objects.

```csharp
public void JsonFeed(string json)
```
#### Parameters

`json` string

A JSON string containing A2UI message(s).

<a name='TizenX.GenUI.A2UIRenderer.JsonFeed.System.Text.Json.Nodes.JsonObject.'></a>

## JsonFeed(JsonObject)

Processes a JsonObject containing a single A2UI message.

```csharp
public void JsonFeed(JsonObject json)
```
#### Parameters

`json` JsonObject

A JsonObject containing an A2UI message.

<a name='TizenX.GenUI.A2UIRenderer.RenderJson.System.String.'></a>

## RenderJson(string)

Renders a JSON string and returns the surface context.
This method is useful for testing or when you need direct access to the rendered context.

```csharp
public SurfaceContext RenderJson(string json)
```
#### Parameters

`json` string

A JSON string containing A2UI message(s).

#### Returns

SurfaceContext

The SurfaceContext for the first rendered surface, or null if no surface was rendered.

<a name='TizenX.GenUI.A2UIRenderer.RenderJson.System.Text.Json.Nodes.JsonArray.'></a>

## RenderJson(JsonArray)

Renders a JsonArray and returns the surface context.
Processes each object in the array sequentially.

```csharp
public SurfaceContext RenderJson(JsonArray jsonArray)
```
#### Parameters

`jsonArray` JsonArray

A JsonArray containing A2UI message(s).

#### Returns

SurfaceContext

The SurfaceContext for the first rendered surface, or null if no surface was rendered.

<a name='TizenX.GenUI.A2UIRenderer.RenderJson.System.Text.Json.Nodes.JsonObject.'></a>

## RenderJson(JsonObject)

Renders a JsonObject and returns the surface context.
This method is useful for testing or when you need direct access to the rendered context.

```csharp
public SurfaceContext RenderJson(JsonObject json)
```
#### Parameters

`json` JsonObject

A JsonObject containing A2UI message(s).

#### Returns

SurfaceContext

The SurfaceContext for the rendered surface, or null if rendering failed.

<a name='TizenX.GenUI.A2UIRenderer.UpdateCatalog.System.Collections.Generic.IEnumerable.TizenX.GenUI.CatalogItem..'></a>

## UpdateCatalog(IEnumerable<CatalogItem>)

Updates the component catalog with custom catalog items.
Use this method to register custom components for rendering.

```csharp
public void UpdateCatalog(IEnumerable<CatalogItem> catalogItems)
```
#### Parameters

`catalogItems` IEnumerable<CatalogItem>

An enumerable collection of catalog items to add or update.

### Events

<a name='TizenX.GenUI.A2UIRenderer.BeginRenderingSurface'></a>

## BeginRenderingSurface

Occurs when a surface begins rendering and its root view is ready.
Subscribe to this event to add the rendered view to your layout.

```csharp
public event EventHandler<SurfaceEventArgs> BeginRenderingSurface
```
<a name='TizenX.GenUI.A2UIRenderer.DeleteSurface'></a>

## DeleteSurface

Occurs when a surface is deleted.
Subscribe to this event to remove the surface view from your layout.

```csharp
public event EventHandler<SurfaceEventArgs> DeleteSurface
```
<a name='TizenX.GenUI.A2UIRenderer.UserAction'></a>

## UserAction

Occurs when a user action is triggered (e.g., button click).
The event args contain a JsonObject with action details including name, source component ID, and context.

```csharp
public event EventHandler<UserActionEventArgs> UserAction
```
