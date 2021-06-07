# Application Filtering

The Tizen platform provides a wide range of features across a variety of hardware and software components. Among the features, there are some that can be selectively supported by the Tizen device manufacturer. For application stores to correctly select your application for installation on an appropriate device, the feature and profile information must be correctly declared in your application.

## Feature-based Filtering

Some features can be selectively supported by the Tizen device manufacturer. To prevent problems when the user is trying to run your application on a device that does not support all the features your application is using, do one of the following:

-   When the application is running, check whether the device supports the needed features. If not, the application can use other features, which are supported by the device, as a workaround.

    For example, if an application wants to use location information, it can check the device capability by using the [`Tizen.System.Information`](/application/dotnet/api/TizenFX/latest/api/Tizen.System.Information.html) class. If the device supports GPS, the application uses GPS information, and if the device supports WPS only, the application uses WPS information instead of GPS.

- Use feature-based filtering to prevent your application from being shown in the application list on Tizen Store, if the user's device does not support all the features of your application. This way you can prevent the application from being installed on an unsupported device in the first place.

    Be careful when defining the feature list for feature-based filtering. The feature list can dramatically reduce your chances of getting the application downloaded by reducing the number of devices which can support the application.

If the `tizen-manifest.xml` file of the application package includes a feature list, Tizen Store compares the capabilities of the device with the required feature conditions of the application. The store only lists the applications whose conditions match the capabilities of the device, and thus prevents incompatible applications from being installed.

**Figure: Feature-based filtering**

![Feature-based filtering](./media/app_filtering_basic_flow.png)

When multiple features are defined in the feature list for feature-based filtering, Tizen Store creates the filtering condition for all using the "AND" operation. For example, if there are `http://tizen.org/feature/network.nfc` and `http://tizen.org/feature/network.bluetooth` features in the feature list of the application package, only a device that has both those features can show the application on Tizen Store application list for downloading.

### Screen Size Feature

The screen size feature is the only exception to the normal feature handling process described above. When the screen size is defined in the feature list, Tizen Store creates the filtering condition with the "OR" operation. For example, if the `http://tizen.org/feature/screen.size.normal.480.800` and `http://tizen.org/feature/screen.size.normal.720.1280` features are defined in your application feature list, a device that supports one or the other of those features can show the application on Tizen Store application list.

If you do not specify a proper screen size in the `tizen-manifest.xml` file, your application can be rejected from Tizen Store.

The following table lists the available screen size features.

**Table: Available screen size features**

| Feature key                              | Description                              | Since |
|------------------------------------------|------------------------------------------|-------|
| `http://tizen.org/feature/screen.size.normal` | Specify this key, if the application supports all possible current and future resolutions on the normal screen size.<br><br>You cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously. If you do, only the most specific resolution key is considered and the less specific resolution keys are ignored. For example, if you specify both `http://tizen.org/feature/screen.size.normal` and `http://tizen.org/feature/screen.size.normal.320.480` keys, only the `http://tizen.org/feature/screen.size.normal.320.480` key is applied.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.240.400` | Specify this key, if the application supports the 240 x 400 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.320.320` | Specify this key, if the application supports the 320 x 320 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.320.480` | Specify this key, if the application supports the 320 x 480 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.360.360` | Specify this key, if the application supports the 360 x 360 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3.2 |
| `http://tizen.org/feature/screen.size.normal.360.480` | Specify this key, if the application supports the 360 x 480 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.480.800` | Specify this key, if the application supports the 480 x 800 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.540.960` | Specify this key, if the application supports the 540 x 960 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.600.1024` | Specify this key, if the application supports the 600 x 1024 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.720.1280` | Specify this key, if the application supports the 720 x 1280 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.1080.1920` | Specify this key, if the application supports the 1080 x 1920 resolution on the normal screen size.<br><br>You can specify multiple `http://tizen.org/feature/screen.size.normal.*` keys, if your application supports multiple screen resolutions on the normal screen size. However, you cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |
| `http://tizen.org/feature/screen.size.all` | Specify this key, if the application supports all possible current and future screen sizes and all possible current and future resolutions per screen size.<br><br>You cannot specify keys on both `screen.size.*` and `screen.size.normal.*` levels simultaneously. If you do, only the most specific resolution key is considered and the less specific resolution keys are ignored. For example, if you specify both `http://tizen.org/feature/screen.size.all` and `http://tizen.org/feature/screen.size.normal.320.480` keys, only the `http://tizen.org/feature/screen.size.normal.320.480` key is applied.<br><br>If no screen size key is declared, it is assumed that the application supports only `screen.size.normal.720.1280`. To avoid this, specify at least 1 screen size key. | 2.2.1 |

### Feature Hierarchy

The feature keys have a hierarchy. For example, consider the `http://tizen.org/feature/location`, `http://tizen.org/feature/location.gps`, and `http://tizen.org/feature/location.wps` features:

-   If the feature list includes the `http://tizen.org/feature/location.gps` feature, only a device which has the `http://tizen.org/feature/location.gps` feature can show the
    application on the Tizen Store application list.

- If the feature list includes the `http://tizen.org/feature/location` feature, a device which has the `http://tizen.org/feature/location.gps`, `http://tizen.org/feature/location.wps`, or `http://tizen.org/feature/location` feature can show the application on the Tizen Store application list.

    This means that Tizen Store considers the `http://tizen.org/feature/location` feature as the `http://tizen.org/feature/location.gps OR http://tizen.org/feature/location.wps` feature.  (If the feature list includes the `http://tizen.org/feature/location.gps` and `http://tizen.org/feature/location.wps` features together, only a device which supports both those features can show the application.)

### Adding the Feature List

To enable filtering for your .NET application, add the feature list for the application `tizen-manifest.xml` file:

1.  To open the manifest editor in the Visual Studio, double-click the `tizen-manifest.xml` file in the **Solution Explorer** view.
2.  Select the features you need, one at a time:

    1.  In the **Features** tab, click **Add**.
    2.  Select a feature.
    3.  Click **OK**.

    The manifest file (`tizen-manifest.xml`) is updated automatically.

The following table shows the available requirements for an application package. If you want to check which features are necessary for using a specific API, see the related feature in the TizenFX [API Reference](/application/dotnet/api/TizenFX/latest/):

**Table: Available requirements**

| Feature key                              | Description                              | Since |
|------------------------------------------|------------------------------------------|-------|
| `http://tizen.org/feature/accessibility.grayscale`  | Specify this key, if the application requires the accessibility grayscale feature. | 5.5   |
| `http://tizen.org/feature/accessibility.negative`  | Specify this key, if the application requires the accessibility negative feature. | 5.5   |
| `http://tizen.org/feature/account`       | Specify this key, if the application requires the account management feature. | 4.0   |
| `http://tizen.org/feature/account.sync`  | Specify this key, if the application requires the synchronization management feature. | 4.0   |
| `http://tizen.org/feature/app_history`   | Specify this key, if the application requires the application history feature. | 4.0   |
| `http://tizen.org/feature/attach_panel`  | Specify this key, if the application requires the application attach panel feature. | 5.0   |
| `http://tizen.org/feature/badge`         | Specify this key, if the application requires the badge feature. | 4.0   |
| `http://tizen.org/feature/battery`         | Specify this key, if the application requires information on the device battery | 2.3*   |
| `http://tizen.org/feature/calendar`      | Specify this key, if the application requires the calendar service. | 4.0   |
| `http://tizen.org/feature/camera`        | Specify this key, if the application requires any kind of a camera. | 2.2.1 |
| `http://tizen.org/feature/camera.back`   | Specify this key, if the application requires a back-facing camera. | 2.2.1 |
| `http://tizen.org/feature/camera.back.flash` | Specify this key, if the application requires a back-facing camera with a flash. | 2.2.1 |
| `http://tizen.org/feature/camera.front`  | Specify this key, if the application requires a front-facing camera. | 2.2.1 |
| `http://tizen.org/feature/camera.front.flash` | Specify this key, if the application requires a front-facing camera with a flash. | 2.2.1 |
| `http://tizen.org/feature/contact`       | Specify this key, if the application requires the contact service. | 4.0   |
| `http://tizen.org/feature/database.encryption` | Specify this key, if the application requires the database encryption feature. | 2.2.1 |
| `http://tizen.org/feature/display`       | Specify this key, if the application requires the display feature. | 5.5   |
| `http://tizen.org/feature/display.state` | Specify this key, if the application requires System Device API to control the display state. | 5.0 |
| `http://tizen.org/feature/download`      | Specify this key, if the application requires the download feature. | 2.3   |
| `http://tizen.org/feature/email`         | Specify this key, if the application requires the email feature. | 4.0   |
| `http://tizen.org/feature/feedback.vibration` | Specify this key, if the application requires the vibration feedback feature. | 5.0   |
| `http://tizen.org/feature/fido.uaf`      | Specify this key, if the application requires the FIDO (Fast Identity Online) UAF (Universal Authentication Framework) client API. | 3.0   |
| `http://tizen.org/feature/fmradio`       | Specify this key, if the application requires an FM radio. | 2.2.1 |
| `http://tizen.org/feature/graphics.acceleration` | Specify this key, if the application requires hardware acceleration for both 2D and 3D graphics. | 2.2.1 |
| `http://tizen.org/feature/input.keyboard` | Specify this key, if the application requires a built-in physical keyboard. | 2.2.1 |
| `http://tizen.org/feature/input.keyboard.layout` | Specify this key with a specific keyboard layout (`string` type), if the application requires a built-in physical keyboard supporting the specified keyboard layout. | 2.2.1 |
| `http://tizen.org/feature/input.rotating_bezel` | Specify this key, if the application requires rotating bezel input. | 2.3.1 |
| `http://tizen.org/feature/iot.ocf`       | Specify this key, if the application requires the Open Connectivity Foundation (OCF) framework. | 3.0   |
| `http://tizen.org/feature/led`           | Specify this key, if the application requires a LED. | 2.3   |
| `http://tizen.org/feature/location`      | Specify this key, if the application requires any location positioning features. | 2.2.1 |
| `http://tizen.org/feature/location.batch` | Specify this key, if the application requires the location tracking with a position batch information feature. | 2.3   |
| `http://tizen.org/feature/location.fused` | Specify this key, if the application requires the Fused Location feature using sensors. | 4.0   |
| `http://tizen.org/feature/location.geofence` | Specify this key, if the application requires the geofence feature. | 2.4   |
| `http://tizen.org/feature/location.gps`  | Specify this key, if the application requires the Global Positioning System (GPS) feature. | 2.2.1 |
| `http://tizen.org/feature/location.wps`  | Specify this key, if the application requires the Wi-Fi-based Positioning System (WPS) feature. | 2.2.1 |
| `http://tizen.org/feature/maps`          | Specify this key, if the application requires the map service feature. | 2.3.2 |
| `http://tizen.org/feature/media.audio_recording`    | Specify this key, if the application requires the audio recording feature. | 2.3 |
| `http://tizen.org/feature/media.image_capture`    | Specify this key, if The application requires image capturing feature. | 2.3 |
| `http://tizen.org/feature/media.video_recording`    | Specify this key, if the application requires the video recording feature. | 2.3 |
| `http://tizen.org/feature/microphone`    | Specify this key, if the application requires a microphone. | 2.2.1 |
| `http://tizen.org/feature/minicontrol`   | Specify this key, if the application requires the minicontrol feature. | 4.0   |
| `http://tizen.org/feature/multi_point_touch.pinch_zoom` | Specify this key, if the application requires a pinch-zoom gesture feature. | 2.2.1 |
| `http://tizen.org/feature/multi_point_touch.point_count` | Specify this key with a specific number (`int` type), if the application requires the minimum of specified number of simultaneous touches in a multi-point touch. | 2.2.1 |
| `http://tizen.org/feature/multimedia.media_codec`     | Specify this key, if the application requires the media codec feature. | 4.0   |
| `http://tizen.org/feature/multimedia.player.spherical_video` | Specify this key, if the application requires the 360-degree video playback feature. | 5.0   |
| `http://tizen.org/feature/multimedia.transcoder` | Specify this key, if the application requires the multimedia transcoder feature. | 2.3   |
| `http://tizen.org/feature/network.bluetooth` | Specify this key, if the application requires the Bluetooth feature. | 2.2.1 |
| `http://tizen.org/feature/network.bluetooth.audio.call` | Specify this key, if the application requires the Bluetooth hands-free feature (HFP). | 2.3   |
| `http://tizen.org/feature/network.bluetooth.audio.controller` | Specify this key, if the application requires the Bluetooth Advanced Audio Distribution (A2DP) sink feature and the Bluetooth Audio Video Remote Control (AVRCP) controller feature. | 3.0   |
| `http://tizen.org/feature/network.bluetooth.audio.media` | Specify this key, if the application requires the Bluetooth Advanced Audio feature (A2DP). | 2.3   |
| `http://tizen.org/feature/network.bluetooth.health` | Specify this key, if the application requires the Bluetooth Health feature (HDP). | 2.3   |
| `http://tizen.org/feature/network.bluetooth.hid` | Specify this key, if the application requires the Bluetooth Human Input Device feature (HID). | 2.3   |
| `http://tizen.org/feature/network.bluetooth.hid_device` | Specify this key, if the application requires the Bluetooth Human Interface Device (HID) device feature. | 3.0   |
| `http://tizen.org/feature/network.bluetooth.le` | Specify this key, if the application requires the Bluetooth LE feature. | 2.3   |
| `http://tizen.org/feature/network.bluetooth.le.gatt.client` | Specify this key, if the application requires the Bluetooth GATT client feature. | 4.0   |
| `http://tizen.org/feature/network.bluetooth.le.gatt.server` | Specify this key, if the application requires the Bluetooth GATT server feature. | 4.0   |
| `http://tizen.org/feature/network.bluetooth.le.ipsp` | Specify this key, if the application requires the Bluetooth Internet Protocol Support Profile (IPSP) feature. | 5.0   |
| `http://tizen.org/feature/network.bluetooth.oob` | Specify this key, if the application requires the Bluetooth Out Of Band (OOB) feature. | 4.0   |
| `http://tizen.org/feature/network.bluetooth.opp` | Specify this key, if the application requires the Bluetooth Object Push feature (OPP). | 2.3   |
| `http://tizen.org/feature/network.bluetooth.phonebook.client` | Specify this key, if the application requires the Bluetooth Phone Book Access (PBAP) client feature. | 3.0   |
| `http://tizen.org/feature/network.ethernet` | Specify this key, if the application requires the Ethernet connection. | 2.4   |
| `http://tizen.org/feature/network.inm` | Specify this key, if the application requires the Intelligent Network Monitoring (INM) feature. | 5.0 |
| `http://tizen.org/feature/network.mtp`   | Specify this key, if the application requires the Media Transfer Protocol (MTP) Host (Initiator) feature. | 3.0   |
| `http://tizen.org/feature/network.net_proxy` | Specify this key, if the application requires the net-proxy feature for the Internet connection. A net-proxy feature for a device acts as an intermediary between client (network service customer) and server (network service provider). | 3.0   |
| `http://tizen.org/feature/network.nfc`   | Specify this key, if the application requires the use of any API that, in turn, requires the Near Field Communication (NFC) feature. | 2.2.1 |
| `http://tizen.org/feature/network.nfc.card_emulation` | Specify this key, if the application requires the NFC card emulation feature. | 2.3   |
| `http://tizen.org/feature/network.nfc.card_emulation.hce` | Specify this key, if the application requires the NFC host-based card emulation feature. | 2.3.1 |
| `http://tizen.org/feature/network.nfc.p2p` | Specify this key, if the application requires the NFC p2p feature. | 2.3.1 |
| `http://tizen.org/feature/network.nfc.tag` | Specify this key, if the application requires the NFC tag feature. | 2.3.1 |
| `http://tizen.org/feature/network.push`  | Specify this key, if the application requires the network-based push service. | 2.2.1 |
| `http://tizen.org/feature/network.secure_element` | Specify this key, if the application requires the secure element feature. | 2.2.1 |
| `http://tizen.org/feature/network.secure_element.ese` | Specify this key, if the application requires the ESE secure element feature. | 2.3   |
| `http://tizen.org/feature/network.secure_element.uicc` | Specify this key, if the application requires the UICC secure element feature. | 2.3   |
| `http://tizen.org/feature/network.service_discovery.dnssd` | Specify this key, if the application requires the DNS-based Service Discovery Feature (DNSSD). | 3.0   |
| `http://tizen.org/feature/network.service_discovery.ssdp` | Specify this key, if the application requires the Simple Service Discovery Protocol feature (SSDP). | 3.0   |
| `http://tizen.org/feature/network.telephony` | Specify this key, if the application requires the use of any API that, in turn, requires the telephony feature. | 2.2.1 |
| `http://tizen.org/feature/network.telephony.mms` | Specify this key, if the application requires the MMS feature. | 2.2.1 |
| `http://tizen.org/feature/network.telephony.sms` | Specify this key, if the application requires the SMS feature. | 2.4   |
| `http://tizen.org/feature/network.vpn`   | Specify this key, if the application requires the Virtual Private Network feature (VPN). | 3.0   |
| `http://tizen.org/feature/network.wifi`  | Specify this key, if the application requires the use of any API that, in turn, requires the Wi-Fi feature. | 2.2.1 |
| `http://tizen.org/feature/network.wifi.direct` | Specify this key, if the application requires the Wi-Fi Direct&reg; feature. | 2.2.1 |
| `http://tizen.org/feature/network.wifi.direct.display` | Specify this key, if the application requires the Wi-Fi Direct display feature. | 2.3   |
| `http://tizen.org/feature/network.wifi.direct.service_discovery` | Specify this key, if the application requires the Wi-Fi Direct service discovery feature. | 2.3   |
| `http://tizen.org/feature/network.wifi.tdls` | Specify this key, if the application requires the Wi-Fi Tunneled Direct Link Setup (TDLS). | 3.0   |
| `http://tizen.org/feature/nlp` | Specify this key, if the application requires the Natural Language Processing (NLP) API. | 5.0 |
| `http://tizen.org/feature/oauth2` | Specify this key, if the application requires the OAuth 2.0 protocol feature. | 4.0 |
| `http://tizen.org/feature/opengles.surfaceless_context` | Specify this key, if the application requires the EGL extension of Surfaceless Context for OpenGL&reg; ES. | 6.0   |
| `http://tizen.org/feature/opengles.version.1_1` | Specify this key, if the application requires OpenGL&reg; ES version 1.1 at minimum. You can specify at most 1 OpenGL&reg; ES version. If you specify multiple versions, only the highest one is considered. | 2.2.1 |
| `http://tizen.org/feature/opengles.version.2_0` | Specify this key, if the application requires OpenGL&reg; ES version 2.0. You can specify at most 1 OpenGL&reg; ES version. If you specify multiple versions, only the highest one is considered. | 2.2.1 |
| `http://tizen.org/feature/opengles.version.3_0` | Specify this key, if the application requires OpenGL&reg; ES version 3.0. You can specify at most 1 OpenGL&reg; ES version. If you specify multiple versions, only the highest one is considered. | 2.4   |
| `http://tizen.org/feature/opengles.version.3_1` | Specify this key, if the application requires OpenGL&reg; ES version 3.1. You can specify at most 1 OpenGL&reg; ES version. If you specify multiple versions, only the highest one is considered. | 3.0   |
| `http://tizen.org/feature/opengles.version.3_2` | Specify this key, if the application requires OpenGL&reg; ES version 3.2. You can specify at most 1 OpenGL&reg; ES version. If you specify multiple versions, only the highest one is considered. | 4.0   |
| `http://tizen.org/feature/platform.core.cpu.arch.armv7` | Specify this key, if the application requires the ARMv7 CPU architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.cpu.arch.armv8` | Specify this key, if the application requires the ARMv8 CPU architecture. | 4.0 |
| `http://tizen.org/feature/platform.core.cpu.arch.x86` | Specify this key, if the application requires the x86 CPU architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.fpu.arch.sse2` | Specify this key, if the application requires the SSE2 Floating Point Unit (FPU) architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.fpu.arch.sse3` | Specify this key, if the application requires the SSE3 FPU architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.fpu.arch.ssse3` | Specify this key, if the application requires the SSSE3 FPU architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.fpu.arch.vfpv3` | Specify this key, if the application requires the VFPv3 FPU architecture. | 2.2.1 |
| `http://tizen.org/feature/platform.core.fpu.arch.vfpv4` | Specify this key, if the application requires the VFPv4 FPU architecture. | 4.0 |
| `http://tizen.org/feature/screen.auto_rotation` | Specify this key, if the application requires the automatic screen rotation feature. | 2.2.1 |
| `http://tizen.org/feature/screen.shape.circle` | Specify this key, if the application requires a circle-shaped screen. | 2.3.1 |
| `http://tizen.org/feature/screen.shape.rectangle` | Specify this key, if the application requires a rectangle-shaped screen. | 2.3.1 |
| `http://tizen.org/feature/screen.size.all` | Specify this key, if the application supports all possible current and future screen sizes and all possible current and future resolutions per screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal` | Specify this key, if the application supports all possible current and future resolutions on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.240.400` | Specify this key, if the application supports the 240 x 400 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.320.320` | Specify this key, if the application supports the 320 x 320 resolution on the normal screen size. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.320.480` | Specify this key, if the application supports the 320 x 480 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.360.360` | Specify this key, if the application supports the 360 x 360 resolution on the normal screen size. | 2.3.2 |
| `http://tizen.org/feature/screen.size.normal.360.480` | Specify this key, if the application supports the 360 x 480 resolution on the normal screen size. | 2.3   |
| `http://tizen.org/feature/screen.size.normal.480.800` | Specify this key, if the application supports the 480 x 800 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.540.960` | Specify this key, if the application supports the 540 x 960 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.600.1024` | Specify this key, if the application supports the 600 x 1024 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.720.1280` | Specify this key, if the application supports the 720 x 1280 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/screen.size.normal.1080.1920` | Specify this key, if the application supports the 1080 x 1920 resolution on the normal screen size. | 2.2.1 |
| `http://tizen.org/feature/security.privacy_privilege` | Specify this key, if the application requires the setting of the privacy privilege to confirm its state. | 5.0 |
| `http://tizen.org/feature/security.tee` | Specify this key, if the application requires the Trusted Execution Environment (TEE). | 4.0 |
| `http://tizen.org/feature/sensor.accelerometer` | Specify this key, if the application requires an acceleration sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.activity_recognition` | Specify this key, if the application requires an activity recognition sensor. | 2.3   |
| `http://tizen.org/feature/sensor.barometer` | Specify this key, if the application requires a barometer sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.geomagnetic_rotation_vector` | Specify this key, if the application requires a geomagnetic-based rotation vector sensor. | 2.4   |
| `http://tizen.org/feature/sensor.gesture_recognition` | Specify this key, if the application requires a gesture recognition sensor. | 2.3   |
| `http://tizen.org/feature/sensor.gravity` | Specify this key, if the application requires a gravity sensor. | 2.3   |
| `http://tizen.org/feature/sensor.gyroscope` | Specify this key, if the application requires a gyro sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.gyroscope.uncalibrated` | Specify this key, if the application requires an uncalibrated gyroscope sensor. | 2.4   |
| `http://tizen.org/feature/sensor.gyroscope_rotation_vector` | Specify this key, if the application requires a gyroscope-based rotation vector sensor. | 2.4   |
| `http://tizen.org/feature/sensor.heart_rate_monitor` | Specify this key, if the application requires a heart rate monitor sensor. | 2.3   |
| `http://tizen.org/feature/sensor.humidity` | Specify this key, if the application requires a humidity sensor. | 2.3   |
| `http://tizen.org/feature/sensor.linear_acceleration` | Specify this key, if the application requires a linear acceleration sensor. | 2.3   |
| `http://tizen.org/feature/sensor.magnetometer` | Specify this key, if the application requires a magnetic sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.magnetometer.uncalibrated` | Specify this key, if the application requires an uncalibrated geomagnetic sensor. | 2.4   |
| `http://tizen.org/feature/sensor.pedometer` | Specify this key, if the application requires a pedometer sensor. | 2.3   |
| `http://tizen.org/feature/sensor.photometer` | Specify this key, if the application requires a photometer sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.proximity` | Specify this key, if the application requires a proximity sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.rotation_vector` | Specify this key, if the application requires a rotation vector sensor. | 2.3   |
| `http://tizen.org/feature/sensor.significant_motion` | Specify this key, if the application requires a significant motion sensor which detects any significant movements caused by changes in the user location. | 4.0   |
| `http://tizen.org/feature/sensor.sleep_monitor` | Specify this key, if the application requires a sleep monitor sensor which tracks the human sleep state or a sleep detector sensor which detects whether the human falls asleep or wakes up. | 3.0   |
| `http://tizen.org/feature/sensor.temperature` | Specify this key, if the application requires a temperature sensor. | 2.3   |
| `http://tizen.org/feature/sensor.tiltmeter` | Specify this key, if the application requires a tilt sensor. | 2.2.1 |
| `http://tizen.org/feature/sensor.ultraviolet` | Specify this key, if the application requires an ultraviolet sensor. | 2.3   |
| `http://tizen.org/feature/sensor.wrist_up` | Specify this key, if the application requires a wrist up sensor. | 2.3   |
| `http://tizen.org/feature/shell.appwidget` | Specify this key, if the application requires the AppWidget (Dynamic Box) feature. | 2.2.1 |
| `http://tizen.org/feature/shortcut`      | Specify this key, if the application requires the shortcut feature. | 4.0   |
| `http://tizen.org/feature/speech.control` | Specify this key, if the application requires the voice control feature. | 2.4   |
| `http://tizen.org/feature/speech.recognition` | Specify this key, if the application requires the speech recognition (STT) feature. | 2.2.1 |
| `http://tizen.org/feature/speech.synthesis` | Specify this key, if the application requires the speech synthesis (text to speech, TTS) feature. | 2.2.1 |
| `http://tizen.org/feature/storage.external` | Specify this key, if the application requires the external storage feature. | 5.5   |
| `http://tizen.org/feature/systemsetting` | Specify this key, if the application requires the SystemSetting feature. | 2.3   |
| `http://tizen.org/feature/systemsetting.font` | Specify this key, if the application requires a font. | 5.0   |
| `http://tizen.org/feature/systemsetting.home_screen` | Specify this key, if the application requires a home screen. | 2.3   |
| `http://tizen.org/feature/systemsetting.incoming_call` | Specify this key, if the application requires incomming call and sound notification. | 2.3   |
| `http://tizen.org/feature/systemsetting.lock_screen` | Specify this key, if the application requires a lock screen. | 2.3   |
| `http://tizen.org/feature/systemsetting.notification_email` | Specify this key, if the application requires an email notification. | 2.3   |
| `http://tizen.org/feature/usb.accessory` | Specify this key, if the application requires the USB client (or accessory) feature. | 2.2.1 |
| `http://tizen.org/feature/usb.host`      | Specify this key, if the application requires the USB host feature. | 2.2.1 |
| `http://tizen.org/feature/vision.barcode_detection` | Specify this key, if the application requires the barcode detection feature. | 2.4   |
| `http://tizen.org/feature/vision.barcode_generation` | Specify this key, if the application requires the barcode generation feature. | 2.4   |
| `http://tizen.org/feature/vision.face_recognition` | Specify this key, if the application requires the face recognition feature. | 2.2.1 |
| `http://tizen.org/feature/vision.image_recognition` | Specify this key, if the application requires the image recognition feature. | 2.2.1 |
| `http://tizen.org/feature/vulkan.version.1_0` | Specify this key, if the application requires Vulkan&trade; version 1.0. | 3.0 |
| `http://tizen.org/feature/watch_app`     | Specify this key, if the application requires the watch application feature. | 4.0   |

\* This key has been available for checking device capabilities since Tizen 2.3. It is recommended for application filtering purposes since Tizen 4.0.

## Profile-based Filtering

A Tizen profile describes the requirements for a category of Tizen devices that have a common application execution environment. Applications are created for a single specific target profile, such as mobile, wearable, or TV, and can run on devices compliant with that profile.

Use profile-based filtering to ensure that your application is only downloaded on the appropriate device profile. To ensure this, declare the intended profile by adding the `profile name` element in the `tizen-manifest.xml` file.

The following table lists the Tizen profiles and related profile name attributes.

**Table: Tizen profiles and profile name attributes**

| Tizen profile | Profile name attribute |
|---------------|------------------------|
| Mobile        | `mobile`               |
| Wearable      | `wearable`             |
| TV            | `tv`                   |

In a Tizen .NET application, the profile name element can be added to the `tizen-manifest.xml` file as follows:

```xml
<manifest xmlns="http://tizen.org/ns/packages" api-version="5" ... >
   <profile name="wearable" />
```

Tizen Store compares the device profile and the `profile name` element in an application. The store only shows the applications with a profile name matching the device profile to prevent unsupported applications from being installed.
