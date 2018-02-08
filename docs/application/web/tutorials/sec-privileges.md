
# Security and API Privileges

To effectively protect the device system and user private data, the Tizen security architecture is based on privileges and application signing of the Linux basic security model, which includes process isolation and mandatory access control. Since Tizen, as an open platform, provides a wide range of features and experiences for users with a variety of applications, the users must be able to grant privileges for security-sensitive operations.

Tizen provides API-level access control for security-sensitive operations which, if not used correctly, can harm user privacy and system stability. Therefore, applications that use such sensitive APIs must declare the required privileges in the [config.xml](../process/setting-properties.md#privilege) file.  Privileges are categorized into public, partner, and platform levels according to their hierarchy:

-   The public level is the minimum privilege level, which means that any application developed using the Tizen Studio can use these privileges.
-   The partner level privileges require at least a partner-signed certificate which is granted to developers who have a business relationship with the vendor.
-   The platform level is the highest privilege level, and an application that needs these privileges requires at least a  platform-signed certificate, which is granted to vendor developers.

Since Tizen platform 3.0, some privileges are categorized as privacy-related and give an option to the user to switch them on and off. If an application invokes a privacy-related privileged API, the Tizen system checks whether the privilege is **allowed** for the application. For the application to use the API, the privilege must be declared in the `config.xml` file and the user must have switched it on.


> **Note**  
> In applications with the platform version 3.0 or higher, if you use privacy-related privileged APIs, make sure that the user has switched the privilege on before making the function call. Otherwise, the application does not work as expected.
>
> Since Tizen 4.0, the status of privacy-related privileges can be [resolved at runtime](../../guides/security/ppm.md) using the Privacy Privilege API (in [mobile](../../../../org.tizen.web.apireference/html/device_api/mobile/tizen/ppm.html) and [wearable](../../../../org.tizen.web.apireference/html/device_api/wearable/tizen/ppm.html) applications).

The Tizen Studio also provides privilege checker tools to check whether the Tizen application source code contains any privilege violations. For more information, see [Verifying Privilege Usage](../../../tizen-studio/web-tools/privilege-checker.md).

<a name="mobile"></a>
## Mobile Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in mobile Web applications.

**Table: Mobile Web Device API privileges**
<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Privacy</th>
<th>Since</th>
<th>Description</th>
</tr>
<tr>

<td>

`http://tizen.org/privilege/account.read`
</td>
<td>public</td>
<td>Account</td>
<td>2.3</td>
<td>

The application can read accounts.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/account.write`
</td>
<td>public</td>
<td>Account</td>
<td>2.3</td>
<td>

The application can create, edit, and delete accounts.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/alarm`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can manage alarms by retrieving saved alarms and waking the device up at scheduled times.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/application.info`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve information related to other applications.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/application.launch`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can open other applications using the application ID or application control.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/appmanager.certificate`
</td>
<td>partner</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve specified application certificates.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/appmanager.kill`
</td>
<td>partner</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can close other applications.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/bluetooth`
</td>
<td>public</td>
<td>-</td>
<td>2.4</td>
<td>

The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/bluetoothmanager`
</td>
<td>platform</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can change Bluetooth system settings related to privacy and security, such as the visibility mode.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/bookmark.read`
</td>
<td>platform</td>
<td>Bookmark</td>
<td>2.2.1</td>
<td>

The application can read bookmarks.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/bookmark.write`
</td>
<td>platform</td>
<td>Bookmark</td>
<td>2.2.1</td>
<td>

The application can create, edit, and delete bookmarks.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/calendar.read`
</td>
<td>public</td>
<td>Calendar</td>
<td>2.2.1</td>
<td>

The application can read events and tasks.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/calendar.write`
</td>
<td>public</td>
<td>Calendar</td>
<td>2.2.1</td>
<td>

The application can create, update, and delete events and tasks.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/call`
</td>
<td>public</td>
<td>Call</td>
<td>2.3</td>
<td>

The application can make phone calls to numbers when they are tapped without further confirmation. This can result in additional charges depending on the user's payment plan.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/callhistory.read`
</td>
<td>public</td>
<td>Contacts and User history</td>
<td>2.2.1</td>
<td>

The application can read call log items.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/callhistory.write`
</td>
<td>public</td>
<td>Contacts and User history</td>
<td>2.2.1</td>
<td>

The application can create, update, and delete call log items.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/contact.read`
</td>
<td>public</td>
<td>Contacts</td>
<td>2.2.1</td>
<td>

The application can read the user profile, contacts, and contact history. Contact history can include social network activity.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/contact.write`
</td>
<td>public</td>
<td>Contacts</td>
<td>2.2.1</td>
<td>

The application can create, update, and delete the user profile, contacts, and any contact history that is related to this application. Contact history can include social network activity.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/content.read`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read media content information.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/content.write`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can create, update, and delete media content information.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/datacontrol.consumer`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read data exported by data control providers.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/datasync`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can synchronize device data, such as contacts and calendar events, using the OMA DS 1.2 protocol.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/download`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can manage HTTP downloads.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/filesystem.read`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read file systems.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/filesystem.write`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can write to file systems.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/healthinfo`
</td>
<td>public</td>
<td>Sensor</td>
<td>2.3</td>
<td>

The application can read the user's health information gathered by device sensors, such as pedometer or heart rate monitor.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/ime`
</td>
<td>public</td>
<td>-</td>
<td>2.4</td>
<td>

The application can provide users with a way to enter characters and symbols into an associated text field.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/led`
</td>
<td>public</td>
<td>-</td>
<td>2.4</td>
<td>

The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/location`
</td>
<td>public</td>
<td>Location</td>
<td>2.2.1</td>
<td>

The application can read the user's location information.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/mediacontroller.client`
</td>
<td>public</td>
<td>-</td>
<td>2.4</td>
<td>

The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/mediacontroller.server`
</td>
<td>public</td>
<td>-</td>
<td>2.4</td>
<td>

The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/messaging.read`
</td>
<td>public</td>
<td>Message</td>
<td>2.2.1</td>
<td>

The application can retrieve messages from message boxes or receive messages.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/messaging.write`
</td>
<td>public</td>
<td>Message</td>
<td>2.2.1</td>
<td>

The application can write, send, sync, and remove text messages, multimedia messages, and emails.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/networkbearerselection`
</td>
<td>partner</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can request and release a specific network connection.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/nfc.admin`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can change NFC settings, such as switching NFC on or off.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/nfc.cardemulation`
</td>
<td>public</td>
<td>-</td>
<td>2.3</td>
<td>

The application can access smart card details, such as credit card details, and allow users to make payments through NFC.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/nfc.common`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can use common NFC features.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/nfc.p2p`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can push NFC messages to other devices.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/nfc.tag`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read and write NFC tag information.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/notification`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can show and hide its own notifications and badges.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/package.info`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve information about installed packages.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/packagemanager.install`
</td>
<td>platform</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can install or uninstall application packages.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/power`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can control power-related settings, such as dimming the screen.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/push`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can receive notifications from the Internet.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/secureelement`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/setting`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can change and read user settings.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/system`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read system information.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/tee.client`
</td>
<td>partner</td>
<td>-</td>
<td>4.0</td>
<td>

The application can communicate with a Trusted Application.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/telephony`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/volume.set`
</td>
<td>public</td>
<td>-</td>
<td>2.3</td>
<td>

The application can adjust the volume for different features, such as notification alerts, ringtones, and media.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/websetting`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can change its Web application settings, including deleting cookies. <strong>Deprecated since 2.4.</strong></td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/widget.viewer`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can show widgets, and information from their associated applications, on the home screen.</td>
</tr>

</table>

**Table: Mobile Web W3C/HTML5 API privileges**
<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Privacy</th>
<th>Since</th>
<th>Description</th>
</tr>

<tr>
<td>

`http://tizen.org/privilege/internet`
</td>
<td>public</td>
<td>-</td>
<td>2.3</td>
<td>

The application can access the Internet using the [WebSocket](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#websocket), [XMLHttpRequest](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#httpreq), [Server-Sent Events](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#serversent), [HTML5 Application caches](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#cache), and [Cross-Origin Resource Sharing](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#cross) APIs.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/mediacapture`
</td>
<td>public</td>
<td>Camera and Microphone</td>
<td>2.2.1</td>
<td>

The application can manipulate streams from cameras and microphones using the [getUserMedia](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#getusermedia) API.<br>

**Privilege behavior:**
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.
- In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked.
</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/unlimitedstorage`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can use the storage with unlimited size with the [File API: Directories and System](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#directory), [File API: Writer](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#writer), [Indexed Database](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#database), and [Web SQL Database](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#sql) APIs.<br>

**Privilege behavior:**
- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.
- In the remote domain, pop-up user prompt is used.
</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/notification`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can display simple notifications using the [Web Notifications](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#webnoti) API.<br>

**Privilege behavior:**
- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.
- In the remote domain, pop-up user prompt is used.
</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/location`
</td>
<td>public</td>
<td>Location</td>
<td>2.2.1</td>
<td>

The application can access geographic locations using the [Geolocation](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#geo) API.<br>

**Privilege behavior:**
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.
- In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked.
</td>
</tr>
</table>

**Table: Mobile Web Supplementary API privileges**
<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Since</th>
<th>Description</th>
</tr>

<tr>
<td>

`http://tizen.org/privilege/fullscreen` </td>
<td>public</td>
<td>2.2.1</td>
<td>
The application can display in the full-screen mode using the [FullScreen API - Mozilla](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_m.html#fullscreen) API.<br>

**Privilege behavior:**
- If this privilege is defined, permission is granted without user interaction. Otherwise, permission is granted by user interaction.
</td>
</tr>
</table>

<a name="wearable"></a>
## Wearable Web API Privileges

The following tables list the API privileges, which you must declare when using security-sensitive API modules in wearable Web applications.

**Table: Wearable Web Device API privileges**

<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Privacy</th>
<th>Since</th>
<th>Description</th>
</tr>

<tr>
<td>

`http://tizen.org/privilege/alarm`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can set alarms and wake up the device at scheduled times.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/application.info`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve information related to other applications.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/application.launch`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can open other applications using the application ID or application control.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/appmanager.certificate`
</td>
<td>partner</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve specified application certificates.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/appmanager.kill`
</td>
<td>partner</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can close other applications.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/bluetooth`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can perform unrestricted actions using Bluetooth, such as scanning for and connecting to other devices.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/bluetoothmanager`
</td>
<td>platform</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can change Bluetooth system settings related to privacy and security, such as the visibility mode.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/call`
</td>
<td>public</td>
<td>Call</td>
<td>2.2.1</td>
<td>

The application can make phone calls to numbers when they are tapped without further confirmation.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/content.read`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read media content information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/content.write`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can create, update, and delete media content information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/datacontrol.consumer`
</td>
<td>public</td>
<td>-</td>
<td>2.3.2</td>
<td>

The application can read data exported by data control providers.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/download`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can manage HTTP downloads.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/filesystem.read`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read file systems.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/filesystem.write`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can write to file systems.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/healthinfo`
</td>
<td>public</td>
<td>Sensor</td>
<td>2.2.1</td>
<td>

The application can read the user's health information gathered by device sensors, such as pedometer or heart rate monitor.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/ime`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can provide users with a way to enter characters and symbols into an associated text field.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/led`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/location`
</td>
<td>public</td>
<td>Location</td>
<td>2.2.1</td>
<td>

The application can read the user's location information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/mediacontroller.client`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can receive information about currently playing media from applications that are allowed to send it, and can control those applications remotely.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/mediacontroller.server`
</td>
<td>public</td>
<td>-</td>
<td>3.0</td>
<td>

The application can send information about currently playing media to applications that are allowed to receive it, and can be controlled remotely by those applications.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/nfc.admin`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can change NFC settings, such as switching NFC on or off.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/nfc.cardemulation`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can access smart card details, such as credit card details, and allow users to make payments through NFC.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/nfc.common`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can use common NFC features.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/nfc.p2p`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can push NFC messages to other devices.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/nfc.tag`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can read and write NFC tag information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/notification`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can show and hide its own notifications and badges.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/package.info`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can retrieve information about installed packages.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/packagemanager.install`
</td>
<td>platform</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can install or uninstall application packages.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/power`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can control power-related settings, such as dimming the screen.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/push`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can receive notifications from the Internet.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/secureelement`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can access secure smart card chips, such as UICC/SIM, embedded secure elements, and secure SD cards.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/setting`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can change and read user settings.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/system`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can read system information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tee.client`
</td>
<td>partner</td>
<td>-</td>
<td>4.0</td>
<td>

The application can communicate with a Trusted Application.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/telephony`
</td>
<td>public</td>
<td>-</td>
<td>2.3.1</td>
<td>

The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/volume.set`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can adjust the volume for different features, such as notification alerts, ringtones, and media.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/widget.viewer`
</td>
<td>public</td>
<td>-</td>
<td>2.3.2</td>
<td>

The application can show widgets, and information from their associated applications, on the home screen.</td>
</tr>
</table>

**Table: Wearable Web W3C/HTML5 API privileges**
<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Privacy</th>
<th>Since</th>
<th>Description</th>
</tr>
<tr>

<td>

`http://tizen.org/privilege/internet`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can access the Internet using the [WebSocket](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#websocket), [XMLHttpRequest](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#httpreq), and [Cross-Origin Resource Sharing](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#cross) APIs.</td>
</tr>
<tr>
<td>

`http://tizen.org/privilege/mediacapture`
</td>
<td>public</td>
<td>Camera and Microphone</td>
<td>2.2.1</td>
<td>

The application can manipulate streams from cameras and microphones using the [getUserMedia](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#getusermedia) API.<br>

**Privilege behavior:**
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.
- In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked.
</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/unlimitedstorage`
</td>
<td>public</td>
<td>-</td>
<td>2.2.1</td>
<td>

The application can use the storage with unlimited size with the [Indexed Database](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#database) API.<br>

**Privilege behavior:**<br>
- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br>
- In the remote domain, pop-up user prompt is used.
</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/location`
</td>
<td>public</td>
<td>Location</td>
<td>2.2.1</td>
<td>

The application can access geographic locations using the [Geolocation](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#geo) API.<br>

**Privilege behavior:**<br>
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>
- In the remote domain, if this privilege is defined, pop-up user prompt is used. Otherwise, execution is blocked.
</td>
</tr>
</table>

**Table: Wearable Web Supplementary API privileges**

<table>
<th>Privilege</th>
<th>Level</th>
<th>Privacy</th>
<th>Since</th>
<th>Description</th>

<tr>
<td>

`http://tizen.org/privilege/camera`
</td>
<td>public</td>
<td>Camera and Microphone</td>
<td>2.2.1</td>
<td>

The application can capture video and image on a target device using the [Camera API (Tizen Extension)](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#camera) (Video Recording and Image Capture) API.<br>

**Privilege behavior:**<br>
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>
- In the remote domain, execution is blocked. |
</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/audiorecorder`
</td>
<td>public</td>
<td>Microphone</td>
<td>2.2.1</td>
<td>

The application can record an audio stream on a target device using the [Camera API (Tizen Extension)](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_w.html#camera) (Audio Recording) API.<br>

**Privilege behavior:**<br>
- In the local domain, if this privilege is defined, permission is granted. Otherwise, execution is blocked.<br>
- In the remote domain, execution is blocked.|
</td>
</tr>
</table>

<a name="tv"></a>
## TV Web API Privileges

The following tables list the API privileges, which you must declare
when using security-sensitive API modules in TV Web applications.

**Table: TV Web Device API privileges**

<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Since</th>
<th>Description</th>
</tr>
<tr>

<td>

`http://tizen.org/privilege/alarm`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can retrieve saved alarms and wake up the device at scheduled times.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/application.info`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can retrieve information related to other applications.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/application.launch`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can open other applications using the application ID or application control.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/appmanager.certificate`
</td>
<td>partner</td>
<td>3.0</td>
<td>

The application can retrieve specified application certificates.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/appmanager.kill`
</td>
<td>partner</td>
<td>3.0</td>
<td>

The application can close other applications.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/content.read`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can read media content information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/content.write`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can change media information. This information can be used by other applications.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/datacontrol.consumer`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can read data exported by data control providers.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/download`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can manage HTTP downloads. This can result in additional charges depending on the user's payment plan.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/filesystem.read`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can read file systems.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/filesystem.write`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can write to file systems.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/fullscreen`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can use the full screen view.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/keymanager`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can save keys, certificates, and data to, and retrieve and delete them from, a password-protected storage. Chdking the status of certificates while connected to a mobile network can result in additional charges depending on the user's payment plan.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/led`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/package.info`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can retrieve information about installed packages.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/packagemanager.install`
</td>
<td>platform</td>
<td>3.0</td>
<td>

The application can install or uninstall application packages.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/push`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can receive notifications from the Internet. This can result in additional charges depending on the user's payment plan.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/system`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can read system information.</td>
</tr>

<tr>

<td>

`http://tizen.org/privilege/systemmanager`
</td>
<td>partner</td>
<td>3.0</td>
<td>

The application can read secure system information.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tee.client`
</td>
<td>partner</td>
<td>4.0</td>
<td>

The application can communicate with a Trusted Application.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/telephony`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tv.audio`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can change the volume, enable and disable the silent mode, detect volume changes, and play beeps.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tv.channel`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can change the TV channel, read information about TV channels and programs, and receive notifications when the TV channel has been changed.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tv.display`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can check whether a device supports 3D and read information about the 3D mode.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tv.inputdevice`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can capture the key events of an input device, such as TV remote control, and release key grabbing.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/tv.window`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can embed the display of a video source, specify the size, and show or hide the embedded display.</td>
</tr>
<tr>

<td>

`http://tizen.org/privilege/volume.set`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can adjust the volume for different features, such as notification alerts, ringtones, and media.</td>
</tr>

<tr>
<td>

`http://tizen.org/privilege/websetting`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can change its Web application settings, including deleting cookies.</td>
</tr>
</table>

**Table: TV Web W3C/HTML5 API privileges**

<table>
<tr>
<th>Privilege</th>
<th>Level</th>
<th>Since</th>
<th>Description</th>
</tr>
<tr>
<td>

`http://tizen.org/privilege/unlimitedstorage`
</td>
<td>public</td>
<td>3.0</td>
<td>

The application can use the storage with unlimited size with the [Indexed Database](https://developer.tizen.org/dev-guide/latest/org.tizen.web.apireference/html/w3c_api/w3c_api_tv.html#database) API.<br>

**Privilege behavior:**<br>
- In the local domain, if this privilege is defined, permission is granted. Otherwise, pop-up user prompt is used.<br>
- In the remote domain, pop-up user prompt is used.
</td>
</tr>
</table>

<a name="nonAPI"></a>
## Non-API Bound Privileges

Tizen application privileges are loosely bound to APIs, so most of the privileges can be identified by the APIs that the application calls. However, there are some privileges that are not coupled with the Tizen APIs. To allow easy identification, those privileges are mapped to corresponding system resources - same as other privileges.

The following table lists the non-API bound privileges.

**Table: Non-API bound privileges**

| Privilege      | Level          | Privacy        | Since          | Description    |
|---------------|---------------|-----------------|----------------|-----------------|
| `http://tizen.org/privilege/mediastorage` | public | Storage | 4.0 | When you connect the device to a computer  (Windows&reg; or   macOS) through USB, you can   access a       dedicated     media storage  area shown as  massive media   storage. This   region of the  storage is     called media   storage and is  usually used   for multimedia  files, such as  photos,      videos, and   music files.  Since this    storage area    is used for   user private   data, access to it must be  protected with  a privilege.<br>  If your       application    does not have   this          privilege, no   file         operations      into the media storage area   succeed and     you receive a  permission      denied error. If you have     this           privilege, you  can read and   write         directories   and files,  create new   files, and    delete files   in the storage area.      |
| `http://tizen.org/privilege/externalstorage` | public | Storage | 4.0 | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br> If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to the external storage. |
