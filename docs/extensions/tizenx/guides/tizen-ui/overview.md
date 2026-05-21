# Tizen.UI

**Tizen.UI** is a lightweight, high-performance C# UI framework for building modern Tizen .NET applications. You can explore the full [API reference](https://pages.github.sec.samsung.net/NUI/Tizen.UI/api/) for a detailed look at all components.

## Key Concepts

Tizen.UI was engineered to be lighter and more performant by focusing on four key design principles.

### 1. Slim View Hierarchy

The framework provides a simpler and lighter view hierarchy than traditional frameworks. We provide only the essential APIs, reducing overhead and complexity.

### 2. Enhanced Layout System

Tizen.UI uses an efficient two-phase layout process: **Measure()** and **Arrange()**. This system optimizes layout passes by recalculating only within the scope of changes, leading to faster UI rendering.

### 3. Effective Memory Management

Performance is a core feature. Tizen.UI achieves this through several advanced memory management techniques:

* **Minimized Reflection:** Reduces the use of expensive runtime reflection.
* **Optimized Data Objects:** Native and C# data objects are managed independently. C# data objects are represented as `structs` to avoid heap allocation. This means you can create and delete C# data objects frequently without incurring the cost of native object creation calls.
* **Object Pooling:** Objects created once (per type) are held in a pool and reused for subsequent creations. This pattern applies to objects that use the Stack, drastically reducing garbage collection.
* **Smart Lifecycle Management:** When a parent view is removed, it automatically removes all of its child views. This eliminates the need for developers to manually clean up the view tree in the `Dispose()` method of each component

### 4. C# Markup (Declarative UI)
Tizen.UI includes a set of fluent helper methods and classes designed to simplify building declarative user interfaces directly in C# code, aligning with modern development patterns.

## Modular Packages

Tizen.UI is fully modular. You can include only the packages you need.

* `Tizen.UI`
* `Tizen.UI.Components`
* `Tizen.UI.Components.Material`
* `Tizen.UI.Layouts`
* `Tizen.UI.Primitives2D`
* `Tizen.UI.Scene3D`
* `Tizen.UI.Skia`
* `Tizen.UI.Visuals`
* `Tizen.UI.Widget`
* `Tizen.UI.WindowBorder`
* `Tizen.UI.Tools`
