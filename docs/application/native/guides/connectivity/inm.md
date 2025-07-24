# Intelligent Network Monitoring

Intelligent Network Monitoring (INM) API is used to get information about the network, provided by Linux functions. Some features of this API are detecting IP collision, dumping network status, dumping TCP, monitoring ethernet, monitoring Wi-Fi module state and getting network statistics.

This feature is supported in mobile, TV, and wearable profile.

> [!NOTE]
> You can test the INM functionality on a target device only. The [Tizen emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the INM API:

1. To use the [INM](../../api/mobile/latest/group__CAPI__NETWORK__INM__MODULE.html) API, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```xml
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
   </privileges>
   ```

2. To use the functions and data types of the INM API, include the `<inm.h>` header file in your application:

   ```cpp
   #include <inm.h>
   ```

3. Call `inm_initialize()` to initialize the library:

    ```cpp
    inm_initialize();
    ```

4. When no longer needed, call `inm_deinitialize()` to deinitialize the library:

   ```cpp
   inm_deinitialize();
   ```
   
## Get Default Connection Info

To retrieve information about the default connection:

   ```cpp
   int get_conn_info(void)
   {
     int ret = INM_ERROR_NONE;
     inm_h inm;
     inm_connection_h conn;

     /* initialize library */
     ret = inm_initialize(&inm);
     if (ret != INM_ERROR_NONE) {
         printf("Initialization failed\n");
         return ret;
     }

     /* get default connection handle */
     if (inm_get_current_connection(inm, &conn) != INM_ERROR_NONE) {
         inm_deinitialize(inm);
         printf("Getting default connection handle failed\n");
         return ret;
     }

     /* retrieve required info */
     inm_link_h link;
     inm_connection_type_e network_type;
     inm_connection_state_e conn_state;
     char *if_name;
     char *ip_addr;
     unsigned long long rx_bytes;
     unsigned long long tx_bytes;

     ret = inm_connection_get_link(conn, &link);
     ret = inm_connection_get_type(conn, &network_type);
     ret = inm_connection_get_state(conn, &conn_state);
     ret = inm_connection_get_network_interface_name(conn, &if_name);
     if(ret != INM_ERROR_NONE) {
         inm_deinitialize(inm);
         printf("Getting basic connection info failed\n");
         return ret;
     }

     printf("conn-info: type[%d] state[%d] if_name[%s]\n",
             network_type, conn_state, if_name);
     
     /* get ipv4 address */
     ret = inm_connection_get_ip_address(conn, INM_ADDRESS_FAMILY_IPV4, &ip_addr);
     if(ret != INM_ERROR_NONE) {
         inm_deinitialize(inm);
         printf("Getting IP address failed\n");
         return ret;
     }

     printf("conn-info: ip_addr[%s]\n", ip_addr);
     
     /* get sent and received bytes data via link */
     ret = inm_link_get_received_bytes(link, &rx_bytes);
     ret = inm_link_get_sent_bytes(link, &tx_bytes);
     if(ret != INM_ERROR_NONE) {
         inm_deinitialize(inm);
         printf("Getting received and sent bytes failed\n");
         return ret;
     }
     
     printf("conn-info: rx_bytes[%llu], tx_bytes[%llu]\n", rx_bytes, tx_bytes);
     
     /* free up allocated memory and deinitialize */
     free(if_name);
     free(ip_addr);
     inm_link_destroy(link);
     inm_connection_destroy(&conn);
     inm_deinitialize(inm);
     
     return ret;
   }
   ```

You can retrieve information about a particular connection by iterating through the connections using `inm_get_connection_iterator()` that returns a connection iterator and `inm_connection_iterator_next()` that gets you a connection handle.

## Monitor Wi-Fi State Change

1. Define a callback function to process the Wi-Fi state change:

    ```cpp
    void __wifi_state_changed_cb(inm_wifi_state_e state,
                                              void *user_data)
    {
     /* Do the necessary action when Wi-Fi state has changed */
    }
    ```
    
2. Set the Wi-Fi state change callback:

    ```cpp
    int monitor_wifi_state(void)
    {
        int ret = INM_ERROR_NONE;
        inm_h inm;
        
        /* initialize library */
        ret = inm_initialize(&inm);
        if (ret != INM_ERROR_NONE) {
            printf("Initialization failed\n");
            return ret;
        }
        
        ret = inm_set_wifi_state_changed_cb(inm, __wifi_state_changed_cb, NULL);
        if (ret != INM_ERROR_NONE) {
            printf("Setting wifi state change callback failed\n");
            return ret;
        }
        else {
            printf("Successfully set wifi state change callback\n");
        }
        
        /* deinitialize */
        inm_deinitialize(inm);
        
        return ret;
    }
    ```
    
You can monitor other types of state changes using certain callback functions, such as `inm_set_cellular_state_changed_cb()` or `inm_set_ethernet_state_changed_cb()`.

## Related Information
- Dependencies
  - Tizen 5.0 and Higher for Mobile
  - Tizen 5.0 and Higher for Wearable
  - Tizen 5.0 and Higher for TV
