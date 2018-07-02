# Geofences

A geofence is a virtual perimeter for a real-world geographic area. A geofence is defined by either a geopoint and radius for geopoint geofences, or by a MAC address for Wi-Fi and Bluetooth geofences. The geofence feature alerts the user when the geofence state changes (the user crosses the perimeter).

This feature is supported in mobile applications only.

The main features of the Geofence Manager API include:

- Using the geofence service

  You can [use the geofence service](#manager) to create different types of geofences and retrieve information about them, get the geofence event state, and track the user for alerts.

- Defining a geofence

  You can [define the type of the geofence](#definition) when creating one.

- Managing the geofence service

  You can allow the user to [manage the geofence places and fences](#settings) through My places.

<a name="manager"></a>
## Geofence Service

With the geofence service, you can:

- [Create different types of geofences](#start)

- [Get the current state](#status)

- Get [in and out alerts](#track) and [proximity alerts](#proximity)

  You can get notifications when the user approaches or crosses any geofences they have defined.

- [Retrieve information about created geofences](#info)

The geofence manager is set to `GEOFENCE_MANAGER_ERROR_NONE` if it is working correctly. The device can receive alerts about the geofence when a particular geofence service is started using the `geofence_manager_start_geofence()` function.

If the user revokes permission to use the location information, the geofence manager state is set to `GEOFENCE_MANAGER_PERMISSION_DENIED` and the same error is returned to the application attempting to use the geofence service.

Asynchronous geofence-related alerts (in or out) and event callbacks (a fence added or removed) are implemented with callback interfaces. Geofence alerts are received using the `GEOFENCE_STATE_UNCERTAIN`, `GEOFENCE_STATE_IN`, and `GEOFENCE_STATE_OUT` values of the [geofence_state_e](../../api/mobile/latest/group__CAPI__GEOFENCE__MANAGER__MODULE.html#ga266085fcc5f8fa9af62e54efe08cd912) enumerator.

<a name="definition"></a>
## Geofence Definition

Geofence definition defines the parameters of a geofence.

The 3 types of available geofences are geopoint, Wi-Fi, and Bluetooth. When creating the geofence, define the type using the `GEOFENCE_TYPE_GEOPOINT`, `GEOFENCE_TYPE_WIFI`, and `GEOFENCE_TYPE_BT` values of the [geofence_type_e](../../api/mobile/latest/group__CAPI__GEOFENCE__MANAGER__MODULE.html#ga15a724d2959e78b49b78b877e964f513) enumerator.

Creating a geopoint geofence requires a geopoint and a radius, whereas Wi-Fi and Bluetooth geofences require a MAC address. Based on the defined geofence type, the geofence manager creates the fence for the particular application.

<a name="settings"></a>
## Geofence Management through My Places

Tizen provides the user a way of managing geofence places and fences through the My places application. The following figure shows the default places and supported fences.

**Figure: My places**

![My places](./media/geofence_setting.png)

My places controls the adding, removing, and updating of places and fences. **Home**, **Office**, and **Car** are the default places, and **Map**, **Wi-Fi**, and **Bluetooth** are the supported fence methods. **Car** supports only Wi-Fi and Bluetooth as fence methods.

## Prerequisites

To use the functions and data types of the [Geofence Manager](../../api/mobile/latest/group__CAPI__GEOFENCE__MANAGER__MODULE.html) API, include the `<geofence_manager.h>` header file in your application:

```
#include <geofence_manager.h>
```

<a name="start"></a>
## Starting the Geofence Service

To start the geofence service:

1. Create a geofence manager handle using the `geofence_manager_create()` function:

   ```
   geofence_manager_h manager;
   geofence_manager_create(&manager);
   ```

   Each geofence manager is an independent service. The callbacks are set for a given geofence manager and are called only if the service is started by their manager.

2. Create a place to be used for the geofences:

   ```
   int place_id = -1; /* This is for creating a place */
   geofence_manager_add_place(manager, "place_name", &place_id);
   ```

   > **Note**  
   > A place is used to accommodate a number of geofences and is identified by a place ID. Each place can have a name. A geofence is identified by a geofence ID.

3. Create the geofences:

   1. Geopoint geofence:

      ```
      double latitude = 12.756738;
      double longitude = 77.386474;
      int radius = 100;
      char* address = "India";
      geofence_h fence_h;
      geofence_create_geopoint(place_id, latitude, longitude, radius, address, &fence_h);
      ```

   2. Bluetooth geofence:

      ```
      char* bssid = "82:45:67:7E:4A:3B";
      char* ssid = "Cafeteria";
      geofence_h fence_h;
      geofence_create_bluetooth(place_id, bssid, ssid, &fence_h);
      ```

   Add the geofence to the manager:

   ```
   int geofence_id = -1;
   geofence_manager_add_fence(manager, fence_h, &geofence_id);
   ```

4. Start the geofence service using the `geofence_manager_start()` function.

   This call is asynchronous and only initiates the process of starting the service. Once the service is started, the registered callbacks are invoked when their corresponding events take place. To know when the service becomes enabled, use the `geofence_manager_set_geofence_state_changed_cb()` callback.

   ```
   geofence_manager_start(manager, geofence_id);
   ```

5. Using the geofence service for geopoints adds to power consumption, so if the service is not used, stop the status alerts using the `geofence_manager_stop()` function. Call the `geofence_manager_start()` function again if the alerts are needed.

   ```
   geofence_manager_stop(manager, geofence_id);
   ```

6. Destroy all used resources, such as the geofence manager handle, using the `geofence_manager_destroy()` function:

   ```
   geofence_manager_destroy(manager);
   manager = NULL;
   ```

   If you destroy the handle, there is no need to call the `geofence_manager_stop()` function to stop the service as the service is automatically stopped. Also, you do not have to unset the previously set callbacks.

<a name="status"></a>
## Monitoring Geofence State Changes

To track the state of the geofence, use the geofence event callback. The geofence event callback is invoked whenever there is a request from the user, such as to add a geofence or to start a geofence service.

1. Register the callback using the `geofence_manager_set_geofence_event_cb()` function:

   ```
   geofence_manager_set_geofence_event_cb(manager, geofence_event, NULL);
   ```

2. Get the success or failure state of the event in the callback:

   ```
   geofence_manage_e user_action;
   geofence_manager_error_e user_error;
   void
   geofence_event(int place_id, int geofence_id, geofence_manager_error_e error,
                  geofence_manage_e manage, void *user_data)
   {
       user_action = manage;
       user_error = error;
   }
   ```

   > **Note**  
   > The geofence change event callback is used to let the user know whether the request is successful on the server side. This event callback is invoked only in the case of an asynchronous API. For a synchronous API, an error is immediately returned.

<a name="track"></a>
## Tracking the User for Geofence Crossing Alerts

To get information about whether the user has crossed the boundary of the geofence:

- Receive event-based notifications with a callback:

  1. You can be notified when the user crosses a particular fence. The callback receives the current state of the user (whether the user is in or out of the virtual boundaries of a geofence) with each call.

     Register the geofence state update callback using the `geofence_manager_set_geofence_state_changed_cb()` function.

     ```
     geofence_manager_set_geofence_state_changed_cb(manager, geofence_state_changed, NULL);
     ```

  2. Define the callback function:

     ```
     void
     geofence_state_changed(int geofence_id, geofence_state_e state, void *user_data) {}
     ```

- Receive the current state on request.

  You can get the current state of the user with respect to a geofence, such as their in or out state and the duration of the current state.

  1. To access the state or the duration, first create a status handle:

     ```
     int geofence_id = 1;
     geofence_status_h status_h;
     geofence_status_create(geofence_id, &status_h);
     ```

  2. To get the current state, call the `geofence_status_get_state()` function:

     ```
     geofence_state_e state;
     geofence_status_get_state(status_h, &state);
     ```

  3. To get the duration of the current state, call the `geofence_status_get_duration()` function:

     ```
     int duration;
     geofence_status_get_duration(status_h, &duration);
     ```

     The duration is provided in seconds.

  4. When no longer needed, destroy the status handle with the `geofence_status_destroy()` function:

     ```
     geofence_status_destroy(status_h);
     ```

<a name="proximity"></a>
## Tracking the User for Proximity Alerts

To get information about the user's proximity to a geofence:

1. You can get notifications about the proximity state updates using the state update callback. The callback receives the current state of the user with respect to proximity with each call.

   Register the proximity state update callback using the `geofence_manager_set_geofence_proximity_state_changed_cb()` function.

   ```
   geofence_manager_set_geofence_proximity_state_changed_cb(manager, proximity_state_changed, NULL);
   ```

2. Define the callback function:

   ```
   void
   proximity_state_changed(int geofence_id, geofence_proximity_state_e state,
                           geofence_proximity_provider_e provider, void *user_data) {}
   ```

<a name="info"></a>
## Retrieving Geofence Information

To get information about a geofence:

- Get common information (such as the type and place) about the geofences:

  ```
  geofence_type_e type;
  int place_id;
  geofence_get_type(fence_h, &type);
  geofence_get_place_id(fence_h, &place_id);
  ```

- Get information specific to a geopoint geofence:

  ```
  double latitude;
  double longitude;
  int radius;
  char *address;
  geofence_get_latitude(fence_h, &latitude);
  geofence_get_longitude(fence_h, &longitude);
  geofence_get_radius(fence_h, &radius);
  geofence_get_address(fence_h, &address);

  /* Release the resource after use */
  free(address);
  ```

- Get information specific to a Wi-Fi or Bluetooth geofence:

  ```
  char *bssid;
  char *ssid;
  geofence_get_bssid(fence_h, &bssid);
  geofence_get_ssid(fence_h, &ssid);

  /* Release the resources after use */
  free(bssid);
  free(ssid);
  ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
