### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## DataModel Class

```csharp
public class DataModel : INotifyPropertyChanged
```

### Properties

<a name='TizenX.GenUI.DataModel.Data'></a>

## Data

```csharp
public JsonObject Data { get; }
```
#### Property Value

JsonObject

### Methods

<a name='TizenX.GenUI.DataModel.GetStrValue.TizenX.GenUI.DataPath.'></a>

## GetStrValue(DataPath)

```csharp
public string GetStrValue(DataPath absolutePath)
```
#### Parameters

`absolutePath` DataPath

#### Returns

string

<a name='TizenX.GenUI.DataModel.GetValue.TizenX.GenUI.DataPath.'></a>

## GetValue(DataPath)

```csharp
public JsonNode GetValue(DataPath absolutePath)
```
#### Parameters

`absolutePath` DataPath

#### Returns

JsonNode

<a name='TizenX.GenUI.DataModel.GetValue..1.TizenX.GenUI.DataPath.'></a>

## GetValue<T>(DataPath)

```csharp
public T GetValue<T>(DataPath absolutePath)
```
#### Parameters

`absolutePath` DataPath

#### Returns

T

<a name='TizenX.GenUI.DataModel.ResolveEventContext.System.Text.Json.Nodes.JsonArray.TizenX.GenUI.DataPath.'></a>

## ResolveEventContext(JsonArray, DataPath)

```csharp
public JsonNode ResolveEventContext(JsonArray contextDefinitions, DataPath basePath)
```
#### Parameters

`contextDefinitions` JsonArray

`basePath` DataPath

#### Returns

JsonNode

<a name='TizenX.GenUI.DataModel.SendPropertyChangedEvent.System.String.'></a>

## SendPropertyChangedEvent(string)

```csharp
protected void SendPropertyChangedEvent(string propertyName)
```
#### Parameters

`propertyName` string

<a name='TizenX.GenUI.DataModel.SetExternalDataProvider.TizenX.GenUI.IExternalDataProvider.'></a>

## SetExternalDataProvider(IExternalDataProvider)

```csharp
public void SetExternalDataProvider(IExternalDataProvider provider)
```
#### Parameters

`provider` IExternalDataProvider

<a name='TizenX.GenUI.DataModel.TryGetValue..1.TizenX.GenUI.DataPath...0..'></a>

## TryGetValue<T>(DataPath, out T)

```csharp
public bool TryGetValue<T>(DataPath absolutePath, out T value)
```
#### Parameters

`absolutePath` DataPath

`value` T

#### Returns

bool

<a name='TizenX.GenUI.DataModel.Update.TizenX.GenUI.DataPath.System.Text.Json.Nodes.JsonNode.'></a>

## Update(DataPath, JsonNode)

```csharp
public void Update(DataPath absolutePath, JsonNode contents)
```
#### Parameters

`absolutePath` DataPath

`contents` JsonNode

<a name='TizenX.GenUI.DataModel.UpdateValue.TizenX.GenUI.DataPath.System.Text.Json.Nodes.JsonNode.'></a>

## UpdateValue(DataPath, JsonNode)

```csharp
public void UpdateValue(DataPath absolutePath, JsonNode value)
```
#### Parameters

`absolutePath` DataPath

`value` JsonNode

### Events

<a name='TizenX.GenUI.DataModel.PropertyChanged'></a>

## PropertyChanged

Occurs when a property value changes.

```csharp
public event PropertyChangedEventHandler PropertyChanged
```
