

Tizen APIs
==========

Using the Tizen Web API modules, you can develop rich Web applications
and build great application experiences with well-known Web programming
languages: HTML, CSS, and JavaScript. Like every major browser in the
market, the Tizen Web API modules support the latest HTML5 capabilities,
such as animation, offline, audio, and video. By utilizing the standard
HTML5 capabilities, your Web applications are ready to run across
various devices and platforms with minimal customization. In addition to
the JavaScript-based Tizen Device API, you can also enable advanced
device access from your Web applications, such as Bluetooth and NFC.

The Tizen platform supports hybrid applications (1 Web application and 1
or more native applications). A hybrid application package is very
useful for Web applications that need background processing or
monitoring. With a hybrid application package, you can register the
included applications in the Tizen Store and install, update, and
uninstall them using a single hybrid package. For more information on
developing hybrid Web applications with Tizen devices, see [Packaging
Hybrid Applications](../process/app-dev-process-w.md#hybrid).

Tizen provides a wide range of Web API modules that allow you to take
full advantage of various Tizen features.

The following table lists the features provided by the [Mobile Web
Device API
Reference](../../../../org.tizen.web.apireference/html/device_api/mobile/index.html).

**Table: Device API features provided for mobile applications**

+----------------+------------------------------+------------------------------+
| Feature        | Purpose                      | Documentation                |
+================+==============================+==============================+
| Base           | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that provide  |                              |
|                | a set of basic definitions   |     [Data Storage and        |
|                | and interfaces that are used |     Management](../../../gui |
|                | in the Tizen Device API.     |   des/web/data/data-cover-   |
|                | You can manage common files  |   w.md)                      |
|                | and ZIP archive files, and   |                              |
|                | define filters and sorting   |     [Error                   |
|                | modes for queries. You can   |     Handling](../../../guide |
|                | also use generic success and |   s/web/error/error-w.md)    |
|                | error event handlers, in     |                              |
|                | addition to a generic error  |                              |
|                | interface and a simple       | -   API Reference:           |
|                | coordinate interface for     |     [Base](../../../../org.t |
|                | defining location            | izen.web.apireference/html/d |
|                | information.                 | evice_api/mobile/index.html# |
|                |                              | Base)                        |
+----------------+------------------------------+------------------------------+
| Account        | This API contains classes    | -   Guides: [Personal        |
|                | and interfaces that enable   |     Data](../../../guides/we |
|                | you to manage account        | b/personal/personal-cover-w. |
|                | features.                    | md)                          |
|                | You can use existing         | -   API Reference:           |
|                | configured on-line accounts  |     [Account](../../../../or |
|                | and providers, and create    | g.tizen.web.apireference/htm |
|                | new accounts of known types. | l/device_api/mobile/index.ht |
|                |                              | ml#Account)                  |
+----------------+------------------------------+------------------------------+
| Application    | These APIs contain classes   | -   Guides:                  |
| Framework      | and interfaces that enable   |                              |
|                | you to manage alarm,         |     [Alarms](../../../guides |
|                | application, and package     | /web/alarm/alarms-w.md)      |
|                | features.                    |                              |
|                | You can schedule an          |                              |
|                | application to be run at a   |     [Application             |
|                | specific time, retrieve      |     Management](../../../gui |
|                | information about the        | des/web/app-management/app-m |
|                | applications installed or    | anagement-cover-w.md)        |
|                | running on the device, and   |                              |
|                | enable package management.   |                              |
|                |                              |     [Notifications](../../.. |
|                |                              | /guides/web/notification/not |
|                |                              | ification-w.md)              |
|                |                              |                              |
|                |                              |                              |
|                |                              |     [Text                    |
|                |                              |     Input](../../../guides/w |
|                |                              | eb/text-input/text-input-cov |
|                |                              | er-w.md)                     |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Application             |
|                |                              |     Framework](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/device_api/mobile/index.h |
|                |                              | tml#Application)             |
+----------------+------------------------------+------------------------------+
| Content        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |                              |
|                | you to manage content and    |     [Connectivity and        |
|                | download features.           |     Wireless](../../../guide |
|                | You can search and manage    | s/web/connectivity/connectiv |
|                | multimedia content locally,  | ity-cover-w.md)              |
|                | download files from the      |                              |
|                | Internet, and monitor the    |                              |
|                | download progress and        |     [Data Storage and        |
|                | status.                      |     Management](../../../gui |
|                |                              | des/web/data/data-cover-w.md |
|                |                              | )                            |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Content](../../../../or |
|                |                              | g.tizen.web.apireference/htm |
|                |                              | l/device_api/mobile/index.ht |
|                |                              | ml#Contents)                 |
+----------------+------------------------------+------------------------------+
| Messaging      | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |     [Messaging](../../../gui |
|                | you to manage SMS, MMS, and  | des/web/messaging/messaging- |
|                | email messages.              | cover-w.md)                  |
|                | You can send and receive     |                              |
|                | messages, and receive push   | -   API Reference:           |
|                | notifications from a push    |     [Messaging](../../../../ |
|                | server.                      | org.tizen.web.apireference/h |
|                |                              | tml/device_api/mobile/index. |
|                |                              | html#Messaging)              |
+----------------+------------------------------+------------------------------+
| Multimedia     | These APIs contain classes   | -   Guides: [Media and       |
|                | and interfaces that enable   |     Camera](../../../guides/ |
|                | you to manage                | web/media/media-cover-w.md)  |
|                | multimedia-related features. |                              |
|                | You can change and monitor   | -   API Reference:           |
|                | playback volume level, and   |     [Multimedia](../../../.. |
|                | listen to the FM radio.      | /org.tizen.web.apireference/ |
|                |                              | html/device_api/mobile/index |
|                |                              | .html#Multimedia)            |
+----------------+------------------------------+------------------------------+
| Network        | These APIs contain classes   | -   Guides: [Connectivity    |
|                | and interfaces that enable   |     and                      |
|                | you to manage Bluetooth, NFC |     Wireless](../../../guide |
|                | (Near Field Communication),  | s/web/connectivity/connectiv |
|                | and secure element features. | ity-cover-w.md)              |
|                | You can transfer data over a |                              |
|                | Bluetooth connection, share  | -   API Reference:           |
|                | contacts, photos, and videos |     [Network](../../../../or |
|                | using NFC, and access secure | g.tizen.web.apireference/htm |
|                | elements, such as SIM card   | l/device_api/mobile/index.ht |
|                | and secure SD card, in a     | ml#Network)                  |
|                | device.                      |                              |
+----------------+------------------------------+------------------------------+
| Security       | This API contains classes    | -   Guides:                  |
|                | and interfaces that enable   |     [Security](../../../guid |
|                | you to manage secure keys in | es/web/security/security-cov |
|                | your application.            | er-w.md)                     |
|                | You can use security         | -   API Reference:           |
|                | functionalities, such as     |     [Security](../../../../o |
|                | storing and recalling        | rg.tizen.web.apireference/ht |
|                | private data.                | ml/device_api/mobile/index.h |
|                |                              | tml#Security)                |
+----------------+------------------------------+------------------------------+
| Social         | These APIs contain classes   | -   Guides: [Personal        |
|                | and interfaces that enable   |     Data](../../../guides/we |
|                | you to manage bookmark,      | b/personal/personal-cover-w. |
|                | calendar, call history,      | md)                          |
|                | contact, and data            | -   API Reference:           |
|                | synchronization features.    |     [Social](../../../../org |
|                | You can manage the Tizen Web | .tizen.web.apireference/html |
|                | browser bookmark list,       | /device_api/mobile/index.htm |
|                | calendar events and tasks,   | l#Social)                    |
|                | call history, and address    |                              |
|                | books and contacts on a      |                              |
|                | device, and you can          |                              |
|                | synchronize device data,     |                              |
|                | such as contacts and         |                              |
|                | calendar events, with the    |                              |
|                | OMA DS server.               |                              |
+----------------+------------------------------+------------------------------+
| System         | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |                              |
|                | you to manage power, system  |     [Device Settings and     |
|                | information and setting,     |     Systems](../../../guides |
|                | time, and Web setting        | /web/device/device-cover-w.m |
|                | features.                    | d)                           |
|                | You can access the state of  |                              |
|                | the device power resource,   |     [Media and               |
|                | device system information,   |     Camera](../../../guides/ |
|                | and device wallpaper         | web/media/media-cover-w.md)  |
|                | settings. You can use        |                              |
|                | locale-specific calendar     |                              |
|                | features by retrieving date  |     [Sensors](../../../guide |
|                | and time information, and    | s/web/sensors/sensors-cover- |
|                | set feedback patterns for    | w.md)                        |
|                | specified actions. You can   |                              |
|                | also manage time features,   | -   API Reference:           |
|                | and set Web view properties, |     [System](../../../../org |
|                | such as setting Web view     | .tizen.web.apireference/html |
|                | user agents and deleting Web | /device_api/mobile/index.htm |
|                | view cookies.                | l#System)                    |
+----------------+------------------------------+------------------------------+
| Cordova        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |     [Cordova](../../../guide |
|                | you use common               | s/web/cordova/cordova-cover- |
|                | functionalities in creating  | w.md)                        |
|                | Tizen Web applications.      | -   API Reference:           |
|                | You can manage the device    |     [Cordova](../../../../or |
|                | filesystem, individual       | g.tizen.web.apireference/htm |
|                | files, and various events,   | l/device_api/mobile/index.ht |
|                | access device and network    | ml#Cordova)                  |
|                | information and the device   |                              |
|                | accelerometer, create dialog |                              |
|                | boxes and system log         |                              |
|                | entries, and play audio      |                              |
|                | files.                       |                              |
+----------------+------------------------------+------------------------------+
| Web UI         | These APIs contain classes   | -   Guides: [Tizen Advanced  |
| Framework      | and interfaces that enable   |     UI](../../../guides/web/ |
|                | you to manage the Tizen      | ui/tau/tau-w.md)             |
|                | Advanced UI (TAU) features.  |                              |
|                | You can create and manage    | -   API Reference: [Advanced |
|                | various kinds of UI          |     UI                       |
|                | components.                  |     Framework](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/ui_fw_api/ui_fw_api_cover |
|                |                              | .htm)                        |
+----------------+------------------------------+------------------------------+

The following table lists the features provided by the [Wearable Web
Device API
Reference](../../../../org.tizen.web.apireference/html/device_api/wearable/index.html).

**Table: Device API features provided for wearable applications**

+----------------+------------------------------+------------------------------+
| Feature        | Purpose                      | Documentation                |
+================+==============================+==============================+
| Base           | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that provide  |                              |
|                | a set of basic definitions   |     [Data Storage and        |
|                | and interfaces that are used |     Management](../../../gui |
|                | in the Tizen Device API.     | des/web/data/data-cover-w.md |
|                | You can manage common files  | )                            |
|                | and ZIP archive files, and   |                              |
|                | define filters and sorting   |     [Error                   |
|                | modes for queries. You can   |     Handling](../../../guide |
|                | also use generic success and | s/web/error/error-w.md)      |
|                | error event handlers, in     |                              |
|                | addition to a generic error  |                              |
|                | interface and a simple       | -   API Reference:           |
|                | coordinate interface for     |     [Base](../../../../org.t |
|                | defining location            | izen.web.apireference/html/d |
|                | information.                 | evice_api/wearable/index.htm |
|                |                              | l#Base)                      |
+----------------+------------------------------+------------------------------+
| Account        | This API contains classes    | -   Guides: [Personal        |
|                | and interfaces that enable   |     Data](../../../guides/we |
|                | you to manage account        | b/personal/personal-cover-w. |
|                | features.                    | md)                          |
|                | You can use existing         | -   API Reference:           |
|                | configured on-line accounts  |     [Account](../../../../or |
|                | and providers, and create    | g.tizen.web.apireference/htm |
|                | new accounts of known types. | l/device_api/wearable/index. |
|                |                              | html#Account)                |
+----------------+------------------------------+------------------------------+
| Application    | These APIs contain classes   | -   Guides:                  |
| Framework      | and interfaces that enable   |                              |
|                | you to manage alarm,         |     [Alarms](../../../guides |
|                | application, and package     | /web/alarm/alarms-w.md)      |
|                | features.                    |                              |
|                | You can schedule an          |                              |
|                | application to be run at a   |     [Application             |
|                | specific time, retrieve      |     Management](../../../gui |
|                | information about the        | des/web/app-management/app-m |
|                | applications installed or    | anagement-cover-w.md)        |
|                | running on the device, and   |                              |
|                | enable package management.   |                              |
|                |                              |     [Notifications](../../.. |
|                |                              | /guides/web/notification/not |
|                |                              | ification-w.md)              |
|                |                              |                              |
|                |                              |                              |
|                |                              |     [Text                    |
|                |                              |     Input](../../../guides/w |
|                |                              | eb/text_input/text-input-cov |
|                |                              | er-w.md)                     |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Application             |
|                |                              |     Framework](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/device_api/wearable/index |
|                |                              | .html#Application)           |
+----------------+------------------------------+------------------------------+
| Content        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |                              |
|                | you to manage content and    |     [Connectivity and        |
|                | download features.           |     Wireless](../../../guide |
|                | You can search and manage    | s/web/connectivity/connectiv |
|                | multimedia content locally,  | ity-cover-w.md)              |
|                | download files from the      |                              |
|                | Internet, and monitor the    |                              |
|                | download progress and        |     [Data Storage and        |
|                | status.                      |     Management](../../../gui |
|                |                              | des/web/data/data-cover-w.md |
|                |                              | )                            |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Content](../../../../or |
|                |                              | g.tizen.web.apireference/htm |
|                |                              | l/device_api/wearable/index. |
|                |                              | html#Contents)               |
+----------------+------------------------------+------------------------------+
| Messaging      | This API contains classes    | -   Guides:                  |
|                | and interfaces that enable   |     [Messaging](../../../gui |
|                | you to manage push           | des/web/messaging/messaging- |
|                | messaging.                   | cover-w.md)                  |
|                | You can receive push         |                              |
|                | notifications from a push    | -   API Reference:           |
|                | server.                      |     [Messaging](../../../../ |
|                |                              | org.tizen.web.apireference/h |
|                |                              | tml/device_api/wearable/inde |
|                |                              | x.html#Messaging)            |
+----------------+------------------------------+------------------------------+
| Multimedia     | These APIs contain classes   | -   Guides: [Media and       |
|                | and interfaces that enable   |     Camera](../../../guides/ |
|                | you to manage                | web/media/media-cover-w.md)  |
|                | multimedia-related features. |                              |
|                | You can change and monitor   | -   API Reference:           |
|                | playback volume level, and   |     [Multimedia](../../../.. |
|                | listen to the FM radio.      | /org.tizen.web.apireference/ |
|                |                              | html/device_api/wearable/ind |
|                |                              | ex.html#Multimedia)          |
+----------------+------------------------------+------------------------------+
| Network        | These APIs contain classes   | -   Guides: [Connectivity    |
|                | and interfaces that enable   |     and                      |
|                | you to manage Bluetooth, NFC |     Wireless](../../../guide |
|                | (Near Field Communication),  | s/web/connectivity/connectiv |
|                | and secure element features. | ity-cover-w.md)              |
|                | You can transfer data over a |                              |
|                | Bluetooth connection, share  | -   API Reference:           |
|                | contacts, photos, and videos |     [Network](../../../../or |
|                | using NFC, and access secure | g.tizen.web.apireference/htm |
|                | elements, such as SIM card   | l/device_api/wearable/index. |
|                | and secure SD card, in a     | html#Network)                |
|                | device.                      |                              |
+----------------+------------------------------+------------------------------+
| Security       | This API contains classes    | -   Guides:                  |
|                | and interfaces that enable   |     [Security](../../../guid |
|                | you to manage secure keys in | es/web/security/security-cov |
|                | your application.            | er-w.md)                     |
|                | You can use security         | -   API Reference:           |
|                | functionalities, such as     |     [Security](../../../../o |
|                | storing and recalling        | rg.tizen.web.apireference/ht |
|                | private data.                | ml/device_api/wearable/index |
|                |                              | .html#Security)              |
+----------------+------------------------------+------------------------------+
| Social         | These APIs contain classes   | -   Guides: [Personal        |
|                | and interfaces that enable   |     Data](../../../guides/we |
|                | you to manage calendar and   | b/personal/personal-cover-w. |
|                | contact features.            | md)                          |
|                | You can manage calendar      | -   API Reference:           |
|                | events and tasks, address    |     [Social](../../../../org |
|                | books, and contacts on a     | .tizen.web.apireference/html |
|                | device.                      | /device_api/wearable/index.h |
|                |                              | tml#Social)                  |
+----------------+------------------------------+------------------------------+
| System         | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |                              |
|                | you to manage power, system  |     [Device Settings and     |
|                | information and setting, and |     Systems](../../../guides |
|                | time features.               | /web/device/device-cover-w.m |
|                | You can access the state of  | d)                           |
|                | the device power resource,   |                              |
|                | device system information,   |     [Media and               |
|                | and device wallpaper         |     Camera](../../../guides/ |
|                | settings. You can use        | web/media/media-cover-w.md)  |
|                | locale-specific calendar     |                              |
|                | features by retrieving date  |                              |
|                | and time information, and    |     [Sensors](../../../guide |
|                | set feedback patterns for    | s/web/sensors/sensors-cover- |
|                | specified actions. You can   | w.md)                        |
|                | also manage time features.   |                              |
|                |                              | -   API Reference:           |
|                |                              |     [System](../../../../org |
|                |                              | .tizen.web.apireference/html |
|                |                              | /device_api/wearable/index.h |
|                |                              | tml#System)                  |
+----------------+------------------------------+------------------------------+
| Cordova        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |     [Cordova](../../../guide |
|                | you use common               | s/web/cordova/cordova-cover- |
|                | functionalities in creating  | w.md)                        |
|                | Tizen Web applications.      | -   API Reference:           |
|                | You can manage the device    |     [Cordova](../../../../or |
|                | filesystem, individual       | g.tizen.web.apireference/htm |
|                | files, and various events,   | l/device_api/wearable/index. |
|                | access device and network    | html#Cordova)                |
|                | information and the device   |                              |
|                | accelerometer, create dialog |                              |
|                | boxes and system log         |                              |
|                | entries, and play audio      |                              |
|                | files.                       |                              |
+----------------+------------------------------+------------------------------+
| Web UI         | These APIs contain classes   | -   Guides: [Tizen Advanced  |
| Framework      | and interfaces that enable   |     UI](../../../guides/web/ |
|                | you to manage the Tizen      | ui/tau/tau-w.md)             |
|                | Advanced UI (TAU) features.  |                              |
|                | You can create and manage    | -   API Reference: [Advanced |
|                | various kinds of UI          |     UI                       |
|                | components.                  |     Framework](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/ui_fw_api/ui_fw_api_cover |
|                |                              | .htm)                        |
+----------------+------------------------------+------------------------------+

The following table lists the features provided by the [TV Web Device
API
Reference](../../../../org.tizen.web.apireference/html/device_api/tv/index.html).

**Table: Device API features provided for TV applications**

+----------------+------------------------------+------------------------------+
| Feature        | Purpose                      | Documentation                |
+================+==============================+==============================+
| Base           | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that provide  |                              |
|                | a set of basic definitions   |     [Data Storage and        |
|                | and interfaces that are used |     Management](../../../gui |
|                | in the Tizen Device API.     | des/web/data/data-cover-w.md |
|                | You can manage common files  | )                            |
|                | and ZIP archive files, and   |                              |
|                | define filters and sorting   |     [Error                   |
|                | modes for queries. You can   |     Handling](../../../guide |
|                | also use generic success and | s/web/error/error-w.md)      |
|                | error event handlers, in     |                              |
|                | addition to a generic error  |                              |
|                | interface and a simple       | -   API Reference:           |
|                | coordinate interface for     |     [Base](../../../../org.t |
|                | defining location            | izen.web.apireference/html/d |
|                | information.                 | evice_api/tv/index.html#Tize |
|                |                              | n)                           |
+----------------+------------------------------+------------------------------+
| Application    | These APIs contain classes   | -   Guides:                  |
| Framework      | and interfaces that enable   |                              |
|                | you to manage alarm,         |     [Alarms](../../../guides |
|                | application, and package     | /web/alarm/alarms-w.md)      |
|                | features.                    |                              |
|                | You can schedule an          |                              |
|                | application to be run at a   |     [Application             |
|                | specific time, retrieve      |     Management](../../../gui |
|                | information about the        | ides/web/app-management/app- |
|                | applications installed or    | management-cover-w.md)       |
|                | running on the device, and   |                              |
|                | enable package management.   |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Application             |
|                |                              |     Framework](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/device_api/tv/index.html# |
|                |                              | Application)                 |
+----------------+------------------------------+------------------------------+
| Content        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |                              |
|                | you to manage content and    |     [Connectivity and        |
|                | download features.           |     Wireless](../../../guide |
|                | You can search and manage    | s/web/connectivity/connectiv |
|                | multimedia content locally,  | ity-cover-w.md)              |
|                | manipulate EXIF data in JPEG |                              |
|                | files, download files from   |                              |
|                | the Internet, and monitor    |     [Data Storage and        |
|                | the download progress and    |     Management](../../../gui |
|                | status.                      | des/web/data/data-cover-w.md |
|                |                              | )                            |
|                |                              |                              |
|                |                              |     [Media and               |
|                |                              |     Camera](../../../guides/ |
|                |                              | web/media/media-cover-w.md)  |
|                |                              |                              |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Content](../../../../or |
|                |                              | g.tizen.web.apireference/htm |
|                |                              | l/device_api/tv/index.html#C |
|                |                              | ontents)                     |
+----------------+------------------------------+------------------------------+
| Messaging      | This API contains classes    | -   Guides:                  |
|                | and interfaces that enable   |     [Messaging](../../../gui |
|                | you to manage push           | des/web/messaging/messaging- |
|                | messaging.                   | cover-w.md)                  |
|                | You can receive push         |                              |
|                | notifications from a push    | -   API Reference:           |
|                | server.                      |     [Messaging](../../../../ |
|                |                              | org.tizen.web.apireference/h |
|                |                              | tml/device_api/tv/index.html |
|                |                              | #Messaging)                  |
+----------------+------------------------------+------------------------------+
| Network        | This API contains classes    | -   Guides: [Connectivity    |
|                | and interfaces that enable   |     and                      |
|                | you to manage IoT            |     Wireless](../../../guide |
|                | connectivity.                | s/web/connectivity/connectiv |
|                | You can create a client and  | ity-cover-w.md)              |
|                | server, and manage their     |                              |
|                | resources locally and        | -   API Reference:           |
|                | remotely.                    |     [Network](../../../../or |
|                |                              | g.tizen.web.apireference/htm |
|                |                              | l/device_api/tv/index.html#N |
|                |                              | etwork)                      |
+----------------+------------------------------+------------------------------+
| Security       | This API contains classes    | -   Guides:                  |
|                | and interfaces that enable   |     [Security](../../../guid |
|                | you to manage secure keys in | es/web/security/security-cov |
|                | your application.            | er-w.md)                     |
|                | You can use security         | -   API Reference:           |
|                | functionalities, such as     |     [Security](../../../../o |
|                | storing and recalling        | rg.tizen.web.apireference/ht |
|                | private data.                | ml/device_api/tv/index.html# |
|                |                              | Security)                    |
+----------------+------------------------------+------------------------------+
| System         | These APIs contain classes   | -   Guides: [Device Settings |
|                | and interfaces that enable   |     and                      |
|                | you to manage system         |     Systems](../../../guides |
|                | information, time, and Web   | /web/device/device-cover-w.m |
|                | setting features.            | d)                           |
|                | You can access the device    | -   API Reference:           |
|                | system information and use   |     [System](../../../../org |
|                | locale-specific calendar     | .tizen.web.apireference/html |
|                | features by retrieving date  | /device_api/tv/index.html#Sy |
|                | and time information. You    | stem)                        |
|                | can also set Web view        |                              |
|                | properties, such as setting  |                              |
|                | Web view user agents and     |                              |
|                | deleting Web view cookies.   |                              |
+----------------+------------------------------+------------------------------+
| Cordova        | These APIs contain classes   | -   Guides:                  |
|                | and interfaces that enable   |     [Cordova](../../../guide |
|                | you use common               | s/web/cordova/cordova-cover- |
|                | functionalities in creating  | w.md)                        |
|                | Tizen Web applications.      | -   API Reference:           |
|                | You can manage the device    |     [Cordova](../../../../or |
|                | filesystem, individual       | g.tizen.web.apireference/htm |
|                | files, and various events,   | l/device_api/tv/index.html#C |
|                | access device and network    | ordova)                      |
|                | information and the device   |                              |
|                | accelerometer, create dialog |                              |
|                | boxes and system log         |                              |
|                | entries, and play audio      |                              |
|                | files.                       |                              |
+----------------+------------------------------+------------------------------+
| TV Controls    | These APIs contain classes   | -   API Reference: [TV       |
|                | and interfaces that enable   |     Controls](../../../../or |
|                | you control the TV           | g.tizen.web.apireference/htm |
|                | functionalities, such as     | l/device_api/tv/index.html#T |
|                | channels and audio.          | V%20Control)                 |
|                | You can modify the volume    |                              |
|                | level, switch TV channels,   |                              |
|                | get program guide            |                              |
|                | information, and manage TV   |                              |
|                | settings. You can also       |                              |
|                | access 3D mode information,  |                              |
|                | monitor remote control key   |                              |
|                | events, and control the main |                              |
|                | and PIP window on the TV     |                              |
|                | screen.                      |                              |
+----------------+------------------------------+------------------------------+

The following table lists the features provided by the [Mobile Web
W3C/HTML5 and Supplementaries API
Reference](../../../../org.tizen.web.apireference/html/w3c_api/w3c_api_m.html).

**Table: W3C/HTML5 and some supplementary API features provided for
mobile applications**

+----------------+------------------------------+------------------------------+
| Feature        | Purpose                      | Documentation                |
+================+==============================+==============================+
| DOM, Forms and | These APIs enable you to     | -   Guides: [User            |
| Styles         | create animations, specify   |     Interface](../../../guid |
|                | the border and background    | es/web/w3c/ui/ui-guide-w.md) |
|                | styles of HTML elements,     |                              |
|                | apply styles to HTML         | -   API Reference: [DOM,     |
|                | documents, specify the color |     Forms and                |
|                | and opacity of HTML          |     Styles](../../../../org. |
|                | elements, create flexible    | tizen.web.apireference/html/ |
|                | and multi-column layouts for | w3c_api/w3c_api_m.html#dom)  |
|                | Web applications, move,      |                              |
|                | rotate, stretch, and scale   |                              |
|                | elements, and add effects    |                              |
|                | using CSS3 properties. They  |                              |
|                | also enable you to use CSS   |                              |
|                | and JavaScript code          |                              |
|                | effectively with HTML        |                              |
|                | elements, implement Web      |                              |
|                | forms for user input, define |                              |
|                | media features for specific  |                              |
|                | output devices, select       |                              |
|                | element nodes in the DOM     |                              |
|                | tree, and store information  |                              |
|                | about the page that the user |                              |
|                | has viewed.                  |                              |
+----------------+------------------------------+------------------------------+
| Device         | These APIs enable you to     | -   Guides:                  |
|                | retrieve the battery status  |     [Device](../../../guides |
|                | and detect changes in it,    | /web/w3c/device/device-guide |
|                | detect rotation and          | -w.md)                       |
|                | acceleration motions, manage | -   API Reference:           |
|                | screen orientation,          |     [Device](../../../../org |
|                | implement and control        | .tizen.web.apireference/html |
|                | various types of touch       | /w3c_api/w3c_api_m.html#devi |
|                | events, and implement        | ce)                          |
|                | different vibration patterns |                              |
|                | on a Tizen device.           |                              |
+----------------+------------------------------+------------------------------+
| Graphics       | These APIs enable you to     | -   Guides:                  |
|                | create images, shapes, and   |     [Graphics](../../../guid |
|                | text using the HTML5 canvas  | es/web/w3c/graphics/graphics |
|                | element and HTML canvas 2D   | -guide-w.md)                 |
|                | context, and create and      |                              |
|                | modify SVG elements in your  | -   API Reference:           |
|                | application.                 |     [Graphics](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_m.html#gr |
|                |                              | aphics)                      |
+----------------+------------------------------+------------------------------+
| Media          | These APIs enable you to     | -   Guides:                  |
|                | access a local device to     |     [Media](../../../guides/ |
|                | generate a multimedia        | web/w3c/media/media-guide-w. |
|                | stream, access the media     | md)                          |
|                | capture capabilities based   | -   API Reference:           |
|                | on their type, control       |     [Media](../../../../org. |
|                | multimedia playback and      | tizen.web.apireference/html/ |
|                | check supported media        | w3c_api/w3c_api_m.html#media |
|                | formats, and play audio      | )                            |
|                | content.                     |                              |
+----------------+------------------------------+------------------------------+
| Communication  | These APIs enable you to     | -   Guides:                  |
|                | send and receive data        |     [Communication](../../.. |
|                | between Web sites and        | /guides/web/w3c/communicatio |
|                | through a message channel,   | n/comm_guide-w.md)           |
|                | exchange push data with the  |                              |
|                | server, connect to the       | -   API Reference:           |
|                | socket server to send and    |     [Communication](../../.. |
|                | receive data, and use        | /../org.tizen.web.apireferen |
|                | cross-origin resource        | ce/html/w3c_api/w3c_api_m.ht |
|                | sharing (CORS) to request    | ml#communication)            |
|                | and send data of various     |                              |
|                | content types.               |                              |
+----------------+------------------------------+------------------------------+
| Storage        | These APIs enable you to     | -   Guides:                  |
|                | retrieve file content and    |     [Storage](../../../guide |
|                | information, slice data      | s/web/w3c/storage/storage-gu |
|                | objects, manage sandboxed    | ide-w.md)                    |
|                | file systems, activate       | -   API Reference:           |
|                | project resource caching and |     [Storage](../../../../or |
|                | manage the cached resources, | g.tizen.web.apireference/htm |
|                | create an object store and   | l/w3c_api/w3c_api_m.html#sto |
|                | save data in it, create      | rage)                        |
|                | databases and access them    |                              |
|                | using SQL statements, and    |                              |
|                | use session storage and      |                              |
|                | local storage.               |                              |
+----------------+------------------------------+------------------------------+
| Security       | These APIs enable you to     | -   Guides:                  |
|                | allow or block specific HTML |     [Security](../../../guid |
|                | elements on a Web page, and  | es/web/w3c/security/security |
|                | make cross-origin requests   | -guide-w.md)                 |
|                | to resources, allowing a     |                              |
|                | client-side Web application  | -   API Reference:           |
|                | to obtain data retrieved     |     [Security](../../../../o |
|                | from another origin.         | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_m.html#se |
|                |                              | curity)                      |
+----------------+------------------------------+------------------------------+
| UI             | These APIs enable you to     | -   Guides: [User            |
|                | copy content and paste it in |     Interface](../../../guid |
|                | an editable area, create and | es/web/w3c/ui/ui-guide-w.md) |
|                | manage draggable elements,   |                              |
|                | and implement drag events.   | -   API Reference:           |
|                |                              |     [UI](../../../../org.tiz |
|                |                              | en.web.apireference/html/w3c |
|                |                              | _api/w3c_api_m.html#ui)      |
+----------------+------------------------------+------------------------------+
| Performance    | These APIs enable you to     | -   Guides: [Performance and |
| and            | retrieve the visibility      |     Optimization](../../../g |
| Optimization   | status of a Web document and | uides/web/w3c/perf-opt/perfo |
|                | detect changes in it,        | rmance-guide-w.md)           |
|                | control animation frame      |                              |
|                | rate, and create and manage  | -   API Reference:           |
|                | HTML5 Web Workers to run an  |     [Performance and         |
|                | independent JavaScript       |     Optimization](../../../. |
|                | thread in the background.    | ./org.tizen.web.apireference |
|                |                              | /html/w3c_api/w3c_api_m.html |
|                |                              | #performance)                |
+----------------+------------------------------+------------------------------+
| Location       | These APIs enable you to     | -   Guides:                  |
|                | retrieve and update position |     [Location](../../../guid |
|                | information.                 | es/web/w3c/location/location |
|                |                              | -guide-w.md)                 |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Location](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_m.html#lo |
|                |                              | cation)                      |
+----------------+------------------------------+------------------------------+
| Supplementary  | These APIs enable you to     | -   Guides: [Supplementary   |
|                | manage some supplementary    |     Features](../../../guide |
|                | features, such as displaying | s/web/w3c/supplement/supplem |
|                | an element on full screen,   | ent-guide-w.md)              |
|                | accessing binary data in     |                              |
|                | JavaScript, and using the    | -   API Reference:           |
|                | WebGLa?¡Ë graphics library to   |     [Supplementary](../../.. |
|                | create 3D visual elements.   | /../org.tizen.web.apireferen |
|                |                              | ce/html/w3c_api/w3c_api_m.ht |
|                |                              | ml#Supplementary)            |
+----------------+------------------------------+------------------------------+

The following table lists the features provided by the [Wearable Web
W3C/HTML5 and Supplementaries API
Reference](../../../../org.tizen.web.apireference/html/w3c_api/w3c_api_w.html).

**Table: W3C/HTML5 and some supplementary API features provided for
wearable applications**

+----------------+------------------------------+------------------------------+
| Feature        | Purpose                      | Documentation                |
+================+==============================+==============================+
| DOM, Forms and | These APIs enable you to     | -   Guides: [User            |
| Styles         | create animations, specify   |     Interface](../../../guid |
|                | the border and background    | es/web/w3c/ui/ui-guide-w.md) |
|                | styles of HTML elements,     |                              |
|                | apply styles to HTML         | -   API Reference: [DOM,     |
|                | documents, specify the color |     Forms and                |
|                | and opacity of HTML          |     Styles](../../../../org. |
|                | elements, create flexible    | tizen.web.apireference/html/ |
|                | layouts for Web              | w3c_api/w3c_api_w.html#dom)  |
|                | applications, move, rotate,  |                              |
|                | stretch, and scale elements, |                              |
|                | and add effects using CSS3   |                              |
|                | properties. They also enable |                              |
|                | you to use CSS and           |                              |
|                | JavaScript code effectively  |                              |
|                | with HTML elements,          |                              |
|                | implement Web forms for user |                              |
|                | input, define media features |                              |
|                | for specific output devices, |                              |
|                | select element nodes in the  |                              |
|                | DOM tree, and store          |                              |
|                | information about the page   |                              |
|                | that the user has viewed.    |                              |
+----------------+------------------------------+------------------------------+
| Device         | These APIs enable you to     | -   Guides:                  |
|                | retrieve the battery status  |     [Device](../../../guides |
|                | and detect changes in it,    | /web/w3c/device/device-guide |
|                | detect rotation and          | -w.md)                       |
|                | acceleration motions,        | -   API Reference:           |
|                | implement and control        |     [Device](../../../../org |
|                | various types of touch       | .tizen.web.apireference/html |
|                | events, and implement        | /w3c_api/w3c_api_w.html#devi |
|                | different vibration patterns | ce)                          |
|                | on a Tizen wearable device.  |                              |
+----------------+------------------------------+------------------------------+
| Graphics       | These APIs enable you to     | -   Guides:                  |
|                | create images, shapes, and   |     [Graphics](../../../guid |
|                | text using the HTML5 canvas  | es/web/w3c/graphics/graphics |
|                | element and HTML canvas 2D   | -guide-w.md)                 |
|                | context.                     |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Graphics](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_w.html#gr |
|                |                              | aphics)                      |
+----------------+------------------------------+------------------------------+
| Media          | These APIs enable you to     | -   Guides:                  |
|                | access a local device to     |     [Media](../../../guides/ |
|                | generate a multimedia        | web/w3c/media/media-guide-w. |
|                | stream, control multimedia   | md)                          |
|                | playback and check supported | -   API Reference:           |
|                | media formats, and play      |     [Media](../../../../org. |
|                | audio content.               | tizen.web.apireference/html/ |
|                |                              | w3c_api/w3c_api_w.html#media |
|                |                              | )                            |
+----------------+------------------------------+------------------------------+
| Communication  | These APIs enable you to     | -   Guides:                  |
|                | send and receive data        |     [Communication](../../.. |
|                | between Web sites and        | /guides/web/w3c/communicatio |
|                | through a message channel,   | n/comm-guide-w.md)           |
|                | and connect to the socket    |                              |
|                | server to send and receive   | -   API Reference:           |
|                | data.                        |     [Communication](../../.. |
|                |                              | /../org.tizen.web.apireferen |
|                |                              | ce/html/w3c_api/w3c_api_w.ht |
|                |                              | ml#communication)            |
+----------------+------------------------------+------------------------------+
| Storage        | These APIs enable you to     | -   Guides:                  |
|                | retrieve file content and    |     [Storage](../../../guide |
|                | information, create an       | s/web/w3c/storage/storage-gu |
|                | object store and save data   | ide-w.md)                    |
|                | in it, and use session       | -   API Reference:           |
|                | storage and local storage.   |     [Storage](../../../../or |
|                |                              | g.tizen.web.apireference/htm |
|                |                              | l/w3c_api/w3c_api_w.html#sto |
|                |                              | rage)                        |
+----------------+------------------------------+------------------------------+
| Security       | These APIs enable you to     | -   Guides:                  |
|                | allow or block specific HTML |     [Security](../../../guid |
|                | elements on a Web page.      | es/web/w3c/security/security |
|                |                              | -guide-w.md)                 |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Security](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_w.html#se |
|                |                              | curity)                      |
+----------------+------------------------------+------------------------------+
| Performance    | These APIs enable you to     | -   Guides: [Performance and |
| and            | retrieve the visibility      |     Optimization](../../../g |
| Optimization   | status of a Web document and | uides/web/w3c/perf-opt/perfo |
|                | detect changes in it,        | rmance-guide-w.md)           |
|                | control animation frame      |                              |
|                | rate, and create and manage  | -   API Reference:           |
|                | HTML5 Web Workers to run an  |     [Performance and         |
|                | independent JavaScript       |     Optimization](../../../. |
|                | thread in the background.    | ./org.tizen.web.apireference |
|                |                              | /html/w3c_api/w3c_api_w.html |
|                |                              | #performance)                |
+----------------+------------------------------+------------------------------+
| Location       | These APIs enable you to     | -   Guides:                  |
|                | retrieve and update position |     [Location](../../../guid |
|                | information.                 | es/web/w3c/location/location |
|                |                              | -guide-w.md)                 |
|                |                              |                              |
|                |                              | -   API Reference:           |
|                |                              |     [Location](../../../../o |
|                |                              | rg.tizen.web.apireference/ht |
|                |                              | ml/w3c_api/w3c_api_w.html#lo |
|                |                              | cation)                      |
+----------------+------------------------------+------------------------------+
| Supplementary  | These APIs enable you to     | -   Guides: [Supplementary   |
|                | manage some supplementary    |     Features](../../../guide |
|                | features, such as managing   | s/web/w3c/supplement/supplem |
|                | the device camera, accessing | ent-guide-w.md)              |
|                | binary data in JavaScript,   |                              |
|                | and using the WebGLa?¡Ë         | -   API Reference:           |
|                | graphics library to create   |     [Supplementary](../../.. |
|                | 3D visual elements.          | /../org.tizen.web.apireferen |
|                |                              | ce/html/w3c_api/w3c_api_w.ht |
|                |                              | ml#Supplementary)            |
+----------------+------------------------------+------------------------------+


