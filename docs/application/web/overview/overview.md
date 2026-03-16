# Tizen Web API Overview

Tizen Web API provides a robust framework for developing web-based applications on the Tizen platform, enabling access to device-specific features and functionalities through standardized web technologies. With Tizen Web API, developers can create rich applications using HTML5, CSS, and JavaScript for a variety of devices.

## What is Tizen Web API?

Tizen Web API is a comprehensive set of JavaScript interfaces that allow web applications to interact with Tizen's native subsystems and device capabilities. It extends standard web technologies with device-specific functionality, enabling developers to create applications that can:

- Access device hardware (sensors, Bluetooth, NFC, etc.)
- Manage application lifecycle and inter-app communication
- Store and retrieve data locally
- Play multimedia content
- Send and receive messages
- Control device settings
- Leverage machine learning capabilities

The Tizen Web Device API, based on JavaScript, provides you advanced access to the device's platform capabilities.
The W3C/HTML5 and Supplementaries API is built on top of the latest HTML5, CSS3, and ECMAScript standards, ensuring cross-platform compatibility while providing access to platform-specific features.

## API Modules

Tizen Web API is organized into functional modules, each providing specific capabilities. The availability of certain modules depends on the device profile and hardware capabilities.

### Base APIs
Core functionality used across the Tizen platform:
- **File System API:** File and directory management
- **Archive API:** ZIP archive creation and manipulation
- **Filter API:** Query filters and sorting modes
- **Error Handling:** Standardized error interfaces

### Application Framework
Manage application lifecycle and inter-app communication:
- **Alarm API:** Schedule application execution at specific times
- **Application API:** Control other applications, retrieve app information
- **Package API:** Package installation, update, and management
- **Application Controls:** Launch other applications with specific actions
- **Message Port API:** Inter-application communication
- **Data Control API:** Secure data sharing between applications

### Connectivity APIs
Connect and communicate with other devices and networks:
- **Bluetooth API:** Device discovery, pairing, and data transfer
- **NFC API:** Near Field Communication for tag reading and peer-to-peer
- **IoTCon API:** IoT connectivity and resource management
- **Network Bearer Selection API:** Network connection management
- **Download API:** File download from the Internet
- **Secure Element API:** Access secure elements (e.g., SIM cards)

### Content & Multimedia
Work with multimedia content and playback:
- **Content API:** Search and manage media files
- **Exif API:** Manipulate EXIF data in JPEG images
- **Metadata API:** Extract media metadata
- **Media Key API:** Media playback control
- **Media Controller API:** Advanced media playback management
- **Player Util API:** Player utility functions
- **Sound API:** Audio playback and management

### Messaging
Send and receive messages and notifications:
- **Push API:** Receive push notifications from servers

### Device APIs
Access device hardware and system information:
- **System Info API:** Device capabilities and properties
- **Power API:** Power state and resource management
- **Time API:** Date, time, and calendar functions
- **System Setting API:** Device system settings
- **Web Setting API:** Web view configuration
- **Feedback API:** Haptic and audio feedback
- **Input Device API:** Input device management
- **Sensor API:** Access device sensors (accelerometer, gyroscope, etc.)
- **Human Activity Monitor API:** Track physical activities (walking, running, etc.)
- **Badge API:** Application badge management

### Security APIs
Secure data storage and access:
- **Key Manager API:** Secure key storage and management
- **Secure Element API:** Access to secure hardware elements
- **Privacy Privilege Manager API:** Privacy settings management

### User Interface APIs
Create rich user interfaces and interactions:
- **Voice Control API:** Voice command recognition and control
- **Notification API:** Display notifications and alerts
- **Widget Service API:** Widget management

### Data Management APIs
Store and manage application data:
- **Preference API:** Key-value data storage
- **File System API:** File and directory operations
- **Archive API:** ZIP archive management
- **Data Control API:** Secure inter-application data sharing

### PIM (Personal Information Management)
Manage personal data:
- **Contact API:** Contact information management
- **Calendar API:** Calendar events and tasks
- **Account API:** Account synchronization and management

### Machine Learning APIs
Implement machine learning features:
- **Machine Learning API:** Pipeline-based inference
- **ML Single API:** Single model inference
- **ML Trainer API:** Model training capabilities

### Cordova APIs
Apache Cordova compatibility layer:
- **File:** File system operations
- **File Transfer:** Upload and download files
- **Media:** Audio recording and playback
- **Device:** Device information
- **Network Information:** Network status
- **Dialogs:** Native dialog boxes
- **Globalization:** Locale-specific operations
- **Events:** Application lifecycle events

### TV Controls
- **TVAudioControl API:** Volume and audio settings
- **TVDisplayControl API:** Display settings and 3D mode
- **TVInfo API:** TV information and status
- **TVInputDevice API:** Input device and remote control
- **TVWindow API:** Picture-in-picture window management

## UI Framework

Tizen provides a comprehensive UI framework with pre-built components optimized for each device profile:

### Animations & Gestures
- **Animation API:** Smooth CSS and JavaScript animations
- **Gesture Events API:** Touch gesture recognition (swipe, pinch, etc.)

### Globalization
Locale and region-specific features:
- Date and time formatting
- Number and currency formatting
- Text direction and layout

## Application Filtering
Applications can specify target devices and capabilities:
- Device profiles (mobile, wearable, TV)
- API version requirements
- Feature requirements (e.g., Bluetooth, GPS)
- Screen size and resolution

### Mandatory APIs
Always available on all Tizen devices supporting the specified API version. These core APIs include:
- File System
- Application Framework (basic features)
- System Info (basic capabilities)
- Error Handling

### Optional APIs
Provide functionality that depends on device hardware or software capabilities. Examples include:
- Bluetooth API (requires Bluetooth hardware)
- NFC API (requires NFC hardware)
- Sensor API (requires specific sensors)
- TV Controls (TV profile only)

Always check for optional API availability using `tizen.systeminfo.getCapability()` before use.

**Documentation:** [TV Web Device API Reference](../api/latest/device_api/tv/index.html)

## Related Documentation

### API References
- [TV Web Device API](../api/latest/device_api/tv/index.html)

### Guides
In-depth guides for major features:
- [Application Management](../guides/app-management/overview.md)
- [Connectivity](../guides/connectivity/connectivity.md)
- [Data Storage](../guides/data/data.md)
- [Device Settings](../guides/device/device.md)
- [Security](../guides/security/security.md)
- [Multimedia](../guides/multimedia/overview.md)
