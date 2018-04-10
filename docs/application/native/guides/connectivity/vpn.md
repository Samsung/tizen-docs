# VPN Connections


A Virtual Private Network (VPN) connects 2 computers securely and privately over the internet. Using the VPN service, you can allow the users of your application to initialize the VPN device, and manage routing, DNS, and firewall features. A VPN connection consists of [multiple components](#components), mainly with the VPN server and client connecting over a tunnel.

This feature is supported in mobile applications only.

The main features of the VPN Service API include:

- VPN manager

  You can create or initialize the tunnel interface for the VPN device with various functions. The application can use those functions to [get various tunnel details](#get_param), such as the tunnel ID and tunnel name, MTU for the tunnel interface, and connection statistics.

  You can also [set various details](#set_param), such as the MTU for the tunnel interface, and the session name.

  The `vpnsvc_tun_s` structure contains detailed information about the tunnel interface, such as the ID, name, and MTU. The possible errors are defined with the [vpnsvc_error_e](../../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html#ga8d8e9c964218d7aad622115bb51491e8) enumerator.

  **Table: Common macros**

  | Macro                       | Description                |
  |-----------------------------|----------------------------|
  | `VPNSVC_IP4_STRING_LEN`     | IPv4 address string length |
  | `VPNSVC_VPN_IFACE_NAME_LEN` | VPN interface name length  |
  | `VPNSVC_SESSION_STRING_LEN` | Session name string length |

- VPN profile

  You can map the VPN profile and get details about the VPN service by using the [vpnsvc_h](../../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html#gaef3a3f46336ee7e8c43dd16144b22ac5) handle.

  The VPN profile provides different functions for routing management, DNS management, and firewall management:

  - The `vpnsvc_init()` function is used to a initialize the VPN interface and get the handle.
  - The `vpnsvc_h` handle is used to [configure the tunnel interface](#config) before using the [VPN application control](../app-management/common-appcontrol.md#vpnservice) to ask the user permission to connect to the VPN service.
  - The `vpnsvc_block_networks()` function is used to [block network traffic](#block) by creating a route parameter for allowed VPN and original interface routes.

- VPN statistics

  The VPN service allows you to [track data transfer information](#read). Use the VPN statistics to gather and reset statistics on network usage, such as the size of the sent or received data, in bytes:

  - The `vpnsvc_read()` function is used to read the data from tunnel interface in a specified time period.
  - The `vpnsvc_write()` function is used to write data to a tunnel file descriptor with a specific size.

The VPN service uses 2 mechanisms for managing access control between the application and service:

- Privilege:

  The application needs the partner level privilege for accessing the VPN service daemon.

- Application control:

  Connecting or disconnecting from a VPN network requires user permission, which is requested by invoking the VPN application control.

<a name="components"></a>
## VPN Connection Components

A VPN connection includes the following components:

- VPN server

  A computer that accepts VPN connections from VPN clients.

- VPN client

  A computer that initiates a VPN connection to a VPN server. A VPN client can be an individual computer or a router.

- Tunnel

  The portion of the connection in which your data is encapsulated.

- VPN connection

  The portion of the connection in which your data is encrypted. For typical secure VPN connections, the data is encrypted and encapsulated along the same portion of the connection.

- Tunneling protocols

  Protocols that are used to manage tunnels and encapsulate private data. Data that is tunneled must also be encrypted to be a VPN connection.

- Tunneled data

  Data that is usually sent across a private point-to-point link.

- Transit inter-network

  The shared or public network crossed by the encapsulated data. The transit inter-network can be the Internet or a private IP-based intranet.

## Prerequisites

To enable your application to use the VPN service functionality:

1. To use the [VPN Service](../../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html) API, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```
    <privileges>
       <privilege>http://developer.samsung.com/tizen/vpnservice</privilege>
    </privileges>
    ```

2. To use the functions and data types of the VPN Service API, include the `<vpn_service.h>` header file in your application:

    ```
    #include <vpn_service.h>
    ```

3. To be able to use all VPN functions, you must create a handle that contains information about the VPN. At the beginning, create a [vpnsvc_h](../../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html#gaef3a3f46336ee7e8c43dd16144b22ac5) type variable, which is a `void*` that stores the VPN handle.

    ```
    vpnsvc_h handle = NULL;
    ```

4. Create the VPN handle using the `vpnsvc_init()` function that allows you to obtain the VPN state and data transfer information:

    ```
    char *name = TEST_VPN_IF_NAME;
    int ret = VPNSVC_ERROR_NONE;

    ret = vpnsvc_init(name, &handle);

    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_init failed: %d\n", ret);
    ```

5. When the VPN handle is no longer needed, destroy it using the `vpnsvc_deinit()` function:

    ```
    if (handle)
        vpnsvc_deinit(handle);

    handle = NULL;
    ```

<a name="get_param"></a>
## Getting Interface Parameters

To get the interface parameters after successfully initializing the VPN service:

- Get the interface file descriptor using the `vpnsvc_get_iface_fd()` function:

    ```
    int int_value;

    if (vpnsvc_get_iface_fd(handle, &int_value) == VPNSVC_ERROR_NONE)
        printf("iface_fd: %d\n", int_value);
    ```

- Get the interface index using the `vpnsvc_get_iface_index()` function:

    ```
    int int_value;

    if (vpnsvc_get_iface_index(handle, &int_value) == VPNSVC_ERROR_NONE)
        printf("iface_index: %d\n", int_value);
    ```

- Get the interface name using the `vpnsvc_get_iface_name()` function:

    ```
    char *result_name = NULL;
    int ret = VPNSVC_ERROR_NONE;

    ret = vpnsvc_get_iface_name(handle, &result_name);
    if (ret == VPNSVC_ERROR_NONE)
        printf("iface_name: %s\n", result_name);
    ```

- Get the session for the interface using the `vpnsvc_get_session()` function:

    ```
    int ret = VPNSVC_ERROR_NONE;
    char *get_session = NULL;

    ret = vpnsvc_get_session(handle, &get_session);
    printf("Session Name = %s\n", get_session);
    printf("vpnsvc_set_session succeeded!\n");
    ```

<a name="set_param"></a>
## Setting Interface Parameters

To set the interface parameters:

- Set the MTU configuration for the tunnel interface using the `vpnsvc_set_mtu()` function, and update the value using the `vpnsvc_update_settings()` function:

    ```
    int ret;

    ret = vpnsvc_set_mtu(handle, 9000);
    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_set_mtu failed!\n");
    else
        printf("vpnsvc_set_mtu succeeded!\n");

    ret = vpnsvc_update_settings(handle);

    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_update_settings failed!\n");
    else
        printf("vpnsvc_update_settings succeeded!\n");
    ```

- Set the session name for the tunnel interface using the `vpnsvc_set_session()` function:

    ```
    char *set_session = "vpnsvc_test VPN Session";
    int ret;

    ret = vpnsvc_set_session(handle, set_session);
    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_set_session failed!\n");
    ```

<a name="config"></a>
## Configuring the Interface and Connecting to the Service

To configure the interface and connect to the VPN service through an application control:

1. Define a function to launch the [VPN application control](../app-management/common-appcontrol.md#vpnservice) and a callback to handle the results:

    ```
    #include <app_control.h>

    void
    launch_vpn_service_appcontrol(void)
    {
        app_control_h service;
        app_control_create(&service);

        app_control_set_operation(service, APP_CONTROL_OPERATION_SETTING_VPN);
        app_control_add_extra_data(service, APP_CONTROL_DATA_TYPE, "up");
        app_control_add_extra_data(service, APP_CONTROL_DATA_NAME, "tizen");
        app_control_set_launch_mode(service, APP_CONTROL_LAUNCH_MODE_GROUP);

        app_control_send_launch_request(service, vpn_appcontrol_result_cb, NULL);
        app_control_destroy(service);
    }

    static void
    vpn_appcontrol_result_cb(app_control_h request, app_control_h reply, app_control_result_e result, void *user_data)
    {
        char *result_txt;

        switch (result) {
        case APP_CONTROL_RESULT_APP_STARTED:
        case APP_CONTROL_RESULT_SUCCEEDED:
          dlog_print(DLOG_INFO, LOG_TAG, "Success!");
          break;
        case APP_CONTROL_RESULT_FAILED:
          dlog_print(DLOG_INFO, LOG_TAG, "Failed!");
          break;
        case APP_CONTROL_RESULT_CANCELED:
          dlog_print(DLOG_INFO, LOG_TAG, "Canceled!");
          break;
        }

        app_control_get_extra_data(reply, APP_CONTROL_DATA_TEXT, &result_txt);
        dlog_print(DLOG_INFO, LOG_TAG, "Result: %s", result_txt);
    }
    ```

2. Protect the underlying VPN traffic to be routed to the VPN itself by binding the socket to the underlying network interface, such as `wlan0`:

    ```
    int sock;
    int ret;

    ret = vpnsvc_protect(handle, sock, "wlan0");
    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_protect failed!\n");
    else
        printf("vpnsvc_protect succeeded!\n");
    ```

3. Set up the connection information, which includes the local IP address and the remote IP address:

   ```
   int ret;
   char local[VPNSVC_IP4_STRING_LEN] = {'\0',};
   char remote[VPNSVC_IP4_STRING_LEN] = {'\0',};

   if (!handle) {
       printf("invalid handle\n");

       return -1;
   }

   strncpy(local, "192.168.0.82", VPNSVC_IP4_STRING_LEN);
   strncpy(remote, "192.168.0.1", VPNSVC_IP4_STRING_LEN);

   /* Local IP address */
   ret = vpnsvc_set_local_ip_address(handle, local);

   if (ret != VPNSVC_ERROR_NONE)
       printf("vpnsvc_set_local_ip_address failed!\n");
   else
       printf("vpnsvc_set_local_ip_address succeeded!\n");

   /* Remote IP address */
   ret = vpnsvc_set_remote_ip_address(handle, remote);

   if (ret != VPNSVC_ERROR_NONE)
       printf("vpnsvc_set_remote_ip_address failed!\n");
   else
       printf("vpnsvc_set_remote_ip_address succeeded!\n");
   ```

4. Update the [vpnsvc_h](../../api/mobile/latest/group__CAPI__NETWORK__VPN__SERVICE__MODULE.html#gaef3a3f46336ee7e8c43dd16144b22ac5) handle with the connection information by calling the `vpnsvc_update_settings()` function:

    ```
    ret = vpnsvc_update_settings(handle);

    if (ret != VPNSVC_ERROR_NONE)
        printf("vpnsvc_update_settings failed!\n");
    else
        printf("vpnsvc_update_settings succeeded!\n");
    ```

5. Launch the application control to allow the user to connect to the VPN service:

   ```
   launch_vpn_service_appcontrol();
   ```

<a name="block"></a>
## Blocking and Unblocking Networks

To block or unblock the network:

- Block all traffic, except specified allowed networks, and send the specified UP addresses to a specified interface:

  ```
  char *block_nets[2];
  int block_prefix[2];
  int block_nr_nets = 2;
  char *allow_nets[2];
  int allow_prefix[2];
  int allow_nr_nets = 2;
  int ret;

  if (!handle) {
      printf("invalid handle\n");

      return -1;
  }

  block_nets[0] = malloc(sizeof(char) * VPNSVC_IP4_STRING_LEN);
  block_nets[1] = malloc(sizeof(char) * VPNSVC_IP4_STRING_LEN);
  memset(block_nets[0], 0, sizeof(char) * VPNSVC_IP4_STRING_LEN);
  memset(block_nets[1], 0, sizeof(char) * VPNSVC_IP4_STRING_LEN);
  strncpy(block_nets[0], "125.209.222.141", VPNSVC_IP4_STRING_LEN);
  block_prefix[0] = 32;
  strncpy(block_nets[1], "180.70.134.19", VPNSVC_IP4_STRING_LEN);
  block_prefix[1] = 32;

  allow_nets[0] = malloc(sizeof(char) * VPNSVC_IP4_STRING_LEN);
  allow_nets[1] = malloc(sizeof(char) * VPNSVC_IP4_STRING_LEN);
  memset(allow_nets[0], 0, sizeof(char) * VPNSVC_IP4_STRING_LEN);
  memset(allow_nets[1], 0, sizeof(char) * VPNSVC_IP4_STRING_LEN);
  strncpy(allow_nets[0], "216.58.221.142", VPNSVC_IP4_STRING_LEN);
  allow_prefix[0] = 32;
  strncpy(allow_nets[1], "206.190.36.45", VPNSVC_IP4_STRING_LEN);
  allow_prefix[1] = 32;

  ret = vpnsvc_block_networks(handle, block_nets, block_prefix, block_nr_nets,
                              allow_nets, allow_prefix, allow_nr_nets);

  if (ret != VPNSVC_ERROR_NONE)
      printf("vpnsvc_block_networks failed!\n");
  else
      printf("vpnsvc_block_networks succeeded!\n");
  ```

- Remove any restrictions from the VPN network:

  ```
  int ret;

  if (!handle) {
      printf("invalid handle\n");

      return -1;
  }

  ret = vpnsvc_unblock_networks(handle);

  if (ret != VPNSVC_ERROR_NONE)
      printf("vpnsvc_unblock_networks failed!\n");
  else
      printf("vpnsvc_unblock_networks succeeded!\n");
  ```

<a name="read"></a>
## Reading and Writing Data

To read or write data:

- Check whether there is data to read within a specified time period:

  ```
  int ret;
  int timeout_ms = 20;

  ret = vpnsvc_read(handle, timeout_ms);

  if (ret == VPNSVC_ERROR_NONE)
      printf("vpnsvc_read: Data available to read!\n");
  ```

- Write data directly to the underlying socket using a system call for performance. The number of bytes written is returned on success (the same as the system write call).

  ```
  int ret;
  char *message = "test message";

  ret = vpnsvc_write(handle, message, strlen(message));

  if (ret < 0)
      printf("vpnsvc_write: failed!\n");
  else if (ret == 0)
      printf("vpnsvc_write: Nothing written!\n");
  else
      printf("vpnsvc_read: %d bytes written!\n", ret);
  ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
