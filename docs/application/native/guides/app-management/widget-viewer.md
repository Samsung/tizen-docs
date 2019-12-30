# EFL Widget Viewer


The widget viewer API provides functionality that display and manage Tizen native widget applications.

The main features of the Widget Viewer Application API include:

- Displaying widgets

  You can create widget objects, which will [display a widget](#display) application's buffer. The buffer is updated when the widget application updated its own window.

- Managing widget life-cycles

  You can [manage created widget applications' life-cycles](#manage_lifecycle).

- Retrieving widget information

  You can [retrieve created widget applications' information](#retrieve_information).



## Prerequisites

To enable your application to use the widget viewer functionality:

1.  To use the widget viewer API (in [mobile](../../api/mobile/latest/group__CAPI__WIDGET__VIEWER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__WIDGET__VIEWER__MODULE.html) applications), the application has to request permission. Add the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/widget.viewer</privilege>
    </privileges>
    ```

2.  To use the functions of the widget viewer API, include the `<widget_viewer_evas.h>` header file in your application:

    ```
    #include <widget_viewer_evas.h>
    ```

<a name="display"></a>
## Display widgets

To display widget application's buffer you have to create widget object which will be the sharing point of the widget application's buffer.

1. Initialize widget viewer with the `widget_viewer_evas_init()` function. Its parameter is an application's window object.

   ```
   Evas_Object *win = elm_win_add(NULL, "VIEWER", ELM_WIN_BASIC);
   int ret = widget_viewer_evas_init(win);
   ```

2. Create widget object with the `widget_viewer_evas_add_widget()` function. Its parameters are parent Evas_Object, widget id (the widget application's appid or class id), content info (Bundle encoded data which contains extra information about widget developer can retrieve it using `widget_viewer_evas_get_content_info`), and widget update period.


   ```
   const char *content_info;
   bundle_raw *raw;
   int len;

   bundle_encode(data, &raw, &len);
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   evas_object_resize(widget, 100, 100);
   evas_object_show(widget);
   ```

3. Finalize widget viewer functionality with the `widget_viewer_evas_fini()` function.

   ```
   int ret = widget_viewer_evas_fini();
   ```

<a name="manage_lifecycle"></a>
## Manage widget lifecycles

After displaying widget, you can manage the widget application's lifecycle as shown in the following code.

1. Resume widget application's instance using an `widget_viewer_evas_resume_widget()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   int ret = widget_viewer_evas_resume_widget(widget);
   ```

2. Pause widget application's instance using an `widget_viewer_evas_pause_widget()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   int ret = widget_viewer_evas_pause_widget(widget);
   ```

3. Resume/Pause all the widget instances displayed by the widget viewer application using `widget_viewer_evas_notify_resumed_status_of_viewer()` and `widget_viewer_evas_notify_paused_status_of_viewer()` functions.

   ```
   int ret = widget_viewer_evas_notify_resumed_status_of_viewer();
   ret = widget_viewer_evas_notify_paused_status_of_viewer();
   ```

<a name="retrieve_information"></a>
## Retrieve widget information

After displaying widget, you can retrieve information about widget instances as shown in the following code.

1. Get content information using an `widget_viewer_evas_get_content_info()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   const char *content = widget_viewer_evas_get_content_info(widget);
   ```

2. Get widget id from the widget object using an `widget_viewer_evas_get_widget_id()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   const char *widget_id = widget_viewer_evas_get_widget_id(widget);
   ```

3. Get widget update period from the widget object using an `widget_viewer_evas_get_period()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   double period = widget_viewer_evas_get_period(widget);
   ```

4. Get widget instance id from the widget object using an `widget_viewer_evas_get_widget_instance_id()` function. Its parameter is an widget object created by the `widget_viewer_evas_add_widget` function.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   const char *instance_id = widget_viewer_evas_get_widget_instance_id(widget);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
