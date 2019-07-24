# Tizen 2.3.2 for Wearable

## SDK Release Notes

### Tizen 2.3.2 Patch (Dec. 23, 2016)

The OPR (on pixel rate) check function is included in the 2.3.2 wearable profile. You can check the OPR of your watch in advance through this function.

#### openssl Upgrade

- openssl has been upgraded to 1.0.1u.
- The following risky SSLv2-related APIs have been removed:
  `SSLv2_method()`, `SSLv2_client_method()`, `SSLv2_server_method()`



### Tizen 2.3.2 (Sep. 1, 2016)

#### Wearable Web Widget Engine

New and Changed Features

- Rendering engine
  - HTML elements and global attributes
    - 13 HTML elements (including the DOCTYPE declaration) and 4 global attributes have been added. In addition, the Widget engine supports only HTML5 documents.
  - CSS properties
    - CSS properties have been added to provide a minimal specification, with a sufficient subset of Web standards.
  - DOM APIs
    - DOM APIs have been added to provide a programming interface for HTML documents.
    - XMLHttpRequest APIs have been added to provide client functionality for exchanging data with a server.
    - Device APIs have been added to allow you to create widget applications that interact with the device hardware.
  - W3C test suites
    - W3C Web platform test suites have been added.
    - DOM conformance test suites have been added.
    - Vendor test suites have been added, including test suites for major browsers, such as Google Chrome&trade;, Safari, and Firefox.
  - Javascript API
    - `console.log()` method has been added for debugging a Web widget.

#### Web Framework

##### New and Changed Features

- Web Device API
  - WidgetService API has been added to the Web Device API.
  - Support for Datacontrol has been added:
    - Provides interfaces and methods for accessing specific data exported by other applications.
  - Support for Preference has been added:
    - Provides interfaces and methods to store and retrieve small pieces of data used as application preferences.
  - Some APIs have been added:
    - Human activity monitor:
      - Supports activity recognition.
      - Adds an interval for the power consumption issue.
      - Adds an `UNKNOWN` type in the Pedometer step status.
      - Adds the Human Activity Recorder.
    - Sensor:
      - Adds sensor hardware information.
      - Adds the `batchLatency` parameter to the `setChangeListener()` method.
      - Supports the gravity, gyroscope, and gyroscope rotation vector sensor types.
      - Adds an interval for the power consumption issue.
    - Screen:
      - Adds new screen feature keys `http://tizen.org/feature/screen.always_on.low_bit_color` and `http://tizen.org/feature/screen.always_on.high_color` which can distinguish whether an always on display (AOD) is high-bit color or low-bit color. These feature keys can be read using the System Info API to determine whether the device supports high-bit color or low-bit color.
- W3C
  - Support has been added for WebSpeech recognition:
    - Unsupported attributes:
      - `SpeechRecognition.serviceURL`
      - `SpeechRecognitionEvent.interpretation`
- Web UI Framework (TAU)
  - Tizen 2.3.2 theme has been applied:
    - Changed component styles:
      - Popup, Button, Checkbox, Radio, Toggle, Selector, and Page Indicator
      - Multi text list sample, thumbnail list sample
      - List animation enabled in all samples (`circle-helper.js`)

#### Service Framework

##### New and Changed Features

- Sensor
  - Sensor Recorder APIs have been added.
  - Reference coordinate system selection support has been added.
- Location
  - Map Service
    - Map meta-data (query to search) APIs have been added.
    - Map widget (rendering map view) APIs have been added.
    - New feature key for the Map Service has been added.
    - New API to check for consent has been added.
    - New error code, `MAPS_ERROR_USER_NOT_CONSENTED`, meaning that the user has not consented yet, has been added.
- Location
  - Location Batch APIs have been added.

#### Native UI Framework

##### New and Changed Features

- Elementary widget
  - Tizen 2.3.2 UX has been implemented.
- Text input
  - Input Delegator based on the application control has been added.
- Voice interaction
  - Speech-to-text engine has been added by default.

#### System / Base

##### New and Changed Features

- Base-utils (i18n)
  - MeasureUnit APIs have been added.
  - AlphabeticIndex APIs have been added.
- ICU upgrade
  - Version has been upgraded from 51.1 to 57.1.