# Component Manager

Component manager provides information about installed and running components.

The main features of the `Tizen.Applications.ComponentBased.ComponentManager` class include:

-   Managing running component context

    For the running components, you can retrieve the component running context and operate on it. You can [manage the component running context](#manage_context) with the `Tizen.Applications.ComponentBased.ComponentManager` class.

-   Managing component information

    For components that are installed but not necessarily running, you can retrieve information with the [Tizen.Applications.ComponentBased.ComponentInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentInfo.html) class.

Iterator methods are used to travel through a list of components. The `GetRunningComponentsAsync()` method of the `Tizen.Applications.ComponentBased.ComponentManager` class is used for the running components and the `GetInstalledComponentsAsync()` method is used for the installed components.

## Prerequisites

To enable your application to use the component management functionality:

1.  To use classes and methods, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```XML
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the [Tizen.Applications.ComponentBased.ComponentManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentManager.html), [Tizen.Applications.ComponentBased.ComponentRunningContext](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentRunningContext.html), and [Tizen.Applications.ComponentBased.ComponentInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentInfo.html) classes, include the [Tizen.Applications.ComponentBased](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.html) namespace in your application:

    ```csharp
    using Tizen.Applications.ComponentBased;
    ```

<a name="manage_context"></a>
## Managing Running Component Context

To get the running component context and its details, and to operate on the context:

1.  Get the context of the currently running component by creating an instance of the [Tizen.Applications.ComponentBased.ComponentRunningContext](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentRunningContext.html) class, with the ID of the context obtained component as a parameter.

    To get a component's context, the component must be running.

    ```csharp
    ComponentRunningContext compoRunningContext = new ComponentRunningContext(Your Component ID);
    ```

2.  Operate on the context:
    -   Get the component ID, application ID, and instance ID from the context:

        ```csharp
        string componentId = compoRunningContext.ComponentId;
        string applicationId = compoRunningContext.ApplicationId;
        string instanceId = compoRunningContext.InstanceId;
        ```

    -   Check the state of the component:

        ```csharp
        if (compoRunningContext.State == ComponentRunningContext.ComponentState.Initialized)
            /// The component is constructed.
        else if (compoRunningContext.State == ComponentRunningContext.ComponentState.Created)
            /// The component is created.
        else if (compoRunningContext.State == ComponentRunningContext.ComponentState.Started)
            /// The component is started.
        else if (compoRunningContext.State == ComponentRunningContext.ComponentState.Resumed)
            /// The component is resumed.
        else if (compoRunningContext.State == ComponentRunningContext.ComponentState.Paused)
            /// The component is paused
        else if (compoRunningContext.State == ComponentRunningContext.ComponentState.Destroyed)
            /// The component is destroyed.
        else
            /// State is undefined
        ```

    -   Resume the running application:

        ```csharp
        compoRunningContext.Resume();
        ```

<a name="filter"></a>
## Managing Component Information

To get the installed information and its details, and to operate on the information:

1.  Get the information of the currently-installed component by creating an instance of the [Tizen.Applications.ComponentBased.ComponentInfo](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentInfo.html) class, with the ID of information obtained component as a parameter.

    To get a component's information, the component must be installed.

    ```csharp
    ComponentInfo compoInfo = new ComponentInfo(Your Component ID);
    ```

2.  Operate on the information:
    -   Get the component ID and application ID:

        ```csharp
        string componentId = compoInfo.ComponentId;
        string applicationId = compoInfo.ApplicationId;
        ```
    -   Check the type of the component:

        ```csharp
        if (compoInfo.ComponentType == ComponentType.Frame)
            /// The component is frame-component.
        else if (compoInfo.ComponentType == ComponentType.Service)
            /// The component is service-component
        else
            /// ComponentType is undefined
        ```

    -   Get the label and the icon path:

        ```csharp
        string label = compoInfo.Label;
        string iconPath = compoInfo.IconPath;
        ```

3.  Call the `GetInstalledComponentsAsync()` method of the [Tizen.Applications.ComponentBased.ComponentManager](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.ComponentBased.ComponentManager.html) class, and retrieve all components and print their information:

    ```csharp
    IEnumerable<ComponentInfo> compoInfoList = await ComponentManager.GetInstalledComponentsAsync();

    foreach (ComponentInfo compoInfo in compoInfoList)
    {
        Log.Debug("Tag", "componentId: " + compoInfo.ComponentId);
        Log.Debug("Tag", "applicationId: " + compoInfo.ApplicationId);
        Log.Debug("Tag", "label: " + compoInfo.Label);
        Log.Debug("Tag", "iconPath: " + compoInfo.IconPath);
        Log.Debug("Tag", "ComponentType: " + compoInfo.ComponentType.ToString());
        Log.Debug("Tag", "isIconDisplayed: " + compoInfo.IsIconDisplayed.ToString());
        Log.Debug("Tag", "isManagedByTaskManager: " + compoInfo.IsManagedByTaskManager.ToString());
    }
    ```


## Related Information
  * Dependencies
    -   Tizen 5.5 and Higher
