# Running Applications on the Emulator
# Dependencies

- Tizen Studio 1.0 and Higher


The Tizen emulator is a tool that reduces the inconvenience of testing the application on a real device, by providing an environment similar to a real device. In other words, if you do not have the real device, you can test on a virtual device with similar features.

Using the Emulator Manager, you can create a variety of environments (different device types) and you can preview the problems during the development process. The emulator provides the actual hardware similar to real device controls, and you can check the application features, such as data processing and user scenarios.

The emulator is based on the open source QEMU project and consists of a virtual CPU, memory, and various peripherals. Currently, the Tizen Studio only supports the x86 machine architecture for guest.

You can use the [Emulator Manager](emulator-manager.md) to create and launch a Virtual Machine (emulator) instance. You can communicate with the emulator instance using the [Smart Development Bridge (SDB)](smart-development-bridge.md).

The emulator provides the following main features:

- Full system emulation, including CPU, memory, and peripheral devices
- Event simulation with the [Emulator Control Panel](emulator-control-panel.md)
- Guest operation acceleration using a host CPU or GPU

For more information, see [Supported Features](#supported).

## Running an Application in the Emulator

To use the emulator, you need the Emulator Manager. If you do not have the Emulator Manager, install it through the Tizen Studio Package Manager.

To start the emulator and run an application:

1. Open the [Emulator Manager](emulator-manager.md#access).If you do not have an applicable emulator instance, [create one](emulator-manager.md#create).
2. Select the emulator instance and click **Launch**.
3. Test your application in the emulator. You can launch your application in 2 ways:
   - In the Tizen Studio, select the project and click **Run As**.
   - Drag an application package file (for example, the WGT file) to the emulator to install and launch the application on the emulator.
4. To close the emulator, right-click the emulator and select **Close**, or click and hold the **Power** key.

The emulator device stores the installed application so you can run it again, if needed. To remove the application, you must uninstall it. If you run the project again on the same emulator, the emulator replaces the application with the new version.

In the Emulator Manager, in addition to creating new emulator instances according to the environments you need, you can also [modify and delete emulator instances](emulator-manager.md#manage).

## Increasing the Application Execution Speed

The Tizen x86 emulator exploits [KVM](http://www.linux-kvm.org/page/Main_Page) (Kernel-based Virtual Machine in Linux) or [HAX](../download/hardware-accelerated-execution-manager.md) (Hardware Accelerated eXecution in Windows® and macOS) with HW virtualization support.

If the CPU VT is disabled in the **Emulator Configuration** view on the Emulator Manager, check the following prerequisites and install KVM or HAX:

1. Prerequisites for using HW virtualization:

   - In Ubuntu:

     To use KVM, you need a processor that supports HW virtualization. Both Intel and AMD have developed those extensions for their processors (Intel VT-x/AMD-V). Check whether the CPU supports HW virtualization with the following command:

     ```
     $egrep -c '(vmx|svm)' /proc/cpuinfo
     ```

     If the output of the command is 0, the CPU does not support HW virtualization. Otherwise, it does.

     The HW virtualization feature can also be disabled on the BIOS setting. Check the setting and enable it if you need the feature.

   - In Windows®:

     To use HAX, you need an Intel VT-x-supported CPU, and you must enable the NX-related setting in the PC BIOS.

   - In macOS:

     To use HAX, install EFI-related updates on your Intel-based Mac computer.

     For more information, see [EFI and SMC firmware updates for Intel-based Mac computers](http://support.apple.com/kb/HT1237).

2. Installing KVM or HAX:

   - In Ubuntu:

     No installation is required for KVM.

   - In Windows® and macOS:

     The HAXM driver is installed during the Tizen Studio installation. For more information on installing HAXM, see [Hardware Accelerated Execution Manager](../download/hardware-accelerated-execution-manager.md).

   **Note**
   If the installation fails with a VT-related message, check the CPU feature and BIOS settings. If the installation fails with an NX-related message, enable NX (or PAE and DEP) -related item in the BIOS. In addition, make sure that the operating system supports the NX feature (for more information, see [MSDN](http://msdn.microsoft.com/en-us/library/windows/hardware/ff542275%28v=vs.85%29.aspx)).

   No configuration is required for KVM or HAX.

### Working with the HW Virtualization, Settings, and Help

To run the emulator with the HW virtualization support in the Emulator Manager, set the **CPU VT** field to **ON**. The field is disabled if your system cannot support HW virtualization.

You can also run the emulator with the HW virtualization support from the command line, by including the `-enable-kvm` (in Ubuntu) or `-enable-hax` (in Windows® and macOS) option in the start-up command.

## Supported Features

The emulator provides various virtual HW, media formats, codecs, and [OpenGL® ES acceleration](#opengl). For better performance of the OpenGL® ES support, the Tizen emulator exploits the latest feature of the graphic driver, so always [install the latest vendor-provided graphic driver](../download/prerequisites.md#emulator). The emulator, however, has some limitations and [differences compared to physical target devices](#target).

The following table lists the basic features supported in the emulator.

**Table: Supported emulator features**

| Feature                | Detail                                   | Status                                   | Notes                                    |
| ---------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Skin                   | Skins are fitted to the screen resolution:Mobile:WVGA (480 x 800, default)qHD (540 x 960)HD (720 x 1280)Wearable:320 x 320360 x 360 (default)360 x 4804 orientation modes are supported:Portrait (default), landscape, reverse portrait, and reverse landscape | Supported                                | 2 skin layout types are supported:Profile-specific skinGeneral purpose skin |
| Touch                  | Maru touchscreen device    | Supported             | Multi-touch is supported.                                                          |
| Key                    | HW keys, host keyboard, and SW keypad    |Supported | The host keyboard is not supported for the wearable emulator. |                                          
| Rotary                 | 360 levels of clockwise or counter-clockwise rotation |Supported | -                                                                                  |
| Display                | VGA card with 100 levels of brightness control |   Supported                                       |                                          |
| OpenGL® ES             |   Compatible with OpenGL® ES 1.1 and 2.0OpenGL® ES API pass-through through PCI |Supported |The OpenGL® ES 1.1 functionality is not guaranteed on the emulator, unless the graphics hardware of your computer supports OpenGL® 1.5.The OpenGL® ES 2.0 functionality is not guaranteed on the emulator, unless the graphics hardware of your computer supports OpenGL® 2.1.The host machine must support OpenGL® 1.4.                                           |
| Sound                  | AC97 device                              |Supported | **Audio in:**Make sure that the input volume of the microphone is enough to record your voice or songs on the host machine.On Windows® 7, inject the microphone into the host machine before starting the emulator.**Audio out:**On Windows® 7, enable at least 1 audio out device before starting the emulator. Make sure that the volume icon in the tray is not disabled.While the emulator is running, do not disable the audio out device, as it can lock the audio system of the guest platform.                                           |
| Network connection     | Virtio                                   |Supported  | Raw socket protocol, such as ICMP, is not supported.                                           |
| Emulator Control Panel | The Emulator Control Panel (ECP) supports different features depending on the device profile:Mobile:Device Manager: Device Tree, Network, Host Directory SharingEvent Injector: Battery, RSSI, 3-Axis Sensor, Light, Proximity, Pressure, Ultraviolet, Heart Rate Monitor, Motion, Ear Jack, USB, SDCard, Location, TelephonyWearable:Device Manager: Network, Host Directory SharingApp Manager: UninstallerEvent Injector: Battery, 3-Axis Sensor, Light, Proximity, Pedometer, Pressure, Ultraviolet, Heart Rate Monitor, Gesture, USB |Supported |  The ECP is a standalone tool, which replaces the Event Injector. It helps to control and monitor the emulator features, and can be launched from the emulator context menu.                                           |
| Camera                 | Virtual camera device connecting a host machine's Webcam:Support: preview, capture, and recordImage format: YUYV, I420, and YV12Attributes: brightness and contrastResolution: 160 x 120, 176 x 144, 320 x 240, 352 x 288, and 640 x 480Video resolution: 1280 x 720 for the WVGA, 320 x 240 for the WQVGA, and 640 x 480 for the HVGA devicesSupported video codecs: MPEG-4, H.263, H.264, and VC-1 for both encoding and decoding |Supported |  While recording a video using the emulator, an audio-video synchronization error can occur depending on your computer hardware and performance.                                           |
| Bluetooth              | -                                        | Not supported                            | -                                        |
| Wi-Fi                  | -                                         | Not supported                                          |                                          |
| Wi-Fi Direct®          | -                                         |  Not supported                                         |                                          |

### OpenGL® ES Acceleration Support

For the emulator to support OpenGL® ES acceleration, you need:

- Graphics chipset driver that supports OpenGL® 1.4 installed on the host machine
- All chipset vendors and driver versions available to support the OpenGL® 1.4 standard

**Note**The emulator supports only ES 1.1, ES 2.0, and EGL™ 1.4 versions.

### Differences Between the Emulator and Target

The following tables describe the differences between a real target device and the emulator. For more information, see the detailed differences in:

- [Input system](#input)
- [Graphics and display](#graphics)
- [Virtual sensor](#sensor)
- [Telephony](#telephony)
- [Power management](#power)
- [Supported media formats and codecs](#codec)

**Table: Comparison summary**

| Category                      | Subject                                  | Physical target                          | Emulator                                 |
| ----------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Development environment       | Target                                   | Buy a target device or reference board (by model) | Download the Tizen Studio (multi-profile and multi-model support) |
|  | Network                       | Need Bluetooth                           | Only the network environment                                                       |
|  | Target connection             | USB                                      | IPC (TCP/UDP)                                                                     |
|  | Source and package management | Source and package for target            | Source and package for the emulator                                                |
|  | Host Directory Sharing        | Not supported                            | Supported                                                                          |
| Portability                   | Screen resolution                        | Fixed                                    | Configurable                             |
|  | RAM, storage size             |       Fixed                                   |      Configurable                                                                              |
|  | 2D and 3D acceleration API    | GPU-dependent                            | GPU-independent (common set)                                                       |
|  | CP, telephony                 | Fully supported                          | Partially supported (only SMS and voice call)                                           |
|  | Wi-Fi                         | Fully supported   | Partially supported (using Ethernet)                                                                                         |
|  | Sensor                        | Fully supported   | Partially supported (using the Emulator Control Panel)                                                                                     |
|  | PnP, external connection      | Fully supported                                             |  Partially supported (using the Emulator Control Panel)                                                                                  |
|  | Camera                        | Fully supported  |Partially supported (preview, capture, recording, contrast, and brightness)                                                                                   |
|  | Vibration, haptic             | Fully supported  | Not supported                                                                                                             |
|  | Bluetooth                     | Fully supported                                           |                                                          Not supported                          |
| Performance                   | CPU performance                          | Mobile CPU                               | Desktop CPU (with hardware virtualization) |
|  | GPU performance               | Real GPU                                 | Desktop GPU (relatively slow)                                                      |
|  | I/O performance               | Real HW I/O                              | Emulated I/O (relatively slow)                                                     |

#### Input System

**Table: Input differences**

| Category                       | Physical target        | Emulator                           |
| ------------------------------ | ---------------------- | ---------------------------------- |
| Touch screen panel             | Real device and driver | Virtual (VirtIO) device and driver |
| Host keyboard and hardware key | Real device and driver |  Virtual (VirtIO) device and driver|

#### Graphics and Display

**Table: Graphics and display differences**

| Category           | Physical target                     | Emulator                             |
| ------------------ | ----------------------------------- | ------------------------------------ |
| Framebuffer device | Display controller in the processor | Virtual VGA card                     |
| Backlight control  | LDI (LCD Driver IC) command         | Additional virtual device and driver |

#### Virtual Sensor (Emulator Control Panel)

**Table: Virtual sensor differences**

| Category           | Physical target                          | Emulator                                 |                                          |
| ------------------ | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| Sensor             | Acceleration                             | Receives the actual acceleration value of the device. | Receives the virtual acceleration value through the Emulator Control Panel.When the emulated device is stationary and vertical in portrait orientation, the acceleration values are 0, 1, and 0 g. |
| | Gyro               | Receives the actual gyroscope value of the device. | Receives the virtual gyroscope value through the Emulator Control Panel. |
| | Geomagnetic        | Receives the actual geomagnetic value of the device. | Receives the virtual geomagnetic value through the Emulator Control Panel.When the emulated device is stationary and vertical in portrait orientation, the Y axis is at true north and the magnetic field strength values are 1, 0, and -10 µT. |
| | Proximity          | Receives the actual proximity value of the device. | Receives the virtual proximity value through the Emulator Control Panel.You can register an event handler for the proximity sensor and test it with the Emulator Control Panel. However, the screen does not power off during the event because the emulator does not connect to the power manager. |
| | Light              | Receives the actual ambient light value of the device. | Receives the virtual ambient light value through the Emulator Control Panel.You can register an event handler for the light sensor and test it with the Emulator Control Panel. However, in order to test the screen brightness change, the brightness setting must be automatic in the setting application.                                           |
| | Pressure           | Receives the actual pressure value of the device. | Receives the virtual actual pressure value through the Emulator Control Panel.                                           |
| | Ultraviolet        | Receives the actual ultraviolet value of the device. | Receives the virtual actual ultraviolet value through the Emulator Control Panel.                                           |
| | Heart Rate Monitor | Receives the actual heart rate and peak-to-peak values of the device. | Receives the virtual actual heart rate and peak-to-peak values through the Emulator Control Panel.                                           |
| Device             | Battery                                  | Receives the actual battery value of the device. | Receives the virtual battery value through the Emulator Control Panel.You can change the battery level and the charger connection status. |
| | Earjack            | Receives the actual earjack connection event of the device. | Receives the earjack connection event through the Emulator Control Panel.You can select a 3-wire or 4-wire connection, or set the earjack as disconnected.                                        |
| | USB                | Receives the actual USB connection event of the device. | Receives the USB connection event through the Emulator Control Panel.                                          |
|  | RSSI               | Receives the actual RSSI value of the device. | Receives the virtual RSSI value through the Emulator Control Panel.                                          |
| Location           | Log                                      | Supported by lbsFW.                      | Receives the virtual GPS log file through the Emulator Control Panel.You can use a log file of the NMEA format. |
| | Manual             | Not supported.                           | Receives the virtual longitude and latitude values through the Emulator Control Panel.                                       |
| | Map                | Not supported.                           | Receives the virtual longitude, latitude, altitude, and horizontal accuracy values through the Emulator Control Panel map.                                           |
| | Auto               | Receives the actual GPS coordinates of the device. | Not supported.                                                                     |

#### Telephony

**Table: Telephony differences**

| Category  | Physical target             | Emulator                                 |                                          |
| --------- | --------------------------- | ---------------------------------------- | ---------------------------------------- |
| Telephony | Call                        | Calls and video calls are supported.     | Call waiting, outgoing call barring, and voice calls with the Emulator Control Panel are supported.Video calls, call forwarding, incoming call barring, and emulator-to-emulator calls are not supported. |
| Telephony | SMS       | SMS messaging is supported. | SMS messaging with the Emulator Control Panel is supported.Sending emulator-to-emulator SMS messages is not supported.                                          |

#### Power Management

**Table: Power management differences**

| Mode           | Physical target                     | Emulator                                 |
| -------------- | ----------------------------------- | ---------------------------------------- |
| Display on/off | Display controller in the processor | Internal emulation                       |
| Power off      | Power management in the processor   | ACPI (Advanced Configuration and Power Interface) |

#### Supported Media Formats and Codecs

**Table: Media format and codec differences**

| Category |  | Physical target | Emulator  |
| -------- | --------------- | --------- | ------------- |
| Decoder  | FLAC            | Supported | Not supported |