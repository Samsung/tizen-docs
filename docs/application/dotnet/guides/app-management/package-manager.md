# Package Manager


The package manager is used to retrieve detailed information on the installed packages on the device. This information includes the package name, label, path to the icon image, version, type, and installed storage.

The main features of the `Tizen.Applications.PackageManager` class include:

-   Retrieving information for all installed packages

    Use the `GetPackages()` method of the `Tizen.Applications.PackageManager` class to [retrieve the package information for all installed packages](#retrieve). The method returns an `IEnumerable<Package>` object with the package information.

- Retrieving individual package information

    To [retrieve package information](#info), get the [Tizen.Applications.Package](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Package.html) object using the `GetPackage()` method of the `Tizen.Applications.PackageManager` class.

- Monitoring changes

    You can [monitor package events](#listen), such as installation, uninstallation, and updates.

## Prerequisites

To enable your application to use the package management functionality:

1.  To use the [Tizen.Applications.PackageManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.PackageManager.html) class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    </privileges>
    ```

2. To use the methods and properties of the `Tizen.Applications.PackageManager` class, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace in your application:

    ```
    using Tizen.Applications;
    ```

<a name="retrieve"></a>
## Retrieving All Package Information

To retrieve all package information for installed packages:

1.  Retrieve all package information with the `GetPackages()` method of the [Tizen.Applications.PackageManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.PackageManager.html) class:

    ```
    IEnumerable<Package> packageList = PackageManager.GetPackages();
    ```

2. Iterate through the returned list to access information about each [Tizen.Applications.Package](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Package.html) object:

    ```
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
## Retrieving Specific Package Information

To get specific package information:

1.  Retrieve information for a specific package with the `GetPackage()` method of the [Tizen.Applications.PackageManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.PackageManager.html) class:

    ```
    Package package = PackageManager.GetPackage("org.tizen.helloworld");
    ```

2. Use the [Tizen.Applications.Package](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.Package.html) object returned by the `GetPackage()` method to access various package details:

    ```
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
## Monitoring Package Events

To detect package-related events, such as installation, uninstallation, and updates:

1.  Register event handlers for various events of the [Tizen.Applications.PackageManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.PackageManager.html) class.

    The following example registers event handlers for package installation, uninstallation, and update events:

    ```
    PackageManager.InstallProgressChanged += new System.EventHandler<PackageManagerEventArgs>(InstallEventHandler);
    PackageManager.UninstallProgressChanged += new System.EventHandler<PackageManagerEventArgs>(UninstallEventHandler);
    PackageManager.UpdateProgressChanged += new System.EventHandler<PackageManagerEventArgs>(UpdateEventHandler);
    ```

2. Define the event handlers. When the related event occurs, the event handler is triggered and you can get the event details from the [Tizen.Applications.PackageManagerEventArgs](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.PackageManagerEventArgs.html) instance.

    The following example implements the installation event handler:

    ```
    void InstallEventHandler(object sender, PackageManagerEventArgs args)
    {
        Log.Debug(LogTag, "pkgId: " + args.PackageId);
        Log.Debug(LogTag, "pkgType:" + args.PackageType);
        Log.Debug(LogTag, "progress:" + args.Progress);
        Log.Debug(LogTag, "eventState:" + args.State);
    }
    ```

## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
