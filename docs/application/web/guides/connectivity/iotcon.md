# IoT Connectivity

[IoTivity](https://www.iotivity.org/) offers seamless device-to-device connectivity to address the emerging needs of the Internet of Things (IoT) through the open source reference implementation of the OIC (Open Interconnect Consortium) standard specifications. IoT connectivity (Iotcon) provides the means of using IoTivity in Tizen.

The Iotcon API is optional for Tizen mobile, wearable, and TV profiles, which means that it may not be supported on all mobile, wearable, and TV devices. The Iotcon API is supported on all Tizen Emulators.

IoT connectivity is usually handled with a server and client. The server is responsible for creating and providing resources, and the client can access those resources through requests.

The main features of the Iotcon API include:

- Creating a server

  You can [create a resource](#creating-a-new-resource) and send a presence event to the client when it becomes online.

- Managing resources

  You can add types and interfaces to an existing resource.

- Creating a client

  You can [find remote resources](#finding-remote-resources), [retrieve device and platform information](#retrieving-device-and-platform-information), and listen for server presence events.

- Remotely managing resources

  You can [retrieve](#sending-get-requests) and [modify](#sending-put-requests) the remote resource attributes with GET and PUT methods. You can also use POST and DELETE methods to modify the resources on a remote server. You can [monitor the resource attribute changes and the `isAlive` state](#observing-resource-changes).

  For more information on all available remote resource management methods, see the native [IoT Connectivity](../../../native/guides/connectivity/iotcon.md) guide.

## Prerequisites

To enable your application to use the IoT functionality:

1. To use the Iotcon API (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html) applications), the application has to request permission by adding the following privilege to the `config.xml` file:

   ```
   <tizen:privilege name="http://tizen.org/privilege/internet"/>
   ```

2. To make your application visible in the Tizen Store only for devices that support Iotcon, the application must specify the following feature in the `config.xml` file:

   ```
    <widget>
       <feature name="http://tizen.org/feature/iot.ocf"/>
    </widget>
   ```

   Additionally, to double-check the for Iotcon API support while the application is running, use the `tizen.systeminfo.getCapability()` method and enable or disable the code that needs the API, as needed:

   ```
   try {
       /* Checks whether a device supports the Iotcon API */
       var iotcon_feature = tizen.systeminfo.getCapability('http://tizen.org/feature/iot.ocf');
       console.log('Iotcon = ' + iotcon_feature);
   } catch (error) {
       console.log('Error name: ' + error.name + ', message: ' + error.message);
   }
   ```

For more information on OIC IoT standard specifications, see the [Open Connectivity Foundation (OCF) Web site](https://openconnectivity.org/).

## Creating a New Resource

To create a new resource:

1. Initialize a server and set the device name:

   1. For managing secure virtual resources, a CBOR format file (Concise Binary Object Representation) must be	available, preferably in the application local storage. For more information on security, see [Iotivity Security](https://wiki.iotivity.org/iotivity_security).

      ```
      var cborPath = 'path_to_my_app_storage/iotcon-server-test.dat';
      ```

   2. Initialize Iotcon and set a human-friendly name:

      ```
      tizen.iotcon.initialize(cborPath);
      tizen.iotcon.deviceName = 'Device 1';
      ```

   3. Get the Iotcon server object:

      ```
      var iotServer = tizen.iotcon.getServer();
      ```

2. Prepare a resource:

   1. On the server side, prepare a variable for storing the resource object and its attributes. The following example shows a door resource:

      ```
      var doorResource;
      var doorAttributes = {openstate: 'open'};
      ```

   2. Prepare handlers for the get, put, post, delete, and observing requests from the client.

      The exact list of required handlers depends on the resource interfaces. The following example uses the "oic.if.b" interface.

      ```
      var requestCallbacks = {
          onget: function(request) {/* Handler code */},
          onput: function(request) {/* Handler code */},
          onpost: function(request) {/* Handler code */},
          ondelete: function(request) {/* Handler code */},
          onobserving: function(request, observeType, observeId) {/* Handler code */}
      }
      ```

   3. Fill the `onget` handler with a code that sends a response to the client. Other handlers remain empty in this example (you can modify attributes in them).

      To send a response to the client:

      1. Create a new `Response` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#Response), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#Response), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#Response) applications) from the `Request` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#Request), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#Request), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#Request) applications): `new tizen.Response(request)`
      2. Create a new `Representation` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#Representation), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#Representation), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#Representation) applications), to be sent inside the response: `new tizen.Representation(doorResource.uriPath)`
      3. Fill the `Representation` object with values from the resource object.
      4. Send the response: `response.send()`

      ```
      var requestCallbacks = {
          onget: function(request) {
              console.log('onget');
              var response = new tizen.Response(request);
              try {
                  var representation = new tizen.Representation(doorResource.uriPath);
                  representation.resourceTypes = doorResource.resourceTypes;
                  representation.resourceInterfaces = doorResource.resourceInterfaces;
                  representation.attributes = doorAttributes;
                  response.representation = representation;
                  response.result = 'SUCCESS';
              } catch (err) {
                  console.log(err.name + ': ' + err.message);
                  response.result = 'ERROR';
              }
              response.send();
          }
      }
      ```

   4. Create a resource using the prepared handlers, chosen resource path, types, and interfaces:

      ```
      var uriPath = '/door';
      var resourceTypes = ['core.door'];
      var resourceInterfaces = ['oic.if.b'];
      var policy = {
          isObservable: true,
          isDiscoverable: true
      };

      doorResource = iotServer.createResource(uriPath, resourceTypes, resourceInterfaces, requestCallbacks, policy);
      ```

## Finding Remote Resources

To find remote resources:

1. Initialize a client and set the device name:

   1. For managing secure virtual resources, a CBOR format file (Concise Binary Object Representation) must be	available, preferably in the application local storage. For more information on security, see [Iotivity Security](https://wiki.iotivity.org/iotivity_security).

      ```
      var cborPath = 'path_to_my_app_storage/iotcon-client-test.dat';
      ```

   2. Initialize Iotcon and set a human-friendly name:

      ```
      tizen.iotcon.initialize(cborPath);
      tizen.iotcon.deviceName = 'Device 2';
      ```

   3. Get the Iotcon client object:

      ```
      var iotClient = tizen.iotcon.getClient();
      ```

   Now you can use the `iotClient` methods for IoT connectivity with the server.

2. On the client side, search for resources on servers:

   1. Get the client object:

      ```
      var client = tizen.iotcon.getClient();
      ```

   2. Set the remote server address and connectivity type.

      The `hostAddress` value must be in the Constrained Application Protocol (CoAP) format (`coap(s)://address:port`), for example, `coaps://[fe80::ae5a:14ff:fe24:b8fe]:12345` or `coaps://192.168.1.10:12345`. The `null` value indicates that the client communicates with all nodes (multicast).

      ```
      var hostAddress = null;
      var connectivityType = 'IP';
      ```

   3. Prepare a query. You can search for specific `resourceType` and `resourceInterface` values, and add an attribute filter:

      ```
      var query = {resourceType: 'core.door'};
      ```

      For more information, see the Query interface (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#Query), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#Query), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#Query) applications).

   4. Find a resource:

      ```
      client.findResource(hostAddress, query, connectivityType, foundSuccess, onerror);
      ```

      The `foundSuccess` and `onerror` parameters are success and error callbacks for an async operation:

      ```
      function onerror(err) {
          console.log('Failed to find resource: ' + err.message);
      }
      ```

      The success callback lists information, types, and interfaces for every found remote resource:

      ```
      function foundSuccess(resource) {
          if (resource) {
              console.log(resource.uriPath);
              console.log(resource.hostAddress);
              console.log(resource.deviceId);
              var resourceTypes = resource.resourceTypes;
              for (var i in resourceTypes) {
                  console.log(resourceTypes[i]);
              }
              var resourceInterfaces = resource.resourceInterfaces;
              for (var i in resourceInterfaces) {
                  console.log(resourceInterfaces[i]);
              }
          }
      }
      ```

## Retrieving Device and Platform Information

On the client side, you can get device and platform information from the server for a given remote resource:

1. Prepare the error and success callbacks:

   ```
   function onerror(err) {
       console.log('Failed to find resource: ' + err.message);
   }

   function foundSuccess(platformInfo) {
       console.log(platformInfo.platformId);
       console.log(platformInfo.modelNumber);
       console.log(platformInfo.platformVersion);
       console.log(platformInfo.operatingSystemVersion);
       console.log(platformInfo.systemTime);
       /* Other PlatformInfo object attributes; see the API Reference for details */
   }
   ```

2. Get the client object:

   ```
   var client = tizen.iotcon.getClient();
   ```

3. Prepare the server address, connectivity type, and query (with optional filters):

   ```
   /* hostAddress must be a valid IP address, or null for all nodes (multicast) */
   var hostAddress = 'coaps://192.168.0.10:12345';
   var connectivityType = 'IP';
   /* null means no filter */
   var query = null;
   ```

4. Retrieve the information:

   - Get the platform information from the remote server:

     ```
     client.findPlatformInfo(hostAddress, query, connectivityType, foundSuccess, onerror);
     ```

     The success callback is called with the `PlatformInfo` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#PlatformInfo), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#PlatformInfo), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#PlatformInfo) applications) as a parameter. You can access the platform information in the object attributes.

   - Get the device information from the remote server:

     ```
     client.findDeviceInfo(hostDeviceIpAddress, query, connectivityType, foundSuccess, onerror);
     ```

     The success callback is called with the `DeviceInfo` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#DeviceInfo), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#DeviceInfo), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#DeviceInfo) applications) as a parameter. You can access the device information in the object attributes.

## Sending GET Requests

On the client side, you can read resource attributes:

1. Prepare a callback for reading the attributes:

   ```
   function onresponse(remoteResponse) {
       if (remoteResponse.result != 'SUCCESS') {
           console.log('the result is not SUCCESS');

           return;
       }

       var repr = remoteResponse.representation;

       /* You can retrieve attributes from Representation object in RemoteResponse */
       for (var key in repr.attributes) {
           console.log(key + ': ' + repr.attributes[key]);
       }
   }
   ```

2. [Find a remote resource](#finding-remote-resources).

3. Once you have a `RemoteResource` object, use the `methodGet()` method to send a request to the server. For a list of resource attributes you can request, see the API Reference (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#RemoteResource), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#RemoteResource), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#RemoteResource) applications).

   ```
   /* filter results, query = null means no filter */
   query['filter'] = {openstate: 'open'};
   resource.methodGet(onresponse, query, onerror);
   ```

   As a result, the `onresponse` or (optional) `onerror` callback is called.

## Sending PUT Requests

On the client side, you can modify remote resource attributes using the PUT method:

1. Prepare a callback that is called after the PUT request:

   ```
   function onresponse(remoteResponse) {
       console.log('result is ' + remoteResponse.result);
       /* remoteResponse.result is expected to be 'RESOURCE_CHANGED' */
   }
   ```

2. [Find a remote resource](#finding-remote-resources).

3. Once you have a `RemoteResource` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#RemoteResource), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#RemoteResource), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#RemoteResource) applications), use the success callback to create a `Representation` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#Representation), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#Representation), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#Representation) applications). This object represents the changes in attributes, types, and interfaces.

   ```
   representation = new tizen.Representation(uriPath);
   representation.resourceTypes = ['core.door'];
   representation.attributes = {openstate: 'closed'};
   ```

4. Call the `methodPut()` method on the `RemoteResource` object:

   ```
   /* Optional filter, query = null means no filter */
   query['filter'] = {openstate: 'open'}
   resource.methodPut(representation, onresponse, query, onerror);
   ```

   After a successful request, the `onresponse` callback is called with the result and updated resource representation. On a failure, the (optional) `onerror` callback is called.

## Observing Resource Changes

On the client side, you can observe remote resource attribute changes with the `startObserving()` method, and the `isAlive` state with the `setResourceStateChangeListener()` method:

1. [Find a remote resource](#finding-remote-resources).

2. Prepare a callback for state change events:

   ```
   function onchanged(isAlive) {
       if (isAlive == true) {
           console.log('Remote resource is alive');
       } else {
           console.log('Remote resource is lost');
       }
   }
   ```

3. Register a listener on the `RemoteResource` object (in [mobile](../../api/latest/device_api/mobile/tizen/iotcon.html#RemoteResource), [wearable](../../api/latest/device_api/wearable/tizen/iotcon.html#RemoteResource), and [TV](../../api/latest/device_api/tv/tizen/iotcon.html#RemoteResource) applications):

   ```
   resource.setResourceStateChangeListener(onchanged);
   ```

4. When the notifications are no longer needed, deregister the listener:

   ```
   resource.unsetResourceStateChangeListener();
   ```

You can monitor attribute changes in a remote resource similarly using the `startObserving()` method on the `RemoteResource` object.

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
