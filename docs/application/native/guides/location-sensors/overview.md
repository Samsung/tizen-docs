# Location and Sensors

The location and sensor features introduce how you can manage information about the geographical location and surrounding environment of the device, as well as human activity data. You can use a location service to track location information, and various device sensors to track the device environment and user activities.

You can use the following location and sensor features in your native applications:

- [Geofences](geofences.md)

  You can create geofences, which are virtual perimeters for a real-world geographic area. When a geofence is active, you can monitor the user location and receive alerts when the user enters or leaves the geofence area.

- [Location Information](location.md)

  The Location Manager provides the geographical location of the device for your application. You can access the user location, monitor location updates, and track the user movements within specific bounds or along a route. You can also manage the location settings, allowing the user to determine whether your application has access to location data.

- [Maps and Maps Service](maps.md)

  You can use the map services, such as geocoder, place searching, and routing. The map service requires a map provider, form which you can retrieve the required map details. Tizen currently supports the [HERE Maps provider](https://developer.here.com/).

- [Device Sensors](device-sensors.md)

  You can read and manage data from various sensors on the device. You can access information from various environmental sensors, such as the light and magnetic sensors, and from user-related sensors, such as the heart rate monitor.
  
- [User Awareness](user-awareness.md)  

  The User Awareness API provides functions to detect user presence and location based on multiple sensors (such as, light, motion, Wi-Fi, etc.). You can test the User Awareness API functionality only on a target device.


## Related Information
- Dependencies
  - Since Tizen 2.4
