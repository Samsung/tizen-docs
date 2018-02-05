# Configuring UI Components

When configuring UI components, you can manage Elementary profiles and Elementary options.

## Managing Elementary Profiles

An Elementary profile is a set of preconfigured options that affects the entire look and feel of an application. The options linked to a specific profile form an Elementary configuration, which can be used to store the desired set of options for use in multiple sessions. Once loaded, the Elementary profile configures all the options and sets the look and feel of your Elementary application.

To manage Elementary profiles:

- List the existing profiles:

  ```
  Eina_List *list = elm_config_profile_list_get();
  ```

- Set a particular profile:

  ```
  elm_config_profile_set("myprofile");
  ```

- Get the current profile:

  ```
  char *profile = elm_config_profile_get();
  ```

- To reload the Elementary configuration saved for the current profile:

  ```
  elm_config_reload();
  ```

## Configuring Elementary Options

The following code snippet is a configuration example from the `base.src` configuration file:

```
group "Elm_Config" struct {
   value "scale" double: 3.0;
   value "finger_size" int: 50;
   value "cache_flush_enable" uchar: 0;
   value "cache_flush_poll_interval" int: 512;
   value "font_cache" int: 512;
   value "image_cache" int: 4096;
   value "edje_cache" int: 32;
   value "edje_collection_cache" int: 64;
   value "glayer_long_tap_start_timeout" double: 0.5;
   value "glayer_double_tap_timeout" double: 0.33;
   value "thumbscroll_bounce_enable" uchar: 0;
   value "thumbscroll_bounce_friction" double: 0.5;
   value "longpress_timeout" double: 0.5;
   value "tooltip_delay" double: 1.0;
   value "password_show_last" uchar: 1;
   value "password_show_last_timeout" double: 2.0;
   value "engine" string: "software_x11";
   value "selection_clear_enable" uchar: 1;
   value "fps" double: 60.0;
}
```

You can set the following options in the Elementary configuration:

- To scale UI components:

  You can configure [UI component scaling](ui-scalability.md) in terms of both interactive and readable areas:

  - Set the global scaling factor (for example, setting it to 2.0 doubles the size of all scalable UI components):

    ```
    elm_config_scale_set(2.0);
    ```

  - Set the finger size:

    ```
    elm_config_finger_size_set(1.5);
    ```

- To manage caches:

  - Enable the globally configured cache flush, and set the flush interval (in this example, to 60 seconds):

    ```
    elm_config_cache_flush_enabled_set(EINA_TRUE);
    elm_config_cache_flush_interval_set(60);
    ```

  - Configure the font and image cache sizes (to 500 and 5 000 000 bytes, respectively):

    ```
    elm_config_cache_font_cache_size_set(500);
    elm_config_cache_image_cache_size_set(5000000);
    ```

  - Set the Edje collection and Edje file cache sizes:

    ```
    elm_config_cache_edje_file_cache_size_set(500);
    elm_config_cache_edje_collection_cache_size_set(500);
    ```

- To configure the gesture layer:

  You can set the duration of the long tap and double tap events on the gesture layer objects. The following example sets the duration to 500 ms.

  ```
  elm_config_glayer_long_tap_start_timeout_set(0.5);
  elm_config_glayer_double_tap_timeout_set(0.5);
  ```

- To manage scrolling:

  - Make the scroller bounce when it reaches its viewport's edge during scrolling by using the `elm_config_scroll_bounce_enabled_set()` function:

    ```
    elm_config_scroll_bounce_enabled_set(EINA_TRUE);
    ```

  - Control the inertia of the bounce animation by using the `elm_config_scroll_bounce_friction_set()` function:

    ```
    elm_config_scroll_bounce_friction_set(0.5);
    ```

    You can also set the friction for a page scroll, include animations, and zoom animations.

  - Set the scroller to be draggable by using the `elm_config_scroll_thumbscroll_enabled_set()` function. You can configure several drag options, such as friction, sensitivity, acceleration, and momentum.  

  The following example sets the scroller to be draggable, defines that the number of pixels one must travel while dragging the scroller view to actually trigger scrolling is 20 pixels.

    ```
    elm_config_scroll_thumbscroll_enabled_set(EINA_TRUE);
    elm_config_scroll_thumbscroll_threshold_set(20);
    ```

- To configure long-press events:

  Get the current timeout before a long-press event is retrieved, and modify it. The following example increases the timeout by 1 second.

  ```
  double lp_timeout = elm_config_longpress_timeout_get();
  elm_config_longpress_timeout_set(lp_timeout + 1.0);
  ```

- To configure tooltips:

  Set the duration after which a tooltip is shown. The following example sets the delay to 2 seconds.

  ```
  elm_config_tooltip_delay_set(2.0);
  ```

- To configure the password show last feature:

  The password show last feature enables the user to view the last input entered for a few seconds before it is masked.

  - Enable the password show last feature:

    ```
    elm_config_password_show_last_set(EINA_TRUE);
    ```

  - Set the visibility timeout (how many seconds the input is visible):

    ```
    elm_config_password_show_last_timeout_set(5.0);
    ```

- To set the Elementary engine:

  You can define the rendering engine that Elementary uses to draw the windows. The following rendering engines are supported:

  - "software_x11"
  - "fb"
  - "directfb"
  - "software_16_x11"
  - "software_8_x11"
  - "xrender_x11"
  - "opengl_x11"
  - "software_gdi"
  - "software_16_wince_gdi"
  - "sdl"
  - "software_16_sdl"
  - "opengl_sdl"
  - "buffer"
  - "ews"
  - "opengl_cocoa"
  - "psl1ght"

  ```
  elm_config_engine_set("opengl_x11");
  ```

- To activate the access mode:

  Set the access mode as active, so that information about an Elementary object is read when the object receives an `EVAS_CALLBACK_MOUSE_IN` event.

- To configure the selection mode:

  Set the selection mode so that the selection is cleared when the entry component is unfocused:

  ```
  elm_config_selection_unfocused_clear_set(EINA_TRUE);
  ```

- To enable mirroring:

  Elementary allows UI mirroring both on a single object and on the entire UI. If mirroring is enabled, an Elementary UI component displays as if there was a vertical mirror in the middle of it. Only the controls and the disposition of the UI component are mirrored. Text is not mirrored.

     By default, UI mirroring is automatically enabled or disabled according to the system language. To manually apply UI mirroring:

    1.  Disable the automatic mirroring:

        ```
        elm_config_language_auto_mirrored_set(EINA_FALSE);
        ```

    2.  Manually enable or disable UI mirroring by using the `elm_config_mirrored_set()` function:

        ```
        elm_config_mirrored_set(EINA_TRUE);
        ```

- To set the frame rate:

  Define the frames per second (FPS) value for the `ecore_animator_frametime` and `edje_frametime` calculations. This example sets the FPS 60.

  ```
  elm_config_fps_set(60.0);
  ```

## Related Information
- Dependencies  
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
