
# Security and API Privileges

To effectively protect the device system and user private data, the
Tizen security architecture is based on privileges and application
signing of the Linux basic security model, which includes process
isolation and mandatory access control. Since Tizen, as an open mobile
platform, provides a wide range of features and experiences for users
with a variety of applications, the users must be able to grant
privileges for security-sensitive operations.

Tizen provides API-level access control for security-sensitive
operations which, if not used correctly, can harm user privacy and
system stability. Therefore, applications that use such sensitive APIs
must declare the required privileges in the
[tizen-manifest.xml](../process/setting-properties.md#setting-the-application-manifest) file.
Privileges are categorized into public, partner, and platform levels
according to their hierarchy:

-   The public level is the minimum privilege level, which means that
    any application developed using the Tizen Studio can use
    these privileges.
-   The partner level privileges require at least a partner-signed
    certificate which is granted to developers who have a business
    relationship with the vendor.
-   The platform level is the highest privilege level, and an
    application that needs these privileges requires at least a
    platform-signed certificate, which is granted to vendor developers.

Since Tizen platform 3.0, some privileges are categorized as
privacy-related and give an option to the user to switch them on and
off. If an application invokes a privacy-related privileged API, the
Tizen system checks whether the privilege is **allowed** for the
application. For the application to use the API, the privilege must be
declared in the `tizen-manifest.xml` file and the user must have
switched it on.

> **Note**  
> In applications with the platform version 3.0 or higher, if you use privacy-related privileged APIs, make sure that the user has switched the privilege on before making the function call. Otherwise, the application does not work as expected.
>
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../../guides/security/requesting-permissions.md) using the Privacy Privilege Manager API (in
[mobile](../../api/mobile/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVACY__PRIVILEGE__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SECURITY__FRAMEWORK__PRIVACY__PRIVILEGE__MANAGER__MODULE.html)
applications).

The Tizen Studio also provides privilege checker tools to check whether the Tizen application source code contains any privilege violations. For more information, see [Verifying APIs and
Privileges](../../../tizen-studio/native-tools/api-checker.md).

<a name="mobile"></a>
## Mobile Native API Privileges

The following table lists the API privileges, which you must declare
when using security-sensitive API modules in mobile native applications.

**Table: Mobile native API privileges**

| Privilege                                | Level    | Privacy      | Since | Description                              |
|----------------------------------------|-------|------------|-----|----------------------------------------|
| `http://tizen.org/privilege/account.read` | public   | Account      | 2.3   | The application can read accounts.       |
| `http://tizen.org/privilege/account.write` | public   | Account      | 2.3   | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm.get`   | public   | -            | 2.3   | The application can read information about the saved alarms. |
| `http://tizen.org/privilege/alarm.set`   | public   | -            | 2.3   | The application can set alarms and wake the device up at scheduled times. |
| `http://tizen.org/privilege/antivirus.admin` | platform | -            | 3.0   | The application can enable or disable antivirus programs and manage detected malware. |
| `http://tizen.org/privilege/antivirus.scan` | partner  | -            | 3.0   | The application can request to scan files in other applications or on the device to detect harmful content. |
| `http://tizen.org/privilege/antivirus.webprotect` | partner  | -            | 3.0   | The application can check the reputation of a Web address and determine whether accessing it can put the user's device at risk. |
| `http://tizen.org/privilege/apphistory.read` | public   | User history | 2.4   | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/appmanager.kill` | platform | -            | 2.3   | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.kill.bgapp` | public   | -            | 2.4   | The application can request to close applications running in the background. |
| `http://tizen.org/privilege/appmanager.launch` | public   | -            | 2.3   | The application can open other applications. |
| `http://tizen.org/privilege/blocknumber.read` | partner  | -            | 4.0   | The application can read rules for blocking calls and messages.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/blocknumber.write` | partner  | -            | 4.0   | The application can write rules for blocking calls and messages.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/bluetooth`   | public   | -            | 2.3   | The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetooth.admin` | platform | -            | 2.3   | The application can change Bluetooth settings, such as switching Bluetooth on or off, setting the device name, and enabling or disabling the AV remote control. |
| `http://tizen.org/privilege/bookmark.admin` | platform | Bookmark     | 2.3   | The application can retrieve, create, edit, and delete Internet bookmarks. |
| `http://tizen.org/privilege/calendar.read` | public   | Calendar     | 2.3   | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public   | Calendar     | 2.3   | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call`        | public   | Call         | 2.3   | The application can make phone calls to numbers when they are tapped without further confirmation. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/callhistory.read` | public   | User history | 2.3   | The application can read call log items. |
| `http://tizen.org/privilege/callhistory.write` | public   | User history | 2.3   | The application can create, update, and delete call log items. |
| `http://tizen.org/privilege/camera`      | public   | Camera       | 2.3   | The application can take pictures and switch the camera flash on and off while using the camera. |
| `http://tizen.org/privilege/contact.read` | public   | Contacts     | 2.3   | The application can read the user profile, contacts, and contact history. Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public   | Contacts     | 2.3   | The application can create, update, and delete the user profile, contacts, and any contact history that is related to this application. Contact history can include social network activity. |
| `http://tizen.org/privilege/content.write` | public   | -            | 2.3   | The application can change media information. This information can be used by other applications. |
| `http://tizen.org/privilege/datasharing` | public   | -            | 2.3   | The application can share data with other applications. |
| `http://tizen.org/privilege/display`     | public   | -            | 2.3   | The application can manage display settings, such as the brightness. This can increase battery consumption. |
| `http://tizen.org/privilege/download`    | public   | -            | 2.3   | The application can manage HTTP downloads. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/dpm.bluetooth` | partner  | -            | 3.0   | The application can restrict Bluetooth connections. This can prevent applications that use Bluetooth from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.browser` | partner  | -            | 3.0   | The application can prevent the use of browser applications. This can prevent applications that use browser applications from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.camera`  | partner  | -            | 3.0   | The application can restrict the use of the camera. This can prevent applications that use the camera from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.clipboard` | partner  | -            | 3.0   | The application can restrict the use of the clipboard. This can prevent applications that use the clipboard from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.debugging` | partner  | -            | 3.0   | The application can restrict the use of debugging. This can prevent applications that use debugging from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.email`   | partner  | -            | 3.0   | The application can restrict POP and IMAP email access. This can prevent applications that use email services from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.location` | partner  | -            | 3.0   | The application can restrict the use of location functions. This can prevent applications that use location functions from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.lock`    | partner  | -            | 3.0   | The application can lock the device.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.message` | partner  | -            | 3.0   | The application can restrict the use of text, multimedia, and chat messaging services. This can prevent applications that use messaging services from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.microphone` | partner  | -            | 3.0   | The application can restrict the use of the microphone. This can prevent applications that use the microphone from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.password` | partner  | -            | 3.0   | The application can manage password policies and reset the passwords used to unlock the device and recover data.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.security` | partner  | -            | 3.0   | The application can change security settings, such as those for certificate installation, data encryption, and factory data resets.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.storage` | partner  | -            | 3.0   | The application can prevent the use of external storages, such as SD cards and USB storage devices. This can prevent applications that use external storage from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.usb`     | partner  | -            | 3.0   | The application can prevent USB connections, including the use of USB tethering. This can prevent applications that use USB connections from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.wifi`    | partner  | -            | 3.0   | The application can restrict the use of Wi-Fi networks and mobile hotspots. If the device cannot connect to a Wi-Fi network, it can connect to a mobile network. This can result in additional charges depending on the user's payment plan.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.wipe`    | partner  | -            | 3.0   | The application can erase all data from the user's device and reset the user's device to its factory default settings.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.zone`    | partner  | -            | 3.0   | The application can create and remove containers. Containers are private workspaces which provide separate application runtime environments and data storage.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/email`       | public   | -            | 2.3   | The application can manage the user's email accounts, including the user's folders and emails, POP3 and IMAP downloads, and SMTP uploads. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/email.admin` | platform | -            | 2.3   | The application can manage the email application settings. |
| `http://tizen.org/privilege/fido.client` | public   | -            | 3.0   | The application can trigger authenticators on the user's device and it can request to use the user's PIN or biometrics (fingerprints or irises) for authentication. |
| `http://tizen.org/privilege/gestureactivation` | platform | -            | 4.0   | The application can allow and block special touch gestures. |
| `http://tizen.org/privilege/gesturegrab` | platform | -            | 4.0   | The application can read special touch gestures, even while it is running in the background. |
| `http://tizen.org/privilege/haptic`      | public   | -            | 2.3   | The application can control vibration feedback. |
| `http://tizen.org/privilege/healthinfo`  | public   | Sensor       | 2.3.1 | The application can read health information gathered by the device sensors, such as the pedometer and heart rate monitor. |
| `http://tizen.org/privilege/ime`         | public   | -            | 2.4   | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/imemanager`  | public   | -            | 2.4   | The application can manage installed input methods. |
| `http://tizen.org/privilege/inputgenerator` | platform | -            | 2.4   | The application can simulate keys being pressed and touch interactions with the screen. |
| `http://tizen.org/privilege/keygrab`     | platform | -            | 2.4   | The application can read actions involving special keys, such as the volume keys on this or other devices (such as TV remote controls), even when it is running in the background. |
| `http://tizen.org/privilege/keymanager`  | public   | -            | 2.3   | The application can save keys, certificates, and data to, and retrieve and delete them from, a password-protected storage. Checking the status of certificates while connected to a mobile network can result in additional charges depending on the user's payment plan.<br>**Deprecated since 3.0.** |
| `http://tizen.org/privilege/keymanager.admin` | platform | -            | 2.3   | The application can lock and unlock a password-protected storage, and manage password changes for it.<br>**Deprecated since 2.4.** |
| `http://tizen.org/privilege/led`         | public   | -            | 2.3   | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/location`    | public   | Location     | 2.3   | The application can read the user's location information. |
| `http://tizen.org/privilege/location.coarse` | public   | Location     | 3.0   | The application can determine the user's approximate location including the user device's Cell ID, LAC (Location Area Code), and TAC (Tracking Area Code). |
| `http://tizen.org/privilege/location.enable` | platform | Location     | 2.3   | The application can control the user's location service settings. |
| `http://tizen.org/privilege/mapservice`  | public   | -            | 2.4   | The application can use map services, such as geocoding, places, and routing (directions). |
| `http://tizen.org/privilege/mediacontroller.client` | public   | -            | 2.4   | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public   | -            | 2.4   | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/mediahistory.read` | public   | User history | 2.4   | The application can read the statistics concerning the music and videos played on the device, such as the peak times for playing music or videos. |
| `http://tizen.org/privilege/message.read` | public   | Message      | 2.3   | The application can read text and multimedia messages, and any information related to them. |
| `http://tizen.org/privilege/message.write` | public   | Message      | 2.3   | The application can write, send, delete, and move text and multimedia messages, and change the settings and status of the messages, such as read or unread. |
| `http://tizen.org/privilege/minicontrol.provider` | public   | -            | 2.4   | The application can show a small toolbar on the notification panel or lock screen while it is open.<br>**Deprecated since 3.0.** |
| `http://tizen.org/privilege/network.get` | public   | -            | 2.3   | The application can retrieve network information, such as the status of each network, its type, and detailed network profile information. |
| `http://tizen.org/privilege/network.profile` | public   | -            | 2.3   | The application can add, remove, and edit network profiles. |
| `http://tizen.org/privilege/network.set` | public   | -            | 2.3   | The application can switch Wi-Fi on and off, and connect to and disconnect from Wi-Fi and mobile networks. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/nfc`         | public   | -            | 2.3   | The application can read and write NFC tag information, and send NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.admin`   | platform | -            | 2.3   | The application can change NFC settings, such as switching NFC on or off. |
| `http://tizen.org/privilege/nfc.cardemulation` | public   | -            | 2.3   | The application can access smart card details, such as credit card details, and allow users to make payments using NFC. |
| `http://tizen.org/privilege/notification` | public   | -            | 2.3   | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/packagemanager.admin` | platform | -            | 2.3   | The application can install and uninstall application packages. |
| `http://tizen.org/privilege/packagemanager.clearcache` | public   | -            | 2.4   | The application can clear other applications' caches. |
| `http://tizen.org/privilege/packagemanager.info` | public   | -            | 2.3   | The application can retrieve detailed application package information. |
| `http://tizen.org/privilege/peripheralio` | platform   | -            | 4.0   | The application can communicate with peripherals using industry standard protocols and interfaces, such as GPIO, I2C, PWM, UART, and SPI. |
| `http://tizen.org/privilege/power`       | public   | -            | 2.3   | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push`        | public   | -            | 2.3   | The application can receive notifications from the Internet. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/reboot`      | platform | -            | 2.3.1 | The application can restart the device.  |
| `http://tizen.org/privilege/recorder`    | public   | Microphone   | 2.3   | The application can record video and audio. |
| `http://tizen.org/privilege/screenshot`  | platform | -            | 2.3   | The application can capture screenshots. |
| `http://tizen.org/privilege/secureelement` | public   | -            | 2.3.1 | The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/shortcut`    | public   | -            | 2.3   | The application can create and delete shortcuts. |
| `http://tizen.org/privilege/systemmonitor` | public   | -            | 2.4   | The application can read system information, including information from the CPU and RAM. |
| `http://tizen.org/privilege/systemsettings` | public   | -            | 2.3   | The application can read and write unrestricted system settings.<br>**Deprecated since 2.3.1.** |
| `http://tizen.org/privilege/systemsettings.admin` | platform | -            | 2.3   | The application can read and write all system settings. |
| `http://tizen.org/privilege/tee.client` | partner | -            | 4.0   | The application can call security related functions running inside a Trusted Execution Environment (TEE), which ensures that sensitive data is stored, processed, and protected in an isolated, trusted environment.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/telephony`   | public   | -            | 2.3   | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/telephony.admin` | platform | -            | 2.3   | The application can manage telephony settings, such as those for incoming and outgoing calls, forwarding and holding calls, networks, and SIM cards. |
| `http://tizen.org/privilege/tethering.admin` | platform | -            | 2.3   | The application can enable and disable tethering services. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/use_ir`      | public   | -            | 3.0   | The application can use the infrared transmitter. |
| `http://tizen.org/privilege/volume.set`  | public   | -            | 2.3   | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/vpnservice`  | public   | -            | 3.0   | The application can manage the VPN (virtual private network) and change its settings. |
| `http://tizen.org/privilege/web-history.admin` | platform | User history | 2.3   | The application can manage the user's Internet history. |
| `http://tizen.org/privilege/widget.viewer` | public   | -            | 2.3.1 | The application can show widgets, and information from their associated applications, on the home screen. |
| `http://tizen.org/privilege/wifidirect`  | public   | -            | 2.3   | The application can enable and disable Wi-Fi Direct&reg;, manage Wi-Fi Direct connections, and change Wi-Fi Direct settings. |
| `http://tizen.org/privilege/window.priority.set` | public   | -            | 2.3   | The application can appear on top of other windows and screens, including the lock screen, according to the order of priority of the windows. This can prevent the user from interacting with other applications or screens until the window for the application is closed. |
| `http://tizen.org/privilege/zigbee` | public   | -            | 4.0   | The application can connect a ZigBee coordinator to end devices and control connected end devices. |
| `http://tizen.org/privilege/zigbee.admin` | platform   | -            | 4.0   | The application can control a connected ZigBee coordinator, e.g. turning it on or off. |

<a name="wearable"></a>
## Wearable Native API Privileges

The following table lists the API privileges, which you must declare
when using security-sensitive API modules in wearable native
applications.

**Table: Wearable native API privileges**

| Privilege                                | Level    | Privacy      | Since | Description                              |
|----------------------------------------|--------|------------|-----|----------------------------------------|
| `http://tizen.org/privilege/account.read` | public   | Account      | 3.0   | The application can read accounts.       |
| `http://tizen.org/privilege/account.write` | public   | Account      | 3.0   | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm.get`   | public   | -            | 2.3.1 | The application can read information about the saved alarms. |
| `http://tizen.org/privilege/alarm.set`   | public   | -            | 2.3.1 | The application can set alarms and wake the device up at scheduled times. |
| `http://tizen.org/privilege/antivirus.admin` | platform | -            | 3.0   | The application can enable or disable antivirus programs and manage detected malware. |
| `http://tizen.org/privilege/antivirus.scan` | partner  | -            | 3.0   | The application can request to scan files in other applications or on the device to detect harmful content. |
| `http://tizen.org/privilege/antivirus.webprotect` | partner  | -            | 3.0   | The application can check the reputation of a Web address and determine whether accessing it can put the user's device at risk. |
| `http://tizen.org/privilege/apphistory.read` | public | User history         | 4.0 | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/appmanager.kill` | platform | -            | 2.3.1 | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.kill.bgapp` | public   | -            | 3.0   | The application can request to close applications running in the background. |
| `http://tizen.org/privilege/appmanager.launch` | public   | -            | 2.3.1 | The application can open other applications. |
| `http://tizen.org/privilege/blocknumber.read` | partner  | -            | 4.0   | The application can read rules for blocking calls and messages.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/blocknumber.write`   | partner    | -      | 4.0 | The application can write rules for blocking calls and messages.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/bluetooth`   | public   | -            | 2.3.1 | The application can perform unrestricted actions using  Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetooth.admin` | platform | -            | 2.3.1 | The application can change Bluetooth settings, such as switching Bluetooth on or off, setting the device name, and enabling or disabling the AV remote control. |
| `http://tizen.org/privilege/calendar.read` | public   | Calendar | 3.0 | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public   | Calendar | 3.0 | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call`        | public   | Call         | 2.3.1 | The application can make phone calls to numbers when they are tapped without further confirmation. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/callhistory.read` | public   | User history | 2.3.1 | The application can read call log items. |
| `http://tizen.org/privilege/callhistory.write` | public   | User history | 2.3.1 | The application can create, update, and delete call log items. |
| `http://tizen.org/privilege/camera`      | public   | Camera       | 2.3.1 | The application can take pictures and switch the camera flash on and off while using the camera. |
| `http://tizen.org/privilege/contact.read` | public   | Contacts     | 3.0   | The application can read the user profile, contacts, and contact history. Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public   | Contacts     | 3.0   | The application can create, update, and delete the user profile, contacts, and any contact history that is related to this application. Contact history can include social network activity. |
| `http://tizen.org/privilege/content.write` | public   | -            | 2.3.1 | The application can change media information. This information can be used by other applications. |
| `http://tizen.org/privilege/datasharing` | public   | -            | 2.3.1 | The application can share data with other applications. |
| `http://tizen.org/privilege/display`     | public   | -            | 2.3.1 | The application can manage display settings, such as the brightness. This can increase battery consumption. |
| `http://tizen.org/privilege/download`    | public   | -            | 2.3.1 | The application can manage HTTP downloads. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/dpm.bluetooth` | partner  | -            | 3.0   | The application can restrict Bluetooth connections. This can prevent applications that use Bluetooth from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.browser` | partner  | -            | 3.0   | The application can prevent the use of browser applications. This can prevent applications that use browser applications from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.camera`  | partner  | -            | 3.0   | The application can restrict the use of the camera. This can prevent applications that use the camera from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.clipboard` | partner  | -            | 3.0   | The application can restrict the use of the clipboard.   This can     prevent     applications   that use the   clipboard from  working       properly.<br>       **Allowed to  licensed    partners.**   |
| `http://tizen.org/privilege/dpm.debugging` | partner  | -            | 3.0   | The application can restrict    the use of   debugging.     This can       prevent      applications   that use       debugging from  working        properly. <br>    **Allowed to   licensed   partners.** |
| `http://tizen.org/privilege/dpm.email`   | partner  | -            | 3.0   | The application can restrict POP and IMAP email access. This can prevent applications that use email services from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.location` | partner  | -            | 3.0   | The application can restrict the use of location functions. This can prevent applications that use location functions from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.lock`    | partner  | -            | 3.0   | The application can lock the device.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.message` | partner  | -            | 3.0   | The application can restrict the use of text, multimedia, and chat messaging services. This can prevent applications that use messaging services from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.microphone` | partner  | -            | 3.0   | The application can restrict the use of the microphone. This can prevent applications that use the microphone from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.password` | partner  | -            | 3.0   | The application can manage password policies and reset the passwords used to unlock the device and recover data.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.security` | partner  | -            | 3.0   | The application can change security settings, such as those for certificate installation, data encryption, and factory data resets.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.storage` | partner  | -            | 3.0   | The application can prevent the use of external storages, such as SD cards and USB storage devices. This can prevent applications that use external storage from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.usb`     | partner  | -            | 3.0   | The application can prevent USB connections, including the use of USB tethering. This can prevent applications that use USB connections from working properly.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.wifi`    | partner  | -            | 3.0   | The application can restrict   the use of   Wi-Fi networks  and mobile     hotspots. If   the device     cannot connect to a Wi-Fi     network, it   can connect to  a mobile       network. This  can result in   additional      charges      depending on   the user's      payment plan.  <br> **Allowed to    licensed    partners.**   |
| `http://tizen.org/privilege/dpm.wipe`    | partner  | -            | 3.0   | The application can erase all data from the user's device and reset the user's device to its factory default settings.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/dpm.zone`    | partner  | -            | 3.0   | The application can create and remove containers. Containers are private workspaces which provide separate application runtime environments and data storage.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/email`       | public   | -            | 3.0   | The application can manage the user's email accounts, including the user's folders and emails, POP3 and IMAP downloads, and SMTP uploads. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/fido.client` | public   | -            | 3.0   | The application can trigger authenticators on the user's device and it can request to use the user's PIN or biometrics (fingerprints or irises) for authentication. |
| `http://tizen.org/privilege/gestureactivation`      | platform   | -            | 4.0 | The application can allow and block special touch gestures. |
| `http://tizen.org/privilege/gesturegrab`      | platform   | -            | 4.0 | The application can read special touch gestures, even while it is running in the background. |
| `http://tizen.org/privilege/haptic`      | public   | -            | 2.3.1 | The application can control vibration feedback. |
| `http://tizen.org/privilege/healthinfo`  | public   | Sensor       | 2.3.1 | The application can read health information gathered by the device sensors, such as the pedometer and heart rate monitor. |
| `http://tizen.org/privilege/ime`         | public   | -            | 3.0   | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/imemanager`  | public   | -            | 3.0   | The application can manage installed input methods. |
| `http://tizen.org/privilege/inputgenerator` | platform | -            | 3.0   | The application can simulate keys being pressed and touch interactions with the screen. |
| `http://tizen.org/privilege/keygrab`     | platform | -            | 3.0   | The application can read actions involving special keys, such as the volume keys on this or other devices (such as TV remote controls), even when it is running in the background. |
| `http://tizen.org/privilege/keymanager`  | public   | -            | 2.3.1 | The application can save keys, certificates, and data to, and retrieve and delete them from, a password-protected storage. |
| `http://tizen.org/privilege/keymanager.admin` | platform | -            | 2.3.1 | The application can lock and unlock a password-protected storage, and manage password changes for it.<br>**Deprecated since 3.0.** |
| `http://tizen.org/privilege/led`         | public   | -            | 2.3.1 | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/location`    | public   | Location     | 2.3.1 | The application can read the user's location information. |
| `http://tizen.org/privilege/location.coarse` | public   | Location     | 3.0   | The application can determine the user's approximate location including the user device's Cell ID, LAC (Location Area Code), and TAC (Tracking Area Code). |
| `http://tizen.org/privilege/location.enable` | platform | Location     | 2.3.1 | The application can control the user's location service settings. |
| `http://tizen.org/privilege/mapservice`  | public   | -            | 2.3.2 | The application can use map services, such as geocoding, places, and routing (directions). |
| `http://tizen.org/privilege/mediacontroller.client` | public   | -            | 3.0   | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public   | -            | 3.0   | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/message.read` | public   | Message      | 2.3.1 | The application can read text and multimedia messages, and any information related to them. |
| `http://tizen.org/privilege/message.write` | public   | Message      | 2.3.1 | The application can write, send, delete, and move text and multimedia messages, download multimedia messages, and change the settings and status of the messages, such as read or unread. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/network.get` | public   | -            | 2.3.1 | The application can retrieve network information, such as the status of each network, its type, and detailed network profile information. |
| `http://tizen.org/privilege/network.profile` | public   | -            | 2.3.1 | The application can add, remove, and edit network profiles. |
| `http://tizen.org/privilege/network.set` | public   | -            | 2.3.1 | The application can switch Wi-Fi on and off, and connect to and disconnect from Wi-Fi and mobile networks. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/nfc`         | public   | -            | 2.3.1 | The application can read and write NFC tag information, and send NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.admin`   | platform | -            | 2.3.1 | The application can change NFC settings, such as switching NFC on or off. |
| `http://tizen.org/privilege/nfc.cardemulation` | public   | -            | 2.3.1 | The application can access smart card details, such as credit card details, and allow users to make payments using NFC. |
| `http://tizen.org/privilege/notification` | public   | -            | 2.3.1 | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/packagemanager.admin` | platform | -            | 2.3.1 | The application can install and uninstall application packages. |
| `http://tizen.org/privilege/packagemanager.clearcache` | public   | -            | 3.0   | The application can clear other applications' caches. |
| `http://tizen.org/privilege/packagemanager.info` | public   | -            | 2.3.1 | The application can retrieve detailed application package information. |
| `http://tizen.org/privilege/peripheralio` | platform   | -            | 4.0 | The application can communicate with peripherals using industry standard protocols and interfaces, such as GPIO, I2C, PWM, UART, and SPI. |
| `http://tizen.org/privilege/power`       | public   | -            | 2.3.1 | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push`        | public   | -            | 2.3.1 | The application can receive notifications from the Internet. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/reboot`      | platform | -            | 2.3.1 | The application can restart the device.  |
| `http://tizen.org/privilege/recorder`    | public   | Microphone   | 2.3.1   | The application can record video and audio. |
| `http://tizen.org/privilege/screenshot`  | platform | -            | 2.3.1   | The application can capture screenshots. |
| `http://tizen.org/privilege/secureelement` | public   | -            | 2.3.1 | The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/systemmonitor` | public   | -            | 3.0   | The application can read system information, including information from the CPU and RAM. |
| `http://tizen.org/privilege/systemsettings.admin` | platform | -            | 2.3.1   | The application can read and write all system settings. |
| `http://tizen.org/privilege/tee.client` | partner | -            | 4.0   | The application can call security related functions running inside a Trusted Execution Environment (TEE), which ensures that sensitive data is stored, processed, and protected in an isolated, trusted environment.<br>**Allowed to licensed partners.** |
| `http://tizen.org/privilege/telephony`   | public   | -            | 2.3.1   | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/telephony.admin` | platform | -            | 2.3.1   | The application can manage telephony settings, such as those for incoming and outgoing calls, forwarding and holding calls, networks, and SIM cards. |
| `http://tizen.org/privilege/use_ir`      | public   | -            | 3.0   | The application can use the infrared transmitter. |
| `http://tizen.org/privilege/volume.set`  | public   | -            | 2.3.1   | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/widget.viewer` | public   | -            | 2.3.1 | The application can show widgets, and information from their associated applications, on the home screen. |
| `http://tizen.org/privilege/window.priority.set` | public   | -            | 2.3.1   | The application can appear on top of other windows and screens, including the lock screen, according to the order of priority of the windows. This can prevent the user from interacting with other applications or screens until the window for the application is closed. |
| `http://tizen.org/privilege/zigbee`      | public   | -            | 4.0   | The application can connect a ZigBee coordinator to end devices and control connected end devices. |
| `http://tizen.org/privilege/zigbee.admin`      | platform   | -            | 4.0   | The application can control a connected ZigBee coordinator, e.g. turning it on or off. |


<a name="nonAPI"></a>
## Non-API Bound Privileges


Tizen application privileges are loosely bound to APIs, so most of the
privileges can be identified by the APIs that the application calls.
However, there are some privileges that are not coupled with the Tizen
APIs. To allow easy identification, those privileges are mapped to
corresponding system resources - same as other privileges.

The following table lists the non-API bound privileges.

**Table: Non-API bound privileges**

| Privilege                                | Level  | Privacy  | Since(mobile/wearable) | Description                              |
|----------------------------------------|------|------|----------------------|----------------------------------------|
| `http://tizen.org/privilege/internet`    | public | - | 2.3 / 2.3.1            | Most of the mobile and wearable devices use a cellular network for IP communication. However, the cellular network can cause data costs and an application that sends data through the Internet can be crucial for user privacy. Due to the importance of the functionality, a privilege for controlling application Internet access has been added.<br><br>The new privilege is coupled with IP addresses of the destination and source of the IP packets. If your socket is connecting or listening to any IP address except 127.0.0.1, this privilege is required to communicate properly. If your application does not have this privilege, the connection is blocked in the kernel layer and returns an error in the `connect()` function as the permission is denied. If you are listening to a socket, you never receive any packets from the outside without errors on the socket functions.<br><br>If you are using the `listen()` and `connect()` functions between the local loopback interface (127.0.0.1), you cannot connect to a random application (due to sandboxing) no matter how you add this privilege. However, you can connect between multiple processes of the same application binary. |
| `http://tizen.org/privilege/mediastorage` | public | Storage | 2.3 / 2.3.1            | When you connect the device to a computer (Windows&reg; or macOS) through USB, you can access a dedicated media storage area shown as massive media storage. This region of the storage is called media storage and is usually used for multimedia files, such as photos, videos, and music files. Since this storage area is used for user private data, access to it must be protected with a privilege.<br>If your application does not have this privilege, no file operations into the media storage area succeed and you receive a permission denied error. If you have this privilege, you can read and write directories and files, create new files, and delete files in the storage area.<br><br>This privilege is treated as privacy privilege since platform version 4.0. |
| `http://tizen.org/privilege/externalstorage` | public | Storage | 2.3 / 2.3.1            | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege. You can find the absolute path of the external storage with the [Storage](../../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) API functions, such as `storage_get_root_directory()` function.<br>If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to the external storage.<br><br>This privilege is treated as privacy privilege since platform version 4.0. |
| `http://tizen.org/privilege/externalstorage.appdata` | public | - | 2.3 / 2.3.1            | Many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br><br>If your application does not have this privilege, no file operations with the application data stored in the external storage area succeed and you receive a permission denied error. If you have this privilege, you can store data in the application-specific directory of the external storage. You can find the path for storing data in the external storage with, for example, the `app_get_external_data_path()`, `app_get_external_cache_path()`, and `app_get_external_shared_data_path()` functions. |
| `http://tizen.org/privilege/appdir.shareddata` | public | - | 3.0 / 3.0              | Since Tizen 3.0, the application must have this privilege to support the `shared/data` directory.<br><br>The `app_get_shared_data_path()` and `app_manager_get_shared_data_path()` functions return an error when the application does not have this privilege. Note that the `shared/data` directory is writable for the application itself and readable for all other applications. You must be careful when you use this privilege and share data through the `shared/data` directory. For a more secure way of sharing files with another application, try to pass the file path through an application control. |
