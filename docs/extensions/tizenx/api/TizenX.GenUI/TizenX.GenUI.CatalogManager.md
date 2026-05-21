### [TizenX.GenUI](TizenX.GenUI.md 'TizenX.GenUI')

## CatalogManager Class

Manages a collection of component catalog items, providing registration and lookup functionality.
Acts as a registry for all available component types that can be rendered from JSON definitions.

```csharp
public class CatalogManager
```

### Constructors

<a name='TizenX.GenUI.CatalogManager..ctor'></a>

## CatalogManager()

Initializes a new instance of the CatalogManager class.
The catalog starts empty and can be populated via UpdateCatalog(IEnumerable<CatalogItem>).

```csharp
public CatalogManager()
```
### Properties

<a name='TizenX.GenUI.CatalogManager.Catalogs'></a>

## Catalogs

Gets all catalog items currently registered in the manager.

```csharp
public IEnumerable<CatalogItem> Catalogs { get; }
```
#### Property Value

IEnumerable<CatalogItem>

An enumerable collection of all registered CatalogItem objects.

<a name='TizenX.GenUI.CatalogManager.Item.System.String.'></a>

## this[string]

Gets the catalog item with the specified name.

```csharp
public CatalogItem this[string name] { get; }
```
#### Parameters

`name` string

The name of the catalog item to retrieve.

#### Property Value

CatalogItem

The CatalogItem with the specified name.

### Methods

<a name='TizenX.GenUI.CatalogManager.IsSupport.System.String.'></a>

## IsSupport(string)

Determines whether a component with the specified name is registered in the catalog.

```csharp
public bool IsSupport(string name)
```
#### Parameters

`name` string

The name of the component to check.

#### Returns

bool

true if a component with the specified name exists in the catalog; otherwise, false.

<a name='TizenX.GenUI.CatalogManager.UpdateCatalog.System.Collections.Generic.IEnumerable.TizenX.GenUI.CatalogItem..'></a>

## UpdateCatalog(IEnumerable<CatalogItem>)

Adds or updates catalog items in the manager.
If an item with the same name already exists, it will be replaced.

```csharp
public void UpdateCatalog(IEnumerable<CatalogItem> catalog)
```
#### Parameters

`catalog` IEnumerable<CatalogItem>

An enumerable collection of CatalogItem objects to register.
Each item's Name property is used as the key.

