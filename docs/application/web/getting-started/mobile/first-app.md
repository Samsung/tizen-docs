# Creating Your First Tizen Mobile Web Application

**Welcome to Tizen mobile Web application development!**

A mobile Web application is basically a Web site stored on a mobile device. You can create it using Web-native languages, such as HTML5, CSS, and JavaScript.

Study the following instructions to help familiarize yourself with the Tizen [Web application development process](../../tutorials/process/app-dev-process.md) as well as using the Tizen Studio and installing the created application on the emulator or target device. With the instructions, you can create and run a basic mobile Web application, which displays some text on the screen and changes the text when the user clicks it:

1.  Before you get started with developing Tizen applications, download and install the [Tizen Studio](../../../tizen-studio/index.md).

    For more information on the installation process, see the [installation guide](../../../tizen-studio/setup/install-sdk.md).

2.  [Create a mobile Web project](#create) using the Tizen Studio.

    This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.

3.  [Build the application](#build).

    After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.

4.  [Run the application](#run).

    This step shows how you can run the application on the emulator, simulator, or a real target device.

5.  [Design a UI](#ui).

    This step shows how you can create the application UI and make small alterations to it to improve the usability of your application.

When you are developing a more complex application, you can take advantage of the [Web tools included in the Tizen Studio](../../../tizen-studio/web-tools/overview.md) to ease the tasks of creating functionality and designing the application UI.

<a name="create"></a>
## Creating a Project

The following example shows you how to create and configure a basic mobile Web application project in the Tizen Studio. An application project contains all the files that make up an application.

The following figure illustrates the application to be created:

-   On the left, the figure shows the application screen when the application starts. The screen displays the **Basic** text.

-   On the right, the figure shows the application screen after you tap the text. The screen now displays the **Tizen** text. Tapping the text area switches between the 2 texts.

**Figure: Mobile Web Basic application**

![Mobile Web Basic application](media/basic_app_running_1_mw.png) ![Mobile Web Basic application](media/basic_app_running_2_mw.png)

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

    2.  Select the profile (**Mobile**) and version from a drop-down list and click **Next**.

        The version depends on the platform version you have installed and with which you are developing the application.

        ![Selecting the profile and version](media/create_project_wizard_version.png)

    3.  Select the **Web Application** application type and click **Next**.

        ![Selecting the application type](media/create_project_wizard_app_web.png)

    4.  Select the **Basic UI** template and click **Next**.

        ![Selecting the template](media/create_project_wizard_template_mw.png)

    5.  Define the project properties and click **Finish**.

        You can enter the project name (3-50 characters) and the unique package ID. You can also select the location and working sets by clicking **More properties**.

        ![Defining properties](media/create_project_wizard_properties_mw.png)

        The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Creating Tizen Projects with Tizen Project Wizard](../../../tizen-studio/web-tools/project-wizard.md).

You can see the created project in the **Project Explorer** view. The most important files and folders include:

-   `css`: Folder for CSS files used by the application to style its content

-   `js`: Folder for JavaScript files used by the application to implement its functional logic

-   `config.xml`: Application configuration file used by the platform to install and launch the application

-   `icon.png`: Application icon file used by the platform to represent the application

-   `index.html`: Main HTML file for the layout of the application screen

**Figure: Application in the Project Explorer**

![Application in the Project Explorer](media/basic_app_project_explorer_mw.png)

> **Note**  
> You can [view and modify the application configuration](#configuration) in the Web application configuration editor. In this example, no configuration changes are required.

Your application project is now ready for further actions. Next, build the application.

<a name="configuration"></a>
### Managing the Application Configuration

To view and modify the application configuration:

1.  In the **Project Explorer** view, double-click the `config.xml` file of the application. The Tizen Studio opens the file in the Web application configuration editor.

2.  In the configuration editor, view and modify the configuration details using the various tabs:

    ![Configuring the application](media/basic_app_config_w.png)

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

        ![Using the automatic build](media/build_automatic_w.png)

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

You can run the Web application on the [emulator](../../tutorials/process/run-debug-app.md#emulator), [Web Simulator](../../tutorials/process/run-debug-app.md#simulator), or a [real target device](../../tutorials/process/run-debug-app.md#target).

<a name="emulator"></a>
### Running on the Emulator

To run the application on the emulator:

1.  Launch an emulator instance in the [Emulator Manager](../../../tizen-studio/common-tools/emulator-manager.md):
    1. In the Tizen Studio menu, select **Tools &gt; Emulator Manager**.

        ![Emulator Manager](media/emulator_icon.png)

    2.  In the Emulator Manager, select a mobile emulator from the list and click **Launch**.

        If no applicable emulator instance exists, [create a new one](../../../tizen-studio/common-tools/emulator-manager.md#create).

        ![Launching the emulator](media/emulator_instance_launch.png)

        The emulator is launched in its own window. You can also see the new emulator instance and its folder structure in the **Device Manager**.

        ![Emulator](media/emulator_window_mobile.png)

2.  Generate a security profile.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3.  Run the application:
    1. In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.

        ![Running the application](media/app_run_w.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have created multiple emulator instances, select the instance you want from the combo box in the toolbar before selecting to run the application. If you select an offline emulator, it is automatically launched when you select to run the application.

        ![Selecting the emulator to use](media/app_run_multiple_emulators.png)

    2.  Confirm that the application launches on the emulator.

        ![Application running in the emulator](media/emulator_running_mw.png)

        > **Note**  
        > If the emulator display has switched off, you cannot see the application launch. To see the application on the emulator screen:
        > 1. To switch the display on, in the key window next to the emulator screen, click `Power`.
        > 2.  On the home screen, swipe left.

        While the application is running, the **Log** view in the Tizen Studio shows the log, debug, and exception messages from the methods defined in the log macros. To see the view, in the Tizen Studio menu, go to **Window &gt; Show View &gt; Log**.

For more information on using the emulator features, see [Using Emulator Control Keys, Menu, and Panel](../../../tizen-studio/common-tools/emulator-control-panel.md) and [Using Extended Emulator Features](../../../tizen-studio/common-tools/emulator-features.md).

<a name="simulator"></a>
### Running on the Web Simulator

To run the application on the Web Simulator:

1.  In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Simulator Application**.

    ![Running the application](media/simulator_run_mw.png)

    Alternatively, you can also select the project in the **Project Explorer** view and click the run icon in the toolbar.

2.  Confirm that the application launches on the Web Simulator.

    ![Application running in the Web Simulator](media/simulator_running_mw.png)

For more information on using the Web Simulator features, see [Taking Advantage of Web Simulator Features](../../../tizen-studio/web-tools/web-simulator-features.md).

<a name="target"></a>
### Running on a Target Device

To run the application on a target device:

1.  Connect the mobile target device to your computer using a USB cable.
2.  Generate an author certificate.

    Before you run the application, you must [sign your application package with a certificate profile](../../../tizen-studio/common-tools/certificate-registration.md) in the Tizen Studio.

3.  Run the application:
    1. In the **Device Manager**, select the device.
    2.  In **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.

        ![Running the application on a target device](media/app_run_w.png)

        Alternatively, you can also select the project in the **Project Explorer** view and do one of the following:

        -   Press the **Ctrl + F11** key.
        -   Click the run icon in the toolbar.

        If you have both a connected device and existing emulator instances, select the device from the combo box in the toolbar before selecting to run the application.

        ![Selecting the device to use](media/app_run_multiple_emulators.png)

    3.  Confirm that the application launches on the target device.

    > **Note**  
	> The application is launched using the default debug run configuration. To create and use another configuration:
    > 1. In the `Project Explorer` view, right-click the project and select `Run As > Run Configurations`.
    > 2.  In the `Run Configurations` window, click the `New Launch Configuration` icon (![New Launch Configuration icon](media/run_new_config_wn.png)), define the configuration details, and launch the application by clicking `Run`.
    > ![Run Configurations window](media/run_configurations_w.png)

<a name="ui"></a>
## Designing a Simple UI

The mobile application created with the **Basic UI** template has a simple user interface with a text component showing the **Basic** text in the middle of the screen.

The UI is created using [W3C/HTML](https://www.w3schools.com). The W3C specifications provide HTML and CSS features for creating a user interface. With HTML, you can define the structure of the application screens, while CSS allows you to define the look and feel of the screens.

**Figure: User interface in the Basic UI template**

![User interface in the Basic template](media/basic_app_running_1_mw.png)

### Creating the Basic UI

The UI in the **Basic UI** template uses the HTML DOM, which is a structured model to control Web elements. It is an official W3C standard to express the document regardless of platforms or languages, and the foundation of the HTML5 APIs. The template contains the following components:

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

    -   `<title>`: Defines the title of the document.
    -   `<meta>`: Defines information, such as encoding, creator, and keywords of the document.
    -   `<style>`, `<link>`: Sets the styles of the document.
    -   `<script>`, `<noscript>`: Adds functions to the document.

    ```
    <head>
       <meta charset="utf-8"/>
       <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
       <meta name="description" content="Tizen Mobile Web Basic Template"/>

       <title>Tizen Mobile Web Basic Application</title>

       <link rel="stylesheet" type="text/css" href="css/style.css"/>
       <script src="js/main.js"></script>
    </head>
    ```

-   The `<body>` element defines the area displaying content on the browser screen. In this case, it defines the **Basic** text component:

    ```
    <body>
       <div id="main" class="page">
          <div class="contents">
             <span id="content-text">Basic</span>
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

In the **Basic UI** template, the CSS file is connected to the HTML file using a `<link>` element in the `<head>` element:

```
<head>
   <meta charset="utf-8"/>
   <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
   <meta name="description" content="Tizen Mobile Web Basic Template"/>

   <title>Tizen Mobile Web Basic Application</title>

   <link rel="stylesheet" type="text/css" href="css/style.css"/>
   <script src="js/main.js"></script>
</head>
```

The following lines in the CSS code describe the styling of the text in an element with the `content-text` ID:

-   `css/style.css`:

    ```
    #content-text {
       font-weight: bold;
       font-size: 5em;
    }
    ```

-   `index.html`:

    ```
    <body>
       <div id="main" class="page">
          <div class="contents">
             <span id="content-text">Basic</span>
          </div>
       </div>
    </body>
    ```

By default, the text uses the `#ffffff` color (white), defined for the `<body>` element. If you change the CSS code and add a separate color for the `content-text` ID, the text color changes (in this case, to `#ff0000` red):

```
#content-text {
   font-weight: bold;
   font-size: 5em;
   color: #ff0000;
}
```

**Figure: Screen with a new text color**

![Screen with a new text color](media/build_ui_basic_textbox_mw.png)

### Adding More Components and Functionality with TAU

TAU (Tizen Advanced UI) is a Web UI library that enables you to create and manage various kinds of UI components. The components represent a visual UI element, such as a button, checkbox, or list view. You can manipulate and interact with the application screens through the UI components. For more information, see [Tizen Advanced UI](../../guides/tau/tau.md) and [Tizen Advanced UI framework Reference](../../api/latest/ui_fw_api/ui_fw_api_cover.htm).

TAU helps you to create Tizen Web applications easily. The following figure shows the role of TAU and its relation to the Web application.

**Figure: TAU and the Web application**

![TAU and the Web application](media/simple_ui_tau_relation_mw.png)

The UI in the **Basic UI** template only contains one visible text component. To create a more elaborate UI with more components, screens, and functionality, use the TAU library in your application. The following example shows how to create a list and a footer button on a page (screen), create a second page, and move between the pages.

To create a Web application and design its UI with TAU:

1.  Install TAU templates.

    The Tizen Studio comes with the Package Manager tool, which you can use to install the TAU packages required for TAU application development.

    Make sure that you have the **TAU (IDE)** package installed to enable you to create the Web application using a TAU template.

    ![TAU package installation](media/simple_ui_update_mgr_mw.png)

2.  Create a project that uses the TAU library.

    To create a project with a **TAU SinglePage** template:

    1.  Go to **File &gt; New &gt; Tizen Project**.
    2.  Select **Template &gt; Mobile v4.0 &gt; Web Application &gt; TAU SinglePage**.

        ![Creating a new project](media/simple_ui_tau_create_mw.png)

    3.  Define the project properties and click **Finish**.

        ![Changing properties](media/simple_ui_tau_properties_mw.png)

    4.  In the **Project Explorer** view, view the project.

        The TAU library is located in the `lib` folder.

        ![TAU library directory](media/simple_ui_tau_dir_mw.png)

    You can create a new project using a TAU template or a TAU sample application included in the Tizen Studio, as shown above, or you can add the required TAU libraries to any existing Web project.

    To import TAU manually to an existing project to load the basic Tizen Advanced UI (TAU) libraries, use the following elements in your HTML file:

    -   Import the TAU library with the `<script>` element: `tau(.min).js`

        This element is mandatory, since you need the TAU library to use the TAU JavaScript Interface.

    -   Import the TAU theme with the `<link>` element: `tau(.min).css`

        This element is also mandatory.

    For better performance, all CSS files must be included in the header and all script elements must be put before the closing `</body>` element. The following example shows the **TAU SinglePage** template where the application title has been modified:

    ```
    <!DOCTYPE html>
    <html>
       <head>
          <meta name="viewport" content="width=device-width, user-scalable=no"/>
          <link rel="stylesheet" href=".lib/tau/mobile/theme/default/tau.css"/>
          <link rel="stylesheet" type="text/css" href="css/style.css"/>
          <title>Hello TAU</title>
       </head>
       <body>
          <!--HTML BODY CONTENT-->
          <script type="text/javascript" src="lib/tau/mobile/js/tau.js"></script>
          <script src="./js/main.js"></script>
       </body>
    </html>
    ```

    You can add additional `<script src="<CUSTOM_LIBRARY_OR_JS_FILE>">` or `<link rel="stylesheet" src="<CUSTOM_CSS>">` elements to include your own scripts and style sheets. However, place them after the default `<script>` elements, so that you can use any TAU APIs provided by the default libraries.

3.  Create the first page.
    1. Open the `index.html` file. By default, the `<body>` element of the HTML file contains 1 page (`<div>` element with the `ui-page` class) which contains a header (`<div>` element with the `ui-header` class) and a content section (`<div>` element with the `ui-content` class).

        ```
        <body>
           <div class="ui-page" id="main">
              <div class="ui-header">
                 <h1>Single-page application </h1>
              </div><!-- /header -->

              <div class="ui-content">
                 <p>This is a single page boilerplate template that you can copy to build your first Tizen Web UI Framework page.</p>
              </div><!-- /content -->
           </div><!-- /page -->

           <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
           <script src="./js/main.js"></script>
        </body>
        ```

        To lay out the page, edit the contents of the header and content blocks, and add a footer with the `ui-footer` class:

        ```
        <div class="ui-page" id="main">
           <div class="ui-header" data-position="fixed">
              <h1>Hello World</h1>
           </div>

           <div class="ui-content">
              <p>This is content area</p>
           </div>
           <div class="ui-footer">
              <p>This is footer area</p>
           </div>
        </div>
        ```

        ![Hello World page](media/simple_ui_hello_tau_mw.png)

    2.  You can add your own styles for the content and footer areas with defined `id` attributes:

        ```
        <body>
           <div class="ui-page" id="main">
              <div class="ui-header" data-position="fixed">
                 <h1>Hello World</h1>
              </div>

              <div class="ui-content" id="contentArea">
                 <p>This is content area</p>
              </div>
              <div class="ui-footer" id="footerArea">
                 <p>This is footer area</p>
              </div>
           </div>

           <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
           <script src="./js/main.js"></script>
        </body>
        ```

        In the `style.css` file, add CSS styles for the new `id` attributes:

        ```
        #contentArea {
           background-color: white;
        }
        #footerArea {
           background-color: blue;
        }
        ```

        The above new styles modify the screen to show a while background for the content area, and a blue one for the footer.

        ![Hello World page with custom styles](media/simple_ui_tau_css_mw.png)

4.  Create more content for the first page:
    -   Add a list.

        You can add a list with the TAU list view component using the `<ul>` element and the `ui-listview` class:

        -   Create a basic static list by overwriting the page content in the `index.html` file with the following code:

            ```
            <body>
               <div class="ui-page" id="main">
                  <div class="ui-header" data-position="fixed">
                     <h1>Hello TAU</h1>
                  </div>
                  <div class="ui-content">
                     <ul class="ui-listview">
                        <li class="ui-li-static">List Item1</li>
                        <li class="ui-li-static">List Item2</li>
                        <li class="ui-li-static">List Item3</li>
                        <li class="ui-li-static">List Item4</li>
                     </ul>
                  </div>
               </div>

               <script type="text/javascript" src="./lib/tau/mobile/js/tau.js"></script>
               <script src="./js/main.js"></script>
            </body>
            ```

            ![TAU list](media/simple_ui_tau_list_mw.png)

        -   For a more advanced option, you can also create an anchor list view (whose items can be clicked to navigate to other pages or show a popup). The list items (`<li>` elements) differ from the basic list by having an additional `<a>` element in them:

            ```
            <div class="ui-page" id="main">
               <div class="ui-header" data-position="fixed">
                  <h1>Hello TAU</h1>
               </div>
               <div class="ui-content">
                  <ul class="ui-listview">
                     <li class="ui-li-anchor"><a href="#">Anchor List 1</a></li>
                     <li class="ui-li-anchor"><a href="#">Anchor List 2</a></li>
                     <li class="ui-li-anchor"><a href="#">Anchor List 3</a></li>
                     <li class="ui-li-anchor"><a href="#">Anchor List 4</a></li>
                  </ul>
               </div>
            </div>
            ```

            ![TAU anchor list](media/simple_ui_tau_anchor_list_mw.png)

    -   Add a button in the footer.

        When implementing Tizen mobile Web applications, you can use the `ui-footer` class as a footer area. You can add 1 or 2 buttons to the footer area, by using the `<button>` elements.

        ```
        <div class="ui-page" id="main">
           <div class="ui-header" data-position="fixed">
              <h1>Hello TAU</h1>
           </div>
           <div class="ui-content">
              <!--Content area with a list-->
           </div>
           <div class="ui-footer">
              <button>OK</button>
           </div>
        </div>
        ```

        ![TAU button](media/simple_ui_tau_button_mw.png)

5.  Create the second page.

    1. In the Tizen Studio, create a new HTML file and name it `second.html`.

        Add the following content to the file to create a title text in the header and a **Hello Tizen!** text in the content area:

        ```
        <!DOCTYPE html>
        <html>
           <head>
              <title>Hello TAU</title>
              <link rel="stylesheet" href="lib/tau/mobile/theme/default/tau.css">
           </head>
           <body>
              <div class="ui-page" id="second">
                 <div class="ui-header" data-position="fixed">
                    <h1>Second Page</h1>
                 </div>
                 <div class="ui-content" id="secondPage">
                    <p>Hello Tizen!</p>
                 </div>
              </div>
              <script type="text/javascript" src="lib/tau/mobile/js/tau.js" data-build-remove="false"></script>
           </body>
        </html>
        ```

    2.  Decorate the page in the same way as `index.html`. In the `style.css` file, add the following CSS style to set the content area background to white:

        ```
        #secondPage {
           background-color: white;
        }
        ```

    ![Second page](media/simple_ui_tau_second_mw.png)

6.  Create navigation between the pages.
    -   To navigate from the first page to the second, in the anchor list in the `index.html` file, add the path to the second page in the `<li><a href>` element:

        ```
        <ul class="ui-listview">
           <li class="ui-li-anchor"><a href="second.html">Go to Second Page</a></li>
           <li class="ui-li-anchor"><a href="#">Anchor List 2</a></li>
           <li class="ui-li-anchor"><a href="#">Anchor List 3</a></li>
           <li class="ui-li-anchor"><a href="#">Anchor List 4</a></li>
        </ul>
        ```

        Run the application in the emulator, and click the **Go to Second Page** link to move from the `index.html` page to the `second.html` page.

        ![Move to the second page](media/simple_ui_tau_move_mw.png)

    -   To navigate from the second page back to the first, use the **Back** key.

        You can navigate from page to page with the `<a href="PAGE_FILE_NAME">` elements, but you cannot go back. To enable the user to return to the first page, you must add some code in a JavaScript file.

        Create a new `app.js` JavaScript file:

        1. In the `index.html` file, add the `<script src="app.js"></script>` line before closing the `</body>` element:

            ```
            <body>
               <div class="ui-page" id="main">
                  <div class="ui-header" data-position="fixed">
                     <h1>Hello TAU</h1>
                  </div>
                  <div class="ui-content">
                     <!--Content-->
                  </div>
                  <div class="ui-footer">
                     <button>OK</button>
                  </div>
               </div>
               <script type="text/javascript" src="lib/tau/mobile/js/tau.js"></script>
               <script src="app.js"></script>
            </body>
            ```

        2.  In the **Project Explorer** view, right-click the project and select **New &gt; JavaScript Source File**.

            ![Create a new JavaScript file](media/simple_ui_tau_new_js_mw.png)

        3.  Enter the file name as **app.js** and click **Finish**.
        4.  In the `app.js` file, all kinds of logic can be added to the application. In this case, add the code for returning to the previous page when the **Back** key is pressed:

            ```
            (function() {
                window.addEventListener('tizenhwkey', function(ev) {
                    if (ev.keyName === 'back') {
                        var page = document.getElementsByClassName('ui-page-active')[0],
                            pageid = page ? page.id : '';

                        if (pageid !== 'main') {
                            window.history.back();
                        }
                    }
                });
            }());
            ```

    -   To exit the application.

        You can make your application exit by adding more lines to the `app.js` file.

        You have to consider the fact that when the user clicks the **Back** key, the application can only exit if it is showing the first page. If the second page is showing, the application must return to the first page.

        The following example shows how to handle the **Back** key input with page navigation and application exit. Similar code is included in the **TAU SinglePage** project template `main.js` file by default.

        ```
        (function() {
            window.addEventListener('tizenhwkey', function(ev) {
                if (ev.keyName === 'back') {
                    var page = document.getElementsByClassName('ui-page-active')[0],
                        pageid = page ? page.id : '';

                    if (pageid === 'main') {
                        try {
                            tizen.application.getCurrentApplication().exit();
                        } catch (ignore) {}
                    } else {
                        window.history.back();
                    }
                }
            });
        }());
        ```
