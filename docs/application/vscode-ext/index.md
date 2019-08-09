# Prerequisites of Visual Studio Code Extension for Tizen

Visual Studio Code Extension for Tizen enables you to develop Tizen .NET and Tizen Web applications easily using Visual Studio Code. To work with VS Code Extension for Tizen, your computer must have below prerequisites.

- Supported host platform

  VS Code Extension for Tizen supports the following operating systems:

  - Windows&reg; 10 (64 bit)
  - Ubuntu 16.04/18.04 (64 bit)
  - macOS 10.12, 10.13 (Sierra)

- Required tools

  To use VS Code Extension for Tizen, you must install the following tools:

  - NET Core SDK 2.0 or later **for Tizen.Net only**

    Download from <https://www.microsoft.com/net/download/>.

  - Node.js

    Download from <https://nodejs.org>.

  - Oracle Java 8 or higher

    Ubuntu 16.04 also supports OpenJDK.

  - Tizen Baseline SDK or Tizen Studio

    If neither of these is found, VS Code Extension for Tizen automatically installs the baseline SDK.

  - Microsoft C\# extension for Visual Studio Code **for Tizen.Net only**

    Install from the Visual Studio Code Marketplace.

### Emulator Requirements

The Tizen emulator for VS Code Extension for Tizen has the same requirements as the emulator in the Tizen Studio. To check the detailed hardware and software requirements for the Tizen emulator, see [Emulator Requirements](../setup/additional-requirements.md#tizen-studio-emulator-requirements).

- Intel&reg; Hardware Acceleration Execution Manager (Intel&reg; HAXM) speeds up the Tizen emulation on Intel-VT-enabled systems. For more information, see [Hardware Accelerated Execution Manager](../tizen-studio-0/setup/hardware-accelerated-execution-manager.md).

- Make sure **Hyper-V** is disabled (in Windows&reg; 10 or higher):
  1. In the **Start** menu, select **Programs and Features**.

     ![Programs and Features](media/cs_prerequisite01-250x401.png)

  2. Select **Turn Windows features on or off**.
  3. Disable **Hyper-V** and click **OK**.

     ![Disable Hyper-V](media/cs_prerequisite-disable-hiperv.png)

  4. Reboot the computer.


