# Wi-Fi Direct&reg;

Wi-Fi Direct&reg; is a technology that allows you to find nearby Wi-Fi Direct devices and form a Wi-Fi Direct group to communicate over a peer-to-peer link without wireless access points (base stations) in the infrastructure mode. Wi-Fi Direct is a synonym for Wi-Fi P2P (Peer-to-Peer).

This feature is supported in mobile applications only.

In a Wi-Fi Direct group, the group owner works as an access point in the Wi-Fi infrastructure mode and the other devices join the group as clients. A group can be created either by negotiation between 2 devices or in an autonomous mode by a single group owner device. In a negotiation-based group creation, 2 devices compete based on the group owner intent value and the higher intent device becomes a group owner, while the other device becomes a group client. In an autonomous group creation, a device becomes a group owner by itself without any group client.

A Wi-Fi Direct device can join an existing group by associating itself with the group owner, as long as the allowed number of clients is not exceeded.

The main features of the Wi-Fi Direct API include:

- Activating Wi-Fi Direct

  You can [activate a local Wi-Fi Direct device](#activating) and [deactivate it](#deactivating).

- Getting the Wi-Fi Direct peer device information

  You can [discover Wi-Fi Direct peer devices](#getting_device_info) and show Wi-Fi Direct peer device information.

- Connecting to a specific Wi-Fi Direct peer device

  You can [connect to a specific Wi-Fi Direct device](#connecting_device). When the connection is no longer needed, you can end it.

- Managing Wi-Fi Direct groups

  You can [create a Wi-Fi Direct group](#creating_group) and manage the group.

> **Note**  
> You can test the Wi-Fi Direct functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the Wi-Fi Direct functionality:

1. To use the [Wi-Fi Direct](../../api/mobile/latest/group__CAPI__NETWORK__WIFI__DIRECT__MODULE.html) API, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/wifidirect</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Wi-Fi Direct API, include the `<wifi_direct.h>` header file in your application:

   ```
   #include <wifi_direct.h>
   ```

3. Call the `wifi_direct_initialize()` function:

    ```
    int error_code;

    error_code = wifi_direct_initialize();
    ```

4. To get the Wi-Fi Direct activation and deactivation events, set up the `wifi_direct_device_state_changed_cb()` callback:

   ```
   void
   device_state_changed_cb(wifi_direct_error_e error_code,
                           wifi_direct_device_state_e device_state,
                           void *user_data);

   error_code = wifi_direct_set_device_state_changed_cb(device_state_changed_cb, NULL);
   ```

5. To get the Wi-Fi Direct discovery events, set up the `wifi_direct_discovery_state_changed_cb()` callback:

   ```
   void
   discovery_state_changed_cb(wifi_direct_error_e error_code,
                              wifi_direct_discovery_state_e discovery_state,
                              void *user_data);

   error_code = wifi_direct_set_discovery_state_changed_cb(discovery_state_changed_cb, NULL);
   ```

6. To get Wi-Fi Direct connection events, set up the `wifi_direct_connection_state_changed_cb()` callback:

   ```
   void
   connection_state_changed_cb(wifi_direct_error_e error_code,
                               wifi_direct_connection_state_e connection_state,
                               void *user_data);

   error_code = wifi_direct_set_connection_state_changed_cb(connection_state_changed_cb, NULL);
   ```

<a name="activating"></a>
## Activating Wi-Fi Direct

To activate a Wi-Fi Direct local device and to check the Wi-Fi Direct local device state:

1. Activate a Wi-Fi Direct local device

   Define the `device_state_changed_cb()` callback function, which is invoked whenever a Wi-Fi Direct local device activates or deactivates. In the following example, an information message is printed in the console.

   ```
   static void
   device_state_changed_cb(wifi_direct_error_e error_code,
                           wifi_direct_discovery_state_e discovery_state,
                           void *user_data)
   {
       if (device_state == WIFI_DIRECT_DEVICE_STATE_ACTIVATED) {
           printf("Activate Wi-Fi Direct device!\n");
           /* Handle the event */
       } else if (device_state == WIFI_DIRECT_DEVICE_STATE_DEACTIVATED) {
           printf("Deactivate Wi-Fi Direct device!\n");
           /* Handle the event */
       }
   }
   ```

2. Switch on the Wi-Fi Direct local device with the `wifi_direct_activate()` function.

   After the `wifi_direct_activate()` function is completed, the `wifi_direct_device_state_changed_cb()` callback is invoked.

   ```
   error_code = wifi_activate(NULL);
   ```

3. Check the Wi-Fi Direct state.

   You can check the Wi-Fi Direct local device state using the `wifi_direct_get_state()` function:

   ```
   wifi_direct_state_e state = WIFI_DIRECT_STATE_DEACTIVATED;
   wifi_direct_get_state(&state);
   printf("Wi-Fi Direct state: %d.\n", state);
   ```

<a name="getting_device_info"></a>
## Getting the Wi-Fi Direct Peer Device Information

To discover nearby Wi-Fi Direct peer devices, and after discovering, to print the results of the discovery, such as Wi-Fi Direct peer device information:

1. Define a callback function for the discovery, to be called when the discovery state is changed:

   ```
   void
   discovery_state_changed_cb(wifi_direct_error_e error_code,
                              wifi_direct_discovery_state_e discovery_state,
                              void *user_data)
   {
       switch (discovery_state) {
       case WIFI_DIRECT_ONLY_LISTEN_STARTED:
           /* Handle the event */

           return "DISCOVERY_STATE: ONLY_LISTEN_STARTED";
       case WIFI_DIRECT_DISCOVERY_STARTED:
           /* Handle the event */

           return "DISCOVERY_STATE: DISCOVERY_STARTED";
       case WIFI_DIRECT_DISCOVERY_FOUND:
           /* Handle the event */

           return "DISCOVERY_STATE: DISCOVERY_FOUND";
       case WIFI_DIRECT_DISCOVERY_FINISHED:
           /* Handle the event */

           return "DISCOVERY_STATE: DISCOVERY_FINISHED";
       default:
           return "UNKNOWN_DISCOVERY_STATE";
       }

       return "UNKNOWN_DISCOVERY_STATE";
   }
   ```

2. Start the discovery by scanning for nearby devices.

   When the Wi-Fi Direct discovery state changes, the `wifi_direct_discovery_state_changed_cb()` function is called.

   ```
   wifi_direct_start_discovery(false, 0);
   ```

3. Show the search results.

   Show the discovery result using the `wifi_direct_discovered_peer_cb()` callback, which is invoked by the `wifi_direct_foreach_discovered_peers()` function. In the following example, the Wi-Fi Direct peer device information is printed.

   ```
   bool
   discovered_peer_cb(wifi_direct_discovered_peer_info_s *peer, void *user_data)
   {
       if (NULL != peer) {
           printf("\nDevice Name: %s", peer->device_name);
           printf("\nMac Address: %s", peer->mac_address);
           /* Handle the event */

           return 1;
       } else {
           return false;
       }
   }

   int rv = wifi_direct_foreach_discovered_peers(discovered_peer_cb, NULL);
   ```

   You can also get other information, including the connection state, device type, Wi-Fi display information, and WPS type.

<a name="connecting_device"></a>
## Connecting to a Specific Wi-Fi Direct Peer Device

To connect to a specific device:

1. Define the callback function for the connection state.

   The connection event received from the Wi-Fi Direct framework invokes a callback. The following example defines a `connection_state_changed_cb()` callback to handle all Wi-Fi Direct connection events.

   ```
   static void
   connection_state_changed_cb(wifi_direct_error_e error_code,
                               wifi_direct_connection_state_e connection_state,
                               const char *mac_address, void *user_data)
   {
       printf("Connection state changed to: [%d] [%s]\n", connection_state,
              test_wfd_convert_connection_state_to_string(connection_state));

       bool accept_connection = false;
       int rv = 0;

       switch (connection_state) {
       case WIFI_DIRECT_CONNECTION_WPS_REQ:
           /* Outgoing requests */
           wifi_direct_wps_type_e wps_mode;
           wifi_direct_get_local_wps_type(&wps_mode);
           /* Handle the event */
           break;
       case WIFI_DIRECT_CONNECTION_REQ:
           /* Incoming requests */
           wifi_direct_wps_type_e wps_mode;
           wifi_direct_get_local_wps_type(&wps_mode);
           /* Handle the event */
           break;
       case WIFI_DIRECT_INVITATION_REQ:
           /* Invitation request from peer */
           /* Handle the event */
           break;
       case WIFI_DIRECT_DISASSOCIATION_IND:
       case WIFI_DIRECT_DISCONNECTION_IND:
           printf("Peer: [%s] disconnected.\n", mac_address);
           /* Handle the event */
           break;
       case WIFI_DIRECT_CONNECTION_IN_PROGRESS:
           printf("Connection in progress\n");
           /* Handle the event */
       case WIFI_DIRECT_CONNECTION_RSP:
           if (error_code == WIFI_DIRECT_ERROR_CONNECTION_FAILED) {
               printf(MAKE_RED"Time Out or connection failed"RESET_COLOR"\n");
               /* Handle the event */
           }
           break;
       case WIFI_DIRECT_GROUP_CREATED:
           /* Handle the event */
           break;
       case WIFI_DIRECT_GROUP_DESTROYED:
           /* Handle the event */
           break;
       case WIFI_DIRECT_DISCONNECTION_RSP:
           /* Handle the event */
           break;
       default:
           printf("Unknown State Received\n");
       }
   }
   ```

2. Connect to a Wi-Fi Direct peer device.

   Check whether Wi-Fi Direct is activated using the `wifi_direct_get_state()` function, and then get the specific device address.

   You can obtain the address directly from the user (as in the following example), or by calling the `wifi_direct_foreach_discovered_peers()` function to the address through the device discovery process.

   ```
   char * mac_address = NULL;
   wifi_direct_state_e state;
   int error_code;

   wifi_direct_get_state(&state);
   if (state < WIFI_DIRECT_STATE_ACTIVATED)
       return -1;

   mac_address = calloc(1, 32*sizeof(char));
   if (!mac_address) {
       printf("cannot allocate memory");

       return -1;
   }

   printf("\nEnter Mac_address: ");
   if (scanf(" %s", mac_address) < 1) {
       free(mac_address);

       return -1;
   }
   if (strlen(mac_address) > 23)
       printf("\nWrong Mac_address");

   error_code = wifi_direct_connect(mac_address);
   if (error_code != WIFI_DIRECT_ERROR_NONE) {
       printf("Failed to connect\n");

       return -1;
   }

   printf("Connection step finished\n");
   ```

3. When the connection is no longer needed, disconnect from the Wi-Fi Direct device:

   ```
   char * mac_address = NULL;
   wifi_direct_state_e state;
   int error_code;

   wifi_direct_get_state(&state);
   if (state < WIFI_DIRECT_STATE_ACTIVATED)
       return -1;

   mac_address = calloc(1, 32*sizeof(char));
   if (!mac_address) {
       printf("cannot allocate memory");

       return -1;
   }

   printf("\nEnter Mac_address: ");
   if (scanf(" %s", mac_address) < 1) {
       free(mac_address);

       return -1;
   }
   if (strlen(mac_address) > 23)
       printf("\nWrong Mac_address");

   error_code = wifi_direct_disconnect(mac_address);
   if (error_code != WIFI_DIRECT_ERROR_NONE) {
       printf("Failed to disconnect\n");

       return -1;
   }

   printf("Disconnection step finished\n");
   ```

<a name="creating_group"></a>
## Managing Wi-Fi Direct Groups

To create an autonomous Wi-Fi Direct group and to make your device the autonomous group owner:

1. Create a Wi-Fi Direct group and become a group owner:

   ```
   wifi_direct_state_e state;
   int error_code;

   wifi_direct_get_state(&state);
   if (state < WIFI_DIRECT_STATE_ACTIVATED || state > WIFI_DIRECT_STATE_DISCOVERING)
       return -1;

   error_code = wifi_direct_create_group();
   if (error_code != WIFI_DIRECT_ERROR_NONE) {
       printf("Failed to create wifi direct group\n");

       return -1;
   }

   printf("Connection step finished\n");
   ```

2. When Wi-Fi Direct connections or group is no longer needed, destroy all connections and the group:

   ```
   wifi_direct_state_e state;
   int error_code;

   wifi_direct_get_state(&state);
   if (state < WIFI_DIRECT_STATE_CONNECTED)
       return -1;

   error_code = wifi_direct_destroy_group();
   if (error_code != WIFI_DIRECT_ERROR_NONE) {
       printf("Failed to destroy wifi direct group\n");

       return -1;
   }

   printf("Disconnection step finished\n");
   ```

<a name="deactivating"></a>
## Deactivating Wi-Fi Direct

To deactivate Wi-Fi Direct when it is no longer needed (or the application is exiting):

1. Power off the local device using the `wifi_direct_deactivate()` function:

   ```
   wifi_direct_deactivate(NULL);
   ```

2. Unset the callbacks:

   ```
   /* Unset the activation or deactivation event callback */
   wifi_direct_unset_device_state_changed_cb(NULL);

   /* Unset the discovery event callback */
   wifi_direct_unset_discovery_state_changed_cb(NULL);

   /* Unset the connection event callback */
   wifi_direct_unset_connection_state_changed_cb(NULL);
   ```

3. Release Wi-Fi Direct:

   ```
   wifi_direct_deinitialize();
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
