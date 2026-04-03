# Getting Started: TizenX.GenUI A2UI Renderer


A2UI Renderer is a library for rendering JSON-based A2UI messages into Tizen.UI views. This document explains how to use A2UI Renderer to render A2UI JSON messages as UI views.

## Table of Contents

1. [Basic Setup](#1-basic-setup)
2. [Creating A2UIRenderer Instance](#2-creating-a2uirenderer-instance)
3. [Subscribing to Events](#3-subscribing-to-events)
4. [Passing JSON Messages and Rendering](#4-passing-json-messages-and-rendering)
5. [Handling User Actions](#5-handling-user-actions)

---

## 1. Basic Setup

Add the necessary project reference to use A2UI Renderer.

```xml
<ItemGroup>
  <PackageReference Include="TizenX.GenUI" Version="1.0.0-rc.1" />
</ItemGroup>
```

## 2. Creating A2UIRenderer Instance

First, create an `A2UIRenderer` instance to render A2UI messages.

```csharp
using TizenX.GenUI;

// Create A2UIRenderer instance
var a2uiRenderer = new A2UIRenderer();
```

## 3. Subscribing to Events

A2UIRenderer provides three main events for handling UI rendering and user interactions.

### 3.1 BeginRenderingSurface Event

Occurs when a surface begins rendering. Use this event to add the rendered root view to your layout.

```csharp
a2uiRenderer.BeginRenderingSurface += (s, e) =>
{
    // e.SurfaceId: The surface identifier
    // e.SurfaceRoot: The rendered root view
    layout.Add(e.SurfaceRoot);
};
```

### 3.2 DeleteSurface Event

Occurs when a surface is deleted. Use this event to remove the surface view from your layout.

```csharp
a2uiRenderer.DeleteSurface += (s, e) =>
{
    // e.SurfaceId: The deleted surface identifier
    // e.SurfaceRoot: The deleted root view
    layout.Remove(e.SurfaceRoot);
};
```

### 3.3 UserAction Event

Occurs when a user action (e.g., button click) is triggered.

```csharp
a2uiRenderer.UserAction += (s, e) =>
{
    // e.Message: JsonObject containing action details
    // - name: Action name
    // - sourceComponentId: ID of the component that triggered the action
    // - context: Action context data
    Console.WriteLine($"User action: {e.Message}");
};
```

## 4. Passing JSON Messages and Rendering

### 4.1 JsonFeed Method

Passes A2UI JSON messages to the renderer. You can pass JSON strings or JsonObject/JsonArray directly.

```csharp
// Pass JSON string
a2uiRenderer.JsonFeed(jsonString);

// Pass JsonObject
a2uiRenderer.JsonFeed(jsonObject);

// Pass JsonArray (multiple messages)
a2uiRenderer.JsonFeed(jsonArray);
```

### 4.2 RenderJson Method

Renders JSON and returns a `SurfaceContext`. Use this when you need direct control over the rendering result.

```csharp
// Render JSON string
var context = a2uiRenderer.RenderJson(jsonString);
if (context?.RootView != null)
{
    layout.Add(context.RootView);
}
```

### 4.3 A2UI JSON Message Structure

A2UI messages can have the following four types:

#### beginRendering
Starts rendering a surface.

```json
{
  "beginRendering": {
    "surfaceId": "main",
    "root": "rootId"
  }
}
```

#### surfaceUpdate
Defines components for a surface.

```json
{
  "surfaceUpdate": {
    "surfaceId": "main",
    "components": [
      {
        "id": "rootId",
        "component": {
          "Column": {
            "children": { "explicitList": ["text1", "button1"] }
          }
        }
      },
      {
        "id": "text1",
        "component": {
          "Text": { "text": { "literalString": "Hello A2UI" } }
        }
      },
      {
        "id": "button1",
        "component": {
          "Button": {
            "child": "button-label",
            "action": { "name": "submit" }
          }
        }
      },
      {
        "id": "button-label",
        "component": {
          "Text": { "text": { "literalString": "Click Me" } }
        }
      }
    ]
  }
}
```

#### dataModelUpdate
Updates the data model. Used for data binding.

```json
{
  "dataModelUpdate": {
    "surfaceId": "main",
    "path": "/user",
    "contents": [
      { "key": "name", "valueString": "John" },
      { "key": "age", "valueNumber": 25 }
    ]
  }
}
```

#### deleteSurface
Deletes a surface.

```json
{
  "deleteSurface": {
    "surfaceId": "main"
  }
}
```

## 5. Handling User Actions

User actions such as button clicks are handled through the `UserAction` event. Information defined in the button's `action` property is passed as event arguments.

### Button Action Definition Example

```json
{
  "id": "submit-btn",
  "component": {
    "Button": {
      "child": "submit-text",
      "action": {
        "name": "submit",
        "context": [
          { "key": "formData", "value": { "path": "/form" } }
        ]
      }
    }
  }
}
```

### Action Handling Example

```csharp
a2uiRenderer.UserAction += (s, e) =>
{
    var actionName = e.Message["name"]?.ToString();
    var sourceId = e.Message["sourceComponentId"]?.ToString();
    var context = e.Message["context"]?.AsObject();
    
    switch (actionName)
    {
        case "submit":
            HandleSubmit(context);
            break;
        case "cancel":
            HandleCancel();
            break;
    }
};
```


## Summary

Basic workflow for using A2UI Renderer:

1. Create `A2UIRenderer` instance
2. Subscribe to `BeginRenderingSurface`, `DeleteSurface`, `UserAction` events
3. Pass A2UI JSON using `JsonFeed()` or `RenderJson()` method
4. Add/remove rendered views to layout in event handlers
5. Handle user interactions via `UserAction` event
