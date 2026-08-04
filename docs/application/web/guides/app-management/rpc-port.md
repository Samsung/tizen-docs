# RPC Port

The RPC Port API provides inter-process communication (IPC) between Tizen applications. It allows applications to establish communication channels, serialize and deserialize data, and exchange messages using a protocol-based messaging system.

The RPC Port API is based on the native rpc-port library and is available for TV, mobile, and wearable profiles. All mandatory APIs are supported on the Tizen emulators.

The main features of the RPC Port API include the following:

- **Parcel serialization**

  The `Parcel` interface (in [TV](../../api/latest/device_api/tv/tizen/rpcport.html#Parcel), [Mobile](../../api/latest/device_api/mobile/tizen/rpcport.html#Parcel), and [Wearable](../../api/latest/device_api/wearable/tizen/rpcport.html#Parcel) applications) provides a serialization container for marshalling data across process boundaries. You can write and read various data types including bytes, integers, strings, arrays, and bundles.

- **Proxy/Stub communication**

  Applications can establish client-server communication patterns using `ProxyBase` and `StubBase` interfaces. The proxy connects to a remote stub to exchange messages and data.

- **Event publishing and receiving**

  Applications can publish events using the `publishEvent()` method of the `RPCPortManager` interface (in [TV](../../api/latest/device_api/tv/tizen/rpcport.html#RPCPortManager), [Mobile](../../api/latest/device_api/mobile/tizen/rpcport.html#RPCPortManager), and [Wearable](../../api/latest/device_api/wearable/tizen/rpcport.html#RPCPortManager) applications) and receive them using event receivers registered with the `addEventReceiver()` method.

- **Port management**

  Communication channels are managed through `Port` objects (in [TV](../../api/latest/device_api/tv/tizen/rpcport.html#Port), [Mobile](../../api/latest/device_api/mobile/tizen/rpcport.html#Port), and [Wearable](../../api/latest/device_api/wearable/tizen/rpcport.html#Port) applications). The API supports MAIN ports for primary communication and CALLBACK ports for response channels.

- **File sharing**

  Applications can share private files through ports using the `shareFile()` and `shareFiles()` methods of the `Port` interface. The target application is granted temporary permission to access the shared files.

## Prerequisites

To use the RPC Port API (in [TV](../../api/latest/device_api/tv/tizen/rpcport.html), [Mobile](../../api/latest/device_api/mobile/tizen/rpcport.html), and [Wearable](../../api/latest/device_api/wearable/tizen/rpcport.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<!-- Required for connecting to remote applications -->
<tizen:privilege name="http://tizen.org/privilege/appmanager.launch"/>

<!-- Required for data sharing between applications -->
<tizen:privilege name="http://tizen.org/privilege/datasharing"/>
```

## Establish RPC communication

Learning how to establish RPC communication using the proxy/stub pattern is a fundamental skill for inter-application communication:

1. Create a stub to listen for incoming connections:

   ```
   var stub = new tizen.rpcport.StubBase("myport");
   stub.listen();
   ```

2. Define callbacks for the stub to handle proxy connections and incoming messages:

   ```
   stub.onConnected = function(sender, instance)
   {
       console.log("Proxy connected: " + sender);
   };

   stub.onDisconnected = function(sender, instance)
   {
       console.log("Proxy disconnected: " + sender);
   };

   stub.onReceived = function(sender, instance, parcel)
   {
       var data = parcel.readString();
       console.log("Received from " + sender + ": " + data);
   };
   ```

3. Create a proxy to connect to the stub:

   ```
   var proxy = new tizen.rpcport.ProxyBase("com.example.targetapp", "myport");
   proxy.onConnected = function(receiver)
   {
       console.log("Connected to: " + receiver);
   };
   proxy.onDisconnected = function(receiver)
   {
       console.log("Disconnected from: " + receiver);
   };
   proxy.connect();
   ```

4. Get a port and send data:

   ```
   var port = proxy.getPort(tizen.rpcport.PortType.MAIN);
   var parcel = tizen.rpcport.createEmptyParcel();
   parcel.writeString("Hello, RPC Port!");
   parcel.send(port);
   ```

## Use Parcel for data serialization

The `Parcel` interface provides methods for serializing and deserializing various data types. Learning how to use Parcel allows you to exchange structured data between applications:

1. Create a parcel and write data:

   ```
   var parcel = tizen.rpcport.createEmptyParcel();
   
   /* Set version and protocol information */
   parcel.setTagEx(1, 0, 0, 1, 0);
   
   /* Write various data types */
   parcel.writeByte(0x12);
   parcel.writeInt16(12345);
   parcel.writeInt32(123456789);
   parcel.writeInt64(9223372036854775807);
   parcel.writeDouble(3.14159);
   parcel.writeBool(true);
   parcel.writeString("Hello, World!");
   ```

2. Read data from a parcel:

   ```
   var byteValue = parcel.readByte();
   var int16Value = parcel.readInt16();
   var int32Value = parcel.readInt32();
   var int64Value = parcel.readInt64();
   var doubleValue = parcel.readDouble();
   var boolValue = parcel.readBool();
   var stringValue = parcel.readString();
   ```

3. Send the parcel through a port:

   ```
   var port = proxy.getPort(tizen.rpcport.PortType.MAIN);
   parcel.send(port);
   ```

4. Convert parcel to bytes or dispose it:

   ```
   var bytes = parcel.toBytes();
   parcel.dispose();
   ```

## Publish and receive events

The event mechanism allows applications to broadcast data to multiple listeners. Learning how to publish and receive events enables loosely coupled communication between applications:

1. Publish an event:

   ```
   var data = new Uint8Array([1, 2, 3, 4, 5]);
   tizen.rpcport.publishEvent("com.example.myevent", data);
   ```

2. Add an event receiver:

   ```
   var watchId = tizen.rpcport.addEventReceiver("com.example.myevent", function(data)
   {
       console.log("Event received with data: " + data);
   });
   ```

3. Remove the event receiver when no longer needed:

   ```
   tizen.rpcport.removeEventReceiver(watchId);
   ```

## Share files

Applications can share private files through RPC ports. The file paths must be under the caller application's data path, and the target application is granted temporary access:

1. Share a single file:

   ```
   var port = proxy.getPort(tizen.rpcport.PortType.MAIN);
   var path = tizen.application.getAppSharedPath() + "data.txt";
   port.shareFile(path);
   ```

2. Share multiple files:

   ```
   var port = proxy.getPort(tizen.rpcport.PortType.MAIN);
   var paths = [
       tizen.application.getAppSharedPath() + "data1.txt",
       tizen.application.getAppSharedPath() + "data2.txt"
   ];
   port.shareFiles(paths);
   ```

3. Disconnect the port when finished:

   ```
   port.disconnect();
   ```

## Related information
* Dependencies
   - Tizen 10.1 and Higher for TV, Mobile, and Wearable
* API References
   - [TV](../../api/latest/device_api/tv/tizen/rpcport.html)
   - [Mobile](../../api/latest/device_api/mobile/tizen/rpcport.html)
   - [Wearable](../../api/latest/device_api/wearable/tizen/rpcport.html)
