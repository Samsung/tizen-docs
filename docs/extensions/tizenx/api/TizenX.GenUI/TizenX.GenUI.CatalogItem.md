### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## CatalogItem Class

Represents a component catalog item that defines how to create, update, and manage a UI component.
Catalog items are used to register custom components that can be rendered from JSON definitions.

```csharp
public class CatalogItem
```

### Properties

<a name='TizenX.GenUI.CatalogItem.CreateComponent'></a>

## CreateComponent

Gets or sets the factory function that creates a new view instance for this component.

```csharp
public Func<string, JsonObject, SurfaceContext, DataPath, View> CreateComponent { get; set; }
```
#### Property Value

Func<string, JsonObject, SurfaceContext, DataPath, View>

A new View instance for this component.

<a name='TizenX.GenUI.CatalogItem.Name'></a>

## Name

Gets or initializes the unique name identifier for this catalog item.
This name is used to match against the "component" key in JSON definitions.

```csharp
public string Name { get; init; }
```
#### Property Value

string

<a name='TizenX.GenUI.CatalogItem.Schema'></a>

## Schema

Gets or initializes the JSON schema definition for this component.
This schema describes the expected JSON structure for the component's properties.
Can be used for validation or documentation generation.

```csharp
public string Schema { get; init; }
```
#### Property Value

string

<a name='TizenX.GenUI.CatalogItem.UpdateComponent'></a>

## UpdateComponent

Gets or sets the action that updates an existing view instance with new property values.
This is called when component properties need to be refreshed without recreating the view.

```csharp
public Action<string, JsonObject, SurfaceContext, View, DataPath> UpdateComponent { get; set; }
```
#### Property Value

Action<string, JsonObject, SurfaceContext, View, DataPath>

<a name='TizenX.GenUI.CatalogItem.UpdateComponentTree'></a>

## UpdateComponentTree

Gets or sets the action that updates the component's child view tree.
This is called to build or rebuild the hierarchy of child components.

```csharp
public Action<string, JsonObject, SurfaceContext, View, bool, DataPath> UpdateComponentTree { get; set; }
```
#### Property Value

Action<string, JsonObject, SurfaceContext, View, bool, DataPath>

