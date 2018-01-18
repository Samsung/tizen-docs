
# Application Manager

The application manager provides information about installed and running applications. It provides functions for obtaining the application name and absolute path to share files among all applications.

The main features of the `Tizen.Applications.ApplicationManager` class include:

-   Managing the application running context

    For running applications, you can retrieve the application running context and operate on it. You can [manage the application running context](#manage_context) with the `Tizen.Applications.ApplicationManager` class.

-   Getting information on filtered applications

    For installed (but not necessarily running) applications, you can retrieve information with the [Tizen.Applications.ApplicationInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationInfo.html) class. You can also [retrieve information through a filter](#filter) with the [Tizen.Applications.ApplicationInfoFilter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationInfoFilter.html) class.

Iterator methods are used to travel through a list of applications. The `GetRunningApplicationsAsync()` method of the `Tizen.Applications.ApplicationManager` class is used for running applications and the `GetInstalledApplicationsAsync()` method is used for installed applications.

## Prerequisites

To enable your application to use the application management functionality:

1.  To use the methods and properties of the [Tizen.Applications.ApplicationManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationManager.html), [Tizen.Applications.ApplicationRunningContext](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationRunningContext.html), and [Tizen.Applications.ApplicationInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationInfo.html) classes, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace in your application:

    ```
    using Tizen.Applications;
    ```

2.  To use the `Resume()` method of the `Tizen.Applications.ApplicationRunningContext` class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
    </privileges>
    ```

<a name="manage_context"></a>
## Managing the Application Running Context

To get the application running context and its details, and to operate on the context:

1.  Get the context of the currently-running application by creating an instance of the [Tizen.Applications.ApplicationRunningContext](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationRunningContext.html) class, with the ID of the application from which the context is being obtained as a parameter.

    When an application is not running, it is impossible to get its context.

    ```
    ApplicationRunningContext appRunningContext = new ApplicationRunningContext(Your App ID);
    ```

2.  Operate on the context:
    -   Get the application ID, package ID, and process ID from the context:

        ```
        string applicationId = appRunningContext.ApplicationId;
        string packageId = appRunningContext.PackageId;
        int processId = appRunningContext.ProcessId;
        ```

    -   Check the state of the application:

        ```
        if (appRunningContext.State == ApplicationRunningContext.AppState.Foreground)
            /// UI application is running in the foreground
        else if (appRunningContext.State == ApplicationRunningContext.AppState.Background)
            /// UI application is running in the background
        else if (appRunningContext.State == ApplicationRunningContext.AppState.Service)
            /// Service application is running
        else if (appRunningContext.State == ApplicationRunningContext.AppState.Terminated)
            /// Application is terminated
        else
            /// State is undefined
        ```

    -   Resume the running application:

        ```
        appRunningContext.Resume();
        ```

<a name="filter"></a>
## Getting Information on Filtered Applications

To get information on filtered applications:

1.  Create the filter as an instance of the [Tizen.Applications.ApplicationInfoFilter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationInfoFilter.html) class:

    ```
    ApplicationInfoFilter appInfoFilter = new ApplicationInfoFilter();
    ```

2.  Add filter rules:

    ```
    appInfoFilter.Filter.Add(ApplicationInfoFilter.Keys.Type, "dotnet");
    ```

3.  Call the `GetInstalledApplicationsAsync()` method of the [Tizen.Applications.ApplicationManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationManager.html) class and retrieve all filtered applications and print their information:

    ```
    IEnumerable<ApplicationInfo> appInfoList = await ApplicationManager.GetInstalledApplicationsAsync(appinfoFilter);

    foreach (ApplicationInfo appInfo in appInfoList)
    {
        Log.Debug("Tag", "applicationId: " + appInfo.ApplicationId);
        Log.Debug("Tag", "packageId: " + appInfo.PackageId);
        Log.Debug("Tag", "label: " + appInfo.Label);
        Log.Debug("Tag", "executablePath: " + appInfo.ExecutablePath);
        Log.Debug("Tag", "iconPath: " + appInfo.IconPath);
        Log.Debug("Tag", "applicationType: " + appInfo.ApplicationType);
        Log.Debug("Tag", "isNoDisplay: " + appInfo.IsNoDisplay.ToString());
        Log.Debug("Tag", "isOnBoot: " + appInfo.IsOnBoot.ToString());
        Log.Debug("Tag", "isPreload: " + appInfo.IsPreload.ToString());
        Log.Debug("Tag", "sharedResourcePath: " + appInfo.SharedResourcePath);
    }
    ```


## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
