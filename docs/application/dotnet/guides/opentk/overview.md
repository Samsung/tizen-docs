
# OpenTK

Tizen OpenTK provides a set of fast and low-level C# bindings for OpenGL&reg; ES 2.0 APIs. From Tizen 5.0, it is integrated with Tizen Application Framework.

For developing the OpenGL&reg; app using C# on the Tizen platform, an app developer uses TizenFX APIs, .NET Standard 2.0 APIs, and OpenTK APIs based on their needs.

Besides the OpenGL&reg; ES APIs, OpenTK also provides several utility libraries including a math or linear algebra package, windowing system, and input handling for application developers.

After setting up the OpenTK development environment, you can quickly create graphic applications with the OpenGL&reg; ES 2.0, such as ambient applications, games, dynamic partial, physics effect.

The OpenTK app offers the following features:

-   Create graphics with the OpenGL&reg; ES 2.0.
-   GUI animation with 3D acceleration.
-   Windowing systems to help you get started.
-   Input handling and other game essentials.
-   Powerful, highly optimized, and reliable linear algebra library.


## Key Concepts

To use OpenTK in your application, understand the following OpenTK key concepts:

-   `TizenGameApplication`: The application lifecycle manager and base class of OpenTK app for Tizen.

    `TizenGameApplication` is integrated with the Tizen Application framework. Therefore, you can get the events from the Tizen Application framework. The OpenTK app implements virtual lifecycle functions to customize their own app flow.  For example, `OnCreate`, `OnPause`, `OnResume`, `OnTerminate`, `OnAppControlReceived`, `OnDeviceOrientationChanged`, and so on.

    For more information, see [Applications](../applications/ui-app.md).

-   `Window`: An attribute of `TizenGameApplication`. It provides window related attributes, which include `X`, `Y`, `Width`, `Height`, `Title`, `WindowInfo`, and so on.

    It also provides **Events** and **OpenGL** context related functions:

    **Events**

    -   `Load`
    -   `Unload`
    -   `UpdateFrame`
    -   `RenderFrame`

    **OpenGL&reg; context related functions**

    -   `MakeCurrent`
    -   `Run`
    -   `SwapBuffers`

-   `WindowAttributes`: An attribute of `TizenGameApplication`.  It provides window-controlling attributes, such as `IsFocusAllowed` and `WindowOpacity`. It also provides a method `AddAuxiliaryHint`.

## Related Information
- Dependencies
  -   Tizen 5.0 and Higher
