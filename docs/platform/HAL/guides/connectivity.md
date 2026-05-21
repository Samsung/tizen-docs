# Connectivity

You can implement various connectivity features, such as Bluetooth, WLAN, and NFC.

## Bluetooth

Bluetooth is a short range communication protocol used to communicate between 2 devices. Tizen uses open source Bluetooth components, such as BlueZ and ObexD. Bluez and ObexD run as a daemon and an interface library, Bluetooth Framework, is used for applications to access them over the D-Bus interface.

This section explains the Bluetooth architecture on the Tizen platform and how Tizen can be ported, along with the configuration parameters and their values.

**Figure: Tizen Bluetooth architecture**

![Tizen Bluetooth architecture](media/bluetooth.png)

The Bluetooth framework provides a dialogue for the user to control the BlueZ and ObexD daemons. Bluetooth provides a standard interface between the Bluetooth chip and AP, called the HCI (Host Controller Interface). HCI can be implemented on USB, UART, and SDIO, but for the mobile environment, UART is the most common. HCI activation can differ depending on the chip vendor. The vendor provides the HCI configuration and the initial scripts. For example, Broadcom and Spreadtrum provide firmware and a loading tool. Tizen supports Bluetooth version 5.0, and the GATT, FTP, OPP, MAP, PBAP, A2DP, AVRCP, HSP/HFP, RFCOMM, HID, HDP, and PAN profiles.

The Tizen Bluetooth framework is based on the open source BlueZ project. BlueZ provides the DBUS API and based on it, Tizen Bluetooth framework provides the C Language API. Using the Tizen Bluetooth framework is recommended.

The following components are necessary for Bluetooth:

- Application
  - User dialogue that controls the BlueZ and ObexD daemons
- ObexD
  - Open source component
  - Object exchange daemon
  - Supports OPP, FTP, PBAP, SYNC, and MAP profile stack
- BluetoothD
  - BluetoothD is the open source component, BlueZ 5.79 is supported
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
  - Package: `bluetooth-firmware-bcm`

### Porting the HAL Backend interface

The Bluetooth HAL Backend is responsible for the low-level control and initialization of specific Bluetooth chipsets. It acts as a bridge between the standard Tizen Bluetooth HAL API and the hardware, abstracting the vendor-specific procedures required to bring a Bluetooth adapter in and out of service. The following scripts are run during the Bluetooth stack start and end sequences. These scripts invoke the Bluetooth chip-specific (such as Broadcom and Spreadtrum) scripts, provided by the chipset vendor, to perform chip-specific configuration. These scripts are available in the `bluetooth-firmware-bcm` package. When this package is installed, it copies the following scripts in the `/hal/etc/bluetooth/` directory:

- `bt-stack-up.sh`
- `bt-stack-down.sh`
- `bt-reset-env.sh`

This HAL Backend is not used directly by application developers or the upper-level framework. Instead, it is invoked by the Tizen Bluetooth HAL API implementation to perform hardware-specific tasks.

The process is as follows:
- An application or system service uses the Tizen Bluetooth Framework.
- The Tizen Bluetooth Framework calls the standard C API functions provided by the Tizen Bluetooth HAL API.
- When the HAL API needs to perform a hardware-level operation, such as powering the adapter on or off, it delegates the task to the vendor-specific Bluetooth HAL Backend.
- The HAL Backend executes the necessary vendor-specific commands, scripts, and tools to manage the hardware and then returns the status to the HAL API.

### References

Open source component : BlueZ

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

When the Wi-Fi activation function is called, the request is sent to the NET-CONFIG daemon to call the Wi-Fi start function in HAL_API Wi-Fi. Similarly, the Wi-Fi deactivation function calls the Wi-Fi stop function through NET_CONFIG daemon. In case of Wi-Fi Direct&reg;, the Wi-Fi Direct activation and deactivation functions make the Wi-Fi Direct manager load or unload the Wi-Fi driver using the `wpa_supplicant`.

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

During initialization, the `nfc-manager` loads the `/hal/api/nfc` library, searches for the NFC controller onload function, and calls the NFC backend function which creates an interface structure instance for mapping all the OAL interfaces. These OAL/OEM interfaces are implemented according to the underlying NFC chipset. Once the mapping is done, the NFC manager interacts with `/hal/api/nfc`, which implements the vendor-specific OAL interfaces.

The `_hal_backend_nfc_funcs` struct is exported in the `/hal/api/nfc`. Using this interface structure, the `nfc-manager` communicates with the OAL interfaces at runtime. The NFC HAL loads when the `nfc-manager` is started and the NFC start function is called to initialize the NFC module.

Pay attention to the following:

- Sending the notification to the upper layer (NFC service)  
See the `phdal4nfc_message_glib.c` file. The `g_idle_add_full` is used for handling the message in the NFC service. You can use the callback client asynchronously in the client context. Post a message in queue, and the message is processed by a client thread.
- Reference implementation of the NFC plugin  
Sample code snippets cannot be reproduced. Code is proprietary. For reference, see the `nfc-plugin-emul` files.

### References

Enable the following configuration options in the kernel `.config` file:

```
Using Pn544: CONFIG_PN544_NFC
Using Pn65n: CONFIG_PN65N_NFC
```

For more information, see [http://nfc-forum.org/](http://nfc-forum.org/).