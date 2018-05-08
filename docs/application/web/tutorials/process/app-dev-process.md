# Web Application Development Process

Tizen provides the tools required to manage your Web application life-cycle from product conception, through development and release, to end-of-life application retirement.

**Figure: Web application development process**

![Web application development process](./media/app_dev_process_mw.png)

<a name="plan"></a>
## Planning and Designing the Application

The first step in creating a Tizen Web application is planning and designing it using the design tools of your choice.

For information on planning and designing your applications, see [Tizen Web Guides](../../guides/index.md) and [Tizen Web API References](../../api/latest/device_api/mobile/index.html).

Once you have finished the application plan and design, you are ready to create the application project.

<a name="create"></a>
## Creating the Application Project

After you have planned and designed your application, you are ready to [create the application project](creating-app-project.md) in the Tizen Studio.

The Tizen Studio provides various project templates that make it easier for you to start coding your application. When you create a new project,
you can select a specific template or sample. Based on the selection, the Tizen Web [Project Wizard](../../../tizen-studio/web-tools/project-wizard.md) automatically creates basic functionalities that the application has to implement to be able to run. The default project files and folders are also created.

<a name="set"></a>
## Setting Project Properties

After creating the application project, you can [configure the properties of the project and the Web application](setting-properties.md) to achieve the required functionality and features for your application.

<a name="design"></a>
## Designing the Application UI

You can design the application UI using the UI components defined in the [Tizen Advanced UI Framework](../../api/latest/ui_fw_api/ui_fw_api_cover.htm).

<a name="code"></a>
## Coding the Application

[Code your application](coding-app.md) in the Tizen Studio using the APIs defined in the Web [API References](../../api/latest/device_api/mobile/index.html).

Once you have finished coding your application, you are ready to build your application.

<a name="build"></a>
## Building the Application

When the Tizen Studio builds an application, the following process is executed:  
  1. Validation check for:
     - JavaScript
     - CSS
     - Privilege

  2. Compile for:
     - Coffeescript
     - Less

 > **Note**  
 > About the output files:  
 > -   Compiled coffeescript output file name is `<file name>.js`. This file is used when the project is packed to the WGT package file, but the script tag's reference path must be changed manually.
 > -   Compiled less output file name is `<file name>.css`. This file is   used when the project is packed to the WGT package file, but the script tag's reference path must be changed manually.

If the project has errors, they are shown in the **Problems** and **Project Explorer** views after the build.

You can build a Web application automatically or manually:

-   Automatic build:

    In the Tizen Studio menu, select **Project &gt; Build Automatically**.

    If you select this option, whenever the source or a resource is changed and saved, the Tizen Studio automatically recognizes any saved changes and rebuilds the project source.

-   Manual build:

    In the Tizen Studio menu, select **Project &gt; Build Project**.

    You can build your project at your convenience. If you want to use the manual build, ensure that the **Project &gt; Build Automatically** option is not selected.

  > **Note**  
  > In the manual build mode:  
  > -   Ensure that you have the latest build output before you run or debug a project.
  > -   To remove a project build output, select `Project > Clean` in the Tizen Studio menu.

 To customize the application, set the build properties:

 -   JS validation  
    Set the options in the Tizen Studio menu: **Window &gt;
    Preferences &gt; Tizen Studio &gt; Web &gt; Editor &gt; JavaScript Editor**.

 -   CSS validation  
    Set the options in Tizen Studio menu: **Window &gt; Preferences &gt; Tizen Studio &gt; Web &gt; Editor &gt; CSS Editor**.

 -   Privilege validation  
    Set the options in Tizen Studio menu: **Window &gt; Preferences &gt; Tizen Studio &gt; Web &gt; Editor &gt; Privilege**.

<a name="run"></a>
## Running and Debugging the Application

When the Tizen Studio runs or debugs the application, the following process is executed:

1.  Build automatically if no build has been created yet.
2.  Package.

    The optimization process is only executed when you execute the packaging process.

3.  Execute the application to the emulator or target device.

You can run your application in one of the following environments:

-   [Emulator](run-debug-app.md#emulator)

    The device emulator, provided with the Tizen Studio, imitates the target environment running Tizen Web applications. Using this
    replicated environment, you can test your application before deploying it to the real target device.

-   [Target device](run-debug-app.md#target)

    Running your application on a target device allows you to debug and test your application in a real-time environment.

-   [Simulator](run-debug-app.md#simulator)

    The Tizen Web simulator allows you to run application that use the Tizen Web APIs.

You can run the application smartly:

-   You can use the [Rapid Development Support (RDS)](run-debug-app.md#rds) mode to run or test faster.
-   You can use the live editing mode to test faster (debug mode does not support it).

For more information on the debugging process and tools, see [Debugging Web Applications](run-debug-app.md#debug).

<a name="package"></a>
## Packaging the Application

When the Tizen Studio packages the application, the following process is executed:

1.  Build automatically if no build has been created yet
2.  Optimize resources:
    -   Obfuscation (for JavaScript)
    -   Minification (for HTML, JavaScript, CSS, and PNG)
3.  Create the frame structure (for hybrid core applications).
4.  Make up resources (for hybrid core, font, and UI   framework applications).
5.  Handle signing.

Web application packaging process is based on the W3C packaging and
configuration.

You can package a Web application using the `web-packaging` command in the [Command Line Interface (CLI)](../../../tizen-studio/common-tools/command-line-interface.md), which is a functional tool in the Tizen Studio:  
```bash
web-packaging project.wgt project/
```

The Tizen Studio provides the functionality to package a Web application quickly in the required format and to set the package properties.

In the Tizen Studio menu, you can set the package properties in **Project &gt; Properties &gt; Tizen Studio &gt; Package** by selecting
the resources to be included in the package. For a Web application, you can set the properties in **Project &gt; Properties &gt; Tizen Studio
&gt; Package &gt; Web**:

-   **Set excluding optimization resources**

    You can minify your JavaScript, CSS, HTML, and PNG resources and put in an exclude file pattern that you do not want to optimize.

-   **Set hybrid application's main service application**

By default, the Web application package is created once. You can view the package content at any point of the application development process
by double-clicking the project `.wgt` file in the **Project Explorer** view. All the files present in the application project are displayed in
a list.

Any changes made to the files in the package content list, such as deleting files or dragging and dropping files, are not reflected in the
actual project files.

**Figure: Viewing the Web application package**

![Viewing the Web application package](./media/view_package_mw.png)

Additionally, you can [localize the Web application](setting-properties.md#localization) to support different languages and environments.

<a name="multi"></a>
## Developing Multiple Projects as a Combined Package

Tizen supports multi-project applications that combine different types of application templates in hybrid and companion applications.

<a name="hybrid"></a>
### Packaging Hybrid Applications

A hybrid application package combines a Web application and 1 or more native service applications.

To create and run a hybrid application:

1. Create a project for a [Web UI application](creating-app-project.md) and [native service application](../../../native/tutorials/process/app-dev-process.md#creating).
2. To establish a project reference between a UI and service application:  
   - In the Web UI application project context menu, select **Properties &gt; Tizen Studio &gt; Package &gt; Multi**.
   - Select the check box for the service application, and click **OK**.

    In the **Project Explorer** view, a **with &lt;Web UI application&gt;** message appears next to the service application project name for each application you have added to the package.

3. [Build](#build) and [run](#run) the Web UI application. The service application is built and executed automatically at the same time,
    and you can find a WGT file (hybrid application package) under the Web UI application project in the **Project Explorer** view.

    To modify the build configuration of the service application, see [Building the
    Application](../../../native/tutorials/process/app-dev-process.md#build).

> **Note**  
> Tizen has limited a multi-project application combination policy for device usability. If you do not follow the policy, the submission of your application to the Tizen Store can be rejected.


The following table shows the possible combinations for a hybrid multi-project. **M** means that multiple applications can be packaged as sub applications.

**Table: Combinations**
<table>
<tr>
 <th rowspan="2">Main project</th> <th colspan="4">Sub project</th>
</tr>
<tr>
   <th>UI</th>
   <th>SERVICE</th>
   <th>WATCH</th>
   <th>WIDGET</th>
</tr>
<tr>
  <td> WEB UI</td>
  <td> No </td>
  <td> M </td>
  <td> No </td>
  <td> M </td>
</tr>
<tr>
  <td> WEB SERVICE</td>
  <td> No </td>
  <td> No </td>
  <td> No </td>
  <td> No </td>
</tr>
</table>

With a hybrid application package, you can register the included applications in the Tizen Store and install, upgrade, and uninstall them using the single hybrid package. When a hybrid application package is installed, the Web application is installed by the Web installer, followed by the native installer installing native service applications.

A hybrid application package is very useful to Web applications that need background processing or monitoring. A native service application does not have a UI and can be run in the background.

The Web application and native service applications within a hybrid application package share the same package ID and data folder. Sharing application data between them is easy. Many useful inter-application APIs, such as Message Port (in
[mobile](../../api/latest/device_api/mobile/tizen/messageport.html),
[wearable](../../api/latest/device_api/wearable/tizen/messageport.html), and
[TV](../../api/latest/device_api/tv/tizen/messageport.html)
applications) and AppControl (in
[mobile](../../api/latest/device_api/mobile/tizen/application.html),
[wearable](../../api/latest/device_api/wearable/tizen/application.html), and
[TV](../../api/latest/device_api/tv/tizen/application.html)
applications), can be used in a hybrid application package.

For more information on hybrid applications and their package structure, see Hybrid Web App sample (in
[mobile](https://developer.tizen.org/development/sample/web/Hybrid/Hybrid_Web_App) and
[wearable](https://developer.tizen.org/development/sample/web/Hybrid/Hybrid_Web_App_1) applications),
[Hybrid Service sample](https://developer.tizen.org/development/sample/native/AppFW/Hybrid_Service), and
[Hybrid Application Package](../../index.md#hap).

<a name="cert"></a>
## Certifying and Publishing the Application

After you have packaged your application, you are ready to certify and publish your application.

To certify and publish your application:

-   Upload your mobile Web application to the Tizen Store, your wearable Web application to the Samsung Galaxy Apps Store, or your TV Web application to the Samsung App Store for registration.

    After the application is uploaded, the application is signed as a certified application installer package and the `<Application_name>.wgt` archive format, which contains the distributor signature, is added by the applicable store.

-   Submit your application to the applicable store for validation and publication.

    The store checks whether your application functions properly before publishing it.

For detailed instructions on how to register your application and submit it for validation and publication in the Tizen Store, see [Tizen Store Overview](https://developer.tizen.org/distribution/tizen-store-overview) and other subtopics within the **Distribution** section of the Tizen Developers site.

You can also upgrade your application after certification. If you want to withdraw your application from distribution and operation, you need to request for application retirement from the store.

<a name="upgrade"></a>
## Upgrading the Application

You can upgrade your application even after you have certified and published it at the Tizen Store, Samsung Galaxy Apps Store, or Samsung App Store.

To upgrade your application:

1.  Update your application version, and if needed the privileges, in the `config.xml` configuration file in the Tizen Studio.
2.  Update the application code as needed.
3.  If needed, update the privileges in the `config.xml` configuration file in the Tizen Studio.
4.  Build, test, and repackage the application.
5.  Register the upgraded application on the applicable store.

When a previously installed application is upgraded on a device, you can decide which data files from the old version are retained and which are deleted. The common Tizen upgrade policy is to overwrite all the application package files, while keeping the user-created files and
directories unchanged.

Once your application has reached the end of its life-cycle, you can remove it from the store.
