# Connection Management


You can create a network connection in your application, and use it to perform various operations. The application can access connection details, such as the IP address, proxy information, gateway information, and connection statistics.

The main features of the Tizen.Network.Connection namespace are:

-   Managing connections

    You can manage various data connections with the [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionManager.html) class. You can [retrieve the connection state and access network details](#connection_info), such as the IP address, proxy address, and MAC address. You can also [monitor connection state change events](#events), and [create cellular connection profiles](#create_profile).

-   Managing connection profiles

    Connection profiles are instances of the [Tizen.Network.Connection.ConnectionProfile](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionProfile.html) class, which allow you to retrieve and set various connection properties, such as the state, type, and name. You can also monitor the profile state changes. You can [retrieve information about available connection profiles](#use_profile), and open, modify, and remove them, using the [Tizen.Network.Connection.ConnectionProfileManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionProfileManager.html) class.

    When you use a socket, it is automatically bound with the network interface of the default connection profile. For example, if the device is connected to the Wi-Fi network, Wi-Fi is the default network. To use another network, you must open the relevant connection profile.

    The `Tizen.Network.Connection.ConnectionProfile` class has child classes for cellular and Wi-Fi profiles:

    -   To manage a cellular profile, use a [Tizen.Network.Connection.CellularProfile](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.CellularProfile.html) class instance, which you can get using the `CreateCellularProfile()` method of the `Tizen.Network.Connection.ConnectionManager` class, or the `GetDefaultCellularProfile()` or `GetProfileListAsync()` methods of the `Tizen.Network.Connection.ConnectionProfileManager` class. You can use the instance to access and modify various cellular connection details.
    -   To manage a Wi-Fi profile, use a [Tizen.Network.Connection.WiFiProfile](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.WiFiProfile.html) class instance, which you can get using the `GetProfileListAsync()` method of the `Tizen.Network.Connection.ConnectionManager` class. You can use the instance to access various Wi-Fi connection details, and set a passphrase for the WPA (Wi-Fi Protected Access).

## Prerequisites


To use the [Tizen.Network.Connection](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

```  
<privileges>
   <privilege>http://tizen.org/privilege/network.get</privilege>
   <privilege>http://tizen.org/privilege/network.set</privilege>
   <privilege>http://tizen.org/privilege/network.profile</privilege>
</privileges>
```

<a name="connection_info"></a>
## Retrieving Connection Information

To get information about a network connection, use the [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionManager.html) class:
-   To retrieve the connection state for a specific connection type (Bluetooth, Ethernet, Ethernet cable, Wi-Fi, or cellular), use the applicable `Tizen.Network.Connection.ConnectionManager.XXXState` property, for example, `Tizen.Network.Connection.ConnectionManager.CellularState`. It returns the connection state using the values of the appropriate enumeration ([Tizen.Network.Connection.CellularState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.CellularState.html), [Tizen.Network.Connection.ConnectionState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionState.html), or [Tizen.Network.Connection.EthernetCableState](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.EthernetCableState.html)):

    ```  
    CellularState state = ConnectionManager.CellularState;

    Log.Info(Globals.LogTag, "State = " + state);
    ```

-   To retrieve a network address, use the appropriate `GetXXX()` method, for example, `GetIPAddress()`. The available method parameter values are defined in the [Tizen.Network.Connection.AddressFamily](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.AddressFamily.html) (for retrieving the IPv4 or IPv6 address family) and [Tizen.Network.Connection.ConnectionType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionType.html) (for retrieving the MAC address or IPv6 address list) enumerations.

    ```  
    System.Net.IPAddress ipAddress = ConnectionManager.GetIPAddress(AddressFamily.IPv4);

    Log.Info(Globals.LogTag, "IpAddress = " + ipAddress.ToString());
    ```

<a name="events"></a>
## Monitoring Connection Changes

You can monitor changes in the IP address, proxy address, Ethernet cable state, and connection type.  

To monitor for changes in connection information, such as IP address and connection type:

1.  To receive notifications on specific connection changes, register event handlers using the related `XXXChanged` events of the [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionManager.html) class:

    ```  
    ConnectionManager.IPAddressChanged += EventHandlerIpAddressChanged;

    ConnectionManager.ConnectionTypeChanged += EventHandlerConnectionTypeChanged;
    ```

2.  Define the event handlers:

    ```  
    public static void EventHandlerIpAddressChanged(object sender, AddressEventArgs e)
    {
        Log.Info(Globals.LogTag, "IPCHANGE = " + e.IPv4Address);
    }
    public static void EventHandlerConnectionTypeChanged(object sender, ConnectionTypeEventArgs e)
    {
        Log.Info(Globals.LogTag, "ConnectionType = " + e.ConnectionType);
    }
    ```

3.  When the notifications are no longer needed, deregister the event handlers:

    ```  
    ConnectionManager.IPAddressChanged -= EventHandlerIpAddressChanged;

    ConnectionManager.ConnectionTypeChanged -= EventHandlerConnectionTypeChanged;
    ```

<a name="create_profile"></a>
## Creating a Cellular Profile

To create a cellular profile, use the `CreateCellularProfile()` method of the [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionManager.html) class:

```  
CellularProfile rCP = null;
string _key = "RequestCellularProfile";
rCP = ConnectionManager.CreateCellularProfile(ConnectionProfileType.Cellular, _key);
```

<a name="use_profile"></a>
## Managing Connection Profiles

To change the active connection profile and access connection details:

-   To open a new connection profile:
    1.  Retrieve the connection profile you want to open. You can do this in 2 ways:
        -   Retrieve a list of all available connection profiles using the `GetProfileListAsync()` method of the [Tizen.Network.Connection.ConnectionProfileManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.ConnectionProfileManager.html) class, and select the profile you want.
        -   Retrieve the connection profile of a specific cellular service.

            Call the `GetDefaultCellularProfile()` method of the `Tizen.Network.Connection.ConnectionProfileManager` class and use the appropriate value from the [Tizen.Network.Connection.CellularServiceType](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.CellularServiceType.html) enumeration as the parameter:

            ```  
            try
            {
                ConnectionProfile currCP = ConnectionProfileManager.GetDefaultCellularProfile(CellularServiceType.Internet);
            }
            catch (Exception e)
            {
                Log.Info(Globals.LogTag, "Exception = " + e.ToString());
            }
            ```

    2.  Open the connection profile using the `ConnectProfileAsync()` method of the `Tizen.Network.Connection.ConnectionProfileManager` class:

        ```  
        await ConnectionProfileManager.ConnectProfileAsync(currCP);
        ```

-   To retrieve the interface name for the active connection profile:

    ```  
    string name = currCP.InterfaceName;

    Log.Info(Globals.LogTag, "InterfaceName = " + Name);
    ```

-   To retrieve the address information of the active connection profile, use the [Tizen.Network.Connection.IAddressInformation](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.Connection.IAddressInformation.html) instance properties:

    ```  
    try
    {
        var iAddressInformation = currCP.IPv4Settings;
    }
    catch (Exception e)
    {
        Log.Info(Globals.LogTag, "Exception = " + e.ToString());
    }
    string address = iAddressInformation.Gateway;
    Log.Info(Globals.LogTag, "GatewayAddress = " + address);
    ```

    You can get and set all the `IAddressInformation` properties: both DNS addresses, gateway and IP addresses, subnet mask, and IP configuration type.


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
