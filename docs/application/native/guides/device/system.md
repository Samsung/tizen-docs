# System Information


You can access various information about fixed platform features or device capabilities by querying system information keys. You can also check for supported features.

The main features of the System Information API include:

- Getting system information

  You can [retrieve system information](#model), such as the model name of the device.

- Checking for supported features

  You can [check whether the device supports a feature](#check), such as camera.

**Table: Device-specific information categories**

| Category             | Description                              |
|----------------------|------------------------------------------|
| Platform information | Platform or API version, screen coordination system, and CPU and FPU architecture. |
| Device capabilities  | Sensors, networks, connections, and additional components. |

To obtain the information, query a feature or system key.

**Table: System information keys**

| [Feature keys](#feature)           |                                |                                  |                                  |
|------------------------------------|--------------------------------|----------------------------------|----------------------------------|
| [Account](#account)                | [FM radio](#fmradio)           | [Microphone](#microphone)        | [Sensor](#sensor)                |
| [Application history](#apphistory) | [Graphics](#graphics)          | [Multimedia](#multimedia)        | [Shell](#shell)                  |
| [Battery](#battery)                | [Human activity monitor](#ham) | [Multi-point touch](#multipoint) | [Sip](#sip)                      |
| [Camera](#camera)                  | [Input](#input)                | [Network](#network)              | [Speech](#speech)                |
| [Consumer IR](#consumer)           | [IOT](#iot)                    | [OAuth 2.0](#oauth2)             | [System setting](#systemsetting) |
| [Contextual trigger](#trigger)     | [LED](#led)                    | [OpenGL&reg; ES](#opengl)            | [USB](#usb)                      |
| [Database](#database)              | [Location](#location)          | [Platform](#platformfeat)        | [Vision](#vision)                |
| [Download](#download)              | [Maps](#maps)                  | [Profile](#profile_feat)         | [Web](#web)                      |
| [FIDO](#fido)                      | [Media](#media)                | [Screen](#screen)                | -                                |
| [System keys](#system)             |                                |                                  |                                  |
| [Build](#build)                    | [Model name](#modelname)       | [Sound](#sound)                  | -                                |
| [Manufacturer](#manufacturer)      | [Platform](#platformsys)       | [TizenID](#tizenid)              | -                                |

> **Note**  
> Some device-specific information keys look similar to feature keys for application filtering, but their usage differs. Feature keys for device-specific information are used to determine whether the feature is supported in the system. Feature keys for application filtering let the Tizen Store filter applications based on features.

## Prerequisites

To use the functions and data types of the System Information API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__SYSTEM__INFO__MODULE.html) applications), include the `<system_info.h>` header file in your application:

```
#include <system_info.h>
```

<a name="model"></a>
## Getting the Device Model Name

Device-specific information consists of "key, value" pairs. To get the device model name, use the `http://tizen.org/system/model_name` key with the data type-specific get function.

The model name key data type is `string`, which means that you need to use the `system_info_get_platform_string()` function.

When no longer needed, release the value of the key with the `free()` function.

```
void
func(void)
{
    char *value;
    int ret;

    ret = system_info_get_platform_string("http://tizen.org/system/model_name", &value);
    if (ret != SYSTEM_INFO_ERROR_NONE) {
        /* Error handling */

        return;
    }

    dlog_print(DLOG_INFO, LOG_TAG, "Model name: %s", value);

    free(value); /* Release after use */
}
```

<a name="check"></a>
## Checking for Supported Features

To determine, for example, whether the device has a camera, use the `http://tizen.org/feature/camera` key with the data type-specific get function.

The camera key data type is `bool`, which means that you need to use the `system_info_get_platform_bool()` function.

```
#include <stdbool.h>

void
func(void)
{
    bool value;
    int ret;

    ret = system_info_get_platform_bool("http://tizen.org/feature/camera", &value);
    if (ret != SYSTEM_INFO_ERROR_NONE) {
        /* Error handling */

        return;
    }

    dlog_print(DLOG_INFO, LOG_TAG, "Camera: %s", value ? "Supported" : "Not supported");
}
```

<a name="feature"></a>
## Feature Keys

The following table lists the account feature keys.

<a name="account"></a>
**Table: Account feature keys**  

| Key                                     | Type   | Description                              |
|-----------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/account`      | `bool` | The platform returns `true` for this key, if the device supports the Account Manager API. |
| `http://tizen.org/feature/account.sync` | `bool` | The platform returns `true` for this key, if the device supports the Sync Manager API. |

The following table lists the application history feature keys.

<a name="apphistory"></a>
**Table: Application history feature keys**  

| Key                                    | Type   | Description                              |
|----------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/app_history` | `bool` | The platform returns `true` for this key, if the device supports the application history feature. |

The following table lists the battery feature keys.

<a name="battery"></a>
**Table: Battery feature keys**  

| Key                                | Type   | Description                              |
|------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/battery` | `bool` | The platform returns `true` for this key, if the device has a battery. |

The following table lists the camera feature keys.

<a name="camera"></a>
**Table: Camera feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/camera`        | `bool` | The platform returns `true` for this key, if the device provides any kind of a camera. |
| `http://tizen.org/feature/camera.back`   | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/camera` key, if the device provides a back-facing camera. |
| `http://tizen.org/feature/camera.back.flash` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/camera.back` key, if the device provides a back-facing camera with a flash. |
| `http://tizen.org/feature/camera.front`  | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/camera` key, if the device provides a front-facing camera. |
| `http://tizen.org/feature/camera.front.flash` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/camera.front` key, if the device provides a front-facing camera with a flash. |

The following table lists the consumer IR feature keys.

<a name="consumer"></a>
**Table: Consumer IR feature keys**  

| Key                                    | Type   | Description                              |
|----------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/consumer_ir` | `bool` | The platform returns `true` for this key, if the device supports the Consumer Infrared (CIR) feature. |

The following table lists the contextual trigger feature keys.

<a name="trigger"></a>
**Table: Contextual trigger feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/contextual_trigger` | `bool` | The platform returns `true` for this key, if the device supports the contextual trigger feature. |

The following table lists the database feature keys.

<a name="database"></a>
**Table: Database feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/database.encryption` | `bool` | The platform returns `true` for this key, if the device supports database encryption. |

The following table lists the download feature keys.

<a name="download"></a>
**Table: Download feature keys**  

| Key                                 | Type   | Description                              |
|-------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/download` | `bool` | The platform returns `true` for this key, if the device supports the Download API. |

The following table lists the FIDO feature keys.

<a name="fido"></a>
**Table: FIDO feature keys**  

| Key                                 | Type   | Description                              |
|-------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/fido.uaf` | `bool` | The platform returns `true` for this key, if the device supports the FIDO (Fast Identity Online) UAF (Universal Authentication Framework) client API. |

The following table lists the FM radio feature keys.

<a name="fmradio"></a>
**Table: FM radio feature keys**  

| Key                                | Type   | Description                              |
|------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/fmradio` | `bool` | The platform returns `true` for this key, if the device supports an FM radio. |

The following table lists the graphics feature keys.

<a name="graphics"></a>
**Table: Graphics feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/graphics.acceleration` | `bool` | The platform returns `true` for this key, if the device supports graphics hardware acceleration. |

The following table lists the human activity monitor feature keys.

<a name="ham"></a>
**Table: Human activity monitor feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/humanactivitymonitor` | `bool` | The platform returns `true` for this key, if the device supports any of the human activity monitor sensors. |

The following table lists the input feature keys.

<a name="input"></a>
**Table: Input feature keys**  

| Key                                      | Type     | Description                              |
|------------------------------------------|----------|------------------------------------------|
| `http://tizen.org/feature/input.keyboard` | `bool`   | The platform returns `true` for this key, if the device provides a built-in keyboard supporting any keyboard layout. |
| `http://tizen.org/feature/input.keyboard.layout` | `String` | The platform returns the keyboard layout (such as `"qwerty"`) supported by the built-in keyboard for this key and returns `true` for the `http://tizen.org/feature/input.keyboard` key.<br>If the device does not provide a built-in keyboard, the platform returns an empty string for this key and returns `false` for the `http://tizen.org/feature/input.keyboard` key. |
| `http://tizen.org/feature/input.rotating_bezel` | `bool`   | The platform returns `true` for this key, if the device supports the rotating bezel feature. |

The following table lists the IOT feature keys.

<a name="iot"></a>
**Table: IOT feature keys**  

| Key                                | Type   | Description                              |
|------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/iot.ocf` | `bool` | The platform returns `true` for this key, if the device supports the Open Connectivity Foundation (OCF) framework. |

The following table lists the LED feature keys.

<a name="led"></a>
**Table: LED feature keys**  

| Key                            | Type   | Description                              |
|--------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/led` | `bool` | The platform returns `true` for this key, if the device supports the LED. |

The following table lists the location feature keys.

<a name="location"></a>
**Table: Location feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/location`      | `bool` | The platform returns `true` for this key, if the device supports location positioning. |
| `http://tizen.org/feature/location.batch` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/location` key, if the device supports the GPS batch feature. |
| `http://tizen.org/feature/location.geofence` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/location` key, if the device supports the geofence feature. |
| `http://tizen.org/feature/location.gps`  | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/location` key, if the device supports the Global Positioning System (GPS). |
| `http://tizen.org/feature/location.gps.satellite` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/location.gps` key, if the device has a GPS chip that supports satellite information. |
| `http://tizen.org/feature/location.wps`  | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/location` key, if the device supports the Wi-Fi-based Positioning System (WPS). |

The following table lists the maps feature keys.

<a name="maps"></a>
**Table: Maps feature keys**  

| Key                             | Type   | Description                              |
|---------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/maps` | `bool` | The platform returns `true` for this key, if the device supports the map service feature. |

The following table lists the media feature keys.

<a name="media"></a>
**Table: Media feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/media.audio_recording` | `bool` | The platform returns `true` for this key, if the device supports the audio recording feature. |
| `http://tizen.org/feature/media.image_capture` | `bool` | The platform returns `true` for this key, if the device supports the image capture feature. |
| `http://tizen.org/feature/media.video_recording` | `bool` | The platform returns `true` for this key, if the device supports the video recording feature. |

The following table lists the microphone feature keys.

<a name="microphone"></a>
**Table: Microphone feature keys**  

| Key                                   | Type   | Description                              |
|---------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/microphone` | `bool` | The platform returns `true` for this key, if the device supports a microphone. |

The following table lists the multimedia feature keys.

<a name="multimedia"></a>
**Table: Multimedia feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/multimedia.transcoder` | `bool` | The platform returns `true` for this key, if the device supports the transcoder. |

The following table lists the multi-point touch feature keys.

<a name="multipoint"></a>
**Table: Multi-point touch feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/multi_point_touch.pinch_zoom` | `bool` | The platform returns `true` for this key, if the device supports pinch zoom gestures. |
| `http://tizen.org/feature/multi_point_touch.point_count` | `int`  | The platform returns the maximum number of supported multi-touch points for this key.<br>The platform returns a value less than 2 for this key, if the device does not support multi-point touch. |

The following table lists the network feature keys.

<a name="network"></a>
**Table: Network feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/network.bluetooth` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth. |
| `http://tizen.org/feature/network.bluetooth.audio.call` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Hands-free Profile (HFP). |
| `http://tizen.org/feature/network.bluetooth.audio.controller` | `bool` | The platform returns `true` for this key, if the device supports the Bluetooth Advanced Audio Distribution (A2DP) sink feature and the Bluetooth Audio Video Remote Control (AVRCP) controller feature. |
| `http://tizen.org/feature/network.bluetooth.audio.media` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Advanced Audio Distribute Profile (A2DP). |
| `http://tizen.org/feature/network.bluetooth.health` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Health Device Profile (HDP). |
| `http://tizen.org/feature/network.bluetooth.hid` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Human Input Device (HID). |
| `http://tizen.org/feature/network.bluetooth.hid.device` | `bool` | The platform returns `true` for this key, if the device supports the Bluetooth Human Interface Device (HID) device feature. |
| `http://tizen.org/feature/network.bluetooth.le` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Low Energy (BLE). |
| `http://tizen.org/feature/network.bluetooth.opp` | `bool` | The platform returns `true` for this key, if the device supports Bluetooth Object Push Profile (OPP). |
| `http://tizen.org/feature/network.bluetooth.phonebook.client` | `bool` | The platform returns `true` for this key, if the device supports the Bluetooth Phone Book Access (PBAP) client feature. |
| `http://tizen.org/feature/network.ethernet` | `bool` | The platform returns `true` for this key, if the device supports Ethernet. |
| `http://tizen.org/feature/network.internet` | `bool` | The platform returns `true` for this key, if the device supports Internet access. |
| `http://tizen.org/feature/network.mtp`   | `bool` | The platform returns `true` for this key, if the device supports the Media Transfer Protocol (MTP) Host (Initiator) feature. |
| `http://tizen.org/feature/network.net_proxy` | `bool` | The platform returns `true` for this key, if the device supports the net-proxy, a proxy type connection for a device that acts as an intermediary between client (network service customer) and server (network service provider). |
| `http://tizen.org/feature/network.nfc`   | `bool` | The platform returns `true` for this key, if the device supports Adapter and NDEF APIs which require Near Field Communication (NFC). |
| `http://tizen.org/feature/network.nfc.card_emulation` | `bool` | The platform returns `true` for this key, if the device is recognized by the NFC card readers. |
| `http://tizen.org/feature/network.nfc.card_emulation.hce` | `bool` | The platform returns `true` for this key, if the device supports the HCE card emulation feature. |
| `http://tizen.org/feature/network.nfc.p2p` | `bool` | The platform returns `true` for this key, if the device supports P2P APIs which require Near Field Communication (NFC). |
| `http://tizen.org/feature/network.nfc.reserved_push` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.nfc` key, if the device supports the NFC reserved push feature. |
| `http://tizen.org/feature/network.nfc.tag` | `bool` | The platform returns `true` for this key, if the device supports Tag APIs which require Near Field Communication (NFC). |
| `http://tizen.org/feature/network.push`  | `bool` | The platform returns `true` for this key, if the device supports the IP push service provided by the Tizen reference implementation. |
| `http://tizen.org/feature/network.secure_element` | `bool` | The platform returns `true` for this key, if the device supports secure elements. |
| `http://tizen.org/feature/network.secure_element.ese` | `bool` | The platform returns `true` for this key, if the device supports eSE secure elements. |
| `http://tizen.org/feature/network.secure_element.uicc` | `bool` | The platform returns `true` for this key, if the device supports UICC secure elements. |
| `http://tizen.org/feature/network.service_discovery.dnssd` | `bool` | The platform returns `true` for this key, if the device supports the DNS-based Service Discovery Feature (DNSSD). |
| `http://tizen.org/feature/network.service_discovery.ssdp` | `bool` | The platform returns `true` for this key, if the device supports the Simple Service Discovery Protocol feature (SSDP). |
| `http://tizen.org/feature/network.telephony` | `bool` | The platform returns `true` for this key, if the device supports telephony. |
| `http://tizen.org/feature/network.telephony.mms` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.telephony` key, if the device supports MMS. |
| `http://tizen.org/feature/network.telephony.service.cdma` | `bool` | The platform returns `true` for this key, if the device supports the CDMA service. |
| `http://tizen.org/feature/network.telephony.service.edge` | `bool` | The platform returns `true` for this key, if the device supports the EDGE service. |
| `http://tizen.org/feature/network.telephony.service.gprs` | `bool` | The platform returns `true` for this key, if the device supports the GPRS service. |
| `http://tizen.org/feature/network.telephony.service.gsm` | `bool` | The platform returns `true` for this key, if the device supports the GSM service. |
| `http://tizen.org/feature/network.telephony.service.hsdpa` | `bool` | The platform returns `true` for this key, if the device supports the HSDPA service. |
| `http://tizen.org/feature/network.telephony.service.hspa` | `bool` | The platform returns `true` for this key, if the device supports the HSPA service. |
| `http://tizen.org/feature/network.telephony.service.hsupa` | `bool` | The platform returns `true` for this key, if the device supports the HSUPA service. |
| `http://tizen.org/feature/network.telephony.service.lte` | `bool` | The platform returns `true` for this key, if the device supports the LTE service. |
| `http://tizen.org/feature/network.telephony.service.umts` | `bool` | The platform returns `true` for this key, if the device supports the UMTS service. |
| `http://tizen.org/feature/network.telephony.sms` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.telephony` key, if the device supports SMS. |
| `http://tizen.org/feature/network.telephony.sms.cbs` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.telephony` key, if the device supports the cell broadcast service (CBS) for SMS. |
| `http://tizen.org/feature/network.tethering` | `bool` | The platform returns `true` for this key, if the device supports any kind of tethering. |
| `http://tizen.org/feature/network.tethering.bluetooth` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.tethering` key, if the device supports tethering over Bluetooth. |
| `http://tizen.org/feature/network.tethering.usb` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.tethering` key, if the device supports tethering over USB connection. |
| `http://tizen.org/feature/network.tethering.wifi` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.tethering` key, if the device supports tethering over Wi-Fi. |
| `http://tizen.org/feature/network.tethering.wifi.direct` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.tethering` key, if the device supports tethering over Wi-Fi Direct. |
| `http://tizen.org/feature/network.vpn`   | `bool` | The platform returns `true` for this key, if the device supports the Virtual Private Network feature (VPN). |
| `http://tizen.org/feature/network.wifi`  | `bool` | The platform returns `true` for this key, if the device supports all APIs which require Wi-Fi. |
| `http://tizen.org/feature/network.wifi.direct` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.wifi` key, if the device supports Wi-Fi Direct&reg;. |
| `http://tizen.org/feature/network.wifi.direct.display` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.wifi` key, if the device supports Wi-Fi Direct display feature. |
| `http://tizen.org/feature/network.wifi.direct.service_discovery` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/network.wifi` key, if the device supports Wi-Fi Direct service discovery. |
| `http://tizen.org/feature/network.wifi.tdls` | `bool` | The platform returns `true` for this key, if the device supports the Wi-Fi Tunneled Direct Link Setup (TDLS). |

The following table lists the OAuth 2.0 feature keys.

<a name="oauth2"></a>
**Table: OAuth 2.0 feature keys**  

| Key                               | Type   | Description                              |
|-----------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/oauth2` | `bool` | The platform returns `true` for this key, if the device supports the OAuth 2.0 API. |

The following table lists the OpenGL&reg; ES feature keys.

<a name="opengl"></a>
**Table: OpenGL&reg; ES feature keys**

| Key                                      | Type     | Description                              |
| ---------------------------------------- | -------- | ---------------------------------------- |
| `http://tizen.org/feature/opengles`      | `bool`   | The platform returns `true` for this key, if the device supports any OpenGL&reg; ES version and any texture format. |
| `http://tizen.org/feature/opengles.texture_format` | `String` | The platform returns `true` for this key, if the device supports any OpenGL&reg; ES or compressed texture format.<br>If the device supports no formats, the platform returns an empty string for this key. |
| `http://tizen.org/feature/opengles.texture_format.3dc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the 3DC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.texture_format.atc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the ATC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.texture_format.etc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the ETC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.texture_format.ptc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the PTC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.texture_format.pvrtc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the PVRTC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.texture_format.utc` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the UTC texture format for OpenGL&reg; ES. |
| `http://tizen.org/feature/opengles.version.1_1` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the OpenGL&reg; ES version 1.1. |
| `http://tizen.org/feature/opengles.version.2_0` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the OpenGL&reg; ES version 2.0. |
| `http://tizen.org/feature/opengles.version.3_0` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the OpenGL&reg; ES version 3.0. |
| `http://tizen.org/feature/opengles.version.3_1` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the OpenGL&reg; ES version 3.1. |
| `http://tizen.org/feature/opengles.version.3_2` | `bool`   | The platform returns `true` for this key and the `http://tizen.org/feature/opengles` key, if the device supports the OpenGL&reg; ES version 3.2. |

The following table lists the platform feature keys.

<a name="platformfeat"></a>
**Table: Platform feature keys**

| Key                                      | Type     | Description                              |
|------------------------------------------|----------|------------------------------------------|
| `http://tizen.org/feature/platform.core.api.version` | `String` | The platform returns the version of the Tizen Core API in the "[Major].[Minor]" format.<br>If a device does not provide the Tizen Core API, it returns an empty string for this key. |
| `http://tizen.org/feature/platform.core.cpu.arch` | `String` | The platform returns the CPU architecture. |
| `http://tizen.org/feature/platform.core.cpu.arch.armv6` | `bool`   | The platform returns `true` for this key, if the device runs on the ARMv6 CPU architecture. |
| `http://tizen.org/feature/platform.core.cpu.arch.armv7` | `bool`   | The platform returns `true` for this key, if the device runs on the ARMv7 CPU architecture. |
| `http://tizen.org/feature/platform.core.cpu.arch.x86` | `bool`   | The platform returns `true` for this key, if the device runs on the x86 CPU architecture. |
| `http://tizen.org/feature/platform.core.cpu.frequency` | `int`    | The platform returns the frequency at which a core CPU is running. |
| `http://tizen.org/feature/platform.core.fpu.arch` | `String` | The platform returns the FPU architecture. |
| `http://tizen.org/feature/platform.core.fpu.arch.sse2` | `bool`   | The platform returns `true` for this key, if the device runs on the SSE2 FPU architecture. |
| `http://tizen.org/feature/platform.core.fpu.arch.sse3` | `bool`   | The platform returns `true` for this key, if the device runs on the SSE3 FPU architecture. |
| `http://tizen.org/feature/platform.core.fpu.arch.ssse3` | `bool`   | The platform returns `true` for this key, if the device runs on the SSSE3 FPU architecture. |
| `http://tizen.org/feature/platform.core.fpu.arch.vfpv2` | `bool`   | The platform returns `true` for this key, if the device runs on the VFPV2 FPU architecture. |
| `http://tizen.org/feature/platform.core.fpu.arch.vfpv3` | `bool`   | The platform returns `true` for this key, if the device runs on the VFPV3 FPU architecture. |
| `http://tizen.org/feature/platform.native.api.version` | `String` | The platform returns the version of the native API in the "[Major].[Minor]" format. |
| `http://tizen.org/feature/platform.native.osp_compatible` | `bool`   | The platform returns `true` for this key, if the device supports the bada compatibility mode. |
| `http://tizen.org/feature/platform.version` | `String` | The platform returns the version of the platform in the "[Major].[Minor].[Patch Version]" format. |
| `http://tizen.org/feature/platform.version.name` | `String` | The platform returns the platform version name. |
| `http://tizen.org/feature/platform.web.api.version` | `String` | The platform returns the version of the Web API in the "[Major].[Minor]" format. |

The following table lists the profile feature keys.

<a name="profile_feat"></a>
**Table: Profile feature keys**  

| Key                                | Type     | Description                              |
|------------------------------------|----------|------------------------------------------|
| `http://tizen.org/feature/profile` | `String` | The platform returns a compliant device profile (such as `"mobile"` or `"wearable"`) for this key. |

The following table lists the screen feature keys.

<a name="screen"></a>
**Table: Screen feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/screen`        | `bool` | The platform returns `true` for this key, if the device has a display screen. |
| `http://tizen.org/feature/screen.always_on.high_color` | `bool` | The platform returns `true` for this key, if the device supports the high color mode Always On Display (AOD) feature. |
| `http://tizen.org/feature/screen.always_on.low_bit_color` | `bool` | The platform returns `true` for this key, if the device supports the low bit color mode Always On Display (AOD) feature. |
| `http://tizen.org/feature/screen.auto_rotation` | `bool` | The platform returns `true` for this key, if the device supports screen auto-rotation. |
| `http://tizen.org/feature/screen.bpp`    | `int`  | The platform returns the number of bits per pixel supported by the device for this key. The value depends on the screen, and is typically 8, 16, 24, or 32. |
| `http://tizen.org/feature/screen.coordinate_system.size.large` | `bool` | The platform returns `true` for this key, if the device supports the large screen size for the coordinate system. |
| `http://tizen.org/feature/screen.coordinate_system.size.normal` | `bool` | The platform returns `true` for this key, if the device supports the normal screen size for the coordinate system. |
| `http://tizen.org/feature/screen.dpi`    | `int`  | The platform returns the number of dots per inch supported by the device for this key. |
| `http://tizen.org/feature/screen.height` | `int`  | The platform returns the height of the screen in pixels supported by the device for this key. |
| `http://tizen.org/feature/screen.output.hdmi` | `bool` | The platform returns `true` for this key, if the device supports HDMI output. |
| `http://tizen.org/feature/screen.output.rca` | `bool` | The platform returns `true` for this key, if the device supports RCA output. |
| `http://tizen.org/feature/screen.shape.circle` | `bool` | The platform returns `true` for this key, if the device supports a circular screen shape. |
| `http://tizen.org/feature/screen.shape.rectangle` | `bool` | The platform returns `true` for this key, if the device supports a rectangular screen shape. |
| `http://tizen.org/feature/screen.size.all` | `bool` | The platform always returns `true`, if the device supports any screen sizes and resolutions. |
| `http://tizen.org/feature/screen.size.large` | `bool` | The platform returns `true` for this key, if the device supports the large screen size. |
| `http://tizen.org/feature/screen.size.normal` | `bool` | The platform always returns `false` for this key. |
| `http://tizen.org/feature/screen.size.normal.240.400` | `bool` | The platform returns `true` for this key, if the device supports the 240 x 400 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.320.320` | `bool` | The platform returns `true` for this key, if the device supports the 320 x 320 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.320.480` | `bool` | The platform returns `true` for this key, if the device supports the 320 x 480 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.360.360` | `bool` | The platform returns `true` for this key, if the device supports the 360 x 360 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.360.480` | `bool` | The platform returns `true` for this key, if the device supports the 360 x 480 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.480.800` | `bool` | The platform returns `true` for this key, if the device supports the 480 x 800 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.540.960` | `bool` | The platform returns `true` for this key, if the device supports the 540 x 960 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.600.1024` | `bool` | The platform returns `true` for this key, if the device supports the 600 x 1024 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.720.1280` | `bool` | The platform returns `true` for this key, if the device supports the 720 x 1280 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.size.normal.1080.1920` | `bool` | The platform returns `true` for this key, if the device supports the 1080 x 1290 resolution for the normal screen size.<br>The platform can return `true` for multiple resolution keys. |
| `http://tizen.org/feature/screen.width`  | `int`  | The platform returns the width of the screen in pixels supported by the device for this key. |

The following table lists the sensor feature keys.

<a name="sensor"></a>
**Table: Sensor feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/sensor.accelerometer` | `bool` | The platform returns `true` for this key, if the device supports the acceleration sensor. |
| `http://tizen.org/feature/sensor.accelerometer.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.accelerometer` key, if the device supports the wake-up operation by the acceleration sensor. |
| `http://tizen.org/feature/sensor.activity_recognition` | `bool` | The platform returns `true` for this key, if the device supports the activity recognition. |
| `http://tizen.org/feature/sensor.barometer` | `bool` | The platform returns `true` for this key, if the device supports the barometer sensor. |
| `http://tizen.org/feature/sensor.barometer.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.barometer` key, if the device supports the wake-up operation by the barometer sensor. |
| `http://tizen.org/feature/sensor.geomagnetic_rotation_vector` | `bool` | The platform returns `true` for this key, if the device supports the geomagnetic-based rotation vector sensor. |
| `http://tizen.org/feature/sensor.gesture_recognition` | `bool` | The platform returns `true` for this key, if the device supports the gesture recognition. |
| `http://tizen.org/feature/sensor.gravity` | `bool` | The platform returns `true` for this key, if the device supports the gravity sensor. |
| `http://tizen.org/feature/sensor.gyroscope` | `bool` | The platform returns `true` for this key, if the device supports the gyro sensor. |
| `http://tizen.org/feature/sensor.gyroscope_rotation_vector` | `bool` | The platform returns `true` for this key, if the device supports the gyroscope-based rotation vector sensor. |
| `http://tizen.org/feature/sensor.gyroscope.uncalibrated` | `bool` | The platform returns `true` for this key, if the device supports the uncalibrated gyroscope sensor. |
| `http://tizen.org/feature/sensor.gyroscope.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.gyroscope` key, if the device supports the wake-up operation by the gyro sensor. |
| `http://tizen.org/feature/sensor.heart_rate_monitor` | `bool` | The platform returns `true` for this key, if the device supports the heart rate monitor. |
| `http://tizen.org/feature/sensor.heart_rate_monitor.led_green` | `bool` | The platform returns `true` for this key, if the device supports the LED green sensor of the heart rate monitor. |
| `http://tizen.org/feature/sensor.heart_rate_monitor.led_ir` | `bool` | The platform returns `true` for this key, if the device supports the LED infrared sensor of the heart rate monitor. |
| `http://tizen.org/feature/sensor.heart_rate_monitor.led_red` | `bool` | The platform returns `true` for this key, if the device supports the LED red sensor of the heart rate monitor. |
| `http://tizen.org/feature/sensor.humidity` | `bool` | The platform returns `true` for this key, if the device supports the humidity sensor. |
| `http://tizen.org/feature/sensor.linear_acceleration` | `bool` | The platform returns `true` for this key, if the device supports the linear acceleration sensor. |
| `http://tizen.org/feature/sensor.magnetometer` | `bool` | The platform returns `true` for this key, if the device supports the magnetic sensor. |
| `http://tizen.org/feature/sensor.magnetometer.uncalibrated` | `bool` | The platform returns `true` for this key, if the device supports the uncalibrated geomagnetic sensor. |
| `http://tizen.org/feature/sensor.magnetometer.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.magnetometer` key, if the device supports the wake-up operation by the magnetic sensor. |
| `http://tizen.org/feature/sensor.pedometer` | `bool` | The platform returns `true` for this key, if the device supports the pedometer. |
| `http://tizen.org/feature/sensor.photometer` | `bool` | The platform returns `true` for this key, if the device supports the photo (light) sensor. |
| `http://tizen.org/feature/sensor.photometer.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.photometer` key, if the device supports the wake-up operation by the photo sensor. |
| `http://tizen.org/feature/sensor.proximity` | `bool` | The platform returns `true` for this key, if the device supports the proximity sensor. |
| `http://tizen.org/feature/sensor.proximity.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.proximity` key, if the device supports the wake-up operation by the proximity sensor. |
| `http://tizen.org/feature/sensor.rotation_vector` | `bool` | The platform returns `true` for this key, if the device supports the rotation vector sensor. |
| `http://tizen.org/feature/sensor.significant_motion` | `bool` | The platform returns `true` for this key, if the device supports the significant motion sensor which detects any significant movements caused by changes in the user location. |
| `http://tizen.org/feature/sensor.sleep_monitor` | `bool` | The platform returns `true` for this key, if the device supports the sleep monitor sensor or the sleep detector sensor which tracks and detects the human sleep state. |
| `http://tizen.org/feature/sensor.stress_monitor` | `bool` | The platform returns `true` for this key, if the device supports the stress monitor which tracks the human stress level. |
| `http://tizen.org/feature/sensor.temperature` | `bool` | The platform returns `true` for this key, if the device supports the temperature sensor. |
| `http://tizen.org/feature/sensor.tiltmeter` | `bool` | The platform returns `true` for this key, if the device supports the tilt sensor. |
| `http://tizen.org/feature/sensor.tiltmeter.wakeup` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/sensor.tiltmeter` key, if the device supports the wake-up operation by the tilt sensor. |
| `http://tizen.org/feature/sensor.ultraviolet` | `bool` | The platform returns `true` for this key, if the device supports the ultraviolet sensor. |
| `http://tizen.org/feature/sensor.wrist_up` | `bool` | The platform returns `true` for this key, if the device supports the wrist up action. |

The following table lists the shell feature keys.

<a name="shell"></a>
**Table: Shell feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/shell.appwidget` | `bool` | The platform returns `true` for this key, if the device supports the AppWidget. |

The following table lists the sip feature keys.

<a name="sip"></a>
**Table: Sip feature keys**  

| Key                                 | Type   | Description                              |
|-------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/sip.voip` | `bool` | The platform returns `true` for this key, if the device supports the Voice over Internet Protocol (VoIP). |

The following table lists the speech feature keys.

<a name="speech"></a>
**Table: Speech feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/speech.control` | `bool` | The platform returns `true` for this key, if the device supports voice control. |
| `http://tizen.org/feature/speech.recognition` | `bool` | The platform returns `true` for this key, if the device supports speech recognition (STT). |
| `http://tizen.org/feature/speech.synthesis` | `bool` | The platform returns `true` for this key, if the device supports speech synthesis (TTS). |

The following table lists the system setting feature keys.

<a name="systemsetting"></a>
**Table: System setting feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/systemsetting` | `bool` | The platform returns `true` for this key, if the device supports the SystemSetting API. |
| `http://tizen.org/feature/systemsetting.home_screen` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/systemsetting` key, if the device supports a way to change or get the picture on the home screen. |
| `http://tizen.org/feature/systemsetting.incoming_call` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/systemsetting` key, if the device supports a way to change or get a ringtone for all incoming calls. |
| `http://tizen.org/feature/systemsetting.lock_screen` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/systemsetting` key, if the device supports a way to change or get the lock screen wallpaper. |
| `http://tizen.org/feature/systemsetting.notification_email` | `bool` | The platform returns `true` for this key and the `http://tizen.org/feature/systemsetting` key, if the device supports a way to change or get a ringtone for all email notifications. |

The following table lists the USB feature keys.

<a name="usb"></a>
**Table: USB feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/usb.accessory` | `bool` | The platform returns `true` for this key, if the device supports the USB client or accessory mode. |
| `http://tizen.org/feature/usb.host`      | `bool` | The platform returns `true` for this key, if the device supports the USB host mode. |

The following table lists the vision feature keys.

<a name="vision"></a>
**Table: Vision feature keys**  

| Key                                      | Type   | Description                              |
|------------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/vision.barcode_detection` | `bool` | The platform returns `true` for this key, if the device supports the barcode detection feature. |
| `http://tizen.org/feature/vision.barcode_generation` | `bool` | The platform returns `true` for this key, if the device supports the barcode generation feature. |
| `http://tizen.org/feature/vision.face_recognition` | `bool` | The platform returns `true` for this key, if the device supports face recognition. |
| `http://tizen.org/feature/vision.image_recognition` | `bool` | The platform returns `true` for this key, if the device supports image recognition. |
| `http://tizen.org/feature/vision.qrcode_generation` | `bool` | The platform returns `true` for this key, if the device supports QR code generation. |
| `http://tizen.org/feature/vision.qrcode_recognition` | `bool` | The platform returns `true` for this key, if the device supports QR code recognition. |

The following table lists the Web feature keys.

<a name="web"></a>
**Table: Web feature keys**  

| Key                                    | Type   | Description                              |
|----------------------------------------|--------|------------------------------------------|
| `http://tizen.org/feature/web.ime`     | `bool` | The platform returns `true` for this key, if the device supports Web IME. |
| `http://tizen.org/feature/web.service` | `bool` | The platform returns `true` for this key, if the device supports the Web service model. |

<a name="system"></a>
## System Keys

The following table lists the build system keys.

<a name="build"></a>
**Table: Build system keys**  

| Key                                      | Type     | Description                              |
|------------------------------------------|----------|------------------------------------------|
| `http://tizen.org/system/build.date`     | `String` | The platform returns the build date. The build date is made when the platform image is created. |
| `http://tizen.org/system/build.id`       | `String` | The platform returns the build ID. The build ID is made when the platform image is created. |
| `http://tizen.org/system/build.string`   | `String` | The platform returns the build information string. The build information string is made when the platform image is created. |
| `http://tizen.org/system/build.time`     | `String` | The platform returns the build time. The build time is made when the platform image is created. |
| `http://tizen.org/system/build.type`     | `String` | The platform returns the build type, such as `"user"` or `"eng"`. The build type is made when the platform image is created. |
| `http://tizen.org/system/build.variant`  | `String` | The platform returns the variant release information. The variant release information is made when the platform image is created. |
| `http://tizen.org/system/build.release` | `String` | The platform returns the build version information. The build version information is made when the platform image is created. |

The following table lists the manufacturer keys.

<a name="manufacturer"></a>
**Table: Manufacturer keys**  

| Key                                    | Type     | Description                              |
|----------------------------------------|----------|------------------------------------------|
| `http://tizen.org/system/manufacturer` | `String` | The platform returns the manufacturer name. |

The following table lists the model name system keys.

<a name="modelname"></a>
**Table: Model name system keys**  

| Key                                  | Type     | Description                              |
|--------------------------------------|----------|------------------------------------------|
| `http://tizen.org/system/model_name` | `String` | The platform returns the device model name. |

The following table lists the platform system keys.

<a name="platformsys"></a>
**Table: Platform system keys**  

| Key                                      | Type     | Description                              |
|------------------------------------------|----------|------------------------------------------|
| `http://tizen.org/system/platform.communication_processor` | `String` | The platform returns the device communication processor name. |
| `http://tizen.org/system/platform.name`  | `String` | The platform returns the platform name.  |
| `http://tizen.org/system/platform.processor` | `String` | The platform returns the device processor name. |

The following table lists the sound system keys.

<a name="sound"></a>
**Table: Sound system keys**  

| Key                                      | Type  | Description                              |
|------------------------------------------|-------|------------------------------------------|
| `http://tizen.org/system/sound.media.volume.resolution.max` | `int` | The platform returns the maximum sound volume level of the media category. |
| `http://tizen.org/system/sound.notification.volume.resolution.max` | `int` | The platform returns the maximum sound volume level of the notification category. |
| `http://tizen.org/system/sound.ringtone.volume.resolution.max` | `int` | The platform returns the maximum sound volume level of the ringtone category. |
| `http://tizen.org/system/sound.system.volume.resolution.max` | `int` | The platform returns the maximum sound volume level of the system category. |

The following table lists the TizenID system keys.

<a name="tizenid"></a>
**Table: TizenID system keys**  

| Key                               | Type     | Description                              |
|-----------------------------------|----------|------------------------------------------|
| `http://tizen.org/system/tizenid` | `String` | The platform returns TizenID. TizenID is a value that is generated based on the pseudo-random generator. |

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
