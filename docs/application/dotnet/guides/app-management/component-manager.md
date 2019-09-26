
# Component Manager

The component manager provides information about installed and running components. 

The main features of the `Tizen.Applications.ComponentBased.ComponentManager` class include:

-   Managing the running component context

    For running components, you can retrieve the application running context and operate on it. You can [manage thec component running context](#manage_context) with the `Tizen.Applications.ComponentBased.ComponentManager` class.

-   Getting the component information

    For installed (but not necessarily running) componentss, you can retrieve information with the [Tizen.Applications.ComponentBased.ComponentInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentInfo.html) class.

Iterator methods are used to travel through a list of components. The `GetRunningComponentsAsync()` method of the `Tizen.Applications.ComponentBased.ComponentManager` class is used for running components and the `GetInstalledComponentsAsync()` method is used for installed components.

## Prerequisites

To enable your application to use the component management functionality:

1.  To use the methods and properties of the [Tizen.Applications.ComponentBased.ComponentManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ApplicationManager.html), [Tizen.Applications.ComponentBased.ComponentRunningContext](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentRunningContext.html), and [Tizen.Applications.ComponentBased.ComponentInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentInfo.html) classes, include the [Tizen.Applications.ComponentBased](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.html) namespace in your application:

    ```
    using Tizen.Applications.ComponentBased;
    ```

2.  To use classes and methods, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/appmanager.launch</privilege>
       <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
    </privileges>
    ```

<a name="manage_context"></a>
## Managing the Component Running Context

To get the component running context and its details, and to operate on the context:

1.  Get the context of the currently-running component by creating an instance of the [Tizen.Applications.ComponentBased.ComponentRunningContext](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentRunningContext.html) class, with the ID of the component from which the context is being obtained as a parameter.

    When an component is not running, it is impossible to get its context.

    ```
    ComponentRunningContext compoRunningContext = new ComponentRunningContext(Your Component ID);
    ```

2.  Operate on the context:
    -   Get the component ID, application ID, and instance ID from the context:

        ```
        string componentId = compoRunningContext.ComponentId;
        string applicationId = compoRunningContext.ApplicationId;
        string instanceId = compoRunningContext.InstanceId;
        ```

    -   Check the state of the component:

        ```
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

        ```
        compoRunningContext.Resume();
        ```

<a name="filter"></a>
## Getting the Component Information

To get the installed information and its details, and to operate on the information:

1.  Get the information of the currently-installed component by creating an instance of the [Tizen.Applications.ComponentBased.ComponentInfo](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentInfo.html) class, with the ID of the component from which the information is being obtained as a parameter.

    When an component is not installed, it is impossible to get its information.

    ```
    ComponentInfo compoInfo = new ComponentInfo(Your Component ID);
    ```

2.  Operate on the context:
    -   Get the component ID and application ID:

        ```
        string componentId = compoInfo.ComponentId;
        string applicationId = compoInfo.ApplicationId;
        ```
    -   Check the type of the component:

        ```
        if (compoInfo.ComponentType == ComponentType.Frame)
            /// The component is frame-component.
        else if (compoInfo.ComponentType == ComponentType.Service)
            /// The component is service-component
        else
            /// ComponentType is undefined
        ```

    -   Get the label and the icon path:

        ```
        string label = compoInfo.Label;
        string iconPath = compoInfo.IconPath;
        ```

3.  Call the `GetInstalledComponentsAsync()` method of the [Tizen.Applications.ComponentBased.ComponentManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.ComponentBased.ComponentManager.html) class and retrieve all components and print their information:

    ```
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
