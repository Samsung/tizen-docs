# Widget Application

You can create widget applications, which are Tizen .NET applications shown on the home screen. They are launched by the home screen when the user selects them in the **Add Widget** menu.

The main widget application features include:

- Creating widget applications

  You can [create a widget application](#create), which usually has 1 process for maintaining the main loop. Within the process, the framework can [create multiple widget instances](#app_instance) that can share the same resources.

  The widget application can also [share data](#share) with other applications.

- Managing multiple widget instances

  Whenever a widget instance is requested, the framework creates one. You can manage the widget instances by updating or destroying them, or by retrieving information about them.

- Managing the life-cycle

  You can manage the [widget instance](#instance) life-cycle through callback methods that are triggered as the instance state changes.

- Creating the widget UI

  The widget application can [draw a UI on the home screen](#get_window).


  > **Note**   
  > The widget application UI has a limitation with the scroll action to provide a better user experience. Design the widget UI to display all the information within the given area of the screen points.
  >
  > To draw the UI, use a single window as a protected property of the [Tizen.Applications.WidgetBase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetBase.html) class. Do not create additional windows. A stack of widget application windows gets corrupted, because the platform handles the widget application window in a special way.


<a name="app_instance"></a>
## Widget Application and Widget Instance

The [Tizen.Applications.WidgetApplication](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetApplication.html) class provides the `WidgetApplication(IDictionary< Type, string > typeInfo)` constructor, which allows a widget application to have multiple widget classes. The widget applications with multiple classes can make diverse class instances whenever widget viewer applications, such as the home screen and the lock screen, request for a widget instance.

The widget instance has its own life-cycle similar to the widget application. However, the widget instance is only an object shown by the widget viewer applications. Many widget instances can be running on the same widget application process.

**Figure: Each widget application has 1 or more widget instances**

![Each widget application has 1 or more widget instances](./media/widget_homescreen.png)

<a name="instance"></a>
## Widget Instance States and Events

The following figure illustrates the widget instance states during the instance life-cycle:

- When the application is in the Ready state, the instance does not exist.
- When the instance is created, it is in the Created state.
- When the instance is visible, it is in the Running state.
- When the instance is invisible, it is in the Paused state.
- When the instance is destroyed, it is in the Destroyed state.

**Figure: Widget instance life-cycle**

![Widget instance life-cycle](./media/csharp_widgetapplication.png)

The following table lists the [callbacks you can use as the instance state changes](#life-cycle).

**Table: Instance state change callbacks**

| Callback      | Description                              |
|---------------|------------------------------------------|
| `OnCreate()`  | Called after the widget instance is created. |
| `OnDestroy()` | Called before the widget instance is destroyed. |
| `OnPause()`   | Called when the widget is invisible.     |
| `OnResume()`  | Called when the widget is visible.       |
| `OnResize()`  | Called before the widget size is changed. |
| `OnUpdate()`  | Called when an event for updating the widget is received. |

You can declare a widget class by inheriting the [Tizen.Applications.WidgetBase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetBase.html) class. For example:

```
class MyWidget : WidgetBase
{
    public override void OnCreate(Bundle content, int w, int h) {}

    public override void OnPause() {}

    public override void OnResume() {}

    public override void OnResize(int w, int h) {}

    public override void OnUpdate(Bundle content, bool isForce) {}

    public override void OnDestroy(WidgetBase.WidgetDestroyType reason, Bundle content) {}
}
```

## Prerequisites

To enable your application to use the widget functionality:

1. To use the methods and properties of the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace, include it in your application:

   ```
   using Tizen.Applications;
    ```

2. Edit the widget application settings in the [manifest](../../../vstools/tools/manifest-editor.md#widget_app) file.

<a name="create"></a>
## Creating the Widget Application

The widget application starts with the `Main()` function, which creates and initializes the application. The `Run()` method of the [Tizen.Applications.WidgetApplication](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetApplication.html) class is used to start the application event loop.

The `Tizen.Applications.WidgetApplication` class provides 2 kinds of constructors:

- If you create the widget application with the `WidgetApplication(Type type)` constructor, that widget application's ID is the same as the application ID.
- Using the `WidgetApplication(IDictionary<Type, string> typeInfo)` constructor, you can make widget applications with multiple widget classes.

A widget viewer application can add the widget application by using the widget application ID.

```
class Program
{
    static void Main(string[] args)
    {
        Elementary.Initialize();
        Elementary.ThemeOverlay();
        WidgetApplication app = new WidgetApplication(typeof(MyFirstWidget));
        WidgetApplication app = new WidgetApplication(new Dictionary<Type, string>()
        {
            {typeof(MySecondWidget), "second@org.tizen.MyWidget"}
        });
        app.Run(args);
    }
}
```

<a name="life-cycle"></a>
## Managing the Widget Instance Life-cycle

To manage the widget instance life-cycle:

1. Define your widget class, which is inherited from the [Tizen.Applications.WidgetBase](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetBase.html) class:

   ```
   class MyWidget : WidgetBase {}
   ```

2. Override the event callback methods of your new class:
   - The `OnCreate()` callback is triggered when the widget instance is created.

     Initialize resources for this widget instance and [draw the UI](#get_window). If bundle content is not `NULL`, restore the previous status.

     ```
     public override void OnCreate(Bundle content, int w, int h)
     {
	     try
	     {
		     base.OnCreate(content, w, h);
		     /// Recover the previous status with the bundle object
		     /// Create the UI
	     }
	     catch (Exception e)
	     {
		     Log.Warn(_logTag, "exception " + e);
	     }
     }
     ```

   - The `OnDestroy()` callback is triggered when the widget instance is destroyed.

     Release all widget resources. If the `reason` for the termination is not `WidgetBase.WidgetDestroyType.Permanent`, store the current status with the incoming bundle.

     ```
     public override void OnDestroy(WidgetBase.WidgetDestroyType reason, Bundle content)
     {
	     if (reason != WidgetBase.WidgetDestroyType.Permanent)
		     /// Save the current status at the bundle object
     }
     ```

   - The `OnPause()` callback is triggered when the widget instance is paused.

     Take the necessary actions when the widget instance becomes invisible. The framework can destroy a paused widget instance.

     ```
     public override void OnPause() {}
     ```

   - The `OnResume()` callback is triggered when the widget instance is resumed.

      Take the necessary actions when the widget instance becomes visible.

      ```
      public override void OnResume() {}
      ```

   - The `OnResize()` callback is triggered before the widget instance is resized.

      Take the necessary actions to accommodate the new size.

      ```
      public override void OnResize(int w, int h) {}
      ```

   - The `OnUpdate()` callback is triggered when a widget update event is received.

      Take the necessary actions for the widget update. If the `isForce` parameter is `true`, the widget can be updated even in the pause state.

      ```
      public override void OnUpdate(Bundle content, bool isForce) {}
      ```

<a name="get_window"></a>
## Drawing the Widget UI

The widget UI is drawn in the `OnCreate()` callback of your widget class:

```
public override void OnCreate(Bundle content, int w, int h)
{
    try
    {
        base.OnCreate(content, w, h);
        Conformant conformant = new Conformant(Window);
        conformant.Show();
        Scroller scroller = new Scroller(Window)
        {
            AlignmentX = -1,
            AlignmentY = -1,
            WeightX = 1,
            WeightY = 1,
            ScrollBlock = ScrollBlock.None,
        };
        scroller.Show();

        Box box = new Box(Window)
        {
            AlignmentX = -1,
            AlignmentY = -1,
            WeightX = 1,
            WeightY = 1,
        };
        box.Show();
        scroller.SetContent(box);
        conformant.SetContent(scroller);

        Button exitButton = new Button(Window)
        {
            Text = "Exit Test",
            AlignmentX = -1,
            AlignmentY = -1,
            WeightX = 1,
            WeightY = 1
        };
        box.PackEnd(exitButton);
        exitButton.Show();
    }
    catch (Exception e)
    {
        Log.Warn(_logTag, "exception " + e);
    }
}
```

<a name="share"></a>
## Data Sharing Between the Widget Application and Other Applications

You can share data between widget applications and UI (or service) applications. However, you must understand that this kind of data sharing is dependent on the file system. The reason is that the system (home screen) controls the widget application life-cycle, while the UI application life-cycle is mostly explicitly controlled by the user.

For example, consider the differences between a Weather application and a Weather widget:

- The Weather application is launched when the user selects it from the application list.
- The widget is launched when the home screen is on screen and is terminated when the home screen is hidden.

Although the widget wants to share some data from the Weather application (such as the user's favorite city), it is ineffective for the widget to launch the Weather application every time to retrieve such data. This inefficiency makes it difficult to use typical IPC mechanisms, such as sockets and [message ports](message-port.md), for which both the receiver and sender processes must be alive. To overcome this limitation, the widget application must use a communication method that stores data permanently somewhere in the system.

In the Tizen platform, applications in the same package (including widget applications) can access files in the `data` directory of the package installation path. This means that the UI (or service) application can first write files to the `data` directory, and the widget can later read them, or vice versa.

**Figure: Sharing through the data directory**

![Sharing through the data directory](./media/widget_data_share.png)

To manage data through the `data` directory, you can use the methods and properties of the [Tizen.Applications.Preference](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Preference.html) class to store and retrieve key-value pairs.

If an application requires complex control over a widget, such as Music Player, it must implement a service application in the middle and use a data control with the classes and methods of the [Tizen.Applications.DataControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.DataControl.html) namespace.

For example, a music-player-service service application is needed to control the audio device, process audio files, and handle play and stop signals. The music-player-ui and music-player-widget applications display the UI controls, title, album art, and other content retrieved from the music-player-service service application. The service application can export its data using the data control to [provide data to the other applications](data-control.md) (widget and UI) simultaneously. The following figure illustrates the typical data control flows between the set of UI, service, and widget applications.

**Figure: Sharing through data control**

![Sharing through data control](./media/widget_data_control_share.png)


## Related Information
- Dependencies
  - Tizen 4.0 and Higher
