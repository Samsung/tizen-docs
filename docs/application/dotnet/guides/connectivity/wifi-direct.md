# Wi-Fi Direct®


Wi-Fi Direct® is a technology that allows you to find nearby Wi-Fi Direct devices and form a Wi-Fi Direct group to communicate over a peer-to-peer link without wireless access points (base stations) in the infrastructure mode. Wi-Fi Direct is a synonym for Wi-Fi P2P (Peer-to-Peer).

In a Wi-Fi Direct group, the group owner works as an access point in the Wi-Fi infrastructure mode and the other devices join the group as clients. A group can be created either by negotiation between 2 devices or in an autonomous mode by a single group owner device. In a negotiation-based group creation, 2 devices compete based on the group owner intent value and the higher intent device becomes a group owner, while the other device becomes a group client. In an autonomous group creation, a device becomes a group owner by itself without any group client.

A Wi-Fi Direct device can join an existing group by associating itself with the group owner, as long as the allowed number of clients is not exceeded.

The main features of the Tizen.Network.WiFiDirect namespace include:

-   Managing Wi-Fi Direct events

    You can register event handlers to [receive notifications](#managing_events) about device, discovery, and connection state changes related to Wi-Fi Direct operations.

-   Activating Wi-Fi Direct

    You can [activate a local Wi-Fi Direct device](#activate_wifi_direct) and [deactivate it](#deactivate_wifi_direct).

-   Getting the Wi-Fi Direct peer device information

    You can [discover Wi-Fi Direct peer devices](#discover_wifi_direct) and show Wi-Fi Direct peer device information.

-   Connecting to a specific Wi-Fi Direct peer device

    You can [connect to a specific Wi-Fi Direct device](#connect_specific_peer). When the connection is no longer needed, you can end it.

-   Managing Wi-Fi Direct groups

    You can [create a Wi-Fi Direct group](#managing_wifi_direct_groups) and manage the group.



> **Note**   
> You can test the Wi-Fi Direct functionality on a target device only. The emulator does not support this feature.



## Prerequisites

To enable your application to use the Wi-Fi Direct functionality:

1.  To use the [Tizen.Network.WiFiDirect](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFiDirect.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/wifidirect</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Network.WiFiDirect namespace, include it in your application:

    ```
    using Tizen.Network.WiFiDirect;
    ```

<a name="managing_events"></a>
## Managing Events

To manage events related to Wi-Fi Direct operations:

1.  Define event handlers:

    -   `EventHandlerDeviceStateChanged()` is triggered when the device state changes (Wi-Fi Direct is activated or deactivated on a local device).
    -   `EventHandlerDiscoveryStateChanged()` is triggered when the discovery state changes (for example, when discovery starts or stops, or a peer device is found).
    -   `EventHandlerConnectionStatusChanged()` is triggered when the Wi-Fi Direct connection state changes (for example, the device is disconnected from or connected to peer devices, or a group is created or destroyed).

    ```
    public static void EventHandlerDeviceStateChanged(object sender, EventArgs e)
    {
        Console.WriteLine("Device state: " + e.DeviceState);
    }
    public static void EventHandlerDiscoveryStateChanged(object sender, EventArgs e)
    {
        Console.WriteLine("Discovery state: " + e.DiscoveryState);
    }
    public static void EventHandlerConnectionStatusChanged(object sender, EventArgs e)
    {
        Console.WriteLine("WiFi Direct connection state: " + e.ConnectionState);
    }
    ```

2.  Register the event handlers for the `DeviceStateChanged`, `DiscoveryStateChanged`, and `ConnectionStatusChanged` events of the [Tizen.Network.WiFiDirect.WiFiDirectManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFiDirect.WiFiDirectManager.html) class:

    ```
    WiFiDirectManager.DeviceStateChanged += EventHandlerDeviceStateChanged;

    WiFiDirectManager.DiscoveryStateChanged += EventHandlerDiscoveryStateChanged;

    WiFiDirectManager.ConnectionStatusChanged += EventHandlerConnectionStatusChanged;
    ```

3.  When they are no longer needed, deregister the event handlers:

    ```
    WiFiDirectManager.DeviceStateChanged -= EventHandlerDeviceStateChanged;

    WiFiDirectManager.DiscoveryStateChanged -= EventHandlerDiscoveryStateChanged;

    WiFiDirectManager.ConnectionStatusChanged -= EventHandlerConnectionStatusChanged;
    ```

<a name="activate_wifi_direct"></a>
## Activating Wi-Fi Direct

To activate a Wi-Fi Direct local device and check the device state:

1.  Activate Wi-Fi Direct on the local device using the `Activate()` method of the [Tizen.Network.WiFiDirect.WiFiDirectManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFiDirect.WiFiDirectManager.html) class.

    ```
    try
    {
        WiFiDirectManager.Activate();
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

2.  Check the Wi-Fi Direct state.

    You can check the Wi-Fi Direct local device state using the `State` property of the `Tizen.Network.WiFiDirect.WiFiDirectManager` class. Since Wi-Fi Direct has just been activated on the device, the device state is `Activated`.

    ```
    try
    {
        if (WiFiDirectManager.State == Activated)
        {
            Console.WriteLine("Wi-Fi Direct is activated");
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="discover_wifi_direct"></a>
## Getting the Wi-Fi Direct Peer Device Information

To discover nearby Wi-Fi Direct peer devices and retrieve their details:

1.  Define an event handler that is triggered each time a peer device is found during discovery.

    In this example, the event handler displays the name and MAC address of each found peer device. You can also get other information, such as the connection state, device type, Wi-Fi display information, and WPS type.

    ```
    public static void EventHandlerPeerFound(object sender, EventArgs e)
    {
        Console.WriteLine("Discovery state: " + e.DiscoveryState);
        if (e.DiscoveryState == WiFiDirectDiscoveryState.Found && e.Peer != null)
        {
            Console.WriteLine("Peer device name: " + e.Peer.Name);
            Console.WriteLine("Peer mac address: " + e.Peer.MacAddress);
        }
    }
    ```

2.  Register the event handler for the `PeerFound` event and start the discovery:

    ```
    try
    {
        WiFiDirectManager.PeerFound += EventHandlerPeerFound;
        WiFiDirectManager.StartDiscovery(false, 30);
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

3.  When you have found all the peer devices you need, deregister the event handler:

    ```
    WiFiDirectManager.PeerFound -= EventHandlerPeerFound;
    ```

<a name="connect_specific_peer"></a>
## Connecting to a Specific Wi-Fi Direct Peer Device

To connect to a specific device:

1.  Start the discovery and retrieve the peer device you want to connect to:

    ```
    string peerName = "PeerDeviceName";
    public static void EventHandlerPeerFound(object sender, EventArgs e)
    {
        Console.WriteLine("Discovery state: " + e.DiscoveryState);
        if (e.DiscoveryState == WiFiDirectDiscoveryState.Found && e.Peer.Name == peerName)
        {
            Console.WriteLine("Peer device found");
            WiFiDirectPeer peer = e.Peer;
        }
    }

    try
    {
        WiFiDirectManager.PeerFound += EventHandlerPeerFound;
        WiFiDirectManager.StartDiscovery(false, 30);
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

2.  Connect to a peer device:
    1.  Define an event handler that is triggered each time the peer device connection state changes.

        In this example, the event handler displays the connection state and MAC address of the connected device:

        ```
        public static void EventHandlerConnectionStateChanged(object sender, EventArgs e)
        {
            Console.WriteLine("Connection state: " + e.State);
            if (e.Error == WiFiDirectError.None && e.State == ConnectionRsp)
            {
                Console.WriteLine("Connected device mac address: " + e.MacAddress);
            }
        }
        ```

    2.  Register the event handler for the `ConnectionStateChanged` event of the [Tizen.Network.WiFiDirect.WiFiDirectPeer](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFiDirect.WiFiDirectPeer.html) class and connect the peer with the local Wi-Fi Direct device using the `Connect()` method:

        ```
        try
        {
            peer.ConnectionStateChanged += EventHandlerConnectionStateChanged;
            peer.Connect();
        }
        catch (Exception e)
        {
            Console.WriteLine("Exception occurred" + e.ToString());
        }
        ```

3.  When the connection is no longer needed, disconnect the peer from the Wi-Fi Direct device and deregister the event handler:

    ```
    try
    {
        peer.Disconnect();
        peer.ConnectionStateChanged -= EventHandlerConnectionStateChanged;
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="managing_wifi_direct_groups"></a>
## Managing Wi-Fi Direct Groups

To create an autonomous Wi-Fi Direct group and to make your device the autonomous group owner:

1.  Create the group:
    1.  Define an event handler that is triggered each time the connection status changes.

        In this example, the event handler checks whether the group has been successfully created:

        ```
        public static void EventHandlerConnectionStatusChanged(object sender, EventArgs e)
        {
            Console.WriteLine("Connection state: " + e.State);
            if (e.Error == WiFiDirectError.None && e.State == GroupCreated)
            {
                Console.WriteLine("Group created successfully");
            }
            if (e.State == GroupDestroyed)
            {
                Console.WriteLine("Group destroyed successfully");
            }
        }
        ```

    2.  Register the event handler for the `ConnectionStatus` event of the `Tizen.Network.WiFiDirect.WiFiDirectManager` class, and create the group using the `CreateGroup()` method:

        ```
        try
        {
            WiFiDirectManager.ConnectionStatusChanged += EventHandlerConnectionStatusChanged;
            WiFiDirectManager.CreateGroup();
        }
        catch (Exception e)
        {
            Console.WriteLine("Exception occurred" + e.ToString());
        }
        ```

2.  When the group is no longer needed, destroy it and deregister the event handler:

    ```
    try
    {
        WiFiDirectManager.DestroyGroup();
        WiFiDirectManager.ConnectionStatusChanged -= EventHandlerConnectionStatusChanged;
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="deactivate_wifi_direct"></a>
## Deactivating Wi-Fi Direct

To deactivate Wi-Fi Direct when it is no longer needed (or the application is exiting):

1.  Deactivate Wi-Fi Direct on the local device using the `Deactivate()` method of the [Tizen.Network.WiFiDirect.WiFiDirectManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFiDirect.WiFiDirectManager.html) class:

    ```
    try
    {
        if (WiFiDirectManager.State == Activated)
        {
            WiFiDirectManger.Deactivate();
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

2.  Check the device state using the `State` property of the `Tizen.Network.WiFiDirect.WiFiDirectManager` class:

    ```
    try
    {
        if (WiFiDirectManager.State == Deactivated)
        {
            Console.WriteLine("Wi-Fi Direct is deactivated");
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
