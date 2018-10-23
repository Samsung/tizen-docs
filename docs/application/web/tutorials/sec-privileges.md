
# Security and API Privileges

To effectively protect the device system and user private data, the Tizen security architecture is based on privileges and application signing of the Linux basic security model, which includes process isolation and mandatory access control. Since Tizen, as an open platform, provides a wide range of features and experiences for users with a variety of applications, the users must be able to grant privileges for security-sensitive operations.

Tizen provides API-level access control for security-sensitive operations which, if not used correctly, can harm user privacy and system stability. Therefore, applications that use such sensitive APIs must declare the required privileges in the [config.xml](process/setting-properties.md#privilege) file.  Privileges are categorized into public, partner, and platform levels according to their hierarchy:

-   The public level is the minimum privilege level, which means that any application developed using the Tizen Studio can use these privileges.
-   The partner level privileges require at least a partner-signed certificate which is granted to developers who have a business relationship with the vendor.
-   The platform level is the highest privilege level, and an application that needs these privileges requires at least a  platform-signed certificate, which is granted to vendor developers.

Since Tizen platform 3.0, some privileges are categorized as privacy-related and give an option to the user to switch them on and off. If an application invokes a privacy-related privileged API, the Tizen system checks whether the privilege is **allowed** for the application. For the application to use the API, the privilege must be declared in the `config.xml` file and the user must have switched it on.


> **Note**  
> In applications with the platform version 3.0 or higher, if you use privacy-related privileged APIs, make sure that the user has switched the privilege on before making the function call. Otherwise, the application does not work as expected.
>
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../guides/security/privacy-related-permissions.md) using the Privacy Privilege API (in [mobile](../api/latest/device_api/mobile/tizen/ppm.html) and [wearable](../api/latest/device_api/wearable/tizen/ppm.html) applications).

The Tizen Studio also provides privilege checker tools to check whether the Tizen application source code contains any privilege violations. For more information, see [Verifying Privilege Usage](../../tizen-studio/web-tools/privilege-checker.md).

<a name="mobile"></a>
## Mobile Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in mobile Web applications.

**Table: Mobile Web Device API privileges**

| Privilege                                | Level    | Privacy                   | Since | Description                              |
| ---------------------------------------- | -------- | ------------------------- | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/account.read` | public   | Account                   | 2.3   | The application can read accounts.       |
| `http://tizen.org/privilege/account.write` | public   | Account                   | 2.3   | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm`       | public   | -                         | 2.2.1 | The application can manage alarms by retrieving saved alarms and waking the device up at scheduled times. |
| `http://tizen.org/privilege/apphistory.read` | public   | -                         | 4.0   | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/application.info` | public   | -                         | 2.2.1 | The application can retrieve information related to other applications. |
| `http://tizen.org/privilege/application.launch` | public   | -                         | 2.2.1 | The application can open other applications using the application ID or application control. |
| `http://tizen.org/privilege/appmanager.certificate` | partner  | -                         | 2.2.1 | The application can retrieve specified application certificates. |
| `http://tizen.org/privilege/appmanager.kill` | partner  | -                         | 2.2.1 | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.launch` | public   | -                         | 4.0   | The application can open other applications. |
| `http://tizen.org/privilege/bluetooth`   | public   | -                         | 2.4   | The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetoothmanager` | platform | -                         | 2.2.1 | The application can change Bluetooth system settings related to privacy and security, such as the visibility mode. |
| `http://tizen.org/privilege/bookmark.read` | platform | Bookmark                  | 2.2.1 | The application can read bookmarks.      |
| `http://tizen.org/privilege/bookmark.write` | platform | Bookmark                  | 2.2.1 | The application can create, edit, and delete bookmarks. |
| `http://tizen.org/privilege/calendar.read` | public   | Calendar                  | 2.2.1 | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public   | Calendar                  | 2.2.1 | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call`        | public   | Call                      | 2.3   | The application can make phone calls to numbers when they are tapped without further confirmation. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/callhistory.read` | public   | Contacts and User history | 2.2.1 | The application can read call log items. |
| `http://tizen.org/privilege/callhistory.write` | public   | Contacts and User history | 2.2.1 | The application can create, update, and delete call log items. |
| `http://tizen.org/privilege/contact.read` | public   | Contacts                  | 2.2.1 | The application can read the user profile, contacts, and contact history.<br> Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public   | Contacts                  | 2.2.1 | The application can create, update, and delete the user profile, contacts, and any contact history that is related to this application.<br> Contact history can include social network activity. |
| `http://tizen.org/privilege/content.read` | public   | -                         | 2.2.1 | The application can read media content information. |
| `http://tizen.org/privilege/content.write` | public   | -                         | 2.2.1 | The application can create, update, and delete media content information. |
| `http://tizen.org/privilege/datacontrol.consumer` | public   | -                         | 2.2.1 | The application can read data exported by data control providers. |
| `http://tizen.org/privilege/datasharing` | public   | -                         | 4.0   | The application can share data with other applications. |
| `http://tizen.org/privilege/datasync`    | public   | -                         | 2.2.1 | The application can synchronize device data, such as contacts and calendar events, using the OMA DS 1.2 protocol. |
| `http://tizen.org/privilege/download`    | public   | -                         | 2.2.1 | The application can manage HTTP downloads. |
| `http://tizen.org/privilege/filesystem.read` | public   | -                         | 2.2.1 | The application can read file systems.   |
| `http://tizen.org/privilege/filesystem.write` | public   | -                         | 2.2.1 | The application can write to file systems. |
| `http://tizen.org/privilege/healthinfo`  | public   | Sensor                    | 2.3   | The application can read the user's health information gathered by device sensors, such as pedometer or heart rate monitor. |
| `http://tizen.org/privilege/ime`         | public   | -                         | 2.4   | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/led`         | public   | -                         | 2.4   | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/location`    | public   | Location                  | 2.2.1 | The application can read the user's location information. |
| `http://tizen.org/privilege/mediacontroller.client` | public   | -                         | 2.4   | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public   | -                         | 2.4   | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/messaging.read` | public   | Message                   | 2.2.1 | The application can retrieve messages from message boxes or receive messages. |
| `http://tizen.org/privilege/messaging.write` | public   | Message                   | 2.2.1 | The application can write, send, sync, and remove text messages, multimedia messages, and emails. |
| `http://tizen.org/privilege/networkbearerselection` | partner  | -                         | 2.2.1 | The application can request and release a specific network connection. |
| `http://tizen.org/privilege/nfc.admin`   | public   | -                         | 2.2.1 | The application can change NFC settings, such as switching NFC on or off. |
| `http://tizen.org/privilege/nfc.cardemulation` | public   | -                         | 2.3   | The application can access smart card details, such as credit card details, and allow users to make payments through NFC. |
| `http://tizen.org/privilege/nfc.common`  | public   | -                         | 2.2.1 | The application can use common NFC features. |
| `http://tizen.org/privilege/nfc.p2p`     | public   | -                         | 2.2.1 | The application can push NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.tag`     | public   | -                         | 2.2.1 | The application can read and write NFC tag information. |
| `http://tizen.org/privilege/notification` | public   | -                         | 2.2.1 | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/package.info` | public   | -                         | 2.2.1 | The application can retrieve information about installed packages. |
| `http://tizen.org/privilege/packagemanager.install` | platform | -                         | 2.2.1 | The application can install or uninstall application packages. |
| `http://tizen.org/privilege/power`       | public   | -                         | 2.2.1 | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push`        | public   | -                         | 2.2.1 | The application can receive notifications from the Internet. |
| `http://tizen.org/privilege/recorder`    | public   | -                         | 4.0   | The application can record video and audio. |
| `http://tizen.org/privilege/secureelement` | public   | -                         | 2.2.1 | The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/setting`     | public   | -                         | 2.2.1 | The application can change and read user settings. |
| `http://tizen.org/privilege/system`      | public   | -                         | 2.2.1 | The application can read system information. |
| `http://tizen.org/privilege/tee.client`  | partner  | -                         | 4.0   | The application can communicate with a Trusted Application. |
| `http://tizen.org/privilege/telephony`   | public   | -                         | 2.3.1 | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/volume.set`  | public   | -                         | 2.3   | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/websetting`  | public   | -                         | 2.2.1 | The application can change its Web application settings, including deleting cookies. **Deprecated since 2.4.** |
| `http://tizen.org/privilege/widget.viewer` | public   | -                         | 3.0   | The application can show widgets, and information from their associated applications, on the home screen. |

**Table: Mobile Web W3C/HTML5 API privileges**

| Privilege                                | Level  | Privacy               | Since | Description                              |
| ---------------------------------------- | ------ | --------------------- | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/internet`    | public | -                     | 2.3   | The application can access the Internet using the [WebSocket](../api/latest/w3c_api/w3c_api_m.html#websocket), [XMLHttpRequest](../api/latest/w3c_api/w3c_api_m.html#httpreq), [Server-Sent Events](../api/latest/w3c_api/w3c_api_m.html#serversent), [HTML5 Application caches](../api/latest/w3c_api/w3c_api_m.html#cache), and [Cross-Origin Resource Sharing](../api/latest/w3c_api/w3c_api_m.html#cross) APIs. |
| `http://tizen.org/privilege/mediacapture` | public | Camera and Microphone | 2.2.1 | The application can manipulate streams from cameras and microphones using the [getUserMedia](../api/latest/w3c_api/w3c_api_m.html#getusermedia) API.<br> **Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |
| `http://tizen.org/privilege/unlimitedstorage` | public | -                     | 2.2.1 | The application can use the storage with unlimited size with the [File API: Directories and System](../api/latest/w3c_api/w3c_api_m.html#directory), [File API: Writer](../api/latest/w3c_api/w3c_api_m.html#writer), [Indexed Database](../api/latest/w3c_api/w3c_api_m.html#database), and [Web SQL Database](../api/latest/w3c_api/w3c_api_m.html#sql) APIs.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br> - In the remote domain, pop-up user prompt is used. |
| `http://tizen.org/privilege/notification` | public | -                     | 2.2.1 | The application can display simple notifications using the [Web Notifications](../api/latest/w3c_api/w3c_api_m.html#webnoti) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br> - In the remote domain, pop-up user prompt is used. |
| `http://tizen.org/privilege/location`    | public | Location              | 2.2.1 | The application can access geographic locations using the [Geolocation](../api/latest/w3c_api/w3c_api_m.html#geo) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |

**Table: Mobile Web Supplementary API privileges**

| Privilege                               | Level  | Since | Description                              |
| --------------------------------------- | ------ | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/fullscreen` | public | 2.2.1 | The application can display in the full-screen mode using the [FullScreen API - Mozilla](../api/latest/w3c_api/w3c_api_m.html#fullscreen) API.<br>**Privilege behavior:**<br> - If this privilege is defined, permission is granted without user interaction. Otherwise, permission is granted by user interaction. |


<a name="wearable"></a>
## Wearable Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in wearable Web applications.

**Table: Wearable Web Device API privileges**

| Privilege                                | Level    | Privacy      | Since | Description                              |
| ---------------------------------------- | -------- | ------------ | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/account.read` | public   | Account      | 4.0   | The application can read accounts.       |
| `http://tizen.org/privilege/account.write` | public   | Account      | 4.0   | The application can create, edit, and delete accounts. |
| `http://tizen.org/privilege/alarm`       | public   | -            | 2.2.1 | The application can set alarms and wake up the device at scheduled times. |
| `http://tizen.org/privilege/apphistory.read` | public   | User history | 4.0   | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/application.info` | public   | -            | 2.2.1 | The application can retrieve information related to other applications. |
| `http://tizen.org/privilege/application.launch` | public   | -            | 2.2.1 | The application can open other applications using the application ID or application control. |
| `http://tizen.org/privilege/appmanager.certificate` | partner  | -            | 2.2.1 | The application can retrieve specified application certificates. |
| `http://tizen.org/privilege/appmanager.kill` | partner  | -            | 2.2.1 | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.launch` | public   | -            | 4.0   | The application can open other applications. |
| `http://tizen.org/privilege/bluetooth`   | public   | -            | 3.0   | The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices. |
| `http://tizen.org/privilege/bluetoothmanager` | platform | -            | 2.3.1 | The application can change Bluetooth system settings related to privacy and security, such as the visibility mode. |
| `http://tizen.org/privilege/calendar.read` | public   | Calendar     | 4.0   | The application can read events and tasks. |
| `http://tizen.org/privilege/calendar.write` | public   | Calendar     | 4.0   | The application can create, update, and delete events and tasks. |
| `http://tizen.org/privilege/call`        | public   | Call         | 2.2.1 | The application can make phone calls to numbers when they are tapped without further confirmation. |
| `http://tizen.org/privilege/contact.read` | public   | Contacts     | 4.0   | The application can read your profile, contacts, and contact history.<br> Contact history can include social network activity. |
| `http://tizen.org/privilege/contact.write` | public   | Contacts     | 4.0   | The application can create, update, and delete your profile, contacts, and any contact history that is related to this application.<br> Contact history can include social network activity. |
| `http://tizen.org/privilege/content.read` | public   | -            | 2.2.1 | The application can read media content information. |
| `http://tizen.org/privilege/content.write` | public   | -            | 2.2.1 | The application can create, update, and delete media content information. |
| `http://tizen.org/privilege/datacontrol.consumer` | public   | -            | 2.3.2 | The application can read data exported by data control providers. |
| `http://tizen.org/privilege/datasharing` | public   | -            | 4.0   | The application can share data with other applications. |
| `http://tizen.org/privilege/download`    | public   | -            | 2.2.1 | The application can manage HTTP downloads. |
| `http://tizen.org/privilege/filesystem.read` | public   | -            | 2.2.1 | The application can read file systems.   |
| `http://tizen.org/privilege/filesystem.write` | public   | -            | 2.2.1 | The application can write to file systems. |
| `http://tizen.org/privilege/healthinfo`  | public   | Sensor       | 2.2.1 | The application can read the user's health information gathered by device sensors, such as pedometer or heart rate monitor. |
| `http://tizen.org/privilege/ime`         | public   | -            | 3.0   | The application can provide users with a way to enter characters and symbols into an associated text field. |
| `http://tizen.org/privilege/led`         | public   | -            | 3.0   | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/location`    | public   | Location     | 2.2.1 | The application can read the user's location information. |
| `http://tizen.org/privilege/mediacontroller.client` | public   | -            | 3.0   | The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely. |
| `http://tizen.org/privilege/mediacontroller.server` | public   | -            | 3.0   | The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications. |
| `http://tizen.org/privilege/nfc.admin`   | public   | -            | 2.3.1 | The application can change NFC settings, such as switching NFC on or off. |
| `http://tizen.org/privilege/nfc.cardemulation` | public   | -            | 2.3.1 | The application can access smart card details, such as credit card details, and allow users to make payments through NFC. |
| `http://tizen.org/privilege/nfc.common`  | public   | -            | 2.3.1 | The application can use common NFC features. |
| `http://tizen.org/privilege/nfc.p2p`     | public   | -            | 2.3.1 | The application can push NFC messages to other devices. |
| `http://tizen.org/privilege/nfc.tag`     | public   | -            | 2.3.1 | The application can read and write NFC tag information. |
| `http://tizen.org/privilege/notification` | public   | -            | 2.2.1 | The application can show and hide its own notifications and badges. |
| `http://tizen.org/privilege/package.info` | public   | -            | 2.2.1 | The application can retrieve information about installed packages. |
| `http://tizen.org/privilege/packagemanager.install` | platform | -            | 2.2.1 | The application can install or uninstall application packages. |
| `http://tizen.org/privilege/power`       | public   | -            | 2.2.1 | The application can control power-related settings, such as dimming the screen. |
| `http://tizen.org/privilege/push`        | public   | -            | 2.2.1 | The application can receive notifications from the Internet. |
| `http://tizen.org/privilege/recorder`    | public   | Microphone   | 4.0   | The application can record video and audio. |
| `http://tizen.org/privilege/secureelement` | public   | -            | 2.3.1 | The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards. |
| `http://tizen.org/privilege/setting`     | public   | -            | 2.2.1 | The application can change and read user settings. |
| `http://tizen.org/privilege/system`      | public   | -            | 2.2.1 | The application can read system information. |
| `http://tizen.org/privilege/tee.client`  | partner  | -            | 4.0   | The application can communicate with a Trusted Application. |
| `http://tizen.org/privilege/telephony`   | public   | -            | 2.3.1 | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/volume.set`  | public   | -            | 2.2.1 | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |
| `http://tizen.org/privilege/widget.viewer` | public   | -            | 2.3.2 | The application can show widgets, and information from their associated applications, on the home screen. |

**Table: Wearable Web W3C/HTML5 API privileges**

| Privilege                                | Level  | Privacy               | Since | Description                              |
| ---------------------------------------- | ------ | --------------------- | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/internet`    | public | -                     | 2.2.1 | The application can access the Internet using the [WebSocket](../api/latest/w3c_api/w3c_api_w.html#websocket), [XMLHttpRequest](../api/latest/w3c_api/w3c_api_w.html#httpreq), and [Cross-Origin Resource Sharing](../api/latest/w3c_api/w3c_api_w.html#cross) APIs. |
| `http://tizen.org/privilege/mediacapture` | public | Camera and Microphone | 2.2.1 | The application can manipulate streams from cameras and microphones using the [getUserMedia](../api/latest/w3c_api/w3c_api_w.html#getusermedia) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |
| `http://tizen.org/privilege/unlimitedstorage` | public | -                     | 2.2.1 | The application can use the storage with unlimited size with the [Indexed Database](../api/latest/w3c_api/w3c_api_w.html#database) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br> - In the remote domain, pop-up user prompt is used. |
| `http://tizen.org/privilege/location`    | public | Location              | 2.2.1 | The application can access geographic locations using the [Geolocation](../api/latest/w3c_api/w3c_api_w.html#geo) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked. |

**Table: Wearable Web Supplementary API privileges**

| Privilege                                | Level  | Privacy               | Since | Description                              |
| ---------------------------------------- | ------ | --------------------- | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/camera`      | public | Camera and Microphone | 2.2.1 | The application can capture video and image on a target device using the [Camera API (Tizen Extension)](../api/latest/w3c_api/w3c_api_w.html#camera) (Video Recording and Image Capture) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, execution is blocked. |
| `http://tizen.org/privilege/audiorecorder` | public | Microphone            | 2.2.1 | The application can record an audio stream on a target device using the [Camera API (Tizen Extension)](../api/latest/w3c_api/w3c_api_w.html#camera) (Audio Recording) API.<br>**Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br> - In the remote domain, execution is blocked. |


<a name="tv"></a>
## TV Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in TV Web applications.

**Table: TV Web Device API privileges**

| Privilege                                | Level    | Since | Description                              |
| ---------------------------------------- | -------- | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/alarm`       | public   | 3.0   | The application can retrieve saved alarms and wake up the device at scheduled times. |
| `http://tizen.org/privilege/apphistory.read` | public   | 4.0   | The application can read the statistics of application usage, such as which applications have been used frequently or recently. |
| `http://tizen.org/privilege/application.info` | public   | 3.0   | The application can retrieve information related to other applications. |
| `http://tizen.org/privilege/application.launch` | public   | 3.0   | The application can open other applications using the application ID or application control. |
| `http://tizen.org/privilege/appmanager.certificate` | partner  | 3.0   | The application can retrieve specified application certificates. |
| `http://tizen.org/privilege/appmanager.kill` | partner  | 3.0   | The application can close other applications. |
| `http://tizen.org/privilege/appmanager.launch` | public   | 4.0   | The application can open other applications. |
| `http://tizen.org/privilege/content.read` | public   | 3.0   | The application can read media content information. |
| `http://tizen.org/privilege/content.write` | public   | 3.0   | The application can change media information. This information can be used by other applications. |
| `http://tizen.org/privilege/datacontrol.consumer` | public   | 3.0   | The application can read data exported by data control providers. |
| `http://tizen.org/privilege/datasharing` | public   | 4.0   | The application can share data with other applications. |
| `http://tizen.org/privilege/download`    | public   | 3.0   | The application can manage HTTP downloads. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/filesystem.read` | public   | 3.0   | The application can read file systems.   |
| `http://tizen.org/privilege/filesystem.write` | public   | 3.0   | The application can write to file systems. |
| `http://tizen.org/privilege/internet`    | public   | 3.0   | The application can access the Internet. This may result in additional charges depending on your payment plan. |
| `http://tizen.org/privilege/led`         | public   | 3.0   | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/mediacapture` | public   | 3.0   | The application can capture video and audio data. |
| `http://tizen.org/privilege/package.info` | public   | 3.0   | The application can retrieve information about installed packages. |
| `http://tizen.org/privilege/packagemanager.install` | platform | 3.0   | The application can install or uninstall application packages. |
| `http://tizen.org/privilege/push`        | public   | 3.0   | The application can receive notifications from the Internet. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/recorder`    | public   | 4.0   | The application can record video and audio. |
| `http://tizen.org/privilege/system`      | public   | 3.0   | The application can read system information. |
| `http://tizen.org/privilege/tee.client`  | partner  | 4.0   | The application can communicate with a Trusted Application. |
| `http://tizen.org/privilege/telephony`   | public   | 3.0   | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/tv.audio`    | public   | 3.0   | The application can change the volume, enable and disable the silent mode, detect volume changes, and play beeps. |
| `http://tizen.org/privilege/tv.channel`  | public   | 3.0   | The application can change the TV channel, read information about TV channels and programs, and receive notifications when the TV channel has been changed. |
| `http://tizen.org/privilege/tv.display`  | public   | 3.0   | The application can check whether a device supports 3D and read information about the 3D mode. |
| `http://tizen.org/privilege/tv.inputdevice` | public   | 3.0   | The application can capture the key events of an input device, such as TV remote control, and release key grabbing. |
| `http://tizen.org/privilege/tv.window`   | public   | 3.0   | The application can embed the display of a video source, specify the size, and show or hide the embedded display. |
| `http://tizen.org/privilege/volume.set`  | public   | 3.0   | The application can adjust the volume for different features, such as notification alerts, ringtones, and media. |

**Table: TV Web W3C/HTML5 API privileges**

| Privilege                                | Level  | Since | Description                              |
| ---------------------------------------- | ------ | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/unlimitedstorage` | public | 3.0   | The application can use the storage with unlimited size with the [Indexed Database](../api/latest/w3c_api/w3c_api_tv.html#database) API.<br> **Privilege behavior:**<br> - In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br> - In the remote domain, pop-up user prompt is used. |

**Table: TV Web Supplementary API privileges**

| Privilege                                | Level  | Since | Description                              |
| ---------------------------------------- | ------ | ----- | ---------------------------------------- |
| `http://tizen.org/privilege/fullscreen`  | public   | 3.0   | The application can use the full screen view. |


<a name="nonAPI"></a>
## Non-API Bound Privileges

Tizen application privileges are loosely bound to APIs, so most of the privileges can be identified by the APIs that the application calls. However, there are some privileges that are not coupled with the Tizen APIs. To allow easy identification, those privileges are mapped to corresponding system resources - same as other privileges.

The following table lists the non-API bound privileges.

**Table: Non-API bound privileges**

| Privilege      | Level          | Privacy        | Since          | Description    |
|---------------|---------------|-----------------|----------------|-----------------|
| `http://tizen.org/privilege/mediastorage` | public | Storage | 4.0 | When you connect the device to a computer (Windows&reg; or macOS) through USB, you can access a dedicated media storage area shown as massive media storage. This region of the storage is called media storage and is usually used for multimedia files, such as photos, videos, and music files. Since this storage area is used for user private data, access to it must be protected with a privilege.<br> If your application does not have this privilege, no file operations into the media storage area succeed and you receive a permission denied error. If you have this privilege, you can read and write directories and files, create new files, and delete files in the storage area.      |
| `http://tizen.org/privilege/externalstorage` | public | Storage | 4.0 | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br> If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to the external storage. |
