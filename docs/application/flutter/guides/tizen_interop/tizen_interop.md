# [tizen_interop](https://github.com/flutter-tizen/tizen_interop)

Provides Dart bindings for Tizen native APIs, powered by [ffigen](https://pub.dev/packages/ffigen).


## Usage

To use this package, add `ffi` and `tizen_interop` as dependencies in your `pubspec.yaml` file.

```yaml
dependencies:
  ffi: ^2.0.1
  tizen_interop: ^0.4.1
```

Then, import `package:ffi/ffi.dart` and `package:tizen_interop/[TIZEN_VERSION]/tizen.dart` in your Dart code.

```dart
import 'package:ffi/ffi.dart';
import 'package:tizen_interop/6.0/tizen.dart';
```

### Examples

```dart
// Getting a string value from the Native API.
// Prefer using `arena` to allocate memory because it frees the memory
// automatically when the `using` block ends.
String appName = using((Arena arena) {
  Pointer<Pointer<Char>> ppStr = arena();
  if (tizen.app_get_name(ppStr) == 0) {
    // The memory allocated by the Native API must be freed by the caller.
    arena.using(ppStr.value, calloc.free);
    return ppStr.value.toDartString();
  }
  return 'unknown';
});

// Passing a string value to the Native API.
// The memory allocated by the `toNativeChar` method must be freed by
// the caller. The `arena` allocator will free it automatically.
using((Arena arena) {
  Pointer<Char> pKey =
      'tizen_interop_test_key_for_int'.toNativeChar(allocator: arena);
  tizen.preference_set_int(pKey, 100);
});

// Getting an integer value from the Native API.
int preferenceValue = using((Arena arena) {
  Pointer<Char> pKey =
      'tizen_interop_test_key_for_int'.toNativeChar(allocator: arena);
  Pointer<Int> pValue = arena();
  if (tizen.preference_get_int(pKey, pValue) == 0) {
    return pValue.value;
  }
  return 0;
});

// Getting a struct value from the Native API.
int freeMemory = using((Arena arena) {
  Pointer<runtime_memory_info_s> pMemInfo = arena();
  if (tizen.runtime_info_get_system_memory_info(pMemInfo) == 0) {
    return pMemInfo.ref.free;
  }
  return 0;
});

// Both sync and async callbacks are supported as long as they are called on
// the same thread.
tizen.storage_foreach_device_supported(
    Pointer.fromFunction(_storageDevice, false), nullptr);

// Callbacks that are called outside the current thread will cause the error:
// "Cannot invoke native callback outside an isolate".
// See the tizen_interop_callbacks package for a solution.
```


## Supported APIs

This package provides bindings for the following APIs of the Tizen [IoT-Headed](https://docs.tizen.org/application/native/api/iot-headed/latest) (or [Common](https://docs.tizen.org/application/native/api/common/latest) for Tizen 8.0 and above) profile.

> **Note**: UI and WebView related APIs are not included.

| Category | Sub category | Tizen 6.0 | Tizen 6.5 | Tizen 7.0 | Tizen 8.0 | Tizen 9.0 |
|-|-|:-:|:-:|:-:|:-:|:-:|
| Account | Account Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | FIDO Client | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Account Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | OAuth 2.0 | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Sync Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| Application Framework | Application | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Alarm | ✔ | ✔ | ✔ | ✔ | ✔ |
| | App Common | ✔ | ✔ | ✔ | ✔ | ✔ |
| | App Control | ✔ | ✔ | ✔ | ✔ | ✔ |
| | App Control URI  | | ✔ | ✔ | ✔ | ✔ |
| | Event | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Internationalization | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Job scheduler | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Preference | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Resource Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Application Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Attach panel |
| | Badge | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Bundle | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Cion  | | ✔ | ✔ | ✔ | ✔ |
| | Component Based Application |
| | Component Manager |
| | Data Control | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Message Port | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Notification | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Notification EX | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Package Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | RPC Port | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Service Application | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Shortcut | ✔ | ✔ | | | ✔ |
| | Tizen Core | | | | | ✔ |
| | Widget |
| Base | Common Error | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Utils |
| Content | Download | ✔ | ✔ | ✔ | ✔ | ✔ |
| | MIME Type | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Content | ✔ | ✔ | ✔ | ✔ | ✔ |
| Context | Activity Recognition | ✔ | | | | |
| | Contextual History | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Contextual Trigger | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Gesture Recognition | ✔ | | | | |
| Location | Geofence Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Location Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Maps Service |
| Machine Learning | Pipeline  | | ✔ | ✔ | ✔ | ✔ |
| | Service | | | ✔ | ✔ | ✔ |
| | Single  | | ✔ | ✔ | ✔ | ✔ |
| | Trainer  | | ✔ | ✔ | ✔ | ✔ |
| Messaging | Email | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Messages | | | | |
| | Push | ✔ | ✔ | ✔ | ✔ | ✔ |
| Multimedia | Audio I/O | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Camera | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Image Util | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Codec | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Controller | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Demuxer | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Muxer | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Streamer | ✔ | ✔ | ✔ | ✔ | |
| | Media Tool | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Vision | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media Editor | | | ✔ | ✔ | ✔ |
| | Metadata Editor | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Metadata Extractor | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Player | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Radio | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Recorder | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Screen Mirroring | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Sound Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Sound Pool | ✔ | ✔ | ✔ | ✔ | ✔ |
| | StreamRecorder | ✔ | ✔ | ✔ | ✔ | |
| | Thumbnail Util | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Tone Player | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Video Util | | | | | |
| | WAV Player | ✔ | ✔ | ✔ | ✔ | ✔ |
| | WebRTC  | | ✔ | ✔ | ✔ | ✔ |
| Network | Application Service Platform | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Bluetooth | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Connection | ✔ | ✔ | ✔ | ✔ | ✔ |
| | DNSSD | ✔ | ✔ | ✔ | ✔ | ✔ |
| | HTTP | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Intelligent Network Monitoring | ✔ | ✔ | ✔ | ✔ | ✔ |
| | IoTCon | ✔ | ✔ | ✔ | ✔ | ✔ |
| | MTP | ✔ | ✔ | ✔ | ✔ | ✔ |
| | NFC | | | | | ✔ |
| | SSDP | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Smart Traffic Control | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Smartcard | | | | | |
| | SoftAP | ✔ | ✔ | ✔ | ✔ | ✔ |
| | User Awareness |
| | VPN Service | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Wi-Fi | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Wi-Fi Aware | | | | | ✔ |
| | Wi-Fi Direct | ✔ | ✔ | ✔ | ✔ | ✔ |
| Security | CSR | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Device Certificate Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Device Policy Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Key Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Key Manager Extened | | | | | ✔ |
| | Privacy Privilege Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Privilege Info | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Web Authentication | | | | | ✔ |
| | YACA | ✔ | ✔ | ✔ | ✔ | ✔ |
| Social | Calendar | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Contacts | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Phonenumber utils | ✔ | ✔ | ✔ | ✔ | ✔ |
| System | Device | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Diagnostics | | | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Dlog | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Feedback | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Media key | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Monitor | | | ✔ | ✔ | ✔ |
| | Peripheral IO | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Runtime information | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Sensor | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Storage | ✔ | ✔ | ✔ | ✔ | ✔ |
| | System Information | ✔ | ✔ | ✔ | ✔ | ✔ |
| | System Settings | ✔ | ✔ | ✔ | ✔ | ✔ |
| | T-trace | ✔ | ✔ | ✔ | ✔ | ✔ |
| | USB Host | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Update Control | ✔ | ✔ | ✔ | ✔ | ✔ |
| Telephony | Telephony Information | | | | | |
| UI | Clipboard History Manager | ✔ | ✔ | ✔ | | |
| | DALi |
| | EFL |
| | External Output Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Minicontrol |
| | TBM Surface | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Tizen WS Shell |
| | UI View Manager |
| UIX | Autofill | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Input Method | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Input Method Manager | ✔ | ✔ | ✔ | ✔ | ✔ |
| | MMI | | | | | ✔ |
| | Multi assistant | ✔ | ✔ | ✔ | ✔ | ✔ |
| | STT | ✔ | ✔ | ✔ | ✔ | ✔ |
| | STT Engine | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Sticker |
| | TTS | ✔ | ✔ | ✔ | ✔ | ✔ |
| | TTS Engine | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Voice control | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Voice control elementary | ✔ |
| | Voice control engine | ✔ | ✔ | ✔ | ✔ | ✔ |
| | Voice control manager | ✔ | ✔ | ✔ | ✔ | ✔ |
