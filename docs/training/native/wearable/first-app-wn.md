# Creating Your First Tizen Wearable Native Application

**Welcome to Tizen wearable native application development!**

A wearable native application is created using the C language, and can be run on Tizen wearable devices. The application uses the native API, which provides various interfaces to the device hardware allowing you to take advantage of numerous capabilities tailored to run with limited device resources.

Study the following instructions to help familiarize yourself with the Tizen [native application development process](../process/app-dev-process-n.md) as well as using the Tizen Studio and installing the created application on the emulator or target device. With the instructions, you can create and run a basic wearable native application, which displays some text on the screen with no user interaction:

1. Before you get started with developing Tizen applications, download and install the [Tizen Studio](../../../../org.tizen.studio/html/download/download.htm).For more information on the installation process, see the [installation guide](../../../../org.tizen.studio/html/download/installing_sdk.htm).
2. [Create a wearable native project](#create) using the Tizen Studio.This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.
3. [Build the application](#build).After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.
4. [Run the application](#run).This step shows how you can run the application on the emulator or a real target device.
5. [Build a UI](#build_ui).This step shows how you can make small alterations to the application UI to improve the usability of your application.

When you are developing a more complex application, you can take advantage of the [native tools included in the Tizen Studio](../../../../org.tizen.studio/html/native_tools/cover_native_n.htm) to ease the tasks of creating functionality and designing the application UI.

## Creating a Project

The following example shows you how to create and configure a basic wearable native application project in the Tizen Studio. An application project contains all the files that make up an application.

The following figure illustrates the application to be created. The application screen displays the **Hello Tizen** text and no user interaction is provided. If you click the **Back** key on the device, the application moves to the background.

**Figure: Wearable native Basic UI application**

![Wearable native Basic UI application](./media/basic_app_running_wn.png)

To create the application project:

1. Launch the Tizen Studio.

2. Make sure the **Native** perspective is selected in the top right corner of the Tizen Studio window.

   ![Checking the perspective](./media/change_perspective_n.png)

   If not, select it. If the perspective is not visible, in the Tizen Studio menu, select **Window > Perspective > Open Perspective > Other > Native**, and click **OK**.

3. In the Tizen Studio menu, select **File > New > Tizen Project**.

   ![Creating a new Tizen Native project](./media/create_project_1_n.png)

   The Project Wizard opens.

4. In the Project Wizard, define the project details.

   The Project Wizard is used to create the basic application skeleton with the required folder structure and mandatory files. You can easily create different applications by selecting an applicable template or sample for the Project Wizard to use.

   1. Select the **Template** project type and click **Next**.

      ![Selecting the project type](./media/create_project_wizard_type.png)

   2. Select the profile (**Wearable**) and version from a drop-down list and click **Next**.

      The version depends on the platform version you have installed and with which you are developing the application.

      ![Selecting the profile and version](./media/create_project_wizard_version_wearable.png)

   3. Select the **Native Application** application type and click **Next**.

      ![Selecting the application type](./media/create_project_wizard_app_wearable.png)

   4. Select the **Basic UI** template and click **Next**.

      ![Selecting the template](./media/create_project_wizard_template_wn.png)

   5. Define the project properties and click **Finish**.

      You can fill the project name (3-50 characters) and the unique package ID. You can also select the location and working sets by clicking **More properties**.

      ![Defining properties](./media/create_project_wizard_properties_wn.png)

      The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Creating Tizen Projects with Tizen Project Wizard](../../../../org.tizen.studio/html/native_tools/project_wizard_n.htm).

You can see the created project in the **Project Explorer** view. The most important files and folders include:

- `inc`: Default folder for included source files
- `res`: Folder for resource files used by the application only
- `shared`: Folder for resource files to be shared with other applications
- `src`: Folder for source code files
- `lib`: Folder for external library files
- `tizen-manifest.xml`: Manifest file used by the platform to install and launch the application

**Figure: Application in the Project Explorer**

![Application in the Project Explorer](./media/basic_app_project_explorer_wn.png)

**Note**You can [view and modify the application configuration](#configuration) in the manifest editor. In this example, no configuration changes are required.

Your application project is now ready for further actions. Next, build the application.

### Managing the Application Configuration

To view and modify the application configuration:

1. In the **Project Explorer** view, double-click the `tizen-manifest.xml` file of the application. The Tizen Studio opens the file in the manifest editor.

2. In the manifest editor, view and modify the configuration details using the various tabs:

   ![Configuring the application](./media/basic_app_config_wn.png)

   - **Overview**: Define general information, such as the package, label, and icon of the application.

   - **Features**: Define required software and hardware features. This information is used for application filtering in the Tizen market place.

   - **Privileges**: Define the security-sensitive APIs or API groups accessed and used by the application.

   - **Localization**: Define localized values for the application label, description, and icon.

   - **Advanced**: Define advanced features, such as application metadata, data control for services, application control functionalities, and account details.

   - **Source**: View and edit the source code of the `tizen-manifest.xml` file. Changes made and saved on the other tabs are reflected in the source code and vice versa.

     **Note**The `tizen-manifest.xml` file must conform to both the XML file format and the Tizen native application specification requirements. Editing the file in the **Source** tab is intended for advanced users only.

3. To save any changes, in the Tizen Studio menu, select **File > Save All**.

For more information on configuring the application, see [Setting the Application Manifest](../process/setting-properties-n.md#manifest).

## Building Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, you must build the application. The building process performs a validation check and compiles your files.

You can build the application in the following ways:

- **Automatically**

  The automatic build means that the Tizen Studio automatically rebuilds the application whenever you change a source or resource file and save the application project.

  To use the automatic build:

  1. Select the project in the **Project Explorer** view.
  2. In the Tizen Studio menu, select **Project > Build Automatically**.![Using the automatic build](./media/build_automatic_wn.png)A check mark appears next to the menu option.

  You can toggle the automatic build on and off by reselecting **Project > Build Automatically**.

- **Manually**

  The manual build means that you determine yourself when the application is built.

  To manually build the application, right-click the project in the **Project Explorer** view and select **Build Project**.

  **Figure: Manually building the application**

  ![Manually building the application](./media/build_manual_wn.png)

  Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

  - In the Tizen Studio menu, select **Project > Build Project**.
  - Press the **F10** key.

You can have more than one build configuration. To see the current active configuration or change it, right-click the project in the **Project Explorer** view and select **Build Configurations > Set Active**. The default configuration is `Debug`. For more information, see [Building Applications](../process/building-app-n.md).

After you have built the application, run it.

## Running Your Application

You can run the application on the emulator or a real target device.

### Running on the Emulator

To run the application on the emulator:

1. Launch an emulator instance in the [Emulator Manager](../../../../org.tizen.studio/html/common_tools/emulator_manager.htm):In the Tizen Studio menu, select **Tools > Emulator Manager**.![Emulator Manager](./media/emulator_icon.png)In the Emulator Manager, select a wearable emulator from the list and click **Launch**.If no applicable emulator instance exists, [create a new one](../../../../org.tizen.studio/html/common_tools/emulator_manager.htm#create).![Launching the emulator](./media/emulator_instance_launch_wearable.png)The emulator is launched in its own window. You can also see the new emulator instance in the **Device Manager**. To view the emulator folder structure, click the arrow next to the emulator instance.![Emulator](./media/emulator_window_wearable.png)

2. Generate a security profile.

   Before you run the application, you must [sign your application package with a certificate profile](../../../../org.tizen.studio/html/common_tools/certificate_registration.htm) in the Tizen Studio.

3. Run the application:

   1. In the **Project Explorer** view, right-click the project and select **Run As > Tizen Native Application**.![Running the application](./media/app_run_wn.png)Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:Press the **Ctrl+F11** key.Click the run icon in the toolbar.If you have created multiple emulator instances, select the instance you want from the combo box in the toolbar before selecting to run the application. If you select an offline emulator, it is automatically launched when you select to run the application.![Selecting the emulator to use](./media/app_run_multiple_emulators.png)

   2. Confirm that the application launches on the emulator.

      ![Application running in the emulator](./media/emulator_running_wn.png)

      **Note**If the emulator display has switched off, you cannot see the application launch. To switch the display on, click the **Power** key (in the right bottom corner of the emulator).

      While the application is running, the **Log** view in the Tizen Studio shows the log, debug, and exception messages from the methods defined in the log macros. To see the view, in the Tizen Studio menu, go to **Window > Show View > Log**.

For more information on using the emulator features, see [Using Emulator Control Keys, Menu, and Panel](../../../../org.tizen.studio/html/common_tools/emulator_control_panel.htm) and [Using Extended Emulator Features](../../../../org.tizen.studio/html/common_tools/emulator_features.htm).

### Running on a Target Device

To run the application on a target device:

1. Connect the wearable target device to your computer:

   1. Define settings on the device:

      - Go to **Settings > Connections**, and switch on Bluetooth.![Switch on Bluetooth](./media/emulator_target_bt.png)![Switch on Bluetooth](./media/emulator_target_bt2.png)
      - Go to **Settings > Connections**, and switch on Wi-Fi.The device and the computer must be connected to the same Wi-Fi network.Note the IP address the device is using.![Switch on Wi-Fi](./media/emulator_target_wifi.png)
      - Go to **Settings > Gear info**, and switch on the debugging mode.![Switch on debugging](./media/emulator_target_debug.png)

   2. Use the Remote Device Manager to connect the wearable device:

      1. In the **Device Manager**, launch the Remote Device Manager by clicking the related icon.![Launch the Remote Device Manager](./media/remote_conn_mgr_ww.png)
      2. In the **Remote Device Manager** window, click **+**.![Add new device](./media/remote_conn_new_ww.png)
      3. In the **Add Device** window, enter the device and network details (use the IP address you noted before), and click **Add**.![Define device details](./media/remote_conn_add_ww.png)
      4. In the **Remote Device Manager** window, switch the new device on by clicking the switch under **Connect**.![Connect the device](./media/remote_connect_ww.png)

   3. The device asks for user confirmation. To allow Gear to read log data, copy files to and from your computer, and install the application manually, click the accept mark.

      ![Allow Gear to access data](./media/remote_allow_gear_ww.png)

   4. In the **Device Manager**, confirm that the device is connected (shown in the device list).![Device is connected](./media/remote_connected_ww.png)

2. Generate an author certificate.

   Before you run the application, you must [sign your application package with a certificate profile](../../../../org.tizen.studio/html/common_tools/certificate_registration.htm) in the Tizen Studio.

3. Run the application:

   1. In the **Device Manager** view, select the device.
   2. In **Project Explorer** view, right-click the project and select **Run As > Tizen Native Application**.![Run the application on a target device](./media/app_run_wn.png)Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:Press the **Ctrl+F11** key.Click the run icon in the toolbar.If you have both a connected device and existing emulator instances, select the device from the combo box in the toolbar before selecting to run the application.![Selecting the device to use](./media/app_run_multiple_emulators.png)
   3. Confirm that the application launches on the target device.

   **Note**The application is launched using the default debug run configuration. To create and use another configuration:In the `Project Explorer` view, right-click the project and select `Run As > Run Configurations`.In the `Run Configurations` window, click the `New Launch Configuration` icon (![New Launch Configuration icon](./media/run_new_config_wn.png)), define the configuration details, and launch the application by clicking `Run`.![Run Configurations window](./media/run_configurations_n.png)

## Building a Simple UI

The following steps demonstrate how to create a simple user interface for a circular wearable device using EFL. The following figure shows the screen you can create with these instructions.

**Figure: Wearable native UI**

![Wearable native UI](./media/emulator_running_wn.png)

This guide consists of the following:

1. Defining the data structure
2. Registering life-cycle callbacks
3. Creating UI objects

### Defining the Data Structure

A pointer to important objects is stored in the following data structure:

```
struct appdata {
    Evas_Object *win;
    Evas_Object *conform;
    Evas_Object *label;
};
typedef struct appdata appdata_s;
```

### Registering Life-cycle Callbacks

The `main()` function has callbacks that manage specific parts of the application life-cycle:

- `app_create`Called when the application process starts.Used to create UI components.
- `app_terminate`Called while the application process is terminating.Called after the main loop quits.
- `app_resume` (UI applications only)Called when the application window is shown.
- `app_pause` (UI applications only)Called when the application window is totally hidden.
- `app_control`Called after the `app_create` callback when the process starts or called when a launch request is received while the process is running.Can receive `app_control` data (parameters for launching the application).Used to implement parameter-specific actions of the application.

```
int
main(int argc, char *argv[])
{
    appdata_s ad = {0,};
    int ret = 0;
    ui_app_lifecycle_callback_s event_callback = {0,};
    app_event_handler_h handlers[5] = {NULL,};

    event_callback.create = app_create;
    event_callback.terminate = app_terminate;
    event_callback.pause = app_pause;
    event_callback.resume = app_resume;
    event_callback.app_control = app_control;

    ret = ui_app_main(argc, argv, &event_callback, &ad);
    if (ret != APP_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "app_main() failed. Err=%d", ret);

    return ret;
}
```

### Creating UI Objects

The `app_create()` function is called when the process starts, and it calls the `create_base_gui()` function:

```
static bool
app_create(void *data)
{
    /*
       Hook to take necessary actions before the main event loop starts
       Initialize UI resources and application data
       If this function returns true, the application main loop starts
       If this function returns false, the application is terminated
    */
    appdata_s *ad = data;

    create_base_gui(ad);

    return true;
}
```

In the `create_base_gui()` function, you can create a simple user interface that consists of window, conformant, and label objects:

```
static void
create_base_gui(appdata_s *ad)
{
    /* Window */
    ad->win = elm_win_util_standard_add(PACKAGE, PACKAGE);
    elm_win_autodel_set(ad->win, EINA_TRUE);

    if (elm_win_wm_rotation_supported_get(ad->win)) {
        int rots[4] = {0, 90, 180, 270};
        elm_win_wm_rotation_available_rotations_set(ad->win, (const int *)(&rots), 4);
    }

    evas_object_smart_callback_add(ad->win, "delete,request", win_delete_request_cb, NULL);
    eext_object_event_callback_add(ad->win, EEXT_CALLBACK_BACK, win_back_cb, ad);

    /* Conformant */
    ad->conform = elm_conformant_add(ad->win);
    elm_win_indicator_mode_set(ad->win, ELM_WIN_INDICATOR_SHOW);
    elm_win_indicator_opacity_set(ad->win, ELM_WIN_INDICATOR_OPAQUE);
    evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_win_resize_object_add(ad->win, ad->conform);
    evas_object_show(ad->conform);

    /* Label */
    ad->label = elm_label_add(ad->conform);
    elm_object_text_set(ad->label, "<align=center>Hello Tizen</align>");
    evas_object_size_hint_weight_set(ad->label, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
    elm_object_content_set(ad->conform, ad->label);

    /* Show the window after the base GUI is set up */
    evas_object_show(ad->win);
}
```

To break down the above code:

- Window objects can be created by using the `elm_win_util_standard_add()` function and adding callbacks on window objects. One of the callbacks handles the `delete,request` event when the window is to be closed, and the other handles the `EEXT_CALLBACK_BACK` event when the hardware back key is pressed.

  ```
  /* Window */
  ad->win = elm_win_util_standard_add(PACKAGE, PACKAGE);
  elm_win_autodel_set(ad->win, EINA_TRUE);

  if (elm_win_wm_rotation_supported_get(ad->win)) {
      int rots[4] = {0, 90, 180, 270};
      elm_win_wm_rotation_available_rotations_set(ad->win, (const int *)(&rots), 4);
  }
  evas_object_smart_callback_add(ad->win, "delete,request", win_delete_request_cb, NULL);
  eext_object_event_callback_add(ad->win, EEXT_CALLBACK_BACK, win_back_cb, ad);
  ```

- You can create a conformant object that is based on the window.

  The `elm_win_indicator_mode_set()` function decides whether the indicator is visible, and the `elm_win_indicator_opacity_set()` function sets the indicator opacity mode.

  You can set the conformant object as a resize object of the window by using the `elm_win_resize_object_add()` function. It means that the conformant size and position are controlled by the window object directly.

  The `evas_object_show()` function makes the conformant object visible.

  ```
  /* Conformant */
  ad->conform = elm_conformant_add(ad->win);
  elm_win_indicator_mode_set(ad->win, ELM_WIN_INDICATOR_SHOW);
  elm_win_indicator_opacity_set(ad->win, ELM_WIN_INDICATOR_OPAQUE);
  evas_object_size_hint_weight_set(ad->conform, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
  elm_win_resize_object_add(ad->win, ad->conform);
  evas_object_show(ad->conform);
  ```

- You can add a label object for text by using the `elm_label_add()` function. It adds a new label to the parent (conformant object).

  You can also set the text to the label by using the `elm_object_text_set()` function.

  ```
  /* Label */
  ad->label = elm_label_add(ad->conform);
  elm_object_text_set(ad->label, "<align=center>Hello Tizen</align>");
  evas_object_size_hint_weight_set(ad->label, EVAS_HINT_EXPAND, EVAS_HINT_EXPAND);
  elm_object_content_set(ad->conform, ad->label);
  ```

- When all the UI components are ready, make the window object visible by using the `evas_object_show()` function:

  ```
  /* Show the window after the base GUI is set up */
  evas_object_show(ad->win);
  ```