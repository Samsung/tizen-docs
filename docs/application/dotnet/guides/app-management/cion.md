# Cion

The Cion API provides functionality to communicate with other devices.

The main features of the `Tizen.Applications.Cion` class includes the following:

-   Communicating with other applications in server-client style.

    You can communicate with other applications in [server-client](#server_client) style.

-   Communicating with other applications in group style.

    You can communicate with other applications in [group](#group) style.

And, you can also generate communication code using [TIDL](#tidl).

## Prerequisites

To enable your application to use the cion functionality, follow these steps:

1.  To use the [Tizen.Applications.Cion](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.html) class, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
       <privilege>http://tizen.org/privilege/d2d.datasharing</privilege>
       <privilege>http://tizen.org/privilege/internet</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Applications.Cion class, include it in your application:

    ```csharp
    using Tizen.Applications.Cion;
    ```

<a name="server_client"></a>
## Communicate in server-client style

The Cion client can try to discover the server to communicate. If the server is discovered, the client can try to connect to the server.
After the client connects to the server, it can send data and payload.

To communicate with the server, use the [Tizen.Applications.Cion.ClientBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.ClientBase.html) class as follows:

1. Create a client instance as follows:

    ```csharp
    public class CionClient : ClientBase
    {
        public event EventHandler ConnectionResultEvent;
        public event EventHandler DisconnectedEvent;
        public event EventHandler DiscoveredEvent;
        public event EventHandler PayloadReceivedEvent;

        public CionClient(string serviceName) : base(serviceName)
        {
        }

        public CionClient(string serviceName, SecurityInfo securityInfo) : base(serviceName, securityInfo)
        {
        }

        protected override void OnConnectionResult(PeerInfo peerInfo, ConnectionResult result)
        {
            ConnectionResultEventArgs eventArgs = new ConnectionResultEventArgs(peerInfo, result);
            ConnectionResultEvent?.Invoke(this, eventArgs);
        }

        protected override void OnDisconnected(PeerInfo peerInfo)
        {
            DisconnectedEventArgs eventArgs = new DisconnectedEventArgs(peerInfo);
            DisconnectedEvent?.Invoke(this, eventArgs);
        }

        protected override void OnDiscovered(PeerInfo peerInfo)
        {
            DiscoveredEventArgs eventArgs = new DiscoveredEventArgs(peerInfo);
            DiscoveredEvent?.Invoke(this, eventArgs);
        }

        protected override void OnPayloadReceived(Payload payload, PayloadTransferStatus status)
        {
            PayloadReceivedEventArgs eventArgs = new PayloadReceivedEventArgs(payload, status);
            PayloadReceivedEvent?.Invoke(this, eventArgs);
        }

        public class ConnectionResultEventArgs : EventArgs
        {
            public ConnectionResultEventArgs(PeerInfo peerInfo, ConnectionResult result)
            {
                PeerInfo = peerInfo;
                Result = result;
            }
            public PeerInfo PeerInfo { get; }
            public ConnectionResult Result { get; }
        }

        public class DisconnectedEventArgs : EventArgs
        {
            public DisconnectedEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class DiscoveredEventArgs : EventArgs
        {
            public DiscoveredEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class PayloadReceivedEventArgs : EventArgs
        {
            public PayloadReceivedEventArgs(Payload payload, PayloadTransferStatus status)
            {
                Payload = payload;
                Status = status;
            }
            public Payload Payload { get; }
            public PayloadTransferStatus Status { get; }
        }
    }
    ```
    ```csharp
    string serviceName = "TestService";
    var client = new CionClient(serviceName);
    ```
    

2. Discover the server to connect; If the server is discovered, connect to it:

    ```csharp
    client.TryDiscovery();

    client.DiscoveredEvent += (sender, e) =>
    {
        CionClient.DiscoveredEventArgs eventArgs = e as CionClient.DiscoveredEventArgs;
        client.Connect(eventArgs.PeerInfo);
    };
    ```

3. Send data and payload:

    ```csharp
    string TestMessage = "Test Message";

    client.SendData(Encoding.UTF8.GetBytes(TestMessage), 5000);
    ```
    ```csharp
    string TestMessage = "Test Message";
    DataPayload dataPayload = new DataPayload(Encoding.UTF8.GetBytes(TestMessage));

    PayloadAsyncResult result = await client.SendPayloadAsync(dataPayload);
    ```

The Cion server can listen to the request from the client; If a connection request comes from the client, the server can accept it.
After the connection is accepted, the server can receive data and payload.

To communicate with the client, use the [Tizen.Applications.Cion.ServerBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.ServerBase.html) class as follows:

1. Create a server instance as follows:

    ```csharp
    public class CionServer : ServerBase
    {
        public event EventHandler ConnectionResultEvent;
        public event EventHandler ConnectionRequestEvent;
        public event EventHandler DataReceivedEvent;
        public event EventHandler DisconnectedEvent;
        public event EventHandler PayloadReceivedEvent;

        public static string ReplyMessage = "Reply Message";

        public CionServer(string serviceName, string displayName) : base(serviceName, displayName)
        {
        }

        public CionServer(string serviceName, string displayName, SecurityInfo securityInfo) : base(serviceName, displayName, securityInfo)
        {
        }

        protected override void OnConnectionResult(PeerInfo peerInfo, ConnectionResult result)
        {
            ConnectionResultEventArgs eventArgs = new ConnectionResultEventArgs(result);
            ConnectionResultEvent?.Invoke(this, eventArgs);
        }

        protected override void OnConnectionRequest(PeerInfo peerInfo)
        {
            ConnectionRequestEventArgs eventArgs = new ConnectionRequestEventArgs(peerInfo);
            ConnectionRequestEvent?.Invoke(this, eventArgs);
        }

        protected override byte[] OnDataReceived(byte[] data, PeerInfo peerInfo)
        {
            DataReceivedEventArgs eventArgs = new DataReceivedEventArgs(data, peerInfo);
            DataReceivedEvent?.Invoke(this, eventArgs);
            eventArgs.ReplyData = Encoding.UTF8.GetBytes(CionServer.ReplyMessage);
            return eventArgs.ReplyData;
        }

        protected override void OnDisconnected(PeerInfo peerInfo)
        {
            DisconnectedEventArgs eventArgs = new DisconnectedEventArgs(peerInfo);
            DisconnectedEvent?.Invoke(this, eventArgs);
        }

        protected override void OnPayloadReceived(Payload data, PeerInfo peerInfo, PayloadTransferStatus status)
        {
            PayloadReceivedEventArgs eventArgs = new PayloadReceivedEventArgs(data, peerInfo, status);
            PayloadReceivedEvent?.Invoke(this, eventArgs);
        }

        public class ConnectionResultEventArgs : EventArgs
        {
            public ConnectionResultEventArgs(ConnectionResult result)
            {
                Result = result;
            }
            public ConnectionResult Result { get; }
        }

        public class ConnectionRequestEventArgs : EventArgs
        {
            public ConnectionRequestEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class DataReceivedEventArgs : EventArgs
        {
            public DataReceivedEventArgs(byte[] data, PeerInfo peerInfo)
            {
                Data = data;
                PeerInfo = peerInfo;
            }
            public byte[] Data { get; }
            public PeerInfo PeerInfo { get; }
            public byte[] ReplyData { get; set; }
        }

        public class DisconnectedEventArgs : EventArgs
        {
            public DisconnectedEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class PayloadReceivedEventArgs : EventArgs
        {
            public PayloadReceivedEventArgs(Payload payload, PeerInfo peerInfo, PayloadTransferStatus status)
            {
                Payload = payload;
                PeerInfo = peerInfo;
                Status = status;
            }
            public Payload Payload { get; }
            public PeerInfo PeerInfo { get; }
            public PayloadTransferStatus Status { get; }
        }
    }
    ```
    ```csharp
    string serviceName = "TestService";
    string displayName = "TestDisplayName";
    var server = new CionServer(serviceName, displayName);
    ```

2. The server starts to listen to the requests from the client:

    ```csharp
    server.Listen();
    ```

3. Accept the connection:

    ```csharp
    server.ConnectionRequestEvent += (sender, e) =>
    {
        ClionServer.ConnectionRequestEventArgs eventArgs = e as CionServer.ConnectionRequestEventArgs;
        server.Accept(eventArgs.PeerInfo);
    };
    ```

4. Receive data and payload:

    ```csharp
    server.DataReceivedEvent += (sender, e) =>
    {
        CionServer.DataReceivedEventArgs eventArgs = e as CionServer.DataReceivedEventArgs;
        // eventArgs.Data
    };
    ```
    ```csharp
    server.PayloadReceivedEvent += (sender, e) =>
    {
        CionServer.PayloadReceivedEventArgs eventArgs = e as CionServer.PayloadReceivedEventArgs;
        // eventArgs.Payload
    };
    ```

<a name="group"></a>
## Communicate in group style

The Cion group is used to share data with other group members. The group members can subscribe to the topic to join the group.
If the data is published, subscribed members receive it.

To communicate with other group members, use the [Tizen.Applications.Cion.GroupBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.GroupBase.html) class as follows:

1. Create a group instance as follows:

    ```csharp
    public class CionGroup : GroupBase
    {
        public event EventHandler JoinedEvent;
        public event EventHandler LeftEvent;
        public event EventHandler PayloadReceivedEvent;

        public CionGroup(string serviceName) : base(serviceName)
        {
        }

        public CionGroup(string serviceName, SecurityInfo securityInfo) : base(serviceName, securityInfo)
        {
        }

        protected override void OnJoined(PeerInfo peerInfo)
        {
            JoinedEventArgs eventArgs = new JoinedEventArgs(peerInfo);
            JoinedEvent?.Invoke(this, eventArgs);
        }

        protected override void OnLeft(PeerInfo peerInfo)
        {
            LeftEventArgs eventArgs = new LeftEventArgs(peerInfo);
            LeftEvent?.Invoke(this, eventArgs);
        }

        protected override void OnPayloadReceived(Payload payload, PeerInfo peer)
        {
            PayloadReceivedEventArgs eventArgs = new PayloadReceivedEventArgs(payload, peer);
            PayloadReceivedEvent?.Invoke(this, eventArgs);
        }

        public class JoinedEventArgs : EventArgs
        {
            public JoinedEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class LeftEventArgs : EventArgs
        {
            public LeftEventArgs(PeerInfo peerInfo)
            {
                PeerInfo = peerInfo;
            }
            public PeerInfo PeerInfo { get; }
        }

        public class PayloadReceivedEventArgs : EventArgs
        {
            public PayloadReceivedEventArgs(Payload payload, PeerInfo peerInfo)
            {
                Payload = payload;
                PeerInfo = peerInfo;
            }
            public Payload Payload { get; }
            public PeerInfo PeerInfo { get; }
        }
    }
    ```
    ```csharp
    string topic = "TestGroup";
    CionGroup group = new CionGroup(topic);
    ```

2. Subscribe topic:

    ```csharp
    group.Subscribe();
    ```

3. Publish data:

    ```csharp
    string testData = "PublishData";
    DataPayload payload = new DataPayload(Encoding.UTF8.GetBytes(testData));
    group.Publish(payload);
    ```

4. Receive the payload:

    ```csharp
    group.PayloadReceivedEvent += (sender, eventArgs) =>
    {
        CionGroup.PayloadReceivedEvent eventArgs = e as CionGroup.PayloadReceivedEvent;
        // eventArgs.Payload
    };
    ```

<a name="tidl"></a>
## TIDL support

Cion communication code can be generated using TIDL.

You can create `CionTest.tidl` file as follows:

```csharp
interface FileSample {
    int ShareFile(file myFile);
    int ShareFilesList(list<file> myFile);
    int ShareFilesArray(array<file> myFile);
}
```

You can compile tidl file to generate cion code as follows:
```
tidlc --cion -p -b -i CionTest.tidl -l C# -o CionProxy
tidlc --cion -s -b -i CionTest.tidl -l C# -o CionStub
```


## Related information
- Dependencies
  -   Tizen 6.5 and Higher
- API Reference
  - [Tizen.Applications.Cion](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion) namespace
  - [Tizen.Applications.Cion.ClientBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.ClientBase) class
  - [Tizen.Applications.Cion.ServerBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.ServerBase) class
  - [Tizen.Applications.Cion.GroupBase](/application/dotnet/api/TizenFX/latest/api/Tizen.Applications.Cion.GroupBase) class
