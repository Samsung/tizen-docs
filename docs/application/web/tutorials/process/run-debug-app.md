
# Running and Debugging Applications

You can run your application on the [emulator](#emulator) or the [target device](#target). You can also run mobile applications on the [simulator](#simulator). Use the [Rapid Development Support](#rds) feature to speed up the development tasks. If your application does not run without problems, you can [debug](#debug) it.

<a name="emulator"></a>
## Running Web Applications on the Emulator

You can debug Tizen Web applications on the [emulator](../../../tizen-studio/common-tools/emulator.md) using the **Project Explorer** view or the Tizen Studio menu.

To launch the emulator, do one of the following:

-   Use the [Emulator Manager](../../../tizen-studio/common-tools/emulator-manager.md):
    1.  Start the Emulator Manager using the Desktop (in Ubuntu) or Start menu (in Windows&reg;), or using the command line.
    2.  In the **Emulator Manager** window, select the emulator instance from the list.

        If you are using the Emulator Manager for the first time, you must create an emulator instance: click **Create**, select the platform (system image) and template (device definition), and click **Finish**.

    3.  Click **Launch**.

-   Use the [command line](../../../tizen-studio/common-tools/emulator-features.md#startup).

To run the application on the emulator, do one of the following:

-   In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.
-   In the Tizen Studio menu, go to **Run &gt; Run As &gt; Tizen Web Application**.
-   On the Tizen Studio toolbar, click **Run**.

To stop the emulator, right-click the emulator and click **Close**.

> **Note**  
> Running an emulator instance requires a minimum free disk space of 20 MB. The emulator image can occupy up to 10 GB of disk space.

<a name="target"></a>
## Running Web Applications on a Target Device

You can run Tizen Web applications on a target device using the **Project Explorer** view or the Tizen Studio menu.

To run your application on the target device:

1.  Connect the target device to your computer.
2.  Open the **Run Configurations** window by doing one of the following:
    -   In the **Project Explorer** view, right-click the project andselect **Run As &gt; Run Configurations**.
    -   In the Tizen Studio menu, go to **Run &gt; Run Configurations**.

3.  In the **Run Configurations** window, click **New Launch
    Configuration**.

    If you have not made any changes to the application source files since the last time the application was run, [Rapid Development Support (RDS)](#rds) is used to skip the package upload and make running the application faster. RDS is enabled as default. To disable it, go to **Window &gt; Preferences &gt; Tizen Studio &gt;    Rapid Development Support**.

4.  Set the timeout using the **Timeout value** slider.

    The timeout value represents the waiting time for the application launch operation. If you are using a lower configuration computer, set a higher timeout value to avoid application launch failure errors.

5.  Start the run by clicking **Run**.

    If no changes are required in the run configuration, you can also run the application on the target device by doing one of the following:

    - In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Application**.
    - In the Tizen Studio menu, go to **Run &gt; Run As &gt; Tizen Web Application**.
    - On the Tizen Studio toolbar, click **Run**.

If the Web application successfully launches on the target device, the [JavaScript Log Console View](../../../tizen-studio/web-tools/web-editor.md#js_log) is automatically launched in the Tizen Studio. The JavaScript Log Console view displays Web application JavaScript logs.

<a name="simulator"></a>
## Running Mobile Web Applications on the Simulator

You can run Tizen Web applications on the [Web Simulator](../../../tizen-studio/web-tools/web-simulator.md) using the **Project Explorer** view or the Tizen Studio menu.

> **Note**  
> The Tizen Web Simulator runs only on the Google Chrome&trade; browser. To use the Web Simulator, download and install the [Google Chrome&trade;](http://www.google.com/chrome/) browser. You can manually specify the installation location of the browser in the [simulator preferences](../../../tizen-studio/web-tools/web-simulator.md#pref).

If you are running your Web application on the Web Simulator for the first time, create a running configuration by selecting **Run &gt; Run Configurations &gt; Tizen Web Simulator Application** in the Tizen Studio menu. The running configuration contains the application launch settings.

To run your application on the Simulator, do one of the following:

-   In the **Project Explorer** view, right-click the project and select **Run As &gt; Tizen Web Simulator Application**.
-   In the Tizen Studio menu, go to **Run &gt; Run As &gt; Tizen Web Simulator Application**.
-   On the Tizen Studio toolbar, click **Run**.

When the application is launched, the Web Simulator loads the file specified in the **Content** field of the `config.xml` file. The mostly commonly specified file is `index.html`.

The simulator renders your application on the browser using the [WebKit](http://www.webkit.org/) engine. All the Google Chrome&trade; browser development features are available (by pressing the **F12** keyboard key) in the simulator, as is the [Web Inspector](../../../tizen-studio/web-tools/web-inspector.md) tool. You can leverage the advantages of the Web Simulator tool by setting the device screen size and orientation, and by sending events and messages, such as geolocation data and sensor input events, to your application for debugging it.

 <a name="debug"></a>
## Debugging Web Applications

Debugging a Web application enables you to understand its flow of control. You can debug a Web application by running it on the target device and debugging its JavaScript code. JavaScript code debugging uses the [Web Inspector](../../../tizen-studio/web-tools/web-inspector.md) tool.

To debug your application on the target device:  
1.  Connect the target device to your computer.
2.  Open the **Debug Configurations** window by doing one of the following:
    -   In the **Project Explorer** view, right-click the project and select **Debug As &gt; Debug Configurations**.
    -   In the Tizen Studio menu, go to **Run &gt; Debug Configurations**.

3.  In the **Debug Configurations** window, click **New Launch Configuration**.

    If you have not made any changes to the application source files since the last time the application was run, [Rapid Development Support (RDS)](#rds) is used to skip the package upload and make running the application faster. RDS is enabled as default. To disable it, go to **Window &gt; Preferences &gt; Tizen Studio &gt; Rapid Development Support**.

4.  Set the timeout using the **Timeout value** slider.

    The timeout value represents the waiting time for the application launch operation. If you are using a lower configuration system, set a higher timeout value to avoid application launch failure errors.

5.  Start the debugging by clicking **Debug**.

    If no changes are required in the debug configuration, you can also debug the application on the target device by doing one of the following:

    -   In the **Project Explorer** view, right-click the project and select **Debug As &gt; Tizen Web Application**.
    -   In the Tizen Studio menu, go to **Run &gt; Debug As &gt; Tizen Web Application**.
    -   On the Tizen Studio toolbar, click **Debug**.

    The Web Inspector tool is displayed in a new Google Chrome&trade; browser window. You can perform the following debugging tasks using the Web Inspector:

    -   Inspect styles
    -   Inspect the DOM
    -   Inspect resources
    -   Debug JavaScript code

    > **Note**  
    > The Web Inspector always opens in a new window. Life-cycle synchronization between the application to be debugged and the Web Inspector browser is not supported.
    >
    > Installing the Google Chrome&trade; browser on the device is mandatory for the Web Inspector to work. When the Google Chrome&trade; browser is installed on the device, the Tizen Studio automatically detects it. To select the browser path, go to `Window > Preferences > Tizen Studio > Web > Chrome`.

6.  To debug the JavaScript code, click **Sources** in the Web Inspector menu.

    You must enable debugging before debugging JavaScript code.

7.  You can also set a break point in the code by right-clicking in the marker bar area on the left side of the editor, and selecting
    **Toggle Breakpoint**.

    Once the break points are set, you can watch variables, expressions, and the current call stack. You can also control the debugging by using the following control buttons.

    **Table: Control buttons for debugging between break points**

    | Button | Description |
    | ------ | ---------- |
    | ![Resume](./media/resume.png)  | Resumes the current execution.|
    | ![Step over](./media/stepover.png) | Steps over the highlighted statement.<br> Executes the current line, and if the line contains a method, executes the method without entering it.|
    | ![Step in](./media/stepin.png)  | Steps into the highlighted statement.<br>  Executes the current line, and if the line contains a method, steps   into the method. |
    | ![Step out](./media/stepout.png)  | Steps out of the current method.|
    |  ![Deactivate all break  points](./media/deactivate.png)    |  Deactivates all break points. |

If the Web application successfully launches on the target device, the [JavaScript Log Console View](../../../tizen-studio/web-tools/web-editor.md#js_log) is automatically launched in the Tizen Studio. The JavaScript Log Console view displays Web application JavaScript logs.

<a name="rds"></a>
## Rapid Development Support

Rapid Development Support (RDS) lets you develop a Tizen application rapidly by saving deployment time.

When using RDS, the application is first launched normally. After the launch, a listener is activated to detect file modifications, additions, and deletions. Any detected file changes are sent to the target as a background process. When the application is launched again, the original packaging, transfer, and installation process is skipped, and only the changed files are reinstalled and executed.

If an error occurs during execution, the application is launched in the normal mode instead.

To launch the application in normal mode:  
1.  Package the application.
2.  Transfer the packaged file to the target.
3.  Install the packaged file in the target. If the application is
    already installed, uninstall it before the installation.

To launch the application in RDS mode:  
1.  Search for the changed files (modified, added, and deleted) and
    transfer them to the target as a background process.
2.  Reinstall the changed files.
3.  If the `config.xml` file has been modified, execute
    directory installation.

The RDS option is enabled as default. To disable it, in the Tizen Studio, go to **Window &gt; Preferences &gt; Tizen Studio &gt; Rapid Development Support**.

> **Note**  
> RDS is not supported in multi-app projects.
>
> If you want to remove an application from your device, you must manually delete the installed application as the launch process does not have an uninstall process.
