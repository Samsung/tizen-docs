# Geolocation API Specification

Geolocation defines a location information interface. Common sources of location information are GPS, location inferred from the network (such as IP address), RFID, Wi-Fi, Bluetooth MAC address, and GSM/CDMA cell IDs. The [Geolocation](http://www.w3.org/TR/2013/REC-geolocation-API-20131024/#geolocation_interface) interface is implemented by the `Navigator` object instances. The location information is represented by the latitude and longitude coordinates.

This feature is supported in mobile and wearable applications only.

Using the `Geolocation` interface, you can [retrieve position information](#retrieving-location-information) with "one-shot" position requests (with the `getCurrentPosition()` method) or repeated position updates (with the `watchPosition()` method). Both methods take the following parameters:

- Success event handler, which is a function invoked when an attempt to obtain the current location is successful.
- Error event handler, which is a function invoked when an attempt to obtain the current location fails (optional).
- Options object, which holds additional properties (optional):
  - `enableHighAccuracy` enables high accuracy of the location information.
  - `timeout` defines the maximum length of time that is allowed to pass from the call until the corresponding success event handler is invoked.
  - `maximumAge` indicates that the application can accept cached location information whose age is no greater than the specified time.

> **Note**  
> In almost all cases, the location information reveals the location of the device user. To provide privacy for the user, a confirmation mechanism is provided for the geolocation features.

## Retrieving Location Information

To provide users with location-based features, you must learn to create a mobile GPS application to retrieve location information:

1. Create event handlers for the location requests.		

   The [Geolocation](http://www.w3.org/TR/2013/REC-geolocation-API-20131024/#geolocation_interface) interface allows 2 types of location requests: "one-shot" position request and repeated position updates. Both request types use the same event handlers. The success event handler is invoked when an attempt to obtain the current location is successful, while the error event handler is invoked when the attempt fails. The success event handler is mandatory, and contains a `position` parameter that hold the actual position information.

   ```
   function successCallback(position) {
       document.getElementById('locationInfo').innerHTML = 'Latitude: ' + position.coords.latitude +
                                                           '<br/>Longitude: ' + position.coords.longitude;
   }

   function errorCallback(error) {
       var errorInfo = document.getElementById('locationInfo');

       switch (error.code) {
           case error.PERMISSION_DENIED:
               errorInfo.innerHTML = 'User denied the request for Geolocation.';
               break;
           case error.POSITION_UNAVAILABLE:
               errorInfo.innerHTML = 'Location information is unavailable.';
               break;
           case error.TIMEOUT:
               errorInfo.innerHTML = 'The request to get user location timed out.';
               break;
           case error.UNKNOWN_ERROR:
               errorInfo.innerHTML = 'An unknown error occurred.';
               break;
       }
   }
   ```

2. Create a "one-shot" position request with the `getCurrentPosition()` method.

   The `maximumAge` parameter determines that if the user agent does not have cached position information that is fresher than 60000 milliseconds (1 minute), new location information is automatically obtained.

   ```
   function oneShotFunc() {
       if (navigator.geolocation) {
           navigator.geolocation.getCurrentPosition(successCallback, errorCallback,
                                                    {maximumAge: 60000});
       } else {
           document.getElementById('locationInfo').innerHTML = 'Geolocation is not supported.';
       }
   }
   ```

   If you do not want to wait for new position information, but are willing to use cached information regardless of how old it is, you can use the `maximumAge` and `timeout` parameters together (`{maximumAge: Infinity, timeout: 0}`). In this case, if the user agent has no position information cached, it automatically invokes the error event handler.

3. Create a repeated position update request with the `watchPosition()` method:

   ```
   function watchFunc() {
       if (navigator.geolocation) {
           watchId = navigator.geolocation.watchPosition(successCallback, errorCallback);
       } else {
           document.getElementById('locationInfo').innerHTML = 'Geolocation is not supported.';
       }
   }
   ```

4. The repeated position update request continues until the `clearWatch()` method is called with the corresponding identifier:

   ```
   function stopWatchFunc() {
       if (navigator.geolocation) {
           navigator.geolocation.clearWatch(watchId);
       } else {
           document.getElementById('locationInfo').innerHTML = 'Geolocation is not supported.';
       }
   }
   ```

The following figure illustrates the GPS application.

**Figure: GPS application (in mobile applications only)**

![GPS application (in mobile applications only)](./media/geolocation.png)

### Source Code

For the complete source code related to this use case, see the following file:

- [geolocation tutorial.html](http://download.tizen.org/misc/examples/w3c_html5/location/geolocation_api_specification)

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
