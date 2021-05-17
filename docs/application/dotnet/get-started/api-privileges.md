# API Privileges

To effectively protect the device system and user private data, the
Tizen security architecture is based on privileges and application
signing of the Linux basic security model, which includes process
isolation and mandatory access control. Since Tizen, as an open 
platform, provides a wide range of features and experiences for users
with a variety of applications, the users must be able to grant
privileges for security-sensitive operations.

Tizen provides API-level access control for security-sensitive
operations which, if not used properly, can harm user privacy and
system stability. Therefore, applications that use such sensitive APIs
must declare the required privileges in the
tizen-manifest.xml file.
Privileges are categorized into public, partner, and platform levels
according to their hierarchy:

-   The public level is the minimum privilege level, which means that
    any application developed using Tizen Studio can use
    these privileges.
-   The partner level privileges require at least a partner-signed
    certificate which is granted to developers who have a business
    relationship with the vendor.
-   The platform level is the highest privilege level, and an
    application that needs these privileges requires at least a
    platform-signed certificate, which is granted to vendor developers.

Since Tizen platform 3.0, some privileges are categorized as
privacy-related and gives an option to the user to switch them **on** and
**off**. If an application invokes a privacy-related privileged API, the
Tizen system checks whether the privilege is **allowed** for the
application. For the application to use the API, the privilege must be
declared in the `tizen-manifest.xml` file and the user must have
switched it **on**.

> [!NOTE]  
> In applications with the platform version 3.0 or higher, if you use privacy-related privileged APIs, make sure that the user has switched the privilege on before making the function call. Otherwise, the application does not work as expected.
>
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../guides/security/privacy-related-permissions.md) using the [Privacy Privilege Manager API](/application/dotnet/api/TizenFX/latest/api/Tizen.Security.PrivacyPrivilegeManager.html).

Tizen Studio also provides privilege checker tools to check whether the Tizen application source code contains any privilege violations. For more information, see [Verifying APIs and
Privileges](../../tizen-studio/native-tools/api-checker.md).

<a name="API"></a>
## .NET API Privileges

The following table lists the API privileges, which you must declare
when using security-sensitive API modules in .net applications:

**Table: .NET API privileges**

| Privilege                            | Level    | Privacy    | Description                              |
|--------------------------------------|----------|------------|------------------------------------------|
| `http://tizen.org/privilege/account.read` | public | Account | The application can read accounts. |
| `http://tizen.org/privilege/account.write` | public | Account | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm.get` | public |  | The application can read information about user's saved alarms. |
| `http://tizen.org/privilege/alarm.set` | public |  | The application can set alarms and wake the device up at scheduled times. |
| `http://tizen.org/privilege/antivirus.admin` | platform |  | The application can enable or disable antivirus programs and manage detected malware. |
| `http://tizen.org/privilege/antivirus.scan` | partner |  | The application can request to scan files in any other applications or on the device to detect harmful content. |
| `http://tizen.org/privilege/antivirus.webprotect` | partner |  | The application can check the reputation of a web address and determine whether or not accessing it could put user's device at risk. |
| `http://tizen.org/privilege/apphistory.read` | public | User history | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/appmanager.kill` | platform |  | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.kill.bgapp` | public |  | The application can request to close applications running in the background. |
| `http://tizen.org/privilege/appmanager.launch` | public |  | The application can open other applications. |
| `http://tizen.org/privilege/autofillmanager` | platform |  | The application can manage installed autofill services, detect which autofill service is currently being used, and change which autofill service to use. |
| `http://tizen.org/privilege/blocknumber.read` | partner |  | The application can read rules for blocking calls and messages. |
| `http://tizen.org/privilege/blocknumber.write` | partner |  | The application can write rules for blocking calls and messages. |
| `http://tizen.org/privilege/bluetooth` | public |  | The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetooth.admin` | platform |  | The application can change Bluetooth settings, such as turning Bluetooth on or off, setting the device name, and enabling or disabling AV remote control. |
| `http://tizen.org/privilege/bookmark.admin` | platform | Bookmark | The application can retrieve, create, edit, and delete internet bookmarks. |
| `http://tizen.org/privilege/calendar.read` | public | Calendar | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public | Calendar | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call` | public | Call | The application can make phone calls to numbers when they are tapped without further confirmation. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/callhistory.read` | public | User history | The application can read call log items. |
| `http://tizen.org/privilege/callhistory.write` | public | User history | The application can create, update, and delete call log items. |
| `http://tizen.org/privilege/camera` | public | Camera | The application can take pictures and turn the camera flash on and off while using Camera. |
| `http://tizen.org/privilege/contact.read` | public | Contacts | The application can read user's profile, contacts, and contact history. Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public | Contacts | The application can create, update, and delete user's profile, contacts, and any contact history that is related to this application. Contact history can include social network activity. |
| `http://tizen.org/privilege/content.write` | public |  | The application can change media information. This information can be used by other applications. |
| `http://tizen.org/privilege/d2d.datasharing` | public |  | The application can share data with other devices. |
| `http://tizen.org/privilege/d2d.remotelaunch` | public |  | The application can be opened or used by applications on other devices. |
| `http://tizen.org/privilege/datasharing` | public |  | The application can share data with other applications. |
| `http://tizen.org/privilege/devicecertificate` | platform |  | The application can use a device certificate and its private key to communicate securely with a remote server. |
| `http://tizen.org/privilege/display` | public |  | The application can manage display settings, such as the brightness. This may increase battery consumption. |
| `http://tizen.org/privilege/download` | public |  | The application can manage HTTP downloads. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/dpm.bluetooth` | partner |  | The application can restrict Bluetooth connections. This may prevent applications that use Bluetooth from working properly. |
| `http://tizen.org/privilege/dpm.browser` | partner |  | The application can prevent the use of browser applications. This may prevent applications that use browser applications from working properly. |
| `http://tizen.org/privilege/dpm.camera` | partner |  | The application can restrict the use of the camera. This may prevent applications that use the camera from working properly. |
| `http://tizen.org/privilege/dpm.clipboard` | partner |  | The application can restrict the use of the clipboard. This may prevent applications that use the clipboard from working properly. |
| `http://tizen.org/privilege/dpm.debugging` | partner |  | The application can restrict the use of debugging. This may prevent applications that use debugging from working properly. |
| `http://tizen.org/privilege/dpm.email` | partner |  | The application can restrict POP and IMAP email access. This may prevent applications that use email services from working properly. |
| `http://tizen.org/privilege/dpm.location` | partner |  | The application can restrict the use of location functions. This may prevent applications that use location functions from working properly. |
| `http://tizen.org/privilege/dpm.lock` | partner |  | The application can lock the device. |
| `http://tizen.org/privilege/dpm.message` | partner |  | The application can restrict the use of text, multimedia, and chat messaging services. This may prevent applications that use messaging services from working properly. |
| `http://tizen.org/privilege/dpm.microphone` | partner |  | The application can restrict the use of the microphone. This may prevent applications that use the microphone from working properly. |
| `http://tizen.org/privilege/dpm.password` | partner |  | The application can manage password policies and reset the passwords used to unlock the phone and recover data. |
| `http://tizen.org/privilege/dpm.security` | partner |  | The application can change security settings such as those for certificate installation, data encryption, and factory data resets. |
| `http://tizen.org/privilege/dpm.storage` | partner |  | The application can prevent the use of external storage such as SD cards and USB storage devices. This may prevent applications that use external storage from working properly. |
| `http://tizen.org/privilege/dpm.usb` | partner |  | The application can prevent USB connections, including the use of USB tethering. This may prevent applications that use USB connections from working properly. |
| `http://tizen.org/privilege/dpm.wifi` | partner |  | The application can restrict the use of Wi-Fi networks and Mobile Hotspots. If the phone can not connect to a Wi-Fi network, it may connect to a mobile network. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/dpm.wipe` | partner |  | The application can erase all data from user's device and reset user's device to its factory default settings. |
| `http://tizen.org/privilege/dpm.zone` | partner |  | The application can create and remove containers. Containers are private workspaces which provide separate app runtime environments and data storage. |
| `http://tizen.org/privilege/email` | public |  | The application can manage user's email accounts, including user's folders and emails, POP3 and IMAP downloads, and SMTP uploads. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/email.admin` | platform |  | The application can manage the settings of email applications. |
| `http://tizen.org/privilege/fido.client` | public |  | The application can trigger authenticators in user's device and it may request to use user's PIN or biometrics (fingerprints or irises) for authentication. |
| `http://tizen.org/privilege/gestureactivation` | platform |  | The application can allow and block special touch gestures. |
| `http://tizen.org/privilege/gesturegrab` | platform |  | The application can read special touch gestures, even while it is running in the background. |
| `http://tizen.org/privilege/haptic` | public |  | The application can control vibration feedback. |
| `http://tizen.org/privilege/healthinfo` | public | Sensor | The application can read health information gathered by the device sensors, such as the pedometer and the heart rate monitor. |
| `http://tizen.org/privilege/ime` | public |  | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/imemanager` | public |  | The application can manage installed input methods. |
| `http://tizen.org/privilege/inputgenerator` | platform |  | The application can simulate keys being pressed and touch interactions with the screen. |
| `http://tizen.org/privilege/keygrab` | platform |  | The application can read actions involving special keys, such as the volume keys on this or other devices (for example, TV remote controls), even when it is running in the background. |
| `http://tizen.org/privilege/keymanager` | public |  | The application can save keys, certificates, and data to, and retrieve and delete them from, password-protected storage. Checking the statuses of certificates while connected to a mobile network may result in additional charges depending on user's payment plan. Deprecated since 3.0. |
| `http://tizen.org/privilege/keymanager.admin` | platform |  | The application can lock and unlock password-protected storage, and manage password changes for it. Deprecated since 3.0. |
| `http://tizen.org/privilege/led` | public |  | The application can turn LEDs on or off. For example, the LED on the front of the device and the camera flash can be turned on or off. |
| `http://tizen.org/privilege/location` | public | Location | The application can use user's location data. |
| `http://tizen.org/privilege/location.coarse` | public | Location | The application can determine user's approximate location including user's device's Cell ID, LAC (Location Area Code), and TAC (Tracking Area Code). |
| `http://tizen.org/privilege/location.enable` | platform |  | The application can control user's location service settings. |
| `http://tizen.org/privilege/mapservice` | public |  | The application can use map services such as Geocoder, Places, and Route (Direction). |
| `http://tizen.org/privilege/mediacontroller.client` | public |  | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public |  | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/mediahistory.read` | public | User history | The application can read the statistics concerning the music and videos played on the device, such as the peak times for playing music or videos. |
| `http://tizen.org/privilege/message.read` | public | Message | The application can read text and multimedia messages, and any information related to them. |
| `http://tizen.org/privilege/message.write` | public | Message | The application can write, send, delete, move text and multimedia messages, download multimedia messages, and change the settings and statuses of messages, such as read or unread. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/minicontrol.provider` | public |  | The application can show a small toolbar on the notification panel or lock screen while it is open. Deprecated since 3.0. |
| `http://tizen.org/privilege/network.get` | public |  | The application can retrieve network information such as the status of each network, its type, and detailed network profile information. |
| `http://tizen.org/privilege/network.profile` | public |  | The application can add, remove, and edit network profiles. |
| `http://tizen.org/privilege/network.route` | partner |  | The application can add or remove route table entries. |
| `http://tizen.org/privilege/network.set` | public |  | The application can turn Wi-Fi on and off, and connect to and disconnect from Wi-Fi and mobile networks. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/nfc` | public |  | The application can read and write NFC tag information, and send NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.admin` | platform |  | The application can change NFC settings, such as turning NFC on or off. |
| `http://tizen.org/privilege/nfc.cardemulation` | public |  | The application can access smart card details, such as credit card details, and allow users to make payments via NFC. |
| `http://tizen.org/privilege/notification` | public |  | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/packagemanager.admin` | platform |  | The application can install and uninstall application packages. |
| `http://tizen.org/privilege/packagemanager.clearcache` | public |  | The application can clear other applications' caches. |
| `http://tizen.org/privilege/packagemanager.info` | public |  | The application can retrieve detailed application package information. |
| `http://tizen.org/privilege/peripheralio` | platform |  | The application can communicate with peripherals using industry standard protocols and interfaces, such as GPIO, I2C, PWM, UART, and SPI. |
| `http://tizen.org/privilege/power` | public |  | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push` | public |  | The application can receive notifications via the internet. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/reboot` | platform |  | The application can restart the device. |
| `http://tizen.org/privilege/recorder` | public | Microphone | The application can record video and audio. |
| `http://tizen.org/privilege/screenshot` | platform |  | The application can capture screenshots. |
| `http://tizen.org/privilege/secureelement` | public |  | The application can access secure smart card chips such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/securesysteminfo` | partner | Device unique ID | The application can read the non-resettable secure device information. |
| `http://tizen.org/privilege/shortcut` | public |  | The application can create and delete shortcuts. |
| `http://tizen.org/privilege/softap` | public |  | The application can manage SoftAP configuration settings, such as the Service Set Identifier (SSID) and password. |
| `http://tizen.org/privilege/softap.admin` | platform |  | The application can turn SoftAP on or off, and change its settings. |
| `http://tizen.org/privilege/systemmonitor` | public |  | The application can read system information, including information from the CPU and RAM. |
| `http://tizen.org/privilege/systemsettings` | public |  | The application can read and write unrestricted system settings. Deprecated since 2.3.1. |
| `http://tizen.org/privilege/systemsettings.admin` | platform |  | The application can read and write all system settings. |
| `http://tizen.org/privilege/tee.client` | partner |  | The application can call security related functions running inside a Trusted Execution Environment (TEE), which ensures that sensitive data is stored, processed, and protected in an isolated, trusted environment. |
| `http://tizen.org/privilege/telephony` | public |  | The application can retrieve telephony information, such as network and SIM card used and statuses of calls. |
| `http://tizen.org/privilege/telephony.admin` | platform |  | The application can manage telephony settings, such as those for incoming and outgoing calls, forwarding and holding calls, networks, and SIM cards. |
| `http://tizen.org/privilege/tethering.admin` | platform |  | The application can enable and disable tethering services. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/use_ir` | public |  | The application can use the infrared transmitter. |
| `http://tizen.org/privilege/voicecontrol.manager` | platform |  | The application can record user's voice and recognize it so that voice commands can be used to control this app. It can also give responses to user's commands. |
| `http://tizen.org/privilege/voicecontrol.tts` | partner |  | The application can use the voice control engine to recognize your voice commands and provide voice feedback using its own voice. |
| `http://tizen.org/privilege/volume.set` | public |  | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/vpnservice` | public |  | The application can manage the Virtual Private Network (VPN) and change its settings. |
| `http://tizen.org/privilege/web-history.admin` | platform | User history | The application can manage user's internet history. |
| `http://tizen.org/privilege/widget.viewer` | public |  | The application can show widgets, and information from their associated applications, on the home screen. |
| `http://tizen.org/privilege/wifidirect` | public |  | The application can enable and disable Wi-Fi Direct, manage Wi-Fi Direct connections, and change Wi-Fi Direct settings. |
| `http://tizen.org/privilege/window.priority.set` | public |  | The application can appear on top of other windows and screens, including the lock screen, according to the order of priority of the windows. This may prevent user from interacting with other applications or screens until the window for this application is closed. |
| `http://tizen.org/privilege/windowsystem.admin` | platform |  | The application can change the settings for services provided by the display server, such as the quick panel and softkey bar. |
| `http://tizen.org/privilege/zigbee` | public |  | The application can connect a ZigBee coordinator to end devices and control connected end devices. |
| `http://tizen.org/privilege/zigbee.admin` | platform |  | The application can control a connected ZigBee coordinator, for example, turning it on or off. |

<a name="nonAPI"></a>
## Non-API Bound Privileges


Tizen application privileges are loosely bound to APIs, so most of the
privileges can be identified by the APIs that the application calls.
However, there are some privileges that are not coupled with Tizen
APIs. To allow easy identification, those privileges are mapped to
corresponding system resources that are similar to other privileges.

The following table lists the non-API bound privileges:

**Table: Non-API bound privileges**

| Privilege                                | Level  | Privacy  | Description                              |
|----------------------------------------|------|------|----------------------------------------|
| `http://tizen.org/privilege/internet`    | public |  | Most of the mobile and wearable devices use a cellular network for IP communication. However, the cellular network can cause data costs and an application that sends data through the internet can be crucial for user privacy. Due to the importance of the functionality, a privilege for controlling application internet access has been added.<br><br>The new privilege is coupled with IP addresses of the destination and source of the IP packets. If your socket is connecting or listening to any IP address except 127.0.0.1, this privilege is required to communicate properly. If your application does not have this privilege, the connection is blocked in the kernel layer. If you are listening to a socket, you never receive any packets from the outside without errors on the socket functions.<br><br>You cannot connect to a random application (due to sandboxing) no matter how you add this privilege but you can connect between multiple processes of the same application binary. |
| `http://tizen.org/privilege/mediastorage` | public | Storage | When you connect the device to a computer (Windows&reg; or macOS) through USB, you can access a dedicated media storage area shown as massive media storage. This region of the storage is called media storage and is usually used for multimedia files, such as photos, videos, and music files. Since this storage area is used for user private data, access to it must be protected with a privilege.<br>If your application does not have this privilege, no file operations into the media storage area succeed and you receive a permission denied error. If you have this privilege, you can read and write directories and files, create new files, and delete files in the storage area.<br><br>This privilege is treated as privacy privilege since platform version 4.0. |
| `http://tizen.org/privilege/externalstorage` | public | Storage | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, access to external storage must be protected with a privilege. You can find the absolute path of the external storage with the [Storage](/application/dotnet/api/TizenFX/latest/api/Tizen.System.Storage.html) API functions, such as `GetAbsolutePath()` method.<br>If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to external storage.<br><br>This privilege is treated as privacy privilege since platform version 4.0. |
| `http://tizen.org/privilege/externalstorage.appdata` | public |  | Many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br><br>If your application does not have this privilege, no file operations with the application data stored in the external storage area succeed and you receive a permission denied error. If you have this privilege, you can store data in the application-specific directory of the external storage. You can get the absolute path to the application's external data directory with `ExternalData` property of `Tizen.Applications.DirectoryInfo`. |
| `http://tizen.org/privilege/appdir.shareddata` | public |  | Since Tizen 3.0, the application must have this privilege to support the `shared/data` directory.<br><br>You can get share directory path with `SharedDataPath` property of `Tizen.Applications.ApplicationInfo` if the application have shared/data directory. Note that the `shared/data` directory is writable for the application itself and readable for all other applications. You must be careful when you use this privilege and share data through the `shared/data` directory. For a more secure way of sharing files with another application, try to pass the file path through an application control. |
