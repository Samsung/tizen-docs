# Prerequisites for the Tizen Studio

## Dependencies

- Tizen Studio 1.0 and Higher


Check the following prerequisites before attempting to install the Tizen Studio.

## OS and System Requirements

The following table lists the supported operating systems and hardware requirements for the Tizen Studio.

**Table: OS and system requirements**

|  |            | Microsoft Windows®          | macOS                      | Ubuntu                                         |
| ------------ | --------------------------- | -------------------------- | ---------------------------------- | ----------- |
| OS           | Version                     | 10/8/7                     | 10.11 (El Capitan)10.10 (Yosemite) | 16.04/14.04 |
| |Bit          | 64 bit / 32 bit             | 64 bit only                | 64 bit / 32 bit                                |
| HW           | CPU                         | Dual Core, 2 GHz or faster |   Dual Core, 2 GHz or faster                                  |  Dual Core, 2 GHz or faster            |
|  | Architecture | x64 (64 bit) / x86 (32 bit) | x64 only                   | x64 / x86                                       |
|  | Memory       | 3 GB or more                | 3 GB or more                           |3 GB or more                                                 |
|  | Disk space   | 6 GB or more                | 6 GB or more                            |6 GB or more                                     |             |

## Java Development Kit (JDK) Requirements

You must install a Java Development Kit (JDK) 8 or higher to use the Tizen Studio. Do not install OpenJDK.

Follow these instructions to install the appropriate JDK version for your system:

- Microsoft Windows®

  Download the JDK from the [official Oracle Web site](http://www.oracle.com/technetwork/java/javase/downloads/index.html). Select the appropriate platform for your hardware architecture and Windows® version. Then, run the downloaded execution file and follow the displayed instructions.

- macOS

  Download the JDK from the [official Oracle Web site](http://www.oracle.com/technetwork/java/javase/downloads/index.html) and follow the instructions to install the JDK.

  To support legacy Java software on macOS, you must download and install the Java for OS X 2015-001. Download it from [https://support.apple.com/kb/DL1572](https://support.apple.com/kb/DL1572).

- Ubuntu

  Go to the [Ubuntu Web site](https://help.ubuntu.com/community/Java#Oracle_Java_8) for detailed instructions for installing the Oracle® JDK version 8 or higher.

## Emulator Requirements

The following table lists the CPU, screen resolution, graphic card, driver, and webcam requirements for using the Tizen emulator.

**Table: Emulator requirements**

| Component                                | Microsoft Windows®                       | macOS                                    | Ubuntu |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ------ |
| CPU                                       <td colspan=3> Recommended: Support for Intel VTx (Virtualization Technology)                                                   |
| Screen resolution                         <td colspan=3>  Recommended: 1280 x 1024                                                                 |
| Graphic card                             <td colspan=3>  Recommended: The following requirements have passed tests with the emulator.<br/><br/> **Supported graphic cards**<br/> - NVIDIA: NVIDIA® GeForce® 8300 GS, GeForce® 8500 GT, GeForce® GT 220, GeForce® GT 430, GeForce® GT 530, GeForce® GT 330M, GeForce® GTX 550Ti, NVIDIA® Quadro® NVS 290<br/> - ATI: RADEON HD 4850, RADEON HD 5450<br/> - Intel: HD Graphics 2000, HD Graphics 2500, HD Graphics 4000<br/><br/>  **Note**<br/>If the host machine is using the NVIDIA® Optimus® technology, the emulator works with the on-board graphics card. To prevent this, either disable the Optimus® technology, or set the emulator to run with the external NVIDIA graphics card.Integrated graphic cards inside Intel's Q33/Q35/Q43/Q45 motherboards are not supported.First generation Intel HD Graphics is not supported.                                                 |
| Driver                                 <td colspan=3>  You must upgrade to the latest vendor-provided version of the graphic card driver for OpenGL® ES acceleration.                                                   |
| |Check and install the necessary drivers in the **Control Panel > System and Security > Windows Update**. | -                                        | For more information on driver upgrades, see the [Ubuntu Web site](https://help.ubuntu.com/community/BinaryDriverHowto/). Check and install the necessary drivers in the **System Settings > Software & Updates > Additional Drivers**.In 16.04 and 14.04, the Intel driver version must be 8.0.1 or higher.         |
| Webcam                                  <td colspan=3> To use the emulator with your computer's webcam, the webcam must support the USB Video Class (UVC) driver. The following image format requirements apply to each OS:                                                   |
| | YUYV or MJPEG                            | RGB24 or YUY2                            | UYYY, YYU420, YUY420, or YUYY                    |

## Google Chrome™ Browser Requirements

You must install the Google Chrome™ browser to use the [Web Inspector](../web-tools/web-inspector-w.md) tool.

Since the Web Inspector server uses the Web core in the platform, there is a limit on the Google Chrome™ browser version in your environment. For all functions of the Web Inspector to work properly, use the [Google Chrome™ browser version 52 or lower](http://www.slimjet.com/chrome/google-chrome-old-version.php).

## Additional Requirements

The following table lists the additional requirements to be met before developing Tizen applications.

**Table: Additional Microsoft Windows® requirements**

| Component                                | Requirement                              |
| ---------------------------------------- | ---------------------------------------- |
| Python for using the T-trace (Tizen profiling tool used to optimize the application performance) | To use the T-trace in Windows® 8/7, you must install a Python 2.7.X version:<br/> 1. On the [Python Web site](https://www.python.org/downloads/), download the appropriate Python version for your hardware and Windows® version.<br/> 2. Run the downloaded installer file and follow the displayed instructions.<br/><br/>**Note**<br/>To use Python conveniently at the command prompt, set the `%PATH%` environment variable in **My Computer > Properties > Advanced > Environment Variables**. |

**Table: Additional macOS requirements**

| Component                                | Requirement                              |
| ---------------------------------------- | ---------------------------------------- |
| Prerequisite packages (`msgfmt`) for build PO files | At the terminal prompt, enter the following commands:<br/>``` $ brew install gettext ```<br/> ```$ brew link gettext –force ```<br/> ``` $ which msgfmt ```<br/> ``` /usr/local/bin/msgfmt ```<br/><br/>**Note**<br/>To install Homebrew, see the [Brew Web site](http://brew.sh/). |

**Table: Additional Ubuntu requirements**

| Component                                | Requirement                              |
| ---------------------------------------- | ---------------------------------------- |
| Prerequisite packages (webkitgtk and cpio) for developing applications | At the terminal prompt, enter the following command:<br/>`$ sudo apt-get install libwebkitgtk-1.0-0 cpio rpm2cpio` |
| Prerequisite packages (glib, curl, sdl, pixel manipulation) for using the emulator | At the terminal prompt, enter the following command for Tizen Studio:<br/>`$ sudo apt-get install acl bridge-utils openvpn libfontconfig1 libglib2.0-0 libjpeg-turbo8 libpixman-1-0 libpng12-0 libsdl1.2debian libsm6 libv4l-0 libx11-xcb1 libxcb-icccm4 libxcb-image0 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xfixes0 libxi6` |