# Bluetooth

You can use Bluetooth functionalities in your application, such as managing the local Bluetooth adapter, bonding, and exchanging data between Bluetooth-enabled devices. The Bluetooth standard provides a peer-to-peer (P2P) data exchange functionality over short distance between compliant devices.

This feature is supported in mobile and wearable applications only.

The main features of the Bluetooth API include:

- Managing the local Bluetooth adapter   

  You can [enable and disable the local Bluetooth adapter](#managing-the-local-bluetooth-adapter), and change the device name for it.

- Discovering devices   

  You can [discover other Bluetooth devices](#discovering-bluetooth-devices).

- Creating a bond with a Bluetooth device   

  You can [create a bond](#creating-a-bond-with-a-bluetooth-device) with another device retrieved through the discovery process. Bonding allows the 2 devices to establish a connection.

- Connecting to and exchanging data with a Bluetooth device   

  You can [connect to and exchange data with a remote Bluetooth device](#connecting-to-and-exchanging-data-with-a-bluetooth-device).

- Communicating with a health source device   

  The Health Device Profile defines the requirements for the Bluetooth health device implementation. In the profile, there are 2 device types: one device is a source, such as a blood pressure monitor or pulse oximeter, while the other is a sink, such as a mobile phone or laptop. You can use your device as a sink and [communicate with a health source device](#communicating-with-a-health-source-device).

The main Bluetooth (4.0) Low Energy features include:

- Managing the local Bluetooth adapter     

  The [Bluetooth adapter management](#managing-the-local-bluetooth-adapter) is performed the same way as in the regular Bluetooth API.

- Discovering Bluetooth Low Energy devices     

  You can [discover Bluetooth Low Energy devices](#discovering-bluetooth-low-energy-devices) in range. Through the discovery process, you can obtain basic information about available remote devices, such as their names and provided services.

- Managing the advertising options     

  You can [manage advertising](#managing-the-advertising-options) to control how your device announces itself to other Bluetooth Low Energy devices for discovery.

- Connecting to a Bluetooth Low Energy device     

  You can [connect to a remote Bluetooth Low Energy device](#connecting-to-a-bluetooth-low-energy-device). When connected, you can access services and characteristics of the remote device.

- Receiving notifications on connection state changes     

  You can [monitor the connection state](#receiving-notifications-on-connection-state-changes) to detect when the connection to the remote device is lost.

- Retrieving Bluetooth GATT services     

  You can [retrieve information about Bluetooth GATT services](#retrieving-bluetooth-gatt-services) provided by the remote device.

  Every GATT service defines characteristics it includes. By knowing the service, you know what features the Bluetooth device exposes.

- Accessing the Bluetooth GATT characteristic value     

  You can [read and write the Bluetooth GATT characteristic value](#accessing-the-bluetooth-gatt-characteristic-value).

  Characteristics allows you to monitor and sometimes control remote Bluetooth Low Energy devices. For example, a sensor reading can be exposed by the sensor device as a Bluetooth GATT characteristic.

- Receiving notifications on characteristic value changes     

  You can [monitor a characteristic value](#receiving-notifications-on-characteristic-value-changes) to detect any changes, for example, in sensor readings and battery level.

- Accessing the Bluetooth GATT descriptor value     

  You can [read and write the Bluetooth GATT descriptor value](#accessing-the-bluetooth-gatt-descriptor-value).

## Prerequisites

To use the Application (in [mobile](../../api/latest/device_api/mobile/tizen/application.html) and [wearable](../../api/latest/device_api/wearable/tizen/application.html) applications) and Bluetooth (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html) applications) APIs, the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/application.launch"/>
<tizen:privilege name="http://tizen.org/privilege/bluetooth"/>
```

## Managing the Local Bluetooth Adapter

You can enable or disable the local Bluetooth adapter, and set the device name using the system-provided service through the `ApplicationControl` interface (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControl) and [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControl) applications).

To use the Bluetooth functionality of the device, you must switch the Bluetooth adapter on. The Bluetooth API does not provide a method to enable or disable the Bluetooth adapter of the device directly. When Bluetooth is required, you must request the built-in Settings application on the device to let the user enable or disable Bluetooth.

**Figure: Bluetooth setting screen**

![Bluetooth setting screen](./media/bluetooth_onoff.png)

1. Retrieve a `BluetoothAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothAdapter) and  [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothAdapter) applications) with the `getDefaultAdapter()` method and prepare the `ApplicationControl` object (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControl) and  [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControl) applications) to request the Bluetooth switching operation:

   ```
   var bluetoothSwitchAppControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/edit', null, 'application/x-bluetooth-on-off');
   var adapter = tizen.bluetooth.getDefaultAdapter();
   ```

2. Define a callback for the `launchAppControl()` method:

   ```
   function launchSuccess() {
       console.log('Bluetooth Settings application is successfully launched.');
   }
   function launchError(error) {
       alert('An error occurred: ' + error.name + '. Please enable Bluetooth through the Settings application.');
   }
   ```

3. Define the reply callback of the application control which implements the `ApplicationControlDataArrayReplyCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/application.html#ApplicationControlDataArrayReplyCallback) and  [wearable](../../api/latest/device_api/wearable/tizen/application.html#ApplicationControlDataArrayReplyCallback) applications):

   ```
   var serviceReply = {
       /* Called when the launched application reports success */
       onsuccess: function(data) {
           if (adapter.powered) {
               console.log('Bluetooth is successfully turned on.');
           } else {
               console.log('Bluetooth is still switched off.');
           }
       },
       /* Called when launched application reports failure */
       onfailure: function() {
           alert('Bluetooth Settings application reported failure.');
       }
   };
   ```

4. If necessary, request launching the Bluetooth Settings with the prepared `bluetoothSwitchAppControl`:

   ```
   if (adapter.powered) {
       console.log('Bluetooth is already enabled');
   } else {
       console.log('Try to launch the Bluetooth Settings application.');
       tizen.application.launchAppControl(bluetoothSwitchAppControl, null, launchSuccess, launchError, serviceReply);
   }
   ```

5. To display the Bluetooth visibility switch, use the `application/x-bluetooth-visibility` MIME option. Bluetooth visibility means that the device is discoverable by other Bluetooth devices.

   ```
   var bluetoothVisibilityAppControl = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/edit', null, 'application/x-bluetooth-visibility');

   function launchVisibilityError(error) {
       alert('An error occurred: ' + error.name + '. Please enable Bluetooth visibility through the Settings application.');
   }
   var serviceVisibilityReply = {
       /* Called when the launched application reports success */
       onsuccess: function(data) {
           console.log('Bluetooth is ' + (adapter.visible ? 'now discoverable.' : 'still not visible.'));
       },
       /* Called when launched application reports failure */
       onfailure: function() {
           alert('Bluetooth Settings application reported failure.');
       }
   };
   tizen.application.launchAppControl(bluetoothVisibilityAppControl, null, null, launchVisibilityError, serviceVisibilityReply);
   ```

6. Set a friendly name for the device using the `setName()` method.

   The name helps to recognize the device in a list of [retrieved devices](#discovering-bluetooth-devices).

   ```
   adapter.setName(chatServerName);
   ```

## Discovering Bluetooth Devices

The device discovery process can retrieve multiple types of Bluetooth devices, such as printers, mobile phones, and headphones. To find the kind of devices you want to communicate with, the `BluetoothClass` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothClass) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothClass) applications) is used to define characteristics and capabilities of a Bluetooth device. The `BluetoothClassDeviceMajor` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothClassDeviceMajor) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothClassDeviceMajor) applications) and `BluetoothClassDeviceMinor` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothClassDeviceMinor) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothClassDeviceMinor) applications) specify the identifiers for major and minor Class of Device (CoD).

You can also retrieve the known devices which were bonded or found in a prior discovery process.

To search for remote devices and get the known devices:

1. Retrieve a `BluetoothAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothAdapter) applications) with the `getDefaultAdapter()` method:

   ```
   var adapter = tizen.bluetooth.getDefaultAdapter();
   ```

2. To search for remote devices, use the `discoverDevices()` method.

   The results of the search are returned in the `BluetoothDiscoverDevicesSuccessCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothDiscoverDevicesSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothDiscoverDevicesSuccessCallback) applications).

   ```
   var discoverDevicesSuccessCallback = {
       /* When a device is found */
       ondevicefound: function(device) {
           console.log('Found device - name: ' + device.name);
       }
   }

   /* Discover devices */
   adapter.discoverDevices(discoverDevicesSuccessCallback, null);
   ```

   > **Note**  
   > To allow other Bluetooth devices to find your device, you must set the device to be visible through the system settings.

3. To retrieve known devices (which have been previously paired or searched for), use the `getKnownDevices()` method.

   The results of the search are returned in the `BluetoothDeviceArraySuccessCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothDeviceArraySuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothDeviceArraySuccessCallback) applications).

   ```
   /* When a known device is found */
   function onGotDevices(devices) {
       console.log('The number of known devices: ' + devices.length);
   }

   /* Retrieve known devices */
   adapter.getKnownDevices(onGotDevices);
   ```

## Creating a Bond with a Bluetooth Device

To create a bond with a Bluetooth device:

1. Retrieve a `BluetoothAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothAdapter) applications) with the `getDefaultAdapter()` method:

   ```
   var adapter = tizen.bluetooth.getDefaultAdapter();
   ```

2. To create a bond with another device, use the `createBonding()` method:

   ```
   function onBondingSuccessCallback(device) {
       console.log('A bond is created - name: ' + device.name);
   }

   function onErrorCallback(e) {
       console.log('Cannot create a bond, reason: ' + e.message);
   }

   adapter.createBonding('35:F4:59:D1:7A:03', onBondingSuccessCallback, onErrorCallback);
   ```

   > **Note**  
   > The MAC address of the Bluetooth device is a `BluetoothAddress` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothAddress) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothAddress) applications). You can get the MAC address of the peer device from the `BluetoothDevice` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothDevice) applications), which is returned in the success callback of the `BluetoothAdapter`'s `getKnownDevices()` and `discoverDevices()` methods.

3. To end the bond with a remote device, use the `destroyBonding()` method:

   ```
   adapter.destroyBonding('35:F4:59:D1:7A:03');
   ```

## Connecting to and Exchanging Data with a Bluetooth Device

When you attempt to open a connection to another device, a Service Discovery Protocol (SDP) look-up is performed on the device, and the protocol and channel to be used for the connection are determined. If a connection is established and the socket is opened successfully, a `BluetoothSocket` instance (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothSocket) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothSocket) applications) with an open state is returned. The socket is subsequently used for exchanging data between the connected devices.

The Radio Frequency Communication (RFCOMM) is a set of transport protocols which allows multiple simultaneous connections to a device. If a device allows other devices to use its functionalities through this kind of connection, it is said to provide a service and it is called a server device. The devices that request the service are called client devices.

To connect to services provided by a server device to the client devices:

1. Retrieve a `BluetoothAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothAdapter) applications) with the `getDefaultAdapter()` method:

   `var adapter = tizen.bluetooth.getDefaultAdapter();`

2. To register a service and allow client devices to connect to it, use the `registerRFCOMMServiceByUUID()` method on the server device:

   ```
   adapter.registerRFCOMMServiceByUUID(serviceUUID, 'My service');
   ```

   > **Note**  
   > For P2P communication between 2 instances of the same application, the UUID can be hard-coded in your application. To retrieve the UUID of a Bluetooth device, use the `BluetoothDevice` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothDevice) applications). The object has an array of UUIDs available for the device.

   When the service has been successfully registered, the `BluetoothServiceSuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothServiceSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothServiceSuccessCallback) applications) is triggered.

3. Before establishing a connection, your device must be bonded with a peer device. For more information, see [Creating a Bond with a Bluetooth Device](#creating-a-bond-with-a-bluetooth-device).

4. To connect to the server device, use the `connectToServiceByUUID()` method on the client device:

   ```
   device.connectToServiceByUUID(serviceUUID, function(sock) {
       console.log('socket connected');
       socket = sock;
   }, function(error) {
       console.log('Error while connecting: ' + error.message);
   });
   ```

   When a connection between 2 devices is established, the `BluetoothSocketSuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothSocketSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothSocketSuccessCallback) applications) on the client device and the `onconnect` event handler in the `BluetoothServiceHandler` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothServiceHandler) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothServiceHandler) applications) on the server device are triggered.

5. To send data to the peer device, use the `writeData()` method:

   ```
   var somemsg = [3, 2, 1];
   var length = socket.writeData(somemsg);
   ```

   To send data between the devices, use a socket mechanism with the `BluetoothSocket` interface. The proper socket is received when the devices are connected.

6. To read the data on the server device, use the `readData()` method:

   ```
   var data = socket.readData();
   ```

   When an incoming message is received from the peer device, the `onmessage` event handler in the `BluetoothSocket` interface is triggered.

## Communicating with a Health Source Device

To increase the communication capabilities of your application, you must learn to communicate with a health source device:

1. Retrieve a `BluetoothHealthProfileHandler` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothHealthProfileHandler) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothHealthProfileHandler) applications):

   ```
   var adapter = tizen.bluetooth.getDefaultAdapter();
   var healthProfileHandler = adapter.getBluetoothProfileHandler('HEALTH');
   var healthApplication = null, healthChannel = null;
   ```

2. Register an application as a sink to wait for connection requests from health source devices (4100 means oximeter):

   ```
   function onSinkApp(app) {
       console.log('Success');
       healthApplication = app;
   }

   healthProfileHandler.registerSinkApplication(4100, 'testSinkApp', onSinkApp);
   ```

   When the sink application is registered successfully, the `BluetoothHealthApplicationSuccessCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothHealthApplicationSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothHealthApplicationSuccessCallback) applications) is invoked and you can get the registered sink application object.

3. Before establishing a connection, your device must be bonded with a health source device. For more information, see [Creating a Bond with a Bluetooth Device](#creating-a-bond-with-a-bluetooth-device).

4. To connect to the health source device, use the `connectToSource()` method of the `BluetoothHealthProfileHandler` interface:

   ```
   function onConnect(channel) {
       console.log('Success');
       healthChannel = channel;
   }

   adapter.getDevice('35:F4:59:D1:7A:03', function(device) {
         healthProfileHandler.connectToSource(device, healthApplication, onConnect);
   });
   ```

   When a connection between 2 devices is established, the success callback of the `connectToSource()` method is called. In addition, the `onconnect` event handler of the `BluetoothHealthApplication` instance (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothHealthApplication) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothHealthApplication) applications) is called, if the success callback attribute is set. You can get the connected `BluetoothHealthChannel` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothHealthChannel) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothHealthChannel) applications) from the callbacks.

5. To send data to the source device, use the `sendData()` method:

   ```
   var dataToSend = [0, 0, 0];
   var length = healthChannel.sendData(dataToSend);
   ```

   The `onmessage` event handler in the `BluetoothHealthChannelChangeCallback` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothHealthChannelChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothHealthChannelChangeCallback) applications) is called when the data is received, if you set a listener on the connected channel by using the `setListener()` method.

6. Disconnect from the health source device:

   ```
   healthChannel.close();
   ```

   When the channel is disconnected, the `onclose` event handler in the `BluetoothHealthChannelChangeCallback` interface is called.

## Discovering Bluetooth Low Energy Devices

To search for remote Bluetooth devices:

1. Define a scan event handler by implementing the `BluetoothLEScanCallback` callback (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEScanCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEScanCallback) applications).  
    The callback is invoked when a remote device has been detected.

   ```
   function successcallback(device) {
       console.log('Found device: ' + device.name + ' [' + device.address + ']');
   }
   ```

   > **Note**  
   > To allow other Bluetooth devices to find your device, you must set the device to be visible through the system settings.

2. Retrieve a `BluetoothLEAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEAdapter) applications) with the `getLEAdapter()` method of the `BluetoothManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothManager) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothManager) applications):

   ```
   var adapter = tizen.bluetooth.getLEAdapter();
   ```

3. To search for remote devices, use the `startScan()` method of the `BluetoothLEAdapter` interface:

   ```
   adapter.startScan(successcallback);
   ```

4. When you find the right remote device or the user cancels the scanning, disable the scan using the `stopScan()` method of the `BluetoothLEAdapter` interface:

   ```
   adapter.stopScan();
   ```

## Managing the Advertising Options

The Bluetooth Low Energy technology allows a device to broadcast some information without a connection between devices. The Bluetooth Low Energy API provides methods to control this advertising (broadcasting).

To control what information is advertised by the device:

1. Retrieve a `BluetoothLEAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEAdapter) applications) with the `getLEAdapter()` method of the `BluetoothManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothManager) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothManager) applications):

   ```
   var adapter = tizen.bluetooth.getLEAdapter();
   ```

2. Set up options and start advertising with the `startAdvertise()` method of the `BluetoothLEAdapter` interface:

   ```
   var advertiseData = new tizen.BluetoothLEAdvertiseData({
       includeName: true,
       serviceuuids: ['180f'] /* 180F is 16bit Battery Service UUID */
   });
   var connectable = true;

   adapter.startAdvertise(advertiseData, 'ADVERTISE', function onstate(state) {
       console.log('Advertising configured: ' + state);
   }, function(error) {
       console.log('startAdvertise() failed: ' + error.message);
   }, 'LOW_LATENCY', connectable);
   ```

   > **Note**  
   > To learn how to make your mobile device visible to other Bluetooth devices, see [Managing the Local Bluetooth Adapter](#managing-the-local-bluetooth-adapter).

3. To disable the advertising, use the `stopAdvertise()` method of the `BluetoothLEAdapter` interface:

   ```
   adapter.stopAdvertise();
   ```

## Connecting to a Bluetooth Low Energy Device

To connect to other Bluetooth Low Energy devices:

1. Retrieve a `BluetoothLEAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEAdapter) applications) with the `getLEAdapter()` method of the `BluetoothManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothManager) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothManager) applications):

   ```
   var adapter = tizen.bluetooth.getLEAdapter();
   ```

2. Define success and error callbacks for the connect operation:

   ```
   function connectFail(error) {
       console.log('Failed to connect to device: ' + e.message);
   }

   function connectSuccess() {
       console.log('Connected to device');
   }
   ```

3. Define a callback for the scan operation that connects to a found device and stops the scan.

   Within the callback request, establish a connection with the found device using the `connect()` method of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var remoteDevice = null;

   function onDeviceFound(device) {
       if (remoteDevice === null) {
           remoteDevice = device;
           console.log('Found device ' + device.name + '. Connecting...');

           device.connect(connectSuccess, connectFail);
       }

       adapter.stopScan();
   }
   ```

4. When the callbacks are completed, initiate the Bluetooth Low Energy scan using the `startScan()` method of the `BluetoothLEAdapter` adapter:

   ```
   adapter.startScan(onDeviceFound);
   ```

5. When the connection to the remote device is no longer required, disconnect from the device by calling the `disconnect()` method of the `BluetoothLEDevice` interface:

   ```
   remoteDevice.disconnect();
   ```

## Receiving Notifications on Connection State Changes

To receive notifications whenever the device connection is established or lost:

1. Retrieve a `BluetoothLEAdapter` object (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEAdapter) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEAdapter) applications) with the `getLEAdapter()` method of the `BluetoothManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothManager) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothManager) applications):

   ```
   var adapter = tizen.bluetooth.getLEAdapter();
   ```

2. Define a connection state change listener by implementing the `BluetoothLEConnectChangeCallback` callback (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEConnectChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEConnectChangeCallback) applications):

   ```
   var connectionListener = {
       onconnected: function(device) {
           console.log('Connected to the device: ' + device.name + ' [' + device.address + ']');
       },
       ondisconnected: function(device) {
           console.log('Disconnected from the device ' + device.name + ' [' + device.address + ']');
       }
   };
   ```

3. Define a callback for the scan operation that connects to a found device and stops the scan.

   Within the callback, register a connection state change listener using the `addConnectStateChangeListener()` method of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var remoteDevice = null;
   var watchId;

   function onDeviceFound(device) {
       if (remoteDevice === null) {
           remoteDevice = device;
           console.log('Found device ' + device.name + '. Connecting...');

           watchId = remoteDevice.addConnectStateChangeListener(connectionListener);

           remoteDevice.connect();
       }

       adapter.stopScan();
   }
   ```

4. When the callbacks are completed, initiate the Bluetooth Low Energy scan:

   ```
   adapter.startScan(onDeviceFound);
   ```

5. When the notifications about the connection are no longer required, deregister the listener from the device by calling the `removeConnectStateChangeListener()` method of the `BluetoothLEDevice` interface:

   ```
   remoteDevice.removeConnectStateChangeListener(watchId);
   ```

## Retrieving Bluetooth GATT Services

To retrieve a list of GATT services (Generic Attribute) provided by a remote device:

1. [Connect to a Bluetooth Low Energy device](#connecting-to-a-bluetooth-low-energy-device).

2. Define a connection state change listener by implementing the `BluetoothLEConnectChangeCallback` (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEConnectChangeCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEConnectChangeCallback) applications):

   ```
   function showGATTService(service, indent) {
       if (indent === undefined) {
           indent = '';
       }

       console.log(indent + 'Service ' + service.uuid + '. Has ' + service.characteristics.length +
                   ' characteristics and ' + service.services.length + ' sub-services.');

       for (var i = 0; i < service.services.length; i++) {
           showGATTService(service.services[i], indent + '   ');
       }
   }
   ```

3. Retrieve a list of GATT service UUIDs from the `uuids` attribute of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var serviceUUIDs = remoteDevice.uuids;
   ```

4. Retrieve GATT service information using the `getService()` method of the `BluetoothLEDevice` interface for every service UUID:

   ```
   var i = 0, service = null;

   for (i; i < serviceUUIDs.length; i++) {
       service = remoteDevice.getService(serviceUUIDs[i]);

       showGATTService(service);
   }
   ```

5. Retrieve all service UUIDs using the `getServiceAllUuids()` method of the `BluetoothLEDevice` interface:

   ```
   var services = remoteDevice.getServiceAllUuids();

   console.log('Services length ' + services.length);
   ```

## Accessing the Bluetooth GATT Characteristic Value

To read and write a value of the Bluetooth characteristic:

1. [Connect to a Bluetooth Low Energy device](#connecting-to-a-bluetooth-low-energy-device).

2. Retrieve a list of GATT service UUIDs from the `uuids` attribute of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var serviceUUIDs = remoteDevice.uuids;
   ```

3. Select a GATT service and use the `getService()` method of the `BluetoothLEDevice` interface to retrieve an object representing the service. In this example, the first service is used:

   ```
   var gattService = remoteDevice.getService(serviceUUIDs[0]);
   ```

4. Select an interesting characteristic from the `characteristics` attribute of the `BluetoothGATTService` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTService) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTService) applications). In this example, the first characteristic is used:

   ```
   var property = gattService.characteristics[0];
   ```

5. Define a callback implementing the `ReadValueSuccessCallback` callback (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#ReadValueSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#ReadValueSuccessCallback) applications), which receives the value of the characteristic:

   ```
   function readSuccess(value) {
       console.log('Characteristic value: ' + value);
   }

   function readFail(error) {
       console.log('readValue() failed: ' + error);
   }
   ```

6. To retrieve the GATT characteristic value, use the `readValue()` method of the `BluetoothGATTCharacteristic` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTCharacteristic) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTCharacteristic) applications):

   ```
   if (!property.isReadable) {
       console.log('Property seems not to be readable. Attempting to read...');
   }
   property.readValue(readSuccess, readFail);
   ```

7. To change the characteristic value, define callbacks and use the `writeValue()` method of the `BluetoothGATTCharacteristic` interface:

   ```
   function writeSuccess(value) {
       console.log('Written');
   }

   function writeFail(error) {
       console.log('writeValue() failed: ' + error);
   }

   if (!property.isWritable) {
       console.log('Property seems not to be writable. Attempting to write...');
   }
   var newValue = [82];

   property.writeValue(newValue, writeSuccess, writeFail);
   ```

## Receiving Notifications on Characteristic Value Changes

To monitor changes in a Bluetooth characteristic:

1. [Connect to a Bluetooth Low Energy device](#connecting-to-a-bluetooth-low-energy-device).

2. Retrieve a list of GATT service UUIDs from the `uuids` attribute of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var serviceUUIDs = remoteDevice.uuids;
   ```

3. Select a GATT service and use the `getService()` method of the `BluetoothLEDevice` interface to retrieve an object representing the service. In this example, the first service is used:

   ```
   var gattService = remoteDevice.getService(serviceUUIDs[0]);
   ```

4. Select an interesting characteristic from the `characteristics` attribute of the `BluetoothGATTService` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTService) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTService) applications). In this example, the first characteristic is used:

   ```
   var property = gattService.characteristics[0];
   ```

5. Define a callback implementing the `ReadValueSuccessCallback` callback (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#ReadValueSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#ReadValueSuccessCallback) applications), which receives the value of the characteristic every time the value changes:

   ```
   function onValueChange(value) {
       console.log('Characteristic value is now: ' + value);
   }
   ```

6. Register a value change listener using the `addValueChangeListener()` method of the `BluetoothGATTCharacteristic` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTCharacteristic) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTCharacteristic) applications):

   ```
   var watchId = property.addValueChangeListener(onValueChange);
   ```

7. When the notifications about the connection are no longer required, deregister the listener from the device by calling the `removeValueChangeListener()` method of the `BluetoothGATTCharacteristic` interface:

   ```
   property.removeValueChangeListener(watchId);
   ```

## Accessing the Bluetooth GATT Descriptor Value

To read and write a value of the Bluetooth descriptor:

1. [Connect to a Bluetooth Low Energy device](#connecting-to-a-bluetooth-low-energy-device).

2. Retrieve a list of GATT service UUIDs from the `uuids` attribute of the `BluetoothLEDevice` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothLEDevice) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothLEDevice) applications):

   ```
   var serviceUUIDs = remoteDevice.uuids;
   ```

3. Select a GATT service and use the `getService()` method  of the `BluetoothLEDevice` interface to retrieve an object representing the service. In this example, the first service is used:

   ```
   var gattService = remoteDevice.getService(serviceUUIDs[0]);
   ```

4. Select an interesting characteristic from the `characteristics` attribute of the `BluetoothGATTService` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTService) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTService) applications). In this example, the first characteristic is used:

   ```
   var characteristic = gattService.characteristics[0];
   ```

5. Select an interesting descriptor from the `descriptors` attribute of the `BluetoothGATTCharacteristic` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTCharacteristic) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTCharacteristic) applications). In this example, the first descriptor is used:

   ```
   var descriptor = characteristic.descriptors[0];
   ```

6. Define a callback implementing the `ReadValueSuccessCallback` callback (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#ReadValueSuccessCallback) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#ReadValueSuccessCallback) applications), which receives the value of the descriptor:

   ```
   function readSuccess(value) {
       console.log('Descriptor value: ' + value);
   }

   function readFail(error) {
       console.log('readValue() failed: ' + error);
   }
   ```

7. To retrieve the GATT descriptor value, use the `readValue()` method of the `BluetoothGATTDescriptor` interface (in [mobile](../../api/latest/device_api/mobile/tizen/bluetooth.html#BluetoothGATTDescriptor) and [wearable](../../api/latest/device_api/wearable/tizen/bluetooth.html#BluetoothGATTDescriptor) applications):

   ```
   descriptor.readValue(readSuccess, readFail);
   ```

8. To change the descriptor value, define callbacks and use the `writeValue()` method of the `BluetoothGATTDescriptor` interface:

   ```
   function writeSuccess(value) {
       console.log('Written');
   }

   function writeFail(error) {
       console.log('writeValue() failed: ' + error);
   }

   var newValue = [3];

   descriptor.writeValue(newValue, writeSuccess, writeFail);
   ```


## Related information
* Dependencies   
   - Tizen 2.4 and Higher for Mobile
   - Tizen 2.3.1 and Higher for Wearable
