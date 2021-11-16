# Create Your First Samsung Smart TV Web Application

**Welcome to Samsung Smart TV Web application development!**

A Samsung TV Web application is basically a Web site stored on a Samsung Smart TV. You can create it using Web-native languages, such as HTML5, CSS, and JavaScript.

Study the following instructions to help familiarize yourself with the Tizen [Web application development process](../../tutorials/process/app-dev-process.md) as well as using Tizen Studio and installing the created application on the emulator or target device. With the instructions, you can create and run a basic TV Web application, which displays some text on the screen and changes the text when the user clicks it:

**Set up Tizen Studio and TV Extention**

1.  Before you get started with developing Tizen applications, download and install the [Tizen Studio](../../../tizen-studio/index.md).

    For more information on the installation process, see the [installation guide](../../../tizen-studio/setup/install-sdk.md).

2.  Update Extension SDK with the Package Manager to install the TV Extension, which provides TV emulator.

    1. Launch the Package Manager.

    2. Select **Extension SDK** tab on Package Manager, click **install** next to **TV Extension**. The Package Manager installs all packages that are required for **TV Extension**.

       ![install TV Extension](./media/install_tv_extension.png)

       For more information on updating packages, see [Updating Tizen Studio](../../../tizen-studio/setup/update-sdk.md).

**Build your first application**

1. [Create a TV Web project](#create) using Tizen Studio.

    This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.

2. [Build the application](#build).

    After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.

3. [Run the application](#run).

    This step shows how you can run the application on the emulator, simulator, or a real target device.

4. [Design a UI](#ui).

    This step shows how you can create the application UI and make small alterations to it to improve the usability of your application.

When you are developing a more complex application, you can take advantage of the [Web tools included in Tizen Studio](../../../tizen-studio/web-tools/index.md) to ease the tasks of creating functionality and designing the application UI.

<a name="create"></a>
## Create a Project

The following example shows you how to create and configure a basic Samsung TV Web application project in Tizen Studio. An application project contains all the files that make up an application.

To create the application project:

1.  Launch Tizen Studio.

2. In the Tizen Studio menu, select **File \> New \> Tizen Project**.

    ![Create a new Tizen Web project](media/create_project_1.png)

    The Project Wizard opens.

3. In the Project Wizard, define the project details.

    The Project Wizard is used to create the basic application skeleton with the required folder structure and mandatory files. You can easily create different applications by selecting an applicable template or sample for the Project Wizard to use.

    1. Select the **Template** project type and click **Next**.

        ![Selecting the project type](media/create_project_wizard_type.png)

    2. Select the profile (**Custom**) and version from a drop-down list and click **Next**.

        The version depends on the platform version you have installed and with which you are developing the application.

        ![Selecting the profile and version](media/create_project_wizard_version_samsung_tv.png)

    3. Select the **Web Application** application type and click **Next**.

        ![Selecting the application type](media/create_project_wizard_app_samsung_tv.png)

    4. Select the **Basic Project** template and click **Next**.

        ![Selecting the template](media/create_project_wizard_template_samsung_tv.png)

    5. Define the project properties and click **Finish**.

        You can enter the project name (3-50 characters) and the unique package ID. You can also select the location and working sets by clicking **More properties**.

        ![Defining properties](media/create_project_wizard_properties_samsung_tv.png)

        The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Create Tizen Projects with Tizen Project Wizard](../../../tizen-studio/web-tools/project-wizard.md).

You can see the created project in the **Project Explorer** view. The most important files and folders include:

-   `css`: Folder for CSS files used by the application to style its content

-   `js`: Folder for JavaScript files used by the application to implement its functional logic

-   `config.xml`: Application configuration file used by the platform to install and launch the application

-   `icon.png`: Application icon file used by the platform to represent the application

-   `index.html`: Main HTML file for the layout of the application screen

![Application in the Project Explorer](media/project_explorer_samsung_tv.png)

> [!NOTE]
> You can [view and modify the application configuration](#configuration) in the Web application configuration editor. In this example, no configuration changes are required.

Your application project is now ready for further actions. Next, build the application.

<a name="configuration"></a>
### Manage the Application Configuration

To view and modify the application configuration:

1.  In the **Project Explorer** view, double-click the `config.xml` file of the application. Tizen Studio opens the file in the Web application configuration editor.

2. In the configuration editor, view and modify the configuration details using the various tabs:

    ![Configuring the application](media/basic_app_config_samsung_tv.png)

    - **Overview**: Define general information, such as the name and icon of the application.

    - **Features**: Define required software and hardware features. This information is used for application filtering in Tizen Store.

    - **Privileges**: Define the security-sensitive APIs or API groups accessed and used by the application.

    - **Localization**: Define localized values for the application name, description, and license.

    - **Policy**: Request network resource permissions to access external network resources.

    - **Preferences**: Define name-value pairs that can be set or retrieved through the application.

    - **Tizen**: Edit the Tizen schema extension properties of the application.

    - **Source**: View and edit the source code of the `config.xml` file. Changes made and saved on the other tabs are reflected in the source code and vice versa.

        > [!NOTE]
        > The `config.xml` file must conform to both the XML file format and the W3C specification requirements. Editing the file in the **Source** tab is intended for advanced users only.

3. To save any changes, in the Tizen Studio menu, select **File \> Save All**.

For more information on configuring the application, see [Setting the Web Application Configuration](../../tutorials/process/setting-properties.md#set_widget).

<a name="build"></a>
## Build Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, you must build the application. The building process performs a validation check and compiles your JavaScript and CSS files.

You can build the application in the following ways:

- **Automatically**

    The automatic build means that Tizen Studio automatically rebuilds the application whenever you change a source or resource file and save the application project.

    To use the automatic build:

    1.  Select the project in the **Project Explorer** view.
    2. In the Tizen Studio menu, select **Project \> Build Automatically**.

        ![Using the automatic build](media/build_automatic_samsung_tv.png)

        A check mark appears next to the menu option.

    You can toggle the automatic build on and off by reselecting **Project \> Build Automatically**.

- **Manually**

    The manual build means that you determine yourself when the application is built.

    To manually build the application, right-click the project in the **Project Explorer** view and select **Build Project**.

    ![Manually building the application](media/build_manual_samsung_tv.png)

    Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

    -   In the Tizen Studio menu, select **Project \> Build Project**.
    -   Press the **F10** key.

After you have built the application, run it.

<a name="run"></a>
## Run Your Application

You can run the Web application on the [emulator](../../tutorials/process/run-debug-app.md#emulator), [Samsung TV Simulator](http://developer.samsung.com/tv/develop/getting-started/using-sdk/tv-simulator), or a [real target device](../../tutorials/process/run-debug-app.md#target).

<a name="emulator"></a>
### Run on the Emulator

To run the application on the emulator:

1. Launch an emulator instance in the [Emulator Manager](../../../tizen-studio/common-tools/emulator-manager.md):

    1. In the Tizen Studio menu, select **Tools \> Emulator Manager**.

        ![Emulator Manager](media/emulator_icon.png)

    2. In the Emulator Manager, select a TV emulator from the list and click **Launch**.

        If no applicable emulator instance exists, [create a new one](../../../tizen-studio/common-tools/emulator-manager.md#create).

        ![Launching the emulator](media/emulator_instance_launch_samsung_tv.png)

2. Generate a security profile.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in Tizen Studio.

3. Run the application:
    1. In the **Project Explorer** view, right-click the project and select **Run As \> Tizen Web Application**.

        ![Running the application](media/run_as_web_app_samsung_tv.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have created multiple emulator instances, select the instance you want from the combo box in the toolbar before selecting to run the application. If you select an offline emulator, it is automatically launched when you select to run the application.

        ![Selecting the emulator to use](media/app_run_multiple_emulators_samsung_tv.png)

    2. Confirm that the application launches on the emulator.

        ![Application running in the emulator](media/emulator_basic_app_samsung_tv.png)

        While the application is running, the **Log** view in Tizen Studio shows the log, debug, and exception messages from the methods defined in the log macros. To see the view, in the Tizen Studio menu, go to **Window \> Show View \> Log**.

For more information on using the emulator features, see [Using Emulator Control Keys, Menu, and Panel](../../../tizen-studio/common-tools/emulator-control-panel.md) and [Using Extended Emulator Features](../../../tizen-studio/common-tools/emulator-features.md).

<a name="simulator"></a>
### Run on the Samsung TV Simulator

To run the application on the simulator:

1.  In the **Project Explorer** view, right-click the project and select **Run As \> Tizen Web Simulator Application (Samsung TV)**.

    ![Running the application](media/run_as_web_simulator_samsung_tv.png)

2. Confirm that the application launches on the simulator.

    ![Application running in the simulator](media/simulator_basic_app_samsung_tv.png)

For more information on using the simulator features, see [TV Simulator](http://developer.samsung.com/tv/develop/getting-started/using-sdk/tv-simulator).

<a name="target"></a>
### Run on a Target Device

To run the application on a target device:

1. Connect the TV target device to your computer:

    1. Define settings on the TV:

        1. Start the TV, press the **Smart Hub** key, and select **Apps**.
        2. In the **Apps** panel, enter the "Magic sequence" (keys **1**, **2**, **3**, **4**, and **5** in sequence).
        3. Set the **Developer mode** to **On**, and enter the IP address of your computer.
        4. Click **OK** and reboot the TV.

    2. In Tizen Studio, use the Remote Device Manager to connect the TV:

        1. In the **Device Manager**, click the **Remote Device Manager** button.

            ![Launch the Remote Device Manager](media/remote_conn_mgr.png)

        2. In the **Remote Device Manager** window, click **+**.

            ![Add new device](media/remote_conn_new_ww.png)

        3. In the **Add Device** window, enter the device and network details, and click **Add**.

            ![Define device details](media/remote_conn_add_ww.png)

        4. In the **Remote Device Manager** window, switch the new device on by clicking the switch under **Connect**.

            ![Connect the device](media/remote_connect_ww.png)

    3. In the **Device Manager**, confirm that the device is connected (shown in the device list).

        ![Device is connected](media/remote_connected_ww.png)

    4. Right-click the device and select **Permit to install application**.

2. Generate an author certificate.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in Tizen Studio.

3. Run the application:
    1.  In the **Device Manager**, select the device.
    2. In **Project Explorer** view, right-click the project and select **Run As \> Tizen Web Application**.

        ![Running the application on a target device](media/run_as_web_app_samsung_tv.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have both a connected device and existing emulator instances, select the device from the combo box in the toolbar before selecting to run the application.

        ![Selecting the device to use](media/app_run_multiple_emulators.png)

    3. Confirm that the application launches on the target device.

    > [!NOTE]
    > The application is launched using the default debug run configuration. To create and use another configuration:
    > 1.  In the `Project Explorer` view, right-click the project and select `Run As > Run Configurations`.
    > 2.  In the `Run Configurations` window, click the `New Launch Configuration` icon (![New Launch Configuration icon](media/run_new_config_wn.png)), define the configuration details, and launch the application by clicking `Run`.
    >    ![Run Configurations window](media/run_configurations_samsung_tv.png)

<a name="ui"></a>
## Design Your UI

The Samsung TV application created with the **Basic Project** template has a simple user interface with basic HTML and JavaScript.

The UI is created using [W3C/HTML](https://www.w3schools.com). The W3C specifications provide HTML and CSS features for creating a user interface. With HTML, you can define the structure of the application screens, while CSS allows you to define the look and feel of the screens.

### Edit HTML

The UI in the **Basic Project** template uses the HTML DOM, which is a structured model to control Web elements. It is an official W3C standard to express the document regardless of platforms or languages, and the foundation of the HTML5 APIs. The template contains the following components:

-   The `<html>` element is the top-level element of the HTML DOM tree that wraps the entire document, and it has the `<head>` and `<body>` elements as child nodes:

    ```html
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

- The `<head>` element contains the information that the browser refers to when rendering the body element to interpret information, such as the title of the HTML document, and the location of the related CSS and JavaScript files:

    -   `<title>`: Defines the title of the document.
    -   `<meta>`: Defines information, such as encoding, creator, and keywords of the document.
    -   `<style>`, `<link>`: Sets the styles of the document.
    -   `<script>`, `<noscript>`: Adds functions to the document.

    ```
    <head>
        <meta charset="utf-8" />
        <meta name="description" content="Tizen basic template generated by Tizen Web IDE"/>
        <title>Tizen Web IDE - Tizen - Samsung Tizen TV basic Application</title>
        <link rel="stylesheet" type="text/css" href="css/style.css"/>
        <script src="js/main.js"></script>
    </head>
    ```

- The `<body>` element defines the area displaying content on the browser screen. In this case, it defines the **Basic** text component:

    ```html
    <body>
      <header>
        <hgroup>
           ...
        </hgroup>
      </header>

      <nav>
        <ul>
           <li><a href="#">Home</a></li>
           <li> ... </li>
        </ul>
      </nav>

      <article>
        <header>
           ...
        </header>
        <section>
           ...
          <div id="divbutton1" style="font-size:40px;">
            <button onclick="startTime();" style="font-size:50px;">Clock</button>
          </div>
        </section>
      </article>

      <footer>
        <p>&copy; 2015 Company Name. All rights reserved.</p>
      </footer>
    </body>
    ```

### Edit CSS

CSS (Cascading Style Sheets) specifies the layout and styling of the Web application.

There are various ways to connect CSS with HTML:

-   `style` attribute in an HTML element
-   `<link>` element in the `<head>` element
-   `@import` attribute in the CSS area
-   `<style>` element in the `<head>` element

Applying the style of an HTML element directly with the `style` attribute has the highest priority. On the other hand, creating a separate CSS file and managing it separately is convenient when it comes to applying changes in the future.

In the **Basic Project** template, the CSS file is connected to the HTML file using a `<link>` element in the `<head>` element:

```html
<head>
   <link rel="stylesheet" type="text/css" href="css/style.css"/>
</head>
```

The following lines in the CSS code describe the styling of the navigation bar in an element with the `nav` class:

```css
nav ul {
    list-style: none;
    padding: 20px;
    display: block;
    clear: right;
    background-color: #666;
    padding-left: 4px;
    height: 48px;
}
```

The background is colored gray (`#666`). To change the color of the background, change the CSS code by modifying the `color` attribute (in this case, it is changed to `#d3d3d3` to make the background of navigation bar):

```css
nav ul {
    list-style: none;
    padding: 20px;
    display: block;
    clear: right;
    background-color: #d3d3d3;
    padding-left: 4px;
    height: 48px;
}
```

### Edit JavaScript

JavaScript is the programming language of HTML and the Web.

In the **Basic Project** template, the js file is included to the HTML file using a `<script>` element in the `<head>` element:

```html
<head>
   <script src="js/main.js"></script>
</head>
```

The following lines in the JavaScript code define `startTime()` function executed when the HTML is loading:
```js
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('divbutton1').innerHTML='Current time: ' + h + ':' + m + ':' + s;
    setTimeout(startTime, 10);
}
```

The current time shows as 24-hour format, between 0 and 23, in the **Basic Project** template. You can convert 24-hour to 12-hour format:
```js
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    console.log(h);
    if ( (h  / 12) >= 1 ) {
        meri = ' PM';
    }
    else {
        meri = ' AM';
    }

    h = h % 12;
    if ( h == 0 ) {
        h = 12;
    }
    m = checkTime(m);
    s = checkTime(s);

    document.getElementById('divbutton1').innerHTML='Current time: ' + h + ':' + m + ':' + s + ' ' + meri;
    setTimeout(startTime, 10);
}
```

![Application screen with the new text color](media/emulator_basic_project_samsung_tv.png)
