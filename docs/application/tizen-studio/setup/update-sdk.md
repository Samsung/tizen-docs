# Update Tizen Studio
This page explains how to install, update, and remove packages using the Package Manager tool, and also guides advanced users to manage packages with the CLI version of the tool. At its core, Tizen Studio primarily comprises of various packages that comprises of necessary files, metadata, installation, and removal scripts, and these packages have interdependencies. 
Once you install Tizen Studio, it is easy to keep the packages, platforms and other tools up to date with automatic updates. Tizen Studio includes a comprehensive package management tool to manage the processes, such as installing, uninstalling, and updating packages, platforms, and other related tools.
## Launch Package Manager
The Package Manager offers a simple way to manage packages without getting into the complicated package dependencies.

To launch Package Manager on your preferred operating system, follow these steps: 

- Windows: Click **Start > All Programs > Tizen Studio > Tools > Package Manager**.
- MacOS: Click **Launchpad > Package Manager**.
- Ubuntu: Click **Dashboard Home > Package Manager**.

>Note: 
>
> Before you launch the Package Manager, ensure to close all the Tizen Studio programs.

## Package Manager Components 

The Package Manager window is made up of the following logical areas as identified in the following figure:

**Figure: Package Manager main window**

![Package Manager main window](./media/updating_sdk_main.png)

The Package Manager window consists of the following logical areas:

- **Header area** comprises of the following elements:

  - **Trouble Shooting** (![Inside Trouble Shooting icon](./media/updating_sdk_icon_troubleshoot.png)): You can  access troubleshooting guides that help you resolve the  common issues related to Package Manager.
  - **Configuration** (![Configuration icon](./media/updating_sdk_icon_config.png)): Lets you change the Package Manager configurations and other related settings, such as package repository locations and proxy options etc.
  - **Information** (![Information icon](./media/updating_sdk_icon_info.png)): You can access the details of Package Manager, such as version number, installation path, package repository URL, distribution name, and package snapshot.

- **Main area** comprises of the following elements:

  - **Main SDK** tab: It enables you to install, remove packages, platforms and tools. In addition, the filter buttons narrows down the choice of the package list display based on the selected profiles.
  - **Extension SDK** tab: It enables you to install or remove extension tools and packages, such as Samsung Certificate Extension etc.
  - **Progress** tab: It facilitates you to see the packages that are being installed or removed.
  In the **Main SDK** and the **Extension SDK** tab, you can also list the installed packages by selecting the **View installed packages** check box.

  **Figure: Package list**

   ![Package list](./media/updating_sdk_main_area.png)

- **Description area**: shows detailed description of each package or platform that is currently selected on the list in the main area.

  **Figure: Description area**

    ![Description area](./media/updating_sdk_description.png)

## Update Packages
Package Manager makes it easy to update your packages and platforms. You can use the Package Manager tool to locate and install updates and new features for the packages that are already installed. 
>**Note:**
- Before you begin to update a package, ensure that the Package Manager has access to the repository that contains the packages and you have access to Internet. 
Tizen Studio notifies you with a **Updates available** button that appears in the Package Manager window, if new updates are available for your existing Tizen Studio packages and platforms.
To update the existing packages, click **Updates available**.
    
  **Figure: Updates available button**

  ![Updates available button](./media/updating_sdk_updates.png)

>**Note:**
>
>- To ensure system integrity across all the packages in Tizen Studio, Package Manager does not support updating packages individually.
>- In case, you do not have access to internet, you can update the packages with an image file, which can be downloaded separately. 

### Update Packages Offline

The Package Manager also facilitates offline upgrade with an update image for all the existing packages.
To install the packages with an image file, follow these steps:
1. In Package Manager, click ![Configuration icon](./media/updating_sdk_icon_config.png).
2. In the Configuration window that appears, enter the full path of the image file in Package Repository. Alternatively, to select the image file, click **...** next to the **combo box**. 
3. To close the dialog, click **Open**.

    >**Note:**
    >
    >If the image file is valid, detailed information about the image is displayed below the combo box.
4. To close the **Configuration** dialog, click **OK**. The **Update available** button appears.
5. To update and install additional platforms and tools with the image file, click **Update available**.

    > **Note**  
    > 
    > Ensure that the image file includes a newer version of Tizen Studio than your installed version before updating or installing with the image file.

## Install Additional Packages

Package manager simplifies the process to install packages, platforms and tools. You can install any platform or tool which are listed under the Main SDK and Extension tabs.
In Main SDK and Extension SDK tab, click **install** next to the desired platform or tool in the list that you want to install. 
>**Note:**
>
>Package Manager installs all packages that are required for that platform or tool.
Package Manager also provides you the flexibility to install even an individual preferred package for a particular platform or tool.
To install individual packages for a particular platform or tool, follow these steps: 
  1. Click on **collapsible** icon located on the left of the main area of the window for each platform or tool to view more packages and tools.
 2. Click **install** next to the package to install that package.
 
  **Figure: Install platform packages**

  ![Installing platform packages](./media/updating_sdk_install_platform.png)

## Cancel Installation

To cancel the installation process, click the **X** on **Progress** tab next to the corresponding package. 

>**Note:** 
>
>Due to package dependencies, cancelling the installation of a single package may also cancel the installation of other packages.

  **Figure: Cancel installation**

  ![Cancelling the installation](./media/updating_sdk_install_cancel.png)

## Retry Cancelled Installation 

To retry a cancelled or failed installation, click ![Retry icon](./media/updating_sdk_icon_retry.png). 

>**Note:**
>
>Due to package interdependencies, retrying the installation of a single package may also cause the installation of other packages.

## Remove Packages

The package manager is a comprehensive tool and provides an intuitive user experience that helps you to remove any package, platform or tool with ease. 

To remove a package, click **delete** located next to the respective package. 

>**Note:**
>
>- Due to package interdependencies, removing a single package may also cause other packages to be removed. 
>- To ensure system integrity across all installed Tizen Studio packages, package removal process cannot be cancelled while the process is in progress.

  **Figure: Remove packages**

  ![Removing packages](./media/updating_sdk_install_remove.png)

## Monitor Progress

Tizen Studio provides a progress bar where you can monitor the installation, update, or removal progress. This progress bar appears on the header area and helps in checking the overall progress of a respective process.  Also, to monitor the progress of specific installation, uninstallation, or update, as well as view the expected time of completion, the Package manager provides respective progress bars for each package or tool.

  **Figure: Progress tab**

  ![Progress tab](./media/updating_sdk_progress.png)

## Update using CLI Package Manager

For advanced users, Tizen Studio provides command line version of package manager tool. It can be used to install, update, remove packages and platform tools respectively using terminal or console window. 

To Run the CLI version of Package Manager with the `update` command, use the following syntax:

```
package-manager-cli update [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] [--latest]
```

The following table lists various options you can append to the syntax for the desired choice of the process:   
**Table: Update command parameters**

| Parameter                   | Description                              |
|---------------------------|----------------------------------------|
| `--accept-license`          | Accepts the license terms.               |
| `--no-java-check`           | Skips the Java version check.            |
| `--proxy <value>`           | Represents proxy configuration value. You can use one of the following values: **direct**, **auto**, or **ip:port**. |
| `-f, --file <file path>`    | If you want to install packages from a local SDK image, specify the full path of the SDK image file. |
| `-p, --password <password>` | Specifies Administrator (sudo) password for authentication. (Ubuntu only) |
| `--latest`                  | Specifies the option for updating the Tizen Studio to the latest version, assuming that you have downgraded it manually to an earlier version. Otherwise, the Package Manager updates it to the latest version with or without this option. |

## Related Information
- Dependencies
  - Tizen Studio 1.0 and Higher
