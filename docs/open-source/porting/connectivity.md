# Connectivity

## Bluetooth

Bluetooth is the short range communication used to communicate between 2 devices. In Tizen, open source Bluetooth components like BlueZ and ObexD are used. Bluez and Obexd run as the daemon and there is an interface library Bluetooth Framework, used for applications to access BlueZ or ObexD over the D-Bus interface.

This section explains the Bluetooth architecture on the Tizen platform and how Tizen can be ported, along with the configuration parameters and its values.

Bluetooth Low Energy function was implemented in BlueZ and `bluetooth-frwk`.

The following figure explains the Bluetooth architecture on Tizen.

[![Bluetooth.png](https://wiki.tizen.org/images/thumb/a/a9/Bluetooth.png/600px-Bluetooth.png)](./media/800px-Bluetooth.png)

The Bluetooth framework provides dialogue for the user. It controls the BlueZ, ObexD, and PulseAudio daemons. Bluetooth provides a standard interface between the Bluetooth chip and AP, called the HCI (Host Controller Interface). HCI can be implemented on USB, UART, SDIO, but for the mobile environment, UART is used most. Depending on the chip vendor, HCI Interface Activation can be different. The vendor provides the HCI configuration and the initial scripts. For example, Broadcom and Spreadtrum provide firmware and a loading tool. Tizen supports Bluetooth version 4.2. The supported profiles are GATT, FTP, OPP, MAP, PBAP, A2DP, AVRCP, HSP/HFP, RFCOMM, HID, HDP, and PAN. Bluetooth framework Tizen Bluetooth is based on the open source BlueZ project. BlueZ provides the DBUS API and based on it, Tizen BT framework provides the C Language API. It is recommended to use the Tizen Bluetooth framework.

The following components are necessary for Bluetooth:

- Application
  - The user dialogue that controls the BlueZ, ObexD, and PulseAudio daemons
- ObexD
  - The open source component
  - Object exchange daemon
  - Supports OPP, FTP, PBAP, SYNC, and MAP profile stack
- BluetoothD
  - BluetoothD is the open souce component, Bluez 5.37 is supported
  - Bluetooth central daemon
  - Supports GAP, SDP, A2DP, AVRCP, HFP, HSP, and GATT profile stack
- Bluetooth Subsystem
  - Provides the BT unix socket. Each protocol can be accessed by its socket.
  - Supports the L2CAP, RFCOMM, SCO, and HCI protocols
- Bluetooth Driver
  - BT Chip Driver
  - In case of UART, [Linux](https://wiki.tizen.org/Linux) kernel provides the interface.
  - GPIO configuration, `rfkill` (Radio Frequency Management) and power management can be handled by both the vendor and the porting engineer.
- BT Firmware Loading Module
  - Depending on the environment, it loads the Bluetooth firmware to the Bluetooth chip.
  - Tizen and the chipset vendor need to implement this together.
  - Package: `bluetooth-tools`

### Porting OAL Interface

The following OAL scripts are run during the Bluetooth stack start and end sequences. These scripts invoke the Bluetooth chip specific (such as Broadcom and Spreadtrum) scripts, provided by the chipset vendor to perform chip specific configuration. These scripts are available in the `bluetooth-dev-tools.under` package. When this package is installed, it copies the scripts in the `/usr/etc/Bluetooth/` directory.

- `bt-stack-up.sh`




- `bt-stack-down.sh`




- `bt-reset-env.sh`




- Tizen BT Obex profiles

In Tizen, for the `obex` based profiles, the open source ObexD is used.

- BT Obex profiles server (`obexd`)




- BT Obex profiles client (`obex-client`)



### Configuration

There are a few configuration changes that need to be made to enable the specific chipset and the scripts and other configuration information, such as UART speed and UART terminal (`tty`), to be opened specific to the chipset. These changes must be provided by the chipset vendors.

- Configuration for the BCM4358 Bluetooth chipset by Broadcomm


- `hciattach`




- The Bluetooth UART used is `/dev/ttySAC3`
- The Broadcom firmware used is `BCM4358A1_001.002.005.0032.0066.hcd`
- The UART speed configuration is 3000000 for BCM4358A1
- The `bcmtool` used is `bcmtool_4358a1`
- The `.bd_addr` contains the unique Bluetooth address, which is generated during the first Bluetooth activation
- Register the Bluetooth device:

```
bcmtool_4358a1 /dev/ttySAC0 –FILE=BCM4358A1_001.002.005.0032.0066.hcd –BAUD=3000000 –ADDR=/csa/bluetooth/.bd_addr –SETSCO=0,0,0,0,0,0,0,3,3,0 –LP
```

- Attach a serial device using UART HCI to the Bluetooth stack for a broadcom device:

```
hciattach /dev/ttySAC3 –S 3000000 bcm2035 3000000 flow
```

- Run the Bluetooth daemon version 5.37:

```
bluetoothd
```

- Bring the device up, set up the device name, and enable the SSP mode:

```
hciconfig hci0 up
hciconfig hci0 name “Tizen-Mobile”
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

- Configuration for the sc2331 Bluetooth chipset by Spreadtrum


- `hciattach`




- Registering the Bluetooth device:




- Install the following files in the target's `/usr/lib/firmware` directory:

```
sc2331_fdl.bin
sc2331_fw.bin
scx35_pikeavivaltove_3M_MARLIN_connectivity_calibration.ini
scx35_pikeavivaltove_3M_MARLIN_connectivity_configure.ini
```

- The Bluetooth UART used is `/dev/ttyS0`.
- The UART speed configuration is 3000000 for sc2331.
- Attach a serial device using UART HCI to the Bluetooth stack:

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
hciconfig hci0 name “Tizen-Mobile”
hciconfig hci0 sspmode 1

```

### References

Open source component version: BlueZ 5.37

For more information, see [http://www.bluez.org/](http://www.bluez.org/).

- Reference kernel configuration for Bluetooth

The following kernel `.config` are enabled for Broadcom Bluetooth support:

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
CONFIG_RXTRA_FIRMWARE_BCM4330=”BCM4330.hcd”
```

The following kernel `.config` are enabled for Bluetooth AVRCP support:

```
CONFIG_INPUT_MISC=y
CONFIG_INPUT_UINPUT=y

```

The following kernel `.config` are enabled for Bluetooth HID support:

```
CONFIG_INPUT_GP2A=y
CONFIG_INPUT_KR3DH=y
```

The following kernel `.config` are enabled for Bluetooth Audio (SCO-over-PCM) support:

```
CONFIG_BT_SCO=y
CONFIG_INPUT_GP2A=y
CONFIG_INPUT_KR3DH=y
```

The following kernel `.config` are enabled for Bluetooth Audio (SCO-over-PCM) support:

```
CONFIG_BT_SCO=y
```

## WLAN

This section provides a step-by-step explanation of what's involved in adding a new Wi-Fi driver and making Wi-Fi work. [![Wlan.png](https://wiki.tizen.org/images/thumb/1/16/Wlan.png/800px-Wlan.png)](./media/785px-Wlan.png)

Feature Overview:

- WLAN (802.11 b/g/n)
- WPS PBC
- EAP (PEAP, TTLS)

Tizen uses `wpa_supplicant` as the platform interface to the Wi-Fi device. Your Wi-Fi driver must be compatible with the standard `wpa_supplicant`.

The Tizen WLAN architecture is centered on the Linux wireless (IEEE-802.11) subsystem. The Linux wireless SW stack defines the WLAN hardware adaptation software interfaces that need to be used in Tizen. In practice, the required interfaces are defined by cfg80211 for FullMAC WLAN devices and by mac80211 for SoftMAC WLAN devices. In addition, a Linux network interface needs to be supported towards the Linux TCP/IP stack.

The Connection Manager (ConnMan) is a daemon for managing internet connections within embedded devices running the Linux operating system.

The `wpa_supplicant` is a WPA Supplicant with support for WPA and WPA2 (IEEE 802.11i / RSN). Supplicant is the IEEE 802.1X/WPA component that is used in the client stations. It implements key negotiation with a WPA Authenticator and it controls the roaming and IEEE 802.11 authentication/association of the WLAN driver.

### Porting OAL Interface

The WLAN driver plugin is specific to a Wi-Fi chipset. This includes firmware and tools specific to Wi-Fi chipsets. Wi-Fi chipset firmware and tools files must be copied to the WLAN driver plugin directory, built, and installed before testing the Wi-Fi functionality. Because of Tizen platform requirement, the Wi-Fi driver must create the `/opt/etc/.mac.info` file, which has the MAC address of device.

The WLAN driver plugin contains the `wlan.sh` file (located in `/usr/bin/wlan.sh`), which is used to load or unload the Wi-Fi driver firmware.

When the `wifi_activate()` function is called, the load driver request is sent to the NET-CONFIG daemon. The NET-CONFIG daemon loads the Wi-Fi driver using the `wlan.sh` script file. Similarly, the `wifi_deactivate()` function requests unloading of the Wi-Fi driver. In case of Wi-Fi Direct, the `wifi_direct_activate()` and `wifi_direct_deactivate()` functions make the Wi-Fi Direct manager load or unload the Wi-Fi driver using the `wlan.sh` script.

Using the `/usr/bin/wlan.sh` script:

- `wlan.sh start`: Power up the Wi-Fi driver in station mode by loading the driver and running the firmware file.
- `wlan.sh p2p`: Power up the Wi-Fi driver in Wi-Fi Direct mode by loading the driver and running the firmware file.
- `wlan.sh softap`: Power up the Wi-Fi driver in Soft AP mode by loading the driver and running the firmware file.
- `wlan.sh stop`: Power down the Wi-Fi driver.

All other Wi-Fi related functionality is handled by the ConnMan daemon

### References

- Connection Manager (ConnMan) project website: [https://01.org/connman](https://01.org/connman)
- Linux wireless (IEEE-802.11) subsystem: [http://linuxwireless.org/](http://linuxwireless.org/)
- Information on Linux WPA/WPA2/IEEE 802.1X Supplicant: [http://hostap.epitest.fi/wpa_supplicant/](http://hostap.epitest.fi/wpa_supplicant/)
- Latest ConnMan release: [http://git.kernel.org/?p=network/connman/connman.git;a=summary](http://git.kernel.org/?p=network/connman/connman.git;a=summary)
- WLAN driver plugin git path: `/adaptation/devices/wlandrv-plugin-tizen-bcm43xx`


- Reference kernel configurations


- These options need to be enabled if the driver supports the cfg802.11 configuration API, instead of the wireless extension API. For more information, see [http://linuxwireless.org](http://linuxwireless.org/).

```
CONFIG_CFG80211
CONFIG_LIB80211
CONFIG_MAC80211 (Enable this flag, if the driver supports the softMAC feature)

```

- The following configuration options must be enabled in the kernel if the driver supports wireless extension APIs.

```
CONFIG_WIRELESS_EXT=y
CONFIG_WEXT_CORE=y
CONFIG_WEXT_PROC=y
CONFIG_WEXT_PRIV=y
CONFIG_WEXT_SPY=y
CONFIG_WIRELESS_EXT_SYSFS=y
```

## NFC

The NFC application enables the user to read and/or import the content written on an NFC tag, edit the content written on an NFC tag, write and save data in an NFC tag, and load and save the NFC data from or in a file.

[![Nfc.png](https://wiki.tizen.org/images/thumb/4/43/Nfc.png/600px-Nfc.png)](./media/Nfc.png)

The NFC client acts as an interface between the NFC app and the NFC manager, while writing or editing tag information in any physical tag. The NFC manager is the main interface, which actually deals with NFC physical tags, creates a connection with tags, and detects it. It is a daemon process to control the NFC chipset (such as NXP pn544). It provides the read and write service and basic P2P communication service, as well as the basic API for the client application. The NFC stack contains the required plugin, based on the NFC chipset. Currently, the `nfc-plugin-nxp` is used for the NXP chipset. The NFC plugin acts as an interface between the NFC chipset with the NFC framework (`nfc-manager`). It must be implemented according to the interface provided by the `nfc-manager`.

### Porting OAL Interface

The NFC plugin is implemented as a shared library and it interfaces the Tizen `nfc-manager` and the vendor NFC chip. The NFC manager loads the `libnfc-plugin.so` library at runtime from the `/usr/lib/libnfc-plugin.so` directory. Any vendor-specific plugin is installed within the same path. The plugin must be written with predefined OAL API interfaces.

During initialization, the `nfc-manager` loads the `nfc-plugin.so` library, searches for the `onload()` function, and calls the function with an interface structure instance as an argument for mapping of all the OAL interfaces. These OAL/OEM interfaces are implemented according to the underlying NFC chipset. Once the mapping is done, the NFC manager interact with `nfc-plugin`, which implements the vendor specific OAL interfaces.

The following example shows the `onload()` function for reference:

```
Bool
onload(net_nfc_oem_interface_s *oem_interfaces)
{
    oem_interfaces->init = xxx;  /* xxx refers to plugin APIs */
    oem_interfaces->deinit = xxx;
    oem_interfaces->register_listener = xxx;
    oem_interfaces->unregister_listener = xxx;
    oem_interfaces->check_firmware_version = xxx;

    return true;
}

```

The NFC OAL interfaces are defined in the following structure. Use the `net_nfc_oem_controller.h` header file.

```
typedef struct _net_nfc_oem_interface_s
{
    net_nfc_oem_controller_init init;
    net_nfc_oem_controller_deinit deinit;
    net_nfc_oem_controller_register_listener register_listener;
    net_nfc_oem_controller_unregister_listener unregister_listener;
    net_nfc_oem_controller_check_firmware_version check_firmware_version;
    net_nfc_oem_controller_update_firmware update_firmeware;
    net_nfc_oem_controller_get_stack_information get_stack_information;
    net_nfc_oem_controller_configure_discovery configure_discovery;
    net_nfc_oem_controller_get_secure_element_list get_secure_element_list;
    net_nfc_oem_controller_set_secure_element_mode set_secure_element_mode;
    net_nfc_oem_controller_connect connect;
    net_nfc_oem_controller_connect disconnect;
    net_nfc_oem_controller_check_ndef check_ndef;
    net_nfc_oem_controller_check_target_presence check_presence;
    net_nfc_oem_controller_read_ndef read_ndef;
    net_nfc_oem_controller_write_ndef write_ndef;
    net_nfc_oem_controller_make_read_only_ndef make_read_only_ndef;
    net_nfc_oem_controller_transceive transceive;
    net_nfc_oem_controller_format_ndef format_ndef;
    net_nfc_oem_controller_exception_handler exception_handler;
    net_nfc_oem_controller_is_ready is_ready;
    net_nfc_oem_controller_llcp_config config_llcp;
    net_nfc_oem_controller_llcp_check_llcp check_llcp_status;
    net_nfc_oem_controller_llcp_activate_llcp activate_llcp;
    net_nfc_oem_controller_llcp_create_socket create_llcp_socket;
    net_nfc_oem_controller_llcp_bind bind_llcp_socket;
    net_nfc_oem_controller_llcp_listen listen_llcp_socket;
    net_nfc_oem_controller_llcp_accept accept_llcp_socket;
    net_nfc_oem_controller_llcp_connect_by_url connect_llcp_by_url;
    net_nfc_oem_controller_llcp_connect connect_llcp;
    net_nfc_oem_controller_llcp_disconnect disconnect_llcp;
    net_nfc_oem_controller_llcp_socket_close close_llcp_socket;
    net_nfc_oem_controller_llcp_recv recv_llcp;
    net_nfc_oem_controller_llcp_send send_llcp;
    net_nfc_oem_controller_llcp_recv_from recv_from_llcp;
    net_nfc_oem_controller_llcp_send_to send_to_llcp;
    net_nfc_oem_controller_llcp_reject reject_llcp;
    net_nfc_oem_controller_llcp_get_remote_config get_remote_config;
    net_nfc_oem_controller_llcp_get_remote_socket_info get_remote_socket_info;
    net_nfc_oem_controller_sim_test sim_test;
    net_nfc_oem_controller_test_mode_on test_mode_on;
    net_nfc_oem_controller_test_mode_off test_mode_off;
net_nfc_oem_controller_support_nfc support_nfc;
} net_nfc_oem_interface_s;

```

The `nfc_oem_interface_s` is exported in the `nfc-plugin`. Using this interface structure, the `nfc-manager` communicates with the OAL interfaces at runtime. The NFC plugin loads when the `nfc-manager` is started and the plugin `init()` function is called to initialize the NFC chip.

```
int (*init) (net_nfc_oem_controller_init*);
```

The `deinit()` function the `nfc-manager` issues to deinitialize the NFC chip:

```
int (*deinit) (net_nfc_oem_controller_deinit *);
```

- Sending the notification to the upper layer (NFC Service)

Refer to the `phdal4nfc_message_glib.c` file. The `g_idle_add_full` is used for handling the message in the NFC Service. You can use the callback client asynchronously in the client context. Post a message in queue, and the message is processed by a client thread.

- Reference implementation of the NFC plugin

Sample code snippets cannot be reproduced. Code is proriatory. For reference, see the `nfc-plugin-emul` and `nfc-plugin-nxp` files.

#### NFC OAL API

| Function                                 | Description                              | Parameter                                |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `net_nfc_oem_controller_init init;`      | Initializes the NFC chip.                | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_deinit deinit;`  | Deinitializes the NFC chip.              | None                                     |
| `net_nfc_oem_controller_register_listener register_listener;` | Registers a callback function for a tag event, SE event, and llcp event. | `target_detection_listener_cb target_detection_listener`: The tag event callback function`se_transaction_listener_cb se_transaction_listener`: The SE event callback function`llcp_event_listener_cb llcp_event_listener`: The llcp event callback function`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_unregister_listener unregister_listener;` | Releases a callback function for a tag event, SE event, and llcp event. | None                                     |
| `net_nfc_oem_controller_check_firmware_version check_firmware_version;` | Checks the firmware version of the NFC chip. | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_update_firmware update_firmware;` | Updates the NFC chip firmware.           | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_get_stack_information get_stack_information;` | Gets the list of supported tags and the current firmware version. | `net_nfc_stack_information_s`: Pointer value to get the information of support tags and the current firmware version`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_configure_discovery configure_discovery;` | Delivers the config information on discovery. | `net_nfc_discovery_mode_e`: The start/stop mode`net_nfc_event_filter_e config`: The information for tag filtering`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_get_secure_element_list get_secure_element_list;` | Gets the information of the current secure element. | `net_nfc_secure_element_info_s`: The pointer value to get secure element information`int`: The pointer value to get the count of the secure element`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_set_secure_element_mode set_secure_element_mode;` | Sets the secure element to use.          | `net_nfc_secure_element_type_e`: Secure element information`net_nfc_secure_element_mode_e`: The mode information to set`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_connect connect;` | Connects to the detected tag/target.     | `net_nfc_target_handle_s`: The tag/target handle for connecting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_connect disconnect;` | Disconnects the connected tag/target.    | `net_nfc_target_handle_s`: The tag/target handle for disconnecting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_check_ndef check_ndef;` | Checks the tag to for ndef support.      | `net_nfc_target_handle_s`: The tag handle to check ndef`int`: The max size supported in the tag`int`: The real data size saved in the tag`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_check_target_presence check_presence;` | Checks if a tag exist in the RF range.   | `net_nfc_target_handle_s`: The tag handle to check presence`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_read_ndef read_ndef;` | Reads ndef data in a tag.                | `net_nfc_target_handle_s`: The tag handle to read`data_s`: The pointer value to save the ndef data`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_write_ndef write_ndef;` | Writes the data to the tag.              | `net_nfc_target_handle_s`: The handle to write`data_s`: The data to write`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_make_read_only_ndef make_read_only_ndef;` | Makes the tag to a read only tag.        | `net_nfc_target_handle_s`: The target tag handle`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_transceive transceive;` | Sends and receives the low command to the tag or target. | `net_nfc_target_handle_s`: The tag or target handle to transceive`net_nfc_transceive_info_s`: The pointer value included command or data to send and data to receive`data_s`: The pointer value to send the information of context`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_format_ndef format_ndef;` | Formats the tag.                         | `net_nfc_target_handle_s`: The tag handle to format`data_s`: The key value to send the tag for formatting`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_exception_handler exception_handler;` | When the `nfc-manager` faces an unwanted exception, it tries to deinitialize and initialize the stack before unregistering and registering the callback function. | None                                     |
| `net_nfc_oem_controller_is_ready is_ready;` | Checks the status of the NFC stack.      | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_config config_llcp;` | Sets the llcp configuration (miu, lto, wks, option). | `net_nfc_target_handle_s`: The target handle to set llcp`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_check_llcp check_llcp_status;` | Checks the llcp configuration (miu, lto, wks, option). | `net_nfc_target_handle_s`: The target handle to check llcp`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_activate_llcp activate_llcp;` | Activates the llcp functionality.        | `net_nfc_target_handle_s`: The target handle to activate`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_create_socket create_llcp_socket;` | Creates the llcp socket                  | `net_nfc_llcp_socket_t`: The pointer value to receive the socket information`net_nfc_socket_type_e socketType`: The type of socket to create`uint16_t miu`: The miu value`uint8_t rw`: The rw value`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_bind bind_llcp_socket;` | Binds the socket.                        | `net_nfc_llcp_socket_t socket`: The information about the socket to bind`uint8_t service_access_point`: The information of access point to bind`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_listen listen_llcp_socket;` | Sets the socket to listen.               | `net_nfc_target_handle_s`: The target handle`uint8_t`: The service name to listen`net_nfc_llcp_socket_t socket`: Socket information`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_accept accept_llcp_socket;` | Accepts the connect request in listening status. | `net_nfc_llcp_socket_t socket`: Socket information to accept`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_connect_by_url connect_llcp_by_url;` | Connects the server with the service name. | `net_nfc_target_handle_s`: The handle of the target to connect`net_nfc_llcp_socket_t socket`: Socket information`uint8_t`: Service name to connect`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_connect connect_llcp;` | Connects to the server with access point (port number). | `net_nfc_target_handle_s`: The target handle`net_nfc_llcp_socket_t socket`: Socket information`uint8_t service_access_point`: Access point number`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_disconnect disconnect_llcp;` | Disconnects the llcp link.               | `net_nfc_target_handle_s`: Socket information to disconnect`net_nfc_llcp_socket_t socket`: The information of the socket to disconnect`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_socket_close close_llcp_socket;` | Closes the llcp socket.                  | `net_nfc_llcp_socket_t socket`: Socket information to close`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_recv recv_llcp;` | Receives the data using the llcp link.   | `net_nfc_target_handle_s`: The target handle to receive`net_nfc_llcp_socket_t socket`: Socket information to receive`data_s`: The pointer value to receive the data`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_send send_llcp;` | Sends the data using llcp link.          | `net_nfc_target_handle_s`: The target handle to send`net_nfc_llcp_socket_t socket`: Socket information to send`data_s`: The data to send`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_recv_from recv_from_llcp;` | Rejects the connect request from the client socket. | `net_nfc_target_handle_s`: The target handle to reject`net_nfc_llcp_socket_t socket`: The socket information to reject`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_send_to send_to_llcp;` | Sends the data using the service access point. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_socket_t socket`: The socket information`data_s`: The data to send`uint8_t service_access_point`: The service access point to send`net_nfc_error_e`: Returns an error code on failure.`void`: The value to control the context (can be set to `NULL`) |
| `net_nfc_oem_controller_llcp_reject reject_llcp;` | Rejects the connect request from the client socket. | `net_nfc_target_handle_s`: The target handle to reject`net_nfc_llcp_socket_t socket`: The socket information to reject`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_get_remote_config get_remote_config;` | Gets te llcp socket config information of the peer device. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_config_info_s`: The pointer value to get config information of peer device's llcp socket`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_llcp_get_remote_socket_info get_remote_socket_info;` | Gets the llcp socket information of the peer device. | `net_nfc_target_handle_s`: The peer target handle`net_nfc_llcp_socket_t socket`: The llcp socket information`net_nfc_llcp_socket_option_s`: The pointer value to save the information of remote socket`net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_sim_test sim_test;` | Tests the SWP link with SIM and NFC chipset. | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_test_mode_on test_mode_on;` | Changes the NFC chip to test mode. (Test mode exists only in the NXP case. If there are none, it does not need to implemented.) | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_test_mode_off test_mode_off;` | Changes the status of the NFC chip from test mode to normal mode. (Test mode exists only in the NXP case. If there are none, it does not need to implemented.) | `net_nfc_error_e`: Returns an error code on failure. |
| `net_nfc_oem_controller_support_nfc support_nfc` | Checks each the device file of each chip. |                                          |

### Configuration

The `nfc-plugin` package must be saved to the `/usr/lib/libnfc-plugin.so` directory when installed. When the `nfc-manager` starts, it looks for the plugin library and loads it dynamically from this path.

### References

Enable the following configuration options in the kernel `.config`.

```
Using Pn544: CONFIG_PN544_NFC
Using Pn65n: CONFIG_PN65N_NFC

```

API references available are under the [Tizen_3.0_Porting_Guide#Appendix_2](https://wiki.tizen.org/Tizen_3.0_Porting_Guide#Appendix_2).

For more information, see [http://nfc-forum.org/](http://nfc-forum.org/).

## MTP

- MTP exchanges can only occur between 2 products at a time, and in each communication, 1 product acts as the initiator and the other as the responder.
- The initiator is the product that initiates actions with the responder by sending operations to the responder.

[![Mtp-initiator.png](https://wiki.tizen.org/images/thumb/2/2f/Mtp-initiator.png/600px-Mtp-initiator.png)](./media/800px-Mtp-initiator.png)

- The responder can not initiate any actions, and can only send responses to operations sent by the initiator or send events.

[![Mtp-responder.png](https://wiki.tizen.org/images/thumb/6/6d/Mtp-responder.png/600px-Mtp-responder.png)](./media/800px-Mtp-responder.png)

- In the Tizen system, the USB host is the initiator, and the USB device is the responder.

### Porting OAL Interface

- Tizen MTP initiator and responder do not have an OAL Interface.
- There are extension possibilities of the MTP Transport layer.

### Configuration

- MTP Initiator


- The MTP Initiator consist of 3 packages.

```
mtp-initiator daemon
mtp-initiator api
libmtp opensource
```

- The MTP initiator does not operate independently. It requires the help of another module, such as USB.
- When the USB device is connected to the host, the module must run the MTP initiator daemon.


- MTP Responder


- The MTP responder consist of 1 package.

```
mtp-responder daemon
```

- The MTP responder does not operate independently. It requires the help of another module, such as USB.
- When the USB device is connected to the host, the module must run the MTP responder daemon.

### References

- Media Transfer Protocol v.1.1 Spec: [http://www.usb.org/developers/docs/devclass_docs/](http://www.usb.org/developers/docs/devclass_docs/)
