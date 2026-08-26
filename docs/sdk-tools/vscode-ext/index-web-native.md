# Prerequisites of Visual Studio Code Extension for Tizen

Visual Studio Code Extension for Tizen enables you to develop Tizen .NET, Tizen Web and Tizen Native applications easily using Visual Studio Code. To work with VS Code Extension for Tizen, your computer must have the following prerequisites:

- Supported host platform
- VS Code with version 1.92.0 and above

    VS Code Extension for Tizen supports the following operating systems:

    - Windows 10 and above (64 bit)
    - Ubuntu 20.04 and above (64 bit)
    - macOS 11.4 (Big Sur) / 12.3 (Monterey)

- Required tools:

    To use VS Code Extension for Tizen, you must install the following tools:

    - Python 2.7 (only for macOS)

      Download from <https://www.python.org/ftp/python/2.7.18/python-2.7.18-macosx10.9.pkg>.

    - Tizen Baseline SDK or Tizen Studio

      If neither of these is found, VS Code Extension for Tizen installs the Baseline SDK.

## Emulator Requirements

Tizen Emulator for VS Code Extension for Tizen has the same requirements as the Emulator in Tizen Studio. To check the detailed hardware and software requirements for Tizen Emulator, see [Emulator Requirements](../tizen-studio/setup/prerequisites.md#emulator):

### Using Intel&reg; HAXM Driver

- Intel&reg; Hardware Accelerated Execution Manager (Intel&reg; HAXM) speeds up Tizen Emulation on Intel-VT-enabled systems. For more information, see [Hardware Accelerated Execution Manager](../tizen-studio/setup/hardware-accelerated-execution-manager.md).

> [!NOTE]
> This option will not be applicable to and will not work on AMD processors.

- Make sure **Hyper-V** is disabled (in Windows 10 or higher):
  1. Input **Control Panel** on the **Search** box in Windows 10.

  2. Click **Control Panel > Programs and Features > Turn Windows features on or off**.

  3. Disable **Hyper-V** and click **OK**.

     ![Disable Hyper-V](./media/cs_prerequisite-disable-hyperv.png)

  4. Reboot the computer.

### Using Microsoft&reg; Hyper-V and Hypervisor Platform

- Microsoft's Hyper-V and the Windows Hypervisor Platform (WHPX). Hyper-V is a virtualization feature of Windows that makes it possible to run virtualized computer systems on a physical host computer.

- Make sure **Hyper-V** is enabled (PowerShell in Windows 10 or higher):
  1. Check the configuration

     > Get-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V-All -Online

     FeatureName      : Microsoft-Hyper-V-All\
     DisplayName      : Hyper-V\
     Description      : Provides services and management tools for creating and running virtual machines and their resources.\
                      RestartRequired  : Possible\
                      State            : Disabled\
                      CustomProperties :

  2. Enable Hyper-V & HypervisorPlatform

     > Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All\
     > Enable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -All

     ![Enable Hyper-V](./media/cs_prerequisite-enable-hyperv.png)

  3. Reboot the computer.

