### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## Component Class

```csharp
public class Component
```

### Constructors

<a name='TizenX.GenUI.Component..ctor.System.String.System.Text.Json.Nodes.JsonObject.System.Nullable.System.Single..TizenX.GenUI.SurfaceContext.'></a>

## Component(string, JsonObject, float?, SurfaceContext)

```csharp
public Component(string id, JsonObject json, float? weight, SurfaceContext context)
```
#### Parameters

`id` string

`json` JsonObject

`weight` float?

`context` SurfaceContext

### Properties

<a name='TizenX.GenUI.Component.ComponentType'></a>

## ComponentType

```csharp
public string ComponentType { get; }
```
#### Property Value

string

<a name='TizenX.GenUI.Component.Id'></a>

## Id

```csharp
public string Id { get; }
```
#### Property Value

string

<a name='TizenX.GenUI.Component.Instance'></a>

## Instance

```csharp
public View Instance { get; }
```
#### Property Value

View

<a name='TizenX.GenUI.Component.Json'></a>

## Json

```csharp
public JsonObject Json { get; }
```
#### Property Value

JsonObject

<a name='TizenX.GenUI.Component.SurfaceContext'></a>

## SurfaceContext

```csharp
public SurfaceContext SurfaceContext { get; }
```
#### Property Value

SurfaceContext

<a name='TizenX.GenUI.Component.Weight'></a>

## Weight

```csharp
public float? Weight { get; }
```
#### Property Value

float?

### Methods

<a name='TizenX.GenUI.Component.CreateTemplateView.TizenX.GenUI.DataPath.'></a>

## CreateTemplateView(DataPath)

```csharp
public View CreateTemplateView(DataPath basePath)
```
#### Parameters

`basePath` DataPath

#### Returns

View

<a name='TizenX.GenUI.Component.Update.TizenX.GenUI.CatalogManager.TizenX.GenUI.SurfaceContext.'></a>

## Update(CatalogManager, SurfaceContext)

```csharp
public void Update(CatalogManager catalogManager, SurfaceContext context)
```
#### Parameters

`catalogManager` CatalogManager

`context` SurfaceContext

<a name='TizenX.GenUI.Component.UpdateJson.System.Text.Json.Nodes.JsonObject.System.Nullable.System.Single..'></a>

## UpdateJson(JsonObject, float?)

```csharp
public void UpdateJson(JsonObject json, float? weight)
```
#### Parameters

`json` JsonObject

`weight` float?

<a name='TizenX.GenUI.Component.UpdateViewTree'></a>

## UpdateViewTree()

```csharp
public void UpdateViewTree()
```
