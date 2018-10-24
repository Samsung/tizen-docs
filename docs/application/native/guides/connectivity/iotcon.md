# IoT Connectivity


[IoTivity](https://www.iotivity.org/) offers seamless device-to-device connectivity to address the emerging needs of the Internet of Things (IoT) through the open source reference implementation of the OCF (Open Connectivity Foundation) standard specifications. IoT connectivity (IoTCon) provides the means of using IoTivity in Tizen.

**Figure: IoTivity in Tizen**

![IoTivity in Tizen](./media/iotivity.png)

IoT connectivity handles the resources between a server and client. The server is responsible for creating and providing resources, and the client can access and control those resources through requests.

The main features of the IoTCon API include:

- Resource management

  Entities in the physical world, such as a light, a fan, or modules of a home appliance, are represented as resources with the following properties:

  - Resource URI path: Value that corresponds to a resource
  - Resource types: Values for identifying a resource
  - Resource interfaces: List of the interfaces supported by the resource
  - Resource properties: Whether the resource is observable and discoverable

  You can manage the IoT resources with the server, which can [create resources](#register) and later destroy them using the `iotcon_resource_create()` and `iotcon_resource_destroy()` functions of the Resource API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__SERVER__RESOURCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__SERVER__RESOURCE__MODULE.html) applications). After creating a resource, the server can bind the resource types and resource interfaces using the `iotcon_resource_bind_type()` and `iotcon_resource_bind_interface()` functions. After a resource is destroyed, the client cannot access the resource anymore.

  If the resource is discoverable, the client can find the resource. Otherwise, only the clients that already know the resource information can access it. If the resource is observable, the client can observe it.

- Remote resource management

  If the resource created by the server is discoverable, the client that knows the resource type can [find the resource](#find) using the `iotcon_find_resource()` function of the Client API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__MODULE.html) applications). If the `host_address` is `NULL`, the find request is sent as multicast. The client can filter the desired resources with a query.

  If the client wants to access a resource whose information it already knows, it can make a proxy using the `iotcon_remote_resource_create()` function of the Remote Resource API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__REMOTE__RESOURCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__REMOTE__RESOURCE__MODULE.html) applications) and access the resource through that proxy.

  You can use the client to get various information about the resource through the `iotcon_remote_resource_h` handle and the `iotcon_remote_resource_get_XXX()` functions. You can retrieve, for example, the resource URI path, host address, type, and interfaces. You can also retrieve the device ID, which defines the device to which the resource belongs. Different resources on the same device have the same device ID.

- CRUDN request and response

  The client can send various requests to the server resources using the Remote Resource API:

  - GET request: Use the `iotcon_remote_resource_get()` function to read the resource information and [get a representation of the resource](#send_get) from the server.
  - PUT request: Use the `iotcon_remote_resource_put()` function to ask the server to [update the resource representation](#send_put).
  - POST request: Use the `iotcon_remote_resource_post()` function to ask the server to create a new resource.
  - DELETE request: Use the `iotcon_remote_resource_delete()` function to ask the server to delete a resource.

  The server receives the request, processes it using the `iotcon_request_handler_cb()` callback, and sends a response to the client using the `iotcon_response_send()` function of the Response API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__RESPONSE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__RESPONSE__MODULE.html) applications).

  The client can check the result and the response in the `iotcon_remote_resource_response_cb()` callback. If the result of the request differs from `IOTCON_ERROR_NONE`, the response information is not reliable.

  **Figure: Requests and responses**

  ![Requests and responses](./media/iotivity_request.png)

  If the server resource is observable, the client can register a callback with the `iotcon_remote_resource_observe_register()` function of the Remote Resource API to [observe the resource](#observe). When the resource state changes, the server notifies the client through the registered callback. Note that, depending on the network environment, the order in which the notifications are sent can be mixed. If the `observe_policy` (the second parameter of the registration function) is `IOTCON_OBSERVE_IGNORE_OUT_OF_ORDER`, the client only receives up-to-date notifications. Otherwise, it receives all notifications, including stale notifications.

  If the resource is not observable, the client cannot receive any notifications.

  **Figure: Observe and notify**

  ![Observe and notify](./media/iotivity_observe.png)

- Resource representation

  Resource representation is a snapshot of a resource at a particular time, representing the resource information exchanged in the request and response interactions between the server and client. The resource representation contains resource properties and the state of the resource.

  To manage the representation, use the Representation API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__REPRESENTATION__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__REPRESENTATION__MODULE.html) applications):

  - Create a resource representation and attributes with the `iotcon_representation_create()` and `iotcon_attributes_create()` functions.
  - Set the properties on the created attributes with the `iotcon_attributes_add_XXX()` functions.
  - Set the attributes on the created representation with the `iotcon_representation_set_attributes()` function.

## Prerequisites

To enable your application to use the IoT functionality:

1. To use the IoTCon API (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__MODULE.html) applications), the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
      <privilege>http://tizen.org/privilege/internet</privilege>
   </privileges>
   ```

2. To use the functions and data types of the IoTCon API, include the `<iotcon.h>` header file in your application:
    ```
    #include <iotcon.h>
    ```
    To ensure that an IoTCon function has been executed properly, make sure that the return is equal to `IOTCON_ERROR_NONE`.

3. To initialize the IoTCon, use the `iotcon_initialize()` function:
    ```
    int ret;
    char *path; /* Must be a file path which can be read/written in the application */

    ret = iotcon_initialize(path);
    ```

4. When the resources are no longer needed, deinitialize the IoTCon using the `iotcon_deinitialize()` function:

    ```
    iotcon_deinitialize();
    ```

<a name="register"></a>
## Registering Resources

To create and register resources:

1. Create the resource types using the `iotcon_resource_types_create()` function. The resource type string can be added using the `iotcon_resource_types_add()` function.

    ```
    int ret;
    const char *res_type = "org.tizen.light";
    iotcon_resource_types_h res_types = NULL;

    ret = iotcon_resource_types_create(&res_types);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_resource_types_add(res_types, res_type);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

2. Register the resource by calling the `iotcon_resource_create()` function.

   In the function, set the URI path, resource types, interfaces (`iotcon_resource_interfaces_h` resource interface handle in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#ga10fbc5191f6d83eaedbcbdeb3e1211a8) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#ga10fbc5191f6d83eaedbcbdeb3e1211a8) applications), policies (1 or more `iotcon_resource_policy_e` enumeration values in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#ga66063156ce698fa862cb9704be86494f) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#ga66063156ce698fa862cb9704be86494f)applications), and the request handler callback function called when a request arrives from a client.

    The URI path must be unique. The `iotcon_resource_create()` function fails, if you use an existing URI to register another resource.

    ```
    int res_interfaces = IOTCON_INTERFACE_DEFAULT;
    int res_properties = IOTCON_RESOURCE_DISCOVERABLE | IOTCON_RESOURCE_OBSERVABLE;
    const char *res_uri = "/light/1";
    iotcon_resource_h resource = NULL;

    ret = iotcon_resource_create(res_uri, res_types, res_interfaces, res_properties,
                                 _request_handler, NULL, &resource);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

3. When no longer needed, destroy the resource types handle using the `iotcon_resource_types_destroy()` function:
    ```
    iotcon_resource_types_destroy(resource_types);
    ```

<a name="find"></a>
## Finding Resources

To find resources:

1. To find a resource, call the `iotcon_find_resource()` function.

   In the function, set the host address, connectivity type (an `iotcon_connectivity_type_e` enumeration value in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#gad35385ec940df271d516337a17185453) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__COMMON__MODULE.html#gad35385ec940df271d516337a17185453) applications), query, secure flag, and the found callback function called whenever the resource is found during the timeout.

   The host address can be `IOTCON_MULTICAST_ADDRESS` for multicast.

    ```
    int ret;
    iotcon_query_h query;
    const char *res_type = "org.tizen.light";

    ret = iotcon_query_create(&query);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_query_set_resource_type(query, res_type);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_find_resource(IOTCON_MULTICAST_ADDRESS, IOTCON_CONNECTIVITY_IP | IOTCON_CONNECTIVITY_PREFER_UDP,
                               res_type, query, _found_cb, NULL);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

2. To get the remote resource handle information, use the found callback registered in the `iotcon_find_resource()` function:

    ```
    static bool
    _found_cb(iotcon_remote_resource_h resource, iotcon_error_e err, void *user_data)
    {
        int ret;
        char *address;
        char *uri_path;

        if (IOTCON_ERROR_NONE != err)
            /* Error handling */

        ret = iotcon_remote_resource_get_host_address(resource, &address);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */
        dlog_print(DLOG_DEBUG, LOG_TAG, "host_address: %s", address);

        ret = iotcon_remote_resource_get_uri_path(resource, &uri_path);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */
        dlog_print(DLOG_DEBUG, LOG_TAG, "uri_path: %s", uri_path);
    }
    ```

   > **Note**
   >
   > The callback parameters are valid only within the callback function. Use the clone handle, if you want to use a parameter after the callback function.

3. To set the timeout interval (in seconds) for the asynchronous functions of the Client (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__MODULE.html) applications) and Remote Resource (in [mobile](../../api/mobile/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__REMOTE__RESOURCE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__IOT__CONNECTIVITY__CLIENT__REMOTE__RESOURCE__MODULE.html) applications) APIs, use the `iotcon_set_timeout()` function:

    ```
    int ret;
    ret = iotcon_set_timeout(10);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

   > **Note**
   >
   > The `iotcon_set_timeout()` function has an effect on the following asynchronous functions:
   > - `iotcon_find_resource()`
   > - `iotcon_find_device_info()`
   > - `iotcon_find_platform_info()`
   > - `iotcon_remote_resource_get()`
   > - `iotcon_remote_resource_put()`
   > - `iotcon_remote_resource_post()`
   > - `iotcon_remote_resource_delete()`

<a name="send_get"></a>
## Sending GET Requests

To send GET requests to a server:

1. On the client side, clone the remote resource handle using the found callback registered in the `iotcon_find_resource()` function:

    ```
    static iotcon_remote_resource_h _light_resource = NULL;

    static bool
    _found_cb(iotcon_remote_resource_h resource, iotcon_error_e err, void *user_data)
    {
        int ret;

        if (IOTCON_ERROR_NONE != err)
            /* Error handling */

        ret = iotcon_remote_resource_clone(resource, &_light_resource);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */
    }
    ```

2. Send the GET request to the server using the `iotcon_remote_resource_get()` function.

    In the function, set the remote resource, query, and the response callback function called when receiving a response from the resource.

    ```
    int ret;

    ret = iotcon_remote_resource_get(_light_resource, NULL, _on_get, NULL);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

3. On the server side, the `_request_handler()` callback function is called when a request arrives from the client. The resource and request handles are passed to the callback.

    Use the callback to get the request information from the request handle, create a representation handle (with the `_get_repr()` function), and sent a response back to the client (with the `_send_response()` function):

    ```
    static void
    _request_handler(iotcon_resource_h resource, iotcon_request_h request, void *data)
    {
        int ret;
        iotcon_request_type_e req_type;
        iotcon_response_result_e result = IOTCON_RESPONSE_ERROR;
        iotcon_representation_h repr = NULL;

        ret = iotcon_request_get_type(request, &req_type);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        switch (req_type) {
        case IOTCON_REQUEST_GET:
            ret = _get_repr(resource, &repr);
            if (0 == ret)
                result = IOTCON_RESPONSE_OK;
            break;
        default:
            dlog_print(DLOG_DEBUG, LOG_TAG, "type: %d", req_type);
        }

        _send_response(request, repr, result);
        if (repr)
            iotcon_representation_destroy(repr);
    }
    ```

4. To process the GET request, the server must create the representation handle, which includes the resource attributes:

   ```
   static int _light_brightness;

   int
   _get_repr(iotcon_resource_h resource, iotcon_representation_h *representation)
   {
       int ret;
       char *uri_path;
       int interfaces;
       iotcon_resource_types_h res_types;
       iotcon_attributes_h attr;
       iotcon_representation_h repr;

       ret = iotcon_representation_create(&repr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_attributes_create(&attr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_resource_get_uri_path(resource, &uri_path);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_representation_set_uri_path(repr, uri_path);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_attributes_add_int(attr, "brightness", _light_brightness);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_representation_set_attributes(repr, attr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */
       iotcon_attributes_destroy(attr);

       *representation = repr;

       return 0;
   }
   ```

5. To send a response to the client, use the `iotcon_response_send()` function.

   In the function, set the response handle that can include the mandatory response result and optional representation.

    ```
    void
    _send_response(iotcon_request_h request, iotcon_representation_h repr, iotcon_response_result_e result)
    {
        int ret;
        iotcon_response_h resp;

        ret = iotcon_response_create(request, &resp);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        ret = iotcon_response_set_result(resp, result);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        if (repr) {
            ret = iotcon_response_set_representation(resp, repr);
            if (IOTCON_ERROR_NONE != ret)
                /* Error handling */
        }

        ret = iotcon_response_send(resp);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        iotcon_response_destroy(resp);
    }
    ```

6. On the client side, the response callback is called when the response arrives from the server. Handle the response appropriately. If the response is a success, the resource information can be included in it.

   ```
   static void
   _parse_representation(iotcon_representation_h repr)
   {
       int ret;
       int brightness;
       iotcon_attributes_h attr = NULL;

       ret = iotcon_representation_get_attributes(repr, &attr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_attributes_get_int(attr, "brightness", &brightness);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */
       dlog_print(DLOG_DEBUG, LOG_TAG, "Brightness: %d", brightness);
   }

   static void
   _on_get(iotcon_remote_resource_h resource, iotcon_error_e err,
           iotcon_request_type_e request_type, iotcon_response_h response, void *user_data)
   {
       int ret;
       iotcon_representation_h repr;
       iotcon_response_result_e result;

       if (IOTCON_ERROR_NONE != err)
           /* Error handling */

       ret = iotcon_response_get_result(response, &result);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       if (IOTCON_RESPONSE_OK != result)
           /* Error handling */

       ret = iotcon_response_get_representation(response, &repr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       _parse_representation(repr);
   }
   ```

<a name="send_put"></a>
## Sending PUT Requests

To send PUT requests to a server:

1. To send a PUT request to the server, use the `iotcon_remote_resource_put()` function.

   First create the representation and attributes, and set the desired attribute values, and then send the representation using `iotcon_remote_resource_put()` function.

    ```
    int ret;
    iotcon_representation_h repr;
    iotcon_attributes_h attr;

    ret = iotcon_representation_create(&repr);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_attributes_create(&attr);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_attributes_add_int(attr, "brightness", 20);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    ret = iotcon_representation_set_attributes(repr, attr);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    iotcon_attributes_destroy(attr);

    ret = iotcon_remote_resource_put(_light_resource, repr, NULL, _on_put, NULL);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */

    iotcon_representation_destroy(repr);
    ```

2. On the server side, the request handler function is called when a request arrives from the client. The resource and request handles are passed to the handler callback.

   You can get the request information from the request handle.

   ```
   static void
   _handle_put(iotcon_request_h request)
   {
       int ret;
       int value;
       iotcon_representation_h repr;
       iotcon_attributes_h attr;

       ret = iotcon_request_get_representation(request, &repr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_representation_get_attributes(repr, &attr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       ret = iotcon_attributes_get_bool(attr, "brightness", &value);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       _light_brightness = value;
   }

   static void
   _request_handler(iotcon_resource_h resource, iotcon_request_h request, void *data)
   {
       int ret;
       iotcon_request_type_e req_type;
       iotcon_response_result_e result = IOTCON_RESPONSE_ERROR;
       iotcon_representation_h repr = NULL;

       ret = iotcon_request_get_request_type(request, &req_type);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       switch (req_type) {
       case IOTCON_REQUEST_PUT:
           _handle_put(request);
           ret = _get_repr(resource, &repr);
           if (0 == ret)
               result = IOTCON_RESPONSE_OK;
           break;
       default:
           dlog_print(DLOG_DEBUG, LOG_TAG, "type: %d", req_type);
       }

       _send_response(request, repr, result);
       if (repr)

           iotcon_representation_destroy(repr);
   }
   ```

3. On the client side, the response callback is called when the response arrives from the server. If the response is a success, the resource information can be included in it.

   ```
   static void
   _on_put(iotcon_remote_resource_h resource, iotcon_error_e err,
           iotcon_request_type_e request_type, iotcon_response_h response, void *user_data)
   {
       int ret;
       iotcon_representation_h repr;
       iotcon_response_result_e result;

       if (IOTCON_ERROR_NONE != err)
           /* Error handling */

       ret = iotcon_response_get_result(response, &result);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       if (IOTCON_RESPONSE_OK != result)
           /* Error handling */

       ret = iotcon_response_get_representation(response, &repr);
       if (IOTCON_ERROR_NONE != ret)
           /* Error handling */

       _parse_representation(repr);
   }
   ```

<a name="observe"></a>
## Observing Resources

To monitor the changes in a resource:

1. If the resource is observable, the client can register a callback to observe the resource using the `iotcon_remote_resource_observe_register()` function:

    ```
    int ret;

    ret = iotcon_remote_resource_observe_register(_light_resource, IOTCON_OBSERVE_IGNORE_OUT_OF_ORDER,
                                                  NULL, _observe_cb, NULL);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

2. On the server side, the request handler callback is called when the observe request arrives from the client. To manage the observers, use the `iotcon_observers_h` handle.

    ```
    static iotcon_observers_h _observers;

    static void
    _handle_observe(iotcon_request_h request, bool is_register)
    {
        int ret;
        int observe_id;

        ret = iotcon_request_get_observe_id(request, &observe_id);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        if (is_register) {
            if (NULL == _observers) {
                ret = iotcon_observers_create(&_observers);
                if (IOTCON_ERROR_NONE != ret)
                    /* Error handling */
            }
            ret = iotcon_observers_add(_observers, observe_id);
            if (IOTCON_ERROR_NONE != ret)
                /* Error handling */
        } else {
            ret = iotcon_observers_remove(_observers, observe_id);
            if (IOTCON_ERROR_NONE != ret)
                /* Error handling */
        }
    }

    static void
    _request_handler(iotcon_resource_h resource, iotcon_request_h request, void *data)
    {
        int ret;
        iotcon_observe_type_e observe_type;

        ret = iotcon_request_get_observe_type(request, &observe_type);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        switch (observe_type) {
        case IOTCON_OBSERVE_REGISTER:
            _handle_observe(request, true);
            break;
        case IOTCON_OBSERVE_DEREGISTER:
            _handle_observe(request, false);
            break;
        case IOTCON_OBSERVE_NO_TYPE:
        default:
            dlog_print(DLOG_DEBUG, LOG_TAG, "type: %d", observe_type);
        }
    }
    ```

3. When a resource changes, notify the observing client using the `iotcon_resource_notify()` function. The second parameter can be `NULL` to notify all observers.

    ```
    int ret;
    iotcon_representation_h repr = NULL;

    ret = _get_repr(resource, &repr);
    if (0 != ret)
        /* Error handling */

    ret = iotcon_resource_notify(resource, _observers, repr, IOTCON_QOS_HIGH);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    if (repr)
        iotcon_representation_destroy(repr);
    ```

4. On the client side, the `_observe_cb()` callback is called when the notify function is called from the server side. The remote resource handle, sequence number, and response handle are passed to the callback.

    ```
    static void
    _observe_cb(iotcon_remote_resource_h resource, iotcon_error_e err,
                int sequence_number, iotcon_response_h response, void *user_data)
    {
        int ret;
        iotcon_representation_h repr;

        if (IOTCON_ERROR_NONE != err)
            /* Error handling */
        dlog_print(DLOG_DEBUG, LOG_TAG, "sequence: %d", sequence_number);

        ret = iotcon_response_get_representation(response, &repr);
        if (IOTCON_ERROR_NONE != ret)
            /* Error handling */

        _parse_representation(repr);
    }
    ```

5. When the client no longer needs to monitor the resource, deregister the observation callback with the `iotcon_remote_resource_observe_deregister()` function:

    ```
    int ret;

    ret = iotcon_remote_resource_observe_deregister(_light_resource);
    if (IOTCON_ERROR_NONE != ret)
        /* Error handling */
    ```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
