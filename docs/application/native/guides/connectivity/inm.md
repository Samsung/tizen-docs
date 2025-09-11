# Intelligent Network Monitoring

The Intelligent Network Monitoring (INM) API provides comprehensive network monitoring and diagnostic capabilities for Tizen applications. This API enables real-time network state tracking, connection management, and advanced network diagnostics by leveraging both Tizen network daemons and underlying Linux network functions.

## Overview

The INM API offers a wide range of network monitoring features:

- **Network State Monitoring**: Real-time monitoring of cellular, Wi-Fi, and Ethernet connection states
- **Network Diagnostics**: IP conflict detection, TCP congestion monitoring, channel interference analysis
- **Connection Management**: Detailed information about network connections including IP configuration, DNS, and proxy settings
- **Wi-Fi Management**: Wi-Fi state monitoring, access point information, and scanning capabilities
- **Link Level Monitoring**: Low-level network interface monitoring including traffic statistics and routing information
- **Network Tools**: ARP requests, gateway checking, DNS lookup validation, and URL reachability testing

The INM API is designed for applications that need to:
- Monitor network connectivity and quality in real-time
- Diagnose network issues automatically
- Provide detailed network information to users
- Optimize application behavior based on network conditions
- Implement network-aware features and services

> [!NOTE]
> You can test the INM functionality on a target device only. The [Tizen emulator](../../../tizen-studio/common-tools/emulator.md) does not support this feature.
> The INM API is available since Tizen 5.0.

## Prerequisites

To enable your application to use the INM API, follow these essential setup steps:

### Required Privileges

The [INM API](../../api/common/latest/group__CAPI__NETWORK__INM__MODULE.html) requires specific privileges based on the functionality you intend to use:

1. **Basic Network Monitoring** (Required for all INM functions):
   ```xml
   <privileges>
      <privilege>http://tizen.org/privilege/network.get</privilege>
   </privileges>
   ```

2. **Network Statistics Reset** (Optional, for resetting statistics):
   ```xml
   <privileges>
      <privilege>http://tizen.org/privilege/network.set</privilege>
   </privileges>
   ```

> [!IMPORTANT]
> - The `http://tizen.org/privilege/network.get` privilege is mandatory for most INM API functions
> - Missing privileges will result in `INM_ERROR_PERMISSION_DENIED` errors
> - Add only the privileges your application actually needs to follow the principle of least privilege

### Header File Inclusion

To use the functions and data types of the INM API, include the `<inm.h>` header file in your application:

```cpp
#include <inm.h>
```

### Library Initialization and Cleanup

Proper initialization and cleanup are crucial for resource management and error-free operation:

#### Basic Initialization Pattern

```cpp
#include <inm.h>

int initialize_inm(inm_h *inm_handle)
{
    int ret = INM_ERROR_NONE;
    inm_h inm_handle = NULL;
    // Initialize the INM library
    ret = inm_initialize(&inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to initialize INM: %s\n", 
               get_error_string(ret));
        return ret;
    }
    
    printf("INM library initialized successfully\n");
    return INM_ERROR_NONE;
}

void cleanup_inm(inm_h inm_handle)
{
    if (inm_handle) {
        // Deinitialize the INM library
        int ret = inm_deinitialize(inm_handle);
        if (ret != INM_ERROR_NONE) {
            printf("Failed to deinitialize INM: %s\n", 
                   get_error_string(ret));
        } else {
            printf("INM library deinitialized successfully\n");
        }
    }
}
```

#### Recommended Usage Pattern

```cpp
int main()
{
    inm_h inm_handle = NULL;
    int ret = INM_ERROR_NONE;
    
    // Initialize INM
    ret = initialize_inm(&inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Application cannot continue without INM\n");
        return -1;
    }
    
    // Your application logic here
    // Use inm_handle for INM API calls
    
    // Cleanup before exit
    cleanup_inm(inm_handle);
    return 0;
}
```

### Error Handling Best Practices

1. **Always Check Return Values**: All INM API functions return error codes that should be checked
2. **Handle Initialization Failures Gracefully**: If initialization fails, your application should either exit or provide alternative functionality
3. **Cleanup Resources Properly**: Always call `inm_deinitialize()` when the INM handle is no longer needed


## Get Default Connection Info

This example demonstrates how to retrieve comprehensive information about the default network connection, including connection details, IP configuration, and network statistics.

### Complete Connection Information Example

```cpp
/**
 * @brief Retrieves comprehensive information about the current network connection
 * @return INM_ERROR_NONE on success, error code on failure
 * 
 * This function demonstrates how to:
 * - Initialize and deinitialize the INM library properly
 * - Get the current connection handle
 * - Retrieve connection details (type, state, interface name)
 * - Get IP address information
 * - Retrieve network statistics via link handle
 * - Properly clean up all allocated resources
 */
int get_current_connection_info(void)
{
    int ret = INM_ERROR_NONE;
    inm_h inm = NULL;                    // INM library handle
    inm_connection_h conn = NULL;        // Connection handle
    inm_link_h link = NULL;              // Link handle for network statistics
    
    // Connection information variables
    inm_connection_type_e network_type;  // Type of connection (WiFi, Cellular, etc.)
    inm_connection_state_e conn_state;   // State of connection
    char *if_name = NULL;                // Network interface name
    char *ip_addr = NULL;                // IP address
    unsigned long long rx_bytes = 0;     // Received bytes
    unsigned long long tx_bytes = 0;     // Sent bytes

    // Step 1: Initialize the INM library
    ret = inm_initialize(&inm);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to initialize INM library: %d\n", ret);
        return ret;
    }

    // Step 2: Get the default connection handle
    ret = inm_get_current_connection(inm, &conn);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get current connection: %d\n", ret);
        goto cleanup;
    }
    printf("Default connection handle obtained\n");

    // Step 3: Get basic connection information
    ret = inm_connection_get_link(conn, &link);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get link handle: %d\n", ret);
        goto cleanup;
    }

    ret = inm_connection_get_type(conn, &network_type);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get connection type: %d\n", ret);
        goto cleanup;
    }

    ret = inm_connection_get_state(conn, &conn_state);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get connection state: %d\n", ret);
        goto cleanup;
    }

    ret = inm_connection_get_network_interface_name(conn, &if_name);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get interface name: %d\n", ret);
        goto cleanup;
    }

    // Step 4: Display basic connection information
    printf("=== Basic Connection Info ===\n");
    printf("Connection Type: %d (%s)\n", network_type, 
           network_type == INM_CONNECTION_TYPE_WIFI ? "WiFi" :
           network_type == INM_CONNECTION_TYPE_CELLULAR ? "Cellular" :
           network_type == INM_CONNECTION_TYPE_ETHERNET ? "Ethernet" : "Unknown");
    printf("Connection State: %d (%s)\n", conn_state,
           conn_state == INM_CONNECTION_STATE_CONNECTED ? "Connected" :
           conn_state == INM_CONNECTION_STATE_DISCONNECTED ? "Disconnected" :
           conn_state == INM_CONNECTION_STATE_ASSOCIATION ? "Associating" :
           conn_state == INM_CONNECTION_STATE_CONFIGURATION ? "Configuring" : "Unknown");
    printf("Interface Name: %s\n", if_name);

    // Step 5: Get IP address information (IPv4)
    ret = inm_connection_get_ip_address(conn, INM_ADDRESS_FAMILY_IPV4, &ip_addr);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get IPv4 address: %d\n", ret);
        goto cleanup;
    }
    printf("IPv4 Address: %s\n", ip_addr);

    // Step 6: Get network statistics via link handle
    ret = inm_link_get_received_bytes(link, &rx_bytes);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get received bytes: %d\n", ret);
        goto cleanup;
    }

    ret = inm_link_get_sent_bytes(link, &tx_bytes);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get sent bytes: %d\n", ret);
        goto cleanup;
    }

    // Step 7: Display network statistics
    printf("=== Network Statistics ===\n");
    printf("Received Bytes: %llu bytes (%.2f MB)\n", rx_bytes, (double)rx_bytes / (1024 * 1024));
    printf("Sent Bytes: %llu bytes (%.2f MB)\n", tx_bytes, (double)tx_bytes / (1024 * 1024));
    printf("Total Traffic: %llu bytes (%.2f MB)\n", rx_bytes + tx_bytes, 
           (double)(rx_bytes + tx_bytes) / (1024 * 1024));

    printf("\nConnection information retrieved successfully\n");

cleanup:
    // Step 8: Clean up all allocated resources
    if (if_name) {
        free(if_name);
        if_name = NULL;
    }
    
    if (ip_addr) {
        free(ip_addr);
        ip_addr = NULL;
    }
    
    if (link) {
        inm_link_destroy(link);
        link = NULL;
    }
    
    if (conn) {
        inm_connection_destroy(&conn);
        conn = NULL;
    }
    
    if (inm) {
        inm_deinitialize(inm);
        inm = NULL;
    }
    
    return ret;
}
```

### Iterating Through All Connections

You can retrieve information about all available connections by using the connection iterator. This is useful when you need to monitor multiple network interfaces or find a specific type of connection:

```cpp
/**
 * @brief Iterates through all available connections and prints their information
 * @param inm_handle Initialized INM handle
 * @return INM_ERROR_NONE on success, error code on failure
 */
int iterate_all_connections(inm_h inm_handle)
{
    int ret = INM_ERROR_NONE;
    inm_connection_iterator_h iter = NULL;
    inm_connection_h conn = NULL;
    int connection_count = 0;

    printf("=== Iterating Through All Connections ===\n");

    // Get connection iterator
    ret = inm_get_connection_iterator(inm_handle, &iter);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get connection iterator: %d\n", ret);
        return ret;
    }

    // Iterate through all connections
    while ((ret = inm_connection_iterator_next(iter, &conn)) == INM_ERROR_NONE) {
        connection_count++;
        
        // Get connection details
        inm_connection_type_e conn_type;
        inm_connection_state_e conn_state;
        char *conn_name = NULL;
        char *if_name = NULL;
        
        if (inm_connection_get_type(conn, &conn_type) == INM_ERROR_NONE &&
            inm_connection_get_state(conn, &conn_state) == INM_ERROR_NONE &&
            inm_connection_get_name(conn, &conn_name) == INM_ERROR_NONE &&
            inm_connection_get_network_interface_name(conn, &if_name) == INM_ERROR_NONE) {
            
            printf("\n--- Connection %d ---\n", connection_count);
            printf("Name: %s\n", conn_name ? conn_name : "Unknown");
            printf("Interface: %s\n", if_name ? if_name : "Unknown");
            printf("Type: %d (%s)\n", conn_type,
                   conn_type == INM_CONNECTION_TYPE_WIFI ? "WiFi" :
                   conn_type == INM_CONNECTION_TYPE_CELLULAR ? "Cellular" :
                   conn_type == INM_CONNECTION_TYPE_ETHERNET ? "Ethernet" : "Unknown");
            printf("State: %d (%s)\n", conn_state,
                   conn_state == INM_CONNECTION_STATE_CONNECTED ? "Connected" :
                   conn_state == INM_CONNECTION_STATE_DISCONNECTED ? "Disconnected" :
                   conn_state == INM_CONNECTION_STATE_ASSOCIATION ? "Associating" :
                   conn_state == INM_CONNECTION_STATE_CONFIGURATION ? "Configuring" : "Unknown");
        }
        
        // Clean up connection-specific resources
        if (conn_name) free(conn_name);
        if (if_name) free(if_name);
        if (conn) inm_connection_destroy(&conn);
    }

    printf("\nTotal connections found: %d\n", connection_count);

    // Clean up iterator
    if (iter) {
        inm_destroy_connection_iterator(iter);
    }

    return (ret == INM_ERROR_DATA_NOT_FOUND) ? INM_ERROR_NONE : ret;
}
```

### Usage Example

Here's how to use these functions in your application:

```cpp
int main()
{
    inm_h inm_handle = NULL;
    int ret = INM_ERROR_NONE;

    // Initialize INM
    ret = inm_initialize(&inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to initialize INM: %d\n", ret);
        return -1;
    }

    // Get default connection information
    ret = get_default_connection_info();
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get default connection info: %d\n", ret);
    }

    // Iterate through all connections
    ret = iterate_all_connections(inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to iterate connections: %d\n", ret);
    }

    // Cleanup
    inm_deinitialize(inm_handle);
    return 0;
}
```

These examples provide a comprehensive guide for retrieving connection information using the INM API, with proper error handling, resource management, and detailed comments for better understanding.

## Monitor Wi-Fi State Change

### Define a callback function to process the Wi-Fi state change

```cpp
void __wifi_state_changed_cb(inm_wifi_state_e state,
                                            void *user_data)
{
    /* Do the necessary action when Wi-Fi state has changed */
}
```
    
### Set the Wi-Fi state change callback

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

## Network Diagnostics

The INM API provides powerful network diagnostic capabilities that help applications detect and analyze network issues in real-time. These features are essential for building network-aware applications that can automatically diagnose connectivity problems and provide users with actionable feedback.

### IP Conflict Detection

IP conflict detection is a critical network diagnostic feature that identifies when multiple devices on the same network are using the same IP address. This can cause network connectivity issues and unpredictable behavior.

#### Overview

IP conflicts occur when two or more devices on the same network segment are configured with the same IP address. The INM API provides automatic detection of IP conflicts and notifies applications through callback mechanisms.

#### Key Features

- **Automatic Detection**: Continuously monitors for IP conflicts on all network interfaces
- **Real-time Notifications**: Immediate callback when conflicts are detected or resolved
- **Interface-specific Information**: Provides the interface name and conflicting IP address
- **Configurable Monitoring**: Can be enabled or disabled based on application needs

#### Implementation

```cpp
/**
 * @brief Callback function for IP conflict detection
 * @param if_name Network interface name where conflict was detected
 * @param ip IP address that has the conflict
 * @param state Current conflict state
 * @param user_data User-provided data passed to the callback
 */
void ip_conflict_callback(char *if_name, char *ip, inm_ip_conflict_state_e state, void *user_data)
{
    printf("IP Conflict Detection Callback:\n");
    printf("  Interface: %s\n", if_name ? if_name : "Unknown");
    printf("  IP Address: %s\n", ip ? ip : "Unknown");
    
    switch (state) {
    case INM_IP_CONFLICT_STATE_CONFLICT_DETECTED:
        printf("  Status: CONFLICT DETECTED!\n");
        printf("  Action: Check network configuration and restart DHCP if needed\n");
        break;
    case INM_IP_CONFLICT_STATE_CONFLICT_NOT_DETECTED:
        printf("  Status: No conflict detected\n");
        break;
    case INM_IP_CONFLICT_STATE_UNKNOWN:
    default:
        printf("  Status: Unknown state\n");
        break;
    }
    
    // You can add application-specific logic here
    // For example: notify user, log the event, trigger network reconfiguration, etc.
}

/**
 * @brief Sets up IP conflict monitoring
 * @param inm_handle Initialized INM handle
 * @return INM_ERROR_NONE on success, error code on failure
 */
int setup_ip_conflict_monitoring(inm_h inm_handle)
{
    int ret = INM_ERROR_NONE;
    bool is_enabled = false;
    
    printf("=== Setting up IP Conflict Monitoring ===\n");
    
    // Step 1: Check if IP conflict detection is currently enabled
    ret = inm_ip_conflict_detect_is_enabled(inm_handle, &is_enabled);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to check IP conflict detection status: %d\n", ret);
        return ret;
    }
    
    printf("IP conflict detection is currently: %s\n", 
           is_enabled ? "ENABLED" : "DISABLED");
    
    // Step 2: Set up the IP conflict callback
    ret = inm_set_ip_conflict_cb(inm_handle, ip_conflict_callback, NULL);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to set IP conflict callback: %d\n", ret);
        return ret;
    }
    
    printf("IP conflict callback registered successfully\n");
    
    // Step 3: Check current IP conflict state
    inm_ip_conflict_state_e current_state;
    ret = inm_get_ip_conflict_state(inm_handle, &current_state);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to get current IP conflict state: %d\n", ret);
        return ret;
    }
    
    switch (current_state) {
    case INM_IP_CONFLICT_STATE_CONFLICT_DETECTED:
        printf("Current status: IP conflict detected!\n");
        break;
    case INM_IP_CONFLICT_STATE_CONFLICT_NOT_DETECTED:
        printf("Current status: No IP conflicts detected\n");
        break;
    case INM_IP_CONFLICT_STATE_UNKNOWN:
    default:
        printf("Current status: Unknown\n");
        break;
    }
    
    printf("IP conflict monitoring is now active\n");
    printf("The callback will be triggered whenever IP conflicts are detected or resolved\n");
    
    return INM_ERROR_NONE;
}

/**
 * @brief Stops IP conflict monitoring
 * @param inm_handle Initialized INM handle
 * @return INM_ERROR_NONE on success, error code on failure
 */
int stop_ip_conflict_monitoring(inm_h inm_handle)
{
    int ret = INM_ERROR_NONE;
    
    printf("=== Stopping IP Conflict Monitoring ===\n");
    
    // Unset the IP conflict callback
    ret = inm_unset_ip_conflict_cb(inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to unset IP conflict callback: %d\n", ret);
        return ret;
    }
    
    printf("IP conflict monitoring stopped successfully\n");
    return INM_ERROR_NONE;
}
```

#### Usage Example

```cpp
int main()
{
    inm_h inm_handle = NULL;
    int ret = INM_ERROR_NONE;
    
    // Initialize INM
    ret = inm_initialize(&inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to initialize INM: %d\n", ret);
        return -1;
    }
    
    // Set up IP conflict monitoring
    ret = setup_ip_conflict_monitoring(inm_handle);
    if (ret != INM_ERROR_NONE) {
        printf("Failed to set up IP conflict monitoring: %d\n", ret);
        goto cleanup;
    }
    
    // Your application logic here
    // The IP conflict callback will be triggered automatically
    printf("Monitoring for IP conflicts...\n");
    printf("Press Ctrl+C to stop monitoring\n");
    
    // Simulate monitoring (in a real app, this would be your main event loop)
    sleep(30); // Monitor for 30 seconds
    
cleanup:
    // Stop IP conflict monitoring
    stop_ip_conflict_monitoring(inm_handle);
    
    // Cleanup
    inm_deinitialize(inm_handle);
    return 0;
}
```

## Related information
- Dependencies
  - Since Tizen 5.0
- API References
  - [INM API](../../api/common/latest/group__CAPI__NETWORK__INM__MODULE.html)
