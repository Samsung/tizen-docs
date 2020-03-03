# Visual Studio Code Extension for Tizen .NET

Visual Studio Code Extension for Tizen (VS Code Extension for Tizen) is a Visual Studio Code extension that enables you to develop Tizen .NET applications easily using Visual Studio Code. This topic covers 2 different ways to perform the installation: installing from the Marketplace or installing from a VSIX file.

Before installing VS Code Extension for Tizen, check [Prerequisites of Visual Studio Code Extension for Tizen](index.md).

## Install from Marketplace

To install VS Code Extension for Tizen from the Visual Studio Code Marketplace:

1. In Visual Studio Code, at the bottom of the **Activity Bar**, click the **Extensions** icon.

   ![Visual Studio Code Marketplace](media/vscode_marketplace.png)

2. In the **Extensions** view's **Search Extensions in Marketplace** field, enter **Tizen**.
3. Locate **Visual Studio Code Extension for Tizen** in the search results and click **Install**.
4. After the installation is complete, activate the extension by clicking **Reload**.
5. Once the extension has been activated, it asks whether you want to use an existing Tizen Baseline SDK installation or install a new one:

   ![Visual Studio Code Marketplace](media/vscode_baselinesdk_exists.png)

   - To perform a fresh installation, click **NO**.

     The extension suggests the path where to install the Tizen Baseline SDK. Click **YES** to proceed.

     > [!NOTE]
     > If you click **NO**, you must finish the Tizen Baseline SDK installation before you can use the extension.

   - To use a previously-installed instance of the Tizen Baseline SDK or Tizen Studio with the VS Code Extension for Tizen, click **YES** and see [Setting Tizen Baseline SDK Configuration](#setting-baseline-config).


## Install using VSIX file

To install VS Code Extension for Tizen from a VSIX file:

1. In Visual Studio Code, at the bottom of the **Activity Bar**, click the **Extensions** icon.
2. In the top right corner of the **Extensions** view, click the **More** button (![More icon](media/vscode_more_icon.png)) and select **Install from VSIX**.

   ![Install from VSIX](media/vscode_install_vsix.png)

3. Select the VSIX file in the file browser and click **Install**.
4. After the installation is complete, activate the extension by clicking **Reload**.
5. Once the extension has been activated, it asks whether you want to use an existing Tizen Baseline SDK installation or install a new one:

   ![Baseline SDK installation query](media/vscode_baselinesdk_exists.png)

   - To perform a fresh installation, click **NO**.

     The extension suggests the path where to install the Tizen Baseline SDK. Click **YES** to proceed.

     > [!NOTE]
     > If you click **NO**, you must finish the Tizen Baseline SDK installation before you can use the extension.

   - To use a previously-installed instance of the Tizen Baseline SDK or Tizen Studio with the VS Code Extension for Tizen, click **YES** and see [Setting Tizen Baseline SDK Configuration](#setting-baseline-config).


<a name="setting-baseline-config"></a>
## Set Tizen Baseline SDK configuration
If you have a previously-installed Tizen Baseline SDK or Tizen Studio instance, you can reuse it for VS Code Extension for Tizen:

1. Once the extension has been activated, it asks if you want to use an existing Tizen Baseline SDK installation or install a new one. If you want to use the existing SDK, click **YES** (if you click **NO**, a new instance of the Tizen Baseline SDK is installed automatically).

   ![Baseline SDK installation query](media/vscode_baselinesdk_exists.png)

2. Enter the existing Tizen Baseline SDK path.

   ![Baseline SDK path](media/vscode_baselinesdk_path.png)

3. Confirm the path by clicking **YES**.

   ![Confirm the Baseline SDK path](media/vscode_baselinesdk_confirm.png)

4. Wait as the Package Manager built into the VS Code Extension for Tizen installs or updates the required files. During this process, the extension remains deactivated.


## Install emulator images

If you do not have a real device, you can run applications in the Tizen Emulator.

To download emulator images, you can use the Tizen Package Manager or the Tizen Emulator Manager.

- To use the Tizen Package Manager:
  1. Open the **Command Palette** and enter **tizen package**.
  2. Select **Tizen .NET: Launch Tizen Package Manager**.
  3. Select the profiles and versions that you want to install and click **Install**.

     ![Package Manager](media/tizen_package_manager.png)

- To use the Tizen Emulator Manager:

  > [!NOTE]
  > The Tizen Emulator Manager shows the emulator images installation window only when no images are installed on your computer.

  1. Open the **Command Palette** and enter **tizen emulator**.
  2. Select **Tizen .NET: Launch Tizen Emulator Manager**.
  3. Select the profiles and versions that you want to install and click **Ok**.

     ![Emulator Manager](media/howtoinstall-emulatormanager.png)


## Develop applications

The following sections explain how to use Visual Studio Code Extension for Tizen to develop your applications.

### Create Tizen .NET project

To create a Tizen .NET project:

1. Create a new directory as the root directory for your project.
2. In Visual Studio Code, open the project directory you created.
3. Open the **Command Palette** and enter **tizen create**.
4. Select **Tizen .NET: Create a Tizen .NET project**.
5. Select a Tizen .NET project template from the template list.
6. Enter the project name.
7. For a building target, select a solution file with the `.sln` extension or a project file with the `.csproj` extension.

### Build your project

To build your project:

1. Open the **Command Palette** and enter **tizen build**.
2. Select **Tizen .NET: Build a Tizen .NET project**.
3. Review the build results in the **Output** window, and check the location of the package file (`.tpk`).

> [!NOTE]
> If you have a Tizen device and want to deploy the application to it, you must create a certificate profile using the Tizen Certificate Manager or Tizen CLI before building your project. For more information, see [Certificate Manager](../vstools/tools/certificate-manager.md).

<a name="emulator-run"></a>
### Deploy and run your application in emulator

To deploy and run your application:

1. To launch the Tizen Emulator Manager, open the **Command Palette** and enter **tizen run**.

   > [!NOTE]
   > You cannot launch an emulator directly from Visual Studio Code. Instead, you must launch the Tizen Emulator Manager and use it to launch the emulator you need.

2. Select **Tizen .NET: Launch Tizen Emulator Manager**.
3. Create and launch an emulator instance in the Emulator Manager.
4. To deploy your application to the target, enter **tizen install** in the **Command Palette** and select **Tizen .NET: Install a Tizen .NET application on the Tizen device**.
5. To run the application on the emulator, enter **tizen run** in the **Command Palette** and select **Tizen .NET: Run a Tizen .NET application on the Tizen device**.

### Debug your application in emulator

To debug your application:

1. [Deploy and run your application in the emulator](#emulator-run).
2. In the Visual Studio Code **Activity Bar**, click the **Debug** icon (![Debug icon](media/vscode_debug_icon.png)).
3. In the **Debug** view, open the **Configuration** drop-down menu and select **Add Configuration**.
4. Select **Tizen LLDB** in the list of configurations.
5. Start the debugging session by pressing **F5**.

> [!NOTE]
> The LLDB RPM packages are automatically installed on the device as a part of the debugging process. If you want to install them at a custom location, see [Manual LLDB Package Installation](#manual-lldb).


## Troubleshoot

This section contains instructions for common problems with the VS Code Extension for Tizen.

### Failed Baseline SDK installation

If the Tizen Baseline SDK installation fails:

1. In the **Command Palette**, enter **tizen set**.
2. Select **Tizen .NET: Set the Tizen Baseline SDK path or install a new Tizen Baseline SDK**.
3. The extension asks if you want to use an existing Baseline SDK installation or install a new one. Proceed as described in [Setting Tizen Baseline SDK Configuration](#setting-baseline-config).

<a name="manual-lldb"></a>
### Manual LLDB package installation

Normally, the following LLDB packages are installed automatically when debugging:

- For a physical target device: `lldb-x.x.x-armv7l.rpm`
- For an x86 emulator: `lldb-x.x.x-i686.rpm`
- For an x86 64-bit emulator: `lldb-x.x.x-x86_64.rpm`

If necessary, you can install the LLDB packages manually:

1. Push the RPM package to the device using the `sdb push` command.
2. Install the package with raised privilege for write permission:

   ```bash
   $ sdb root on
   $ sdb shell mount -o remount, rw /
   $ sdb shell rpm -Uvh "<RPM package path>" --force
   $ sdb root off
   ```
