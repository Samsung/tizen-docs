## TizenX.GenUI Namespace

| Classes | |
| :--- | :--- |
| [A2UIMessage](TizenX.GenUI.A2UIMessage.md 'TizenX.GenUI.A2UIMessage') |  |
| [A2UIRenderer](TizenX.GenUI.A2UIRenderer.md 'TizenX.GenUI.A2UIRenderer') | Main renderer class that processes JSON-based UI definitions and creates Tizen.UI views. This class manages surface rendering, component catalogs, and user action handling. |
| [BeginRenderingMessage](TizenX.GenUI.BeginRenderingMessage.md 'TizenX.GenUI.BeginRenderingMessage') |  |
| [CatalogItem](TizenX.GenUI.CatalogItem.md 'TizenX.GenUI.CatalogItem') | Represents a component catalog item that defines how to create, update, and manage a UI component. Catalog items are used to register custom components that can be rendered from JSON definitions. |
| [CatalogManager](TizenX.GenUI.CatalogManager.md 'TizenX.GenUI.CatalogManager') | Manages a collection of component catalog items, providing registration and lookup functionality. Acts as a registry for all available component types that can be rendered from JSON definitions. |
| [Component](TizenX.GenUI.Component.md 'TizenX.GenUI.Component') |  |
| [DataContext](TizenX.GenUI.DataContext.md 'TizenX.GenUI.DataContext') |  |
| [DataModel](TizenX.GenUI.DataModel.md 'TizenX.GenUI.DataModel') |  |
| [DataModelUpdateMessage](TizenX.GenUI.DataModelUpdateMessage.md 'TizenX.GenUI.DataModelUpdateMessage') |  |
| [DataPath](TizenX.GenUI.DataPath.md 'TizenX.GenUI.DataPath') |  |
| [DeleteSurfaceMessage](TizenX.GenUI.DeleteSurfaceMessage.md 'TizenX.GenUI.DeleteSurfaceMessage') |  |
| [Logger](TizenX.GenUI.Logger.md 'TizenX.GenUI.Logger') |  |
| [SurfaceContext](TizenX.GenUI.SurfaceContext.md 'TizenX.GenUI.SurfaceContext') | Represents the context for a single UI surface, managing its UI definition, data model, and lifecycle events. Each surface has its own isolated context with separate component definitions and data bindings. |
| [SurfaceEventArgs](TizenX.GenUI.SurfaceEventArgs.md 'TizenX.GenUI.SurfaceEventArgs') | Provides data for surface lifecycle events such as BeginRendering and DeleteSurface. Contains information about the surface being rendered or deleted. |
| [SurfaceManager](TizenX.GenUI.SurfaceManager.md 'TizenX.GenUI.SurfaceManager') | Manages the creation, retrieval, and lifecycle of multiple surface contexts. Acts as a central registry for all surfaces and forwards events from individual surfaces. |
| [SurfaceUpdateMessage](TizenX.GenUI.SurfaceUpdateMessage.md 'TizenX.GenUI.SurfaceUpdateMessage') |  |
| [UIDefinition](TizenX.GenUI.UIDefinition.md 'TizenX.GenUI.UIDefinition') | Manages UI component definitions and view instances within a surface. Stores component metadata and provides methods to retrieve and create views. |
| [UserActionEventArgs](TizenX.GenUI.UserActionEventArgs.md 'TizenX.GenUI.UserActionEventArgs') | Provides data for the UserAction and UserAction events. Contains the message describing the user action that was triggered. |

| Interfaces | |
| :--- | :--- |
| [IExternalDataProvider](TizenX.GenUI.IExternalDataProvider.md 'TizenX.GenUI.IExternalDataProvider') |  |

