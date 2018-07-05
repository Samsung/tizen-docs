# Input Method


The input method editor (IME) is an input panel (keyboard) that lets the user input text and the platform receive the entered data. The user can [select an IME as their default keyboard in the device Settings application](#manager).

You can create a Tizen native IME application that provides a new IME. You can start the IME application life-cycle, interact with the current IME UI state, and retrieve attributes and events.

The main features of the Input Method API include:

- Managing the IME life-cycle

  The system can have multiple keyboards, and the user can choose which one to use as the default keyboard. The IME application [starts its life-cycle](#start) when it is selected as the default keyboard. The following figure shows the IME application life-cycle.

  **Figure: IME application life-cycle**

  ![IME application life-cycle](./media/ime_lifecycle.png)

  The IME application runs as follows:

  1. Once the IME application is started, the `create()` callback function is called.
  2. When a text input UI control gets the focus, the `show()` callback function is called.

     The IME application can call Input Method APIs to interact with the UI control. The event callback functions are called when the UI control state changes. When the text input UI control loses the focus, the `hide()` callback function is called.

  3. When the IME application is finished, the `terminate()` callback function is called.

- Managing the main loop and event callback functions

  The IME application must implement the `ime_app_main()` function. It is the main entry point, in which you can [register event callback functions](#callback) and call the `ime_run()` function to start the main loop.

  During its life-cycle, the IME application can receive a number of events from the Tizen input service framework through the callback functions. You must register the mandatory `create()`, `terminate()`, `show()`, and `hide()` callbacks. Other callbacks can be registered as required by the specific IME application.

- Showing and hiding the keyboard

  When an associated text input UI control has the focus, the active keyboard is requested to be shown. When the text input UI control loses the focus, the keyboard is requested to be hidden.

  The `show()` and `hide()` callback functions are used to manage the keyboard visibility, and the IME application must register both of them when starting the IME main loop.

  The client application can set various configurations for each text input UI control, such as the cursor position, key layout type, return key type, and flags of predictive text. The configurations are delivered to the IME application though the `show()` callback function, to allow the keyboard to show the correct look to the user.

- Using the keyboard option menu

  Each keyboard can [offer its own option menu](#menu) to allow the user to manage the keyboard settings. Nowadays, most platforms provide the keyboard option menu from the device Settings application or from the keyboard directly.

  You can register callback functions that are called when the keyboard option menu opens or closes. These callback functions can be registered before the `ime_run()` function call in the `ime_app_main()` function.

  The device Settings application triggers the callback function to open the keyboard option menu. The keyboard itself can also trigger the callback function to open its option menu.

<a name="manager"></a>
## Input Method Manager

The Input Method Manager (in [mobile](../../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) applications) is a module used to manage the installed IMEs. You can use it to open the installed IME list or selector menu after your IME application is installed, and guide the user to select the installed IME:

- Showing the IME list

  You can [request the installed IME list menu](#list) to be opened. If a new IME has been installed, the user can see its name in the IME list, and can use the toggle button to enable the keyboard they want. All keyboards enabled in the IME list are shown in the IME selector to allow the user to select them as the default keyboard.

  **Figure: IME list**

  ![IME list](./media/ime_list.png)

- Showing the IME selector

  You can [request the IME selector menu](#selector) to be opened. When the user opens the IME selector menu, it shows all the keyboards enabled in the IME list. The user can change the default keyboard by selecting a new one. By clicking **Select keyboard**, the user can return to the IME list menu to enable a new IME.

  **Figure: IME selector**

  ![IME selector](./media/ime_selector.png)

- Checking the IME status

  You can [check whether a specific IME is enabled or disabled](#enable) in the system keyboard setting. You can also check which IME is currently selected as the default keyboard, or how many IMEs are enabled (usable). These features are useful when the user installs a new keyboard.

## Prerequisites

To enable your application to use the input method functionality:

1. To use the Input Method Manager API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/imemanager</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Input Method API (in [mobile](../../api/mobile/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__UIX__INPUTMETHOD__MODULE.html) applications), include the `<inputmethod.h>` header file in your application:

    ```
    #include <inputmethod.h>

    #include <Elementary.h>
    ```

3. To use the functions and data types of the Input Method Manager API, include the `<inputmethod_manager.h>` header file in your application:

    ```
    #include <inputmethod_manager.h>
    ```

<a name="start"></a>
## Starting the IME Life-cycle

To start the IME application life-cycle:

1. Implement the `ime_app_main()` function as the main entry point of IME application:

    ```
    void ime_app_main(int argc, char **argv);
    ```

	The function is called when the user selects the IME as default from the IME selector menu.
2. Inside the `ime_app_main()` function, add the required callbacks and call the `ime_run()` function to start the application:

    ```
    int ime_run(ime_callback_s *basic_cb, void *user_data);
    ```

<a name="callback"></a>
## Adding Event Callbacks

To register and define event callbacks for the IME application:

1. Implement the mandatory callbacks:

   1. You must register the `create()`, `terminate()`, `show()`, and `hide()` callbacks.

      Add the callbacks to the `ime_callback_s` structure (in [mobile](../../api/mobile/latest/structime__callback__s.html) and [wearable](../../api/wearable/latest/structime__callback__s.html) applications), and pass the structure as a parameter to the `ime_run()` function:

      ```
      static void create(void *user_data);
      static void terminate(void *user_data);
      static void show(int context_id, ime_context_h context, void *user_data);
      static void hide(int context_id, void *user_data);

      void
      ime_app_main(int argc, char **argv)
      {
          ime_callback_s basic_callback = {
              create, /* When the input panel is created */
              terminate, /* When the input panel is terminated */
              show, /* When the input panel is shown */
              hide, /* When the input panel is hidden */
          };

          ime_run(&basic_callback, NULL);
      }
      ```

   2. Define the callbacks:

      ```
      static void
      create(void *user_data)
      {
          int portrait_w, portrait_h, landscape_w, landscape_h;
          Evas_Object *ime_win = ime_get_main_window();

          /* Update IME size information */
          ime_set_size(portrait_w, portrait_h, landscape_w, landscape_h);

          /* Create or initialize resources */
      }

      static void
      terminate(void *user_data)
      {
          /* Release the resources */
      }

      static void
      show(int context_id, ime_context_h context, void *user_data)
      {
          Ecore_IMF_Input_Panel_Layout layout;
          ime_layout_variation_e layout_variation;
          int cursor_pos;
          Ecore_IMF_Autocapital_Type autocapital_type;
          Ecore_IMF_Input_Panel_Return_Key_Type return_key_type;
          bool return_key_state, prediction_mode, password_mode;
          Ecore_IMF_Input_Hints input_hint;
          Ecore_IMF_BiDi_Direction bidi;
          Ecore_IMF_Input_Panel_Lang language;

          Evas_Object *ime_win = ime_get_main_window();

          ime_context_get_layout(context, &layout);
          ime_context_get_layout_variation(context, &layout_variation);
          /* Draw the proper layout */

          ime_context_get_autocapital_type(context, &autocapital_type);
          ime_context_get_cursor_position(context, &cursor_pos);
          /* Draw the capital or small characters accordingly */

          ime_context_get_return_key_type(context, &return_key_type);
          ime_context_get_return_key_state(context, &return_key_state);
          /* Draw the proper Return key */

          /* Show the IME window */
          evas_object_show(ime_win);
      }

      static void
      hide(int context_id, void *user_data)
      {
          Evas_Object *ime_win = ime_get_main_window();

          /* Hide the IME window */
          evas_object_hide(ime_win);
      }
      ```

      In the `show()` callback, the IME application can get the contextual information from an associated text input UI control to configure the keyboard state and look accordingly. The contextual information for each input UI control is provided through the `ime_context_get_XXX()` functions defined in the `inputmethod.h` header file.

2. Implementing the optional callbacks, as needed:

   1. You can register optional callbacks with the `ime_event_set_XXX_cb()` functions provided in the `inputmethod.h` header file:

      ```
      static int focus_in(int context_id, void *user_data);
      static int focus_out(int context_id, void *user_data);
      static int cursor_position_updated(int cursor_pos, void *user_data);

      void
      ime_app_main(int argc, char **argv)
      {
          ime_callback_s basic_callback = {
              /* Add the mandatory callbacks */
          };

          ime_event_set_focus_in_cb(focus_in, NULL);
          ime_event_set_focus_out_cb(focus_out, NULL);
          ime_event_set_cursor_position_updated_cb(cursor_position_updated, NULL);

          ime_run(&basic_callback, NULL);
      }
      ```

   2. Define the registered callbacks:

      - The `focus_in()` callback is triggered when an associated text input UI control in any application gets the focus. Usually, the `focus_in()` event is followed by the `show()` event.

        ```
        static int
        focus_in(int context_id, void *user_data)
        {
            /* Take action */
        }
        ```
      - The `focus_out()` callback is triggered when an associated text input UI control in any application loses the focus. Usually, the `focus_out()` event is followed by the `hide()` event.

        ```
        static int
        focus_out(int context_id, void *user_data)
        {
            /* Take action */
        }
        ```
      - The `cursor_position_updated()` callback is triggered when the position of the cursor in an associated text input UI control changes. You can use this callback to provide, for example, auto-capitalization or predictive text features.

        ```
        static int
        cursor_position_updated(int cursor_pos, void *user_data)
        {
            /* Take action */
        }
        ```

<a name="menu"></a>
## Making a Keyboard Option Menu

To make the option menu for the keyboard:

1. Add the necessary callbacks for reacting to the keyboard option menu opening and closing, before calling the `ime_run()` function:

    ```
    static void option_window_created(Evas_Object *window, ime_option_window_type_e type, void *user_data);
    static void option_window_destroyed(Evas_Object *window, void *user_data);

    void
    ime_app_main(int argc, char **argv)
    {
        ime_callback_s basic_callback = {
            /* Add the mandatory callbacks */
        };

        ime_event_set_option_window_created_cb(option_window_created, NULL);
        ime_event_set_option_window_destroyed_cb(option_window_destroyed, NULL);

        ime_run(&basic_callback, NULL);
    }
    ```

2. The option menu can be opened in 2 different ways:

   - The device Settings application can open the keyboard option menu from **Settings > Language and input > Keyboard > Keyboard settings**.

     If the user selects the keyboard settings, the `option_window_created()` callback is executed:

     ```
     static void
     option_window_created(Evas_Object *window, ime_option_window_type_e type, void *user_data)
     {
         /* Create the option window */
         /* Draw the content to the given window object */

         evas_object_show(window);
     }
     ```

   - The keyboard can have a specific key button for its option menu, allowing the user to open the option menu directly from the keyboard.

     If the user clicks the key button, you can use the `ime_create_option_window()` function in the button click callback to open the option menu:

     ```
     static void
     _clicked(void *data, Evas_Object *obj, void *event_info)
     {
         /* Open the IME option menu window */
         ime_create_option_window();
     }
     ```

     The `ime_create_option_window()` function call triggers the `option_window_created()` callback, in which you can draw the option menu content on the given window.

3. To close the option menu, call the `ime_destroy_option_window()` function. The function call triggers the `option_window_destroyed()` callback:

    ```
    static void
    option_window_destroyed(Evas_Object *window, void *user_data)
    {
        /* Destroy the option window */
        /* Release the resources */
    }
    ```

<a name="list"></a>
## Showing the IME List

To launch the IME list menu to show the installed IMEs, use the `ime_manager_show_ime_list()` function:

```
void
show_ime_list()
{
    int ret = ime_manager_show_ime_list();
    if (IME_MANAGER_ERROR_NONE != ret)
        /* Error handling */
}
```

If the menu opens successfully, the function returns 0.

<a name="selector"></a>
## Showing the IME Selector

To launch the IME selector menu to allow the user to select the default keyboard, use the `ime_manager_show_ime_selector()` function:

```
void
show_ime_selector()
{
    int ret = ime_manager_show_ime_selector();
    if (IME_MANAGER_ERROR_NONE != ret)
        /* Error handling */
}
```

If the menu opens successfully, the function returns 0.

<a name="enable"></a>
## Checking the IME State

To check the current default keyboard or whether a specific IME is enabled, or to get the number of enabled (usable) IMEs:

- To check whether a specific IME is enabled, call the `ime_manager_is_ime_enabled()` function. The first parameter is the application ID of the IME whose status you want to check.

    ```
    boolean
    is_ime_enabled(const char *app_id)
    {
        boolean enabled = false;
        int ret = ime_manager_is_ime_enabled(app_id, &enabled);
        if (IME_MANAGER_ERROR_NONE != ret)
            /* Error handling */

        return enabled;
    }
    ```
	If the function is successful, it returns 0.

- To check which IME is currently selected as the default keyboard, call the `ime_manager_get_active_ime()` function:

    ```
    void
    get_active_ime()
    {
        char *app_id = NULL;
        int ret = ime_manager_get_active_ime(&app_id);
        if (IME_MANAGER_ERROR_NONE != ret)
            /* Error handling */
        /* Take action */

        free(app_id);
    }
    ```

	If the function is successful, it returns 0.

- To get the number of enabled (usable) IMEs, call the `ime_manager_get_enabled_ime_count()` function:

    ```
    int
    get_enabled_ime_count()
    {
        int count = ime_manager_get_enabled_ime_count();
        if (count == 0) {
            if (get_last_result() != IME_MANAGER_ERROR_NONE) {
                /* Error handling */
            }
        }
        /* Take action */

       return count;
    }
    ```

	If the function is successful, it returns the number of enabled IMEs. Otherwise, 0.

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
