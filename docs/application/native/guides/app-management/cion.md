# Cion

The Cion API provides functionality to communicate with other devices.

The main features of the Cion API include:

- Communicating with other applications in server-client style.

  You can communicate with other applications in [server-client](#server_client) style.

- Communicating with other applications in group style.

  You can communicate with other applications in [group](#group) style.

- Supporting TIDL

  You can generate communication code using [TIDL](#tidl).

## Prerequisites

1.  To use the [Cion API](../../api/common/latest/group__CAPI__CION__MODULE.html), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

    ```xml
    <privileges>
       <privilege>http://tizen.org/privilege/d2d.datasharing</privilege>
       <privilege>http://tizen.org/privilege/internet</privilege>
    </privileges>
    ```

2.  To use the functions of the Cion API, include the `<cion.h>` header file in your application:

    ```cpp
    #include <cion.h>
    ```

<a name="server_client"></a>
## Communicate in server-client style

Cion API provides functions to communicate with the other applications in server-client style.

The Cion client can try to discover the server to communicate; If the server is discovered, the client can try to connect to it.
After the client connects to the server, it can send data and payload.

Cion client can be used as follows:

1. Create the client handle:

    ```cpp
    int ret;
    cion_client_h client;

	ret = cion_client_create(&client, "TEST_SERVICE", NULL);
    ```

2. Discover the server to connect:

    ```cpp
    static void __client_server_discovered_cb(const char *service_name,
		const cion_peer_info_h peer_info, void *user_data)
    {
    }
    ```
    ```cpp
    ret = cion_client_try_discovery(client, __client_server_discovered_cb, NULL);
    ```

3. Connect to the server:

    ```cpp
    ret = cion_client_connect(client, peer_info);
    ```

    > [!NOTE]
    > You can get the `peer_info` from discovered callback function.

    > [!NOTE]
    > You can add callback function using `cion_client_add_connection_result_cb` to get the connection result.

4. Send the data:

    ```cpp
    unsigned char str[] = "test_data";
    unsigned char *return_data = NULL,
    unsigned int return_size;

    ret = cion_client_send_data(client, strlen((const char*)str), 5000, &return_data, &return_size);
    ```
5. Send the payload:

    ```cpp
    static void __cion_client_payload_async_result_cb(
        const cion_payload_async_result_h result, void *user_data);
    ```
    ```cpp
    cion_payload_h payload;
    unsigned char data[] = "test_payload";

    ret = cion_payload_create(&payload, CION_PAYLOAD_TYPE_DATA);
    ret = cion_payload_set_data(payload, data, sizeof(data));

    ret = cion_client_send_payload_async(client, payload, __cion_client_payload_async_result_cb, NULL);
    ```

The Cion server can listen to the request from the client; if a connection request comes from the client, the server can accept it.
After the connection is accepted, the server can receive data and payload.

Cion server can be used as follows:

1. Create the server handle:

    ```cpp
    cion_server_h server;

    ret = cion_server_create(&server, "TEST_SERVICE", "MY_DISPLAY_NAME", NULL);
    ```

2. The server starts to listen to the requests from the client:

    ```cpp
    static void __cion_server_connection_request_cb(const char *service_name,
        const cion_peer_info_h peer_info, void *user_data) 
    {
    }
    ```
    ```cpp
    int cion_server_listen(server, __cion_server_connection_request_cb, void *user_data);
    ```

3. Accept the connection:

    ```cpp
    ret = cion_server_accept(server, peer_info);
    ```

    > [!NOTE]
    > You can get the `peer_info` from connection request callback function.

4. Add the callback function to receive data and payload:

    ```cpp
    static void __server_data_received_cb(const char *service_name,
	    const cion_peer_info_h peer_info, const unsigned char *data,
		unsigned int data_size, unsigned char **return_data,
		unsigned int *return_data_size, void *user_data)
    {
    }
    ```
    ```cpp
    ret = cion_server_set_data_received_cb(server, __server_data_received_cb, NULL);
    ```

    ```cpp
    static void __server_payload_received_cb(const char *service_name,
		const cion_peer_info_h peer_info, const cion_payload_h payload,
		cion_payload_transfer_status_e status,
		void *user_data)
    {
    }
    ```
    ```cpp
    ret = cion_server_add_payload_received_cb(server, __server_payload_received_cb, NULL);
    ```

<a name="group"></a>
## Communicate in group style

The Cion API provides functions to communicate with the other applications in group style.

The Cion group is used to share data with other group members. The group members can subscribe to the topic to join the group.
If the data is published, subscribed members receive it.

1. Create the group handle:

    ```cpp
    cion_group_h group;

	ret = cion_group_create(&group, "test_topic", NULL);
    ```

2. Subscribe the topic:

    ```cpp
    ret = cion_group_subscribe(group);
    ```

3. Add callback function to receive payload:

    ```cpp
    static void __cion_group_payload_received_cb(const char *topic_name,
        const cion_peer_info_h peer_info, cion_payload_h payload, void *user_data)
    {
    }
    ```
    ```cpp
    ret = cion_group_add_payload_received_cb(group, __cion_group_payload_received_cb, NULL);
    ```

4. Publish the data:

    ```cpp
   	cion_payload_h payload;
	unsigned char data[] = "test data";

    ret = cion_payload_create(&payload, CION_PAYLOAD_TYPE_DATA);
    ret = cion_payload_set_data(payload, data, sizeof(data));

    ret = cion_group_publish(group, payload);
    ```


<a name="tidl"></a>
## TIDL support

Cion communication code can be generated using TIDL.

You can create `CionTest.tidl` file as follows:
```csharp
interface FileSample {
    int ShareFile(file myFile);
    int ShareFilesList(list<file> myFile);
    int ShareFilesArray(array<file> myFile);
}
```

You can compile tidl file to generate cion code as follows:
```
tidlc --cion -p -b -i CionTest.tidl -l C -o CionProxy
tidlc --cion -s -b -i CionTest.tidl -l C -o CionStub
```


## Related information
- Dependencies
  - Tizen 6.5 and Higher for Mobile
  - Tizen 6.5 and Higher for Wearable
  - Tizen 6.5 and Higher for iot
- API Reference
  - [Cion](../../api/common/latest/group__CAPI__CION__MODULE.html)
  - [Cion Client](../../api/common/latest/group__CAPI__CION__CLIENT__MODULE.html)
  - [Cion Group](../../api/common/latest/group__CAPI__CION__GROUP__MODULE.html)
  - [Cion Server](../../api/common/latest/group__CAPI__CION__SERVER__MODULE.html)
