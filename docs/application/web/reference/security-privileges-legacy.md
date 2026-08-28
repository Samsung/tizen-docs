# Security and API Privileges for Apps with API Version 4.0 or Earlier

The API version restriction of privileges are deprecated since 5.0. This page provides privilege information with its supported version for developing apps with API version 4.0 or less.


<a name="tv"></a>
## TV Web API privileges

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
| `http://tizen.org/privilege/keymanager` | public | 2.4 | The application can save keys, certificates, and data to, and retrieve and delete them from, password-protected storage. Checking the statuses of certificates while connected to a mobile network may result in additional charges depending on user's payment plan. Deprecated since 3.0. |
| `http://tizen.org/privilege/led`         | public   | 3.0   | The application can switch LEDs on or off, such as the LED on the front of the device and the camera flash. |
| `http://tizen.org/privilege/mediacapture` | public   | 3.0   | The application can capture video and audio data. |
| `http://tizen.org/privilege/package.info` | public   | 3.0   | The application can retrieve information about installed packages. |
| `http://tizen.org/privilege/packagemanager.install` | platform | 3.0   | The application can install or uninstall application packages. |
| `http://tizen.org/privilege/push`        | public   | 3.0   | The application can receive notifications from the Internet. This can result in additional charges depending on the user's payment plan. |
| `http://tizen.org/privilege/recorder`    | public   | 4.0   | The application can record video and audio. |
| `http://tizen.org/privilege/system`      | public   | 3.0   | The application can read system information. |
| `http://tizen.org/privilege/systemmanager` | partner | 2.3 | The application can read secure system information. Deprecated since 2.4. |
| `http://tizen.org/privilege/tee.client`  | partner  | 4.0   | The application can communicate with a Trusted Application. |
| `http://tizen.org/privilege/telephony`   | public   | 3.0   | The application can retrieve telephony information, such as the network and SIM card used, the IMEI, and the status of calls. |
| `http://tizen.org/privilege/tv.audio`    | public   | 3.0   | The application can change the volume, enable and disable the silent mode, detect volume changes, and play beeps. |
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
## Non-API bound privileges

Tizen application privileges are loosely bound to APIs, so most of the privileges can be identified by the APIs that the application calls. However, there are some privileges that are not coupled with the Tizen APIs. To allow easy identification, those privileges are mapped to corresponding system resources that are similar to other privileges.

The following table lists the non-API bound privileges:

**Table: Non-API bound privileges**

| Privilege      | Level          | Privacy        | Since          | Description    |
|---------------|---------------|-----------------|----------------|-----------------|
| `http://tizen.org/privilege/mediastorage` | public | Storage | 4.0 | When you connect the device to a computer (Windows&reg; or macOS) through USB, you can access a dedicated media storage area shown as massive media storage. This region of the storage is called media storage and is usually used for multimedia files, such as photos, videos, and music files. Since this storage area is used for user private data, access to it must be protected with a privilege.<br> If your application does not have this privilege, no file operations into the media storage area succeed and you receive a permission denied error. If you have this privilege, you can read and write directories and files, create new files, and delete files in the storage area.      |
| `http://tizen.org/privilege/externalstorage` | public | Storage | 4.0 | Similar to the media storage, many devices support external storages, such as MicroSD card or USB memory. As with the media storage, the access to an external storage must be protected with a privilege.<br> If your application does not have this privilege, all file operations fail with a permission denied error. If you have this privilege, you have full access to the external storage. |
