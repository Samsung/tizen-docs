# Network Information

You can access information about the connection (such as cellular, Wi-Fi, or Ethernet) by reading the `navigator.connection.type` property. It is a textual representation of the current network status. Each time a connection is established or closed, the type changes.

The Network Information API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Network Information API include:

- Getting the connection status        

  You can compare the `navigator.connection.type` value with one of the values in the `Connection` global dictionary to [check the current connection status](#checking-the-connection-status).

- Monitoring network status changes        

  To [monitor the changes in the network status](#handling-network-related-events), you can use the `document.addEventListener()` method to register the required callbacks.

## Prerequisites

To enable your application to use the network information functionality:

1. To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

   ```
   document.addEventListener('deviceready', onDeviceReady, false);

   function onDeviceReady() {
       console.log('Cordova features now available');
   }
   ```

2. To use the Network Information API (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/networkInformation.html), [wearable](../../api/latest/device_api/wearable/tizen/cordova/networkInformation.html), and [TV](../../api/latest/device_api/tv/tizen/cordova/networkInformation.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/telephony"/>
   ```

## Checking the Connection Status

The following table lists the available connection types in the `Connection` global dictionary, which you can use to determine the current connection status.

**Table: Connection types**

| Property              | Value description             |
| --------------------- | ----------------------------- |
| `Connection.UNKNOWN`  | Connected, unknown connection |
| `Connection.ETHERNET` | Ethernet connection           |
| `Connection.WIFI`     | Wi-Fi connection              |
| `Connection.CELL_2G`  | Cellular 2G connection        |
| `Connection.CELL_3G`  | Cellular 3G connection        |
| `Connection.CELL_4G`  | Cellular 4G connection        |
| `Connection.CELL`     | Cellular generic connection   |
| `Connection.NONE`     | Not connected                 |

To determine whether the device is connected to a Wi-Fi network:

1. Place a `div` element with the `id="wifi-indicator"` attribute somewhere in the application HTML for text output:

   ```
   <div id="wifi-indicator">
   </div>
   ```

2. Get the connection type.

   It is a case-sensitive string in the `navigator.connection` object.

   ```
   var state = navigator.connection.type;
   ```

3. Compare the connection type to one of the defined values in the `Connection` global dictionary:

  ```
  if (state == Connection.WIFI) {
      document.querySelector('#wifi-indicator').textContent = 'Connected to WiFi';
  } else {
      document.querySelector('#wifi-indicator').textContent = 'Not connected to WiFi';
  }
  ```

The above code fills the `div` element with text, based on whether the device is connected to a Wi-Fi network.

## Handling Network-related Events

Manage the situations where the device connects to and disconnects from a network:

1. Register event handlers after Cordova is set up. The most convenient way is to use the `deviceready` event callback.

   ```
   document.addEventListener('deviceready', register);

   function register() {
       document.addEventListener('online', went_online);
       document.addEventListener('offline', went_offline);
   }   
   ```

2. Define the handlers:

   ```
   function went_online() {
       console.log('Went online');
   }

   function went_offline() {
       console.log('Went offline');
   }
   ```

   The `online` event fires when `connection.type` changes from `Connection.NONE` to any other value. Similarly, the `offline` event fires when `connection.type` becomes `Connection.NONE`.


## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 3.0 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
