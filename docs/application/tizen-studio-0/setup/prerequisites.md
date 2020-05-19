# Prerequisites for Tizen Studio

Check the following prerequisites before attempting to install Tizen Studio.

## Java Development Kit (JDK) Requirements
> **Note**
>
> There is no JDK prerequisite for Tizen Studio 3.7 and higher.

You must install Oracle Java Development Kit (JDK) 8 or OpenJDK 12 for Tizen Studio 3.5 and Tizen Studio 3.6.

Follow these instructions to install the appropriate JDK version for your system:

- Microsoft Windows&reg;

  Download the JDK from the [official Oracle Web site](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html). Select the appropriate platform for your hardware architecture and Windows&reg; version. Then, run the downloaded execution file and follow the displayed instructions.

- macOS

  Download the JDK from the [official Oracle Web site](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) and follow the instructions to install the JDK.

  To support legacy Java software on macOS, you must download and install the Java for OS X 2015-001. Download it from [https://support.apple.com/kb/DL1572](https://support.apple.com/kb/DL1572).

- Ubuntu

  Go to the [Ubuntu Web site](https://help.ubuntu.com/community/Java) for detailed instructions for installing the Oracle&reg; JDK version 8. The raw binaries can be downloaded directly from Oracle ([Oracle Java download page](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)).

  > **Note**
  >
  > For RT IDE use Oracle Java Development Kit (JDK) 8 only.

You can also use Oracle's OpenJDK. For more installation details, see [OpenJDK 12 and OpenJFX Installation Guide](openjdk.md).

## OS and System Requirements

The following table lists the supported operating systems and hardware requirements for Tizen Studio.

**Table: OS and system requirements**

<table>
<thead>
<tr>
<th colspan="2"> </th>
<th>Microsoft Windows&reg;</th>
<th>macOS</th>
<th>Ubuntu</th>
</tr>
</thead>
<tbody>
<tr>
<th rowspan="2">OS</th>
<th>Version</th>
<td>10</td>
<td>10.13 (High Sierra)</p>
<p>10.12 (Sierra)</p>
</td>
<td>18.04/16.04</td>
</tr>
<tr>
<th>Bit</th>
<td>64 bit only</td>
<td>64 bit only</td>
<td>64 bit only</td>
</tr>
<tr>
<th rowspan="4">HW</th>
<th>CPU</th>
<td>Dual Core, 2 GHz or faster</td>
<td>Dual Core, 2 GHz or faster</td>
<td>Dual Core, 2 GHz or faster</td>
</tr>
<tr>
<th>Architecture</th>
<td>x64 (64 bit)</td>
<td>x64 only</td>
<td>x64 (64 bit)</td>
</tr>
<tr>
<th>Memory</th>
<td>3 GB or more</td>
<td>3 GB or more</td>
<td>3 GB or more</td>
</tr>
<tr>
<th>Disk space</th>
<td>6 GB or more</td>
<td>6 GB or more</td>
<td>6 GB or more</td>
</tr>
</tbody>
</table>

<a name="emulator"></a>
## Emulator Requirements

The following table lists the CPU, screen resolution, graphic card, driver, and webcam requirements for using the Tizen Emulator.

**Table: Emulator requirements**

<table>
<thead>
<tr>
<th>Component</th>
<th>Microsoft Windows&reg;</th>
<th>macOS</th>
<th>Ubuntu</th>
</tr>
</thead>
<tbody>
<tr>
<td>CPU</td>
<td colspan="3">Recommended: Support for Intel&reg; VTx (Virtualization Technology)</td>
</tr>
<tr>
<td>Screen resolution</td>
<td colspan="3">Recommended: 1280 x 1024</td>
</tr>
<tr>
<td>Graphic card</td>
<td colspan="3">Recommended: The following requirements have passed tests with the emulator.</p>
<p class="Table"><strong>Table: Supported graphic cards</strong></p>
<table>
<thead>
<tr>
<th>Brand</th>
<th>Product</th>
</tr>
</thead>
<tbody>
<tr>
<td>NVIDIA</td>
<td>NVIDIA&reg; GeForce&reg; 8300 GS, GeForce&reg; 8500 GT, GeForce&reg; GT 220, GeForce&reg; GT 430, GeForce&reg; GT 530, GeForce&reg; GT 330M, GeForce&reg; GTX 550Ti, NVIDIA&reg; Quadro&reg; NVS 290</td>
</tr>
</tbody>
</table>
<strong>Note</strong
<ul>
<li>If the host machine is using the NVIDIA&reg; Optimus&reg; technology, the emulator works with the on-board graphics card. To prevent this, either disable the Optimus&reg; technology, or set the emulator to run with the external NVIDIA graphics card.</li>
</ul>
</p>
</td>
</tr>
<tr>
<td rowspan="2">Driver</td>
<td colspan="3">You must upgrade to the latest vendor-provided version of the graphic card driver for OpenGL&reg; ES acceleration.</td>
</tr>
<tr>
<td>Check and install the necessary drivers in the <strong>Control Panel &gt; System and Security &gt; Windows Update</strong>.</td>
<td>-</td>
<td>For more information on driver upgrades, see the <a href="https://help.ubuntu.com/community/BinaryDriverHowto/" target="_blank">Ubuntu Web site</a>. Check and install the necessary drivers in the <strong>System Settings &gt; Software &amp; Updates &gt; Additional Drivers</strong>.</p>
<p>In 16.04 and 14.04, the Intel driver version must be 8.0.1 or higher.</p>
</td>
</tr>
<tr>
<td rowspan="2">Webcam</td>
<td colspan="3">To use the emulator with your computer's webcam, the webcam must support the USB Video Class (UVC) driver. The following image format requirements apply to each OS:</td>
</tr>
<tr>
<td>YUYV or MJPEG</td>
<td>RGB24 or YUY2</td>
<td>UYYY, YYU420, YUY420, or YUYY</td>
</tr>
</tbody>
</table>

## Google Chrome&trade; Browser Requirements

You must install the Google Chrome&trade; browser to use the [Web Inspector](../web-tools/web-inspector.md) tool.

Since the Web Inspector server uses the Web core in the platform, there is a limit on the Google Chrome&trade; browser version in your environment. For all functions of the Web Inspector to work properly, use the **Google Chrome&trade; browser version 77 or higher**.

## Additional Requirements

The following table lists the additional requirements to be met before developing Tizen applications.

**Table: Additional Microsoft Windows&reg; requirements**

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Python for using the T-trace (Tizen profiling tool used to optimize the application performance)
</td>
<td>To use the T-trace in Windows&reg; 8/7, you must install a Python 2.7.X version:
<ul>
<li>On the <a href="https://www.python.org/downloads/">Python Web site</a>, download the appropriate Python version for your hardware and Windows&reg; version.
</li>
<li>Run the downloaded installer file and follow the displayed instructions.</li>
</ul>
<strong>Note</strong> <br>
To use Python conveniently at the command prompt, set the <code>%PATH%</code> environment variable in <strong>My Computer > Properties > Advanced > Environment Variables</strong>.
</td>
</tr>
</tbody>
</table>


**Table: Additional macOS requirements**

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prerequisite packages (<code>msgfmt</code>) for build PO files
</td>
<td>At the terminal prompt, enter the following commands:
<pre><code>$ brew install gettext
$ brew link gettext --force
$ which msgfmt
/usr/local/bin/msgfmt
</code></pre>
<strong>Note</strong><br>
To install Homebrew, see the <a href="http://brew.sh/">Brew Web site</a>.
</td>
</tr>
</tbody>
</table>


**Table: Additional Ubuntu requirements**

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prerequisite packages (webkitgtk and cpio) for developing applications</td>
<td>At the terminal prompt, enter the following command:
<pre><code>$ sudo apt-get install libwebkitgtk-1.0-0 cpio rpm2cpio</code></pre></td>
</tr>
<tr>
<td>Prerequisite packages (glib, curl, sdl, pixel manipulation) for using the emulator
</td>
<td>At the terminal prompt, enter the following command for Tizen Studio:
<pre><code>$ sudo apt-get install acl bridge-utils openvpn libfontconfig1 libglib2.0-0 libjpeg-turbo8 libpixman-1-0 libpng12-0 libsdl1.2debian libsm6 libv4l-0 libx11-xcb1 libxcb-icccm4 libxcb-image0 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xfixes0 libxi6</code></pre></td>
</tr>
</tbody>
</table>

## Related Information
* Dependencies
  - Tizen Studio 1.0 and Higher
