
# Widget Control

The widget control provides information about installing and running widget applications.

Also, it provides functions for sending update requests and retrieving details of running instances for the same package widget application.


The main features of the `Tizen.Applications.WidgetControl` class include:

-   Getting information on widget applications

    For installed (but not necessarily running) widget applications, you can [retrieve widget information](#getting_information) with the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class.


-   Listening widget lifecycle events on widget applications.

    For running widget applications, you can [listen widget application lifecycle events](#listening_events) with the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class.


-   Communicating with running widget instances

    For running widget instances, you can [trigger an update event, sending updated data, and retrieving running widget instances detail](#communicating_instances) with the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class.


## Prerequisites

To enable your application to use the widget control functionality:

1.  To use the methods and properties of the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class, include the [Tizen.Applications](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.html) namespace in your application:

    ```
    using Tizen.Applications;
    ```

2.  To use the methods and properties for getting information on widget applications of the `Tizen.Applications.WidgetControl` class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/widget.viewer</privilege>
    </privileges>
    ```

<a name="getting_information"></a>
## Getting information on widget applications

To get information on widget applications:

1.  Get the control of the installed widget application by creating an instance of the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class, with the ID of the widget application.

    ```
    WidgetControl control = new WidgetControl(Your Widget ID);
    ```

2.  Operate on the control:
    -   Get the main application ID, package ID, and available scale lists from the control:

        ```
        string mainId = control.MainAppId;
        string packageId = control.PackageId;
        IEnumerable<WidgetControl.Scale> scales = control.GetScales();
        ```


<a name="listening_events"></a>
## Listening widget lifecycle events on widget applications

To listen widget lifecycle events:

1.  Get the control of the installed widget application by creating an instance of the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class, with the ID of the widget application.

    ```
    WidgetControl control = new WidgetControl(Your Widget ID);
    ```

2.  Operate on the control:
    -   Add lifecycle listeners on the control

        ```
        private static void OnCreated(object sender, Tizen.Applications.WidgetLifecycleEventArgs args)
        {
            string instanceId = args.InstanceId;
            string widgetId = args.WidgetId;
            /// Widget application is created
        }

        private static void OnDestroyed(object sender, Tizen.Applications.WidgetLifecycleEventArgs args)
        {
            /// Widget application is destroyed
        }

        private static void OnPaused(object sender, Tizen.Applications.WidgetLifecycleEventArgs args)
        {
            /// Widget application is paused
        }

        private static void OnResumed(object sender, Tizen.Applications.WidgetLifecycleEventArgs args)
        {
            /// Widget application is resumed
        }

        control.Created += OnCreated;
        control.Created += OnDestroyed;
        control.Created += OnPaused;
        control.Created += OnResumed;

        string mainId = control.MainAppId;
        string packageId = control.PackageId;
        IEnumerable<WidgetControl.Scale> scales = control.GetScales();
        ```

<a name="communicating_instances"></a>
## Communicating with running widget instances

To communicate with running widget instances:

1.  Get the control of the installed widget application by creating an instance of the [Tizen.Applications.WidgetControl](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Applications.WidgetControl.html) class, with the ID of the widget application.

    ```
    WidgetControl control = new WidgetControl(Your Widget ID);
    ```

2.  Operate on the control:
    -   Get running widget instances

    ```
    IEnumerable<WidgetControl.Instance> instances = control.GetInstances();
    ```

3.  Operate on the instances:
    -   Get details of running widget instances and send an update to widget application.

    ```
    foreach (WidgetControl.Instance ins in instances) {
        /// Get widget instance content
        var data = ins.GetContent();

        /// Change widget update period
        ins.ChangePeriod(2.0);

        /// Trigger widget update
        ins.ChangeContent(data, true);
    }
    ```

## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
