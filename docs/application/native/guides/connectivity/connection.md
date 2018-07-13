# Connection Management


You can create a network connection in your application, and use it to perform various operations. The application can access connection details, such as the IP address, proxy information, gateway information, and connection statistics. It can also manage [IP sockets](#socket).

The main features of the Connection API include:

- Managing connections

  You can establish and manage various data connections using a connection handle, which is created with the `connection_create()` function of the Connection Manager API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) applications). You can use the handle to:

  - [Get a state of the connection interface](#detail).

    You can access the state of the Bluetooth, cellular, and Wi-Fi connections only. Use the `connection_get_[interface]_state()` function to retrieve the state as the `connection_bt_state_e` (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gaf4abc0a653145fb9dec7e885c9081395) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gaf4abc0a653145fb9dec7e885c9081395) applications), `connection_cellular_state_e` (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga9ca508e61d795be15ee1795581a66396) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga9ca508e61d795be15ee1795581a66396) applications), or `connection_wifi_state_e` (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gab3ad7fdb200354b3c34878d88fc97dcd) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gab3ad7fdb200354b3c34878d88fc97dcd) applications) enumerator.

  - Access various network details, such as the IP address, proxy, and gateway information.

    You can use the `connection_address_family_e` enumerator in ([mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html#ga5910989495b39e8c4dbbd05ec9482d19) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html#ga5910989495b39e8c4dbbd05ec9482d19) applications) to get the IPv4 or IPv6 address family. You can use it as a parameter when you retrieve the IP address of the current connection or proxy.

  - [Register property change callbacks](#register).

  - Create a `connection_profile_h` profile handle, which provides information according to the connection type.

- Mapping connection profiles

  You can map a connection profile to retrieve details about specific connections, using the Connection Profile API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html) applications).

  Each connection profile is defined by a set of configuration information defined in the `connection_profile_h` handle. The profile provides different information according to the connection type (such as Bluetooth, cellular, Ethernet, and Wi-Fi). You can access various profile details, such as the state, type, and name with the `connection_profile_get_XXX()` functions.

  The Connection Profile API has child APIs for cellular and Wi-Fi profiles:

  - To manage a cellular profile, use the Cellular Profile API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__CELLULAR__PROFILE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__CELLULAR__PROFILE__MODULE.html) applications). You can access and modify various cellular connection details.
  - To manage a Wi-Fi profile, use the Wi-Fi Profile API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__WIFI__PROFILE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__WIFI__PROFILE__MODULE.html) applications). You can access various Wi-Fi connection details, and set a passphrase for the WPA (Wi-Fi Protected Access).

- Gathering statistics

  You can [gather various statistics on the network usage](#info), such as the amounts of sent and received data, using the Connection Statistics API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html) and [wearable](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html) applications). You can also retrieve the cumulative size of packets sent or received since the last reset based on the operation mode, such as packet switching (PS). To define the specific type of statistics information you want, use the `connection_statistics_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63) applications).

  > **Note**
  >
  > Statistics are supported for Wi-Fi and cellular connections only.

  You can re-initialize the statistics with the `connection_reset_statistics()` function.

<a name="socket"></a>
## IP Sockets

The Connection Manager API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html) applications) is related to [libcurl](http://curl.haxx.se/libcurl/) (see the [Curl](curl_n.htm) guide) and sockets. After a network connection is established, you can create a socket on the kernel Linux stack to be used directly or by libcurl or any other network library. If you want to create a socket directly without libcurl, you must check whether you are using the IPv4 or IPv6 environment, and create an applicable IP socket.

To manage IP sockets, you can:

1. [Initialize a socket](#socket_init) for use and check the default connection.
2. [Change the connection profile manually](#socket_profile) to use the connection you want instead of the default connection.
3. [Retrieve the IP address family for a client-side socket](#socket_family) or [for a server-side socket](#socket_familyserver).
4. [Create the client-side socket, and communicate with the remote host](#socket_create), or [create the server-side socket, and communicate with the client](#socket_createserver).
5. [Close the socket](#socket_close) and release the resources.

> **Note**
>
> To handle HTTP and HTTPS requests in a proxy environment, [get the proxy address](#detail) using the Connection Manager and then set the proxy address using the Connection Profile API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html) applications).
>
> For libcurl, you can [use the `CURLOPT_PROXY` option](curl.md#manage).

<a name="prerequisites"></a>
## Prerequisites

To enable your application to use the connection functionality:

1. To use the Connection API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
      <privilege>http://tizen.org/privilege/network.set</privilege>
      <privilege>http://tizen.org/privilege/network.profile</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Connection API, include the `<net_connection.h>` header file in your application:

   ```
   #include <net_connection.h>
   ```

3. To be able to use all connection functions, you must create a handle that contains information about the connection. Use the `connection` static variable that stores the connection handle.

   ```
   static connection_h connection;
   ```

   Create the connection handle using the `connection_create()` function that allows you to obtain the connection state and data transfer information:

   ```
   int error_code;

   error_code = connection_create(&connection);
   if (error_code != CONNECTION_ERROR_NONE)
       return;
   ```

4. When no longer needed, destroy the created connection handle:

   ```
   connection_destroy(connection);
   ```

<a name="detail"></a>
## Getting Network Connection Details

To get the type of the current connection, IP address, and proxy information:

1. To get the type of the current profile for data connection, use the `connection_get_type()` function. The second parameter is the network type defined in the `connection_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee) applications).

    ```
    int error_code;
    connection_type_e net_state;
    error_code = connection_get_type(connection, &net_state);
    if (error_code == CONNECTION_ERROR_NONE)
        dlog_print(DLOG_INFO, LOG_TAG, "Network connection type: %d", net_state);
    ```

	To monitor changes in the connection type, register and define a callback:

    ```
    connection_set_type_changed_cb(connection, __connection_changed_cb, NULL);

    static void
    __connection_changed_cb(connection_type_e type, void* user_data)
    {
        dlog_print(DLOG_INFO, LOG_TAG, "Type changed callback, connection type: %d", type);
    }
    ```

2. To get the connection IPv4 address, use the `connection_get_ip_address()` function. The Connection API supports both IPv4 and IPv6, as defined in the `connection_address_family_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html#ga5910989495b39e8c4dbbd05ec9482d19) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__PROFILE__MODULE.html#ga5910989495b39e8c4dbbd05ec9482d19) applications).

    The IP address can be printed using the dlog util tool (as in the following example), or shown to the user in another way. Free the memory allocated for the `ip_addr` temporary variable.
    ```
    char *ip_addr = NULL;
    error_code = connection_get_ip_address(connection, CONNECTION_ADDRESS_FAMILY_IPV4,
                                           &ip_addr);
    if (error_code == CONNECTION_ERROR_NONE) {
        dlog_print(DLOG_INFO, LOG_TAG, "IP address: %s", ip_addr);
        free(ip_addr);
    }
    ```
3. To get the connection proxy information, use the `connection_get_proxy()` function. The following example prints the proxy address using the dlog util tool.

    Free the memory allocated for the `proxy_addr` variable.
    ```
    error_code = connection_get_proxy(connection, address_family, &proxy_addr);
    if (error_code == CONNECTION_ERROR_NONE) {
        dlog_print(DLOG_INFO, LOG_TAG, "Proxy address: %s", proxy_addr);
        free(proxy_addr);
    }
    ```

<a name="info"></a>
## Getting Connection Information

To obtain cellular and Wi-Fi connection information with data transfer statistics, such as the amount of total sent or received data and last sent or received data (only cellular and Wi-Fi statistics information is supported):

1. To get the cellular connection state, use the `connection_get_cellular_state()` function. The function fills the second parameter with the current state, whose possible values are defined in the `connection_cellular_state_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga9ca508e61d795be15ee1795581a66396) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga9ca508e61d795be15ee1795581a66396) applications).

    In the following example, a `switch` statement is used to show the cellular state:
    ```
    connection_cellular_state_e cellular_state;
    connection_get_cellular_state(connection, &cellular_state);
    switch (cellular_state) {
    case CONNECTION_CELLULAR_STATE_OUT_OF_SERVICE:
        dlog_print(DLOG_INFO, LOG_TAG, "Out of service");
        break;
    case CONNECTION_CELLULAR_STATE_FLIGHT_MODE:
        dlog_print(DLOG_INFO, LOG_TAG, "Flight mode");
        break;
    case CONNECTION_CELLULAR_STATE_ROAMING_OFF:
        dlog_print(DLOG_INFO, LOG_TAG, "Roaming is turned off");
        break;
    case CONNECTION_CELLULAR_STATE_CALL_ONLY_AVAILABLE:
        dlog_print(DLOG_INFO, LOG_TAG, "Call only");
        break;
    case CONNECTION_CELLULAR_STATE_AVAILABLE:
        dlog_print(DLOG_INFO, LOG_TAG, "Available");
        break;
    case CONNECTION_CELLULAR_STATE_CONNECTED:
        dlog_print(DLOG_INFO, LOG_TAG, "Connected");
        break;
    default:
        dlog_print(DLOG_INFO, LOG_TAG, "error");
        break;
    }
    ```

2. To get the Wi-Fi connection state, use the `connection_get_wifi_state()` function. The function fills the second parameter with the current state, whose possible values are defined in the `connection_wifi_state_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gab3ad7fdb200354b3c34878d88fc97dcd) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#gab3ad7fdb200354b3c34878d88fc97dcd) applications).

    In the following example, a `switch` statement is used to show the Wi-Fi state:
    ```
    connection_wifi_state_e wifi_state;
    connection_get_wifi_state(connection, &wifi_state);
    switch (wifi_state) {
    case CONNECTION_WIFI_STATE_DEACTIVATED:
        dlog_print(DLOG_INFO, LOG_TAG, "Deactivated state");
        break;
    case CONNECTION_WIFI_STATE_DISCONNECTED:
        dlog_print(DLOG_INFO, LOG_TAG, "Disconnected state");
        break;
    case CONNECTION_WIFI_STATE_CONNECTED:
        dlog_print(DLOG_INFO, LOG_TAG, "Connected state");
        break;
    default:
        dlog_print(DLOG_INFO, LOG_TAG, "error");
        break;
    }
    ```

3. To get connection statistics, use the `connection_get_statistics()` function.

    Connection statistics include the amount of total sent and received data and the last sent and received data. The function parameters determine which statistics are received, and for which connection type:
    - The second parameter defines the connection type using the `connection_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__MANAGER__MODULE.html#ga85c33901b8ac24f2e5f66440ec4519ee) applications).

    - The third parameter defines the statistic type using the `connection_statistics_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__STATISTICS__MODULE.html#ga24b29d70490e8cd9ee34f45615ea1c63) applications).

    The following example reads all statistics for cellular and Wi-Fi connections:
    ```
    long long last_received_size;
    error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                           CONNECTION_STATISTICS_TYPE_LAST_RECEIVED_DATA,
                                           &last_received_size);
    /* Handle statistics */

    long long last_sent_size;
    error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                           CONNECTION_STATISTICS_TYPE_LAST_SENT_DATA,
                                           &last_sent_size);
    /* Handle statistics */

    long long total_received_size;
    error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                           CONNECTION_STATISTICS_TYPE_TOTAL_RECEIVED_DATA,
                                           &total_received_size);
    /* Handle statistics */

    long long total_sent_size;
    error_code = connection_get_statistics(connection, CONNECTION_TYPE_CELLULAR,
                                           CONNECTION_STATISTICS_TYPE_TOTAL_SENT_DATA,
                                           &total_sent_size);
    /* Handle statistics */

    error_code = connection_get_statistics(connection, CONNECTION_TYPE_WIFI,
                                           CONNECTION_STATISTICS_TYPE_LAST_RECEIVED_DATA,
                                           &last_received_size);
    /* Handle statistics */

    error_code = connection_get_statistics(connection, CONNECTION_TYPE_WIFI,
                                           CONNECTION_STATISTICS_TYPE_LAST_SENT_DATA,
                                           &last_sent_size);
    /* Handle statistics */

    error_code = connection_get_statistics(connection, CONNECTION_TYPE_WIFI,
                                           CONNECTION_STATISTICS_TYPE_TOTAL_RECEIVED_DATA,
                                           &total_received_size);
    /* Handle statistics */

    error_code = connection_get_statistics(connection, CONNECTION_TYPE_WIFI,
                                           CONNECTION_STATISTICS_TYPE_TOTAL_SENT_DATA,
                                           &total_sent_size);
    /* Handle statistics */
    ```

<a name="register"></a>
## Registering Property Change Callbacks

To register callback functions that are called when information changes:

1. Define callback functions.

   In this use case, the registered callbacks are the `__ip_changed_cb()` and `__proxy_changed_cb()` functions, used for address changes. When an address changes, an information message is printed in the file (or shown to the user in another way). The message contains information on which address has been changed and what the new value is.

   ```
   static void
   __ip_changed_cb(const char* ipv4_address, const char* ipv6_address, void* user_data)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "%s callback, IPv4 address: %s, IPv6 address: %s",
                  (char *)user_data, ipv4_address, (ipv6_address ? ipv6_address : "NULL"));
   }

   static void
   __proxy_changed_cb(const char* ipv4_address, const char* ipv6_address, void* user_data)
   {
       dlog_print(DLOG_INFO, LOG_TAG, "%s callback, IPv4 address: %s, IPv6 address: %s",
                  (char *)user_data, ipv4_address, (ipv6_address ? ipv6_address : "NULL"));
   }
   ```

2. Register the defined callback functions.

   You have to register the previously defined callback functions using the `connection_set_ip_address_changed_cb()` and `connection_set_proxy_address_changed_cb()` functions. The last parameter (`user_data`) is set to a message which is printed in the callback.

   ```
   error_code = connection_set_ip_address_changed_cb(connection, __ip_changed_cb,
                                                     "IP addr changed:");
   if (error_code != CONNECTION_ERROR_NONE)
       /* Error handling */

   error_code = connection_set_proxy_address_changed_cb(connection, __proxy_changed_cb,
                                                        "Proxy IP addr changed:");
   if (error_code != CONNECTION_ERROR_NONE)
       /* Error handling */
   ```

3. Deregister the callback functions.

   When the callbacks are no longer needed, deregister them with the applicable unset functions:

   ```
   error_code = connection_unset_ip_address_changed_cb(connection);
   if (error_code != CONNECTION_ERROR_NONE)
       /* Error handling */

   error_code = connection_unset_proxy_address_changed_cb(connection);
   if (error_code != CONNECTION_ERROR_NONE)
       /* Error handling */
   ```

<a name="socket_init"></a>
## Initializing a Socket

To initialize a client or server-side socket for use:

1. To use the functions and data types of the Socket API, include the following header files in your application:

   ```
   #include <sys/stat.h>
   #include <arpa/inet.h>
   #include <netdb.h>
   #include <net/if.h>
   ```

2. Declare the necessary variables:

   ```
   int
   main(int argc, char **argv)
   {
       int rv = 0;
       int ip_type = -1;
       char user_url[100] = {0,};
       char user_port[10] = {0,};
       char user_msg[200] = {0,};
       char *local_ipv4 = NULL;
       char *local_ipv6 = NULL;
       char *interface_name = NULL;

       connection_type_e net_state;
       connection_h connection = NULL;
       connection_profile_h profile_h = NULL;
   ```

3. [Include the required header file and create a connection handle](#prerequisites).

4. Check whether the default connection is available:

   ```
       connection_type_e net_state;

       rv = connection_get_type(connection, &net_state);
       if (rv != CONNECTION_ERROR_NONE || net_state == CONNECTION_TYPE_DISCONNECTED) {
           dlog_print(DLOG_INFO, LOG_TAG, "Not connected %d\n", rv);
           connection_destroy(connection);

           return -1;
       }
   ```

5. Check the address type of the default connection.

   The address type can be IPv4 or IPv6.

   ```
       int ip_type = -1;
       char *local_ipv4 = NULL;
       char *local_ipv6 = NULL;
       connection_profile_h profile_h = NULL;

       rv = connection_get_current_profile(connection, &profile_h);
       if (rv != CONNECTION_ERROR_NONE) {
           dlog_print(DLOG_INFO, LOG_TAG, "Failed to get profile handle %d\n", rv);
           connection_destroy(connection);

           return -1;
       }

       rv = connection_profile_get_ip_address(profile_h, CONNECTION_ADDRESS_FAMILY_IPV6,
                                              &local_ipv6);
       if (rv == CONNECTION_ERROR_NONE && g_strcmp0(local_ipv6, "::") != 0) {
           ip_type = CONNECTION_ADDRESS_FAMILY_IPV6;
           dlog_print(DLOG_INFO, LOG_TAG, "IPv6 address: %s\n", local_ipv6);
       }

       /* If both IPv4 and IPv6 types are set, the IPv4 type is used as default here */
       rv = connection_profile_get_ip_address(profile_h, CONNECTION_ADDRESS_FAMILY_IPV4,
                                              &local_ipv4);
       if (rv == CONNECTION_ERROR_NONE && g_strcmp0(local_ipv4, "0.0.0.0") != 0) {
           ip_type = CONNECTION_ADDRESS_FAMILY_IPV4;
           dlog_print(DLOG_INFO, LOG_TAG, "IPv4 address: %s\n", local_ipv4);
       }

       if (ip_type != CONNECTION_ADDRESS_FAMILY_IPV6
           && ip_type != CONNECTION_ADDRESS_FAMILY_IPV4) {
           dlog_print(DLOG_INFO, LOG_TAG, "No IP address!\n");
           /* Error handling */
       }

       connection_profile_get_network_interface_name(profile_h, &interface_name);
       dlog_print(DLOG_INFO, LOG_TAG, "Interface Name: %s\n", interface_name);
   }
   ```

<a name="socket_profile"></a>
## Changing the Connection Profile

When you use a socket, it is automatically bound with the network interface of the default connection profile. For example, if the device is connected to the Wi-Fi network, Wi-Fi is the default network. To use another network, you must open the applicable connection profile.

You can open the connection profile manually in 2 ways:

- Use the `connection_get_profile_iterator()` function to retrieve all available profiles, and select the profile you want.
- Use the `connection_get_default_cellular_service_profile()` function to retrieve the connection profile of a specific cellular service.

  This use case covers this way of opening the profile.

To change the connection profile:

1. To get the default cellular profile, call the `connection_get_default_cellular_service_profile()` function. As the second parameter, define the cellular service type, whose available values are defined in the `connection_cellular_service_type_e`enumerator (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__CONNECTION__CELLULAR__PROFILE__MODULE.html#ga0c60b4110e648d6cb64f35348037a9ff) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__CONNECTION__CELLULAR__PROFILE__MODULE.html#ga0c60b4110e648d6cb64f35348037a9ff) applications):
    ```
    int rv;
    rv = connection_get_default_cellular_service_profile(connection,
                                                         CONNECTION_CELLULAR_SERVICE_TYPE_INTERNET,
                                                         &profile);
    if (ret != CONNECTION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to get default cellular service profile\n");
    ```

2. Open the profile with the `connection_open_profile()` function and define a callback, which is called after the profile is opened:
    ```
    rv = connection_open_profile(connection, profile, test_connection_opened_callback, NULL);
    if (rv != CONNECTION_ERROR_NONE)
        dlog_print(DLOG_ERROR, LOG_TAG, "Failed to open profile\n");
    ```

3. If the callback function is invoked with a success result, refresh the profile and get the interface name of the opened profile.

   The interface name is used to bind with a socket manually. For binding, use a general socket or HTTP APIs. In this example, libcurl is used. After the `curl_easy_perform()` function is called, data is transported through the specified network interface.

   ```
   static void
   test_connection_opened_callback(connection_error_e result, void* user_data)
   {
       int rv;
       char *interface_name;
       CURL *curl;
       CURLcode res;

       if (result == CONNECTION_ERROR_NONE) {
           /* Refresh the profile */
           rv = connection_profile_refresh(profile);
           if (rv != CONNECTION_ERROR_NONE) {
               dlog_print(DLOG_ERROR, LOG_TAG, "Failed to refresh profile\n");

               return;
           }

           /* Get the interface name */
           rv = connection_profile_get_network_interface_name(profile, &interface_name);
           if (rv != CONNECTION_ERROR_NONE) {
               dlog_print(DLOG_ERROR, LOG_TAG, "Fail to get interface name!\n");

               return;
           }

           dlog_print(DLOG_ERROR, LOG_TAG, "Interface name(%s)\n", interface_name);
           curl = curl_easy_init();
           if (curl) {
               curl_easy_setopt(curl, CURLOPT_URL, "https://www.tizen.org");
               /* Bind the interface name with the socket */
               curl_easy_setopt(curl, CURLOPT_INTERFACE, interface_name);

               res = curl_easy_perform(curl);
               if (res != CURLE_OK)
                   dlog_print(DLOG_ERROR, LOG_TAG, "curl_easy_perform() failed");

               curl_easy_cleanup(curl);
           }
       }

       dlog_print(DLOG_ERROR, LOG_TAG, "Failed to open profile");

       return;
   }
   ```

<a name="socket_family"></a>
## Retrieving the Address Family for a Client-side Socket

To get the hostname IP addresses to connect to the server-side socket:

1. Define the user URL and message to be sent.

2. Retrieve the IP addresses:

   ```
   {
       struct sockaddr_in6 *addr6;
       struct addrinfo hints;
       struct addrinfo *result;
       char user_url[100] = {0,};
       char user_port[10] = {0,};

       memset(&hints, 0x00, sizeof(struct addrinfo));

       hints.ai_family = PF_UNSPEC;
       hints.ai_socktype = SOCK_STREAM;
       hints.ai_protocol = IPPROTO_TCP;

       if (getaddrinfo(user_url, user_port, &hints, &result) != 0) {
           dlog_print(DLOG_INFO, LOG_TAG, "getaddrinfo() error\n");
           /* Error handling */
       }
   }
   ```

<a name="socket_familyserver"></a>
## Retrieving the Address Family for a Server-side Socket

To get the hostname IP addresses to connect:

```
struct addrinfo hints;
struct addrinfo *result;
struct addrinfo *rp;

char buf[257];
int sockfd = -1;
int csockfd = -1;
int count = 0;
int rwcount = 0;

memset(&hints, 0x00, sizeof(struct addrinfo));

hints.ai_flags = AI_PASSIVE;
hints.ai_family = PF_UNSPEC;
hints.ai_socktype = SOCK_STREAM;

if (getaddrinfo(default_ip, argv[1], &hints, &result) != 0) {
    printf("getaddrinfo() error\n");
    goto done;
}
```

<a name="socket_create"></a>
## Creating the Client-side Socket and Managing the Remote Host Connection

To create the socket and connect to a remote host:

1. Find the proper address family and create the socket:

   ```
   int sockfd = -1;
   struct addrinfo *rp;

   rp = result;

   for (rp = result; rp != NULL; rp = rp->ai_next) {
       if (rp->ai_family == AF_INET && ip_type == CONNECTION_ADDRESS_FAMILY_IPV4) {
           if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
               dlog_print(DLOG_INFO, LOG_TAG, "socket error\n");
               freeaddrinfo(result);
           }
           dlog_print(DLOG_INFO, LOG_TAG, "IPv4\n");
       } else if (rp->ai_family == AF_INET6 && ip_type == CONNECTION_ADDRESS_FAMILY_IPV6) {
           if ((sockfd = socket(AF_INET6, SOCK_STREAM, 0)) < 0) {
               dlog_print(DLOG_INFO, LOG_TAG, "socket error\n");
               freeaddrinfo(result);
           }
           dlog_print(DLOG_INFO, LOG_TAG, "IPv6\n");
       }
   }
   ```

2. Connect to the remote host:

   - Use the IPv4 socket:

     ```
     if (connect(sockfd, rp->ai_addr, rp->ai_addrlen) < 0) {
         dlog_print(DLOG_INFO, LOG_TAG, "connect() error: %s\n", strerror(errno));
         freeaddrinfo(result);
         close(sockfd);
     }
     ```

   - Use the IPv6 socket.

     The interface index is needed for the IPv6 connection.

     ```
     char *interface_name = NULL;

     connection_profile_get_network_interface_name(profile_h, &interface_name);
     dlog_print(DLOG_INFO, LOG_TAG, "Interface Name: %s\n", interface_name);

     addr6 = (struct sockaddr_in6 *)rp->ai_addr;
     addr6->sin6_scope_id = if_nametoindex(interface_name);

     if ((sockfd = connect(sockfd, (struct sockaddr *)addr6, rp->ai_addrlen)) < 0) {
         dlog_print(DLOG_INFO, LOG_TAG, "connect() error: %s\n", strerror(errno));
         freeaddrinfo(result);
         close(sockfd);
     }
     ```

3. Manage messages:

   - Send a message to the remote host:

     ```
     if ((count = write(sockfd, user_msg, 200)) < 0) {
         dlog_print(DLOG_INFO, LOG_TAG, "write() error: %s\n", strerror(errno));

         freeaddrinfo(result);
         close(sockfd);
     }
     dlog_print(DLOG_INFO, LOG_TAG, "Sent count: %d, msg: %s\n", count, user_msg);
     ```

   - Read a message from the remote host:

     ```
     char buf[257];
     memset(buf, 0x00, 257);

     if ((count = read(sockfd, buf, 256)) < 0) {
         dlog_print(DLOG_INFO, LOG_TAG, "read() error: %s\n", strerror(errno));

         freeaddrinfo(result);
         close(sockfd);
     }
     buf[count] = '\0';
     dlog_print(DLOG_INFO, LOG_TAG, "\nRead: %s\n", buf);
     ```

<a name="socket_createserver"></a>
## Creating the Server-side Socket and Managing the Connection

To create the socket and manage the connection to a client:

1. Find the proper address family and create the socket:

   ```
   int sockfd = -1;
   struct addrinfo *rp;

   rp = result;

   for (rp = result; rp != NULL; rp = rp->ai_next) {
       if (rp->ai_family == AF_INET &&
           ip_type == CONNECTION_ADDRESS_FAMILY_IPV4) {
           if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
               printf("socket error\n");
               freeaddrinfo(result);
               goto done;
           }
           printf("IPv4\n");
       } else if (rp->ai_family == AF_INET6 &&
                ip_type == CONNECTION_ADDRESS_FAMILY_IPV6) {
           if ((sockfd = socket(AF_INET6, SOCK_STREAM, 0)) < 0) {
               printf("socket error\n");
               freeaddrinfo(result);
               goto done;
           }
           printf("IPv6\n");
       }
   }
   ```

2. Bind the found address:

   ```
   if (bind(sockfd, rp->ai_addr, rp->ai_addrlen) != 0) {
       printf("bind() error: %s\n", strerror(errno));

       freeaddrinfo(result);
       close(sockfd);

       goto done;
   }
   ```

3. Listen for client-side connections.

   Mark the `sockfd` socket as a passive socket.

   ```
   if (listen(sockfd, 5) != 0) {
       printf("listen() error: %s\n", strerror(errno));

       freeaddrinfo(result);
       close(sockfd);

       goto done;
   }
   ```

4. Manage messages:

   - Read a message from the client:

     ```
     char buf[257];
     memset(buf, 0x00, 257);

     if ((count = read(csockfd, buf, 256)) < 0) {
         printf("read() error: %s\n", strerror(errno));

         freeaddrinfo(result);
         close(sockfd);
         close(csockfd);
         goto done;
     }
     buf[count] = '\0';
     printf("\nRead: %s\n", buf);
     ```

   - Echo the received message back to the client:

     ```
     if ((count = write(csockfd, buf, 256)) < 0) {
         printf("write() error: %s\n", strerror(errno));

         freeaddrinfo(result);
         close(sockfd);
         close(csockfd);

         goto done;
     }

     printf("sent count: %d, msg: %s\n", count, buf);
     close(csockfd);
     ```

<a name="socket_close"></a>
## Closing the Socket

To close the client or server-side socket and release the resources:

```
freeaddrinfo(result);
close(sockfd);

done:
    connection_profile_destroy(profile_h);
    connection_destroy(connection);

    free(local_ipv6);
    free(local_ipv4);
    free(interface_name);

    return 0;
```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
