# Location Information

Location information allows you to get a device's geographic position. Additionally, location-related information can contain information about altitude, accuracy of the location and altitude readings, and the user's movement speed and direction. The location manager manages location information on the device.

The main features of the Location Manager API include:

- Enabling the location service

  You can [use the location service](#service) to get the current or last known location, get location updates and satellite information, use location bounds, or track routes.

- Defining the location method

  You can [select the appropriate quality level](#method) of the location manager service.

- Defining the location settings

  You can [enable or disable specific positioning technologies](#settings) through the device location settings.

<a name="service"></a>
## Location Service

The Location Manager API (in [mobile](../../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) applications) provides the current location using the location sources specified in the [location method](#method). You can [use the location service](#start) to manage location information in various ways.

With the location manager, you can:

- Get the current location
- [Get the last known location](#last_known)
- [Get location updates](#update)
- [Use location bounds](#bound)
- [Retrieve satellite information](#satellite)
- [Track routes](#track)

> **Note**
>
> To test the Tizen location-based services on the emulator, provide location data (longitude and latitude) using the Emulator Control Panel.
>
> Since satellite data is not supported on the emulator, GPS status data is available on a target device only.

Asynchronous location-related updates and region monitoring notifications are implemented with callback interfaces (functions whose names end with "cb").

You can use the location state and updates as follows:

- If the location manager is working correctly, the location state is set to `LOCATIONS_SERVICE_ENABLED`. The device can receive notifications about location updates and accuracy changes only in this update state.
- If the location manager is unable to run on the requested device due to weak radio reception, the location update state is set to `LOCATIONS_SERVICE_DISABLED (LOCATIONS_ERROR_SERVICE_NOT_AVAILABLE)`. If this situation persists for a longer period, it is recommended to stop the service and try again to conserve the device battery.
- If the user revokes permission for the application to use location information, the location update state is set to `LOCATIONS_ACCESS_STATE_DENIED`, and the location manager stops all on-going services with the application. The application can request the device user for permission to continue the stopped service.

<a name="method"></a>
## Location Methods

The location method is used to specify the desired quality of service of the location manager. For example, a location-based weather forecast application can require location-related information only to distinguish a city or a neighborhood, while a GPS navigation application can require the highest quality level to pinpoint a map location. Selecting the appropriate quality level not only helps the location manager to run the system efficiently, but also leads to a good user experience.

Using the `location_method_e` structure (in [mobile](../../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#gaec8a29c8b701753a7c9d91f4f8acfac5) and [wearable](../../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#gaec8a29c8b701753a7c9d91f4f8acfac5) applications) allows your application to specify the following methods of location positioning system:

- GPS, which uses the global positioning system
- WPS, which uses the Wi-Fi positioning system
- Hybrid, which selects the best method available at the moment
- Passive, which passively receives location updates
- Fused, which uses the fused location method

Based on the desired method, the location manager provides best-effort location-based services, such as an asynchronous location update or region monitoring notification.

<a name="settings"></a>
## Location Settings

Tizen provides a robust way of controlling the usage of the location data through the device location settings. The following figure shows the various options for enabling or disabling specific positioning technologies.

**Figure: Location settings and indicator**

![Location settings and indicator](./media/location_setting_and_indicator.png)

The location-related functions work differently depending on which location settings are used.

The **GPS** setting controls the Global Positioning System usage. It uses GPS satellite signals and provides accurate positioning services, generally outdoors. The **Wireless networks** setting enables the usage of network-based positioning technology, which includes Wi-Fi and cell tower-based positioning, and improves the coverage of positioning services to indoors.

All location settings are initially enabled, if the device supports GPS. To disable them, the user must manually toggle the buttons. The manual task required from the user is understood as an implicit user consent.

> **Note**
>
> Either the **GPS** or the **Wireless networks** setting must be enabled to retrieve the current location of the device user.

Once the **GPS** or **Wireless networks** setting is enabled, the user can control the usage of the location data for each application separately using the privacy setting. If the privacy setting of the application is disabled, location data is no longer available for the application.

The applications whose location setting is enabled can get the current and last known location of the user.

## Prerequisites

To use the functions and data types of the Location Manager API (in [mobile](../../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html) applications), include the `<locations.h>` header file in your application:

```
#include <locations.h>
```

<a name="start"></a>
## Starting the Location Service

To start the location service:

1. Create a location manager handle using the `location_manager_create()` function before you use the location service.

   In this example, GPS is used as the source of the position data, so the first parameter is `LOCATIONS_METHOD_GPS`. You can use other values of the `location_method_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#gaec8a29c8b701753a7c9d91f4f8acfac5) and [wearable](../../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#gaec8a29c8b701753a7c9d91f4f8acfac5) applications), such as `LOCATIONS_METHOD_HYBRID`, `LOCATIONS_METHOD_WPS`, `LOCATIONS_METHOD_PASSIVE`, or `LOCATIONS_METHOD_FUSED`. `LOCATIONS_METHOD_HYBRID` uses both `LOCATIONS_METHOD_GPS` and `LOCATIONS_METHOD_WPS`, but the latter is less accurate.
   ```
   location_manager_h manager;
   location_manager_create(LOCATIONS_METHOD_GPS, &manager);
   ```

   Each location manager is an independent service. Multiple location managers can be created in the same application to provide different services, such as GPS and Bluetooth. Callbacks are set for a given location manager and are called only if the service is started for their manager.

   > **Note**
   >
   > The location manager is not thread-safe and depends on the main loop. Implement the location service within the main loop, and do not use it in a thread.

2. Start the location service using the `location_manager_start()` function. This call is asynchronous and only initiates the process of starting the location manager service. Once the manager is started, the registered callbacks are invoked when their corresponding events take place. To know when the service becomes enabled, use the `location_manager_set_service_state_changed_cb()` function.

   ```
   location_manager_start(manager);
   ```

3. Using the location service consumes power, so if the service is not used, stop updating the location using the `location_manager_stop()` function. Call the `location_manager_start()` function again if updated position information is needed.

   ```
   location_manager_stop(manager);
   ```

4. At the end of the application life-cycle, destroy all used resources, such as the location manager (`location_manager_destroy()`):

   ```
   location_manager_destroy(manager);
   manager = NULL;
   ```

   If you destroy the handle, there is no need to call the `location_manager_stop()` function to stop the service. The service is automatically stopped. Also, you do not have to unset previously set callbacks.

<a name="last_known"></a>
## Getting the Last Known Location

To retrieve synchronously the last known location of the device:

1. Register a callback function for location service state changes and start the location manager:

   ```
   ret = location_manager_set_service_state_changed_cb(manager, __state_changed_cb, NULL);
   ret = location_manager_start(manager);
   ```

   The `__state_changed_cb()` function is a callback, which is called when the status of the location service state changes.

   ```
   static location_service_state_e service_state;
   static void
   __state_changed_cb(location_service_state_e state, void *user_data)
   {
       service_state = state;
   }
   ```

2. After starting the location manager, call the `location_manager_get_last_location()` function to get the last location information, including the altitude, latitude, and direction:

    ```
    double altitude;
    double latitude;
    double longitude;
    double climb;
    double direction;
    double speed;
    double horizontal;
    double vertical;
    location_accuracy_level_e level;
    time_t timestamp;
    ret = location_manager_get_last_location(manager, &altitude, &latitude, &longitude,
                                             &climb, &direction, &speed, &level, &horizontal,
                                             &vertical, &timestamp);
    ```

	The function returns the last location stored in the system. When the current location is not fixed, the last location may not be the current location, but the old location.

    Use this function instead of repeatedly requesting current locations to spare the location manager from running costly positioning systems.

3. To get the current location information, call the `location_manager_get_location()` function after the service is enabled:

    ```
    static void
    __state_changed_cb(location_service_state_e state, void *user_data)
    {
        double altitude;
        double latitude;
        double longitude;
        double climb;
        double direction;
        double speed;
        double horizontal;
        double vertical;
        location_accuracy_level_e level;
        time_t timestamp;

        if (state == LOCATIONS_SERVICE_ENABLED) {
            ret = location_manager_get_location(manager, &altitude, &latitude, &longitude,
                                                &climb, &direction, &speed, &level,
                                                &horizontal, &vertical, &timestamp);
        }
    }
    ```

4. When you no longer need the state updates, unset the callback:

   ```
   location_manager_unset_service_state_changed_cb(manager);
   ```

<a name="update"></a>
## Getting Location Updates

You can get a notification of the position update using the position update callback. The callback is invoked periodically, receiving the device's current position with every call. You can use the callback to retrieve the device position (given as coordinates) and convert it to the corresponding address.

1. Register the callback using the `location_manager_set_position_updated_cb()` function:

   ```
   location_manager_set_position_updated_cb(manager, position_updated, 2, NULL);
   ```

   The third parameter determines the frequency of callback calls. In this example, the callback is called every 2 seconds.

2. When the update is received, you can, for example, update the variables that store the current position:

   ```
   static double user_latitude;
   static double user_longitude;
   static void
   position_updated(double latitude, double longitude, double altitude,
                    time_t timestamp, void *user_data)
   {
       user_latitude = latitude;
       user_longitude = longitude;
   }
   ```

   > **Note**
   >
   > The callback is called only if the location manager has been started. The same holds for all other callbacks registered with the manager.

<a name="bound"></a>
## Using Location Bounds

You can define a virtual perimeter, which is monitored to see whether the device enters or exits the area.

To use location bounds:

1. Create location bounds with the required area type (rectangle, circle, or polygon) needed for your application (each type has its own API sets):

   ```
   int poly_size = 3; /* Triangle shaped bounds */
   location_coords_s coord_list[poly_size];
   coord_list[0].latitude = 37; /* Temporary value */
   coord_list[0].longitude = 126;
   coord_list[1].latitude = 38;
   coord_list[1].longitude = 128;
   coord_list[2].latitude = 35;
   coord_list[2].longitude = 128;
   location_bounds_h bounds_poly;
   ret = location_bounds_create_polygon(coord_list, poly_size, &bounds_poly);
   ```

   When a circular bound is needed, use the `location_bounds_create_circle()` function.

2. To get the generated polygon bounds, register a callback function to notify you of the polygon coordinates:

   ```
   ret = location_bounds_foreach_polygon_coords(bounds_poly, capi_poly_coords_cb, NULL);
   ```

   Implement the callback function (the second parameter in the function above) separately:

   ```
   static double latitude;
   static double longitude;
   static bool
   capi_poly_coords_cb(location_coords_s coords, void *user_data)
   {
       latitude = coords.latitude;
       longitude = coords.longitude;

       return true;
   }
   ```

3. Register a callback, which is called when you enter or exit the defined region, using the `location_bounds_set_state_changed_cb()` function:

   ```
   location_bounds_set_state_changed_cb(bounds_poly, bounds_state_changed_cb, NULL);
   ```

   Implement the `bounds_state_changed_cb()` callback separately:

   ```
   static location_boundary_state_e bound_state;
   static void
   bounds_state_changed_cb(location_boundary_state_e state, void *user_data)
   {
       bound_state = state;
   }
   ```

4. Call the `location_manager_add_boundary()` function to add the bounds to a location manager:

   ```
   location_manager_add_boundary(manager, bounds_poly);
   ```

5. When the bounds are no longer needed, destroy them:

   ```
   location_bounds_destroy(bounds_poly);
   ```

<a name="satellite"></a>
## Getting Satellite Information

You can retrieve and update information about a satellite visible to the device. The information includes azimuth, elevation, PRN, SNR, and NMEA data. You can also get a notification of the satellite update using the satellite update callback. The callback is invoked periodically, receiving information about the visible satellites with every call.

1. Register the callback using the `location_manager_set_satellite_updated_cb()` function:

   ```
   gps_status_set_satellite_updated_cb(manager, capi_gps_status_satellite_updated_cb, 10, NULL);
   ```

   The third parameter determines the frequency of callback calls. In this example, the callback is called every 10 seconds.

2. When the update is received, the callback containing brief satellite information is called. To get detailed information on the satellite, call the `gps_status_foreach_satellites_in_view()` function in the callback. Variables that store the current satellite information are updated.

    ```
    int cur_azimuth;
    int cur_elevation;
    int cur_prn;
    int cur_snr;

    static bool
    capi_gps_status_get_satellites_cb(unsigned int azimuth, unsigned int elevation, unsigned int prn,
                                      int snr, bool is_in_use, void *user_data)
    {
        cur_azimuth = azimuth;
        cur_elevation = elevation;
        cur_prn = prn;
        cur_snr = snr;

        return true;
    }

    static int numofactive;
    static int numofinview;

    static void
    capi_gps_status_satellite_updated_cb(int num_of_active, int num_of_inview,
                                         time_t timestamp, void *user_data)
    {
        numofinview = num_of_active;
        if (num_of_inview > 0)
            gps_status_foreach_satellites_in_view(manager, capi_gps_status_get_satellites_cb, NULL);
    }
    ```

    > **Note**
    >
    > The callback is called only if the location manager has been started. The same holds for all other callbacks registered with the manager.

<a name="track"></a>
## Tracking the Route

To get information about the current position, velocity, and distance:

1. Receive periodic notifications.

   1. To get notifications of the position and velocity updates, register the position and velocity update callbacks. The callbacks are invoked periodically, receiving the device's current position or velocity with every call.

      - Register the position update callback using the `location_manager_set_position_updated_cb()` function:

        ```
        location_manager_set_position_updated_cb(manager, position_updated, 2, NULL);
        ```

      - Register the velocity update callback using the `location_manager_set_velocity_updated_cb()` function:

        ```
        location_manager_set_position_updated_cb(manager, velocity_updated, 2, NULL);
        ```

      The third parameter determines the frequency of the callback calls. In this example, the callbacks are called every 2 seconds.

   2. Define the position and velocity callback functions:

      ```
      void
      position_updated(double latitude, double longitude, double altitude,
                       time_t timestamp, void *user_data) {}
      void
      velocity_updated(double speed, double direction, double climb,
                       time_t timestamp, void *user_data) {}
      ```

      Within the callback, you can collect obtained data to get the points you have visited, to calculate traveled distance more precisely, or to calculate the average speed or climb.

2. Receive the current information.

   You can get the current information about position, velocity, or location accuracy:

   - To get information about the current position (altitude, latitude, and longitude), use the `location_manager_get_position()` function:

     ```
     time_t timestamp;
     double altitude;
     double latitude;
     double longitude;
     location_manager_get_position(manager, &altitude, &latitude, &longitude, &timestamp);
     ```

   - To get information about the current velocity (climb in km/h, direction as degrees from the north, and speed in km/h), use the `location_manager_get_velocity()` function:

     ```
     double climb;
     double direction;
     double speed;
     location_manager_get_velocity(manager, &climb, &direction, &speed, &timestamp);
     ```

   - To get information about the current accuracy level (see the `location_accuracy_level_e` enumeration in [mobile](../../api/mobile/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#ga4878b9a0afa5990dd2bb500850c1828b) and [wearable](../../api/wearable/latest/group__CAPI__LOCATION__MANAGER__MODULE.html#ga4878b9a0afa5990dd2bb500850c1828b) applications), and horizontal and vertical accuracy, use the `location_manager_get_accuracy()` function:

     ```
     location_accuracy_level_e level;
     double horizontal;
     double vertical;
     location_manager_get_accuracy(manager, &level, &horizontal, &vertical);
     ```

   - Use the `location_manager_get_location()` function to get all of the above 10 values at once:

     ```
     location_manager_get_location(manager, &altitude, &latitude, &longitude, &climb,
                                   &direction, &speed, &level, &horizontal, &vertical, &timestamp);
     ```

   - If the location service is currently unavailable, get the last values recorded by the location manager when the GPS signal was available. To get the information, use the following functions:

     - `location_manager_get_last_position()`
     - `location_manager_get_last_velocity()`
     - `location_manager_get_last_accuracy()`
     - `location_manager_get_last_location()`

     The syntax of these functions corresponds to the functions presented above.

3. Get the distance.

   To get a distance (in meters) between 2 points, use the `location_manager_get_distance()` function. The obtained value is a great-circle distance; the shortest distance between 2 points on the sphere.

   Provide the latitude and longitude of the starting point, the latitude and longitude of the end point, and the variable to store the obtained distance.

   ```
   double distance;
   location_manager_get_distance(37.28, 127.01, 52.23, 21.01, &distance);
   ```

   To get more a precise traveled distance, sum the distances between each 2 consecutive points, delivered by the periodic position update callback.


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
