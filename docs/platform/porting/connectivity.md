# Connectivity

You can implement various connectivity features, such as Bluetooth, WLAN, and NFC.

## Bluetooth

Bluetooth is a short range communication protocol used to communicate between 2 devices. Tizen uses open source Bluetooth components, such as BlueZ and ObexD. Bluez and ObexD run as a daemon and an interface library, Bluetooth Framework, is used for applications to access them over the D-Bus interface.

This section explains the Bluetooth architecture on the Tizen platform and how Tizen can be ported, along with the configuration parameters and their values.

**Figure: Tizen Bluetooth architecture**

![Tizen Bluetooth architecture](media/800px-bluetooth.png)

The Bluetooth framework provides a dialogue for the user to control the BlueZ, ObexD, and PulseAudio daemons. Bluetooth provides a standard interface between the Bluetooth chip and AP, called the HCI (Host Controller Interface). HCI can be implemented on USB, UART, and SDIO, but for the mobile environment, UART is the most common. HCI activation can differ depending on the chip vendor. The vendor provides the HCI configuration and the initial scripts. For example, Broadcom and Spreadtrum provide firmware and a loading tool. Tizen supports Bluetooth version 4.2, and the GATT, FTP, OPP, MAP, PBAP, A2DP, AVRCP, HSP/HFP, RFCOMM, HID, HDP, and PAN profiles. Bluetooth Low Energy functions have been implemented in BlueZ and `bluetooth-frwk`.

The Tizen Bluetooth framework is based on the open source BlueZ project. BlueZ provides the DBUS API and based on it, Tizen Bluetooth framework provides the C Language API. Using the Tizen Bluetooth framework is recommended.

The following components are necessary for Bluetooth:

- Application
  - User dialogue that controls the BlueZ, ObexD, and PulseAudio daemons
- ObexD
  - Open source component
  - Object exchange daemon
  - Supports OPP, FTP, PBAP, SYNC, and MAP profile stack
- BluetoothD
  - BluetoothD is the open source component, BlueZ 5.37 is supported
  - Bluetooth central daemon
  - Supports GAP, SDP, A2DP, AVRCP, HFP, HSP, and GATT profile stack
- Bluetooth subsystem
  - Provides the BT unix socket. Each protocol can be accessed by its socket.
  - Supports the L2CAP, RFCOMM, SCO, and HCI protocols
- Bluetooth driver
  - BT Chip driver
  - For UART, the interface is provided by the [Linux](https://wiki.tizen.org/Linux) kernel.
  - GPIO configuration, `rfkill` (radio frequency management), and power management can be handled by both the vendor and the porting engineer
- Bluetooth firmware loading module
  - Depending on the environment, it loads the Bluetooth firmware to the Bluetooth chip
  - Tizen and the chipset vendor need to implement this together
  - Package: `bluetooth-tools`

### Porting the OAL interface

The following OAL scripts are run during the Bluetooth stack start and end sequences. These scripts invoke the Bluetooth chip-specific (such as Broadcom and Spreadtrum) scripts, provided by the chipset vendor, to perform chip-specific configuration. These scripts are available in the `bluetooth-dev-tools.under` package. When this package is installed, it copies the following scripts in the `/usr/etc/Bluetooth/` directory:

- `bt-stack-up.sh`
- `bt-stack-down.sh`
- `bt-reset-env.sh`

#### Tizen BT Obex profiles

In Tizen, the open source ObexD is used for the `obex`-based profiles:

- BT Obex profiles server (`obexd`)
- BT Obex profiles client (`obex-client`)


### Configuration

There are a few configuration changes that need to be made to enable the specific chipset and the scripts and other chipset-specific configuration information, such as UART speed and UART terminal (`tty`). These changes must be provided by the chipset vendor.

- Configuration for the Broadcomm BCM4358 Bluetooth chipset:
  - `hciattach`  
    The `bluez/tools/hciattach.c` file is patched to enable the `hciattach` tool specific to the BCM4358 chipset. This service attaches the BT UART HCI interface to the Bluetooth stack at a baud rate of 3000000. It is also responsible for loading the Bluetooth firmware on BCM4358.
  - Bluetooth UART used is `/dev/ttySAC3`
  - Broadcom firmware used is `BCM4358A1_001.002.005.0032.0066.hcd`
  - UART speed configuration for BCM4358A1 is 3000000
  - `bcmtool` used is `bcmtool_4358a1`
  - `.bd_addr` contains the unique Bluetooth address, which is generated during the first Bluetooth activation
  - Register the Bluetooth device:
    ```
    bcmtool_4358a1 /dev/ttySAC0 -FILE=BCM4358A1_001.002.005.0032.0066.hcd -BAUD=3000000 -ADDR=/csa/bluetooth/.bd_addr -SETSCO=0,0,0,0,0,0,0,3,3,0 -LP
    ```
  - Attach a serial device to the Bluetooth stack using the UART HCI for a Broadcomm device:
    ```
    hciattach /dev/ttySAC3 -S 3000000 bcm2035 3000000 flow
    ```
  - Run the Bluetooth daemon version 5.37:
    ```
    bluetoothd
    ```
  - Bring the device up, set up the device name, and enable the SSP mode:
    ```
    hciconfig hci0 up
    hciconfig hci0 name "Tizen-Mobile"
    hciconfig hci0 sspmode 1
    ```
  - Switch on the Bluetooth radio:
    ```
    rfkill unblock bluetooth
    ```
  - Switch off the Bluetooth radio:
    ```
    rfkill block bluetooth
    ```
- Configuration for the Spreadtrum sc2331 Bluetooth chipset
  - `hciattach`  
    The `bluez/tools/hciattach.c` file is patched to enable the `hciattach` tool specific to the sc2331 chipset. This service attaches the BT UART HCI interface to the Bluetooth stack at a baud rate of 3000000. It is also responsible for loading the Bluetooth firmware on sc2331.
  - Register the Bluetooth device:  
    The `cp2-download` tool is provided for downloading the Spreadtrum firmware. This tool also downloads the Wi-Fi firmware at boot time.
  - Install the following files in the target's `/usr/lib/firmware` directory:
    ```
    sc2331_fdl.bin
    sc2331_fw.bin
    scx35_pikeavivaltove_3M_MARLIN_connectivity_calibration.ini
    scx35_pikeavivaltove_3M_MARLIN_connectivity_configure.ini
    ```
  - Bluetooth UART used is `/dev/ttyS0`
  - UART speed configuration for sc233 is 3000000
  - Attach a serial device to the Bluetooth stack using the UART HCI:
    ```
    hciattach -s 3000000 /dev/ttyS0 sprd 3000000 flow
    ```
  - Run the bluetooth daemon version 5.37:
    ```
    bluetoothd
    ```
  - Bring the device up, set up the device name, and enable the SSP mode:
    ```
    hciconfig hci0 up
    hciconfig hci0 name "Tizen-Mobile"
    hciconfig hci0 sspmode 1
    ```

### References

Open source component version: BlueZ 5.37

For more information, see [http://www.bluez.org/](http://www.bluez.org/).

The reference kernel configuration for Bluetooth:

- The following kernel `.config` lines are enabled for Broadcom Bluetooth support:
  ```
  CONFIG_BT=y
  CONFIG_BT_L2CAP=y
  CONFIG_BT_RFCOMM=y
  CONFIG_BT_RFCOMM_TTY=y
  CONFIG_BT_BNEP=y
  CONFIG_BT_HIDP=y
  CONFIG_BT_HCIUART=y
  CONFIG_BT_HCIUART_H4=y
  CONFIG_BCM4330=y
  CONFIG_RFKILL=y
  CONFIG_RFKILL_INPUT=y
  CONFIG_RXTRA_FIRMWARE_BCM4330="BCM4330.hcd"
  ```
- The following kernel `.config` lines are enabled for Bluetooth AVRCP support:
  ```
  CONFIG_INPUT_MISC=y
  CONFIG_INPUT_UINPUT=y
  ```
- The following kernel `.config` lines are enabled for Bluetooth HID support:
  ```
  CONFIG_INPUT_GP2A=y
  CONFIG_INPUT_KR3DH=y
  ```
- The following kernel `.config` lines are enabled for Bluetooth Audio (SCO-over-PCM) support:
  ```
  CONFIG_BT_SCO=y
  CONFIG_INPUT_GP2A=y
  CONFIG_INPUT_KR3DH=y
  ```


## WLAN

This section provides a step-by-step explanation of what is involved in adding a new Wi-Fi driver and making Wi-Fi work.

**Figure: Tizen Wi-FI architecture**

![Tizen Wi-FI architecture](media/wlan.png)

Feature overview:

- WLAN (802.11 b/g/n)
- WPS PBC
- EAP (PEAP, TTLS)

Tizen uses `wpa_supplicant` as the platform interface to Wi-Fi devices. Your Wi-Fi driver must be compatible with the standard `wpa_supplicant`.

The Tizen WLAN architecture is centered on the Linux wireless (IEEE-802.11) subsystem. The Linux wireless SW stack defines the WLAN hardware adaptation software interfaces that need to be used in Tizen. In practice, the required interfaces are defined by cfg80211 for FullMAC WLAN devices and by mac80211 for SoftMAC WLAN devices. In addition, a Linux network interface needs to be supported towards the Linux TCP/IP stack.

The Connection Manager (ConnMan) is a daemon for managing Internet connections within embedded devices running the Linux operating system.

The `wpa_supplicant` interface is a WPA Supplicant with support for WPA and WPA2 (IEEE 802.11i / RSN). WPA Supplicant is the IEEE 802.1X/WPA component that is used in the client stations. It implements key negotiation with a WPA Authenticator, and it controls roaming and the IEEE 802.11 authentication/association of the WLAN driver.

### Porting the OAL interface

The WLAN driver plugin is specific to a Wi-Fi chipset. This includes firmware and chipset-specific tools. Wi-Fi chipset firmware and tool files must be copied to the WLAN driver plugin directory, built, and installed before testing the Wi-Fi functionality. Because of Tizen platform requirements, the Wi-Fi driver must create the `/opt/etc/.mac.info` file, which has the device MAC address.

When the `wifi_manager_activate()` function is called, the request is sent to the NET-CONFIG daemon to call `hal_wifi_sta_start()` in HAL_API Wi-Fi. Similarly, the `wifi_manager_deactivate()` function calls `hal_wifi_stop()` through NET_CONFIG daemon. In case of Wi-Fi Direct&reg;, the `wifi_direct_activate()` and `wifi_direct_deactivate()` functions make the Wi-Fi Direct manager load or unload the Wi-Fi driver using the `wpa_supplicant`.

All other Wi-Fi related functionality is handled by the ConnMan daemon.

### References

- Linux wireless (IEEE-802.11) subsystem: [https://wireless.wiki.kernel.org](https://wireless.wiki.kernel.org)
- Information on Linux WPA/WPA2/IEEE 802.1X Supplicant: [http://hostap.epitest.fi/wpa_supplicant/](http://hostap.epitest.fi/wpa_supplicant/)
- Latest ConnMan release: [http://git.kernel.org/?p=network/connman/connman.git;a=summary](http://git.kernel.org/?p=network/connman/connman.git;a=summary)
- WLAN driver plugin Git path: `/adaptation/devices/wlandrv-plugin-tizen-bcm43xx`
- Reference kernel configurations
- The following options must be enabled if the driver supports the cfg802.11 configuration API, instead of the wireless extension API. For more information, see [https://wireless.wiki.kernel.org](http://wireless.wiki.kernel.org/):
  ```
  CONFIG_CFG80211
  CONFIG_LIB80211
  CONFIG_MAC80211 (Enable this flag, if the driver supports the softMAC feature)
  ```
- The following configuration options must be enabled in the kernel if the driver supports wireless extension APIs:
  ```
  CONFIG_WIRELESS_EXT=y
  CONFIG_WEXT_CORE=y
  CONFIG_WEXT_PROC=y
  CONFIG_WEXT_PRIV=y
  CONFIG_WEXT_SPY=y
  CONFIG_WIRELESS_EXT_SYSFS=y
  ```

## NFC

The NFC application enables the user to:
- Read and import the content written on an NFC tag.
- Edit the content written on an NFC tag.
- Write and save data on an NFC tag.
- Load and save the NFC data from or in a file.

**Figure: NFC architecture**

![NFC architecture](media/nfc.png)

The NFC implementation has the following main components:

- **Tizen NFC Framework** contains the NFC manager API layer, the NFC common library and the NFC manager daemon. The `nfc-manager` is the main interface, which actually deals with NFC physical tags, creates a connection with tags, and detects it. It is a daemon process to control the NFC chipset (such as NXP pn544). It provides the read and write service and basic P2P communication service, as well as the basic API for the client application.
- **NFC HAL** contains the NFC HAL API, and the OAL layer. The NFC HAL acts as an interface between the NFC chipset with the NFC framework (`nfc-manager`). It must be implemented according to the interface provided by the `nfc-manager`.

### Porting the OAL interface

The NFC HAL is implemented as a shared library and it interfaces the Tizen NFC Framework and the vendor NFC chip. The NFC manager loads the `libnfc-common.so` library at runtime. Any vendor-specific function is installed within the same path. The library must be written with predefined OAL API interfaces.

During initialization, the `nfc-manager` loads the `/hal/api/nfc` library, searches for the `net_nfc_controller_onload()` function, and calls the `hal_nfc_get_backend()` function which creates an interface structure instance for mapping all the OAL interfaces. These OAL/OEM interfaces are implemented according to the underlying NFC chipset. Once the mapping is done, the NFC manager interacts with `/hal/api/nfc`, which implements the vendor-specific OAL interfaces.

The following example shows the `hal_nfc_get_backend()` function:

```cpp
int hal_nfc_get_backend(void)
{
  g_nfc_funcs = calloc(1, sizeof(hal_backend_nfc_funcs));
}
```

The NFC OAL interfaces are defined in the following structure. Use the `net_nfc_oem_controller.h` header file:

```cpp
typedef struct _hal_backend_nfc_funcs {
	int (*start)(void);
	int (*stop)(void);
	int (*register_listener)(net_nfc_target_detection_listener_cb target_detection_listener,
        net_nfc_se_transaction_listener_cb se_transaction_listener,
        net_nfc_llcp_event_listener_cb llcp_event_listener,
        net_nfc_hce_apdu_listener_cb hce_apdu_listener);
	int (*unregister_listener)(void);
	int (*get_firmware_version)(net_nfc_data_s ** data);
	int (*support_nfc)(void);
	int (*check_firmware_version)(void);
	int (*update_firmware)(void);
	int (*get_stack_information)(net_nfc_stack_information_s * stack_info);
	int (*configure_discovery)(net_nfc_discovery_mode_e mode, net_nfc_event_filter_e config);
	int (*check_target_presence)(net_nfc_target_handle_s * handle);
	int (*connect)(net_nfc_target_handle_s * handle);
	int (*disconnect)(net_nfc_target_handle_s * handle);
	int (*check_ndef)(net_nfc_target_handle_s * handle, uint8_t * ndef_card_state, int *max_data_size, int *real_data_size);
	int (*read_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s ** data);
	int (*write_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s * data);
	int (*make_read_only_ndef)(net_nfc_target_handle_s * handle);
	int (*format_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s * secure_key);
	int (*transceive)(net_nfc_target_handle_s * handle, net_nfc_transceive_info_s * info, net_nfc_data_s ** data);
	int (*exception_handler)(void);
	int (*is_ready)(void);
	int (*llcp_config)(net_nfc_llcp_config_info_s * config);
	int (*llcp_check_llcp)(net_nfc_target_handle_s * handle);
	int (*llcp_activate_llcp)(net_nfc_target_handle_s * handle);
	int (*llcp_create_socket)(net_nfc_llcp_socket_t * socket, net_nfc_socket_type_e type, uint16_t miu, uint8_t rw, void *user_param);
	int (*llcp_bind)(net_nfc_llcp_socket_t socket, uint8_t service_access_point);
	int (*llcp_listen)(net_nfc_target_handle_s * handle, uint8_t * service_access_name, net_nfc_llcp_socket_t socket, void *user_param);
	int (*llcp_accept)(net_nfc_llcp_socket_t socket, void *user_param);
	int (*llcp_connect_by_url)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, uint8_t * service_access_name, void *user_param);
	int (*llcp_connect)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, uint8_t service_access_point, void *user_param);
	int (*llcp_disconnect)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, void *user_param);
	int (*llcp_socket_close)(net_nfc_llcp_socket_t socket);
	int (*llcp_recv)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);
	int (*llcp_send)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);
	int (*llcp_recv_from)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);
	int (*llcp_send_to)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, uint8_t service_access_point, void *user_param);
	int (*llcp_reject)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket);
	int (*llcp_get_remote_config)(net_nfc_target_handle_s * handle, net_nfc_llcp_config_info_s * config);
	int (*llcp_get_remote_socket_info)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_llcp_socket_option_s * option);
	int (*secure_element_open)(net_nfc_secure_element_type_e element_type, net_nfc_target_handle_s ** handle);
	int (*secure_element_get_atr)(net_nfc_target_handle_s * handle, net_nfc_data_s ** atr);
	int (*secure_element_send_apdu)(net_nfc_target_handle_s * handle, net_nfc_data_s * command, net_nfc_data_s ** response);
	int (*secure_element_close)(net_nfc_target_handle_s * handle);
	int (*get_secure_element_list)(net_nfc_secure_element_info_s * list, int *count);
	int (*set_secure_element_mode)(net_nfc_secure_element_type_e element_type, net_nfc_secure_element_mode_e mode);
	int (*test_mode_on)(void);
	int (*test_mode_off)(void);
	int (*hce_response_apdu)(net_nfc_target_handle_s * handle, net_nfc_data_s * response);
	int (*secure_element_route_aid)(net_nfc_data_s * aid, net_nfc_se_type_e se_type, int power);
	int (*secure_element_unroute_aid)(net_nfc_data_s * aid);
	int (*secure_element_commit_routing)(void);
	int (*secure_element_set_default_route)(net_nfc_se_type_e switch_on, net_nfc_se_type_e switch_off, net_nfc_se_type_e battery_off);
	int (*secure_element_clear_aid_table)(void);
	int (*secure_element_get_aid_table_size)(int *table_size);
	int (*secure_element_set_route_entry)(net_nfc_se_entry_type_e type, net_nfc_se_tech_protocol_type_e value, net_nfc_se_type_e route, int power);
	int (*secure_element_clear_routing_entry)(net_nfc_se_entry_type_e type);
	int (*secure_element_set_listen_tech_mask)(net_nfc_se_tech_protocol_type_e screen_state);
	int (*set_screen_state)(net_nfc_screen_state_type_e screen_state);
} hal_backend_nfc_funcs;
```

The `_hal_backend_nfc_funcs` struct is exported in the `/hal/api/nfc`. Using this interface structure, the `nfc-manager` communicates with the OAL interfaces at runtime. The NFC HAL loads when the `nfc-manager` is started and the `hal_nfc_start()` function is called to initialize the NFC module:

```cpp
int hal_nfc_start(void) (start());
```

The `nfc-manager` issues the `hal_nfc_stop` function to deinitialize the NFC chip:

```cpp
int hal_nfc_start(void) (stop());
```

Pay attention to the following:

- Sending the notification to the upper layer (NFC service)  
See the `phdal4nfc_message_glib.c` file. The `g_idle_add_full` is used for handling the message in the NFC service. You can use the callback client asynchronously in the client context. Post a message in queue, and the message is processed by a client thread.
- Reference implementation of the NFC plugin  
Sample code snippets cannot be reproduced. Code is proprietary. For reference, see the `nfc-plugin-emul` files.

#### NFC HAL API

The following table lists all the NFC HAL API functions.

**Table: NFC HAL API functions**

| Function | Description | Parameter |
| --- | --- | --- |
| `int (*start)(void);` | Starts the NFC module. | - |
| `int (*stop)(void);` | Stops the NFC module. | - |
| `int (*register_listener)(net_nfc_target_detection_listener_cb target_detection_listener, net_nfc_se_transaction_listener_cb se_transaction_listener, net_nfc_llcp_event_listener_cb llcp_event_listener, net_nfc_hce_apdu_listener_cb hce_apdu_listener);` | Registers listeners for specific events. | `net_nfc_target_detection_listener_cb target_detection_listener`: Callback for target detection events<br>`net_nfc_se_transaction_listener_cb se_transaction_listener`: Callback for SE transaction events<br>`net_nfc_llcp_event_listener_cb llcp_event_listener`: Callback for LLCP events<br>`net_nfc_hce_apdu_listener_cb hce_apdu_listener`: Callback for HCE APDU events |
| `int (*unregister_listener)(void);` | Unregisters the registered listener. | - |
| `int (*get_firmware_version)(net_nfc_data_s ** data);` | Gets the firmware version of the NFC module. | `net_nfc_data_s ** data`: Pointer to store the firmware version data |
| `int (*support_nfc)(void);` | Checks whether the NFC module is supported. | - |
| `int (*check_firmware_version)(void);` | Checks the firmware version of the NFC module. | - |
| `int (*update_firmware)(void);` | Updates the firmware of the NFC module. | - |
| `int (*get_stack_information)(net_nfc_stack_information_s * stack_info);` | Gets the stack information of the NFC module. | `net_nfc_stack_information_s * stack_info`: Pointer to store the stack information |
| `int (*configure_discovery)(net_nfc_discovery_mode_e mode, net_nfc_event_filter_e config);` | Configures the discovery mode and settings. | `net_nfc_discovery_mode_e mode`: Discovery mode (start/stop)<br>`net_nfc_event_filter_e config`: Information for tag filtering |
| `int (*check_target_presence)(net_nfc_target_handle_s * handle);` | Checks whether a target is present. | `net_nfc_target_handle_s * handle`: Target handle to check presence |
| `int (*connect)(net_nfc_target_handle_s * handle);` | Connects to a target. | `net_nfc_target_handle_s * handle`: Target handle for connecting |
| `int (*disconnect)(net_nfc_target_handle_s * handle);` | Disconnects from a target. | `net_nfc_target_handle_s * handle`: Target handle for disconnecting |
| `int (*check_ndef)(net_nfc_target_handle_s * handle, uint8_t * ndef_card_state, int *max_data_size, int *real_data_size);` | Checks whether an NDEF message is supported. | `net_nfc_target_handle_s * handle`: Tag handle to check NDEF<br>`uint8_t * ndef_card_state`: Pointer to store NDEF card state<br>`int *max_data_size`: Pointer to store max NDEF size<br>`int *real_data_size`: Pointer to store current NDEF data size |
| `int (*read_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s ** data);` | Reads an NDEF message. | `net_nfc_target_handle_s * handle`: Tag handle to read<br>`net_nfc_data_s ** data`: Pointer to store the NDEF data |
| `int (*write_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s * data);` | Writes an NDEF message. | `net_nfc_target_handle_s * handle`: Handle to write<br>`net_nfc_data_s * data`: Data to write |
| `int (*make_read_only_ndef)(net_nfc_target_handle_s * handle);` | Makes an NDEF message read-only. | `net_nfc_target_handle_s * handle`: Target tag handle |
| `int (*format_ndef)(net_nfc_target_handle_s * handle, net_nfc_data_s * secure_key);` | Formats an NDEF message. | `net_nfc_target_handle_s * handle`: Tag handle to format<br>`net_nfc_data_s * secure_key`: Key value to send the tag for formatting |
| `int (*transceive)(net_nfc_target_handle_s * handle, net_nfc_transceive_info_s * info, net_nfc_data_s ** data);` | Transceives data with a target. | `net_nfc_target_handle_s * handle`: Tag or target handle to transceive<br>`net_nfc_transceive_info_s * info`: Pointer including command or data to send and data to receive<br>`net_nfc_data_s ** data`: Pointer to store the received data |
| `int (*exception_handler)(void);` | Handles exceptions. | - |
| `int (*is_ready)(void);` | Checks whether the NFC module is ready. | - |
| `int (*llcp_config)(net_nfc_llcp_config_info_s * config);` | Configures LLCP settings. | `net_nfc_llcp_config_info_s * config`: LLCP configuration (miu, lto, wks, option) |
| `int (*llcp_check_llcp)(net_nfc_target_handle_s * handle);` | Checks whether LLCP is supported. | `net_nfc_target_handle_s * handle`: Target handle to check LLCP |
| `int (*llcp_activate_llcp)(net_nfc_target_handle_s * handle);` | Activates LLCP. | `net_nfc_target_handle_s * handle`: Target handle to activate |
| `int (*llcp_create_socket)(net_nfc_llcp_socket_t * socket, net_nfc_socket_type_e type, uint16_t miu, uint8_t rw, void *user_param);` | Creates a socket. | `net_nfc_llcp_socket_t * socket`: Pointer to receive the socket information<br>`net_nfc_socket_type_e type`: Type of socket to create<br>`uint16_t miu`: MIU value<br>`uint8_t rw`: RW value<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_bind)(net_nfc_llcp_socket_t socket, uint8_t service_access_point);` | Binds a socket. | `net_nfc_llcp_socket_t socket`: Information about the socket to bind<br>`uint8_t service_access_point`: Information of access point to bind |
| `int (*llcp_listen)(net_nfc_target_handle_s * handle, uint8_t * service_access_name, net_nfc_llcp_socket_t socket, void *user_param);` | Listens on a socket. | `net_nfc_target_handle_s * handle`: Target handle<br>`uint8_t * service_access_name`: Service name to listen<br>`net_nfc_llcp_socket_t socket`: Socket information<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_accept)(net_nfc_llcp_socket_t socket, void *user_param);` | Accepts a connection request. | `net_nfc_llcp_socket_t socket`: Socket information to accept<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_connect_by_url)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, uint8_t * service_access_name, void *user_param);` | Connects using a URL. | `net_nfc_target_handle_s * handle`: Handle of the target to connect<br>`net_nfc_llcp_socket_t socket`: Socket information<br>`uint8_t * service_access_name`: Service name to connect<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_connect)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, uint8_t service_access_point, void *user_param);` | Connects using a service access point. | `net_nfc_target_handle_s * handle`: Target handle<br>`net_nfc_llcp_socket_t socket`: Socket information<br>`uint8_t service_access_point`: Access point number<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_disconnect)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, void *user_param);` | Disconnects from a socket. | `net_nfc_target_handle_s * handle`: Socket information to disconnect<br>`net_nfc_llcp_socket_t socket`: Information of the socket to disconnect<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_socket_close)(net_nfc_llcp_socket_t socket);` | Closes a socket. | `net_nfc_llcp_socket_t socket`: Socket information to close |
| `int (*llcp_recv)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);` | Receives data on a socket. | `net_nfc_target_handle_s * handle`: Target handle to receive<br>`net_nfc_llcp_socket_t socket`: Socket information to receive<br>`net_nfc_data_s * data`: Pointer to receive the data<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_send)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);` | Sends data on a socket. | `net_nfc_target_handle_s * handle`: Target handle to send<br>`net_nfc_llcp_socket_t socket`: Socket information to send<br>`net_nfc_data_s * data`: Data to send<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_recv_from)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, void *user_param);` | Receives data from a specific service access point. | `net_nfc_target_handle_s * handle`: Target handle to receive<br>`net_nfc_llcp_socket_t socket`: Socket information to receive<br>`net_nfc_data_s * data`: Pointer to receive the data<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_send_to)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_data_s * data, uint8_t service_access_point, void *user_param);` | Sends data to a specific service access point. | `net_nfc_target_handle_s * handle`: Peer target handle<br>`net_nfc_llcp_socket_t socket`: Socket information<br>`net_nfc_data_s * data`: Data to send<br>`uint8_t service_access_point`: Service access point to send<br>`void *user_param`: User parameter (can be `NULL`) |
| `int (*llcp_reject)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket);` | Rejects a connection request. | `net_nfc_target_handle_s * handle`: Target handle to reject<br>`net_nfc_llcp_socket_t socket`: Socket information to reject |
| `int (*llcp_get_remote_config)(net_nfc_target_handle_s * handle, net_nfc_llcp_config_info_s * config);` | Gets the remote LLCP configuration. | `net_nfc_target_handle_s * handle`: Peer target handle<br>`net_nfc_llcp_config_info_s * config`: Pointer to get config information of peer device's LLCP socket |
| `int (*llcp_get_remote_socket_info)(net_nfc_target_handle_s * handle, net_nfc_llcp_socket_t socket, net_nfc_llcp_socket_option_s * option);` | Gets the remote socket information. | `net_nfc_target_handle_s * handle`: Peer target handle<br>`net_nfc_llcp_socket_t socket`: LLCP socket information<br>`net_nfc_llcp_socket_option_s * option`: Pointer to save the information of remote socket |
| `int (*secure_element_open)(net_nfc_secure_element_type_e element_type, net_nfc_target_handle_s ** handle);` | Opens a secure element. | `net_nfc_secure_element_type_e element_type`: Type of secure element to open<br>`net_nfc_target_handle_s ** handle`: Pointer to store the handle of the opened SE |
| `int (*secure_element_get_atr)(net_nfc_target_handle_s * handle, net_nfc_data_s ** atr);` | Gets the ATR information of a secure element. | `net_nfc_target_handle_s * handle`: Handle of the SE<br>`net_nfc_data_s ** atr`: Pointer to store the ATR data |
| `int (*secure_element_send_apdu)(net_nfc_target_handle_s * handle, net_nfc_data_s * command, net_nfc_data_s ** response);` | Sends an APDU command to a secure element. | `net_nfc_target_handle_s * handle`: Handle of the SE<br>`net_nfc_data_s * command`: APDU command to send<br>`net_nfc_data_s ** response`: Pointer to store the APDU response |
| `int (*secure_element_close)(net_nfc_target_handle_s * handle);` | Closes a secure element. | `net_nfc_target_handle_s * handle`: Handle of the SE to close |
| `int (*get_secure_element_list)(net_nfc_secure_element_info_s * list, int *count);` | Gets the list of secure elements. | `net_nfc_secure_element_info_s * list`: Pointer to store secure element information<br>`int * count`: Pointer to store the count of secure elements |
| `int (*set_secure_element_mode)(net_nfc_secure_element_type_e element_type, net_nfc_secure_element_mode_e mode);` | Sets the mode of a secure element. | `net_nfc_secure_element_type_e element_type`: Secure element type<br>`net_nfc_secure_element_mode_e mode`: Mode information to set |
| `int (*test_mode_on)(void);` | Enables test mode. | - |
| `int (*test_mode_off)(void);` | Disables test mode. | - |
| `int (*hce_response_apdu)(net_nfc_target_handle_s * handle, net_nfc_data_s * response);` | Sends a response APDU in HCE mode. | `net_nfc_target_handle_s * handle`: Target handle<br>`net_nfc_data_s * response`: APDU response to send |
| `int (*secure_element_route_aid)(net_nfc_data_s * aid, net_nfc_se_type_e se_type, int power);` | Routes an AID to a secure element. | `net_nfc_data_s * aid`: AID to route<br>`net_nfc_se_type_e se_type`: Destination SE type<br>`int power`: Power state for the route |
| `int (*secure_element_unroute_aid)(net_nfc_data_s * aid);` | Unroutes an AID from a secure element. | `net_nfc_data_s * aid`: AID to unroute |
| `int (*secure_element_commit_routing)(void);` | Commits the routing table. | - |
| `int (*secure_element_set_default_route)(net_nfc_se_type_e switch_on, net_nfc_se_type_e switch_off, net_nfc_se_type_e battery_off);` | Sets the default route for different states. | `net_nfc_se_type_e switch_on`: Default SE when screen on<br>`net_nfc_se_type_e switch_off`: Default SE when screen off<br>`net_nfc_se_type_e battery_off`: Default SE when battery off |
| `int (*secure_element_clear_aid_table)(void);` | Clears the AID table. | - |
| `int (*secure_element_get_aid_table_size)(int *table_size);` | Gets the size of the AID table. | `int *table_size`: Pointer to store the AID table size |
| `int (*secure_element_set_route_entry)(net_nfc_se_entry_type_e type, net_nfc_se_tech_protocol_type_e value, net_nfc_se_type_e route, int power);` | Sets a routing entry. | `net_nfc_se_entry_type_e type`: Entry type (tech, protocol, AID)<br>`net_nfc_se_tech_protocol_type_e value`: Technology/Protocol value<br>`net_nfc_se_type_e route`: Destination SE for the route<br>`int power`: Power state for the route |
| `int (*secure_element_clear_routing_entry)(net_nfc_se_entry_type_e type);` | Clears a routing entry. | `net_nfc_se_entry_type_e type`: Entry type to clear |
| `int (*secure_element_set_listen_tech_mask)(net_nfc_se_tech_protocol_type_e screen_state);` | Sets the technology mask for listening. | `net_nfc_se_tech_protocol_type_e screen_state`: Screen state to configure tech mask for |
| `int (*set_screen_state)(net_nfc_screen_state_type_e screen_state);` | Sets the screen state. | `net_nfc_screen_state_type_e screen_state`: Screen state to set |

### References

Enable the following configuration options in the kernel `.config` file:

```
Using Pn544: CONFIG_PN544_NFC
Using Pn65n: CONFIG_PN65N_NFC
```

For more information, see [http://nfc-forum.org/](http://nfc-forum.org/).

## MTP
The Media Transfer Protocol (MTP) is used for exchanging media files between 2 devices:

- MTP exchanges can only occur between 2 devices at a time.
- In each communication, 1 devices acts as the initiator and the other as the responder.
- The initiator is the device that initiates actions with the responder by sending operations to the responder.

  **Figure: MTP Initiator**

  ![MTP Initiator](media/800px-mtp-initiator.png)
- The responder cannot initiate any actions, and can only send responses to operations sent by the initiator or send events.

  **Figure: MTP Responder**

  ![MTP Responder](media/800px-mtp-responder.png)
- In the Tizen system, the USB host is the initiator, and the USB device is the responder.

### Porting the OAL interface

The Tizen MTP initiator and responder do not have an OAL Interface. There are extension possibilities for the MTP Transport layer.

### Configuration

The following configuration is needed:

- MTP initiator
  - The MTP Initiator consists of 3 packages:
    ```
    mtp-initiator daemon
    mtp-initiator api
    libmtp opensource
    ```
  - The MTP initiator does not operate independently. It requires the help of another module, such as USB.
  - When the USB device is connected to the host, the module must run the MTP initiator daemon.
- MTP responder
  - The MTP responder consists of 1 package:
    ```
    mtp-responder daemon
    ```
  - The MTP responder does not operate independently. It requires the help of another module, such as USB.
  - When the USB device is connected to the host, the module must run the MTP responder daemon.

### References

- Media Transfer Protocol v.1.1 Spec: [http://www.usb.org/developers/docs/devclass_docs/](http://www.usb.org/developers/docs/devclass_docs/)
