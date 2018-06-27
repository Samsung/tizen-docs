# Creating Your First Tizen Wearable Native Watch Application

**Welcome to Tizen wearable native watch application development!**

A wearable native watch application is created using the C language, and can be run on Tizen wearable devices to display a customized watch face to the user.

Study the following instructions to help familiarize yourself with the Tizen [native application development process](../../tutorials/process/app-dev-process.md) as well as using the Tizen Studio and installing the created application on the emulator or target device. With the instructions, you can create and run a basic wearable native watch application, which displays some text and the current time on the screen:

1. Before you get started with developing Tizen applications, download and install the [Tizen Studio](../../../tizen-studio/setup/download.md).

   For more information on the installation process, see the [installation guide](../../../tizen-studio/setup/install-sdk.md).

2. [Create a wearable native watch project](#create) using the Tizen Studio.

   This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.


3. [Build the application](#build).

    After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.

4. [Run the application](#run).

    This step shows how you can run the application on the emulator or a real target device.

5. [Design a UI](#build).

    This step shows how you can create the application UI and make small alterations to it to improve the usability of your application.

When you are developing a more complex application, you can take advantage of the [native tools included in the Tizen Studio](../../../tizen-studio/native-tools/cover-native.md) to ease the tasks of creating functionality and designing the application UI.

<a name="create"></a>
## Creating a Project

The following example shows you how to create and configure a basic wearable native watch application project in the Tizen Studio. An application project contains all the files that make up an application.

The following figure illustrates the application to be created. The application screen displays the **Hello Watch** text and the current time, which continues to be refreshed every second while the application runs.

**Figure: Wearable native Watch application**

![Wearable native Watch application](media/basic_app_running_wn_watch.png)

To create the application project:

1.  Launch the Tizen Studio.

2. Make sure the **Native** perspective is selected in the upper-right corner of the Tizen Studio window.

    ![Checking the perspective](media/change_perspective_n.png)

    If not, select it. If the perspective is not visible, in the Tizen Studio menu, select **Window &gt; Perspective &gt; Open Perspective &gt; Other &gt; Native**, and click **OK**.

3. In the Tizen Studio menu, select **File &gt; New &gt; Tizen Project**.

    ![Creating a new Tizen Native project](media/create_project_1.png)

    The Project Wizard opens.

4. In the Project Wizard, define the project details.

    The Project Wizard is used to create the basic application skeleton with the required folder structure and mandatory files. You can easily create different applications by selecting an applicable template or sample for the Project Wizard to use.

    1.  Select the **Template** project type and click **Next**.

        ![Selecting the project type](media/create_project_wizard_type.png)

    2. Select the profile (**Wearable**) and version from a drop-down list and click **Next**.

        The version depends on the platform version you have installed and with which you are developing the application.

        ![Selecting the profile and version](media/create_project_wizard_version_wearable.png)

    3. Select the **Native Application** application type and click **Next**.

        ![Selecting the application type](media/create_project_wizard_app_wearable.png)

    4. Select the **Watch** template and click **Next**.

        ![Selecting the template](media/create_project_wizard_template_wn_watch.png)

    5. Define the project properties and click **Finish**.

        You can enter the project name (3-50 characters) and the unique package ID. You can also select the location and working sets by clicking **More properties**.

        ![Defining properties](media/create_project_wizard_properties_wn_watch.png)

        The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Creating Tizen Projects with Tizen Project Wizard](../../../tizen-studio/native-tools/project-wizard.md).

You can see the created project in the **Project Explorer** view. The most important files and folders include:

-   `inc`: Default folder for included source files

-   `res`: Folder for resource files used by the application only

-   `shared`: Folder for resource files to be shared with other applications

-   `src`: Folder for source code files

-   `lib`: Folder for external library files

-   `tizen-manifest.xml`: Manifest file used by the platform to install and launch the application

**Figure: Application in the Project Explorer**

![Application in the Project Explorer](media/basic_app_project_explorer_wn_watch.png)

> **Note**
>
> You can [view and modify the application configuration](#configuration) in the manifest editor. In this example, no configuration changes are required.


Your application project is now ready for further actions. Next, build the application.

<a name="configuration"></a>
### Managing the Application Configuration

To view and modify the application configuration:

1.  In the **Project Explorer** view, double-click the `tizen-manifest.xml` file of the application. The Tizen Studio opens the file in the manifest editor.

2. In the manifest editor, view and modify the configuration details using the various tabs:

    ![Configuring the application](media/basic_app_config_wn_watch.png)

    -   **Overview**: Define general information, such as the package, label, and icon of the application.

    - **Features**: Define required software and hardware features. This information is used for application filtering in the Tizen Store.

    - **Privileges**: Define the security-sensitive APIs or API groups accessed and used by the application.

    - **Localization**: Define localized values for the application label, description, and icon.

    - **Advanced**: Define advanced features, such as application metadata and some miscellaneous options.

    - **Source**: View and edit the source code of the `tizen-manifest.xml` file. Changes made and saved on the other tabs are reflected in the source code and vice versa.

        > **Note**
        >
        > The `tizen-manifest.xml` file must conform to both the XML file format and the Tizen native application specification requirements. Editing the file in the **Source** tab is intended for advanced users only.

3. To save any changes, in the Tizen Studio menu, select **File &gt; Save All**.

For more information on configuring the application, see [Setting the Application Manifest](../../tutorials/process/setting-properties.md#manifest).

### Understanding the Source Code

Pay attention to the following main issues in the application source code (in the `inc/watch.h` and `src/watch.c` files), to understand how the application is designed and how it works. For source code details related to the UI, see [Designing a Simple UI](#build_ui).

-   The watch application is initialized to use the functions and data types of the [Watch Application](../../api/wearable/latest/group__CAPI__WATCH__APP__MODULE.html) API by including the `<watch_app.h>` header file in your application:

    ```
    #include <watch_app.h>
    ```

    All header files that you need are already included in the `watch.h` file, which is generated by the Tizen Studio when the template project is created.

- The life-cycle callbacks manage specific parts of the application life-cycle. They are set in the [watch\_app\_lifecycle\_callback\_s](../../api/wearable/latest/structwatch__app__lifecycle__callback__s.html) structure, and the structure is passed to the `watch_app_main()` function of the Watch Application API to start the watch application event loop:

    ```
    int
    main(int argc, char *argv[])
    {
        appdata_s ad = {0,};
        int ret = 0;

        watch_app_lifecycle_callback_s event_callback = {0,};
        app_event_handler_h handlers[5] = {NULL,};

        event_callback.create = app_create;
        event_callback.terminate = app_terminate;
        event_callback.pause = app_pause;
        event_callback.resume = app_resume;
        event_callback.app_control = app_control;
        event_callback.time_tick = app_time_tick;
        event_callback.ambient_tick = app_ambient_tick;
        event_callback.ambient_changed = app_ambient_changed;

        ret = watch_app_main(argc, argv, &event_callback, &ad);
        if (ret != APP_ERROR_NONE)
            dlog_print(DLOG_ERROR, LOG_TAG, "watch_app_main() is failed. err = %d", ret);

        return ret;
    }
    ```

    -   The `create` event is triggered before the application main loop starts. In this callback, you can initialize the application resources, such as create windows and data structures.

        ```
        static bool
        app_create(int width, int height, void *data)
        {
            /*
               Hook to take necessary actions before the main event loop starts
               Initialize UI resources and application's data
               If this function returns true, the main loop of application starts
               If this function returns false, the application is terminated
            */
            appdata_s *ad = data;

            create_base_gui(ad, width, height);

            return true;
        }
        ```

    - The `time_tick` event is triggered at least once per second. The watch applications can get the current time from the `watch_time` time handle to draw a normal watch.

        ```
        static void
        app_time_tick(watch_time_h watch_time, void *data)
        {
            /* Called each second while your app is visible; update the watch UI */
            appdata_s *ad = data;
            update_watch(ad, watch_time, 0);
        }
        ```

    > **Note**
    >
    > For more information on the application life-cycle callbacks, see [Applications](../../guides/app-management/applications.md).

- An ambient mode is available on a low-powered wearable device. In this mode, the watch application shows a limited UI and receives only the ambient tick event every minute to reduce power consumption.

    The details of the limited UI drawn in the ambient mode depend on the device. In addition, due to the ambient mode being a low power mode, there are limits to the colors that can be shown on the screen. Usually, when designing the ambient mode UI, draw it with limited colors (cyan, magenta, yellow, red, green, blue, black and white), and use less than 15% of the pixels on the screen. If you do not want to draw your own ambient mode UI, set the `ambient-support` attribute to `false` in the watch application manifest file to allow the platform to show a default ambient mode UI.

    > **Note**
    >
    > To use the ambient mode, the user must enable it in the device settings. In addition, on the Gear S2 device, the ambient mode activates only when you are wearing the watch on the wrist.

    -   The `ambient_tick` callback is triggered every minute while the device is in the ambient mode. You can use the callback to update the time on your watch application in the ambient mode. In this callback, do not perform time-consuming tasks and always update the UI as quickly as possible. The platform can put the device to sleep shortly after the ambient tick expires.

        ```
        static void
        app_ambient_tick(watch_time_h watch_time, void *data)
        {
            /* Called at each minute while the device is in ambient mode. Update watch UI. */
            appdata_s *ad = data;
            update_watch(ad, watch_time, 1);
        }
        ```

    - The `ambient_changed` callback is triggered when the ambient mode is enabled or disabled on the device. You can use the callback to initialize your ambient mode UI.

        ```
        static void
        app_ambient_changed(bool ambient_mode, void *data)
        {
            if (ambient_mode)
                /* Prepare to enter the ambient mode */
            else
                /* Prepare to exit the ambient mode */
        }
        ```

<a name="build"></a>
## Building Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, you must build the application. The building process performs a validation check and compiles your files.

You can build the application in the following ways:

-   **Automatically**

    The automatic build means that the Tizen Studio automatically rebuilds the application whenever you change a source or resource file and save the application project.

    To use the automatic build:

    1.  Select the project in the **Project Explorer** view.
    2. In the Tizen Studio menu, select **Project &gt; Build Automatically**.

        ![Using the automatic build](media/build_automatic_wn_watch.png)

        A check mark appears next to the menu option.

    You can toggle the automatic build on and off by reselecting **Project &gt; Build Automatically**.

- **Manually**

    The manual build means that you determine yourself when the application is built.

    To manually build the application, right-click the project in the **Project Explorer** view and select **Build Project**.

    **Figure: Manually building the application**

    ![Manually building the application](media/build_manual_n.png)

    Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

    -   In the Tizen Studio menu, select **Project &gt; Build Project**.
    -   Press the **F10** key.

You can have more than one build configuration. To see the current active configuration or change it, right-click the project in the **Project Explorer** view and select **Build Configurations &gt; Set Active**. The default configuration is `Debug`. For more information, see [Building Applications](../../tutorials/process/building-app.md).

After you have built the application, run it.

<a name="run"></a>
## Running Your Application

You can run the application on the emulator or a real target device.

<a name="emulator"></a>
### Running on the Emulator

To run the application on the emulator:

1.  Launch an emulator instance in the [Emulator Manager](../../../tizen-studio/common-tools/emulator-manager.md):
    1.  In the Tizen Studio menu, select **Tools &gt; Emulator Manager**.

        ![Emulator Manager](media/emulator_icon.png)

    2. In the Emulator Manager, select a wearable emulator from the list and click **Launch**.

        If no applicable emulator instance exists, [create a new one](../../../tizen-studio/common-tools/emulator-manager.md#create).

        ![Launching the emulator](media/emulator_instance_launch_wearable.png)

        The emulator is launched in its own window. You can also see the new emulator instance and its folder structure in the **Device Manager**.

        ![Emulator](media/emulator_window_wearable.png)

2. Generate a security profile.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3. Run the application:
    1.  In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Native Application**.

        ![Running the application](media/app_run_n.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have created multiple emulator instances, select the instance you want from the combo box in the toolbar before selecting to run the application. If you select an offline emulator, it is automatically launched when you select to run the application.

        ![Selecting the emulator to use](media/app_run_multiple_emulators.png)

    2. Confirm that the application launches on the emulator.

        ![Successful installation](media/watch_run_face_wn.png)

        > **Note**
        >
        > If the emulator display has switched off, you cannot see the application launch. To switch the display on, click the **Power** key (in the lower-right corner of the emulator).

    3. Change the watch face.<a name="watchface"></a>

        To change the watch face and make the installed watch application visible:

        ![Changing the watch face](media/watch_run_change_wn.png)

        1. If the emulator display has been switched off, activate it by pressing the **Power** key (in the lower-right corner of the emulator).
        2. On the home screen (showing the default watch face), press the **Power** key.
        3. In the Recent Apps screen, select **Settings &gt; Watch faces and styles &gt; Watch faces**.
        4. Swipe right until you find your application icon, and select it.

           The **Clock changed** message is displayed.

        5. Press the **Back** key (in the upper-right corner of the emulator device) multiple times, until the home screen with your new watch face is shown.

           ![Application running in the emulator](media/watch_run_face_wn.png)

        While the application is running, the **Log** view in the Tizen Studio shows the log, debug, and exception messages from the methods defined in the log macros. To see the view, in the Tizen Studio menu, go to **Window &gt; Show View &gt; Log**.

For more information on using the emulator features, see [Using Emulator Control Keys, Menu, and Panel](../../../tizen-studio/common-tools/emulator-control-panel.md) and [Using Extended Emulator Features](../../../tizen-studio/common-tools/emulator-features.md).

<a name="target"></a>
### Running on a Target Device

To run the application on a target device:

1.  Connect the wearable target device to your computer:
    1.  Define settings on the device:
        -   Go to **Settings &gt; Connections**, and switch on Bluetooth.

            ![Switch on Bluetooth](media/emulator_target_bt.png)

            ![Switch on Bluetooth](media/emulator_target_bt2.png)

        - Go to **Settings &gt; Connections**, and switch on Wi-Fi.

            The device and the computer must be connected to the same Wi-Fi network.

            Note the IP address the device is using.

            ![Switch on Wi-Fi](media/emulator_target_wifi.png)

        - Go to **Settings &gt; Gear info**, and switch on the debugging mode.

            ![Switch on debugging](media/emulator_target_debug.png)

    2. In the terminal, enter the following commands:

        ```
        cd tizen-sdk/tools
        ./sdb connect <IP address of Gear S2>
        ```

        Use the IP address you noted before.

        Instead of the terminal, you can also use the [Remote Device Manager](../wearable/first-app-wn.md#remote_device) for the connection.

    3. In the first attempt, the connection fails and the device asks for user confirmation. To allow Gear to read log data, copy files to and from your computer, and install the application manually, click the accept mark.

        ![Allow Gear to access data](media/remote_allow_gear_ww.png)

    4. In the **Device Manager**, confirm that the device is connected (shown in the device list).

        ![Device is connected](media/remote_connected_ww.png)

2. Generate an author certificate.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3. Run the application:
    1.  In the **Device Manager**, select the device.
    2. In **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Native Application**.

        ![Run the application on a target device](media/app_run_n.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have both a connected device and existing emulator instances, select the device from the combo box in the toolbar before selecting to run the application.

        ![Selecting the device to use](media/app_run_multiple_emulators.png)

    3. Confirm that the application launches on the target device.

        Like with the [emulator](#watchface), you can change the watch face in the device settings to see the watch application on the home screen.

    > **Note**
    >
    > The application is launched using the default debug run configuration. To create and use another configuration:
    > 1.  In the `Project Explorer` view, right-click the project and select `Run As > Run Configurations`.
    > 2.  In the `Run Configurations` window, click the `New Launch Configuration` icon (![New Launch Configuration icon](media/run_new_config_wn.png)), define the configuration details, and launch the application by clicking `Run`.
    >     ![Run Configurations window](media/run_configurations_wn_watch.png)

<a name="build_ui"></a>
## Designing a Simple UI

The wearable watch application created with the **Watch** template has a simple user interface with a label component showing the **Hello Watch** text and the current time (hour, minute, and second). The UI is created using [EFL](../../guides/ui/efl/introduction.md).

In the ambient mode, the **Watch** template UI is identical to the normal UI, except that is shows the current time without the seconds.

**Figure: User interface in the Watch template (ambient mode on the right)**

![User interface in the Watch template (ambient mode on the right)](media/simple_ui_basic_wn_watch.png)

### Creating the Basic UI

The UI in the **Watch** template contains the following components:

-   The EFL UI always contains a window component, which is the root component of the entire UI.
-   The application uses the conformant component as a container for other UI components.
-   The label showing the **Hello Watch** text and the current time is implemented with a label component.

The UI is created in the `watch.c` file:

1.  Data structure

    A pointer to the UI components is stored in the `appdata_s` data structure:

    ```
    struct appdata {
        /* Window */
        Evas_Object *win;
        /* Conformant */
        Evas_Object *conform;
        /* Label */
        Evas_Object *label;
    };
    typedef struct appdata appdata_s;
    ```

2. UI creation

    The `app_create()` life-cycle callback is called when the application main loop starts, and it calls the `create_base_gui()` function to create the UI:

    ```
    static bool
    app_create(int width, int height, void *data)
    {
        /* Define system callbacks */

        appdata_s *ad = data;

        create_base_gui(ad, width, height);

        return true;
    }
    ```

3. UI components
    1.  The `create_base_gui()` function creates the UI components: window, conformant, and label.

        The function receives a pointer to fill in the `appdata_s` structure.

        ```
        static void
        create_base_gui(appdata_s *ad, int width, int height)
        {
        ```

    2. The window object of the idle screen is retrieved with the `watch_app_get_elm_win()` function of the [Watch Application](../../../api/wearable/latest/group__CAPI__WATCH__APP__MODULE.html) API.

        The `watch_time_h` handle is created for managing the current time, and the `evas_object_resize()` function is used to resize the window to fit the screen.

        ```
            int ret;
            watch_time_h watch_time = NULL;

            ret = watch_app_get_elm_win(&ad->win);

            if (ret != APP_ERROR_NONE) {
                dlog_print(DLOG_ERROR, LOG_TAG, "failed to get window. err = %d", ret);

                return;
            }

            evas_object_resize(ad->win, width, height);
        ```

    3. The conformant component is used as a container for the other UI components:

        -   The component is the first object added inside the window with the `elm_conformant_add()` function.
        -   The conformant component is set as a resize object of the window by using the `elm_win_resize_object_add()` function. It means that the conformant size and position are controlled by the window component directly.
        -   The `evas_object_show()` function makes the conformant component visible.

        ```
            ad->conform = elm_conformant_add(ad->win);
            evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND,
                                             EVAS_HINT_EXPAND);
            elm_win_resize_object_add(ad->win, ad->conform);
            evas_object_show(ad->conform);
        ```

    4. The label component for the text and time is added with the `elm_label_add()` function. The label is added inside the conformant component, which is the label's parent.

        The label is resized and moved so that it is located below the first third of the screen height.

        ```
            ad->label = elm_label_add(ad->conform);
            evas_object_resize(ad->label, width, height / 3);
            evas_object_move(ad->label, 0, height / 3);
            evas_object_show(ad->label);
        ```

    5. The `watch_time_get_current_time()` function retrieves the current time, and the `update_watch()` function uses the current time to set the label component content. Finally, the `watch_time_h` handle is deleted.

        ```
            ret = watch_time_get_current_time(&watch_time);

            if (ret != APP_ERROR_NONE)
                dlog_print(DLOG_ERROR, LOG_TAG,
                           "failed to get current time. err = %d", ret);

            update_watch(ad, watch_time, 0);
            watch_time_delete(watch_time);
        ```

    6. When all the UI components are ready, the `evas_object_show()` function makes the window component visible. This means that the window displays everything on the screen at once.

        ```
            evas_object_show(ad->win);
        }
        ```

### Modifying Existing Components

When the basic UI exists, you can easily modify the components in the UI by using the component-specific functions, or more general Evas object functions.

For example, the following modification to the label component changes the text color to red:

```
    ad->label = elm_label_add(ad->conform);
    evas_object_color_set(ad->label, 255, 0, 0, 255);
    evas_object_resize(ad->label, width, height / 3);
    evas_object_move(ad->label, 0, height / 3);
    evas_object_show(ad->label);
```

**Figure: Modified label component**

![Modified label component](media/simple_ui_label_wn_watch.png)

### Showing the Current Time

You can update the time on the screen with the `time_tick` (in the normal mode) or `ambient_tick` (in the ambient mode) callback:

1.  Both callbacks contain the current time handle, and call the `update_watch()` function to update the label content on the screen:

    ```
    static void
    app_time_tick(watch_time_h watch_time, void *data)
    {
        appdata_s *ad = data;
        update_watch(ad, watch_time, 0);
    }

    static void
    app_ambient_tick(watch_time_h watch_time, void *data)
    {
        appdata_s *ad = data;
        update_watch(ad, watch_time, 1);
    }
    ```

2. In the `update_watch()` function, the `watch_time_h` handle is used to retrieve the current time elements (hour, minute, and second) with the `watch_time_get_hour24()`, `watch_time_get_minute()`, and `watch_time_get_second()` functions of the [Watch Application](../../api/wearable/latest/group__CAPI__WATCH__APP__MODULE.html) API.

    The text for the label component is defined (based on whether the normal or ambient mode is used), and set with the `elm_object_text_set()` function.

    ```
    static bool
    update_watch(appdata_s *ad, watch_time_h watch_time, int ambient)
    {
        char watch_text[TEXT_BUF_SIZE];
        int hour24;
        int minute;
        int second;
        if (watch_time == NULL)
            return;

        watch_time_get_hour24(watch_time, &hour24);
        watch_time_get_minute(watch_time, &minute);
        watch_time_get_second(watch_time, &second);
        if (!ambient) {
            snprintf(watch_text, TEXT_BUF_SIZE,
                     "<align=center>Hello Watch<br/>%02d:%02d:%02d</align>",
                     hour24, minute, second);
        } else {
            snprintf(watch_text, TEXT_BUF_SIZE,
                     "<align=center>Hello Watch<br/>%02d:%02d</align>",
                     hour24, minute);
        }

        elm_object_text_set(ad->label, watch_text);
    }
    ```
