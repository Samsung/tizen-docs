# Package Information

You can retrieve detailed information about packages, such as package name, icon path, version details, and package ID. You can receive notifications if packages are updated or removed, or new packages are installed. You can also perform package management tasks, such as installing or uninstalling packages.

The Package API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main package information features are:

- Package management   

  You can [install or uninstall packages](#manage).

- Package information retrieval   

  You can display a list of installed packages on the device, and [retrieve package information](#retrieve), such as name, ID, icon path, and version.

- Package change notifications   

  You can [receive notifications](#receive) when packages are installed, updated, or uninstalled.

## Prerequisites

To use the Package API (in [mobile](../../api/latest/device_api/mobile/tizen/package.html), [wearable](../../api/latest/device_api/wearable/tizen/package.html), and [TV](../../api/latest/device_api/tv/tizen/package.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/package.info"/>
<tizen:privilege name="http://tizen.org/privilege/packagemanager.install"/>
```

<a name="retrieve"></a>
## Retrieving Package Information

You can retrieve information about packages in various ways:

- Retrieve information about installed packages using the `getPackageInfo()` and `getPackagesInfo()` methods of the `PackageManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageManager), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageManager), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageManager) applications).
- Use the `PackageInformation` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageInformation), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageInformation), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageInformation) applications) to retrieve information about installed packages, such as name, icon path, and version.

Learning how to retrieve information about installed packages allows you to manage device packages from your application:

1. To retrieve a list of installed packages, use the `getPackagesInfo()` method of the `PackageManager` interface:

   ```
   function onListInstalledPackages(lists) {
       console.log('The number of installed package is ' + lists.length);
   }

   tizen.package.getPackagesInfo(onListInstalledPackages);
   ```

   The list of installed packages is returned to the `PackageInformationArraySuccessCallback()` methods as an array of `PackageInformation` objects.

2. To retrieve basic package information, use the `getPackageInfo()` method of the `PackageManager` interface, specifying the package ID. If no package ID is set, the method retrieves the information for the application package calling the method.

   ```
   var packageInfo = tizen.package.getPackageInfo('org.tizen.calculator');
   ```

<a name="manage"></a>
## Managing Packages

You can manage the package installation using the `install()` and `uninstall()` methods of the `PackageManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageManager), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageManager), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageManager) applications). Additionally, you can receive notifications of the installation and uninstallation progress using the `PackageProgressCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageProgressCallback), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageProgressCallback), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageProgressCallback) applications).

Learning how to install and uninstall packages is a basic package management skill:

1. To install a package, use the `install()` method of the `PackageManager` interface, specifying the local package installation path on your device. You can retrieve the installation progress using the `PackageProgressCallback` interface.

   ```
   var onInstallation = {
       onprogress: function(packageId, percentage) {
           console.log('On installation(' + packageId + '): progress(' + percentage + ')');
       },
       oncomplete: function(packageId) {
           console.log('Installation(' + packageId + ') Complete');
       }
   };

   tizen.filesystem.resolve('downloads/test.wgt', function(packageFile) {
       tizen.package.install(packageFile.toURI(), onInstallation);
   });
   ```

2. To uninstall a package, use the `uninstall()` method of the `PackageManager` interface, specifying the package ID. You can retrieve the uninstallation progress using the `PackageProgressCallback` interface.

   ```
   var onUninstallation = {
       onprogress: function(packageId, percentage) {
           console.log('On uninstallation(' + packageId + '): progress(' + percentage + ')');
       },
       oncomplete: function(packageId) {
           console.log('Uninstallation(' + packageId + ') Complete');
       }
   };

   tizen.package.uninstall('TEST_APP_ID', onUninstallation);
   ```

<a name="receive"></a>
## Receiving Package Change Notifications

You can receive notifications of changes in the list of installed packages. The `setPackageInfoEventListener()` method of the `PackageManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageManager), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageManager), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageManager) applications) registers an event listener for changes in the installed packages list. To unsubscribe the listener, use the `unsetPackageInfoEventListener()` method. You can use the `PackageInformationEventCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/package.html#PackageInformationEventCallback), [wearable](../../api/latest/device_api/wearable/tizen/package.html#PackageInformationEventCallback), and [TV](../../api/latest/device_api/tv/tizen/package.html#PackageInformationEventCallback) applications) to define listeners for receiving notifications.

Learning to receive notifications when the list of installed packages changes allows you to manage device packages from your application:

1. Define the event handlers for different notifications using the `PackageInformationEventCallback` listener interface:

   ```
   var packageEventCallback = {
       oninstalled: function(packageInfo) {
           console.log('The package ' + packageInfo.name + ' is installed');
       },
       onupdated: function(packageInfo) {
           console.log('The package ' + packageInfo.name + ' is updated');
       },
       onuninstalled: function(packageId) {
           console.log('The package ' + packageId + ' is uninstalled');
       }
   };
   ```

2. Register the listener to use the defined event handlers with the `setPackageInfoEventListener()` method of the `PackageManager` interface:

   ```
   tizen.package.setPackageInfoEventListener(packageEventCallback);
   ```

3. To stop receiving notifications, use the `unsetPackageInfoEventListener()` method of the `PackageManager` interface:

   ```
   tizen.package.unsetPackageInfoEventListener();
   ```


## Related Information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
