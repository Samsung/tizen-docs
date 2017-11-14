Connection Management
=====================

## Dependencies

- Tizen 4.0 and Higher

You can create a network connection in your application, and use it to
perform various operations. The application can access connection
details, such as the IP address, proxy information, gateway information,
and connection statistics.

The main features of the Tizen.Network.Connection namespace are:

-   Managing connections

    You can manage various data connections with the
    [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionManager.html) class.
    You can [retrieve the connection state and access network
    details](#connection_info), such as the IP address, proxy address,
    and MAC address. You can also [monitor connection state change
    events](#events), and [create cellular connection
    profiles](#create_profile).

- Managing connection profiles

    Connection profiles are instances of the
    [Tizen.Network.Connection.ConnectionProfile](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionProfile.html)
    class, which allow you to retrieve and set various connection
    properties, such as the state, type, and name. You can also monitor
    the profile state changes. You can [retrieve information about
    available connection profiles](#use_profile), and open, modify, and
    remove them, using the
    [Tizen.Network.Connection.ConnectionProfileManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionProfileManager.html) class.

    When you use a socket, it is automatically bound with the network
    interface of the default connection profile. For example, if the
    device is connected to the Wi-Fi network, Wi-Fi is the
    default network. To use another network, you must open the relevant
    connection profile.

    The `Tizen.Network.Connection.ConnectionProfile` class has child
    classes for cellular and Wi-Fi profiles:

    -   To manage a cellular profile, use a
        [Tizen.Network.Connection.CellularProfile](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1CellularProfile.html)
        class instance, which you can get using the
        `CreateCellularProfile()` method of the
        `Tizen.Network.Connection.ConnectionManager` class, or the
        `GetDefaultCellularProfile()` or `GetProfileListAsync()` methods
        of the
        `Tizen.Network.Connection.ConnectionProfileManager` class. You
        can use the instance to access and modify various cellular
        connection details.
    -   To manage a Wi-Fi profile, use a
        [Tizen.Network.Connection.WiFiProfile](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1WiFiProfile.html)
        class instance, which you can get using the
        `GetProfileListAsync()` method of the
        `Tizen.Network.Connection.ConnectionManager` class. You can use
        the instance to access various Wi-Fi connection details, and set
        a passphrase for the WPA (Wi-Fi Protected Access).



Prerequisites
-------------

To use the
[Tizen.Network.Connection](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html)
namespace, the application has to request permission by adding the
following privileges to the `tizen-manifest.xml` file:
``` {.prettyprint}
<privileges>
   <privilege>http://tizen.org/privilege/network.get</privilege>
   <privilege>http://tizen.org/privilege/network.set</privilege>
   <privilege>http://tizen.org/privilege/network.profile</privilege>
</privileges>
```


Retrieving Connection Information <a id="connection_info"></a>
---------------------------------

To get information about a network connection, use the
[Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionManager.html)
class:
-   To retrieve the connection state for a specific connection type
    (Bluetooth, Ethernet, Ethernet cable, Wi-Fi, or cellular), use the
    applicable `Tizen.Network.Connection.ConnectionManager.XXXState`
    property, for example,
    `Tizen.Network.Connection.ConnectionManager.CellularState`. It
    returns the connection state using the values of the appropriate
    enumeration
    ([Tizen.Network.Connection.CellularState](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#acca0f98bded3809d947e84cab4ddb3b0),
    [Tizen.Network.Connection.ConnectionState](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#a87018c9157d037d7a73d5130238d7ac3),
    or
    [Tizen.Network.Connection.EthernetCableState](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#aed66f3243666bffe5d5093140eb340ff)):

    ``` {.prettyprint}
    CellularState state = ConnectionManager.CellularState;

    Log.Info(Globals.LogTag, "State = " + state);
    ```

- To retrieve a network address, use the appropriate `GetXXX()`
    method, for example, `GetIPAddress()`. The available method
    parameter values are defined in the
    [Tizen.Network.Connection.AddressFamily](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#a629d06087a32927639f03dc0d794828b)
    (for retrieving the IPv4 or IPv6 address family) and
    [Tizen.Network.Connection.ConnectionType](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#a1c8ddac20ac35918df660ba47678eaf1)
    (for retrieving the MAC address or IPv6 address list) enumerations.

    ``` {.prettyprint}
    System.Net.IPAddress ipAddress = ConnectionManager.GetIPAddress(AddressFamily.IPv4);

    Log.Info(Globals.LogTag, "IpAddress = " + ipAddress.ToString());
    ```



Monitoring Connection Changes <a id="events"></a>
-----------------------------

You can monitor changes in the IP address, proxy address, Ethernet cable
state, and connection type.
To monitor for changes in connection information, such as IP address and
connection type:

1.  To receive notifications on specific connection changes, register
    event handlers using the related `XXXChanged` events of the
    [Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionManager.html)
    class:

    ``` {.prettyprint}
    ConnectionManager.IPAddressChanged += EventHandlerIpAddressChanged;

    ConnectionManager.ConnectionTypeChanged += EventHandlerConnectionTypeChanged;
    ```

2. Define the event handlers:

    ``` {.prettyprint}
    public static void EventHandlerIpAddressChanged(object sender, AddressEventArgs e)
    {
        Log.Info(Globals.LogTag, "IPCHANGE = " + e.IPv4Address);
    }
    public static void EventHandlerConnectionTypeChanged(object sender, ConnectionTypeEventArgs e)
    {
        Log.Info(Globals.LogTag, "ConnectionType = " + e.ConnectionType);
    }
    ```

3. When the notifications are no longer needed, deregister the event
    handlers:

    ``` {.prettyprint}
    ConnectionManager.IPAddressChanged -= EventHandlerIpAddressChanged;

    ConnectionManager.ConnectionTypeChanged -= EventHandlerConnectionTypeChanged;
    ```



Creating a Cellular Profile <a id="create_profile"></a>
---------------------------

To create a cellular profile, use the `CreateCellularProfile()` method
of the
[Tizen.Network.Connection.ConnectionManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionManager.html)
class:

``` {.prettyprint}
CellularProfile rCP = null;
string _key = "RequestCellularProfile";
rCP = ConnectionManager.CreateCellularProfile(ConnectionProfileType.Cellular, _key);
```


Managing Connection Profiles <a id="use_profile"></a>
----------------------------

To change the active connection profile and access connection details:

-   To open a new connection profile:
    1.  Retrieve the connection profile you want to open. You can do
        this in 2 ways:
        -   Retrieve a list of all available connection profiles using
            the `GetProfileListAsync()` method of the
            [Tizen.Network.Connection.ConnectionProfileManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1Network_1_1Connection_1_1ConnectionProfileManager.html)
            class, and select the profile you want.
        - Retrieve the connection profile of a specific
            cellular service.

            Call the `GetDefaultCellularProfile()` method of the
            `Tizen.Network.Connection.ConnectionProfileManager` class
            and use the appropriate value from the
            [Tizen.Network.Connection.CellularServiceType](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1Network_1_1Connection.html#ae5cadb185a0c270f1b0f2cc321b0dc15)
            enumeration as the parameter:

            ``` {.prettyprint}
            try
            {
                ConnectionProfile currCP = ConnectionProfileManager.GetDefaultCellularProfile(CellularServiceType.Internet);
            }
            catch (Exception e)
            {
                Log.Info(Globals.LogTag, "Exception = " + e.ToString());
            }
            ```

    2. Open the connection profile using the `ConnectProfileAsync()`
        method of the
        `Tizen.Network.Connection.ConnectionProfileManager` class:

        ``` {.prettyprint}
        await ConnectionProfileManager.ConnectProfileAsync(currCP);
        ```

- To retrieve the interface name for the active connection profile:

    ``` {.prettyprint}
    string name = currCP.InterfaceName;

    Log.Info(Globals.LogTag, "InterfaceName = " + Name);
    ```

- To retrieve the address information of the active connection
    profile, use the
    [Tizen.Network.Connection.IAddressInformation](https://developer.tizen.org/dev-guide/csapi/interfaceTizen_1_1Network_1_1Connection_1_1IAddressInformation.html)
    instance properties:

    ``` {.prettyprint}
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

    You can get and set all the `IAddressInformation` properties: both
    DNS addresses, gateway and IP addresses, subnet mask, and IP
    configuration type.
