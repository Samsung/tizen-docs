# Wi-Fi


You can connect to a Wireless Local Area Network (WLAN) and transfer data over the network. The Wi-Fi Manager enables your application to activate and deactivate a local Wi-Fi device, and to connect to a WLAN network in the infrastructure mode.

The main features of the Wi-Fi Manager API include:

- Wi-Fi device and connection management

  You can to implement and manage Wi-Fi connections with the Wi-Fi Manager API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__MODULE.html) applications). For example, you can [activate or deactivate](#activate) a local Wi-Fi device, [connect to an access point](#connect) asynchronously, and [scan for available access points](#scan) and retrieve information from the found access points.

- <a name="ap"></a>Access point management

  You can connect to a specific access point (AP) with the Access Point API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__MODULE.html) applications). The infrastructure mode is used to connect to a wireless local area network (WLAN). The infrastructure mode requires a wireless AP. To connect to a WLAN, a client must be configured to use the same service set identifier (SSID) as the AP.

  To manage APs, you must create an AP handle (`wifi_manager_ap_h`), which allows you to retrieve Wi-Fi network and security information:

  - Network information details, such as the SSID, frequency band, and maximum speed of the access point, are available through the Network Information API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__NETWORK__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__NETWORK__MODULE.html) applications).

  - Security information details, such as the used encryption type and whether WPS is supported, are available through the Security Information API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__SECURITY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__SECURITY__MODULE.html) applications).

    You can also obtain EAP information through the EAP API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__SECURITY__EAP__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__AP__SECURITY__EAP__MODULE.html) applications).

- Wi-Fi state monitoring

  You can register a callback with the Wi-Fi Monitor API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__MONITOR__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__MONITOR__MODULE.html) applications) to monitor the Wi-Fi connection state changes. The supported states are defined in the `wifi_manager_connection_state_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__MONITOR__MODULE.html#gafa0bc807592532fbd1fa3a4df82b24b2) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__MONITOR__MODULE.html#gafa0bc807592532fbd1fa3a4df82b24b2) applications).

  You can also register callbacks for monitoring changes in the Wi-Fi device state (whether Wi-Fi is activated) and the RSSI level of the Wi-Fi connection.

> **Note**
>
> You can test the Wi-Fi functionality only on a target device. The emulator does not support this feature.

## Prerequisites

To enable your application to use the Wi-Fi functionality:

1. To use the Wi-Fi Manager API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__WIFI__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
      <privilege>http://tizen.org/privilege/network.set</privilege>
      <privilege>http://tizen.org/privilege/network.profile</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Wi-Fi Manager API, include the `<wifi-manager.h>` header file in your application:

   ```
   #include <wifi-manager.h>
   ```

3. To be able to use all Wi-Fi functions, initialize Wi-Fi using the `wifi_manager_initialize()` function:

   ```
   int error_code;

   error_code = wifi_manager_initialize(wifi);
   if (error_code != WIFI_ERROR_NONE)
       return;
   ```

4. When Wi-Fi is no longer needed or the application is exiting, release Wi-Fi:

   ```
   wifi_manager_deinitialize(wifi);
   ```

> **Note**
>
> The Wi-Fi feature is not thread-safe and depends on the ecore main loop. Implement Wi-Fi within the ecore main loop, and do not use it in a thread.

<a name="activate"></a>
## Activating a Wi-Fi Device

To activate and deactivate a local Wi-Fi device, and to check that Wi-Fi is activated:

1. Activate a Wi-Fi device using the `wifi_manager_activate()` function:

    ```
    error_code = wifi_manager_activate(wifi, __wifi_manager_activated_cb, NULL);
    ```
    Define the `__wifi_manager_activated_cb()` callback, which is invoked when the Wi-Fi activation is completed.

    In the following example, the callback prints an information message using the dlogutil tool:

    ```
    static void
    __wifi_manager_activated_cb(wifi_error_e result, void *user_data)
    {
        if (result == WIFI_ERROR_NONE)
            dlog_print(DLOG_INFO, LOG_TAG, "Success to activate Wi-Fi device!");
    }
    ```

2. Check the Wi-Fi connection using the `wifi_manager_is_activated()` function. The parameter indicates whether Wi-Fi is activated.

    ```
    bool wifi_manager_activated = false;
    wifi_manager_is_activated(wifi, &wifi_manager_activated);
    if (wifi_manager_activated)
        dlog_print(DLOG_INFO, LOG_TAG, "Success to get Wi-Fi device state.");
    else
        dlog_print(DLOG_INFO, LOG_TAG, "Failed to get Wi-Fi device state.");
    ```

3. To deactivate the Wi-Fi device when Wi-Fi is no longer needed (or the application is exiting), use the `wifi_manager_deactivate()` function:

   ```
   wifi_manager_deactivate(wifi, NULL, NULL);
   ```

<a name="scan"></a>
## Scanning for Access Points

To scan nearby access points and print the scanning result, such as the AP name and state:

1. Scan nearby access points asynchronously:

   ```
   wifi_manager_scan(wifi, __scan_request_cb, NULL);
   ```

2. Define a callback, which is invoked when the scan is finished.

   In the following example, the callback calls the `wifi_manager_foreach_found_ap()` function for getting information on the found AP. The `wifi_manager_foreach_found_ap()` function gets the result of the scan, and the `__wifi_manager_found_ap_cb()` callback is called for each found access point.

   ```
   void
   __scan_request_cb(wifi_error_e error_code, void *user_data)
   {
       error_code = wifi_manager_foreach_found_ap(wifi, __wifi_manager_found_ap_cb, NULL);
       if (error_code != WIFI_ERROR_NONE)
           dlog_print(DLOG_INFO, LOG_TAG, "Failed to scan");
   }
   ```

3. Show the result of the scan using the `__wifi_manager_found_ap_cb()` callback.

    In the following example, the callback prints the AP name and connection state:

    ```
    bool
    __wifi_manager_found_ap_cb(wifi_ap_h ap, void *user_data)
    {
        int error_code = 0;
        char *ap_name = NULL;
        wifi_connection_state_e state;

        error_code = wifi_manager_ap_get_essid(ap, &ap_name);
        if (error_code != WIFI_ERROR_NONE) {
            dlog_print(DLOG_INFO, LOG_TAG, "Failed to get AP name.");

            return false;
        }
        error_code = wifi_manager_ap_get_connection_state(ap, &state);
        if (error_code != WIFI_ERROR_NONE) {
            dlog_print(DLOG_INFO, LOG_TAG, "Failed to get state.");

            return false;
        }
        dlog_print(DLOG_INFO, LOG_TAG, "AP name: %s, state: %s", ap_name, print_state(state));

        return true;
    }

    static const char*
    print_state(wifi_connection_state_e state)
    {
        switch (state) {
        case WIFI_CONNECTION_STATE_DISCONNECTED:
            return "Disconnected";
        case WIFI_CONNECTION_STATE_ASSOCIATION:
            return "Association";
        case WIFI_CONNECTION_STATE_CONNECTED:
            return "Connected";
        case WIFI_CONNECTION_STATE_CONFIGURATION:
            return "Configuration";
        }
    }
    ```

	You can get other information, including frequency, IP address, and security type. For more information, see [access point management](#ap).

<a name="connect"></a>
## Connecting to a Specific Access Point

To make a connection using a specific access point:

1. Select an access point.

   Check whether Wi-Fi is activated using the `wifi_manager_is_activated()` function, and receive the specific AP name from the user. Call the `wifi_manager_foreach_found_ap()` function to compare the AP name with the result of the scan:

   ```
   char ap_name[33];
   bool state = false;

   wifi_manager_is_activated(wifi, &state);
   if (state == false)
       return -1;

   dlog_print(DLOG_INFO, LOG_TAG, "Input a part of AP name to connect: ");
   error_code = scanf("%32s", ap_name);

   error_code = wifi_manager_foreach_found_ap(wifi, __found_connect_ap_cb, ap_name);
   if (error_code != WIFI_ERROR_NONE) {
       dlog_print(DLOG_INFO, LOG_TAG, "Failed to connect (can't get AP list)");

       return -1;
   }

   dlog_print(DLOG_INFO, LOG_TAG, "Connection step finished");
   ```

2. Make a connection with an access point.

   Define the `__found_connect_ap_cb()` callback invoked by the `wifi_manager_foreach_found_ap()` function.

   The callback compares `user_data` (the AP name from the user input) with the name of the found AP. If it is correct, the function checks whether the AP requires a passphrase. Set the passphrase using the `wifi_manager_ap_set_passphrase()` function.

   Finally, connect to a specific AP using the `wifi_manager_connect()` function.

   ```
   static bool
   __found_connect_ap_cb(wifi_ap_h ap, void *user_data)
   {
       int error_code = 0;
       char *ap_name = NULL;
       char *ap_name_part = (char*)user_data;

       error_code = wifi_manager_ap_get_essid(ap, &ap_name);
       if (error_code != WIFI_ERROR_NONE) {
           dlog_print(DLOG_INFO, LOG_TAG, "Failed to get AP name");

           return false;
       }

       if (strstr(ap_name, ap_name_part) != NULL) {
           bool required = false;

           if (wifi_manager_ap_is_passphrase_required(ap, &required) == WIFI_ERROR_NONE)
               dlog_print(DLOG_INFO, LOG_TAG, "Passphrase required: %s", required ? "True" : "False");
           else
               dlog_print(DLOG_INFO, LOG_TAG, "Failed to get Passphrase required");

           if (required) {
               char passphrase[100];
               dlog_print(DLOG_INFO, LOG_TAG, "Input passphrase for %s: ", passphrase);
               error_code = scanf("99%s", passphrase);

               error_code = wifi_manager_ap_set_passphrase(ap, passphrase);
               if (error_code != WIFI_ERROR_NONE) {
                   dlog_print(DLOG_INFO, LOG_TAG, "Failed to set passphrase");

                   return false;
               }
           }

           error_code = wifi_manager_connect(wifi, ap, __connected_cb, NULL);
           if (error_code != WIFI_ERROR_NONE)
               dlog_print(DLOG_INFO, LOG_TAG, "Failed in connection request");
           else
               dlog_print(DLOG_INFO, LOG_TAG, "Success in connection request");

           free(ap_name);

           return false;
       }

       free(ap_name);

       return true;
   }
   ```

3. Provide a notification about the connection result.

   The `wifi_manager_connect()` function called within the `__found_connect_ap_cb()` callback invokes the `__connected_cb()` function, which you can use to notify the user of the connection result:

   ```
   static void
   __connected_cb(wifi_error_e result, void* user_data)
   {
       if (result == WIFI_ERROR_NONE)
           dlog_print(DLOG_INFO, LOG_TAG, "Wi-Fi Connection Succeeded");
       else
           dlog_print(DLOG_INFO, LOG_TAG, "Wi-Fi Connection Failed!");
   }
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
