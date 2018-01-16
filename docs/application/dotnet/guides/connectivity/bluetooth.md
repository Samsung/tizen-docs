# Bluetooth

You can use Bluetooth functionalities in your application to, for example, manage the local Bluetooth adapter, and bond with and exchange data between Bluetooth-enabled devices. The Bluetooth standard provides a peer-to-peer (P2P) data exchange functionality over short distance between compliant devices.

**Figure: Bluetooth connections**

![Bluetooth connections](./media/bluetooth_device_discovering.png)

The main features of the Tizen.Network.Bluetooth namespace include:

-   Managing the local Bluetooth adapter

    The [Tizen.Network.Bluetooth.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class provides methods for setting up Bluetooth and discovering other devices. The class is used to control the Bluetooth adapter: you must [enable the adapter](#enable) before any other Bluetooth actions, and when you no longer need it, disable it to save device power. You can [check and monitor the adapter state](#state).

    You can [control the visibility of the device](#visibility_control), meaning whether its name appears to others searching for Bluetooth devices. In addition, you can discover neighboring Bluetooth devices. This process is asynchronous, so you must build and hold the list of devices in the neighborhood.

-   Discovering devices

    The [Tizen.Network.Bluetooth.BluetoothDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothDevice.html) class provides methods for managing bonds with other devices and searching for supported services. The class is used to handle the connection with other devices and to search for services available on remote devices.

    You can [discover other Bluetooth devices](#find). The device discovery process can retrieve multiple types of Bluetooth devices, such as printers, mobile phones, and headphones.

-   Creating a bond with a Bluetooth device

    You can create a bond with another device with the `Tizen.Network.Bluetooth.BluetoothDevice` class. Bonding allows the 2 devices to establish a connection.

    Connected devices exchange keys needed for encrypted communication, but each connection has to be approved by the latest application user. You can also set authorization of other devices. Authorized devices are connected automatically without the latest user being asked for authorization.

-   Connecting to and exchanging data with a Bluetooth device using a Bluetooth socket

    The `Tizen.Network.Bluetooth.BluetoothAdapter` class provides methods for managing connections to other devices and exchanging data. The class is used for exchanging data between 2 Bluetooth devices, where your device can have the role both of a server (service provider) and client (service user). The connection creation process depends on the role. After the connection is established, the processes for exchanging data and disconnecting are the same for both roles.

    When you attempt to open a connection to another device, a Service Discovery Protocol (SDP) look-up is performed on the device, and the protocol and channel to be used for the connection are determined. If a connection is established and the socket is opened successfully, the `Connected` value of the [Tizen.Network.Bluetooth.BluetoothSocketState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothSocketState.html) enumerator is returned in the `ConnectionStateChanged` event of the [Tizen.Network.Bluetooth.IBluetoothClientSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothClientSocket.html) interface. The socket is subsequently used for exchanging data between the connected devices.

    You can use Serial Port Profile (SPP) operations to [connect to other devices](#connect), [exchange data](#exchange), and [disconnect from connected devices](#disconnect).

-   Connecting to audio devices with Bluetooth

    Connect to Bluetooth audio devices, such as headsets, hands-free devices, and headphones, using the [Tizen.Network.Bluetooth.BluetoothAudio](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAudio.html) class.

-   Handling attributes with Bluetooth GATT

    The Bluetooth GATT-related classes, such as [Tizen.Network.Bluetooth.BluetoothGattClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothGattClient.html), provide methods for creating and destroying the GATT client handle, discovering, reading, and modifying attributes, and setting and releasing callbacks to be notified when characteristic values are changed at the remote device.

    As a client, you can connect to and use a specific service on the server device. Once the connection is established, the client can manage the service attributes. When the GATT client operations are no longer required, deregister the callbacks and destroy the GATT client handle.

    You can use GATT operations to [handle preconditions](#pre_gatt), [manage client operations](#gatt), [manage getter operations](#gatt_getter), and [manage setter operations](#gatt_setter).

-   Connecting to devices with Bluetooth HID

    Connect to a Bluetooth HID, such as a keyboard or mouse, using the [Tizen.Network.Bluetooth.BluetoothHid](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothHid.html) class.

-   Exchanging data with Bluetooth LE

    The [Tizen.Network.Bluetooth.BluetoothLeDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeDevice.html) class provides methods for managing the Bluetooth Low Energy (BLE) connections with other BLE devices and exchanging data between them.

    You can control the visibility of the BLE device, meaning whether its name appears to others searching for BLE devices. In addition, you can discover neighboring BLE devices through scanning. This process is asynchronous, so you must build and hold the list of devices in the neighborhood.

    You can use LE operations to [manage scans](#le_scan), [add advertising data](#add_adv_data), [set the advertising connectable mode](#set_adv_conn), [set the advertising mode](#set_adv_mode), and [start and stop advertising](#start_adv).

-   Controlling remote audio and video devices with Bluetooth AVRCP

    The [Tizen.Network.Bluetooth.BluetoothAvrcp](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAvrcp.html) class provides methods for remotely controlling audio and video devices.

    Bluetooth AVRCP is used with the Advanced Audio Distribution Profile (A2DP). Through AVRCP, you can handle remote controls (such as [PlayerState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.PlayerState.html), [EqualizerState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.EqualizerState.html), [RepeatMode](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.RepeatMode.html), [ShuffleMode](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.ShuffleMode.html), and [ScanMode](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.ScanMode.html)).

    You can [receive notifications of Bluetooth AVRCP events](#avrcp).

Remember to [release all resources](#release) when you are done.

Bluetooth use is based on profiles. Tizen Bluetooth features support the Audio, GATT, and HID profiles.


> **Note**   
> You can test the Bluetooth functionality on a target device only. The emulator does not support this feature.


## Prerequisites

To enable your application to use the Bluetooth functionality:

1.  To use the [Tizen.Network.Bluetooth](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.html) namespace, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/bluetooth</privilege>
    </privileges>
    ```

2.  To use the methods and properties of the Tizen.Network.Bluetooth namespace, include it in your application:

    ```
    using Tizen.Network.Bluetooth;
    ```
<a name="enable"></a>
## Enabling and Disabling Bluetooth

To allow the user to enable or disable Bluetooth, use the application control to display the Bluetooth activation settings.

The [Tizen.Network.Bluetooth](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.html) namespace does not contain methods for enabling or disabling Bluetooth directly. You must display the Bluetooth activation settings application to allow the user to toggle the Bluetooth state.

**Figure: Bluetooth activation settings application (off screen on the left and on screen on the right)**

![Bluetooth activation settings application (off screen on the left and on screen on the right)](./media/bluetooth_onoff.png)

```
using Tizen.Applications;

public static bt_onoff_operation(void)
{
    /// Launch the Bluetooth activation settings to allow the user to enable Bluetooth
    AppControl myAppControl = new AppControl();
    myAppControl.Operation = AppControlOperations.SettingBluetoothEnable;
    AppControl.SendLaunchRequest(myAppControl);
}
```
<a name="state"></a>
## Checking the Bluetooth Adapter State

To check the Bluetooth adapter state and monitor adapter state changes:

1.  Check whether the Bluetooth adapter is enabled on your device by using the `IsBluetoothEnabled` property of the [Tizen.Network.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class:

    ```
    public class BluetoothAdapterTests
    {
        static bool isEnabled = false;
        isEnabled = BluetoothAdapter.IsBluetoothEnabled;
        if (!isEnabled)
        {
            Assert.Fail("Bluetooth is not enabled");

            return;
        }
    ```

2.  To monitor changes in the Bluetooth adapter state, define an event handler and register it for the `StateChanged` event of the `Tizen.Network.BluetoothAdapter` class:

    ```
        public static void EventHandlerStateChanged(object sender, StateChangedEventArgs e)
        {
            Assert.IsTrue((int)e.Result == 0, "StateChanged event is not working properly");
        }

        BluetoothAdapter.StateChanged += EventHandlerStateChanged;
    }
    ```
<a name="find"></a>
## Finding Other Devices

To find remote Bluetooth devices, you can either discover them and bond with them, or you can query the list of previously bonded devices:

-   Discover and bond with new devices:
    1.  Define a discovery state change event handler to manage the discovery process.

        The properties of the [Tizen.Network.Bluetooth.DiscoveryStateChangedEventArgs](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.DiscoveryStateChangedEventArgs.html) class instance passed to the event handler contain information on the state of the discovery process and any devices discovered:

        -   The `Result` property contains the result of the Bluetooth discovery process as a value of the [Tizen.Network.Bluetooth.BluetoothError](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothError.html) enumeration. If discovery has been successful, the parameter value is `BluetoothError.None`. If the discovery failed to start due to an error, the parameter value is `BluetoothError.TimedOut`.
        -   The `DiscoveryState` property contains the current state of the discovery process as a value of the [Tizen.Network.Bluetooth.BluetoothDeviceDiscoveryState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothDeviceDiscoveryState.html) enumeration:
            -   When you start the discovery process, the event is triggered with the `BluetoothDeviceDiscoveryState.Started` state.

                Similarly, when you stop the discovery process, the event is triggered with the `BluetoothDeviceDiscoveryState.Finished` state.

            -   Each time a remote Bluetooth device is found, the event is triggered with the `BluetoothDeviceDiscoveryState.Found` state.

                In this state, you can get some information about the discovered device, such as the device MAC address, name, class, RSSI (received signal strength indicator), and bonding state. Using this information, you can bond with the discovered device.

        -   The `DeviceFound` property contains the discovered Bluetooth device, as an instance of the [Tizen.Network.Bluetooth.BluetoothDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothDevice.html) class.

        ```
        public class DiscoveryCallbackTests
        {
            static bool _flagStarted = false;
            static bool _flagDiscovery = false;
            static bool _flagDiscoveryFinished = false;
            static BluetoothError _result;
            static BluetoothDevice _device = null;
            static BluetoothDeviceDiscoveryState _state;
            public static BluetoothError result;

            public static void EventHandlerDiscoveryChanged(object sender, DiscoveryStateChangedEventArgs e)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "e.DiscoveryState :" + e.DiscoveryState);
                _state = e.DiscoveryState;
                if (_state == BluetoothDeviceDiscoveryState.Started)
                {
                    _flagStarted = true;
                }
                if (_state == BluetoothDeviceDiscoveryState.Found)
                {
                    _result = e.Result;
                    _device = e.DeviceFound;
                    _flagDiscovery = true;
                }
                if (_state == BluetoothDeviceDiscoveryState.Finished)
                {
                    _flagDiscoveryFinished = true;
                }
            }
        }
        ```

    2.  Register the event handler with the `DiscoveryStateChanged` event of the [Tizen.Network.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class, and start the discovery process with the `StartDiscovery()` method:

        ```
        BluetoothAdapter.DiscoveryStateChanged += EventHandlerDiscoveryChanged;
        if (_device)
        {
            BluetoothAdapter.StartDiscovery();
            await WaitStartedFlag();
            await WaitDiscoveryFlag();
        ```

        You can discover a nearby remote Bluetooth device, if the remote device Bluetooth is enabled and in a discovery mode.

        To stop the device discovery, call the `BluetoothAdapter.StopDiscovery()` method.

        ```
            BluetoothAdapter.StopDiscovery();
            await WaitFinishedFlag();
        }
        BluetoothAdapter.DiscoveryStateChanged -= EventHandlerDiscoveryChanged;
        ```

    3.  To bond with a discovered remote device, use the `CreateBond()` method of the [Tizen.Network.Bluetooth.BluetoothDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothDevice.html) class. To cancel bonding, call the `CancelBonding()` method.

        To get notified when the bonding process has finished, define a bond created event handler and register it for the `BondCreated` event of the `Tizen.Network.Bluetooth.BluetoothDevice` class.

        ```
        if (device)
        {
            device.BondCreated += EventHandlerBondCreated;
            device.CreateBond();
        }
        ```

        In the bond created event handler, you can get the service UUID and the list of services provided by the remote Bluetooth device:

        ```
        static bool flagDeviceDiscovery = false;
        static BluetoothDevice device = null;
        public static void EventHandlerBondCreated(object sender, BondCreatedEventArgs e)
        {
            if (e.Result == 0 && e.Device != null)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "EventHandlerBondCreated Bond Created");
            }
            Assert.IsNotNull(device.Address, "Bonded device address is not null");
            Assert.IsNotNull(device.Name, "Bonded device name is not null");
            Assert.IsInstanceOf<int>(device.Rssi);
            foreach (string uuid in device.ServiceUuidList)
            {
                Assert.IsInstanceOf<string>(uuid);
                Assert.IsNotNull(uuid, "Uuid should not be null");
            }
            BluetoothClass btClass = device.Class;
            Assert.IsInstanceOf<BluetoothMajorDeviceClassType>(btClass.MajorDeviceClassType);
            Assert.IsInstanceOf<BluetoothMinorDeviceClassType>(btClass.MinorDeviceClassType);
            Assert.IsInstanceOf<int>(btClass.MajorServiceClassMask);
            Assert.IsInstanceOf<int>(device.ServiceCount);
            Assert.IsInstanceOf<int>(device.ManufacturerDataLength);
            Assert.IsInstanceOf<bool>(device.IsAuthorized);
            Assert.IsInstanceOf<bool>(device.IsPaired);
            Assert.IsInstanceOf<bool>(device.IsConnected);
            device.BondCreated -= EventHandlerBondCreated;
        }
        ```

        After you have successfully bonded with a remote device, it is included in the bonded device list. When you want to connect to that device again in the future, you do not need to discover it again. Instead, you can simply query the bonded device list to receive the information (such as address and name) you need to connect to the device. You can also query the bonded device list to verify that bonding was successful.

-   Query the bonded device list.

    To query the list of previously bonded devices, use the `GetBondedDevices()` method of the `Tizen.Network.Bluetooth.BluetoothAdapter` class. The method lists all the bonded devices, and accessing the properties of each bonded device object gives more information (such as device name, MAC address, and service list) that you need to connect to the device.

    ```
    public static void BondedDeviceTest(BluetoothDevice item)
    {
        if (item.Address != null && item.Name != null && item.IsPaired && item.ServiceUuidList != null)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "[BondedDeviceTest] " + "item.Address " + "item.Name");
        }
    }

    /// Get the bonded device list
    try
    {
        IEnumerable<BluetoothDevice> list = BluetoothAdapter.GetBondedDevices();
        if (!list.Any())
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "No bonded devices are found.");
        }
        else
        {
            foreach (BluetoothDevice item in list)
            {
                /// Logic to process the device information
                BondedDeviceTest(item);
            }
        }
    }
    catch (Exception e)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "BluetoothAdapter.GetBondedDevices should not throw exception " + e.ToString());
    }
    ```

    To remove a device from the bonded list, call the `DestroyBond()` method of the `Tizen.Network.Bluetooth.BluetoothDevice` class.


> **Note**   
> A Bluetooth device must be in a discovery mode (visible) for other devices to find it and connect to it. If you want other devices to find your device, you must set the device to be visible.


To manage the device visibility and enable discovery:

1.  Check the current visibility of your device:

    ```
    /// Visibility mode of the Bluetooth device
    VisibilityMode mode = BluetoothAdapter.Visibility;

    public static void EventHandlerVisibilityDurationChanged(object sender, VisibilityDurationChangedEventArgs e)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Duration value: " + e.Duration);
    }

    if (mode == VisibilityMode.NonDiscoverable)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is not discoverable.");
    }
    else if (mode == VisibilityMode.Discoverable)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is discoverable. No time limit.");
    }
    else
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is discoverable for a set period of time.");
    }

    BluetoothAdapter.VisibilityDurationChanged += EventHandlerVisibilityDurationChanged;
    ```

2.  To allow the user to change the visibility mode of the device, use the application control to display the Bluetooth visibility setting application.

    The [Tizen.Network.Bluetooth](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.html) namespace does not contain methods for changing the visibility. You must display the Bluetooth visibility setting application to allow the user to toggle the visibility state.

    ![Bluetooth visibility setting application](./media/bluetooth_visibility.png)

    ```
    using Tizen.Applications;

    public static bt_set_visibility_operation(void)
    {
        /// Launch the Bluetooth visibility settings to allow the user to toggle visibility
        AppControl myAppControl = new AppControl();
        myAppControl.Operation = AppControlOperations.SettingBluetoothVisibility;
        AppControl.SendLaunchRequest(myAppControl);
    }
    ```

3.  To get notifications when the visibility mode and duration change, define and register event handlers for the `VisibilityModeChanged` and `VisibilityDurationChanged` events of the `Tizen.Network.Bluetooth.BluetoothAdapter` class:

    ```
    public static void EventHandlerVisibilityDurationChanged(object sender, VisibilityDurationChangedEventArgs e)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Duration value: " + e.Duration);
    }

    public static void EventHandlerVisibilityModeChanged(object sender, VisibilityModeChangedEventArgs e)
    {
        if (mode == VisibilityMode.NonDiscoverable)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is not discoverable.");
        }
        else if (mode == VisibilityMode.Discoverable)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is discoverable. No time limit.");
        }
        else
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "The device is discoverable for a set period of time.");
        }
    }

    BluetoothAdapter.VisibilityDurationChanged += EventHandlerVisibilityDurationChanged;
    BluetoothAdapter.VisibilityModeChanged += EventHandlerVisibilityModeChanged;
    ```
<a name="connect"></a>
## Connecting to Other Devices Using SPP

To connect to other devices:

-   Connect as a server:
    1.  To establish a connection with your device acting as a server, create an RFCOMM Bluetooth socket using the `CreateServerSocket()` method of the [Tizen.Network.Bluetooth.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class, with the UUID of the service as a parameter. The UUID uniquely identifies which service to provide, and it must match with the UUID of the client's incoming connection in order to be accepted.

        The socket is created as an instance of the [Tizen.Network.Bluetooth.BluetoothServerSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothServerSocket.html) class.

        ```
        private static bool flagCreateSocketDone = false;
        public static BluetoothServerSocket Server = null;
        public static string ServiceUuid = "00001101-0000-1000-8000-00805F9B7777";

        public static void CreateServerSocketUtil()
        {
            if (Server == null && flagCreateSocketDone == false)
            {
                Server = BluetoothAdapter.CreateServerSocket(ServiceUuid);
                flagCreateSocketDone = true;
            }
        }
        ```

    2.  To listen for an incoming connection from a client, call the `Listen()` method of the `Tizen.Network.Bluetooth.BluetoothServerSocket` class and define and register an event handler for the `AcceptStateChanged` event.

        ```
        public static IBluetoothServerSocket Socket = null;
        public static SocketConnection AcceptConnection = null;
        public static BluetoothError AcceptResult;
        public static BluetoothSocketState AcceptState;

        public static void AcceptStateChangedEventHandler(object sender, AcceptStateChangedEventArgs args)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "AcceptStateChangedCallback state: " + args.State);
            Socket = args.Server;
            AcceptConnection = args.Connection;
            AcceptResult = args.Result;
            AcceptState = args.State;
            FlagAcceptStateChanged = true;
        }

        Server.AcceptStateChanged += AcceptStateChangedEventHandler;
        Server.Listen();
        /// Wait for the accept flag to be set
        await WaitAcceptFlag();
        Server.AcceptStateChanged -= AcceptStateChangedEventHandler;
        if (FlagAcceptStateChanged)
        {
            flagAcceptSocketDone = true;
        }
        ```

    3.  When you no longer want to accept any other connections or provide a service, destroy the server socket with the `DestroyServerSocket()` method of the `Tizen.Network.Bluetooth.BluetoothAdapter` class.

-   Connect as a client:
    1.  Define a socket connection state change event handler and register it for the `ConnectionStateChanged` event of the [Tizen.Network.Bluetooth.IBluetoothClientSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothClientSocket.html) interface. The event triggers whenever the connection state changes (for example, when a client connects to a service on the server).

        The event handler receives the result of the connection state change as a value of the [Tizen.Network.Bluetooth.BluetoothError](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothError.html) enumeration, the new connection state as a value of the [Tizen.Network.Bluetooth.BluetoothSocketState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothSocketState.html) enumeration, and an instance of the [Tizen.Network.Bluetooth.SocketConnection](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.SocketConnection.html) class that specifies connection details, including the client device MAC address.

        ```
        public static void ConnectionStateChangedEventHandler(object sender, SocketConnectionStateChangedEventArgs args)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "ConnectionStateChanged callback in client " + args.State);
            ClientState = args.State;
            ClientConnection = args.Connection;
            ClientResult = args.Result;

            if (args.State == BluetoothSocketState.Connected)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Connected.");
                if (ClientConnection != NULL)
                {
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Socket of connection -" + ClientConnection.SocketFd);
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Address of connection -" + ClientConnection.Address);
                }
                else
                {
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: No connection data");
                }
            }
            else
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Disconnected.");
                if (ClientConnection != NULL)
                {
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Socket of disconnection -" + ClientConnection.SocketFd);
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: Address of disconnection -" + ClientConnection.Address);
                }
                else
                {
                    LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Callback: No connection data");
                }
            }
        }

        /// Once the server is listening for incoming connection, register for connection callback
        Client.ConnectionStateChanged += ConnectionStateChangedEventHandler;
        ```



        > **Note**   
		> When you connect to a Bluetooth server device, retrieve the server socket file descriptor (the `SocketFd` property of the `Tizen.Network.Bluetooth.SocketConnection` class instance) in the callback and store it for later use. You need the file descriptor when sending data or disconnecting from the service.



    2.  To request a connection to the Bluetooth server, first discover the server, and then create a socket using the `CreateSocket()` method of the [Tizen.Network.Bluetooth.BluetoothDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothDevice.html) class, using the UUID of the RFCOMM-based service as a parameter. This UUID must match the UUID used by the server when it created the server socket using the `CreateServerSocket()` method of the [Tizen.Network.Bluetooth.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class.

        ```
        const char *service_uuid="00001101-0000-1000-8000-00805F9B34FB";
        public static bool FlagDeviceFound = false;

        /// From discovered device, create the client socket
        public static void DiscoveryStateChangedEventHandler(object sender, DiscoveryStateChangedEventArgs args)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "DiscoveryStateChanged callback " + args.DiscoveryState);
            if (args.DiscoveryState == BluetoothDeviceDiscoveryState.Found)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "DiscoveryStateChanged callback device found: " + args.DeviceFound.Name);
                Client = args.DeviceFound.CreateSocket(ServiceUuid);
                FlagDeviceFound = true;
            }
        }

        public static async Task WaitDiscoveryFlag()
        {
            int count = 0;
            while(true)
            {
                await Task.Delay(2000);
                count++;
                if (FlagDeviceFound)
                {
                    break;
                }
                if (count == 15)
                {
                    break;
                }
            }
        }

        /// Discover the remote device
        BluetoothAdapter.DiscoveryStateChanged += DiscoveryStateChangedEventHandler;
        BluetoothAdapter.StartDiscovery();
        await WaitDiscoveryFlag();
        BluetoothAdapter.DiscoveryStateChanged -= DiscoveryStateChangedEventHandler;
        if (FlagDeviceFound)
        {
            flagCreateClientDone = true;
        }

        Client.ConnectionStateChanged += ConnectionStateChangedEventHandler;
        ```

        When the socket has been created, connect to the server with the `Connect()` method of the [Tizen.Network.Bluetooth.IBluetoothClientSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothClientSocket.html) interface:

        ```
        Client.Connect();
        ```
<a name="exchange"></a>
## Exchanging Data Using SPP

To share data between devices after establishing a connection:

1.  To write data, use the `SendData()` method of the [Tizen.Network.Bluetooth.IBluetoothClientSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothClientSocket.html) interface, which accepts the data as a string parameter:

    ```
    private static string dataFromClient = "Test from client";
    /// The client is created after successful socket connection with server device
    Client.SendData(dataFromClient);
    ```

2.  To read data from other devices, you must define the data received event handler, which is invoked when your device receives data from other Bluetooth devices.

    Register the event handler for the `DataReceived` event of the [Tizen.Network.Bluetooth.IBluetoothServerSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothServerSocket.html) interface.

    The received data is passed to the event handler as an instance of the [Tizen.Network.Bluetooth.SocketData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.SocketData.html) class, which contains the socket file descriptor, the size of the received data in bytes, and the data itself as a string.

    ```
    public static IBluetoothServerSocket Socket = null;

    public static void DataReceivedServerEventHandler(object sender, SocketDataReceivedEventArgs args)
    {
        BluetoothSetup.Data = args.Data;
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "DataReceived in client: " + args.Data.Data);
        flagServerDataReceived = true;
    }
    /// The socket is created on the server device, after the socket connection is accepted from the client device
    Socket.DataReceived += DataReceivedServerEventHandler;
    ```
<a name="disconnect"></a>
## Disconnecting from the Connected Device Using SPP

To disconnect from a device:

-   If your device is a Bluetooth server, disconnect from the client with the `DestroyServerSocket()` method of the [Tizen.Network.Bluetooth.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class:

    ```
    if (Server != null)
    {
        BluetoothAdapter.DestroyServerSocket(Server);
    }
    ```

-   If your device is a Bluetooth client, disconnect from the server with the `Disconnect()` method of the [Tizen.Network.Bluetooth.IBluetoothClientSocket](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.IBluetoothClientSocket.html) interface:

    ```
    if (flagDisconnectSocketDone == false)
    {
        Client.Disconnect();
    }
    ```
<a name="pre_gatt"></a>
## Handling GATT Operation Preconditions

Before you can use the Bluetooth GATT functionalities, you must successfully connect to the BLE target.

Find the target device and connect to it with the `GattConnect()` method of the [Tizen.Network.Bluetooth.BluetoothLeDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeDevice.html) class:

```
public static BluetoothLeDevice leDevice = null;
public static BluetoothGattClient client = null;

/// For more information on scanning for BLE devices, see Managing Bluetooth LE Scans
BluetoothAdapter.ScanResultChanged += scanResultEventHandler;
if (leDevice == null)
{
    BluetoothAdapter.StartLeScan();
    /// Wait while the system searches for the LE target you want to connect to
    /// If you find the LE target you want, stop the scan
    await WaitScanFlag();

    BluetoothAdapter.StopLeScan();
    await Task.Delay(5000);
}
leDevice.GattConnectionStateChanged += LeDevice_GattConnectionStateChanged;
client = leDevice.GattConnect(false);
```
<a name="gatt"></a>
## Managing GATT Client Operations

To perform GATT client operations:

1.  Define a connection state change event handler and register it for the `GattConnectionStateChanged` event of the [Tizen.Network.Bluetooth.BluetoothLeDevice](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeDevice.html) class:

    ```
    /// Register for GATT connection event handler
    public static void LeDevice_GattConnectionStateChanged(object sender, GattConnectionStateChangedEventArgs e)
    {
        if (e.Result != (int)BluetoothError.None)
        }
            StateChanged_flag = false;
        }
        else if (!e.RemoteAddress.Equals(remote_addr))
        {
            StateChanged_flag = false;
        }
        else if (e.IsConnected.Equals(false))
        {
            StateChanged_flag = false;
        }
        else
        {
            StateChanged_flag = true;
        }
    }

    leDevice.GattConnectionStateChanged += LeDevice_GattConnectionStateChanged;
    ```

2.  Connect to the BLE target device:

    ```
    client = leDevice.GattConnect(false);
    ```

3.  Retrieve the address of the remote device:

    ```
    string address = leDevice.RemoteAddress;
    ```

4.  Discover the service, characteristics, and descriptors of the remote service:
    1.  To retrieve a list of the services belonging to the remote device, use the `GetServices()` method of the [Tizen.Network.Bluetooth.BluetoothGattClient](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothGattClient.html) class:

        ```
        IEnumerable<BluetoothGattService> srv_list;
        srv_list = client.GetServices();
        ```

    2.  To retrieve a list of the characteristics of each service belonging to the remote device, use the `GetCharacteristics()` method of the [Tizen.Network.Bluetooth.BluetoothGattService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothGattService.html) class:

        ```
        foreach (BluetoothGattService item in srv_list)
        {
            IEnumerable<BluetoothGattCharacteristic> charc_list;
            charc_list = item.GetCharacteristics();
        }
        ```

    3.  To retrieve a list of the descriptors of each characteristic, use the `GetDescriptors()` method of the [Tizen.Network.Bluetooth.BluetoothGattCharacteristic](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothGattCharacteristic.html) class:

        ```
        foreach (BluetoothGattCharacteristic item in charc_list)
        {
            IEnumerable<BluetoothGattDescriptor> desc_list;
            desc_list = item.GetDescriptors();
        }
        ```

    4.  To retrieve the descriptor data:

        ```
        BluetoothGattDescriptor desc = desc_list.First<BluetoothGattDescriptor>();
        ```

5.  To read the value of the given attribute handle, use the `ReadValueAsync()` method of the `Tizen.Network.Bluetooth.BluetoothGattClient` class:

    ```
    IEnumerable<BluetoothGattService> srv_list = client.GetServices();
    Assert.IsNotNull(srv_list, "srv_list should not be null");

    BluetoothGattService srv = srv_list.First<BluetoothGattService>();
    Assert.IsNotNull(srv, "srv should not be null");

    IEnumerable<BluetoothGattCharacteristic> charc_list = srv.GetCharacteristics();
    Assert.IsNotNull(charc_list, "charc_list should not be null");

    BluetoothGattCharacteristic charc = charc_list.First<BluetoothGattCharacteristic>();
    Assert.IsNotNull(charc, "charc should not be null");

    IEnumerable<BluetoothGattDescriptor> desc_list = charc.GetDescriptors();
    Assert.IsNotNull(desc_list, "desc_list should not be null");

    BluetoothGattDescriptor desc = desc_list.First<BluetoothGattDescriptor>();
    Assert.IsNotNull(desc, "desc should not be null");

    bool status = await client.ReadValueAsync(desc);
    /// Wait for the read operation to be complete
    Assert.IsTrue(status, "ReadValueAsync Status should be true");
    ```

6.  To set a value for the given attribute handle, use the `WriteValueAsync()` method:

    ```
    charc.SetValue(charc_value);
    bool status = await client.WriteValueAsync(charc);
    Assert.IsTrue(status, "WriteValueAsync Status should be true");
    string value = charc.GetValue(0);
    Assert.AreEqual(charc_value, value);
    ```

7.  Manage characteristic data changes:
    1.  Register an event handler for the `ValueChanged` event of the `Tizen.Network.Bluetooth.BluetoothGattCharacteristic` class, which triggers when the characteristic value changes on the remote device:

        ```
        charc.ValueChanged += Charc_ValueChanged;
        /// Wait for a value change notification from remote device.
        ```

    2.  Once the `ValueChanged` event triggers, use the event handler to display the changed value:

        ```
        private static void Charc_ValueChanged(object sender, ValueChangedEventArgs e)
        {
            byte[] b = e.Value;
        }
        ```

    3.  When you no longer need the value change notifications, deregister the event handler:

        ```
        Assert.IsNotNull(charc, "charc should not be null");
        /// If the change notification is not required deregister the event handler
        charc.ValueChanged -= Charc_ValueChanged;
        ```

8.  When you no longer need the client, deregister the connection state change event handler, and disconnect from the remote device using the `GattDisconnect()` method of the `Tizen.Network.Bluetooth.BluetoothLeDevice` class:

    ```
    /// Deregister the GATT connection state change event handler
    leDevice.GattConnectionStateChanged -= LeDevice_GattConnectionStateChanged;

    /// Disconnect from the client
    leDevice.GattDisconnect();
    ```
<a name="gatt_getter"></a>
## Managing Common GATT Getter Operations

To perform getter operations for client-related information:

-   Retrieve the UUID of a service, characteristic, or descriptor:

    ```
    /// Service UUID
    IEnumerable<BluetoothGattService> srv_list = client.GetServices();
    Assert.IsNotNull(srv_list, "srv_list should not be null");

    BluetoothGattService srv = srv_list.First();
    Assert.IsNotNull(srv, "srv should not be null");
    string ServiceUuid = srv.Uuid;

    /// Characteristic UUID
    IEnumerable<BluetoothGattCharacteristic> charc_list = srv.GetCharacteristics();
    Assert.IsNotNull(charc_list, "charc_list should not be null");

    BluetoothGattCharacteristic characteristics = charc_list.First();
    string CharacteristicUuid = characteristics.Uuid;

    /// Descriptor UUID
    IEnumerable<BluetoothGattDescriptor> desc_list = charc.GetDescriptors();
    Assert.IsNotNull(desc_list, "desc_list should not be null");

    BluetoothGattDescriptor desc = desc_list.First<BluetoothGattDescriptor>();
    Assert.IsNotNull(desc, "desc should not be null");
    string DescriptorUuid = desc.Uuid;
    ```

-   Retrieve the value of a characteristic or descriptor:

    ```
    int offset = 0;
    const string DescriptorUuid = "2902";
    static string DescriptorStringValue = "descriptorValue";
    const BluetoothGattPermission descriptorPermissions = BluetoothGattPermission.Read;
    static byte[] descriptorValue = Encoding.UTF8.GetBytes(DescriptorStringValue);

    const string CharacteristicUuid = "2A19";
    const string CharacteristicStringValue = "CharacteristicValue";
    static byte[] _characteristicValue = Encoding.UTF8.GetBytes(CharacteristicStringValue);
    static BluetoothGattPermission _characteristicPermissions = BluetoothGattPermission.Read | BluetoothGattPermission.Write;
    static BluetoothGattProperty _characteristicProperties = BluetoothGattProperty.Read | BluetoothGattProperty.Notify;

    _attributeObjs = new Dictionary<BluetoothGattAttribute, AttributeTestData>
    {
        {new BluetoothGattDescriptor(DescriptorUuid, descriptorPermissions, descriptorValue), new AttributeTestData(DescriptorUuid, descriptorPermissions, DescriptorStringValue)},
        {new BluetoothGattCharacteristic(CharacteristicUuid, _characteristicPermissions, _characteristicProperties, _characteristicValue), new AttributeTestData(CharacteristicUuid, _characteristicPermissions, CharacteristicStringValue)},
    };

    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;

        int actualValue = attribute.GetValue(IntDataType.SignedInt8, offset);
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "attribute.Uuid " + attribute.Uuid + " ActualValue " + actualValue));
    }
    ```

-   Retrieve a value of a characteristic or descriptor as an `integer` type:

    ```
    /// Assuming all the input parameters (type, and offset) are available
    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;

        int actualValue = attribute.GetValue(IntDataType.SignedInt16, offset);
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "attribute.Uuid " + attribute.Uuid + " ActualValue " + actualValue));
    }
    ```

-   Retrieve a value of a characteristic or descriptor as a `float` type:

    ```
    /// Assuming all the input parameters (type, and offset) are available
    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;

        double actualValue = attribute.GetValue(FloatDataType.Float, offset);
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "attribute.Uuid " + attribute.Uuid + " ActualValue " + actualValue));
    }
    ```

-   Retrieve a service, characteristic, or descriptor with a specific UUID:

    ```
    string svc_uuid = "0000180f-0000-1000-8000-00805f9b34fb"; /// Battery service
    string chr_uuid = "00002a19-0000-1000-8000-00805f9b34fb"; /// Battery level
    string desc_uuid = "00002902-0000-1000-8000-00805f9b34fb"; /// Client characteristic configuration
    BluetoothGattService svc;
    BluetoothGattCharacteristic chr;
    BluetoothGattDescriptor desc;

    svc = client.GetService(svc_uuid);
    Assert.IsNotNull(svc, "svc should not be null");

    chr = svc.GetCharacteristic(chr_uuid);
    Assert.IsNotNull(chr, "chr should not be null");

    desc = chr.GetDescriptor(desc_uuid);
    Assert.IsNotNull(desc, "desc should not be null");
    ```

-   Retrieve the properties of a specified characteristic by using the `Properties` property of the `Tizen.Network.Bluetooth.BluetoothGattCharacteristic` class:

    ```
    BluetoothGattProperty properties;
    string svc_uuid = "0000180f-0000-1000-8000-00805f9b34fb"; /// Battery service
    string chr_uuid = "00002a19-0000-1000-8000-00805f9b34fb"; /// Battery level
    BluetoothGattService svc;
    BluetoothGattCharacteristic chr;

    svc = client.GetService(svc_uuid);
    Assert.IsNotNull(svc, "svc should not be null");

    chr = svc.GetCharacteristic(chr_uuid);
    Assert.IsNotNull(chr, "chr should not be null");

    properties = chr.Properties;
    ```

-   Retrieve the write type of a specified characteristic by using the `WriteType` property of the `Tizen.Network.Bluetooth.BluetoothGattCharacteristic` class:

    ```
    BluetoothGattWriteType WriteType;
    string svc_uuid = "0000180f-0000-1000-8000-00805f9b34fb"; /// Battery service
    string chr_uuid = "00002a19-0000-1000-8000-00805f9b34fb"; /// Battery level
    BluetoothGattService svc;
    BluetoothGattCharacteristic chr;

    /// Service UUID
    svc = client.GetService(svc_uuid);
    Assert.IsNotNull(svc, "svc should not be null");

    chr = svc.GetCharacteristic(chr_uuid);
    Assert.IsNotNull(chr, "chr should not be null");

    WriteType = chr.WriteType;
    ```

-   Retrieve an included service instance with a specific UUID by using the `GetIncludeService()` method of the [Tizen.Network.Bluetooth.BluetoothGattService](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothGattService.html) class:

    ```
    const string ServiceUuid = "180D";
    const string Service1Uuid = "180F";
    const string Service2Uuid = "1811";

    BluetoothGattService service = new BluetoothGattService(ServiceUuid, BluetoothGattServiceType.Primary);
    Assert.IsNotNull(service, "PRECONDITION Failed: service should not be null");

    BluetoothGattService service1 = new BluetoothGattService(Service1Uuid, BluetoothGattServiceType.Secondary);
    Assert.IsNotNull(service1, "PRECONDITION Failed: service 1 should not be null");

    BluetoothGattService service2 = new BluetoothGattService(Service2Uuid, BluetoothGattServiceType.Secondary);
    Assert.IsNotNull(service2, "PRECONDITION Failed: service 2 should not be null");

    service.AddService(service1);
    service.AddService(service2);

    var result = service.GetIncludeService(Service1Uuid);
    Assert.IsNotNull(result, "Expecting added service back, got null");
    ```
<a name="gatt_setter"></a>
## Managing Common GATT Setter Operations

To set the client properties and attribute values:

-   Set or update the characteristic value (`uint8` type value):

    ```
    int unsignedInt8Value = byte.MaxValue;
    int offset = 0;

    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;
        attribute.SetValue(IntDataType.UnsignedInt8, unsignedInt8Value, offset);
    }
    ```

-   Set or update the characteristic value (`integer` type value):

    ```
    int unsignedInt8Value = UInt16.MaxValue;
    int offset = 0;

    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;
        attribute.SetValue(IntDataType.UnsignedInt16, unsignedInt16Value, offset);
    }
    ```

-   Set or update the characteristic value (`float` type value):

    ```
    int mantissa = 123, exponent = 2;
    int offset = 0;

    foreach (KeyValuePair<BluetoothGattAttribute, AttributeTestData> item in _attributeObjs)
    {
        BluetoothGattAttribute attribute = item.Key;
        attribute.SetValue(FloatDataType.Float, mantissa, exponent, offset);
    }
    ```

-   Set the characteristic write type:

    ```
    const string CharacteristicUuid = "2A19";
    const string CharacteristicStringValue = "CharacteristicValue";
    static BluetoothGattPermission _characteristicPermissions = BluetoothGattPermission.Read | BluetoothGattPermission.Write;

    BluetoothGattProperty _characteristicProperties = BluetoothGattProperty.WriteWithoutResponse;
    BluetoothGattCharacteristic characteristic = new BluetoothGattCharacteristic(CharacteristicUuid, _characteristicPermissions, _characteristicProperties, _characteristicValue);
    characteristic.WriteType = BluetoothGattWriteType.NoResponse;
    ```
<a name="le_scan"></a>
## Managing Bluetooth LE Scans

To discover nearby LE devices, perform an LE scan operation:

1.  Register an event handler for the `ScanResultChanged` event of the [Tizen.Network.Bluetooth.BluetoothAdapter](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAdapter.html) class, and start the LE scan with the `StartLeScan()` method:

    ```
    public static BluetoothLeDevice leDevice = null;

    BluetoothAdapter.ScanResultChanged += scanResultEventHandler;
    if (leDevice == null)
    {
        BluetoothAdapter.StartLeScan();
        /// Wait while the system searches for the LE target you want to connect to
        /// If you find the LE target you want, stop the scan
        /// BluetoothAdapter.StartLeScan() operates continually until you call BluetoothAdapter.StopLeScan()
        /// If you do not call BluetoothAdapter.StopLeScan() after calling BluetoothAdapter.StartLeScan(),
        /// calling BluetoothAdapter.StartLeScan() again can cause an in-progress error

        /// Wait for the device to be found and flag to be set
        await WaitScanFlag();

        BluetoothAdapter.StopLeScan();
    }
    ```

2.  In the event handler method, handle the scan results. The parameters contain information on all the scanned LE devices, such as the device name, transmission level, service data list, appearance, and manufacturer data of the devices.

    To handle the scan result:

    ```
    public static void scanResultEventHandler(object sender, AdapterLeScanResultChangedEventArgs e)
    {
        int txLevel;
        int rssi;
        BluetoothError result;
        string address;
        BluetoothLeDevice leDevice = null;
        BluetoothLePacketType PacketType;

        if (!e.DeviceData.Equals(null) && e.DeviceData.RemoteAddress.Equals(remote_addr))
        {
            Log.Info("TCT", "[TestCase] found the matching device ");
            leDevice = e.DeviceData;
            result = e.Result;
            scanFlag = true;
        }
        address = leDevice.RemoteAddress;
        rssi = leDevice.Rssi;

        txLevel = leDevice.TxPowerLevel;
        if (txLevel != -1)
        {
            Assert.IsInstanceOf<int>(leDevice.TxPowerLevel, "BluetoothLeDevice TxPowerLevel is not valid");
        }

        IEnumerable<string> ssuuid = leDevice.ServiceSolictationUuid;
        if (ssuuid != null)
        {
            foreach (string uuid in ssuuid)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "ServiceSolictationUuid is : " + uuid);
            }
        }

        byte[] scanDataInfo = leDevice.ScanDataInformation;
        if (scanDataInfo != null && scanDataInfo.Length > 0)
        {
            LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Found Scan Data of length : " + scanDataInfo.Length);
        }

        IEnumerable<string> svcuuid = leDevice.ServiceUuid;
        if (svcuuid != null)
        {
            foreach (string uuid in svcuuid)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "UUID is : " + uuid);
            }
        }

        IEnumerable<BluetoothLeServiceData> serviceList = leDevice.GetServiceDataList();
        if (serviceList != null)
        {
            foreach (BluetoothLeServiceData data in serviceList)
            {
                LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "Retrieved service data list UUID : " + data.ServiceUuid + " length is " + data.ServiceDataLength);
            }
        }

        leDevice.PacketType = BluetoothLePacketType.BluetoothLeScanResponsePacket;
        PacketType = leDevice.PacketType;
        Assert.AreEqual(BluetoothLePacketType.BluetoothLeScanResponsePacket, PacketType);

        leDevice.PacketType = BluetoothLePacketType.BluetoothLeAdvertisingPacket;
        PacketType = leDevice.PacketType;
        Assert.AreEqual(BluetoothLePacketType.BluetoothLeAdvertisingPacket, PacketType);
    }
    ```
<a name="add_adv_data"></a>
## Adding Advertising Data to the LE Advertisement

LE advertising data can be added to the LE advertisement or the scan response data. You can add various information, such as the device name, service UUID, service solicitation UUID, advertising appearance, advertising transmission power level, device name, and manufacturer data.

To add advertising data:

1.  Create a new instance of the [Tizen.Network.Bluetooth.BluetoothLeAdvertiseData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeAdvertiseData.html) class and add advertising data to it:

    ```
    static int _appearance = 192;
    static BluetoothLeAdvertiseData _advertiseData = null;

    if (_advertiseData == null)
    {
        _advertiseData = new BluetoothLeAdvertiseData();
    }

    // Add appearance
    _advertiseData.PacketType = BluetoothLePacketType.BluetoothLeAdvertisingPacket;
    _advertiseData.Appearance = _appearance;

    /// Add device name
    _advertiseData.PacketType = BluetoothLePacketType.BluetoothLeAdvertisingPacket;
    _advertiseData.IncludeDeviceName = true;

    /// Add TX power level
    _advertiseData.PacketType = BluetoothLePacketType.BluetoothLeAdvertisingPacket;
    _advertiseData.IncludeTxPowerLevel = true;

    /// Add manufacturer data
    ManufacturerData manufData = new ManufacturerData();
    manufData.Data = new byte[5] {0x01, 0x02, 0x03, 0x04, 0x05};
    manufData.Id = 117;
    manufData.DataLength = 5;
    _advertiseData.AddAdvertisingManufacturerData(BluetoothLePacketType.BluetoothLeScanResponsePacket, manufData);

    /// Add service solicitation UUID
    string serviceSolicitationUuid = "180d";
    _advertiseData.AddAdvertisingServiceSolicitationUuid(BluetoothLePacketType.BluetoothLeScanResponsePacket, serviceSolicitationUuid);

    /// Add service UUID
    string serviceUuid = "1805";
    _advertiseData.AddAdvertisingServiceUuid(BluetoothLePacketType.BluetoothLeScanResponsePacket, serviceUuid);

    /// Add service data
    BluetoothServiceData serviceData = new BluetoothServiceData();
    serviceData.Uuid = "1805";
    serviceData.DataLength = 3;
    serviceData.Data = new byte[3] {0x01, 0x02, 0x03};
    BluetoothLeAdvertiseData newAdvertiseData = new BluetoothLeAdvertiseData();
    newAdvertiseData.AddAdvertisingServiceData(BluetoothLePacketType.BluetoothLeScanResponsePacket, serviceData);
    ```

2.  When you are done, destroy the `Tizen.Network.Bluetooth.BluetoothLeAdvertiseData` class instance:

    ```
    _advertiseData = null;
    ```
<a name="set_adv_conn"></a>
## Setting the LE Advertising Connectable Mode

When advertising to a remote device, use the `AdvertisingConnectable()` property of the [Tizen.Network.Bluetooth.BluetoothLeAdvertiseData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeAdvertiseData.html) class to define whether the advertising type is connectable or non-connectable:

```
static BluetoothLeAdvertiseData _advertiseData = null;
_advertiseData = new BluetoothLeAdvertiseData();

_advertiseData.AdvertisingConnectable = true;
Assert.IsTrue(_advertiseData.AdvertisingConnectable, "AdvertisingConnectable is not equal to the value set");

_advertiseData.AdvertisingConnectable = false;
Assert.IsFalse(_advertiseData.AdvertisingConnectable, "AdvertisingConnectable is not equal to the value set");
```

<a name="set_adv_mode"></a>
## Setting the LE Advertising Mode

The advertising mode controls the advertising power and latency, and can be set to be balanced, low latency, or low energy.

Set the advertising mode by setting the `AdvertisingMode` property of the [Tizen.Network.Bluetooth.BluetoothLeAdvertiseData](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeAdvertiseData.html) class instance to one of the values of the [Tizen.Network.Bluetooth.BluetoothLeAdvertisingMode](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeAdvertisingMode.html) enumeration:

```
static BluetoothLeAdvertiseData _advertiseData = null;
_advertiseData = new BluetoothLeAdvertiseData();

_advertiseData.AdvertisingMode = BluetoothLeAdvertisingMode.BluetoothLeAdvertisingBalancedMode;
Assert.IsInstanceOf<BluetoothLeAdvertisingMode>(_advertiseData.AdvertisingMode, "AdvertisingMode value is not of type BluetoothLeAdvertisingMode");
```
<a name="start_adv"></a>
## Starting and Stopping LE Advertising

To manage advertising:

1.  To start advertising with the given advertiser and advertising parameter information, use the `StartAdvertising()` method of the [Tizen.Network.Bluetooth.BluetoothLeAdvertiser](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothLeAdvertiser.html) class:

    ```
    static BluetoothLeAdvertiser advertiser = null;
    static BluetoothLeAdvertiseData advertiseData = null;
    static bool advertisingFlag = false;

    advertiseData = new BluetoothLeAdvertiseData();
    advertiseData.AdvertisingMode = BluetoothLeAdvertisingMode.BluetoothLeAdvertisingBalancedMode;
    advertiseData.AdvertisingConnectable = true;
    advertiseData.Appearance = 192;

    BluetoothLePacketType packetType = BluetoothLePacketType.BluetoothLeAdvertisingPacket;
    string serviceUuid = "1805"; /// time_svc_uuid_16
    advertiseData.AddAdvertisingServiceUuid(packetType, serviceUuid);

    string serviceSolicitationUuid = "180d"; /// heart_rate_svc_uuid_16
    advertiseData.AddAdvertisingServiceSolicitationUuid(packetType, serviceSolicitationUuid);

    /// Add sample service data for testing
    BluetoothServiceData serviceData = new BluetoothServiceData();
    serviceData.Uuid = "1805";
    serviceData.DataLength = 3;
    serviceData.Data = new byte[3] {0x01, 0x02, 0x03};
    advertiseData.AddAdvertisingServiceData(packetType, serviceData);

    advertiseData.IncludeDeviceName = true;
    advertiseData.IncludeTxPowerLevel = true;

    /// Add sample manufacturer data for testing
    packetType = BluetoothLePacketType.BluetoothLeScanResponsePacket;
    ManufacturerData manufData = new ManufacturerData();
    manufData.Data = new byte[5] {0x01, 0x02, 0x03, 0x04, 0x05};
    manufData.Id = 117;
    manufData.DataLength = 5;
    advertiseData.AddAdvertisingManufacturerData(packetType, manufData);

    public static void AdvertisingChangedEventHandler(object sender, AdvertisingStateChangedEventArgs e)
    {
        LogUtils.Write(LogUtils.DEBUG, LogUtils.TAG, "advertising callback");
        if ((int)e.State == (int)BluetoothLeAdvertisingState.BluetoothLeAdvertisingStarted)
        {
            advertisingFlag = true;
        }
        if ((int)e.State == (int)BluetoothLeAdvertisingState.BluetoothLeAdvertisingStopped)
        {
            advertisingFlag = false;
        }
    }

    advertiser.AdvertisingStateChanged += AdvertisingChangedEventHandler;
    advertiser.StartAdvertising(advertiseData);
    ```

2.  To stop advertising with the given advertiser, use the `StopAdvertising()` method:

    ```
    if (advertiser != NULL)
    {
        advertiser.StopAdvertising(advertiseData);
        advertiser.AdvertisingStateChanged -= AdvertisingChangedEventHandler;
    }
    ```
<a name="avrcp"></a>
## Handling Bluetooth AVRCP Events

To receive notifications of Bluetooth AVRCP events:

-   To receive notifications when the connection state is changed, register an event handler for the `TargetConnectionStateChanged` event of the [Tizen.Network.Bluetooth.BluetoothAvrcp](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Bluetooth.BluetoothAvrcp.html) class:

    ```
    static BluetoothAvrcp avrcpProfile = null;

    avrcpProfile = pairedDevice.GetProfile<BluetoothAvrcp>();

    if (avrcpProfile != null)
    {
        avrcpProfile.TargetConnectionStateChanged += EventHandlerTargetConnectionChanged;
    }
    ```

-   To receive notifications when the remote control device changes the repeat mode, register an event handler for the `RepeatModeChanged` event of the `Tizen.Network.Bluetooth.BluetoothAvrcp` class:

    ```
    static BluetoothAvrcp avrcpProfile = null;

    avrcpProfile = pairedDevice.GetProfile<BluetoothAvrcp>();

    if (avrcpProfile != null)
    {
        avrcpProfile.RepeatModeChanged += EventHandlerRepeatModeChanged;
    }

    public static void EventHandlerRepeatModeChanged(object sender, RepeatModeChangedEventArgs e)
    {
        if (e.Mode == AllTrack)
        {
            avrcpProfile.NotifyRepeatMode(RepeatMode.AllTrack);
        }
    }
    ```
<a name="release"></a>
## Releasing All Resources

To release all Bluetooth resources, deregister the event handlers:

```
/// Deregister event handlers
BluetoothAdapter.StateChanged -= EventHandlerStateChanged;
BluetoothAdapter.VisibilityDurationChanged -= EventHandlerVisibilityDurationChanged;
BluetoothAdapter.VisibilityModeChanged -= EventHandlerVisibilityModeChanged;
BluetoothAdapter.DiscoveryStateChanged -= EventHandlerDiscoveryChanged;
BluetoothAdapter.ScanResultChanged -= scanResultEventHandler;
advertiser.AdvertisingStateChanged -= AdvertisingChangedEventHandler;
Client.ConnectionStateChanged -= ConnectionStateChangedEventHandler;
avrcpProfile.TargetConnectionStateChanged -= EventHandlerTargetConnectionChanged;
avrcpProfile.RepeatModeChanged -= EventHandlerRepeatModeChanged;
```



## Related Information
  * Dependencies
    -   Tizen 4.0 and Higher
