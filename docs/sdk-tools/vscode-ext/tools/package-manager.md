# Manage SDK packages

Use Package Manager to install, update, and remove Tizen platform packages, SDK components, extensions, and emulator images.

## Opening Package Manager

In the **Tizen** panel, under **Baseline Tools**, select **Package Manager**.

![Open Package Manager from Baseline Tools](media/launch_pm.png)

## Install or Update Packages

The **Installed Packages** tab lists installed packages by category and shows their versions. Expand a category to review its packages. When updates are available, select **Update** in the summary bar to install them.

![Installed Packages tab with an expanded category](media/package-manager-installed-packages.png)

## Install a Platform Version

Use **Advanced SDK Installation** to add or remove an entire Tizen platform version:

1. Select **Advanced SDK Installation**.
2. Select **Install** next to the platform version that you need.
3. To remove an installed version, select **Uninstall**.

![Advanced SDK Installation](media/package-manager-advanced-sdk.png)

The available versions include Tizen 10.0, 9.0, 8.0, 7.0, 6.5, 6.0, and TV extensions. Install the platform version and profile required by the application and target device.

## Configure Package Repositories

1. Select the **Repository** (gear) button in Package Manager.
2. Configure the Tizen repository for official SDK packages and the TV repository for TV extension packages or local ZIP files.
3. Select **Apply** after changing a repository URL.
4. Select **Update** in Package Manager to complete the repository update.

![Repository configuration](media/package-manager-repository.png)

### Install TV packages from a local ZIP file

You can select a local `.zip` file as the TV repository to install TV SDK packages and an emulator image.

1. In Package Manager, select **Repository** to open **Repository Configuration**.
2. Select **Browse** next to **TV repository**, select the TV `.zip` file, and select **Open**.

   ![Select a local TV ZIP file using the Browse button](../media/TV_ZIP.png)

3. Select **Apply** and wait for the repository configuration to finish applying.

   ![Package Manager applying the local TV ZIP repository configuration](../media/TV_ZIP_Apply.png)

4. Select **Update** in Package Manager and wait for the update to complete.

The package list in **Advanced SDK Installation** updates to reflect the TV packages from the ZIP file. The TV emulator also appears in Emulator Manager.

![Updated TV package list in Advanced SDK Installation and the TV emulator in Emulator Manager](../media/TV_ZIP_list.png)

To run the emulator, open **Emulator Manager** from **Baseline Tools** in the **Tizen** panel, select the TV emulator, and select **Launch**. For more information, see [Launch and manage emulators](emulator-manager.md#launch-and-manage-emulators).

## Report an Issue

Select **Issue Report** in the upper-right corner of Package Manager to open the GitHub issues page and report an issue.

![Issue Report button](media/package_manager_issue_report_highlighted.png)
