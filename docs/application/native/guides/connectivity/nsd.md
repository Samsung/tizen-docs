# Network Service Discovery


You can use 2 different protocols to perform network service discoveries to announce local services and search for remote services on a network, DNS-SD (DNS Service Discovery) and SSDP (Simple Service Discovery Protocol).

- The DNS-SD protocol provides functions for mDNS- and DNS-based service discovery.

  The main features of the DNSSD API include:

  - Creating and registering a local service

    You can [manage a local service](#dnssd_service) using a local service handle.

  - Searching for remote services

    You can [search for the available remote services](#dnssd_search) on a network.

- The SSDP protocol provides functions for simple service discovery.

  The main features of the SSDP API include:

  - Creating and registering a local service

    You can [manage a local service](#ssdp_service) using a local service handle.

  - Searching for remote services

    You can [search for the available remote services](#ssdp_search) on a network.

Both protocols allow the application to get details, such as the service names and the service locations on a network.

## Prerequisites

To enable your application to use the network service discovery functionality:

- To use the DNS-SD protocol:

  1. To use the functions and data types of the DNSSD API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__DNSSD__MODULE.html) applications), include the `<dnssd.h>` header file in your application:

     ```
     #include <dnssd.h>
     ```

  2. Initialize DNS-SD using the `dnssd_initialize()` function:

     ```
     int error_code;

     error_code = dnssd_initialize();
     if (error_code != DNSSD_ERROR_NONE)
         return;
     ```

     When no longer needed, release the DNS-SD:

     ```
     dnssd_deinitialize();
     ```

- To use the SSDP protocol:

  1. To use the functions and data types of the SSDP API (in [mobile](../../api/mobile/latest/group__CAPI__NETWORK__SSDP__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__NETWORK__SSDP__MODULE.html) applications), include the `<ssdp.h>` header file in your application:

     ```
     #include <ssdp.h>
     ```

  2. Initialize SSDP using the `ssdp_initialize()` function:

     ```
     int error_code;

     error_code = ssdp_initialize();
     if (error_code != SSDP_ERROR_NONE)
         return;
     ```

     When no longer needed, release the SSDP:

     ```
     ssdp_deinitialize();
     ```

<a name="dnssd_service"></a>
## Managing a Local Service with DNSSD

To announce a local service, create a local service handle using the `dnssd_create_local_service()` function, and set the service information using the handle. Afterwards, you can register the local service using the `dnssd_register_local_service()` function.

To manage a local service, you must create and register the service:

1. Create the local service:

   1. To provide a local service on a network, you must create a handle containing information about the service.

      At the beginning, define a `dnssd_service_h` variable to store the service handle. The target is used to create the handle, which represents a DNS-SD service to be advertised through a network. To set the service type, see [http://www.dns-sd.org/ServiceTypes.html](http://www.dns-sd.org/ServiceTypes.html).

      ```
      dnssd_service_h service_handle;
      char *service_type = "_http._tcp";
      int error_code;

      error_code = dnssd_create_local_service(service_type, &service_handle);
      if (error_code == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in creating a service handle.");
      ```

   2. Set a unique service name and a port number for the created service:

      ```
      char* service_name = "SamsungTest";
      int port = 80;

      if (dnssd_service_set_name(service_handle, service_name) == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in setting service name");
      if (dnssd_service_set_port(service_handle, port) == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in setting port");
      ```

   3. You can add a TXT record, which gives additional information about the created service. The TXT record is stored in a structured form using key-value pairs.

      For more information, see section 6 of [http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt). The TXT record of the known service types can be found at [http://www.dns-sd.org/ServiceTypes.html](http://www.dns-sd.org/ServiceTypes.html).

      ```
      char* key = "path";
      char* value = "http://www.samsung.com";
      int length = 30;

      if (dnssd_service_add_txt_record_value(service_handle, key, length, value) == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in setting service TXT");
      ```

      When no longer needed, you can remove the TXT record from the created service:

      ```
      char* key = "path";

      if (dnssd_service_remove_txt_record_value(service_handle, key) == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in removing service TXT");
      ```

2. Register the local service:

   1. Register the service to announce its availability on a network:

      ```
      error_code = dnssd_register_local_service(service_handle, __registered_cb, NULL);
      if (error_code == DNSSD_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in registering a local service.");
      ```

   2. The callback defined in the `dnssd_register_local_service()` function is called when the service registration is finished:

      ```
      void
      __registered_cb(dnssd_error_e result, dnssd_service_h dnssd_service, void* user_data)
      {
          if (result == DNSSD_ERROR_NONE) {
              /* Service is registered successfully */
              dlog_print(DLOG_DEBUG, LOG_TAG, "Registered");
          } else if (result == DNSSD_NAME_CONFLICT) {
              /* Name conflict exists */
              dlog_print(DLOG_DEBUG, LOG_TAG, "Name conflict");
          } else if (result == DNSSD_ALREADY_REGISTERED) {
              /* Service is already registered */
              dlog_print(DLOG_DEBUG, LOG_TAG, "Already registered");
          } else {
              /* Result is unknown */
              dlog_print(DLOG_DEBUG, LOG_TAG, "Unknown result");
          }
      }
      ```

3. When you no longer want to provide the local service, deregister it with the `dnssd_deregister_local_service()` function.

    To destroy the local service handle, use the `dnssd_destroy_local_service()` function.

    ```
    dnssd_deregister_local_service(service_handle):
    dnssd_destroy_local_service(service_handle);
    ```

<a name="dnssd_search"></a>
## Browsing Remote Services with DNSSD

To search for available services on a network, use a service type or target information:

1. To start searching, use the `dnssd_start_browsing_service()` function.

    The DNS-SD browser handle is stored in a `dnssd_browser_h` variable. For more information on the service types, see [http://www.dns-sd.org/ServiceTypes.html](http://www.dns-sd.org/ServiceTypes.html).

    ```
    dnssd_browser_h browser_handle;
    char *service_type = "_ftp._tcp";
    int error_code;

    error_code = dnssd_start_browsing_service(service_type, &browser_handle, __found_cb, NULL);
    if (error_code == DNSSD_ERROR_NONE)
        dlog_print(DLOG_DEBUG, LOG_TAG, "Start browsing");
    ```

2. The callback defined in the `dnssd_start_browsing_service()` function is called when the remote service becomes available or unavailable:

    ```
    void
    __dnssd_print_found(dnssd_service_h dnssd_remote_service)
    {
        /* Handling the found service */
        char *service_name = NULL;
        char *service_type = NULL;
        char *ip_v4_address = NULL
        char *ip_v6_address = NULL;
        char *txt_record_value = NULL;
        int length = 0;
        int port = 0;
        error_code = dnssd_service_get_name(dnssd_remote_service, &service_name);
        if (error_code == DNSSD_ERROR_NONE && service_ name!= NULL)
            dlog_print(DLOG_DEBUG, LOG_TAG, "Service name [%s]", service_ name);

        error_code = dnssd_service_get_type(dnssd_remote_service, &service_type);
        if (error_code == DNSSD_ERROR_NONE && service_type != NULL)
            dlog_print(DLOG_DEBUG, LOG_TAG, "Service type [%s]", service_type);

        error_code = dnssd_service_get_ip(dnssd_remote_service, &ip_v4_address, &ip_v6_address)
        if (error_code == DNSSD_ERROR_NONE) {
            if (ip_v4_address)
                dlog_print(DLOG_DEBUG, LOG_TAG, "IPV4 address [%s]", ip_v4_address);
            if (ip_v6_address)
                dlog_print(DLOG_DEBUG, LOG_TAG, "IPV6 address [%s]", ip_v6_address);
        }

        error_code = dnssd_service_get_port(dnssd_remote_service, &port)
        if (error_code == DNSSD_ERROR_NONE)
            dlog_print(DLOG_DEBUG, LOG_TAG, "Service port [%d]", port);
        error_code = dnssd_service_get_txt_record_value(dnssd_remote_service, &txt_record_value, &value);
        if (error_code == DNSSD_ERROR_NONE && txt_record_value!= NULL)
            dlog_print(DLOG_DEBUG, LOG_TAG, "Service TXT [%s]", txt_record_value);

        if (service_name)
            free(service_name);
        if (service_type)
            free(service_type);
        if (ip_v4_address)
            free(ip_v4_address);
        if (ip_v6_address)
            free(ip_v6_address);
        if (txt_record_value)
            free(txt_record_value);
    }

    void
    __found_cb(dnssd_service_h dnssd_remote_service, dnssd_service_state_e state, void *user_data)
    {
        dlog_print(DLOG_DEBUG, LOG_TAG, "Browse Service Callback\n");
        dlog_print(DLOG_DEBUG, LOG_TAG, "Handler: %u\n", dnssd_remote_service);
        dlog_print(DLOG_DEBUG, LOG_TAG, "State: ");
        switch (browse_state) {
        case DNSSD_SERVICE_STATE_AVAILABLE:
            /* DNS-SD service found */
            __dnssd_print_found(dnssd_remote_service);
            dlog_print(DLOG_DEBUG, LOG_TAG, "Available\n");
            break;
        case DNSSD_SERVICE_STATE_UNAVAILABLE:
            /* DNS-SD service becomes unavailable */
            dlog_print(DLOG_DEBUG, LOG_TAG, "Un-Available\n");
            break;
        case DNSSD_SERVICE_STATE_NAME_LOOKUP_FAILED:
            /* Browsing failed */
            dlog_print(DLOG_DEBUG, LOG_TAG, "Browse Failure\n");
            break;
        case DNSSD_SERVICE_STATE_HOST_NAME_LOOKUP_FAILED:
            /* Resolving service name failed */
            dlog_print(DLOG_DEBUG, LOG_TAG, "Resolve Service Name Failure\n");
            break;
        case DNSSD_SERVICE_STATE_ADDRESS_LOOKUP_FAILED:
            /* Resolving service address failed */
            dlog_print(DLOG_DEBUG, LOG_TAG, "Resolve Service Address\n");
            break;
        default:
            dlog_print(DLOG_DEBUG, LOG_TAG, "Unknown Browse State\n");
            break;
        }
    }
    ```

3. When the services no longer interest you, stop the search using the browser handle:

   ```
   dnssd_stop_browsing_service(browser_handle);
   ```

<a name="ssdp_service"></a>
## Managing a Local Service with SSDP

To announce a local service, create a local service handle using the `ssdp_create_local_service()` function, and set the service information using the handle. Afterwards, you can register the local service using the `ssdp_register_local_service()` function.

To manage a local service, you must create and register the service:

1. Create the local service:

   1. To provide a local service on a network, you must create a handle containing information about the service.

      At the beginning, define an `ssdp_service_h` variable to store the service handle. The target is used to create the handle, which represents a device or service type specified in the [UPnP forum](http://upnp.org).

      ```
      ssdp_service_h service_handle;
      char *target = "upnp:rootdevice";
      int error_code;

      error_code = ssdp_create_local_service(target, &service_handle);
      if (error_code == SSDP_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in creating a service handle.");
      ```

   2. Set a USN (Unique Service Name) and a URL (Uniform Resource Locator) for the created service.

      The USN format is also specified in the UPnP forum. For the URL, see the RFC 3986.

      ```
      char* usn = "uuid:1234abcd-12ab-12ab-12ab-1234567abc12::upnp:rootdevice";
      char* url = "192.168.0.2:1234";

      if (ssdp_service_set_usn(service_handle, usn) == SSDP_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in setting USN");
      if (ssdp_service_set_url(service_handle, url) == SSDP_ERROR_NONE)
          dlog_print(DLOG_DEBUG, LOG_TAG, "Success in setting URL");
      ```

2. Register the local service:

   1. Register the service to announce its availability on a network.

       The target can be a device or service type specified in the UPnP forum.

       ```
       error_code = ssdp_register_local_service(service_handle, __registered_cb, NULL);
       if (error_code == SSDP_ERROR_NONE)
           dlog_print(DLOG_DEBUG, LOG_TAG, "Success in registering a local service.");
       ```

   2. The callback defined in the `ssdp_register_local_service()` function is called when the service registration is finished:

       ```
       void
       __registered_cb(ssdp_error_e result, ssdp_service_h ssdp_service, void *user_data)
       {
           dlog_print(DLOG_DEBUG, LOG_TAG, "Register result: %d\n", result);
       }
       ```

3. When you no longer want to provide the local service, deregister it with the `ssdp_deregister_local_service()` function.

    To destroy the local service handle, use the `ssdp_destroy_local_service()` function.

    ```
    ssdp_deregister_local_service(service_handle);
    ssdp_destroy_local_service(service_handle);
    ```

<a name="ssdp_search"></a>
## Browsing Remote Services with SSDP

To search for available services on a network, use a service type or target information:

1. To start searching, use the `ssdp_start_browsing_service()` function.

    The SSDP browser handle is stored in an `ssdp_browser_h` variable.

    ```
    ssdp_browser_h browser_handle;
    char *target = "upnp:rootdevice";
    int error_code;

    error_code = ssdp_start_browsing_service(target, &browser_handle, __found_cb, NULL);
    if (error_code == SSDP_ERROR_NONE)
        dlog_print(DLOG_DEBUG, LOG_TAG, "Start browsing");
    ```

2. The callback defined in the `ssdp_start_browsing_service()` function is called when the remote service becomes available or unavailable:

    ```
    void
    __found_cb(ssdp_service_h ssdp_remote_service, ssdp_service_state_e state, void *user_data)
    {
        char *usn;
        char *url;
        ssdp_service_get_usn(ssdp_remote_service, &usn);
        ssdp_service_get_url(ssdp_remote_service, &url);
        dlog_print(DLOG_DEBUG, LOG_TAG, "state: %s\n", state==SSDP_SERVICE_STATE_AVAILABLE ? "AVAILABLE" : "UNAVAILABLE");
        dlog_print(DLOG_DEBUG, LOG_TAG, "usn: %s\n", usn);
        dlog_print(DLOG_DEBUG, LOG_TAG, "url: %s\n", url);
    }
    ```

3. When the services no longer interest you, stop the search using the browser handle:

   ```
   ssdp_stop_browsing_service(browser_handle);
   ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
