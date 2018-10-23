# Device Information

You can use a `device` global dictionary to access the device information, such as hardware UUID (unique ID) and software version.

The Device API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The following table lists the properties available in the global `Device` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/device.html#Device), [wearable](../../api/latest/device_api/wearable/tizen/cordova/device.html#Device), and [TV](../../api/latest/device_api/tv/tizen/cordova/device.html#Device) applications), and which allow you to [access specific device information](#loginfo).

**Table: Device properties**

| Property   | Description                              |
|------------|------------------------------------------|
| `cordova`  | Version of Cordova running on the device (as a string). For example: `5.1.1` |
| `model`    | Name of the device model. The value can be a production code name. |
| `platform` | Operating system name. For example: `Tizen` |
| `uuid`     | Device's Universally Unique Identifier (UUID). The value can be the device IMEI (International Mobile Equipment Identity) or other unique value for the device. The value is converted to a string. |
| `version`  | Operating system version (as a string). For example: `3.0` |

## Prerequisites

To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

```
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady() {
    console.log('Cordova features now available');
}
```

<a name="loginfo"></a>
## Accessing Device Properties

To retrieve information on the device, Cordova, and operating system, and output it in the system log:

1. Prepare a handler for the `deviceready` event:

   ```
   function onDeviceReady() {
       /* Cordova is ready */

       console.log('Cordova version: ' + device.cordova);
       console.log('Model name: ' + device.model);
       console.log('Platform: ' + device.platform);
       console.log('OS version: ' + device.version);
       console.log('Device UUID: ' + device.uuid);
   }
   ```

   UUID is a unique identifier for a device, and can be the device IMEI (International Mobile Equipment Identity).

2. Wait for the `deviceready` event:

   ```
   document.addEventListener('deviceready', onDeviceReady);
   ```


## Related Information
* Dependencies   
   - Tizen 3.0 and Higher for Mobile
   - Tizen 3.0 and Higher for Wearable
   - Tizen 3.0 and Higher for TV
