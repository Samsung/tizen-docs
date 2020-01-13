# EFL Widget Viewer


The widget viewer API provides functionality that displays and manages Tizen native widget applications.

The main features of the widget viewer application API include:

- Displaying widgets

  You can create widget objects that can [display a widget](#display) application's buffer. The buffer is updated when the widget application updates its window.

- Managing widget life-cycle

  You can [manage the instance life-cycle](#manage_life-cycle) of a created widget application.

- Retrieving widget information

  You can [retrieve the created widget application's information](#retrieve_information).



## Prerequisites

To enable your application to use the widget viewer functionality:

1.  To use the widget viewer API (in [mobile](../../api/mobile/latest/group__CAPI__WIDGET__VIEWER__EVAS__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__WIDGET__VIEWER__EVAS__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

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
## Display Widgets

To display widget application's buffer you have to create widget object which will be the sharing point of the widget application's buffer. You can create the widget object as shown in the following code.

1. Initialize widget viewer using `widget_viewer_evas_init()`. The parameter of `widget_viewer_evas_init()` is the window object of an application:

   ```
   Evas_Object *win = elm_win_add(NULL, "VIEWER", ELM_WIN_BASIC);
   int ret = widget_viewer_evas_init(win);
   ```

2. Create a widget object using `widget_viewer_evas_add_widget()`. The parameters of `widget_viewer_evas_add_widget()` are parent Evas_Object, widget ID, content information, and widget update period. The widget ID is the widget application's app ID or class ID. Content information is the bundle encoded data, which contains extra information on the widget. You can retrieve the content information using `widget_viewer_evas_get_content_info()`:


   ```
   const char *content_info;
   bundle_raw *raw;
   int len;

   bundle_encode(data, &raw, &len);
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   evas_object_resize(widget, 100, 100);
   evas_object_show(widget);
   ```

3. Finalize widget viewer functionality using `widget_viewer_evas_fini()`:

   ```
   int ret = widget_viewer_evas_fini();
   ```

<a name="manage_life-cycle"></a>
## Manage widget life-cycle

After displaying a widget, you can manage the widget application's lifecycle:

1. Create widget object with `widget_viewer_evas_add_widget()`.

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   ```

2. Resume the instance of a widget application using `widget_viewer_evas_resume_widget()`. The parameter of `widget_viewer_evas_resume_widget()` is a widget object created by `widget_viewer_evas_add_widget()`:

   ```
   int ret = widget_viewer_evas_resume_widget(widget);
   ```

3. Pause an instance of a widget application instance using `widget_viewer_evas_pause_widget()`. The parameter of `widget_viewer_evas_pause_widget()` is a widget object created by `widget_viewer_evas_add_widget()`:

   ```
   int ret = widget_viewer_evas_pause_widget(widget);
   ```

4. Resume or pause all the widget instances displayed by the widget viewer application using `widget_viewer_evas_notify_resumed_status_of_viewer()` and `widget_viewer_evas_notify_paused_status_of_viewer()`:

   ```
   int ret = widget_viewer_evas_notify_resumed_status_of_viewer();
   ret = widget_viewer_evas_notify_paused_status_of_viewer();
   ```

<a name="retrieve_information"></a>
## Retrieve Widget Information

After displaying widget, you can retrieve information about widget instances as shown in the following code.

1. Get the content information using `widget_viewer_evas_get_content_info()`. The parameter of `widget_viewer_evas_get_content_info()` is a widget object created by widget_viewer_evas_add_widget:

   ```
   Evas_Object *widget = widget_viewer_evas_add_widget(win, "widget_id", (const char *)raw, 0.0);
   const char *content = widget_viewer_evas_get_content_info(widget);
   ```

2. Get widget ID from the widget object using `widget_viewer_evas_get_widget_id()`. The parameter for `widget_viewer_evas_get_widget_id()` is a widget object created by `widget_viewer_evas_add_widget()`:

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
