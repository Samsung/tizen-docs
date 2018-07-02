# Wi-Fi


You can connect to a Wireless Local Area Network (WLAN) and transfer data over the network. The Wi-Fi Manager enables your application to activate and deactivate a local Wi-Fi device, and to scan for available access points.

The main features of the Tizen.Network.WiFi namespace include:

-   Wi-Fi device management

    You can use the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class to control aspects of your application's wireless connection. For example, you can [activate](#activating_wifi_device) or [deactivate](#deactivating_wifi_device) Wi-Fi, [monitor connection state changes](#managing_events), and [scan for available access points](#accesspoint_scan).

- Access point management

    With the [Tizen.Network.WiFi.WiFiAP](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiAP.html) class, you can [connect to a specific access point](#accesspoint_connect) and manage the Wi-Fi access point and security information:

    -   Access point details are instances of the [Tizen.Network.WiFi.WiFiNetwork](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiNetwork.html) class, which allows you to retrieve various access point information, such as the SSID, frequency band, and maximum speed of the access point.

    - Access point security details are instances of the [Tizen.Network.WiFi.WiFiSecurity](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiSecurity.html) class, which allows you to retrieve security information, such as the used encryption type and whether WPS is supported.

        You can also obtain EAP information, which is encapsulated in the [Tizen.Network.WiFi.WiFiEap](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiEap.html) class.

        **Table: Access point EAP information**

        | Information         | Description                              |
        |---------------------|------------------------------------------|
        | Authentication type | Wi-Fi EAP phase2 authentication type     |
        | EAP type            | Wi-Fi EAP type                           |
        | CA certificate      | EAP CA certificate (valid only if the EAP type is TLS) |
        | Client certificate  | EAP client certificate (valid only if the EAP type is TLS) |
        | Passphrase          | EAP passphrase (valid if the EAP type is PEAP or TTLS) |
        | Private key file    | EAP private key file (valid only if the EAP type is TLS) |  

    To create a `Tizen.Network.WiFi.WiFiAP` instance, use its constructor with the ESSID, or retrieve the instance from the `GetFoundAPs()` method of the `Tizen.Network.WiFi.WiFiManager` class.

The application uses the infrastructure mode to connect to a wireless local area network (WLAN). The infrastructure mode requires a wireless access point. To connect to a WLAN, the application client must be configured to use the same service set identifier (SSID) as the access point.


> **Note**  
> You can test the Wi-Fi functionality on a target device only. The emulator does not support this feature.


## Prerequisites

To enable your application to use the Wi-Fi functionality:

1.  To use the [Tizen.Network.WiFi](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.html) namespace, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://tizen.org/privilege/network.get</privilege>
       <privilege>http://tizen.org/privilege/network.set</privilege>
       <privilege>http://tizen.org/privilege/network.profile</privilege>
    </privileges>
    ```

2. To use the methods and properties of the Tizen.Network.WiFi namespace, include it in your application:

    ```
    using Tizen.Network.WiFi;
    ```

<a name="managing_events"></a>
## Managing Events

To manage events related to Wi-Fi operations, use event handlers registered to the following events of the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class:

-   `DeviceStateChanged` is called when the device state changes (Wi-Fi is activated or deactivated).
-   `ConnectionStateChanged` is called when the device access point connection state changes (connection to an access point is formed or lost).
-   `RssiLevelChanged` is called when the RSSI of the connected Wi-Fi changes
-   `BackgroundScanFinished` is called when a background scan has finished.

To manage device and connection state events:

1.  Define event handlers:

    ```
    public static void EventHandlerDeviceStateChanged(object sender, EventArgs e)
    {
        Console.WriteLine("Device state: " + e.State);
    }
    public static void EventHandlerConnectionStateChanged(object sender, EventArgs e)
    {
        Console.WriteLine("WiFi connection state: " + e.State);
    }
    ```

2. Register the event handlers for the `DeviceStateChanged` and `ConnectionStateChanged` events of the `Tizen.Network.WiFi.WiFiManager` class:

    ```
    WiFiManager.DeviceStateChanged += EventHandlerDeviceStateChanged;

    WiFiManager.ConnectionStateChanged += EventHandlerConnectionStateChanged;
    ```

3. When they are no longer needed, deregister the event handlers:

    ```
    WiFiManager.DeviceStateChanged -= EventHandlerDeviceStateChanged;

    WiFiManager.ConnectionStateChanged -= EventHandlerConnectionStateChanged;
    ```

<a name="activating_wifi_device"></a>
## Activating a Wi-Fi Device

To activate a Wi-Fi local device and check the connection state:

1.  Activate a Wi-Fi device using the asynchronous `ActivateAsync()` method of the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class:

    ```
    try
    {
        await WiFiManager.ActivateAsync();
    ```

2. Check whether the connection has been made by using the `IsActive` property of the `Tizen.Network.WiFi.WiFiManager` class:

    ```
        if (WiFiManager.IsActive)
        {
            Console.WriteLine("WiFi is activated");
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="accesspoint_scan"></a>
## Scanning for Access Points

To scan nearby access points and get their details:

1.  Scan nearby access points using the `ScanAsync()` method of the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class:

    ```
    try
    {
        await WiFiManager.ScanAsync();
    ```

2. Retrieve the scan results (the found access points) with the `GetFoundAPs()` method of the `Tizen.Network.WiFi.WiFiManager` class.

    In this example, the application displays the name and connection state of each access point it finds. You can also get other information, such as the used frequency or the maximum speed the access point supports.

    ```
        var apList = WiFiManager.GetFoundAPs();
        foreach (var item in apList)
        {
            Console.WriteLine("AP name: " + item.NetworkInformation.Essid);
            Console.WriteLine("Connection state: " + item.NetworkInformation.ConnectionState);
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="accesspoint_connect"></a>
## Connecting to a Specific Access Point

To make a connection using a specific access point:

1.  Scan nearby access points using the `ScanAsync()` method of the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class, and select the one you want:

    ```
    try
    {
        string ap = "APName";
        WiFiAP connectAP;
        await WiFiManager.ScanAsync();
        var apList = WiFiManager.GetFoundAPs();
        foreach (var item in apList)
        {
            if (item.NetworkInformation.Essid == ap)
            {
                connectAP = item;
                break;
            }
        }
    }
    catch (Exception e)
    {
         Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

2. Establish a connection with the selected access point:

    ```
    try
    {
        await connectAP.ConnectAsync();
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

3. Check whether the connection has been established successfully:

    ```
    try
    {
        WiFiAP connect = WiFiManager.GetConnectedAP();
        if (connect.NetworkInformation.Essid == ap)
        {
            Console.WriteLine("Connection is successful");
        }
    }
    catch (Exception e)
    {
        Console.WriteLine("Exception occurred" + e.ToString());
    }
    ```

<a name="deactivating_wifi_device"></a>
## Deactivating a Wi-Fi Device

To deactivate Wi-Fi when it is no longer needed (or the application is exiting), use the asynchronous `DeactivateAsync()` method of the [Tizen.Network.WiFi.WiFiManager](https://developer.tizen.org/dev-guide/csapi/api/Tizen.Network.WiFi.WiFiManager.html) class:

```
try
{
    await WiFiManager.DeactivateAsync();
}
catch (Exception e)
{
    Console.WriteLine("Exception occurred" + e.ToString());
}
```


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
