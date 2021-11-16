
# Application Manager

The application manager provides information about installed and running applications. It provides functions for obtaining the application name and absolute path to share files among all applications.

The main features of the `Tizen.Applications.ApplicationManager` class include:

-   Managing the application running context

    For running applications, you can retrieve the application running context and operate on it. You can [manage the application running context](#manage_context) with the `Tizen.Applications.ApplicationManager` class.

-   Getting information on filtered applications

    For installed (but not necessarily running) applications, you can retrieve information with the [Tizen.Applications.ApplicationInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationInfo.html) class. You can also [retrieve information through a filter](#filter) with the [Tizen.Applications.ApplicationInfoFilter](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationInfoFilter.html) class.

-   Getting information on the current application

    For current applications, you can [retrieve information](#manage_current) using the [Tizen.Applications](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Application.html) class. You can use the retrieved information to manage the current application.


Iterator methods are used to travel through a list of applications. The `GetRunningApplicationsAsync()` method of the `Tizen.Applications.ApplicationManager` class is used for running applications and the `GetInstalledApplicationsAsync()` method is used for installed applications.

## Prerequisites

To enable your application to use the application management functionality:

1.  To use the methods and properties of the [Tizen.Applications.ApplicationManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationManager.html), [Tizen.Applications.ApplicationRunningContext](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationRunningContext.html), and [Tizen.Applications.ApplicationInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationInfo.html) classes, include the [Tizen.Applications](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.html) namespace in your application:

    ```csharp
    using Tizen.Applications;
    ```

2.  To use the `Resume()` method of the `Tizen.Applications.ApplicationRunningContext` class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
    </privileges>
    ```

<a name="manage_context"></a>
## Managing Application Running Context

To manage the context of the currently running application, follow these steps:

1.  Get the context of the currently running application.
To get the context, create an instance of the [Tizen.Applications.ApplicationRunningContext](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationRunningContext.html) class, with the ID of the application from which the context is being obtained as a parameter.

    If you do not have the application ID, you can retrieve it as:

    ```csharp
    string applicationId = ApplicationManager.GetAppId(Your PID);
    ```

    When an application is not running, it is impossible to get its context:

    ```csharp
    ApplicationRunningContext appRunningContext = new ApplicationRunningContext(Your App ID);
    ```

2.  Operate on the application context:
    -   Get the application ID, package ID, and process ID from the context:

        ```csharp
        string applicationId = appRunningContext.ApplicationId;
        string packageId = appRunningContext.PackageId;
        int processId = appRunningContext.ProcessId;
        ```

    -   Check the state of the application:

        ```csharp
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

        if (appRunningContext.IsTerminated) {
            /// Application is not running now
        }
        ```

    -   Resume the running application:

        ```csharp
        appRunningContext.Resume();
        ```

    -   Terminate the background application:

        ```csharp
        appRunningContext.TerminateBackgroundApplication();
        ```

<a name="filter"></a>
## Getting Information on Filtered Applications

To get information on filtered applications:

1.  Create the filter as an instance of the [Tizen.Applications.ApplicationInfoFilter](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationInfoFilter.html) class:

    ```csharp
    ApplicationInfoFilter appInfoFilter = new ApplicationInfoFilter();
    ```

2.  Add filter rules:

    ```csharp
    appInfoFilter.Filter.Add(ApplicationInfoFilter.Keys.Type, "dotnet");
    ```

3.  Call the `GetInstalledApplicationsAsync()` method of the [Tizen.Applications.ApplicationManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ApplicationManager.html) class and retrieve all filtered applications and print their information:

    ```csharp
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

<a name="manage_current"></a>
## Getting Information on Current Application

To get information on the current application, follow these steps:

1.  Call the `Current` property of the [Tizen.Applications](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Application.html) class:

    ```csharp
    Application application = Application.Current;
    ```

2.  Operate on the application information:
    -   Get the application directory information:

        ```csharp
        DirectoryInfo directory = application.DirectoryInfo;
        ```

    -   Get the application name:

        ```csharp
        string name = application.Name;
        ```

    -   Get the application version:

        ```csharp
        string version = application.Version;
        ```


## Related Information
  - Dependencies
    -   Tizen 4.0 and Higher
