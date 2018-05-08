# Creating Your First Tizen Wearable Web Widget Application

**Welcome to Tizen wearable Web widget application development!**

A wearable Web application is basically a Web site stored on a wearable device. You can create it using Web-native languages, such as HTML5, CSS, and JavaScript.

A widget application is one of the Tizen application types. It can be shown by specific UI applications (such as the home screen and lock screen) that can contain widget applications.

**Figure: Widget application on a wearable device**

![Widget application on a wearable device](media/widget_app_wearable_widget.png)

Study the following instructions to help familiarize yourself with the Tizen [Web application development process](../../tutorials/process/app-dev-process.md) as well as using the Tizen Studio and installing the created application on the emulator or target device. With the instructions, you can create and run a basic wearable Web widget application (a Web widget), which displays some text on the screen with no user interaction:

1.  Before you get started with developing Tizen applications, download and install the [Tizen Studio](../../../tizen-studio/index.md).

    For more information on the installation process, see the [installation guide](../../../tizen-studio/setup/install-sdk.md).

2.  [Create a wearable Web widget project](#create) using the Tizen Studio.

    This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.

3.  [Build the application](#build).

    After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.

4.  [Run the application](#run).

    This step shows how you can run the application on the emulator or a real target device.

5.  [Design a UI](#ui).

    This step shows how you can create the application UI and make small alterations to it to improve the usability of your application.

When you are developing a more complex application, you can take advantage of the [Web tools included in the Tizen Studio](../../../tizen-studio/web-tools/overview.md) to ease the tasks of creating functionality and designing the application UI.

<a name="create"></a>
## Creating a Project

The following example shows you how to create and configure a basic wearable Web widget application project in the Tizen Studio. An application project contains all the files that make up an application.

> **Note**  
> Standalone widget application packages are not allowed in the Tizen Store.
>
> For user convenience, you can use a standalone widget application for testing purposes in the Tizen Studio. If you want to publish the application in the Tizen Store, combine it with at least 1 UI application in the same package. For more information, see [Developing Multiple Projects as a Combined Package](../../tutorials/process/app-dev-process.md#multi).

The following figure illustrates the application to be created. The application screen displays the **Hello Widget** text and no user interaction is provided.

**Figure: Wearable Web Widget application**

![Wearable Web Widget application](media/basic_app_running_ww_widget.png)

To create the application project:

1.  Launch the Tizen Studio.

2.  Make sure the **Web** perspective is selected in the upper-right corner of the Tizen Studio window.

    ![Checking the perspective](media/change_perspective_w.png)

    If not, select it. If the perspective is not visible, in the Tizen Studio menu, select **Window &gt; Perspective &gt; Open Perspective &gt; Other &gt; Web**, and click **OK**.

3.  In the Tizen Studio menu, select **File &gt; New &gt; Tizen Project**.

    ![Creating a new Tizen Web project](media/create_project_1.png)

    The Project Wizard opens.

4.  In the Project Wizard, define the project details.

    The Project Wizard is used to create the basic application skeleton with the required folder structure and mandatory files. You can easily create different applications by selecting an applicable template or sample for the Project Wizard to use.

    1.  Select the **Template** project type and click **Next**.

        ![Selecting the project type](media/create_project_wizard_type.png)

    2.  Select the profile (**Wearable**) and version from a drop-down list and click **Next**.

        The version depends on the platform version you have installed and with which you are developing the application.

        ![Selecting the profile and version](media/create_project_wizard_version_wearable.png)

    3.  Select the **Web Application** application type and click **Next**.

        ![Selecting the application type](media/create_project_wizard_app_web_wearable.png)

    4.  Select the **Widget** template and click **Next**.

        ![Selecting the template](media/create_project_wizard_template_ww_widget.png)

    5.  Define the project properties and click **Finish**.

        You can enter the project name (3-50 characters) and the unique package ID. You can also select the location and working sets by clicking **More properties**.

        ![Defining properties](media/create_project_wizard_properties_ww_widget.png)

        The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Creating Tizen Projects with Tizen Project Wizard](../../../tizen-studio/web-tools/project-wizard.md).

You can see the created project in the **Project Explorer** view. The most important files and folders include:

-   `css`: Folder for CSS files used by the application to style its content

-   `js`: Folder for JavaScript files used by the application to implement its functional logic

-   `config.xml`: Application configuration file used by the platform to install and launch the application

-   `icon.png`: Application icon file used by the platform to represent the widget

-   `index.html`: Main HTML file for the layout of the application screen

-   `preview.png`: Preview of the widget application file that is displayed in the widget view on the target.

**Figure: Application in the Project Explorer**

![Application in the Project Explorer](media/basic_app_project_explorer_ww_widget.png)

> **Note**  
> You can [validate your widget](#validate) and [view and modify the application configuration](#configuration) in the Web application configuration editor. In this example, no configuration changes are required.

Your application project is now ready for further actions. Next, build the application.

<a name="validate"></a>
### Checking the Application with the API Validator

You can validate a Tizen wearable widget application using one of 3 validators:

-   HTML validator
-   CSS validator
-   JS validator

You can enable or disable these validators in the application preferences: go to **Window &gt; Preferences &gt; Tizen Studio &gt; WebWidget**, and check the applicable check boxes.

**Figure: Validation preferences**

![Validation preferences](media/widget_validate_pref_w.png)

The validation is performed automatically when the project or package is built, or when the application is run.

When the validation is complete, its results are shown in the **Problems** view. If the view is not displayed, select it from **Window &gt; Show view &gt; Problems** (keyboard shortcut: **Shift + Alt + Q + X**).

**Figure: Validation results**

![Validation results](media/widget_validate_result_w.png)

<a name="configuration"></a>
### Managing the Application Configuration

To view and modify the application configuration:

1.  In the **Project Explorer** view, double-click the `config.xml` file of the application. The Tizen Studio opens the file in the Web application configuration editor.

2.  In the configuration editor, view and modify the configuration details using the various tabs:

    ![Configuring the application](media/basic_app_config_widget_w.png)

    -   **Overview**: Define general information, such as the name and icon of the application.

    -   **Features**: Define required software and hardware features. This information is used for application filtering in the Tizen Store.

    -   **Privileges**: Define the security-sensitive APIs or API groups accessed and used by the application.

    -   **Localization**: Define localized values for the application name, description, and license.

    -   **Policy**: Request network resource permissions to access external network resources.

    -   **Preferences**: Define name-value pairs that can be set or retrieved through the application.

    -   **Tizen**: Edit the Tizen schema extension properties of the application.

    -   **Source**: View and edit the source code of the `config.xml` file. Changes made and saved on the other tabs are reflected in the source code and vice versa.

        > **Note**  
		> The `config.xml` file must conform to both the XML file format and the W3C specification requirements. Editing the file in the **Source** tab is intended for advanced users only.

3.  To save any changes, in the Tizen Studio menu, select **File &gt; Save All**.

For more information on configuring the application, see [Setting the Web Application Configuration](../../tutorials/process/setting-properties.md#set_widget).

### Understanding the Source Code

Pay attention to the following main issues in the application source code, to understand how the application is designed and how it works. For source code details related to the UI, see [Designing a Simple UI](#ui).

-   The widget application settings are defined in the `config.xml` file.

    The file includes various information for the widget application. The following code shows an example of the widget content in the file:

    -   The `<tizen:app-widget>` element indicates the widget settings.
    -   The widget application is started and initialized with the `index.html` file. The `<content>` field `src` attribute defines the starting point.
    -   If the widget requires privileges, add them to the `config.xml` file as well.

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <widget xmlns:tizen="http://tizen.org/ns/widgets" xmlns="http://www.w3.org/ns/widgets"
            id="http://yourdomain/Widget" version="1.0.0">
       <tizen:app-widget id="0lVPHbX9t6.Widget.Widget" primary="true">
          <tizen:widget-label>Hello Web Widget!</tizen:widget-label>
          <tizen:widget-content src="widget/Widget/index.html">
             <tizen:widget-size preview="widget/Widget/preview.png">2x2</tizen:widget-size>
          </tizen:widget-content>
       </tizen:app-widget>
       <tizen:application id="0lVPHbX9t6.Widget" package="0lVPHbX9t6" required_version="4.0"/>
       <content src="index.html"/>
       <feature name="http://tizen.org/feature/screen.size.normal"/>
       <icon src="icon.png"/>
       <name>Widget</name>
       <tizen:profile name="wearable"/>
    </widget>
    ```

-   The widget application consists of the following folder architecture:

    ```
    widget
       Widget
          css
             style.css
          js
             main.js
          index.html
          preview.png
    config.xml
    icon.png
    index.html
    ```

    You can customize the `widget/Widget/index.html`, `widget/Widget/css/style.css`, and `widget/Widget/js/main.js` files. You can add various features (such as asynchronous functions, JS library, and effects) to the widget application using JS. For example, if a JS-based animation effect is needed, add the `requestAnimationFrame()` method or some other animation library to the JS file. Similarly, to change the UI elements' visual looks or add CSS-based effects (including animation), modify the CSS file.

-   You can define the widget as a standalone or combined (Web application + Web widget) application.

    The widget application can be a standalone application, which means that it does not connect to a Web application, or it can be combined in the same package with a Web UI application. However, you cannot publish a standalone widget in the Tizen Store.

    When you create a widget application in the Tizen Studio, it is always first a standalone application. If you want to connect to a Web UI application, you can package the widget with a Web UI application:

    1.  Create a Web UI application and the widget application.
    2.  In the **Project Explorer** view, right-click the Web application, and select **Properties &gt; Tizen Studio &gt; Package &gt; Multi**, and select the widget to be included in the package.
    3.  Click **OK**.

    In the following figure, the **Widget** widget application is packaged with the **App** UI application. The **Widget** widget application indicates this with the **\[with App\]** text.

    ![Widget application reference](media/widget_app_reference_w.png)

<a name="build"></a>
## Building Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, you must build the application. The building process performs a validation check and compiles your JavaScript and CSS files.

You can build the application in the following ways:

-   **Automatically**

    The automatic build means that the Tizen Studio automatically rebuilds the application whenever you change a source or resource file and save the application project.

    To use the automatic build:

    1.  Select the project in the **Project Explorer** view.
    2.  In the Tizen Studio menu, select **Project &gt; Build Automatically**.

        ![Using the automatic build](media/build_automatic_widget.png)

        A check mark appears next to the menu option.

    You can toggle the automatic build on and off by reselecting **Project &gt; Build Automatically**.

-   **Manually**

    The manual build means that you determine yourself when the application is built.

    To manually build the application, right-click the project in the **Project Explorer** view and select **Build Project**.

    **Figure: Manually building the application**

    ![Manually building the application](media/build_manual_w.png)

    Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

    -   In the Tizen Studio menu, select **Project &gt; Build Project**.
    -   Press the **F10** key.

After you have built the application, run it.

<a name="run"></a>
## Running Your Application

You can run the Web widget application on the [emulator](../../tutorials/process/run-debug-app.md#emulator) or a [real target device](../../tutorials/process/run-debug-app.md#target).

> **Note**  
> Since the Web Simulator does not support a circular UI, this topic does not cover the instructions for running the application on the Web Simulator.

<a name="emulator"></a>
### Running on the Emulator

To run the application on the emulator:

1.  Launch an emulator instance in the [Emulator Manager](../../../tizen-studio/common-tools/emulator-manager.md):
    1.  In the Tizen Studio menu, select **Tools &gt; Emulator Manager**.

        ![Emulator Manager](media/emulator_icon.png)

    2.  In the Emulator Manager, select a wearable emulator from the list and click **Launch**.

        If no applicable emulator instance exists, [create a new one](../../../tizen-studio/common-tools/emulator-manager.md#create).

        ![Launching the emulator](media/emulator_instance_launch_wearable.png)

        The emulator is launched in its own window. You can also see the new emulator instance and its folder structure in the **Device Manager**.

        ![Emulator](media/emulator_window_wearable.png)

2.  Generate a security profile.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3.  Run the application:
    1.  In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.

        ![Running the application](media/app_run_w.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have created multiple emulator instances, select the instance you want from the combo box in the toolbar before selecting to run the application. If you select an offline emulator, it is automatically launched when you select to run the application.

        ![Selecting the emulator to use](media/app_run_multiple_emulators.png)

    2.  Confirm that the application launches on the emulator.

        ![Application running in the emulator](media/widget_app_wearable_widget.png)

        > **Note**  
		> If the emulator display has switched off, you cannot see the application launch. To switch the display on, click the **Power** key (in the lower-right corner of the emulator).

        The above screen is shown through the Viewer, to allow you to develop a lone widget application for testing purposes.

        To see the widget running on the home screen, add the widget there:

        1.  Press the **Back** key (in the upper-right corner of the emulator device) to return to the home screen (showing a watch face).
        2.  Swipe the home screen right until you see **+ Add widget**. Select it.
        3.  Swipe right until you see your widget application. Select it.

        ![Adding to home screen](media/widget_run_add_home_ww.png)

        You can see the added widget on the home screen. To access the widget from the home screen, swipe right.

        ![Home screen widget](media/widget_app_wearable_widget.png)

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

        -   Go to **Settings &gt; Connections**, and switch on Wi-Fi.

            The device and the computer must be connected to the same Wi-Fi network.

            Note the IP address the device is using.

            ![Switch on Wi-Fi](media/emulator_target_wifi.png)

        -   Go to **Settings &gt; Gear info**, and switch on the debugging mode.

            ![Switch on debugging](media/emulator_target_debug.png)

    2.  In the terminal, enter the following commands:

        ```
        cd tizen-sdk/tools
        ./sdb connect <IP address of Gear S2>
        ```

        Use the IP address you noted before.

        Instead of the terminal, you can also use the [Remote Device Manager](../wearable/first-app.md#remote_device) for the connection.

    3.  In the first attempt, the connection fails and the device asks for user confirmation. To allow Gear to read log data, copy files to and from your computer, and install the application manually, click the accept mark.

        ![Allow Gear to access data](media/remote_allow_gear_ww.png)

    4.  In the **Device Manager**, confirm that the device is connected (shown in the device list).

        ![Device is connected](media/remote_connected_ww.png)

2.  Generate an author certificate.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3.  Run the application:
    1.  In the **Device Manager**, select the device.
    2.  In **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.

        ![Running the application](media/app_run_w.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have both a connected device and existing emulator instances, select the device from the combo box in the toolbar before selecting to run the application.

        ![Selecting the device to use](media/app_run_multiple_emulators.png)

    3.  Confirm that the application launches on the target device.

        Like with the [emulator](#viewer), you can add the widget to the home screen to easily access it.

    > **Note**  
	> The application is launched using the default debug run configuration. To create and use another configuration:
    > 1.  In the `Project Explorer` view, right-click the project and select `Run As > Run Configurations`.
    > 2.  In the `Run Configurations` window, click the `New Launch Configuration` icon (![New Launch Configuration icon](media/run_new_config_wn.png)), define the configuration details, and launch the application by clicking `Run`.
    >  ![Run Configurations window](media/run_configurations_w_widget.png)

<a name="ui"></a>
## Designing a Simple UI

The widget application created with the **Widget** template has a simple user interface with a text component showing the **Hello Widget** text on the screen.

The UI is created using [W3C/HTML](https://www.w3schools.com) in the `index.html` file. The W3C specifications provide HTML and CSS features for creating a user interface. With HTML, you can define the structure of the application screens, while CSS allows you to define the look and feel of the screens.

**Figure: User interface in the Widget template**

![Wearable Web Widget application](media/basic_app_running_ww_widget.png)

### Creating the Basic UI

The UI in the **Widget** template uses the HTML DOM, which is a structured model to control Web elements. It is an official W3C standard to express the document regardless of platforms or languages, and the foundation of the HTML5 APIs. The template contains the following components:

-   The `<html>` element is the top-level element of the HTML DOM tree that wraps the entire document, and it has the `<head>` and `<body>` elements as child nodes:

    ```
    <!DOCTYPE html>
    <html>
       <head>
          <!--Content-->
       </head>
       <body>
          <!--Content-->
       </body>
    </html>
    ```

-   The `<head>` element contains the information that the browser refers to when rendering the body element to interpret information, such as the title of the HTML document, and the location of the related CSS and JavaScript files:

    -   `<meta>`: Defines information, such as encoding, creator, and keywords of the document.
    -   `<style>`, `<link>`: Sets the styles of the document.
    -   `<script>`, `<noscript>`: Adds functions to the document.

    ```
    <head>
       <meta charset="UTF-8">
       <link rel="stylesheet" type="text/css" href="css/style.css"/>
       <script src="js/main.js"></script>
       <style></style>
    </head>
    ```

-   The `<body>` element defines the area displaying content on the browser screen. In this case, it defines the **Hello Widget** text component:

    ```
    <body>
       <div id="page">
          <div id="container">
             <p id="content-text">Hello Widget</p>
          </div>
       </div>
    </body>
    ```

### Modifying Existing Components with CSS

CSS (Cascading Style Sheets) specifies the layout and styling of the Web application.

There are various ways to connect CSS with HTML:

-   `style` attribute in an HTML element
-   `<link>` element in the `<head>` element
-   `@import` attribute in the CSS area
-   `<style>` element in the `<head>` element

Applying the style of an HTML element directly with the `style` attribute has the highest priority. On the other hand, creating a separate CSS file and managing it separately is convenient when it comes to applying changes in the future.

In the **Widget** template, the CSS file is connected to the HTML file using a `<link>` element in the `<head>` element:

```
<head>
   <meta charset="UTF-8">
   <link rel="stylesheet" type="text/css" href="css/style.css"/>
   <script src="js/main.js"></script>
   <style></style>
</head>
```

The following lines in the CSS code describe the styling of the text in an element with the `content-text` ID:

-   `css/style.css`:

    ```
    html, body {
       width: 100%;
       height: 100%;
       margin: 0;
       padding: 0;
    }

    #page {
       background-color: #000;
       color: #fff;
       height: 100%;
       position: relative;
       width: 100%;
    }

    #container {
       width: 100%;
       height: 100%;
    }

    #content-text {
       font-weight: bold;
       font-size: 40px;
       width: 100%;
       height: 100%;
       line-height: 360px;
       margin: 0;
       text-align: center;
    }
    ```

-   `index.html`:

    ```
    <body>
       <div id="page">
          <div id="container">
             <p id="content-text">Hello Widget</p>
          </div>
       </div>
    </body>
    ```

By default, the text uses the `#fff` color (white), defined for the `<div>` element with the `page` ID. If you change the CSS code and add a separate color for the `content-text` ID, the text color changes (in this case, to `#ff0000` red):

```
#content-text {
   font-weight: bold;
   font-size: 40px;
   width: 100%;
   height: 100%;
   line-height: 360px;
   margin: 0;
   text-align: center;
   color: #ff0000;
}
```

**Figure: Screen with a new text color**

![Screen with a new text color](media/basic_app_color_ww_widget.png)
