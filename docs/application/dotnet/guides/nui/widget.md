# NUI Widget Application

[NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) helps you to create Tizen.NET widget applications, which are small versions of Tizen.NET applications on the home screen.
You can launch these applications on the home screen when you select them in the **Add Widget** menu.

**Figure: NUI widget application**

![NUI widget application](./media/dali_widget_application.png)

The main features of NUIWidgetApplication include:

- Create widget applications

  You can [create a NUI widget application](#create-a-nui-widget-application), which usually is composed of one process having the main loop. The NUIWidgetApplication framework enables you to create a widget instance that shares the same resources within the process. The widget application can also share data with other applications.

- Manage the life-cycle

  You can manage the life-cycle of widget instances through callback methods that are triggered as the instance states are changed.

- Manage widget instances
  
  Whenever a widget instance is requested, the framework creates one.
  You can manage the widget instances by updating or destroying them, or by retrieving information about them.

- Create the widget UI

  The widget application can create a user interface that appears on the home screen or viewer.

    > **Note**
    >
    > The UI of widget application limits scroll actions to provide a better user experience. It is recommended that you design a UI layout within the given screen size.
    >
    > To draw the layout, you must use the [`Window`](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.Window.html) instance received from the `OnCreate` callback. If you create additional windows, the stack of widget application windows gets corrupted. This is because the platform handles the widget application window in a particular way.

## Application and Viewer

[`NUIWidgetApplication`](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) makes diverse class instances whenever [`WidgetView`](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.WidgetView.html) requests for a widget instance.

The widget instance has its own life-cycle similar to that of the widget application. However, the widget instance is an object created by the widget viewer application. Many widget instances can be running on a widget application process.

>**Note**
>
>The case to use many widget instances in one widget application is known as multi-instance. In some devices, the multi-instance may not be supported. If a device does not support multi-instance, an error message is displayed.

[`WidgetView`](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.WidgetView.html) shows the contents drawn by [`Widget`](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.Widget.html) on the screen.

To sum up, you [create a NUI WidgetApplication](#create-a-nui-widget-application), [create a NUI WidgetView](#create-a-nui-widget-view), and use Widget to view layout on the screen.

## Instance States and Events
The following figure illustrates the widget instance states during the instance life-cycle:

**Figure: NUI widget flow**

![NUI widget flow](./media/WidgetInstanceFlow.png)

The `Widget` class provides interface for creating custom widget.

The following table lists the main functions to manage the widget instance:

**Table: Main functions**

| Function           | Description                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------|
| `OnCreate()`       | This function is called after the widget instance is created.                                 |
| `OnTerminate()`    | This function is called after the widget instance is terminated.                              |
| `OnPause()`        | This function is called when the widget is invisible.                                         |
| `OnResume()`       | This function is called when the widget is visible.                                           |
| `OnResize()`       | This function is called before the widget size is changed.                                    |
| `OnUpdate()`       | This function is called when an event for updating the widget is received.                    |
| `SetContentInfo()` | This function sends data about current state of widget instance to a widget viewer application. |

Most of functions are used for managing widget instance life-cycle. You can describe what will be done on each lifecycle functions.

Widget instance can send data to widget viewer application using `SetContentInfo()` function. If you want to save the current state of widget before deleting it, you can transmit the current status to the viewer using `SetContentInfo()`.

## Create a NUI Widget Application

If you want to use NUI for your widget application, you must create the application with the [NUI Widget Application](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class. 

To create a NUI widget application:
1. To use the methods and properties of the [Tizen.NUI](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.html) namespace, include the following code:

   ```csharp
   using Tizen.NUI;
   ```

2. Define your widget application class, which is inherited from the [NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class:

   ```csharp
   class Program : NUIWidgetApplication
   ```
3. The widget application starts with the `Main()` function, which creates and initializes the application. The `Run()` method of the [NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class is used to start the application event-loop.

   The `NUIWidgetApplication` class provides two kinds of constructors:
   - For using the `NUIWidgetApplication(Type type)` constructor, in case that widget application's ID is the same as the application ID.
      ```csharp
        static void Main(string[] args)
        {
            var app = new program(typeof(MyWidget));
            app.Run(args);
        }    
      ```

   - For using the `NUIWidgetApplication(Dictionary< Type, string > typeInfo) ` constructor, in case that your widget applications has multiple widget classes.

      For multiple instances, add `<widget-class>` in XML as follow:
        ```XML
          <widget-class classid="second" update-period="0">
            <support-size preview="Widget.png">2x2</support-size>
          </widget-class>
        ```
      And then edit code as follow:
        ```csharp
        static void Main(string[] args)
        {
           Dictionary<System.Type, string> widgetSet = new Dictionary<Type, string>();
            widgetSet.Add(typeof(MyWidget), "second@org.tizen.example.WidgetTemplate");
            var app = new Program(widgetSet);
            app.Run(args);
        }    
        ```

4. Define your widget class, which is inherited from [Widget](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.Widget.html)

   ```csharp
   class MyWidget : Widget
   ```

   

5. Overide event callback methods of your new class:
    ```csharp
    class MyWidget : Tizen.NUI.Widget
    {
      protected override void OnCreate(string contentInfo, Window window)
      {
        /// Create the UI
        /// ....
        base.OnCreate(contentInfo, window);
      }
    }
    ```

    The `Widget` class provies the following callback:

    - The `OnCreate()` callback is triggered when the      widget instance is created.

      Initialize resources for this widget instance and draw wldthe UI.

    - The `OnTerminate()` callback is triggered when the widget instance is terminated.

      ```csharp
      protected override void OnTerminate(string contentInfo, TerminationType type)
      ```

    - The `OnPause()` callback is triggered when the widget instance is paused.


      Take the necessary actions when the widget instance becomes invisible. The framework can destroy a paused widget instance.

      ```csharp
      protected override void OnPause()
      ```

    - The `OnResume()` callback is triggered when the widget instance is resumed.

      Take the necessary actions when the widget instance becomes visible.

      ```csharp
      protected override void OnResume()
      ```

    - The `OnResize()` callback is triggered when the widget instance is resized.

      Take the necessary actions to accommodate the new size.
      ```csharp
      protected override void OnResize(Window window)
      ```

    - The `OnUpdate()` callback is triggered when a widget update event is received. 

      Take the necessary actions for the widget update. If the isForce parameter is true, the widget can be updated even in the pause state.
      ```csharp
      protected override void OnUpdate(string contentInfo, int isForce)
      ```

6. Drawing the Widget UI in OnCreate()

    The widget UI is drawn in the `OnCreate()` callback of your widget class:

    ```csharp
    protected override void OnCreate(string contentInfo, Window window)
    {
        View rootView = new View();
        rootView.BackgroundColor = Color.White;
        rootView.Size2D = window.Size;
        rootView.PivotPoint = PivotPoint.Center;
        window.GetDefaultLayer().Add(rootView);

        TextLabel sampleLabel = new TextLabel("Hello World!");
        sampleLabel.FontFamily = "SamsungOneUI 500";
        sampleLabel.PointSize = 71;
        sampleLabel.TextColor = Color.Black;
        sampleLabel.SizeWidth = 200;
        sampleLabel.PivotPoint = PivotPoint.Center;

        rootView.Add(sampleLabel);
    }
    ```

## Create a NUI Widget View

If necessary, you can create a Widget Viewer that shows UI drawn by Widget

The steps to create a nui widget view:<br>
1. Add privileges for viewer to `tizen-manifest.xml`:

  ```XML
    <privileges>
      <privilege>http://tizen.org/privilege/widget.viewer</privilege>
      <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
    </privileges>
  ```
2. Create widget manager and request add widget to widget manager

    You can create a widget manager using two different constructors:
    - The `NUIWidgetApplication(Type type)` constructor for adding a widget using the widget app ID.
      ```csharp
      protected override void OnCreate()
      {
        WidgetViewManager widgetViewManager = new WidgetViewManager(this, this.ApplicationInfo.ApplicationId);

        WidgetView myWidgetView = widgetViewManager.AddWidget("org.tizen.example.Widget", encodedBundle, width, height, 0);
        Window.Instance.GetDefaultLayer().Add(myWidgetView);
        ...
      }
      ```

    - The `NUIWidgetApplication(Dictionary< Type, string > typeInfo) ` constructor for adding a widget using class and app ID.

      ```csharp
      protected override void OnCreate()
      {
        WidgetViewManager widgetViewManager = new WidgetViewManager(this, this.ApplicationInfo.ApplicationId);

        WidgetView myWidgetVie1 = widgetViewManager.AddWidget("second@org.tizen.example.Widget", encodedBundle, width, height, 0);
        Window.Instance.GetDefaultLayer().Add(myWidgetView);
        ...
      ```

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
