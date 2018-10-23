# Location and Sensors

The location and sensor features introduce how you can manage information about the geographical location and surrounding environment of the device, as well as human activity data. You can use a location service to track location information, and various device sensors to track the device environment and user activities.

You can use the following location and sensor features in your native applications:

- [Geofences](geofences.md) **in mobile applications only**

  You can create geofences, which are virtual perimeters for a real-world geographic area. When a geofence is active, you can monitor the user location and receive alerts when the user enters or leaves the geofence area.

- [Location Information](location.md)

  The Location Manager provides the geographical location of the device for your application. You can access the user location, monitor location updates, and track the user movements within specific bounds or along a route. You can also manage the location settings, allowing the user to determine whether your application has access to location data.

- [Maps and Maps Service](maps.md)

  You can use the map services, such as geocoder, place searching, and routing. The map service requires a map provider, form which you can retrieve the required map details. Tizen currently supports the [HERE Maps provider](https://developer.here.com/).

- [Device Sensors](device-sensors.md)

  You can read and manage data from various sensors on the device. You can access information from various environmental sensors, such as the light and magnetic sensors, and from user-related sensors, such as the heart rate monitor.

- [Activity Recognition](activity.md)

  You can use the activity recognizer to gather information about the user movements and activity, such as walking and running. You can also recognize the stationary state and activities on a moving vehicle.

- [Gesture Recognition](gesture.md)

  You can monitor user gestures, such as double-taps, shakes, tilts, and wrist up movements. You can receive notifications about different device movement patterns, identify device states, and trigger events when the movement data meets predefined conditions.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
