# SoftAP

SoftAP means Software Access Point for local area connections without internet access.

The main features of the SoftAP API include:

- Enabling and Disabling SoftAP
You can turn SoftAP on or off.


- Managing SoftAP
You can manage SoftAP configuration settings, such as the Service Set Identifier (SSID) and passphrase.
The following table lists the attributes of SoftAP.

**Table: the attributes of SoftAP**
| attributes			| Description								|
|----------------------|-------------------------------------------|
| `SSID`				| SSID (Service set identifier) 			|
| `Security type` 		| None, WPA2_PSK and WPS 					|
| `Passphrase `		| Passphrase for wireless access			|
| `Visibility` 		| Visibility of SSID						|
| `IP address` 		| Local IP address							|
| `Mode` 				| Wireless mode (B, G, A and AD)			|
| `Channel` 			| Channel									|


- SoftAP Client
You can get information about connected client such as name, IP address, MAC address and connection time.


## Prerequisites

1. To use the SoftAP API (in [mobile](../../api/mobile/latest/group__CAPI_NETWORK_SOFTAP_MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI_NETWORK_SOFTAP_MODULE.html) applications), the application has to request permission by adding the following privileges to the 'tizen-manifest.xml' file:

   ```
   <privileges>
     <!--Needed for configuring SoftAP settings-->
     <privilege>http://tizen.org/privilege/softap</privilege>
     <!--Needed for enabling and disabling SoftAP-->
     <privilege>http://tizen.org/privilege/softap.admin</privilege>
   </privileges>
   ```
2. To use the functions and data types of the SoftAP API, include the `<softap.h>` header file in your application:

   ```
   #include <softap.h>
   ```


## Creating SoftAP handle

To create SoftAP handle:

   ```
   softap_h softap;
   int ret = SOFTAP_ERROR_NONE;

   ret = softap_create(&softap);
   if (ret != SOFTAP_ERROR_NONE)
     printf("softap_create failed: %d", ret);
   ```




## Configuring SoftAP settings

To configure SoftAP settings:

1. Set SSID with the `softap_set_ssid()` function. If you don't use this function, device nam is used as SSID:
   ```
   int ret = SOFTAP_ERROR_NONE;
   softap_h softap = NULL;

   ret = softap_set_ssid(softap, "Tizen");
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to set SSID");
   ```

2. Set security type and passphrase. If the passphrase is not set, random string of 8 characters is used:
   ```
   ret = softap_set_security_type(softap, SOFTAP_SECURITY_TYPE_WPA2_PSK);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to set security type");

   ret = softap_set_passphrase(softap, "1q2w3e4r!@");
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to set passphrase");
   ```

3. Set visibility of SSID. In this example, client can find SoftAP device from Wi-Fi scan list.
   ```
   ret = softap_set_ssid_visibility(softap, true);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to set visibility");
   ```

## Enabling SoftAP

To enable SoftAP:

1. Define and register `enabled_cb()` callback. It will be called when the SoftAP is enabled.
   `is_requested` indicates whether this chage is requested by self or not.

   ```
   static void __enabled_cb(softap_error_e error, bool is_requested, void *data)
   {
     if (error != SOFTAP_ERROR_NONE) {
       if (!is_requested)
         return;
       printf("Failed to enable SoftAP[0x%X]", error);
       return;
   }   

   if (is_requested)
     printf("SoftAP is enabled successfully");
   else
     printf("SoftAP is enabled by other app");
   }
   ```

To register the callback:	
   ```
   ret = softap_set_enabled_cb(softap, enabled_cb, NULL);                                 
   if (ret != SOFTAP_ERROR_NONE)
     printf("Fail to regester the callback.");
   ```

2. Define and register `disabled_cb()` callback. It will be called when the SoftAP is disabled.
   `code` indicates the cause of disabling.
   ```
   static void __disabled_cb(softap_error_e error, softap_disabled_cause_e code, void *data)
   {
     if (error != SOFTAP_ERROR_NONE) {
       if (code != SOFTAP_DISABLED_BY_REQUEST)
         return;

       printf("Failed to disable SoftAP[0x%X]", error);
       return;
   }
     printf("SoftAP is disabled.");
   }	
   ```

To register the callback:	
   ```
   ret = softap_set_enabled_cb(softap, enabled_cb, NULL);                                 
   if (ret != SOFTAP_ERROR_NONE)
     printf("Fail to regester the callback.");
   ``` 

## Handling SoftAP client

To handle SoftAP client:

1. Define and register `client_connection_state_changed_cb()`. It will be called when client is conneced or disconnected. 
   ```
   static void cliet_connection_state_changed_cb(softap_client_h client, bool open, void *data)
   {
     softap_client_h clone = NULL;
     char *ip_address = NULL;
     char *mac_address = NULL;
     char *hostname = NULL;

     softap_client_clone(&clone, client);
     if (clone == NULL) {
       printf("Failed to clone client handle");
       return;
     }

     softap_client_get_ip_address(clone, SOFTAP_ADDRESS_FAMILY_IPV4, &ip_address);
     softap_client_get_mac_address(clone, &mac_address);
     softap_client_get_name(clone, &hostname);

     if (open) {
       printf("New station IP [%s], MAC [%s], hostname [%s]",
                                   ip_address, mac_address, hostname);
     } else {
       print("Disconnected station IP [%s], MAC [%s], hostname [%s]\n",
                                           ip_address, mac_address, hostname);
     }

     if (ip_address)
       free(ip_address);
     if (mac_address)
       free(mac_address);
     if (hostname)
       free(hostname);

     softap_client_destroy(clone);
   }
   ```

To register the callback:
   ```
   ret = softap_set_client_connection_state_changed_cb(softap, client_connection_state_changed_cb, NULL);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Fail to regater the callback.");
   ```

2. Get all of connected clients.
   You can obtain all of connected clients by using `softap_foreach_connected_clients()`
   The second parameter is the callback function. This callback is invoked when you get the connected client repeatedly.
   ```
   ret = softap_foreach_connected_clients(softap, connected_client_cb, NULL);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to get connected clients");
   ```

Define `connected_client_cb():
   ```
   static bool __clients_foreach_cb(softap_client_h client, void *data)
   {
     softap_client_h clone = NULL;
     char *ip_address = NULL;
     char *mac_address = NULL;
     char *hostname = NULL;
     time_t timestamp;
     struct tm t;

     if (softap_client_clone(&clone, client) != SOFTAP_ERROR_NONE) {
       printf("softap_client_clone is failed\n");
       return false;
     }

     /* Get information */
     if (softap_client_get_ip_address(clone, SOFTAP_ADDRESS_FAMILY_IPV4, &ip_address) != SOFTAP_ERROR_NONE)
       printf("Failed to get client IP address");

     if (softap_client_get_mac_address(clone, &mac_address) != SOFTAP_ERROR_NONE)
       printf("Failed to get client MAC address");

     if (softap_client_get_name(clone, &hostname) != SOFTAP_ERROR_NONE)
       printf("Failed to get client name");

     if (softap_client_get_time(clone, &timestamp) != SOFTAP_ERROR_NONE)
       printf("Failed to get connected time");

     localtime_r(&timestamp, &t);

     printf("\n< Client Info. >\n");
     printf("\tIP Address %s\n", ip_address);
     printf("\tMAC Address : %s\n", mac_address);
     printf("\tHostname : %s\n", hostname);
     printf("\tTime stamp : %04d-%02d-%02d %02d:%02d:%02d",
              t.tm_year + 1900, t.tm_mon + 1,
              t.tm_mday, t.tm_hour,
              t.tm_min, t.tm_sec);

     if (ip_address)
       free(ip_address);
     if (mac_address)
       free(mac_address);
     if (hostname)
       free(hostname);

     softap_client_destroy(clone);

     /* Continue iteration */
     return true;
   }
   ```


## Disabling SoftAP

To disable SoftAP:

   ```
   ret = softap_disable(softap);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to disable SoftAP");   
   ```

## Releasing all resources

To release all SoftAP resources:

1. Unregister callback functions.
    ```
    ret = softap_unset_enabled_cb(softap);
    if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to unset the callback");

   ret = softap_unset_disabled_cb(softap);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to unset the callback");

   ret = softap_unset_client_connection_state_changed_cb(softap);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to unset the callback");

   ```


2. Destroy SoftAP handle.

When no longer needed, destroy the handle:

   ```
   ret = softap_destroy(softap);
   if (ret != SOFTAP_ERROR_NONE)
     printf("Failed to destory the handle");
   ```


## Related Information
   - Dependencies
   - Tizen 5.0 and Higher for Mobile
   - Tizen 5.0 and Higher for Wearable
