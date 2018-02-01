# Running Applications

You can run Tizen native applications on the [emulator](../../../tizen-studio/common-tools/emulator.md) using the **Project Explorer** view or the Tizen Studio menu.

To run your application on the emulator:

1. Before you run the application, you must sign your application package by generating an author certificate and registering it in the Tizen Studio.

   If you have already registered your certificate in the Tizen Studio, the signature is generated automatically while running your application.

2. Start the emulator in the **Connections** view.

3. Start the run by doing one of the following:

   - In the **Project Explorer** view, right-click the project and select **Run As > Tizen Native Application**.
   - In the Tizen Studio menu, go to **Run > Run As > Tizen Native Application**.
   - On the Tizen Studio toolbar, click **Run**.

   If the application binary does not exist, it is built automatically for the emulator.

   If many active emulator instances are connected, select the emulator to run the application from the dialog box.

4. Use the application in the emulator as you would on a target device.

   While the application is running, the Tizen Studio **Log** view shows the log, debug, and exception messages from the methods defined in the log macros.

5. To terminate the run, exit the application on the emulator.

In the emulator settings, you can change the display language settings, keyboard language settings, proxy address, and location settings. In addition, you can use the Emulator Control Panel to simulate application events (such as sensor data, incoming calls, or location data) for debugging and testing purposes.

## Rapid Development Support

Rapid Development Support (RDS) lets you develop a Tizen application rapidly by saving deployment time.

When using RDS, the application is first launched normally. After the launch, a listener is activated to detect file modifications, additions, and deletions. Any detected file changes are sent to the target as a background process. When the application is launched again, the original packaging, transfer, and installation process is skipped, and only the changed files are reinstalled and executed.

If an error occurs during execution, the application is launched in the normal mode instead.

To launch the application in normal mode:

1. Package the application.
2. Transfer the packaged file to the target.
3. Install the packaged file in the target. If the application is already installed, uninstall it before the installation.

To launch the application in RDS mode:

1. Search for the changed files (modified, added, and deleted) and transfer them to the target as a background process.
2. Reinstall the changed files.
3. If the `tizen-manifest.xml` file has been modified, execute directory installation.

The RDS option is enabled as default. To disable it, in the Tizen Studio, go to **Window > Preferences > Tizen Studio > Rapid Development Support**.

> **Note**  
> Currently, this option is not supported in multi-app projects.
