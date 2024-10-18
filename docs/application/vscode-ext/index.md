# Prerequisites of Visual Studio Code Extension for Tizen

Visual Studio Code Extension for Tizen enables you to develop Tizen .NET, Tizen Web and Tizen Native applications easily using Visual Studio Code. To work with VS Code Extension for Tizen, your computer must have below prerequisites:

- Supported host platform
- VSCode with Version 1.92.0 and above.

  VS Code Extension for Tizen supports the following operating systems:

  - Windows 10 and above (64 bit)
  - Ubuntu 18.04 and above (64 bit)
  - macOS 11.4(Big Sur)/12.3(Monterey)

- Required tools

  To use VS Code Extension for Tizen, you must install the following tools:

  - .NET Core SDK 6.0 or later **for Tizen .NET only**

    Download from <https://www.microsoft.com/net/download/>.

  - Python 2.7 (only for macOS)

    Download from <https://www.python.org/ftp/python/2.7.18/python-2.7.18-macosx10.9.pkg>.

  - Tizen Baseline SDK or Tizen Studio

    If neither of these is found, VS Code Extension for Tizen installs the Baseline SDK.

## Emulator requirements

Tizen Emulator for VS Code Extension for Tizen has the same requirements as the emulator in Tizen Studio. To check the detailed hardware and software requirements for Tizen Emulator, see [Emulator Requirements](../tizen-studio/setup/prerequisites.md#emulator).

- Intel&reg; Hardware Acceleration Execution Manager (Intel&reg; HAXM) speeds up the Tizen emulation on Intel-VT-enabled systems. For more information, see [Hardware Accelerated Execution Manager](../tizen-studio/setup/hardware-accelerated-execution-manager.md).

- Make sure **Hyper-V** is disabled (in Windows 10 or higher):
  1. Input **Control Panel** on the **Search** box in Windows 10.

  2. Click **Control Panel > Programs and Features > Turn Windows features on or off**.

  3. Disable **Hyper-V** and click **OK**.

     ![Disable Hyper-V](media/cs_prerequisite-disable-hiperv.png)

  4. Reboot the computer.


