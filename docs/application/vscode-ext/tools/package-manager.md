# Configuring the Packages

The Packages configuration allows you to manage the packages of the VS Code Extension for Tizen. With the Packages configuration, you can change the options for the package repository for the main and extension SDK.

> [!NOTE]
> The SDK resources are downloaded to the Tizen SDK path that you configure during the [initial setup after installation](../Tizen/dotnet.md#after-installation-setting-the-tizen-sdk-path). The package directories described below are created relative to that path.

## Configuring the Main SDK Repository

You can configure the installation and update settings for SDK components.

### Configuring the Package Repository

The Package Repository configuration allows you to define server locations for downloading and updating SDK components and related packages. You can configure repository URLs for both Tizen and TV development environments directly within the extension.

**Figure: Packages View with Repository Settings**

![Configuration window with the Package Repository selected](media/package-repository.png)

To configure the package repository:

1. Open the **Notice** view in the Primary Sidebar.
2. Click the **Packages** button to open the **Packages** page.
3. Click the **Repository Setting** icon (<img src="./media/advanced_conf_browse.png" alt="More Options icon" height="25" style="vertical-align: middle;"/>) in the upper-right corner.
4. In the configuration panel, enter the repository URL for the **Tizen Repository** or **TV Repository** as needed.
5. Click **Apply** to validate and save the configuration.
   The **Update** button becomes active once the settings are applied.
6. Click **Update** to synchronize and install the latest packages from the specified repositories.

## SDK Installation Directories

After the initial SDK path setup, the extension creates a `.tizen-extension-platform` directory at the selected location. Within this directory, SDK resources are organized as follows:

| Component | Directory |
|-----------|-----------|
| Tizen SDK tools and data | `$HOME/.tizen-extension-platform/server/sdktools/data` |
| .NET SDK and Tizen workload | `$HOME/.tizen-extension-platform/server/sdktools/dotnet` |

> [!NOTE]
> If you selected a custom SDK path during installation, replace `$HOME/.tizen-extension-platform` with your chosen path.

## Advanced Package Installation

To install the full SDK for a specific platform version, use the **Advanced** feature:

**Figure: Advanced Package Installation**

![Advanced Package Installation](media/advanced-package-installation.png)

1. Open the **Packages** page from the **Notice** view in the Primary Sidebar.
2. Click the **Advanced** button to open the advanced package installation view.
3. Select the platform profile (for example, **Mobile**, **Wearable**, or **TV**) and the desired version.
4. Click **Install** to download and install the full SDK for the selected platform version.
5. Monitor the installation progress in the **Output** panel.

