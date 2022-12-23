
# OpenTK

Tizen OpenTK provides a set of fast and low-level C# bindings for OpenGL&reg; ES 2.0 APIs. Since Tizen 5.0, it is integrated with Tizen application framework.

For developing the OpenGL&reg; app using C# on the Tizen platform, an app developer uses TizenFX APIs, .NET Standard 2.0 APIs, and OpenTK APIs based on their needs.

Besides the OpenGL&reg; ES APIs, OpenTK also provides several utility libraries including a math or linear algebra package, a windowing system, and input handling for application developers.

After setting up the OpenTK development environment, you can quickly create graphic applications with OpenGL&reg; ES 2.0, such as ambient applications, games, dynamic partial, and physics effect.

For more information on how to create a .NET application with OpenTK on Tizen, see [Quickstart](quickstart.md).

The OpenTK app offers the following features:

-   Create graphics with the OpenGL&reg; ES 2.0.
-   GUI animation with 3D acceleration.
-   Windowing systems to help you get started.
-   Input handling and other game essentials.
-   Powerful, highly optimized, and reliable linear algebra library.


## Key concepts

To use OpenTK in your application, understand the following OpenTK key concepts:

-   `TizenGameApplication`: The application lifecycle manager and base class of OpenTK app for Tizen.

    `TizenGameApplication` is integrated with the Tizen application framework. Therefore, you can get the events from the Tizen application framework. The OpenTK app implements virtual lifecycle functions to customize its own app flow.  For example, `OnCreate`, `OnPause`, `OnResume`, `OnTerminate`, `OnAppControlReceived`, `OnDeviceOrientationChanged`, and so on.

    For more information, see [UI Applications](../../applications/uiapplication/ui-app.md).

-   `Window`: An attribute of `TizenGameApplication`. It provides window related attributes, which include `X`, `Y`, `Width`, `Height`, `Title`, `WindowInfo`, and so on.

    It also provides **Events** and **OpenGL** context related functions, which are described below:

    **Events**

    -   `Load`
    -   `Unload`
    -   `UpdateFrame`
    -   `RenderFrame`

    **OpenGL&reg; context related functions**

    -   `MakeCurrent`
    -   `Run`
    -   `SwapBuffers`

    For more information, see [Window of OpenTK](window-of-opentk.md).

-   `WindowAttributes`: An attribute of `TizenGameApplication`.  It provides window-controlling attributes, such as `IsFocusAllowed` and `WindowOpacity`. It also provides a method `AddAuxiliaryHint`.

## Related information
- Dependencies
  -   Tizen 5.0 and Higher
