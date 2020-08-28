
# Security and API Privileges

To effectively protect the device system and user private data, the Tizen security architecture is based on privileges and application signing of the Linux basic security model, which includes process isolation and mandatory access control. Since Tizen, as an open platform, provides a wide range of features and experiences for users with a variety of applications, the users must be able to grant privileges for security-sensitive operations.

Tizen provides API-level access control for security-sensitive operations which, if not used properly, can harm user privacy and system stability. Therefore, applications that use such sensitive APIs must declare the required privileges in the [config.xml](process/setting-properties.md#privilege) file.  Privileges are categorized into public, partner, and platform levels according to their hierarchy:

-   The public level is the minimum privilege level, which means that any application developed using Tizen Studio can use these privileges.
-   The partner level privileges require at least a partner-signed certificate which is granted to developers who have a business relationship with the vendor.
-   The platform level is the highest privilege level, and an application that needs these privileges requires at least a  platform-signed certificate, which is granted to vendor developers.

Since Tizen platform 3.0, some privileges are categorized as privacy-related and give an option to the user to switch them **on** and **off**. If an application invokes a privacy-related privileged API, the Tizen system checks whether the privilege is **allowed** for the application. For the application to use the API, the privilege must be declared in the `config.xml` file and the user must have switched it **on**.


> **Note**
>
> In applications with the platform version 3.0 or higher, if you use privacy-related privileged APIs, make sure that the user has switched the privilege on before making the function call. Otherwise, the application does not work as expected.
>
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../guides/security/privacy-related-permissions.md) using the Privacy Privilege API (in [mobile](../api/latest/device_api/mobile/tizen/ppm.html) and [wearable](../api/latest/device_api/wearable/tizen/ppm.html) applications).

Tizen Studio also provides privilege checker tools to check whether the Tizen application source code contains any privilege violations. For more information, see [Verifying Privilege Usage](../../tizen-studio/web-tools/privilege-checker.md).

The API version restriction of privileges are deprecated since platform version 5.0. So, if you are develeoping an app with an earlier API version and need information about supported version, see [this page](./old-versioned-sec-privileges.md). The page does not include privileges issued after 4.0.

<a name="API"></a>
## Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in Web applications:

**Table: Web Device API privileges**

| Privilege                            | Level    | Privacy    | Description |
|--------------------------------------|----------|------------|-------------|
| `http://tizen.org/privilege/account.read` | public | Account | The application can read accounts. |
| `http://tizen.org/privilege/account.write` | public | Account | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm` | public |  | The application can manage alarms by retrieving saved alarms and waking the device up at scheduled times. |
| `http://tizen.org/privilege/apphistory.read` | public | User history | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/application.info` | public |  | The application can retrieve information related to other applications. |
| `http://tizen.org/privilege/application.launch` | public |  | The application can open other applications using the application ID or application control. |
| `http://tizen.org/privilege/appmanager.certificate` | partner |  | The application can retrieve specified application certificates. |
| `http://tizen.org/privilege/appmanager.kill` | partner |  | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.launch` | public |  | The application can open other applications. |
| `http://tizen.org/privilege/bluetooth` | public |  | The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetooth.admin` | public |  | The application can change Bluetooth settings, such as turning Bluetooth on or off, setting the device name, and enabling or disabling AV remote control. Deprecated since 3.0. |
| `http://tizen.org/privilege/bluetooth.gap` | public |  | The application can use the Bluetooth Generic Access Profile (GAP). As an example, it can scan and pair with devices. Deprecated since 3.0. |
| `http://tizen.org/privilege/bluetooth.health` | public |  | The application can use the Bluetooth Health Device Profile (HDP). As an example, it can send health information. Deprecated since 3.0. |
| `http://tizen.org/privilege/bluetooth.spp` | public |  | The application can use the Bluetooth Serial Port Profile (SPP). As an example, it can send serial data. Deprecated since 3.0. |
| `http://tizen.org/privilege/bluetoothmanager` | platform |  | The application can change Bluetooth system settings related to privacy and security, such as the visibility mode. |
| `http://tizen.org/privilege/bookmark.read` | platform | Bookmark | The application can read bookmarks. |
| `http://tizen.org/privilege/bookmark.write` | platform | Bookmark | The application can create, edit, and delete bookmarks. |
| `http://tizen.org/privilege/calendar.read` | public | Calendar | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public | Calendar | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call` | public | Call | The application can make phone calls to numbers when they are tapped without further confirmation. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/callhistory.read` | public | Contacts & User history | The application can read call log items. |
| `http://tizen.org/privilege/callhistory.write` | public | Contacts & User history | The application can create, update, and delete call log items. |
| `http://tizen.org/privilege/contact.read` | public | Contacts | The application can read user's profile, contacts, and contact history. Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public | Contacts | The application can create, update, and delete user's profile, contacts, and any contact history that is related to this application. Contact history can include social network activity. |
| `http://tizen.org/privilege/content.read` | public |  | The application can read media content information. |
| `http://tizen.org/privilege/content.write` | public |  | The application can change media information. This information can be used by other applications. |
| `http://tizen.org/privilege/datacontrol.consumer` | public |  | The application can read data exported by data control providers. |
| `http://tizen.org/privilege/datasharing` | public |  | The application can share data with other applications. |
| `http://tizen.org/privilege/datasync` | public |  | The application can sync device data, such as contacts and calendar events, using the OMA DS 1.2 protocol. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/download` | public |  | The application can manage HTTP downloads. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/filesystem.read` | public |  | The application can read file systems. |
| `http://tizen.org/privilege/filesystem.write` | public |  | The application can write to file systems. |
| `http://tizen.org/privilege/healthinfo` | public | Sensor | The application can read health information gathered by the device sensors, such as the pedometer and the heart rate monitor. |
| `http://tizen.org/privilege/ime` | public |  | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/internet` | public | | The application can access the Internet. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/keymanager` | public |  | The application can save keys, certificates, and data to, and retrieve and delete them from, password-protected storage. Checking the statuses of certificates while connected to a mobile network may result in additional charges depending on user's payment plan. Deprecated since 3.0. |
| `http://tizen.org/privilege/led` | public |  | The application can turn LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/location` | public | | The application can use user's location data. |
| `http://tizen.org/privilege/mediacapture` | public | Camera & Microphone | The application can capture video and audio data.  |
| `http://tizen.org/privilege/mediacontroller.client` | public |  | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public |  | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/messaging.read` | public | Message & Storage | The application can retrieve emails, text messages, and multimedia messages from the server or receive them directly. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/messaging.write` | public | Message & Storage | The application can write text messages, multimedia messages, and emails. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/networkbearerselection` | partner |  | The application can restrict the device so some specific domains can only be accessed via mobile networks. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/nfc.admin` | public |  | The application can change NFC settings, such as turning NFC on or off. Deprecated since 2.3. |
| `http://tizen.org/privilege/nfc.cardemulation` | public |  | The application can access smart card details, such as credit card details, and allow users to make payments via NFC. |
| `http://tizen.org/privilege/nfc.common` | public |  | The application can use NFC common features. |
| `http://tizen.org/privilege/nfc.p2p` | public |  | The application can push NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.tag` | public |  | The application can read and write NFC tag information. |
| `http://tizen.org/privilege/notification` | public | | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/package.info` | public |  | The application can receive package information. |
| `http://tizen.org/privilege/packagemanager.install` | platform |  | The application can install or uninstall application packages. |
| `http://tizen.org/privilege/power` | public |  | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push` | public |  | The application can receive notifications via the internet. This may result in additional charges depending on user's payment plan. |
| `http://tizen.org/privilege/recorder` | public | Microphone | The application can record video and audio. |
| `http://tizen.org/privilege/secureelement` | public |  | The application can access secure smart card chips such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/setting` | public |  | The application can change and read user settings. |
| `http://tizen.org/privilege/system` | public |  | The application can read system information. |
| `http://tizen.org/privilege/systemmanager` | partner |  | The application can read secure system information. Deprecated since 2.4. |
| `http://tizen.org/privilege/tee.client` | partner |  | The application can call security related functions running inside a Trusted Execution Environment (TEE), which ensures that sensitive data is stored, processed, and protected in an isolated, trusted environment. |
| `http://tizen.org/privilege/telephony` | public |  | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the statuses of calls. |
| `http://tizen.org/privilege/tv.audio` | public |  | The application can change the volume, enable and disable silent mode, detect volume changes, and play beeps. Deprecated since 5.0. |
| `http://tizen.org/privilege/tv.display` | public |  | The application can check whether a device supports 3D and read information about 3D mode. Deprecated since 5.0. |
| `http://tizen.org/privilege/tv.inputdevice` | public |  | The application can capture the key events of an input device, for example, TV remote control, and release key grabbing. |
| `http://tizen.org/privilege/tv.window` | public |  | The application can embed the display of a video source, specify the size, and show or hide the embedded display. |
| `http://tizen.org/privilege/volume.set` | public |  | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/websetting` | public |  | The application can change its web application settings, including deleting its cookies. Deprecated since 2.4. |
| `http://tizen.org/privilege/widget.viewer` | public |  | The application can show widgets, and information from their associated applications, on the home screen. |

**Table: Web W3C/HTML5 API privileges**

| Privilege                                | Level  | Privacy               | Description                              |
| ---------------------------------------- | ------ | --------------------- | ---------------------------------------- |
| `http://tizen.org/privilege/internet`    | public |                       | The application can access the internet using the [WebSocket](../api/latest/w3c_api/w3c_api_m.html#websocket), [XMLHttpRequest](../api/latest/w3c_api/w3c_api_m.html#httpreq), [Server-Sent Events](../api/latest/w3c_api/w3c_api_m.html#serversent), [HTML5 Application caches](../api/latest/w3c_api/w3c_api_m.html#cache), and [Cross-Origin Resource Sharing](../api/latest/w3c_api/w3c_api_m.html#cross) APIs. |
| `http://tizen.org/privilege/location`    | public | Location              | The application can access geographic locations using the [Geolocation](../api/latest/w3c_api/w3c_api_m.html#geo) API.<br>**Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>- In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |
| `http://tizen.org/privilege/mediacapture` | public | Camera & Microphone | The application can manipulate streams from cameras and microphones using the [getUserMedia](../api/latest/w3c_api/w3c_api_m.html#getusermedia) API.<br> **Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>-  In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |
| `http://tizen.org/privilege/notification` | public |                       | The application can display simple notifications using the [Web Notifications](../api/latest/w3c_api/w3c_api_m.html#webnoti) API.<br>**Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br>- In the remote domain, pop-up user prompt is used. |
| `http://tizen.org/privilege/unlimitedstorage` | public |                       | The application can use the storage with unlimited size with the [File API: Directories and System](../api/latest/w3c_api/w3c_api_m.html#directory), [File API: Writer](../api/latest/w3c_api/w3c_api_m.html#writer), [Indexed Database](../api/latest/w3c_api/w3c_api_m.html#database), and [Web SQL Database](../api/latest/w3c_api/w3c_api_m.html#sql) APIs.<br>**Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br>- In the remote domain, pop-up user prompt is used. |

**Table: Web Supplementary API privileges**

| Privilege                               | Level  | Privacy | Description                              |
| --------------------------------------- | ------ | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/audiorecorder` | public | Microphone            | The application can record an audio stream on a target device using the [Camera API (Tizen Extension)](../api/latest/w3c_api/w3c_api_w.html#camera) (Audio Recording) API.<br>**Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>- In the remote domain, execution is blocked. |
| `http://tizen.org/privilege/camera`      | public | Camera & Microphone | The application can capture video and image on a target device using the [Camera API (Tizen Extension)](../api/latest/w3c_api/w3c_api_w.html#camera) (Video Recording and Image Capture) API.<br>**Privilege behavior:**<br>- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>- In the remote domain, execution is blocked. |
| `http://tizen.org/privilege/fullscreen` | public |  | The application can display in the full-screen mode using the [FullScreen API - Mozilla](../api/latest/w3c_api/w3c_api_m.html#fullscreen) API.<br>**Privilege behavior:**<br>- If this privilege is defined, permission is granted without user interaction. Otherwise, permission is granted by user interaction. |


<a name="nonAPI"></a>
## Non-API Bound Privileges

Tizen application privileges are loosely bound to APIs, so most of the privileges can be identified by the APIs that the application calls. However, there are some privileges that are not coupled with the Tizen APIs. To allow easy identification, those privileges are mapped to corresponding system resources that are similar to other privileges.

The following table lists the non-API bound privileges:

**Table: Non-API bound privileges**

| Privilege      | Level          | Privacy        | Description    |
|---------------|---------------|-----------------|-----------------|
| `http://tizen.org/privilege/mediastorage` | public | Storage | When you connect the device to a computer (Windows&reg; or macOS) through USB, you can access a dedicated media storage area shown as massive media storage. This region of the storage is called media storage and is usually used for multimedia files, such as photos, videos, and music files. Since this storage area is used for user private data, access to it must be protected with a privilege.<br> If your application does not have this privilege, no file operations into the media storage area succeed and you receive a permission denied error. If you have this privilege, you can read and write directories and files, create new files, and delete files in the storage area.      |
| `http://tizen.org/privilege/externalstorage` | public | Storage | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br> If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to the external storage. |
