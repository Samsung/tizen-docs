# Prerequisites of Visual Studio Code Extension for Tizen

Visual Studio Code Extension for Tizen enables you to develop Tizen .NET and Tizen Web applications easily using Visual Studio Code. To work with VS Code Extension for Tizen, your computer must have below prerequisites.

- Supported host platform

  VS Code Extension for Tizen supports the following operating systems:

  - Windows 10 (64 bit)
  - Ubuntu 18.04/20.04 (64 bit)
  - macOS 10.15 (Catalina)

- Required tools

  To use VS Code Extension for Tizen, you must install the following tools:

  - NET Core SDK 2.0 or later **for Tizen .Net only**

    Download from <https://www.microsoft.com/net/download/>.

  - Node.js

    Download from <https://nodejs.org>.

  - Tizen Baseline SDK or Tizen Studio

    If neither of these is found, VS Code Extension for Tizen installs the Baseline SDK.

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


