# DALi Basic UI Application


To create a DALi basic UI application, you must:

- Use the [Dali::Application class](#api).
- Make sure you [start the event loop](#mainloop).
- [React to application events](#callback) with callbacks.

For the steps of creating the basic parts of a simple DALi UI application, see [Basics of Creating a DALi Application](#create).

<a name="api"></a>
## Main Application Class

If you want to use DALi for your application UI, you must create the application with the `Dali::Application` class (in [mobile](../../../api/mobile/latest/classDali_1_1Application.html) and [wearable](../../../api/wearable/latest/classDali_1_1Application.html) applications). This class provides the means for initializing the resources required by DALi.

The following table lists the main functions you need in your application. They are all provided by the `Dali::Application` class.

**Table: Main functions**

| Function        | Description                              |
|-----------------|------------------------------------------|
| `New()`         | Constructs the `Dali::Application` class. |
| `GetWindow()`   | Retrieves the window used by the `Dali::Application` class. |
| `SetViewMode()` | Sets the viewing mode for the application. |
| `Quit()`        | Quits the application.                   |

<a name="mainloop"></a>
## Event Loop

Like all ordinary Tizen applications, the DALi application must start the main event loop. Afterwards, it can receive events from the platform.

The `mainloop()` function is used to start the event loop. If you do not call the function and start the event loop, DALi cannot call any callback functions for application events.

<a name="callback"></a>
## Event Callbacks

The `Dali::Application` class emits several signals which you can connect to.

The following table lists the callbacks for the basic signals provided by the `Dali::Application` class. These signals originally occur in the Tizen application framework, and you can use the callbacks to react to them.

**Table: Callbacks for basic application event signals**

| Callback                  | Description                              |
|---------------------------|------------------------------------------|
| `InitSignal()`            | Called when the DALi application is ready to start. The signal is emitted when the DALi core components (windows, resource, thread) are ready for use. |
| `ResumeSignal()`          | Called when the application becomes visible. The signal is most useful when the application is ready to restart from the paused state. |
| `PauseSignal()`           | Called when the application becomes invisible. The signal is emitted when the application is paused due to another application becoming active (for example, because of a call, alarm, or message alert). |
| `TerminateSignal()`       | Called when the application is terminated. The signal is useful when the application has resources to release at the end. By releasing those resources, you allow other applications to use them. |
| `ResizeSignal()`          | Called when the window size is changes. The signal is called when a window is created or resized. You can use the signal to change the UI layout according to the new window size. |
| `AppControlSignal()`      | Called when an [application control](../app-controls.md) signal is emitted from another application. This provides the means to communicate between applications. |
| `LanguageChangedSignal()` | Called when the language is changed on the device. You can use the signal to refresh the display with the new language. |
| `RegionChangedSignal()`   | Called when the region is changed. You can use the signal to refresh any region-specific information on the screen. |
| `BatteryLowSignal()`      | Called when the battery state is low. You can use the signal to save any crucial information in case the battery state becomes so low that the application is forcefully terminated. |
| `MemoryLowSignal()`       | Called when the memory state is low. You can use the signal to release any unused memory. |

For more information on Tizen UI applications in general, see [UI Application](index.md).

<a name="create"></a>
## Basics of Creating a DALi Application

To create a DALi basic UI application:

1. Initialize the application:

   1. To use the functions and data types of the DALi API, (in [mobile](../../../api/mobile/latest/group__dali.html) and [wearable](../../../api/wearable/latest/group__dali.html) applications), include the `<dali-toolkit/dali-toolkit.h>` header file in your application:
      ```
      #include <dali-toolkit/dali-toolkit.h>
      ```
   2. Use the following 2 `using` directives for convenience, because all DALi APIs are contained in either `Dali` or `Dali::Toolkit` namespace:
      ```
      using namespace Dali;
      using namespace Dali::Toolkit;
      ```

2. Create the `Dali::Application` class instance to initialize and set up DALi:
   ```
   Application application = Application::New( &argc, &argv );
   ```

3. Connect signals to keep yourself informed when certain system events occur.

   To manage signal connection safely, DALi provides the `Dali::ConnectionTracker` class (in [mobile](../../../api/mobile/latest/classDali_1_1ConnectionTracker.html) and [wearable](../../../api/wearable/latest/classDali_1_1ConnectionTracker.html) applications). A typical way to start a DALi application is to create a class derived from the `Dali::ConnectionTracker` class and use its member functions as callback functions for DALi signals.

   When the application receives the `InitSignal()`, it can build the 3D scene graph. Connect the `HelloWorld::Create()` callback to the `Dali::Application::InitSignal()` function:

   ```
   mApplication.InitSignal().Connect( this, &HelloWorld::Create );
   ```

4. Create an actor and add it to the stage.

   The `Dali::Toolkit::TextLabel` UI component (in [mobile](../../../api/mobile/latest/classDali_1_1Toolkit_1_1TextLabel.html) and [wearable](../../../api/wearable/latest/classDali_1_1Toolkit_1_1TextLabel.html) applications) renders a short text string.

   To display the text label, add it to a stage. The stage instance is a singleton object (the only instance of its class during the lifetime of the program), so you can get it using a static function:

   ```
   Stage stage = Stage::GetCurrent();

   TextLabel textLabel = TextLabel::New( "Hello World" );
   stage.Add( textLabel );
   ```

   The application stores the actor and resource handles. DALi objects are reference-counted, which makes sure they exist only as long as they are needed. Even if the `TextLabel` component is removed from the stage, it remains alive through the reference.

5. Handle touch and key event signals:

   ```
   stage.GetRootLayer().TouchSignal().Connect( this, &HelloWorld::OnTouch );
   stage.KeyEventSignal().KeyEventSignal().Connect( this, &HelloWorld::OnKeyEvent );
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
