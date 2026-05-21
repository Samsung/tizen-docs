# TizenX.Aurum

**TizenX.Aurum** (also known as Aurum#) is a C# library designed for UI automation testing on Tizen platforms. It empowers developers and QA engineers to write reliable, maintainable, and asyncronous UI tests for Tizen applications.

## Key Features

* **UI Navigation** Locate elements reliably using object properties, `AutomationId`, or flexible XPath-style queries.

* **Action Simulation** Perform user actions such as clicks, text input, and scrolling to simulate real-world interaction.

* **Asynchronous Waits** Automatically wait for elements to appear or change state (e.g., become visible or enabled) before proceeding, making your tests more stable.

## Getting Started

### 📦 Installation

You can eadily add TizenX.Aurum to your project via the NuGet package manager.

### Manual Reference

#### .NET CLI

```sh
> dotnet add package TizenX.Aurum --version 1.0.5.10051
```

#### PackageReference

```xml
<PackageReference Include="TizenX.Aurum" Version="1.0.5.10051" />
```

### 🚀 Quick Start

Here is the simple snippet to get you started with TizenX.Aurum:

```csharp
using Aurum;

AccessibleWatcher.getInstance();
UiDevice device = UiDevice.getInstance();

device.sendKeyAndWaitForEvents("XF86SysMenu", A11yEvent.EVENT_WINDOW_ACTIVATE, 5000, "org.tizen.menu");
UiSelector sel = new UiSelector();
sel.text("Sound");

UiObject found = device.waitFor(Until.findObject(sel));
found.click();
```
