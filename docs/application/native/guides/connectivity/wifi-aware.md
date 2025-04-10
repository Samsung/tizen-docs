# Wi-Fi Aware&reg;

Wi-Fi Aware&reg; is a technology that enable devices to discover and connect directly to each other without any other type of connectivity between them or without wireless access points (base stations) in the infrastructure mode. Wi-Fi Aware is a synonym for Wi-Fi NAN (Neighbor Awareness Networking).

Wi-Fi Aware networking operates by establishing clusters. A Wi-Fi Aware device can join an existing cluster or create a new cluster if that device is the first in the area. Once a cluster is established, devices can start service discovery and messaging using publish, subscribe and send message APIs. After service discovery data path can be established by devices to send and receive data over network layer.
## Features

The main features of the Wi-Fi Aware API include the following:

- Initialization and deinitialization of Wi-Fi Aware functionalities.
  You can initialize Wi-Fi Aware functionalities using the `wifi_aware_initialize()` API, and deinitialize them using the `wifi_aware_deinitialize()` API. These APIs allow you to initialize and deinitialize the Wi-Fi Aware module in your application.

- Enabling and disabling Wi-Fi Aware functionalities.
  You can [enable](#enabling-wi-fi-aware) or [disable](#disabling-wi-fi-aware) Wi-Fi Aware functionalities.

- Creating and destroying Wi-Fi Aware sessions.
  You can [create a new Wi-Fi Aware session](#session-creation) and [destroy an existing session](#disabling-wi-fi-aware).

- Starting and Stopping Wi-Fi Aware sessions.
  Based on session type you can [start publish session](#publish-service) or [subscribe session](#subscribe-service).
  You can [stop an active Wi-Fi Aware session](#stop-service-discovery).

- Updating existing publish session.
  You can update an existing publish session using the `wifi_aware_session_update_publish()` API. This allows you to modify the parameters of an ongoing publish service session.

- Updating existing subscribe session.
  You can update an existing subscription using the `wifi_aware_session_update_subscribe()` API. This allows you to modify the parameters of an ongoing subscribe service session.

- Sending messages to peers.
  You can [send messages to peers](#send-message).

- Setting up data paths between peers
  You can [set up data path](#data-path-setup) between peers.

Overall, the Wi-Fi Aware module provides a comprehensive set of APIs to control and interact with Wi-Fi Aware functionalities, allowing developers to leverage the power of Wi-Fi Aware for direct device-to-device communication.

> [!NOTE]
> You can test the Wi-Fi Aware functionality on a target device only. The [emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.

## Prerequisites

To enable your application to use the Wi-Fi Aware functionality, follow these steps:

1. To use the [Wi-Fi Aware](../../api/common/latest/group__CAPI__NETWORK__WIFI__AWARE__MODULE.html) API, the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/wifiaware</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Wi-Fi Aware API, include the `<wifi_aware.h>` header file in your application:

   ```
   #include <wifi_aware.h>
   ```

3. Call the `wifi_aware_initialize()` function to initialize Wi-Fi Aware module:

   ```
	int error_code;
	error_code = wifi_aware_initialize();
   ```

<a name="Enable"></a>
## To enable Wi-Fi Aware

Enabling Wi-Fi Aware allows you to start the Wi-Fi Aware daemon service (aka NAN-manager) on your device, which allows you to control the availability of Wi-Fi Aware capabilities and Wi-Fi Aware operations, such as, service discovery, data path creation, etc., on the device.
To enable a Wi-Fi Aware local device, use the following steps:

1. Define callbacks for the Wi-Fi Aware enable/disable events:

   Define the `wifi_aware_enabled_cb()` and `wifi_aware_disabled_cb()` callback function, which are invoked whenever a Wi-Fi Aware local device enables or disables. In the following example, an information message is printed in the console.

   ```
	static void __wifi_aware_enabled_cb(wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware is enabled\n");
		else
			printf("Wi-Fi Aware is not enabled. Error: %d\n", error);
	}

	static void __wifi_aware_disabled_cb(wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware is disabled\n");
		else
			printf("Wi-Fi Aware is not disabled. Error: %d\n", error);
	}
   ```

2. Enable the Wi-Fi Aware local device:

   After the `wifi_aware_enable()` function is completed, the `wifi_aware_enabled_cb()` callback is invoked.

   ```
	error_code = wifi_aware_enable(__wifi_aware_enabled_cb, NULL);
   ```

<a name="session_creation"></a>
## Session Creation

Wi-Fi Aware session will be required to perform Wi-Fi Aware operations such as, service discovery, data path creation, etc., on the device.
To create a Wi-Fi Aware session:

1. For Wi-Fi Aware publish session handle use `wifi_aware_session_create()` function with type `WIFI_AWARE_SESSION_PUBLISH`:
   ```
	wifi_aware_session_h session_handle;
	int error_code;
	error_code = wifi_aware_session_create(WIFI_AWARE_SESSION_PUBLISH, &session_handle);
   ```
   If session creation is successful then session handle will be created otherwise it will return error code.
   If session creation fails then session handle will be `NULL`.

   Set callbacks for Wi-Fi Aware publish session events:
   Define the `wifi_aware_message_received_cb()` callback function, which are invoked whenever a message is received from subscriber. In the following example, an information message is printed in the console.

   ```
	static void __wifi_aware_message_received_cb(wifi_aware_session_h session, const unsigned char *message, int message_len, void *user_data)
	{
		printf("Message received: %s\n", message);
		// Handle message reception here
	}
   ```
   Set callback for message reception event using `wifi_aware_session_set_message_received_cb()` function.
   ```
	int error_code;
	error_code = wifi_aware_session_set_message_received_cb(session_handle, __wifi_aware_message_received_cb, NULL);
   ```

2. For Wi-Fi Aware subscribe session handle use `wifi_aware_session_create()` function with type `WIFI_AWARE_SESSION_SUBSCRIBE`:
   ```
	wifi_aware_session_h session_handle;
	int error_code;
	error_code = wifi_aware_session_create(WIFI_AWARE_SESSION_SUBSCRIBE, &session_handle);
   ```
   If session creation is successful then session handle will be created otherwise it will return error code.
   If session creation fails then session handle will be `NULL`.

   Set callbacks for Wi-Fi Aware subscribe session events:
   Define the `wifi_aware_service_discovered_cb()` and `wifi_aware_message_received_cb()` callback function, which are invoked whenever a Wi-Fi Aware service publisher is discovered or a message is received from publisher. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_service_discovered_cb(wifi_aware_session_h session, const char *service_name, const unsigned char *service_specific_info, int ssi_len, const char *match_filter, int match_filter_len, int distance_mm, void *user_data)
	{
		printf("Service discovered: %s\n", service_name);
		printf("Service Specific Info: %s\n", service_specific_info);
		// Handle service discovery here
	}

	static void __wifi_aware_message_received_cb(wifi_aware_session_h session, const unsigned char *message, int message_len, void *user_data)
	{
		printf("Message received: %s\n", message);
		// Handle message reception here
	}
   ```
   Set callback for service discovery event using `wifi_aware_session_set_service_discovered_cb()` function.
   ```
	int error_code;
	error_code = wifi_aware_session_set_service_discovered_cb(session_handle, __wifi_aware_service_discovered_cb, NULL);
   ```
   Set callback for message reception event using `wifi_aware_session_set_message_received_cb()` function.
	```
	int error_code;
	error_code = wifi_aware_session_set_message_received_cb(session_handle, __wifi_aware_message_received_cb, NULL);
   ```
   If callback setting is successful then it will return `WIFI_AWARE_ERROR_NONE` otherwise it will return error code.

<a name="service_discovery"></a>
## Service Discovery

This is the process of publishing or subscribing to Wi-Fi Aware services that will advertise and discover Wi-Fi Aware services respectively.
To perform Wi-Fi Aware service discovery:

<a name="publish_service"></a>
### Publish Service

To publish a Wi-Fi Aware service:

1. Create a Wi-Fi Aware publish session and create a publish handle using `wifi_aware_publish_create()` function.
   ```
	wifi_aware_publish_h publish_handle;
	int error_code;
	error_code = wifi_aware_publish_create(&publish_handle);
   ```

2. Set publish parameters using `wifi_aware_publish_set_service_name()`, `wifi_aware_publish_set_type()`, `wifi_aware_publish_set_service_specific_info()`, `wifi_aware_publish_set_match_filter()` and `wifi_aware_publish_set_ttl()` functions.
   ```
	int error_code;
	error_code = wifi_aware_publish_set_service_name(publish_handle, "MyServiceName");
	error_code = wifi_aware_publish_set_type(publish_handle, WIFI_AWARE_PUBLISH_TYPE_UNSOLICITED);
	error_code = wifi_aware_publish_set_service_specific_info(publish_handle, "MyServiceSpecificInfo", strlen("MyServiceSpecificInfo"));
	error_code = wifi_aware_publish_set_ttl(publish_handle, 10);
   ```

3. Define `wifi_aware_published_cb` callback function which is invoked whenever a Wi-Fi Aware service is published successfully or failed. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_published_cb(wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware service published successfully\n");
		else
			printf("Wi-Fi Aware service not published. Error: %d\n", error);
	}
   ```

4. Publish service using `wifi_aware_session_publish()` function with publish handle and callback function.
   ```
	int error_code;
	error_code = wifi_aware_session_publish(session_handle, publish_handle, __wifi_aware_published_cb, NULL);
   ```

<a name="subscribe_service"></a>
### Subscribe Service

To subscribe to a Wi-Fi Aware service:

1. Create a Wi-Fi Aware subscribe session and create a subscribe handle using `wifi_aware_subscribe_create()` function.
   ```
	wifi_aware_subscribe_h subscribe_handle;
	int error_code;
	error_code = wifi_aware_subscribe_create(&subscribe_handle);
   ```

2. Set subscribe parameters using `wifi_aware_subscribe_set_service_name()`, `wifi_aware_subscribe_set_type()`, `wifi_aware_subscribe_set_service_specific_info()`, `wifi_aware_subscribe_set_match_filter()` and `wifi_aware_subscribe_set_ttl()` functions.
   ```
	int error_code;
	error_code = wifi_aware_subscribe_set_service_name(subscribe_handle, "MyServiceName");
	error_code = wifi_aware_subscribe_set_type(subscribe_handle, WIFI_AWARE_SUBSCRIBE_TYPE_PASSIVE);
	error_code = wifi_aware_subscribe_set_service_specific_info(subscribe_handle, "MyServiceSpecificInfo", strlen("MyServiceSpecificInfo"));
	error_code = wifi_aware_subscribe_set_ttl(subscribe_handle, 10);
   ```

3. Define `wifi_aware_subscribed_cb` callback function which is invoked whenever a Wi-Fi Aware service is subscribed successfully or failed. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_subscribed_cb(wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware service subscribed successfully\n");
		else
			printf("Wi-Fi Aware service not subscribed. Error: %d\n", error);
	}
   ```

4. Subscribe service using `wifi_aware_session_subscribe()` function with subscribe handle and callback function.
   ```
	int error_code;
	error_code = wifi_aware_session_subscribe(session_handle, subscribe_handle, __wifi_aware_subscribed_cb, NULL);
   ```

<a name="send_message"></a>
### Send Message

This allows you to exchange messages with other devices within the same Wi-Fi Aware cluster.
To send a message to a Wi-Fi Aware peer:

1. Define `wifi_aware_send_message_result_cb` callback function which is invoked whenever a Wi-Fi Aware message is sent successfully or failed. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_send_message_result_cb(wifi_aware_session_h session, wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware message sent successfully\n");
		else
			printf("Wi-Fi Aware message not sent. Error: %d\n", error);
	}
   ```

2. Send message using `wifi_aware_session_send_message()` function with session handle, peer handle, message and callback function.
   ```
	int error_code;
	unsigned char message[] = "Hello World!";
	error_code = wifi_aware_session_send_message(session_handle, peer, message, sizeof(message), __wifi_aware_send_message_result_cb, NULL);
   ```
   Peer handle can be found in either `service_discovered_cb` or `message_received_cb` callback functions.

   Sent message will be received by peer in `message_received_cb` callback function.

<a name="stop_session"></a>
### Stop Service Discovery

This allows user to gracefully terminate an ongoing session by cancelling the service discovery process.
To stop a Wi-Fi Aware service discovery session:

1. Set callbacks for Wi-Fi Aware session events:
   Define the `wifi_aware_session_terminated_cb()` callback function, which is invoked whenever a Wi-Fi Aware session terminates. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_session_terminated_cb(wifi_aware_error_e error, void *user_data)
	{
		if (error == WIFI_AWARE_ERROR_NONE)
			printf("Wi-Fi Aware session terminated\n");
		else
			printf("Wi-Fi Aware session not terminated. Error: %d\n", error);
	}
   ```
   Set callback for session termination event using `wifi_aware_session_set_terminated_cb()` function.
   ```
	int error_code;
	error_code = wifi_aware_session_set_terminated_cb(session_handle, __wifi_aware_session_terminated_cb, NULL);
   ```
   If callback setting is successful then it will return `WIFI_AWARE_ERROR_NONE` otherwise it will return error code.

2. Stop Wi-Fi Aware session using `wifi_aware_session_stop()` function.
   ```
	int error_code;
	error_code = wifi_aware_session_stop(session_handle);
   ```

<a name="data_path_setup"></a>
## Data Path Setup

Data path can be setup only after service discovery is done and peer is found on both devices.
Data path allows devices to establish communication channels for data transfer over network layer.

1. After service discovery is completed, prepare Wi-Fi Aware data path handle using `wifi_aware_data_path_create()` function.
   ```
	wifi_aware_data_path_h data_path_handle;
	int error_code;
	error_code = wifi_aware_data_path_create(session_handle, peer, &data_path_handle);
   ```

2. Define `wifi_aware_data_path_opened_cb` and ` wifi_aware_data_path_terminated_cb` callback functions which are invoked whenever a Wi-Fi Aware data path is opened successfully or failed and whenever data path is terminated respectively. In the following example, an information message is printed in the console.
   ```
	static void __wifi_aware_data_path_opened_cb(wifi_aware_data_path_h data_path, wifi_aware_error_e error, void *user_data)
	{
		printf("Wi-Fi Aware data path opened\n");
		// Handle data path open here
	}
	static void __wifi_aware_data_path_terminated_cb(wifi_aware_data_path_h data_path, wifi_aware_termination_reason_e reason, void *user_data)
	{
		printf("Wi-Fi Aware data path terminated\n");
		// Handle data path termination here
	}
   ```
   Set callback for data path terminated event using `wifi_aware_data_path_set_terminated_cb()` function.
   ```
	int error_code;
	error_code = wifi_aware_data_path_set_terminated_cb(data_path_handle, __wifi_aware_data_path_terminated_cb, NULL);
   ```

3. Set data path parameters like security type, passphrase or pmk, port, etc. using `wifi_aware_data_path_set_security()`, `wifi_aware_data_path_set_psk()`, `wifi_aware_data_path_set_pmk()` and `wifi_aware_data_path_set_port()` functions.
   ```
	int error_code;
	error_code = wifi_aware_data_path_set_security(data_path_handle, WIFI_AWARE_SECURITY_TYPE_PSK);
	error_code = wifi_aware_data_path_set_psk(data_path_handle, "MyPassphrase");
	error_code = wifi_aware_data_path_set_port(data_path_handle, 12345);
   ```

4. Open data path using `wifi_aware_data_path_open()` function with data path handle and callback function.
   ```
	int error_code;
	error_code = wifi_aware_data_path_open(data_path_handle, __wifi_aware_data_path_opened_cb, NULL);
   ```

<a name="data_path_terminate"></a>
### Terminate Established Data Path

To terminate an established Wi-Fi Aware data path:

1. Terminate data path using `wifi_aware_data_path_close()` function.
   ```
	int error_code;
	error_code = wifi_aware_data_path_close(data_path_handle);
   ```

2. Destroy data path handle using `wifi_aware_data_path_destroy()` function.
   ```
	int error_code;
	error_code = wifi_aware_data_path_destroy(data_path_handle);
   ```

<a name="Disabling"></a>
## To disable Wi-Fi Aware

To disable Wi-Fi Aware when it is no longer needed (or the application is exiting):

1. Stop any existing Wi-Fi Aware session, then destroy the session handle using `wifi_aware_session_stop()` and `wifi_aware_session_destroy()` functions respectively.
   ```
	int error_code;
	error_code = wifi_aware_session_destroy(session_handle);
   ```

2. Power off the local device using the `wifi_aware_disable()` function:

   ```
	wifi_aware_disbale(__wifi_aware_disabled_cb, NULL);
   ```

3. Release Wi-Fi Aware:

   ```
	wifi_aware_deinitialize();
   ```

## Related information
- Dependencies
  - Tizen 9.0 and Higher for Mobile
- API References
  - [Wi-Fi Aware](../../api/common/latest/group__CAPI__NETWORK__WIFI__AWARE__MODULE.html)
