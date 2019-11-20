# Introduction

Visual Studio Tools for Tizen provides Tizen-specific tools to improve your productivity. You can create, build, and debug Tizen applications using Visual Studio. Using Visual Studio Tools for Tizen you can:
- Create applications for TV, wearable, and mobile profiles
- Debug your application from Visual Studio
- Verify the profile performance and memory usage of your application

## Prerequisites

To work with Visual Studio Tools for Tizen, you must have Visual Studio 2019.

![Visual Studio Tools for Tizen](media/prerequisite-vs.png)

> **Note**
>
> Visual Studio Tools for Tizen works with all Visual Studio variations, including Community. Installing or re-installing Visual Studio with .NET desktop development and .NET Core cross-platform development toolsets is recommended.

# Visual Studio Tools for Tizen 

To use the Tizen SDK tools in Visual Studio, you must install:

1. [Visual Studio Tools for Tizen Extension](#installing-visual-studio-tools-for-tizen-extension )
2. [Tizen Baseline SDK](#install-tizen-baseline-sdk)

<a name="install"></a>
## Install Visual Studio Tools for Tizen Extension 

The Visual Studio Tools for Tizen extension is registered in the Visual Studio Marketplace. You can install the extensions from the Visual Studio Marketplace in the Visual Studio IDE.

1. In the Visual Studio menu, select **Tools > Extensions > Manage Extensions**.
2. In the **Visual Studio Marketplace**, search for **Tizen**.  
3. In the **Visual Studio Tools for Tizen** option that appears, click **Download** and close the Visual Studio IDE. \   
   The installation begins.

![Visual Studio Tools for Tizen](media/v1-install-tools.gif)

Alternatively, you can download the Visual Studio Tools for Tizen extension from [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=tizen.VisualStudioToolsforTizen).

## Install Tizen Baseline SDK

Baseline SDK contains Tizen-specific libraries and tools such as profiler, debugger, and so on.

After installing the Visual Studio Tools for Tizen extension, you must set up the Tizen baseline SDK. You can either install a new Tizen baseline SDK or configure an existing Tizen baseline SDK:

- [Install a new Tizen baseline SDK](#install-new-tizen-baseline-sdk)
- [Configure an existing Tizen baseline SDK](#configure-existing-tizen-baseline-sdk)

### Install New Tizen Baseline SDK

1. In the Visual Studio menu, select **Tools > Tizen > Tizen Package Manager**.
2. Select **Install new Tizen SDK**.
3. Read the license document and click **I Agree**.
4. Enter the root directory path where you want to install the Tizen baseline SDK and click **Next**. \
   The baseline SDK is installed automatically.
5. In the **Package Manager** window that appears, select **Main SDK**.
6. Install **Tizen SDK tools**.

![Visual Studio Tools for Tizen](media/v2-install-baseline-sdk.gif)

### Configure Existing Tizen Baseline SDK

You can use Tizen Package Manager to configure the existing Tizen baseline SDK path and each tool path directly:

To set up the Tizen baseline SDK path:

1. In the Visual Studio menu, select **Tools > Tizen > Tizen Package Manager**.
2. Select **Use installed Tizen SDK**.
3. Enter the root directory of your existing Tizen Studio installation and click **OK**. \
   The Tizen baseline SDK is installed automatically.

To set up each tool path directly:

1. In the Visual Studio menu, select **Tools > Options > Tizen > Tools**.
2. Enter the root directory of your existing Tizen Studio installation in the **Tool Path (Tizen SDK)** field.
   The other tools paths are configured automatically.
	
![Visual Studio Tools for Tizen](media/v3-install-existing-sdk.gif)
  
## Troubleshoot

If you encounter any issue with the installation, verify whether:

- VSIX is installed correctly. To verify that, go to **Tools > Extensions > Manage Extensions** and search for **Tizen**.

  ![Check VSIX](media/cps-extension-and-updates.png)

- Tizen baseline SDK is installed correctly. To verify that, go to **Tools &gt; Options &gt; Tizen &gt; Tools**.

  ![Check the SDK tool path](media/howtoinstall-checktoolpath.png)

- Tizen Project properties have been copied correctly. Ensure that the `Tizen.NET.ProjectType.props` and `Tizen.NET.ProjectType.targets` files are located in the `C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\MSBuild\Tizen\VisualStudio` folder.

  ![Project Property](media/cps-project-property.png)

## Uninstall Visual Studio Tools for Tizen

To uninstall the Visual Studio Tools for Tizen:

1. In the Visual Studio menu, select **Tools > Extensions > Manage Extensions**.
2. In the **Manage Extensions** window that appears, select **Installed > Visual Studio Tools for Tizen** and click **Uninstall**.
3. Read the warning and click **close**. Close the IDE. 
4. In the VSIX Installer window that appears, click **Modify**. \
   The modifications are completed and the tools are unistalled.

![Visual Studio Tools for Tizen](media/v4-uninstall-tools.gif)
