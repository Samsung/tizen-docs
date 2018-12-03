
# OpenTK

Tizen OpenTK app mode provide a set of fast, low-level C# bindings for OpenGL ES, it had been integrated with
Tizen Application Framework since Tizen 5.0. For developing OpenGL app in C# on Tizen platform, App developer 
could use TizenFX APIs, .NET Standard 2.0 APIs and OpenTK APIs as their need.

Besides the OpenGL ES APIs, OpenTK also provides several utility libraries, including a math/linear algebra 
package, windowing system, and input handling for application developer.

After you have set up the OpenTK development environment, you can quickly create graphic applications with OpenGL ES 2.0, such as: 
-   Ambient App
-   Game
-   Dynamic Partial
-   Physics effect


OpenTK offers the following main features:
-   Create cutting-edge graphics with OpenGL ES 2.0.
-   Spice up your GUI with 3d acceleration.
-   Windowing systems to help get you started.
-   Input and other game essentials.
-   Performant, highly optimized and reliable linear algebra library.


## Key Concepts

To be able to use OpenTK in your application, you must become familiar with the following OpenTK key concepts:
-   **TizenGameApplication**: Application lifecyle manager and the base class of OpenTK app for Tizen. It is 
integrated with Tizen application framework, so you can get the events from the Tizen system.
    OpenTK app could implements virtual lifecycle functions to customize their own app flow. 
    For example: `OnCreate`, `OnPause`, `OnResume`, `OnTerminate`, `OnAppControlReceived`, `OnDeviceOrientationChanged`, etc. For more information about these methods, please reference to [Application](https://developer.tizen.org/development/guides/.net-application/application-management/applications).
-   **Window**: an attribute of TizenGameApplication. It provides window related attributes include: `X`, `Y`, `Width`, `Height`, `Title`, `WindowInfo`, and so on. It also provides events and OpenGL context related functions. The events include: `Load`, `Unload`, `UpdateFrame`, `RenderFrame`; the OpenGL context related funcitons, including: `MakeCurrent`, `Run`, `SwapBuffers`.
-   **WindowAttributes**: an attribute of TizenGameApplication. It provides window controlling attributes, including: `IsFocusAllowed`, `WindowOpacity`; it also provides a method `AddAuxiliaryHint`.

## Prerequisite

- Visual Studio 2017
- Visual Studio Tools for Tizen
  - [How to install Visual Studio Tools for Tizen](https://github.com/Samsung/tizen-docs/blob/master/docs/application/vstools/install.md)
- Tizen emulator image (supports version Tizen 5.0 and higher)

## Related Information
- Dependencies
  -   Tizen 5.0 and Higher
