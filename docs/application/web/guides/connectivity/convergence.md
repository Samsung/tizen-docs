# Convergence Services

You can establish connections between different devices as well as propagate data and commands among them using a collection of device-to-device Convergence services. The Convergence services are remote functions to access and control nearby devices. If you implement an application with the Convergence API, the application can discover devices within the same network, obtain information about available device-to-device Convergence services, connect to applicable devices, and execute the services remotely, while you need no understanding of the communication details, such as connectivity type.

This feature is supported in mobile and wearable applications only.

The main features of the Convergence API include:

- Service discovery		

  You can [discover all Convergence services](#searching-for-nearby-devices) supported by nearby devices.

- Remote communication		

  You can implement [communication between applications](#setting-up-the-appcommunicationservice-and-exchanging-messages) on remote devices.

- Remote launch and actions		

  You can [launch applications remotely](#launching-an-application-remotely), and [request them to take specific actions](#sending-an-application-control-remotely).

The following Convergence services are currently provided:

- AppCommunicationService            

  You can spawn 2 types of instances: server and client. Typically, the client finds available server services through a discovery, establishes a connection with one of the servers, and launches an application on the server side. The server cannot launch an application on the client side. Both the client and server can exchange text messages and binary payloads.

> **Note**
> The server for the AppCommunicationService can only be implemented on a TV device based on Tizen 3.0. You can develop a mobile or wearable client for the AppCommunicationService, if a server exists.

- RemoteAppControlService            

  The communication between RemoteAppControlService device instances does not involve servers. If the RemoteAppControlService is available on the device, remote applications can launch applications and send application control requests. The communication between devices begins after a discovery of the RemoteAppControlService.

## Prerequisites

To use the Convergence API (in [mobile](../../api/latest/device_api/mobile/tizen/convergence.html) and [wearable](../../api/latest/device_api/wearable/tizen/convergence.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/bluetooth"/>
<tizen:privilege name="http://tizen.org/privilege/internet"/>
<tizen:privilege name="http://tizen.org/privilege/d2d.datasharing"/>
```

## Searching for Nearby Devices

A discovery is a search for Convergence services in the same device-to-device network. To launch a discovery procedure and attempt to connect with the found service:

1. Search for nearby devices with the `startDiscovery()` method:

   ```
   var timeout = 60 * 60;

   try {
       tizen.convergence.startDiscovery(discoverySuccessCallback, onerror, timeout);
   } catch (err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

2. Implement the `discoverySuccessCallback` callback defined in the first parameter of the `startDiscovery()` method.

   The callback must contain 2 methods:

   - When a nearby device is detected, the `onfound` event is triggered. The `device` parameter holds the services available on the found device. In the following example, the `connect()` method is called on the found `RemoteAppControlService`.
   - When the discovery is finished and no more devices are found, the `onfinished` event is triggered.

   ```
   var discoverySuccessCallback = {
       onfound: function(device) {
           console.log('Found a device');
           console.log(' - id: ' + device.id);
           console.log(' - name: ' + device.name);
           console.log(' - type: ' + device.type);
           console.log(' - service amount: ' + device.services.length);
           for (i in device.services) {
               if (device.services[i] instanceof RemoteAppControlService) {
                   if (device.services[i].connectionState != 'CONNECTED') {
                       device.services[i].connect(onconnected, onerror);
                   }
               }
           }
       },

       onfinished: function(foundDevices) {
           console.log(' Device discovery has finished');
           if (foundDevices.length > 0) {
               console.log(' - devices found: ' + foundDevices.length);
           }
       }
   };

   function onerror(err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

3. When a connection is established, the `onconnected` callback is invoked with the connected `service` as a parameter:

   ```
   function onconnected(service) {
       console.log('Connected to the service');
   }
   ```

## Setting up the AppCommunicationService and Exchanging Messages

You can set up a server service, establish a connection between it and a client, and exchange messages.

### Launching a Server Service

To instantiate a server service:

1. Create a `ChannelInfo` object. It identifies the server and is used by the clients to address their demands. The first parameter of the `ChannelInfo` constructor is the server's application ID, set in its `config.xml` file. The second parameter is an ID set by you.

   ```
   var requestChannel = new tizen.ChannelInfo('targetApp0.main', 'chA');      
   ```

2. Define the success and error callbacks for the server service start:

   ```
   function onerror(err) {
       console.log(err.name +': ' + err.message);
   }

   function onstarted(channel, clientInfo) {
       console.log('Channel started');
       console.log('channel uri: ' + channel.uri);
       console.log('channel id: ' + channel.id);

       if (clientInfo) {
           console.log('clientInfo');
           console.log('isHost: ' + clientInfo.isHost);
           console.log('client id: ' + clientInfo.clientId);
           console.log('connection time: ' + clientInfo.connectionTime);
       }
   }
   ```

3. Instantiate an `AppCommunicationServerService` object:

   ```
   var service = new tizen.AppCommunicationServerService();     
   ```

4. Start the server service. In addition to the `ChannelInfo` object, you must provide the success and error callbacks defined earlier.

   ```
   service.start(requestChannel, onstarted, onerror);
   ```

### Listening for Incoming Messages on the Server Side

Applications can transfer data as **payload** objects, consisting of a key string and a data chunk in form of a string or binary values array.

To wait for incoming messages on the server side:

1. The started server service handles incoming messages through the `onnotify` callback, which is invoked when another service attempts to communicate with the server. The callback receives the sent payload and data about its sender.

   ```
   function onnotify(channel, payload, senderclientid) {
       console.log('On service notification');
       console.log('channel uri: ' + channel.uri);
       console.log('channel id: ' + channel.id);
       console.log('client id of sender: ' + senderclientid);
       for (i in payload) {
           console.log('payload: ' + payload[i].key + '-' + payload[i].value);
       }
   }
   ```

2. To be able to receive messages, register the `onnotify` callback with the `setListener()` method:

   ```
   service.setListener(onnotify);
   ```

   After the callback has been registered, all incoming data is handled by the `onnotify` callback.

### Communicating with the Server

In contrast to the server, a client service does not have to be instantiated. It can communicate with the server after discovering it.

To communicate with the server:

1. Discover available server services on the client side:

   ```
   function onerror(err) {
       console.log(err.name +': ' + err.message);
   }

   var timeout = 60 * 60;

   try {
       tizen.convergence.startDiscovery(discoverySuccessCallback, onerror, timeout);
   } catch (err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

2. Create a `ChannelInfo` instance with the same URI and ID as the channel used on the server side. Then start the available server service and send the payload to it.

   ```
   var serverService;
   var channel = new tizen.ChannelInfo('targetApp0.main', 'chA');

   function onerror(err) {
       console.log(err.name +': ' + err.message);
   }

   var requestPayload = {
       key: 'testPayload',
       value: 'Hello!'
   };

   function sendSuccessCallback(channel) {
       console.log('requestPayload sent');
       console.log('channel uri: ' + channel.uri);
       console.log('channel id: ' + channel.id);
   }

   function onstarted(channel, clientInfo) {
       serverService.send(channel, requestPayload, sendSuccessCallback, onerror);
   }

   var discoverySuccessCallback = {
       onfound: function(device) {
           for (i in device.services) {
               if (device.services[i] instanceof AppCommunicationServerService) {
                   serverService = device.services[i];
                   device.services[i].start(channel, onstarted, onerror);
               }
           }
       },

       onfinished: function(foundDevices) {
           console.log(' Device discovery has finished');
       }
   };
   ```

## Launching an Application Remotely

This use case assumes that a "targetApp0.main" application has been installed on the remote device.

To launch an application on a remote device:

1. Call the `startDiscovery()` method to establish connections with remote devices:

   ```
   var discoverySuccessCallback = {
       onfound: function(device) {
           for (i in device.services) {
               if (device.services[i].type === 'REMOTE_APP_CONTROL') {
                   if (device.services[i].connectionState != 'CONNECTED') {
                       device.services[i].connect(onconnected, onerror);
                   } else {
                       device.services[i].start(onstarted, onerror);
                   }
               }
           }
       },

       onfinished: function(foundDevices) {
           console.log('Device discovery has finished');
       }
   };

   function onerror(err) {
       console.log(err.name +': ' + err.message);
   }

   var timeout = 60 * 60;

   try {
       tizen.convergence.startDiscovery(discoverySuccessCallback, onerror, timeout);
   } catch (err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

2. An application on the remote device is started from the `onconnected` callback. The `remoteAppControlCallback` method handles the data sent from the remote device.

   ```
   var requestAppId = 'targetApp0.main';

   function remoteAppControlCallback(data) {
       for (var i = 0; i < data.length; i++) {
           console.log('key: ' + data[i].key + 'value: ' + data[i].value[0]);
       }
       service.disconnect();
   }

   function onstarted(service) {
       console.log('Remote app control service started');
       service.launch(requestAppId, remoteAppControlCallback, onerror);
   }

   function onconnected(service) {
       console.log('Connected to the remote app control service');
       service.start(onstarted, onerror);
       service.launch(requestAppId, remoteAppControlCallback, onerror);
   }
   ```

## Sending an Application Control Remotely

The `ApplicationControl` object is used to request applications to perform particular actions. This use case shows how to ask an image viewer to display a picture. For more information on application controls, see [Application Controls](../app-management/app-controls.md).

1. Use the `startDiscovery()` method to search for and connect to a `RemoteAppControlService`:

   ```
   var discoverySuccessCallback = {
       onfound: function(device) {
           for (i in device.services) {
               if (device.services[i] instanceof RemoteAppControlService) {
                   if (device.services[i].connectionState != 'CONNECTED') {
                       device.services[i].connect(onconnected, onerror);
                   }
               }
           }
       },

       onfinished: function(foundDevices) {
           console.log(' Device discovery has finished');
       }
   };

   function onerror(err) {
       console.log(err.name +': ' + err.message);
   } try {
       tizen.convergence.startDiscovery(discoverySuccessCallback, onerror, 60 * 60);
   } catch (err) {
       console.log(err.name + ': ' + err.message);
   }
   ```

2. Create the `ApplicationControl` object:

   ```
   var requestAppControl =
       new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/view', null,
                                    'image/jpeg', null,
                                    [new tizen.ApplicationControlData('images', [testImgData])]);
   ```

3. Use the `onconnected()` callback to send the application control request to the remote service. The `launchAppControl()` method takes as parameters the `ApplicationControl` object, optionally the target application ID, and a callback defining the actions to be taken on the remote service reply.

   ```
   function remoteAppControlCallback(data) {
       for (var i = 0; i < data.length; i++) {
           console.log('key: ' + data[i].key + 'value: ' + data[i].value[0]);
       }
   }

   function onconnected(service) {
       service.launchAppControl(requestAppControl, null,
                                remoteAppControlCallback, onerror);
   }
   ```


## Related Information
* Dependencies   
   - Tizen 4.0 and Higher for Mobile
   - Tizen 4.0 and Higher for Wearable
