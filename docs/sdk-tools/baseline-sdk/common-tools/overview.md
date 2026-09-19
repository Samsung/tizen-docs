# Overview Tizen SDK

> [!IMPORTANT]
> **Tizen Studio is deprecated and no longer supported.** Tizen Studio — the retired Eclipse-based IDE — must not be installed or used. Tizen application development is supported through the IDE extensions below, which install and share the Baseline SDK.

Tizen SDK supports IDE Extensions for Tizen App development based on two IDEs (Visual Studio and Visual Studio Code).

IDE Extensions share Baseline SDK, which is a common tool required for Tizen application development.

## How to get these tools

**Install the extension for your IDE. The extension installs the Baseline SDK for you** —
there is no separate SDK download to perform first.

- **Visual Studio Code**: install [Visual Studio Code Extension for Tizen](../../vscode-ext/Tizen/dotnet.md)
  from the Visual Studio Code Marketplace. On first launch the extension asks for a Tizen
  SDK path and then downloads and installs the required SDK resources. If no Baseline SDK
  is found on the machine, the extension installs one.
- **Visual Studio**: install [Visual Studio Tools for Tizen](../../vstools/install.md) from
  the Visual Studio Marketplace. On first launch it asks for an SDK resource path and then
  installs the server and core apps.

For a machine without an IDE — a build server, or a terminal-only environment — install the
Baseline SDK with the CLI installer instead. See
[Installing the Tizen SDK](../setup/install-sdk.md).

Baseline SDK includes the following standalone tools.

* Tizen-Core : Consistent Tizen SDK interface to use baseline tools and CLI from various IDE and external tools.
* Package Manager : a comprehensive package management tool for installing, updating, and removing tizen platform and sdk components
* Certificate Manager : Tizen certificate management tools to store developer's certificates for singing Tizen application.
* Emulator Manager : Tool to create and manage emulator instances.
* Device Manager : Standalone tool that manages device and allows you to access your internal file systems and logs.
* Command-line Interface : CLI provides functionalities for entire Tizen application development process by using the terminal.
* Dynamic Analyzer : Native profiling tool for Tizen application
* SDB (Smart Device Bridge) : Command line tool that communicates with a conneted target device (It can be an emulator instance of a real Tizen devce like TV)

**Figure : Overview Tizen SDK Components**

  ![Overview Tizen SDK Components](./media/overview_sdk.png)

Tizen SDK provides various development tools and platform resources for native (c, c++), web(HTML, JS, CSS), and .NET(c#) application and also supports hybrid application packaging tool.

Developers can use "Visual Studio Code Extension for Tizen" or "Visual Studio Tools for Tizen" for developing all types of application supported by Tizen platform from project creation to onboarding debug and tests on actual devices.

| Development Tools              | Native                                      | Web                                         | .NET                                                                                                                                                              |
| ------------------------------ | ------------------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Project Creation               | Project wizard & Templates                  | Project wizard & Templates                  | Project wizard & Templates                                                                                                                                        |
| Build Tools                    | GCC, Ninja/Make                             | -                                           | `dotnet sdk` or `MSBuild`                                                                                                                                     |
| Configuration Tool             | Manifest Editor                             | Web Config Editor                           | -                                                                                                                                                                 |
| Code Edit Tool                 | Content Assist<br />API & Privilege Checker | Content Assist<br />API & Privilege Checker | Content Assist                                                                                                                                                    |
| Debugger                       | GDB                                         | Web Inspector                               | Netcoredbg                                                                                                                                                        |
| Static Analyzer                | Static Analyzer                             | JavaScript Analyzer                         | -                                                                                                                                                                 |
| Unit Test & Code Coverage Tool | gtest & gcov                                | `<QUnit>`                                 | `<NUnit>`<br />※ .NET Unit Test Tool is provided by .NET CLI.<br />You can refer to [LINK](https://learn.microsoft.com/en-us/dotnet/core/testing/#testing-tools) |
| Address & Leak Sanitizer       | ASAN/LSAN                                   | -                                           | -                                                                                                                                                                 |
| Profiler                       | <br />Dynamic Analyzer<br />T-Trace         | Web Inspector                               | Core Profiler<br />Memory Profiler<br />.NET Diagnostics<br />(dotnet dummp/Trace, GC dump)                                                                      |
