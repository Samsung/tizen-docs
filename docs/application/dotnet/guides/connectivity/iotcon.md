# IoT Connectivity


[IoTivity](https://www.iotivity.org/) offers seamless device-to-device connectivity to address the emerging needs of the Internet of Things (IoT) through the open source reference implementation of the OCF (Open Connectivity Foundation) standard specifications. The Tizen.Network.IoTConnectivity namespace provides the means of using IoTivity in Tizen.

**Figure: IoTivity in Tizen**

![IoTivity in Tizen](./media/iotivity.png)

You can handle the resources between a server and client. The server is responsible for creating and providing resources, and the client can access and control those resources through requests.

The main features of the Tizen.Network.IoTConnectivity namespace include:

-   Resource management

    Entities in the physical world, such as a light, a fan, or modules of a home appliance, are represented as resources. You can manage the IoT resources with the server, which can [create resources](#scenario_1) and later destroy them.

- Remote resource management

    If the resource created by the server is discoverable, the client that knows the resource type can [find the resource](#scenario_2) and access its information.

- Requests and responses

    The client can send various requests to the server resources:

    -   GET request: Read the resource information and [get a representation of the resource](#scenario_3) from the server
    -   PUT request: Ask the server to [update the resource representation](#scenario_4).

    The server receives the request, processes it, and sends a response to the client. The client can check the result and the response.

    If the server resource is observable, the client can register an event handler to [observe the resource](#scenario_5). When the resource state changes, the server notifies the client through the registered event handler.

## Prerequisites


To enable your application to use the IoT functionality:

1.  To use the [Tizen.Network.IoTConnectivity](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/network.get</privilege>
       <privilege>http://tizen.org/privilege/internet</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Network.IoTConnectivity namespace, include it in your application:

    ```
    using Tizen.Network.IoTConnectivity;
    ```

3. To initialize IoT connectivity, use the `Initialize()` method of the [Tizen.Network.IoTConnectivity.IoTConnectivityClientManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.IoTConnectivityClientManager.html) class:

    ```
    string datPathClient = "/opt/usr/home/owner/share/res/iotcon-test-svr-db-client.dat";
    /// Must be a file path which can be read and written in the application

    IoTConnectivityClientManager.Initialize(datPathClient);
    ```

4. When the resources are no longer needed, deinitialize the IoT connection using the `Deinitialize()` method:

    ```
    IoTConnectivityClientManager.Deinitialize();
    ```

<a name="scenario_1"></a>
## Registering Resources

To create and register resources:

1.  Create the resource types by creating a new instance of the [Tizen.Network.IoTConnectivity.ResourceTypes](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.ResourceTypes.html) class.

    In the following example, a door resource type is added:

    ```
    ResourceTypes types = new ResourceTypes(new List<string>() {"oic.iot.door"});
    ```

2. Register the door resource by calling the `DoorResource()` constructor which is a user-defined child class of the [Tizen.Network.IoTConnectivity.Resource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.Resource.html) abstract class:

    ```
    public class DoorResource : Resource
    {
        public const string DoorUri = "/door/uri1";

        public DoorResource(string uri, ResourceTypes types, ResourceInterfaces interfaces, ResourcePolicy policy)
            : base(uri, types, interfaces, policy) {}

        protected override Response OnDelete(Request request)
        {
            return response;
        }

        protected override Response OnGet(Request request)
        {
            return response;
        }

    }

    ResourceInterfaces ifaces = new ResourceInterfaces(new List<string>() { ResourceInterfaces.DefaultInterface });
    ifaces.Add(ResourceInterfaces.BatchInterface);

    Resource resource = new DoorResource(DoorResource.DoorUri, types, ifaces, ResourcePolicy.Discoverable | ResourcePolicy.Observable);
    ```

<a name="scenario_2"></a>
## Finding Resources

To find resources:

1.  To find a resource, call the `StartFindingResource()` method of the [Tizen.Network.IoTConnectivity.IoTConnectivityClientManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.IoTConnectivityClientManager.html) class:

    ```
    int RequestId = -1;

    ResourceQuery query = new ResourceQuery();
    query.Type = "oic.iot.door";

    RequestId = IoTConnectivityClientManager.StartFindingResource(IoTConnectivityClientManager.MulticastAddress, query);
    ```

2. To get the remote resource handle information, use an event handler registered for the `ResourceFound` event of the `Tizen.Network.IoTConnectivity.IoTConnectivityClientManager` class before calling the `StartFindingResource()` method:

    ```
    ResourceFoundEventArgs outArgs = null;

    EventHandler<ResourceFoundEventArgs> handler = null;
    EventHandler<FindingErrorOccurredEventArgs> errorHandler = null;

    handler = (sender, e) =>
    {
        Log.Info(LOGTAG, "ResourceFound:" + e.RequestId + ", HostAddress:" + e.Resource.HostAddress + ", UriPath:" + e.Resource.UriPath);
        IoTConnectivityClientManager.ResourceFound -= handler;
        IoTConnectivityClientManager.FindingErrorOccurred -= errorHandler;
        outArgs = e;
    };

    errorHandler = (sender, e) =>
    {
        Log.Info(LOGTAG, "FindingErrorOccurred:" + e.RequestId + ", Message:" + e.Error.Message);
    };

    IoTConnectivityClientManager.ResourceFound += handler;
    IoTConnectivityClientManager.FindingErrorOccurred += errorHandler;
    ```

<a name="scenario_3"></a>
## Sending GET Requests

To send GET requests to a server:

1.  On the client side, [find resources](#scenario_2) and retrieve the remote resource handle using an event handler registered for the `ResourceFound` event of the [Tizen.Network.IoTConnectivity.IoTConnectivityClientManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.IoTConnectivityClientManager.html) class.
2. Send the GET request to the server using the `GetAsync()` method of the [Tizen.Network.IoTConnectivity.RemoteResource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.RemoteResource.html) class:

    ```
    if (outArgs != null)
    {
        var response = await outArgs.Resource.GetAsync();
    }
    ```

3. On the server side, the `OnGet()` method (which was defined when [registering resources](#scenario_1)) is called when a request arrives from the client. The request handles are passed to this method.

    You can return a response to the client in the `OnGet()` method:

    ```
    public class DoorResource : Resource
    {
        private const string DOOR_ATTRIBUTE = "DOOR_ATTRIBUTE";

        protected override Response OnGet(Request request)
        {
            Representation representation = new Representation();

            representation.UriPath = UriPath;
            Attributes attributes = new Attributes()
            {
                {DOOR_ATTRIBUTE, 4}
            };
            representation.Attributes = attributes;

            Response response = new Response()
            {
                Representation = representation,
                Result = ResponseCode.Ok
            };

            return response;
        }
    }
    ```

4. On the client side, handle the response returned by the `GetAsync()` method of the `Tizen.Network.IoTConnectivity.RemoteResource` class.

    Handle the response appropriately. If the response is a success, the resource information can be included in it.

    ```
    if (outArgs != null)
    {
        var response = await outArgs.Resource.GetAsync();

        if (response != null)
        {
            string DOOR_ATTRIBUTE = "DOOR_ATTRIBUTE";
            Log.Info(LOGTAG, "response.Result: " + response.Result); /// 0 (ResponseCode.Ok)
            Log.Info(LOGTAG, "response.Representation.UriPath: " + response.Representation.UriPath); /// /door/uri1
            Log.Info(LOGTAG, "response.Representation.Attributes[DOOR_ATTRIBUTE]: " + response.Representation.Attributes[DOOR_ATTRIBUTE]); /// 4
        }
    }
    ```

<a name="scenario_4"></a>
## Sending PUT Requests

To send PUT requests to a server:

1.  On the client side, [find resources](#scenario_2) and retrieve the remote resource handle using an event handler registered for the `ResourceFound` event of the [Tizen.Network.IoTConnectivity.IoTConnectivityClientManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.IoTConnectivityClientManager.html) class.
2. Send the PUT request to the server using the `PutAsync()` method of the [Tizen.Network.IoTConnectivity.RemoteResource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.RemoteResource.html) class.

    First create the representation and attributes, and set the desired attribute values, and then send the representation using the `PutAsync()` method.

    ```
    if (outArgs != null)
    {
        Representation repr = new Representation();
        repr.UriPath = "/door/uri1";
        repr.Type = new ResourceTypes(new List<string>() {"oic.iot.door"});
        repr.Attributes = new Attributes()
        {
            {"DOOR_ATTRIBUTE", 1}
        };

        var response = await outArgs.Resource.PutAsync(repr);
    }
    ```

3. On the server side, the `OnPut()` method (which was defined when [registering resources](#scenario_1)) is called when a request arrives from the client. The request handles are passed to this method.

    You can set this request on the server side and return a response to the client in the `OnPut()` method:

    ```
    public class DoorResource : Resource
    {
        private const string DOOR_ATTRIBUTE = "DOOR_ATTRIBUTE";

        protected override Response OnPut(Request request)
        {
            Representation representation = request.Representation;
            SetAttributes(representation.Attributes);

            Representation newRepresentation = new Representation();
            newRepresentation.UriPath = UriPath;
            Attributes attributes = new Attributes()
            {
                {DOOR_ATTRIBUTE, 4}
            };
            newRepresentation.Attributes = attributes;

            Response response = new Response()
            {
                Representation = newRepresentation,
                Result = ResponseCode.Ok
            };

            return response;
        }

        private void SetAttributes(Attributes s) {}
    }
    ```

4. On the client side, handle the response returned by the `PutAsync()` method.

    Handle the response appropriately. If the response is a success, the resource information can be included in it.

    ```
    if (outArgs != null)
    {
        Representation repr = new Representation();
        repr.UriPath = "/door/uri1";
        repr.Type = new ResourceTypes(new List<string>() {"oic.iot.door"});
        repr.Attributes = new Attributes()
        {
            {"DOOR_ATTRIBUTE", 1}
        };
        var response = await outArgs.Resource.PutAsync(repr);

        if (response != null)
        {
            string DOOR_ATTRIBUTE = "DOOR_ATTRIBUTE";
            Log.Info(LOGTAG, "response.Result: " + response.Result); /// 0 (ResponseCode.Ok)
            Log.Info(LOGTAG, "response.Representation.UriPath: " + response.Representation.UriPath); /// /door/uri1
            Log.Info(LOGTAG, "response.Representation.Attributes[DOOR_ATTRIBUTE]: " + response.Representation.Attributes[DOOR_ATTRIBUTE]); /// 4
        }
    }
    ```

<a name="scenario_5"></a>
## Observing Resources

To monitor the changes in a resource:

1.  On the server side, [register resources](#scenario_1) as observable and implement the `OnObserving()` method:

    ```
    public class DoorResource : Resource
    {
        public const string DoorUri = "/door/uri1";

        public DoorResource(string uri, ResourceTypes types, ResourceInterfaces interfaces, ResourcePolicy policy)
            : base(uri, types, interfaces, policy) {}

        protected override bool OnObserving(Request request, ObserveType type, int observeId)
        {
            return true;
        }
    }
    ```

2. On the client side, [find resources](#scenario_2) and retrieve the remote resource handle using an event handler registered for the `ResourceFound` event of the [Tizen.Network.IoTConnectivity.IoTConnectivityClientManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.IoTConnectivityClientManager.html) class.
3. On the client side, call the `StartObserving()` method of the [Tizen.Network.IoTConnectivity.RemoteResource](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.IoTConnectivity.RemoteResource.html) class. On the server side, your observing request is handled as adding a new observer.

    Now whenever a resource changes on the server side, the client receives the information through an event handler registered for the `ObserverNotified` event of the `Tizen.Network.IoTConnectivity.RemoteResource` class.

    ```
    if (outArgs != null)
    {
        string DOOR_ATTRIBUTE = "DOOR_ATTRIBUTE";

        ObserverNotifiedEventArgs eObserverArgs = null;

        observerNotifiedHandler = (sender, e) =>
        {
            Log.Info(LOGTAG, "ObserverNotified: Result:" + e.Result);
            eObserverArgs = e;
        };

        outArgs.Resource.ObserverNotified += observerNotifiedHandler;

        outArgs.Resource.StartObserving(ObservePolicy.IgnoreOutOfOrder);

        Log.Info(LOGTAG, "Value is:" + eObserverArgs.Representation.Attributes[DOOR_ATTRIBUTE]);
    }
    ```

4. When the client no longer needs to monitor the resource, deregister the event handler and stop observation with the `StopObserving()` method:

    ```
    outArgs.Resource.ObserverNotified -= observerNotifiedHandler;
    outArgs.Resource.StopObserving();
    ```



## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
