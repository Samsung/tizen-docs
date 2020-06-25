# Prerequisites of Visual Studio Code Extension for Tizen

Visual Studio Code Extension for Tizen enables you to develop Tizen .NET and Tizen Web applications easily using Visual Studio Code. To work with VS Code Extension for Tizen, your computer must have below prerequisites.

- Supported host platform

  VS Code Extension for Tizen supports the following operating systems:

  - Windows 10 (64 bit)
  - Ubuntu 16.04/18.04 (64 bit)
  - macOS 10.12, 10.13 (Sierra)

- Required tools

  To use VS Code Extension for Tizen, you must install the following tools:

  - NET Core SDK 2.0 or later **for Tizen .Net only**

    Download from <https://www.microsoft.com/net/download/>.

  - Node.js

    Download from <https://nodejs.org>.

  - Java Development Kit (JDK)

    You must install Oracle Java Development Kit (JDK) 8 or OpenJDK 12 to use Tizen Baseline SDK. Make sure you download and install the EXACT version.

    - [Oracle Java Development Kit(JDK) 8](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).
 
    - OpenJDK 12 and OpenJFX: [OpenJDK 12 and OpenJFX Installation Guide](../tizen-studio/setup/openjdk.md).

  - Tizen Baseline SDK or Tizen Studio

    If neither of these is found, VS Code Extension for Tizen automatically installs the Baseline SDK.

  - Microsoft C\# extension for Visual Studio Code **for Tizen .Net only**

    Install from the Visual Studio Code Marketplace.

## Emulator requirements

The Tizen Emulator for VS Code Extension for Tizen has the same requirements as the emulator in Tizen Studio. To check the detailed hardware and software requirements for the Tizen Emulator, see [Emulator Requirements](../tizen-studio/setup/prerequisites.md#emulator).

- Intel&reg; Hardware Acceleration Execution Manager (Intel&reg; HAXM) speeds up the Tizen emulation on Intel-VT-enabled systems. For more information, see [Hardware Accelerated Execution Manager](../tizen-studio/setup/hardware-accelerated-execution-manager.md).

- Make sure **Hyper-V** is disabled (in Windows 10 or higher):
  1. Input **Control Panel** on the **Search** box in Windows 10.

  2. Click **Control Panel > Programs and Features > Turn Windows features on or off**.

  3. Disable **Hyper-V** and click **OK**.

     ![Disable Hyper-V](media/cs_prerequisite-disable-hiperv.png)

  4. Reboot the computer.


