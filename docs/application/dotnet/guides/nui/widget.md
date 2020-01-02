# NUI Widget Application

[NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html)  is to show a small version of application on home screen.

**Figure: NUI widget application**

![NUI widget application](./media/dali_widget_application.png)

<br>
The main widget application features include:

- Creating widget applications

  You can [Create a NUI Widget Application](#create-a-nui-widget-application)
, which usually has 1 process for maintaining the main loop. Within the process, the framework can be create widget instance that can share the same resources.
  The Widget application can also share data with other applications.

- Managing widget instances
  
  Whenever a widget instance is requested, the framework creates one.
  You can manage the widget instances by updating or destroying them, or by retrieving information about them.

- Managing the life-cycle
  
  You can manage the widget instance life-cycle through callback methods that are triggered as the instance state changes.

- Creating the widget UI

  The widget application can draw a UI on the Home screen or viewer


    > **Note**
    >
    > The widget application UI has a limitation with the scroll action to provide a better user experience. Design the widget UI to display all the information within the given area of the screen points.
    >
    > To draw the UI, you must use the [Window](https://developer.tizen.org/dev-guide/csapi/api/Tizen.NUI.Window.html) received from the OnCreate Callback.  Do not create additional windows. A stack of widget application windows gets corrupted, because the platform handles the widget application window in a special way.

## Application and Viewer

[NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) can make diverse class instances whenever [WidgetView](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.WidgetView.html) request for a widget instance.<br>

The widget instance has its own life-cycle similar to the widget application. However, the widget instance is only an object shown by the widget viewer applications. Many widget instances can be running on the same widget application process.

> **Note**
>
>The case to use many widget instances in one widget application is called multi-instance.
> In some devices, this feature may not supported. If the device does not support multi-instance,an error message is displayed.

[WidgetView](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.WidgetView.html)
shows the contents drawn by Widget on the screen.<br>
WidgetView may receive a value from the widget.<br>

[Create a NUI Widget Application](#create-a-nui-widget-application), [Create a NUI Widget View](#create-a-nui-widget-view), and use widgets.

## Instance States and Events
The following figure illustrates the widget instance states during the instance life-cycle:


**Figure: NUI widget flow**

![NUI widget flow](./media/WidgetInstanceFlow.png)

`Widget` class provides interface for creating custom widget.

The table list the main functions to manage widget instance:

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

Most of functions are used for managing widget instance lifecycle. You can describe what will be done on each lifecycle functions.

Widget instance can send data to widget viewer application using `SetContentInfo()` function. If you want to save the current state of widget before deleting it, view the current state of the widget and delete it.

## Create a NUI Widget Application

If you want to use NUI for your widget application, you must create the application with the [NUI Widget Application](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class. 

The steps to create a NUI widget application:
1. To use the methods and properties of the [Tizen.NUI](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.html) namespace, include it in your application.

   ```csharp
   using Tizen.NUI;
   ```

2. Define your widget application class, which is inherited from the [NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class:

   ```csharp
   class Program : NUIWidgetApplication
   ```
3. The widget application starts with the `Main()` function, which creates and initializes the application. The `Run()` method of the [NUIWidgetApplication](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.NUIWidgetApplication.html) class is used to start the application event loop.

   The `NUIWidgetApplication` class provides 2 kinds of constructors:
   - Using the `NUIWidgetApplication(Type type)` constructor, that widget application's ID is the same as the application ID.
      ```csharp
        static void Main(string[] args)
        {
            var app = new program(typeof(MyWidget));
            app.Run(args);
        }    
      ```

   - Using the `NUIWidgetApplication(Dictionary< Type, string > typeInfo) ` constructor, you can make widget applications with multiple widget classes.

      - For using multiple widget classes, Information of widget-class must also be added to XML.
          ```XML
            <widget-class classid="second" update-period="0">
            <support-size preview="Widget.png">4x4</support-size>
          < /widget-class>
          ```
      - Using constructor as follows
        ```csharp
        static void Main(string[] args)
        {
           Dictionary<System.Type, string> widgetSet = new Dictionary<Type, string>();
            widgetSet.Add(typeof(MyWidget), "second@org.tizen.example.WidgetTemplate");
            var app = new Program(widgetSet);
            app.Run(args);
        }    
        ```
      
    

4. Define your widget class, which is inherited from the [Widget](https://samsung.github.io/TizenFX/latest/api/Tizen.NUI.Widget.html)

   ```csharp
   class MyWidget : Widget
   ```

   

5. Overide the event callback methods of your new class:

  - The `OnCreate()` callback is triggered when the widget instance is created.

     Initialize resources for this widget instance and draw the UI.

   
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
      protected override void OnUpdate(string contentInfo, int force)
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
1. Add privileges for viewer to tizen-manifest.xml

```XML
  <privileges>
    <privilege>http://tizen.org/privilege/widget.viewer</privilege>
    <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
  </privileges>
```
2. Create widget manager and request add widget to widget manager

- Using the `NUIWidgetApplication(Type type)` constructor, add a widget using widget app ID.
```csharp
protected override void OnCreate()
{
  WidgetViewManager widgetViewManager = new WidgetViewManager(this, this.ApplicationInfo.ApplicationId);

  WidgetView myWidgetView = widgetViewManager.AddWidget("org.tizen.example.Widget", encodedBundle, width, height, 0);
  Window.Instance.GetDefaultLayer().Add(myWidgetView);
```

- Using the `NUIWidgetApplication(Dictionary< Type, string > typeInfo) ` constructor, add a widget using class and app ID
```csharp
protected override void OnCreate()
{
  WidgetViewManager widgetViewManager = new WidgetViewManager(this, this.ApplicationInfo.ApplicationId);

  WidgetView myWidgetVie1 = widgetViewManager.AddWidget("second@org.tizen.example.Widget", encodedBundle, width, height, 0);
  Window.Instance.GetDefaultLayer().Add(myWidgetView);
```

## Related Information
- Dependencies
  - Tizen 5.5 and Higher for Mobile
  - Tizen 5.5 and Higher for Wearable
