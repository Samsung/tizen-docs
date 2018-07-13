# Running Applications on the Emulator

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

1. Open the [Emulator Manager](emulator-manager.md#access).

   If you do not have an applicable emulator instance, [create one](emulator-manager.md#create).

2. Select the emulator instance and click **Launch**.

3. Test your application in the emulator. You can launch your application in 2 ways:
   - In the Tizen Studio, select the project and click **Run As**.
   - Drag an application package file (for example, the WGT file) to the emulator to install and launch the application on the emulator.

4. To close the emulator, right-click the emulator and select **Close**, or click and hold the **Power** key.

The emulator device stores the installed application so you can run it again, if needed. To remove the application, you must uninstall it. If you run the project again on the same emulator, the emulator replaces the application with the new version.

In the Emulator Manager, in addition to creating new emulator instances according to the environments you need, you can also [modify and delete emulator instances](emulator-manager.md#manage).

<a name="speed"></a>
## Increasing the Application Execution Speed

The Tizen x86 emulator exploits [KVM](http://www.linux-kvm.org/page/Main_Page) (Kernel-based Virtual Machine in Linux) or [HAX](../setup/hardware-accelerated-execution-manager.md) (Hardware Accelerated eXecution in Windows&reg; and macOS) with HW virtualization support.

If the CPU VT is disabled in the **Emulator Configuration** view on the Emulator Manager, check the following prerequisites and install KVM or HAX:

1. Prerequisites for using HW virtualization:

   - In Ubuntu:

     To use KVM, you need a processor that supports HW virtualization. Both Intel and AMD have developed those extensions for their processors (Intel VT-x/AMD-V). Check whether the CPU supports HW virtualization with the following command:

     ```
     $egrep -c '(vmx|svm)' /proc/cpuinfo
     ```

     If the output of the command is 0, the CPU does not support HW virtualization. Otherwise, it does.

     The HW virtualization feature can also be disabled on the BIOS setting. Check the setting and enable it if you need the feature.

   - In Windows&reg;

     To use HAX, you need an Intel VT-x-supported CPU, and you must enable the NX-related setting in the PC BIOS.

   - In macOS:

     To use HAX, install EFI-related updates on your Intel-based Mac computer.

     For more information, see [EFI and SMC firmware updates for Intel-based Mac computers](http://support.apple.com/kb/HT1237).

2. Installing KVM or HAX:

   - In Ubuntu:

     No installation is required for KVM.

   - In Windows&reg; and macOS:

     The HAXM driver is installed during the Tizen Studio installation. For more information on installing HAXM, see [Hardware Accelerated Execution Manager](../setup/hardware-accelerated-execution-manager.md).

   > **Note**  
   > If the installation fails with a VT-related message, check the CPU feature and BIOS settings. If the installation fails with an NX-related message, enable NX (or PAE and DEP) -related item in the BIOS. In addition, make sure that the operating system supports the NX feature (for more information, see [MSDN](http://msdn.microsoft.com/en-us/library/windows/hardware/ff542275%28v=vs.85%29.aspx)).

   No configuration is required for KVM or HAX.

### Working with the HW Virtualization, Settings, and Help

To run the emulator with the HW virtualization support in the Emulator Manager, set the **CPU VT** field to **ON**. The field is disabled if your system cannot support HW virtualization.

You can also run the emulator with the HW virtualization support from the command line, by including the `-enable-kvm` (in Ubuntu) or `-enable-hax` (in Windows&reg; and macOS) option in the start-up command.

<a name="supported"></a>
## Supported Features

The emulator provides various virtual HW, media formats, codecs, and [OpenGL&reg; ES acceleration](#opengl). For better performance of the OpenGL&reg; ES support, the Tizen emulator exploits the latest feature of the graphic driver, so always [install the latest vendor-provided graphic driver](../setup/prerequisites.md#emulator). The emulator, however, has some limitations and [differences compared to physical target devices](#target).

The following table lists the basic features supported in the emulator.

**Table: Supported emulator features**

<table>
	<thead>
		<tr>
			<th>Feature</th>
			<th>Detail</th>
			<th>Status</th>
			<th>Notes</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Skin</td>
			<td>Skins are fitted to the screen resolution:
			<p>Mobile:</p>
			<ul>
				<li>WVGA (480 x 800, default)</li>
				<li>qHD (540 x 960)</li>
				<li>HD (720 x 1280)</li>
			</ul>
			<p>Wearable:</p>
			<ul>
				<li>320 x 320</li>
				<li>360 x 360 (default)</li>
				<li>360 x 480</li>
			</ul>
			<p>4 orientation modes are supported:</p>
			<p>Portrait (default), landscape, reverse portrait, and reverse landscape</p>
			</td>
			<td>Supported</td>
			<td>2 skin layout types are supported:
			<ul>
				<li>Profile-specific skin</li>
				<li>General purpose skin</li>
			</ul>
			</td>
		</tr>
		<tr>
			<td>Touch</td>
			<td>Maru touchscreen device</td>
			<td>Supported</td>
			<td>Multi-touch is supported.</td>
		</tr>
		<tr>
			<td>Key</td>
			<td>HW keys, host keyboard, and SW keypad</td>
			<td>Supported</td>
			<td>The host keyboard is not supported for the wearable emulator.</td>
		</tr>
		<tr>
			<td>Rotary</td>
			<td>360 levels of clockwise or counter-clockwise rotation</td>
			<td>Supported</td>
			<td>-</td>
		</tr>
		<tr>
			<td>Display</td>
			<td>VGA card with 100 levels of brightness control</td>
			<td>Supported</td>
			<td>-</td>
		</tr>
		<tr>
			<td>OpenGL&reg; ES</td>
			<td>Compatible with OpenGL&reg; ES 1.1 and 2.0
			<p>OpenGL&reg; ES API pass-through through PCI</p>
			</td>
			<td>Supported</td>
			<td>The OpenGL&reg; ES 1.1 functionality is not guaranteed on the emulator, unless the graphics hardware of your computer supports OpenGL&reg; 1.5.
			<p>The OpenGL&reg; ES 2.0 functionality is not guaranteed on the emulator, unless the graphics hardware of your computer supports OpenGL&reg; 2.1.</p>
			<p>The host machine must support OpenGL&reg; 1.4.</p>
			</td>
		</tr>
		<tr>
			<td>Sound</td>
			<td>AC97 device</td>
			<td>Supported</td>
			<td><strong>Audio in:</strong>
			<p>Make sure that the input volume of the microphone is enough to record your voice or songs on the host machine.</p>
			<p>On Windows&reg; 7, inject the microphone into the host machine before starting the emulator.</p>
			<p><strong>Audio out:</strong></p>
			<p>On Windows&reg; 7, enable at least 1 audio out device before starting the emulator. Make sure that the volume icon in the tray is not disabled.</p>
			<p>While the emulator is running, do not disable the audio out device, as it can lock the audio system of the guest platform.</p>
			</td>
		</tr>
		<tr>
			<td>Network connection</td>
			<td>Virtio</td>
			<td>Supported</td>
			<td>Raw socket protocol, such as ICMP, is not supported.</td>
		</tr>
		<tr>
			<td>Emulator Control Panel</td>
			<td>The Emulator Control Panel (ECP) supports different features depending on the device profile:
			<p>Mobile:</p>
			<ul>
				<li>Device Manager: Device Tree, Network, Host Directory Sharing</li>
				<li>Event Injector: Battery, RSSI, 3-Axis Sensor, Light, Proximity, Pressure, Ultraviolet, Heart Rate Monitor, Motion, Ear Jack, USB, SDCard, Location, Telephony</li>
			</ul>
			<p>Wearable:</p>
			<ul>
				<li>Device Manager: Network, Host Directory Sharing</li>
				<li>App Manager: Uninstaller</li>
				<li>Event Injector: Battery, 3-Axis Sensor, Light, Proximity, Pedometer, Pressure, Ultraviolet, Heart Rate Monitor, Gesture, USB</li>
			</ul>
			</td>
			<td>Supported</td>
			<td>The ECP is a standalone tool, which replaces the Event Injector. It helps to control and monitor the emulator features, and can be launched from the emulator context menu.</td>
		</tr>
		<tr>
			<td>Camera</td>
			<td>Virtual camera device connecting a host machine's Webcam:
			<ul>
				<li>Support: preview, capture, and record</li>
				<li>Image format: YUYV, I420, and YV12</li>
				<li>Attributes: brightness and contrast</li>
				<li>Resolution: 160 x 120, 176 x 144, 320 x 240, 352 x 288, and 640 x 480</li>
				<li>Video resolution: 1280 x 720 for the WVGA, 320 x 240 for the WQVGA, and 640 x 480 for the HVGA devices</li>
				<li>Supported video codecs: MPEG-4, H.263, H.264, and VC-1 for both encoding and decoding</li>
			</ul>
			</td>
			<td>Supported</td>
			<td>While recording a video using the emulator, an audio-video synchronization error can occur depending on your computer hardware and performance.</td>
		</tr>
		<tr>
			<td>Bluetooth</td>
			<td>-</td>
			<td>Not supported</td>
			<td>-</td>
		</tr>
		<tr>
			<td>Wi-Fi</td>
			<td>-</td>
			<td>Not supported</td>
			<td>-</td>
		</tr>
		<tr>
			<td>Wi-Fi Direct&reg;</td>
			<td>-</td>
			<td>Not supported</td>
			<td>-</td>
		</tr>
	</tbody>
</table>

<a name="opengl"></a>
### OpenGL&reg; ES Acceleration Support

For the emulator to support OpenGL&reg; ES acceleration, you need:

- Graphics chipset driver that supports OpenGL&reg; 1.4 installed on the host machine
- All chipset vendors and driver versions available to support the OpenGL&reg; 1.4 standard

> **Note**  
> The emulator supports only ES 1.1, ES 2.0, and EGL&trade; 1.4 versions.

<a name="target"></a>
### Differences Between the Emulator and Target

The following tables describe the differences between a real target device and the emulator. For more information, see the detailed differences in:

- [Input system](#input)
- [Graphics and display](#graphics)
- [Virtual sensor](#sensor)
- [Telephony](#telephony)
- [Power management](#power)
- [Supported media formats and codecs](#codec)

**Table: Comparison summary**

<table>
	<thead>
		<tr>
			<th>Category</th>
			<th>Subject</th>
			<th>Physical target</th>
			<th>Emulator</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="5">Development environment</td>
			<td>Target</td>
			<td>Buy a target device or reference board (by model)</td>
			<td>Download the Tizen Studio (multi-profile and multi-model support)</td>
		</tr>
		<tr>
			<td>Network</td>
			<td>Need Bluetooth</td>
			<td>Only the network environment</td>
		</tr>
		<tr>
			<td>Target connection</td>
			<td>USB</td>
			<td>IPC (TCP/UDP)</td>
		</tr>
		<tr>
			<td>Source and package management</td>
			<td>Source and package for target</td>
			<td>Source and package for the emulator</td>
		</tr>
		<tr>
			<td>Host Directory Sharing</td>
			<td>Not supported</td>
			<td>Supported</td>
		</tr>
		<tr>
			<td rowspan="10">Portability</td>
			<td>Screen resolution</td>
			<td>Fixed</td>
			<td>Configurable</td>
		</tr>
		<tr>
			<td>RAM, storage size</td>
			<td>Fixed</td>
			<td>Configurable</td>
		</tr>
		<tr>
			<td>2D and 3D acceleration API</td>
			<td>GPU-dependent</td>
			<td>GPU-independent (common set)</td>
		</tr>
		<tr>
			<td>CP, telephony</td>
			<td>Fully supported</td>
			<td>Partially supported (only SMS and voice call)</td>
		</tr>
		<tr>
			<td>Wi-Fi</td>
			<td>Fully supported</td>
			<td>Partially supported (using Ethernet)</td>
		</tr>
		<tr>
			<td>Sensor</td>
			<td>Fully supported</td>
			<td>Partially supported (using the Emulator Control Panel)</td>
		</tr>
		<tr>
			<td>PnP, external connection</td>
			<td>Fully supported</td>
			<td>Partially supported (using the Emulator Control Panel)</td>
		</tr>
		<tr>
			<td>Camera</td>
			<td>Fully supported</td>
			<td>Partially supported (preview, capture, recording, contrast, and brightness)</td>
		</tr>
		<tr>
			<td>Vibration, haptic</td>
			<td>Fully supported</td>
			<td>Not supported</td>
		</tr>
		<tr>
			<td>Bluetooth</td>
			<td>Fully supported</td>
			<td>Not supported</td>
		</tr>
		<tr>
			<td rowspan="3">Performance</td>
			<td>CPU performance</td>
			<td>Mobile CPU</td>
			<td>Desktop CPU (with hardware virtualization)</td>
		</tr>
		<tr>
			<td>GPU performance</td>
			<td>Real GPU</td>
			<td>Desktop GPU (relatively slow)</td>
		</tr>
		<tr>
			<td>I/O performance</td>
			<td>Real HW I/O</td>
			<td>Emulated I/O (relatively slow)</td>
		</tr>
	</tbody>
</table>


<a name="input"></a>
#### Input System

**Table: Input differences**

| Category                       | Physical target        | Emulator                           |
|------------------------------|----------------------|----------------------------------|
| Touch screen panel             | Real device and driver | Virtual (VirtIO) device and driver |
| Host keyboard and hardware key | Real device and driver | Virtual (VirtIO) device and driver |

<a name="graphics"></a>
#### Graphics and Display

**Table: Graphics and display differences**

| Category           | Physical target                     | Emulator                             |
|------------------|-----------------------------------|------------------------------------|
| Framebuffer device | Display controller in the processor | Virtual VGA card                     |
| Backlight control  | LDI (LCD Driver IC) command         | Additional virtual device and driver |

<a name="sensor"></a>
#### Virtual Sensor (Emulator Control Panel)

**Table: Virtual sensor differences**

<table>
	<thead>
		<tr>
			<th colspan="2">Category</th>
			<th>Physical target</th>
			<th>Emulator</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td rowspan="8">Sensor</td>
			<td>Acceleration</td>
			<td>Receives the actual acceleration value of the device.</td>
			<td>Receives the virtual acceleration value through the Emulator Control Panel.
			<p>When the emulated device is stationary and vertical in portrait orientation, the acceleration values are 0, 1, and 0 g.</p>
			</td>
		</tr>
		<tr>
			<td>Gyro</td>
			<td>Receives the actual gyroscope value of the device.</td>
			<td>Receives the virtual gyroscope value through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td>Geomagnetic</td>
			<td>Receives the actual geomagnetic value of the device.</td>
			<td>Receives the virtual geomagnetic value through the Emulator Control Panel.
			<p>When the emulated device is stationary and vertical in portrait orientation, the Y axis is at true north and the magnetic field strength values are 1, 0, and -10 µT.</p>
			</td>
		</tr>
		<tr>
			<td>Proximity</td>
			<td>Receives the actual proximity value of the device.</td>
			<td>Receives the virtual proximity value through the Emulator Control Panel.
			<p>You can register an event handler for the proximity sensor and test it with the Emulator Control Panel. However, the screen does not power off during the event because the emulator does not connect to the power manager.</p>
			</td>
		</tr>
		<tr>
			<td>Light</td>
			<td>Receives the actual ambient light value of the device.</td>
			<td>Receives the virtual ambient light value through the Emulator Control Panel.
			<p>You can register an event handler for the light sensor and test it with the Emulator Control Panel. However, in order to test the screen brightness change, the brightness setting must be automatic in the setting application.</p>
			</td>
		</tr>
		<tr>
			<td>Pressure</td>
			<td>Receives the actual pressure value of the device.</td>
			<td>Receives the virtual actual pressure value through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td>Ultraviolet</td>
			<td>Receives the actual ultraviolet value of the device.</td>
			<td>Receives the virtual actual ultraviolet value through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td>Heart Rate Monitor</td>
			<td>Receives the actual heart rate and peak-to-peak values of the device.</td>
			<td>Receives the virtual actual heart rate and peak-to-peak values through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td rowspan="4">Device</td>
			<td>Battery</td>
			<td>Receives the actual battery value of the device.</td>
			<td>Receives the virtual battery value through the Emulator Control Panel.
			<p>You can change the battery level and the charger connection status.</p>
			</td>
		</tr>
		<tr>
			<td>Earjack</td>
			<td>Receives the actual earjack connection event of the device.</td>
			<td>Receives the earjack connection event through the Emulator Control Panel.
			<p>You can select a 3-wire or 4-wire connection, or set the earjack as disconnected.</p>
			</td>
		</tr>
		<tr>
			<td>USB</td>
			<td>Receives the actual USB connection event of the device.</td>
			<td>Receives the USB connection event through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td>RSSI</td>
			<td>Receives the actual RSSI value of the device.</td>
			<td>Receives the virtual RSSI value through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td rowspan="4">Location</td>
			<td>Log</td>
			<td>Supported by lbsFW.</td>
			<td>Receives the virtual GPS log file through the Emulator Control Panel.
			<p>You can use a log file of the NMEA format.</p>
			</td>
		</tr>
		<tr>
			<td>Manual</td>
			<td>Not supported.</td>
			<td>Receives the virtual longitude and latitude values through the Emulator Control Panel.</td>
		</tr>
		<tr>
			<td>Map</td>
			<td>Not supported.</td>
			<td>Receives the virtual longitude, latitude, altitude, and horizontal accuracy values through the Emulator Control Panel map.</td>
		</tr>
		<tr>
			<td>Auto</td>
			<td>Receives the actual GPS coordinates of the device.</td>
			<td>Not supported.</td>
		</tr>
	</tbody>
</table>

<a name="telephony"></a>
#### Telephony

**Table: Telephony differences**

| Category  |               | Physical target                    | Emulator                               |
|-----------|---------------|------------------------------------|----------------------------------------|
| Telephony | Call            | Calls and video calls are supported. | Call waiting, outgoing call barring, and voice calls with the Emulator Control Panel are supported. <br>Video calls, call forwarding, incoming call barring, and emulator-to-emulator calls are not supported. |
| Telephony | SMS             | SMS messaging is supported.          | SMS messaging with the Emulator Control Panel is supported. <br>Sending emulator-to-emulator SMS messages is not supported. |

<a name="power"></a>
#### Power Management

**Table: Power management differences**

| Mode           | Physical target                     | Emulator                                 |
|----------------|-------------------------------------|------------------------------------------|
| Display on/off | Display controller in the processor | Internal emulation                       |
| Power off      | Power management in the processor   | ACPI (Advanced Configuration and Power Interface) |

<a name="codec"></a>
#### Supported Media Formats and Codecs

**Table: Media format and codec differences**

| Category |      | Physical target | Emulator      |
|----------|------|-----------------|---------------|
| Decoder  | FLAC | Supported       | Not supported |


## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
