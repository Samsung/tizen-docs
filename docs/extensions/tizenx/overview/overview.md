# Tizen Extension Library

## What is Tizen Extension Library?

The Tizen eXtension Library (TizenX) is a collection of modular, open-source C# libraries that enhance and extend the Tizen platform.

Unlike built-in platform APIs, TizenX libraries are unbundled from the operating system and delivered **independently via NuGet**. This approach allows developers to adopt new features, UI components, and performance improvements at their own pace, free from the long OS update cycle.

> **Extend. Experience. Evolve.**

TizenX provides you with ready-to-use components, productivity tools, and pre-integrated functionalities that simplify app development and boost performance.

## Why TizenX?

 * **Modern .NET Design**
    All libraries comply with the .NET Design Guidelines and follow the latest architectural patterns.

 * **Performance and Optimization**
    Benefit from built-in memory and performance optimizations designed for the Tizen platform.

 * **Enhanced Productivity**
    Build apps faster with commercial-level UI components, declarative UI helpers, enhanced layouts, and powerful development tools.

 * **Flexible and Modular**
    TizenX is divided into independent modules. You can include only the libraries you need, keeping your application lightweight.

 * **Rapid Updates**
    Receive the latest features and bug fixes through NuGet without waiting for a new Tizen OS release.

## Tizen.UI

**Tizen.UI** is a lightweight, high-performance C# UI framework for building modern Tizen .NET applications. You can explore the full [API reference](https://pages.github.sec.samsung.net/NUI/Tizen.UI/api/) for a detailed look at all components and browse the [source code](https://github.sec.samsung.net/NUI/Tizen.UI) in our repository.

### Key Concepts

Tizen.UI was engineered to be lighter and more performant by focusing on four key design principles.

#### 1. Slim View Hierarchy

The framework provides a simpler and lighter view hierarchy than traditional frameworks. We provide only the essential APIs, reducing overhead and complexity.

#### 2. Enhanced Layout System

Tizen.UI uses an efficient two-phase layout process: **Measure()** and **Arrange()**. This system optimizes layout passes by recalculating only within the scope of changes, leading to faster UI rendering.

#### 3. Effective Memory Management

Performance is a core feature. Tizen.UI achieves this through several advanced memory management techniques:

* **Minimized Reflection:** Reduces the use of expensive runtime reflection.
* **Optimized Data Objects:** Native and C# data objects are managed independently. C# data objects are represented as `structs` to avoid heap allocation. This means you can create and delete C# data objects frequently without incurring the cost of native object creation calls.
* **Object Pooling:** Objects created once (per type) are held in a pool and reused for subsequent creations. This pattern applies to objects that use the Stack, drastically reducing garbage collection.
* **Smart Lifecycle Management:** When a parent view is removed, it automatically removes all of its child views. This eliminates the need for developers to manually clean up the view tree in the `Dispose()` method of each component

#### 4. C# Markup (Declarative UI)
Tizen.UI includes a set of fluent helper methods and classes designed to simplify building declarative user interfaces directly in C# code, aligning with modern development patterns.

### Modular Packages

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

---

## TizenX.Aurum

**TizenX.Aurum** (also known as Aurum#) is a C# library designed for UI automation testing on Tizen platforms. You can browse the [source code](https://github.sec.samsung.net/NUI/TizenX.Aurum) in our repository.

### Key Features

* **UI Navigation** Locate elements reliably using object properties, `AutomationId`, or flexible XPath-style queries.

* **Action Simulation** Perform user actions such as clicks, text input, and scrolling to simulate real-world interaction.

* **Asynchronous Waits** Automatically wait for elements to appear or change state (e.g., become visible or enabled) before proceeding, making your tests more stable.

---

## TizenX.ZLog (Utility)

**TizenX.ZLog** is a high-performance logging library designed specifically for performance-critical applications on Tizen. Its key feature is the **minimization of temporary string object creation** during logging operations, which significantly reduces garbage collector (GC) pressure.
You can browse the [source code](https://github.sec.samsung.net/qad/TizenX.ZLog) in our repository.

### Key Features

#### Zero-Allocation String Interpolation

ZLog uses an advanced string interpolation method that avoids allocating temporary string objects on the heap.

* **No Temporary Objects:** Drastically reduces GC pressure.
* **Memory Efficient:** Uses thread-local buffers for string building.
* **Stack-Based Allocation:** Utilizes stack allocation where possible.

#### Comprehensive Logging Levels

ZLog supports all standard logging levels:

* Verbose: Detailed debugging information
* Debug: Debug-level messages
* Info: General informational messages
* Warn: Warning conditions
* Error: Error conditions
* Fatal: Critical error conditions

#### Advanced Features

* **Automatic Caller Info:** Automatically captures the file path, function name, and line number of the log call.
* **UTF-8 Encoding:** Full support for UTF-8 encoding in log messages.

## TizenX RPC-Port

X-RPC-Port is an optimized version of Tizen's existing RPC-PORT for .NET. While following the basic architecture of RPC-PORT, it has been modified to work more efficiently when used in .NET environments. This library provides an efficient data serialization and transmission mechanism for inter-process communication (IPC) on the Tizen platform.

### Key Features

* **High Performance**: Provides improved performance compared to legacy Tizen RPC
* **Efficient Serialization**: Parcel system for efficient data serialization/deserialization
* **Type Safety**: Safe data handling using C#'s strong type system
* **Easy to Use**: Intuitive API for easy integration
* **Tizen Platform Optimized**: Design optimized for the Tizen operating system

### Architecture

X-RPC-Port consists of the following core components:

* **Parcel**: Core class for data serialization/deserialization
* **ParcelHeader**: Manages message header information (tag, sequence number, timestamp)
* **IParcelable**: Interface that makes custom data types serializable
* **ParcelBuilder**: Builder class that allows chaining multiple data additions to construct a Parcel
