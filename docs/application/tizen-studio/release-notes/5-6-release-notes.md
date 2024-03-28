# Tizen Studio 5.6 Release Notes

- Release Date: Mar 29, 2024

## IDE and tools

### New features
- Tizen Studio
  - Tizen Studio is now supported in MacOS Sonoma version.
  - Modified packaging structure of NUIGadget application on Tizen-core.

### Fixed bugs
  - Fixed the installation failure issue in Package Manager on Windows OS.
  - Fixed multiple packaging issue of Tizen .NET applications.
  - Fixed the issue of baseline tools not launched when no folder is opened on VSCode.
  - Fixed Device Manager and Emulator Manager crash issue on MacOS Sonoma.
  - Fixed the issue of Debugging native application in 64 bit Emulator from Visual Studio (Windows) and VSCode

### Known issues

  - On macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from the previous installation.
  - In case you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
  - On macOS, since Catalina and above versions, Native Templates-5.5 will not build with CLI when the compiler is set to **GCC**.
- Common
  - If you install Tizen Studio in a directory that requires administrator privileges for access, an alert will be given. For example, for **C:\ProgramFiles**, location administrator privilege is needed to run Tizen SDK tools. Tizen Installer and Baseline SDK Installer alerts you if you try to install it into such a directory.
  - On macOS, Tizen Studio won't work properly if it is installed on Desktop directory, that is **$HOME/Desktop**. However it works properly if it is installed on any other directory.
- Web and Native IDE
  - You can create unit tests for Tizen 2.3.2 and higher version projects only. Unit testing for older versions is not supported.
- Web IDE
  - The preview tab in the Web Page Editor sometimes does not appear properly. In this case, you can use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature **Ctrl + 4** of the Web SDK HTML Editor.
  - In Rapid Development Support (RDS) mode, the web unit test result is not updated.
  - Remote Inspector does not allow audit in the updated version of Chrome.
- Certificate Manager
  - Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
- Emulator
  - In Tizen 5.5 version, the emulator images app uninstallation might take some time to complete if the app name contains more than 14 characters. A patch for the same is expected to be released in the next update.
  - To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, see [Prerequisites for Tizen Studio](../setup/prerequisites.md).
  - If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows, you must set Tizen Emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [Bumblebee Project](https://wiki.ubuntu.com/Bumblebee){:target="_blank"}. For Windows, select **High Speed NVIDIA&reg; Processor** as **Preferred Graphics Processor** in the NVIDIA&reg; Control Panel.    
  - On Ubuntu, if the graphics driver is out-of-date while launching Emulator Manager, your Ubuntu desktop session occasionally logs out or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows, if an error with the message "failed to allocate memory" occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /setincreaseuserva 3072** command on the console with administrator rights (only in Windows 7), and reboot.
  - If you use a MacBook Pro that has both Intel HD and NVIDIA&reg; GPUs, the emulator can terminate unexpectedly when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the **General** tab in the emulator configuration window, set OpenGL ES version to version 2.0, or to version 3.0.
  - When you launch Emulator Manager in Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.
  - Basic web applications are not installed on SD cards.
  - To use Tizen Emulator in Tizen platform 3.0 or lower, disable the CPU VT option in the **HW Support** tab of emulator configuration.
- CLI and SDB
  - Tizen Studio does not support the [Smart Development Bridge](../common-tools/smart-development-bridge.md) (SDB) bash auto-completion on Windows (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:
    - The core frequency information is not shown.
    - The screenshots on the scene transitions feature will not work.
  - When analyzing applications on Tizen 4.0 Emulator or reference device, the startup profiling information is not shown.
  - The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot show lifecycle information for web applications.
  - Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
  - The Dynamic Analyzer sometimes gets stuck, which is caused by an internal security checking program.
- Visual Studio
  - NUI XAML application build error can be resolved by doing a clean build.
