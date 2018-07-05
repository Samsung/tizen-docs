# Input Device

You can manage input device keys and monitor key events.

This feature is supported in mobile and wearable applications only.

The main features of the Input Device API include:

- Gathering a list of supported keys   

  You can [get a list of all supported keys](#getting-a-list-of-all-supported-keys) and perform actions for the list.

- Getting key information by its name   

  You can [gather the key code based on the key name](#gathering-key-information).

- Registering and deregistering key events   

  You can [register keys](#registering-and-deregistering-keys) to handle DOM events for them.

The key names are listed in the [DOM Level 3 KeyboardEvent key Values](http://www.w3.org/TR/2014/WD-DOM-Level-3-Events-key-20140612) specification. The `name` attribute in the Input Device API is equal to the key value specified in the specification (the [Media Controller Keys](http://www.w3.org/TR/2014/WD-DOM-Level-3-Events-key-20140612/#keys-media-controller) section is the most relevant to the Input Device API). If the specification does not contain an appropriate entry for the key, the Input Device API provides a device-specific `name`.

## Getting a List of All Supported Keys

To get a list of all supported keys:

1. To get a supported key list, use the `getSupportedKeys()` method of the `InputDeviceManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/inputdevice.html#InputDeviceManager) and [wearable](../../api/latest/device_api/wearable/tizen/inputdevice.html#InputDeviceManager) applications):

   ```
   var keyCodes = {};
   var supportedKeys = tizen.inputdevice.getSupportedKeys();

   console.log('Supported keys list');
   for (var i = 0; i < supportedKeys.length; ++i) {
       keyCodes[supportedKeys[i].name] = supportedKeys[i].code;
       console.log(i + ': ' + supportedKeys[i].name + ' - ' + supportedKeys[i].code);
   }
   ```

2. Use the gathered list to handle `keydown` and `keyup` events.

## Gathering Key Information

To gather information about the key by its name:

1. Create a list of keys for which you want the information by using the `InputDeviceKey` object (in [mobile](../../api/latest/device_api/mobile/tizen/inputdevice.html#InputDeviceKey) and [wearable](../../api/latest/device_api/wearable/tizen/inputdevice.html#InputDeviceKey) applications).

   If you do not want to gather information about all supported keys, create a separate list of keys for information gathering. If you want information about all supported keys, use the list retrieved in the previous use case.

   ```
   var keys = ['VolumeUp', 'VolumeDown'];
   var keyCodes = {};
   ```

2. Check each key separately using the `getKey()` method of the `InputDeviceManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/inputdevice.html#InputDeviceManager) and [wearable](../../api/latest/device_api/wearable/tizen/inputdevice.html#InputDeviceManager) applications).

   If the result of the `getKey()` method is not `null`, you can access the key information. If the result is `null`, the key is not supported.

   ```
   for (var i = 0; i < keys.length; i++) {
       try {
           var key = tizen.inputdevice.getKey(keys[i]);
           if (key == null) {
               console.log('key: ' + keys[i] + ' is not supported');
           } else {
               keyCodes[key.name] = key.code;
               console.log('key: ' + key.name + ' has code: ' + key.code);
           }
       } catch (e) {
           console.log('error: ' + e.name + ':' + e.message + ', when getting key with name ' + keys[i]);
       }
   }
   ```

## Registering and Deregistering Keys

When you want to react to input device key presses, register the applicable key using the `InputDeviceManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/inputdevice.html#InputDeviceManager) and [wearable](../../api/latest/device_api/wearable/tizen/inputdevice.html#InputDeviceManager) applications). After registering the input device key, the application receives a DOM keyboard event when the key is pressed or released. When the events are no longer needed, deregister the key.

> **Note**  
> The application cannot register the mandatory keys (**ArrowLeft**, **ArrowRight**, **ArrowUp**, **ArrowDown**, **Enter**, and **Back**).

To manage input device keys, you must learn to change the action of a supported key:

1. To gather the keys, [get a list of all supported keys](#getting-a-list-of-all-supported-keys).

2. To register all supported keys for handling `keydown` and `keyup` events:

   ```
   var codeNamesMap = {};
   var supportedKeys = tizen.inputdevice.getSupportedKeys();

   for (var i = 0; i < supportedKeys.length; ++i) {
       try {
           tizen.inputdevice.registerKey(supportedKeys[i].name);
           codeNamesMap[supportedKeys[i].code] = supportedKeys[i].name;
           console.log('key: ' + supportedKeys[i].name + ' was registered for event handling');
       } catch (error) {
           console.log('failed to register ' + supportedKeys[i].name + ': ' + error);
       }
   }
   ```

   If you know the exact list of keys you want to register, the registration can also be done with the asynchronous `registerKeyBatch()` method:

   ```
   var keys = ['VolumeUp', 'VolumeDown'];

   function errorCB(err) {
       console.log('The following error occurred: ' + err.name);
   }

   function successCB() {
       console.log('All keys registered successfully');
   }

   tizen.inputdevice.registerKeyBatch(keys, successCB, errorCB);
   ```

3. To handle events for registered keys:

   ```
   window.addEventListener('keydown', function(keyEvent) {
       if (codeNamesMap.hasOwnProperty(keyEvent.keyCode)) {
           console.log('Registered key was pressed');
           /* Define some custom action */
       } else {
           console.log('Some other key was pressed');
       }
   });

   window.addEventListener('keyup', function(keyEvent) {
       if (codeNamesMap.hasOwnProperty(keyEvent.keyCode)) {
           console.log('Registered key was released');
           /* Define some custom action */
       } else {
           console.log('Some other key was released');
       }
   });
   ```

4. When custom actions are no longer needed, deregister the keys:

   ```
   for (var i = 0; i < supportedKeys.length; ++i) {
       tizen.inputdevice.unregisterKey(supportedKeys[i].name);
       console.log('key: ' + supportedKeys[i].name + ' was unregistered for event handling');
   }
   ```

   The deregistration can also be done with the `unregisterKeyBatch()` method:

   ```
   var keys = ['VolumeUp', 'VolumeDown'];

   function errorCB(err) {
       console.log('The following error occurred: ' + err.name);
   }

   function successCB() {
       console.log('Unregistered successfully');
   }

   tizen.inputdevice.unregisterKeyBatch(keys, successCB, errorCB);
   ```

   After deregistration, the `keydown` and `keyup` events are no longer triggered for the keys.

## Related Information
* Dependencies   
  - Tizen 2.4 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
