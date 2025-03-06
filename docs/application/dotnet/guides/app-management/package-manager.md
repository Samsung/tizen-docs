# Package Manager


The package manager is used to retrieve detailed information on the installed packages on the device. This information includes the package name, label, path to the icon image, version, type, and installed storage.

The main features of the `Tizen.Applications.PackageManager` class includes the following:

-   Retrieving information for all installed packages

    Use the `GetPackages()` method of the `Tizen.Applications.PackageManager` class to [retrieve the package information for all installed packages](#retrieve). The method returns an `IEnumerable<Package>` object with the package information.

- Retrieving individual package information

    To [retrieve package information](#info), get the [Tizen.Applications.Package](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Package.html) object using the `GetPackage()` method of the `Tizen.Applications.PackageManager` class.

- Monitoring changes

    You can [monitor package events](#listen), such as installation, uninstallation, and updates.

- Removing package user data

    You can [clear user data](#clear) by targeting a specific file or directory. (Since Tizen 8.0)

## Prerequisites

To enable your application to use the package management functionality, follow these steps:

1.  To use the [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    </privileges>
    ```

2. To use the methods and properties of the `Tizen.Applications.PackageManager` class, include the [Tizen.Applications](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.html) namespace in your application:

    ```csharp
    using Tizen.Applications;
    ```

<a name="retrieve"></a>
## Retrieve all package information

To retrieve all package information for installed packages, follow these steps:

1.  Retrieve all package information with the `GetPackages()` method of the [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) class:

    ```csharp
    IEnumerable<Package> packageList = PackageManager.GetPackages();
    ```

2. Iterate through the returned list to access information about each [Tizen.Applications.Package](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Package.html) object:

    ```csharp
    foreach (Package package in packageList)
    {
        Log.Debug(LogTag, "pkgid: " + package.Id);
        Log.Debug(LogTag, "label: " + package.Label);
        Log.Debug(LogTag, "icon: " + package.IconPath);
        Log.Debug(LogTag, "version: " + package.Version);
        Log.Debug(LogTag, "type: " + package.PackageType);
        Log.Debug(LogTag, "storage: " + package.InstalledStorageType);
        Log.Debug(LogTag, "system: " + package.IsSystemPackage);
        Log.Debug(LogTag, "removable: " + package.IsRemovable);
        Log.Debug(LogTag, "preload: " + package.IsPreloaded);
    }
    ```

<a name="info"></a>
## Retrieve specific package information

To get specific package information, follow these steps:

1.  Retrieve information for a specific package with the `GetPackage()` method of the [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) class:

    ```csharp
    Package package = PackageManager.GetPackage("org.tizen.helloworld");
    ```

2. Use the [Tizen.Applications.Package](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Package.html) object returned by the `GetPackage()` method to access various package details:

    ```csharp
    /// Use package information
    Log.Debug(LogTag, "pkgid: " + package.Id);
    Log.Debug(LogTag, "label: " + package.Label);
    Log.Debug(LogTag, "icon: " + package.IconPath);
    Log.Debug(LogTag, "version: " + package.Version);
    Log.Debug(LogTag, "type: " + package.PackageType);
    Log.Debug(LogTag, "storage: " + package.InstalledStorageType);
    Log.Debug(LogTag, "system: " + package.IsSystemPackage);
    Log.Debug(LogTag, "removable: " + package.IsRemovable);
    Log.Debug(LogTag, "preload: " + package.IsPreloaded);
    ```

<a name="listen"></a>
## Monitor package events

To detect package-related events, such as installation, uninstallation, and updates, follow the steps below:

1.  Register event handlers for various events of the [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) class.

    The following example registers event handlers for package installation, uninstallation, and update events:

    ```csharp
    PackageManager.InstallProgressChanged += new System.EventHandler<PackageManagerEventArgs>(InstallEventHandler);
    PackageManager.UninstallProgressChanged += new System.EventHandler<PackageManagerEventArgs>(UninstallEventHandler);
    PackageManager.UpdateProgressChanged += new System.EventHandler<PackageManagerEventArgs>(UpdateEventHandler);
    ```

2. Define the event handlers. When the related event occurs, the event handler is triggered and you can get the event details from the [Tizen.Applications.PackageManagerEventArgs](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManagerEventArgs.html) instance.

    The following example implements the installation event handler:

    ```csharp
    void InstallEventHandler(object sender, PackageManagerEventArgs args)
    {
        Log.Debug(LogTag, "pkgId: " + args.PackageId);
        Log.Debug(LogTag, "pkgType:" + args.PackageType);
        Log.Debug(LogTag, "progress:" + args.Progress);
        Log.Debug(LogTag, "eventState:" + args.State);
    }
    ```

<a name="clear"></a>
## Clear user data

If you want to delete specific user data from a specific app, you can use the `ClearUserData()` method of the [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager.html) class.

The following example removes the `testDir/test.txt` file from `org.tizen.sample` package's user directory:

```csharp
PackageManager.ClearUserData("org.tizen.sample", "testDir/test.txt");
```

If you want to use this API, you need to add the below privilege on `tizen-manifest.xml`.

 - `http://tizen.org/privilege/packagemanager.admin`


## Related information
  * Dependencies
    -   Tizen 4.0 and Higher
  * API Reference
    - [Tizen.Applications.PackageManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.PackageManager) class
    - [Tizen.Applications.Package](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Package) class
