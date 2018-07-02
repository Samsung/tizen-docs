# Location Information

Location information allows you to get a device's geographic position. Additionally, location-related information can also contain information about altitude, accuracy of the location and altitude readings, and the user's movement speed and direction.

The main features of the Tizen.Location namespace include:

-   Enabling the location service

    You can [use the location service](#service) to get the current location, receive location change events and satellite information, use location bounds, or track routes.

-   Defining the location type

    You can [select the appropriate location positioning system type](#method) to achieve the optimal quality level for the location service.


<a name="service"></a>
## Location Service

The [Tizen.Location](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.html) namespace provides the current location using the location sources specified in the [Tizen.Location.LocationType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.LocationType.html) enumeration. You can [use the location service](#start) to manage location information in various ways:

-   Get the user's current location

    You can set up event handlers to [track the current location](#current_location) of the device and [be notified of location change events](#update).

-   Get satellite information

    You can [access information on available GPS satellites](#satellite).

-   Use location bounds

    You can create [virtual perimeters](#bound) and monitor when a device enters or leaves them.


> **Note**
>
> To test the Tizen location-based services on the emulator, provide location data (longitude and latitude) using the Emulator Control Panel.  
>
> Since satellite data is not supported on the emulator, GPS status data is available on a target device only.


Asynchronous location-related updates and region monitoring notifications are implemented with events. Location-related events are called only if the location service has been started

You can use the location state and updates as follows:

-   If the location service is working correctly, [Tizen.Location.ServiceState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.ServiceState.html) is set to `Enabled`. The device can receive notifications about location change events only in this service state.
-   If the location service is unable to run on the requested device due to weak radio reception, the location service state is set to `Disabled`. If this situation persists for a longer period, stop the service and try again later, to conserve the device battery.

<a name="method"></a>
## Location Types

The [Tizen.Location.LocationType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.LocationType.html) enumeration is used to specify the desired quality of service of the [Tizen.Location.Location](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.Location.html) instance. For example, a location-based weather forecast application can require only very basic information to distinguish a city or a neighborhood, while a GPS navigation application can require the highest quality level to pinpoint a map location. Selecting the appropriate quality level not only helps to run the system efficiently, but also leads to a good user experience.

Using the `Tizen.Location.LocationType` enumeration allows your application to specify the following location positioning system types:

-   `Hybrid`, which selects the best method available at the moment
-   `Gps`, which uses the global positioning system
-   `Wps`, which uses the Wi-Fi positioning system
-   `Passive`, which uses the passive mode

## Prerequisites

To use the [Tizen.Location](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

```
<privileges>
   <privilege>http://tizen.org/privilege/location</privilege>
</privileges>
```

<a name="start"></a>
## Starting the Location Service

To start the location service:

1.  Create a [Tizen.Location.Locator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.Locator.html) instance with a specific value for its `LocationType` property before you use the location service.

    In this example, GPS is used as the source of the position data. You can use other values of the [Tizen.Location.LocationType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.LocationType.html) enumeration for hybrid and WPS sources.

    ```
    Tizen.Location.Locator locator;
    locator = new Locator(LocationType.Gps);
    ```

    Each `Tizen.Location.Locator` is an independent service. Multiple instances can be created in the same application to provide different services, such as GPS and WPS. Events are set for a given instance and are called only if the service is started for their `Tizen.Location.Locator` instance.

2.  Start the location service using the `Start()` method. This call is asynchronous and only initiates the process of starting the location service. Once the service is started, registered event handlers are invoked when their corresponding events take place. To know when the service becomes enabled, use the `ServiceStateChanged` event of the `Tizen.Location.Locator` class.

    ```
    locator.Start();
    ```

3.  Using the location service consumes power, so if the service is not used, stop updating the location using the `Stop()` method. Call the `Start()` method again if updated position information is needed.

    ```
    locator.Stop();
    ```

4.  At the end of the application life-cycle, destroy all used resources, such as the `Tizen.Location.Locator` instance:

    ```
    locator.Dispose();
    locator = NULL;
    ```

    If you destroy the `Tizen.Location.Locator` instance, there is no need to call the `Stop()` method to stop the service, as the service is automatically stopped. In addition, you do not have to remove any previously added event handlers.

<a name="current_location"></a>
## Getting the Current Location

To synchronously retrieve the current location of the device:

1.  Register an event handler for location service state changes and start the location service:

    ```
    locator.ServiceStateChanged += ServiceStateHandler;
    locator.Start();
    ```

    The `ServiceStateHandler()` method is an event handler, which is called when the location service state changes:

    ```
    bool serviceEnabled = false;
    void ServiceStateHandler(Object sender, ServiceStateChangedEventArgs e)
    {
        if (e.ServiceState == ServiceState.Enabled)
            serviceEnabled = true;
    }
    ```

2.  After starting the location service, call the `GetLocation()` method to get the current location information:

    ```
    Tizen.Location.Location location = locator.GetLocation();
    ```

    When the service state is set to `Disabled`, the `GetLocation()` method may not return the current location, but a previous one.

3.  When you no longer need the state updates, remove the event handler:

    ```
    locator.ServiceStateChanged -= ServiceStateHandler;
    ```

<a name="update"></a>
## Getting Location Events

You can get a notification of the device position being updated by using an event handler for the `LocationChanged` event of the [Tizen.Location.Locator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.Locator.html) class. The event handler is invoked periodically, receiving the device's current position with every call. You can use the event handler to retrieve the device position (given as coordinates) and convert it to the corresponding address.

To use the location change event handler:

1.  Register the event handler:

    ```
    locator.Interval = 2;
    locator.LocationChanged += LocationChangedHandler
    ```

    The `Interval` property determines the event call frequency. In this example, the event is called every 2 seconds.

2.  When the update is received, you can, for example, update the location that stores the device's current position:

    ```
    void LocationChangedHandler(Object sender, LocationChangedEventArgs e)
    {
        Tizen.Location.Location location = e.Location;
    }
    ```


    > **Note**   
	> The event is called only if the location service has already been started.


<a name="satellite"></a>
## Getting Satellite Information

You can retrieve and update information about a satellite visible to the device. The information includes azimuth, elevation, PRN, SNR, and NMEA data. An event handler is invoked periodically, receiving information about the visible satellites with every call.

To retrieve satellite information:

1.  Register an event handler for the `SatelliteStatusUpdated` event of the [Tizen.Location.GpsSatellite](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.GpsSatellite.html) class:

    ```
    satellite.Interval = 3;
    satellite.SatelliteStatusUpdated += SatelliteStatusChangedHandler;
    ```

    The `Interval` property of the `Tizen.Location.GpsSatellite` class determines the event call frequency. In this example, the event is called every 3 seconds.

2.  When the event handler is invoked, update the count of active and total satellites in view of the device:

    ```
    void SatelliteStatusChangedHandler(Object sender, SatelliteStatusChangedEventArgs e)
    {
        int active = e.ActiveCount;
        int inview = e.InViewCount;
    }
    ```


    > **Note**   
	> The event is called only if the location service has already been started.


<a name="bound"></a>
## Using Location Bounds

You can define a virtual perimeter, which is monitored to see whether the device enters or exits the area.

To use a location boundary:

1.  Create location bounds with the required area type (rectangle, circle, or polygon) needed for your application:

    ```
    Coordinate one, two, three;
    List<:Coordinate> list = new List<Coordinate>();
    one.Latitude = 10.10;
    one.Longitude = 10.10;
    two.Latitude = 20.20;
    two.Longitude = 20.20;
    three.Latitude = 30.30;
    three.Longitude = 10.10;
    list.Add(one);
    list.Add(two);
    list.Add(three);
    PolygonBoundary polygon = new PolygonBoundary(list);
    ```

    When a circular bound is needed, use the [Tizen.Location.CircleBoundary](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.CircleBoundary.html) class.

2.  To get notifications when the user enters or exits the defined perimeter, register an event handler:

    ```
    locator.ZoneChanged += ZoneChangedHandler;
    ```

    Implement the event handler for the `ZoneChanged` event of the [Tizen.Location.Locator](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Location.Locator.html) class:

    ```
    void ZoneChangedHandler(Object sender, ZoneChangedEventArgs e)
    {
        if (BoundaryState.In == e.BoundState) {
            /// Boundary changed
        }
    }
    ```

3.  Call the `AddBoundary()` method to add the boundary to a location service:

    ```
    locator.AddBoundary(polygon);
    ```

4.  When the boundary is no longer needed, destroy it:

    ```
    locator.RemoveBoundary(polygon);
    polygon.Dispose();
    ```

## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
