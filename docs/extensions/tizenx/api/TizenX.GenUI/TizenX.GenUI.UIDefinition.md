### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## UIDefinition Class

Manages UI component definitions and view instances within a surface.
Stores component metadata and provides methods to retrieve and create views.

```csharp
public class UIDefinition
```

### Constructors

<a name='TizenX.GenUI.UIDefinition..ctor.System.String.'></a>

## UIDefinition(string)

Initializes a new instance of the UIDefinition class with the specified surface ID.

```csharp
public UIDefinition(string surfaceId)
```
#### Parameters

`surfaceId` string

The ID of the surface this definition belongs to.

### Properties

<a name='TizenX.GenUI.UIDefinition.RootView'></a>

## RootView

Gets or sets the root view for this UI definition.

```csharp
public View RootView { get; set; }
```
#### Property Value

View

<a name='TizenX.GenUI.UIDefinition.SurfaceId'></a>

## SurfaceId

Gets the surface ID that this UI definition belongs to.

```csharp
public string SurfaceId { get; }
```
#### Property Value

string

### Methods

<a name='TizenX.GenUI.UIDefinition.Add.System.String.TizenX.GenUI.Component.'></a>

## Add(string, Component)

Adds or updates a component definition with the specified ID.

```csharp
public void Add(string id, Component component)
```
#### Parameters

`id` string

The unique identifier for the component.

`component` Component

The component definition to add or update.

<a name='TizenX.GenUI.UIDefinition.Debug'></a>

## Debug()

Outputs debug information about all components in this definition to the console.
Useful for troubleshooting component registration and view hierarchy issues.

```csharp
public void Debug()
```
<a name='TizenX.GenUI.UIDefinition.GetTemplateView.System.String.TizenX.GenUI.DataPath.'></a>

## GetTemplateView(string, DataPath)

Creates a new view instance from a template component definition.
Use this method for data-bound list items where each item needs its own view instance.

```csharp
public View GetTemplateView(string id, DataPath basePath)
```
#### Parameters

`id` string

The unique identifier for the template component.

`basePath` DataPath

The base data path for resolving data bindings.
This allows each template instance to bind to different data items.

#### Returns

View

A new view instance created from the template, or null if the template is not found.

<a name='TizenX.GenUI.UIDefinition.GetView.System.String.System.Boolean.TizenX.GenUI.DataPath.'></a>

## GetView(string, bool, DataPath)

Retrieves a view instance by its component ID.

```csharp
public View GetView(string id, bool isTemplate = false, DataPath basePath = null)
```
#### Parameters

`id` string

The unique identifier for the component.

`isTemplate` bool

If true, creates a new view instance from the template using the specified base path.
If false, returns the existing view instance.

`basePath` DataPath

The base data path for resolving data bindings in template views.
Only used when isTemplate is true.

#### Returns

View

The view instance if found; otherwise, null.
For templates, returns a new view instance created from the template definition.

<a name='TizenX.GenUI.UIDefinition.TryGet.System.String.TizenX.GenUI.Component..'></a>

## TryGet(string, out Component)

Attempts to retrieve a component definition by its ID.

```csharp
public bool TryGet(string id, out Component component)
```
#### Parameters

`id` string

The unique identifier for the component.

`component` Component

When this method returns, contains the component definition if found; otherwise, null.

#### Returns

bool

true if the component was found; otherwise, false.

<a name='TizenX.GenUI.UIDefinition.UpdateViewTree'></a>

## UpdateViewTree()

Updates the view tree for all components in this definition.
This rebuilds the parent-child relationships for all component views.

```csharp
public void UpdateViewTree()
```
