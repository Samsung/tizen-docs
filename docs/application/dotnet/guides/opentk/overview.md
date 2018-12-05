
# OpenTK

The Tizen OpenTK app mode provide a set of fast, low-level C# bindings for OpenGL. Since Tizen 5.0, it is integrated with Tizen Application Framework.

For developing the OpenGL app using C# on the Tizen platform, an app developer uses the TizenFX APIs, the .NET Standard 2.0 APIs, and the OpenTK APIs based on their needs.

Besides the OpenGL ES APIs, the OpenTK also provides several utility libraries including a math or linear algebra package, windowing system, and input handling for application developer.

After setting up the OpenTK development environment, you can quickly create graphic applications with the OpenGL ES 2.0, such as:
-   Ambient App
-   Game
-   Dynamic Partial
-   Physics effect


The OpenTK app offers the following main features:
-   Create cutting-edge graphics with the OpenGL ES 2.0
-   Spice up your GUI with 3D acceleration.
-   Windowing systems, helps you to started..
-   Input and other game essentials.
-   Performant, highly optimized and reliable linear algebra library.


## Key Concepts

To be able to use OpenTK in your application, you must become familiar with the following OpenTK key concepts:
-   **TizenGameApplication**: Application lifecycle manager and base class of OpenTK app for Tizen is integrated with the Tizen application framework. Therefore, you can get the events from the Tizen system.
    The OpenTK app implements virtual lifecycle functions to customize their own app flow.
    For example: `OnCreate`, `OnPause`, `OnResume`, `OnTerminate`, `OnAppControlReceived`, `OnDeviceOrientationChanged`, and so on. 
    
    For more information, see [Applications](https://developer.tizen.org/development/guides/.net-application/application-management/applications).
-   **Window**: An attribute of TizenGameApplication. It provides window related attributes include: `X`, `Y`, `Width`, `Height`, `Title`, `WindowInfo`, and so on. 

    It also provides events and OpenGL context related functions.  which includes the following:
    
    **Events**:
    -   `Load`
    -   `Unload`
    -   `UpdateFrame`
    -   `RenderFrame`
    
    **OpenGL context related**:
    -   `MakeCurrent`
    -   `Run`
    -   `SwapBuffers`
-   **WindowAttributes**: an attribute of TizenGameApplication. It provides window-controlling attributes, which includes the following:
    -   `IsFocusAllowed`
    -   `WindowOpacity`
    
    It also provides a method `AddAuxiliaryHint`.

## Prerequisite

- Visual Studio 2017
- Visual Studio Tools for Tizen
  - [How to install Visual Studio Tools for Tizen](https://github.com/Samsung/tizen-docs/blob/master/docs/application/vstools/install.md)
- Tizen emulator image (supports version Tizen 5.0 and higher)

## Related Information
- Dependencies
  -   Tizen 5.0 and Higher
