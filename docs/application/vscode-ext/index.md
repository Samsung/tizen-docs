# Prerequisites for Visual Studio Code Extension for Tizen

The Visual Studio Code Extension for Tizen enables you to easily develop Tizen .NET, Tizen Web, and Tizen Native applications using Visual Studio Code. To use the VS Code Extension for Tizen, your computer must meet the following prerequisites:

- Supported host platform
- VS Code version 1.100.0 or higher

  The extension supports the following operating systems:

  - Windows 10 and above (64-bit)
  - Ubuntu 20.04 and above (64-bit)
  - macOS 11.4 (Big Sur) / 12.3 (Monterey)

## Emulator Requirements

The Tizen Emulator for the VS Code Extension has the same requirements as the Tizen Studio Emulator. For detailed hardware and software requirements, see [Emulator Requirements](../tizen-studio/setup/prerequisites.md#emulator):

### Using the Intel&reg; HAXM Driver

- The Intel&reg; Hardware Accelerated Execution Manager (Intel&reg; HAXM) speeds up Tizen emulation on Intel VT-enabled systems. For more information, see [Hardware Accelerated Execution Manager](../tizen-studio/setup/hardware-accelerated-execution-manager.md).

> [!NOTE]
> This option is not applicable to and will not work on AMD processors.

- Ensure **Hyper-V** is disabled (on Windows 10 or higher):

  1. Type **Control Panel** in the **Search** box.

  2. Click **Control Panel > Programs and Features > Turn Windows features on or off**.

  3. Disable **Hyper-V** and click **OK**.

     ![Disable Hyper-V](./media/cs_prerequisite-disable-hyperv.png)

  4. Reboot the computer.

### Using Microsoft&reg; Hyper-V and Hypervisor Platform

- Microsoft Hyper-V and the Windows Hypervisor Platform (WHPX) allow running virtualized computer systems on a physical host.

- Ensure **Hyper-V** is enabled (using PowerShell on Windows 10 or higher):

  1. Check the configuration:

     ```powershell
     Get-WindowsOptionalFeature -FeatureName Microsoft-Hyper-V-All -Online
     ```

     Output example:
     ```text
     FeatureName      : Microsoft-Hyper-V-All
     DisplayName      : Hyper-V
     Description      : Provides services and management tools for creating and running virtual machines and their resources.
     RestartRequired  : Possible
     State            : Disabled
     CustomProperties :
     ```

  2. Enable Hyper-V & HypervisorPlatform:

     ```powershell
     Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
     Enable-WindowsOptionalFeature -Online -FeatureName HypervisorPlatform -All
     ```

     ![Enable Hyper-V](./media/cs_prerequisite-enable-hyperv.png)

  3. Reboot the computer.

