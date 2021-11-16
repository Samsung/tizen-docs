# Tizen Studio 3.7 Release Notes

- Release Date: Apr 6, 2020

## IDE and Tools

### New Features

- IDE
  - JDK has been bundled with Tizen Studio removing the dependency of Java being installed in the system.
  - Support for Chrome 80 has been added.
  - Log Viewer has been re-enabled in Tizen IDE.

- Certificate Manager
  - The security of the Tizen certificates has been enhanced by adding support for SHA512 encryption.

### Known Issues

- Tizen Studio
  - In macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from previous installation.
  - In case if you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
- Common
  - If you install Tizen Studio in a directory that requires administrator privileges for access. For example, for C:\ProgramFiles, administrator privileges are required to run the Tizen SDK tools. The Tizen Installer and the baseline SDK Installer alerts you, if you try to install into such a directory.
- Web and Native IDE
  - You can create unit tests for Tizen 2.3.2 and higher version projects only. Now Tizen Studio does not support unit testing for older versions.
- Web IDE
  - The preview tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature **Ctrl + 4** of the Web SDK HTML Editor.
  - In Rapid Development Support (RDS) mode, the web unit test result is not updated.
- Certificate Manager
  - Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
- Emulator
  - In the Tizen 5.5 version, the emulator images app un-installation might take some time to complete if the app name contains more than 14 characters. A patch for the same will be released in the next update.
  - To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, see [Prerequisites for Tizen Studio](../setup/prerequisites.md).
    - If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [bumblebee project](https://wiki.ubuntu.com/Bumblebee). For Windows, select **High Speed NVIDIA&reg; Processor** as **Preferred Graphics Processor** in the NVIDIA&reg; control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session occasionally logs out while launching Emulator Manager, or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows, if an error with message "failed to allocate memory" occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /setincreaseuserva 3072** command on the console with administrator rights (only in Windows 7), and reboot.
  - If you use a MacBook Pro that has both Intel HD and NVIDIA&reg; GPUs, the emulator can be unexpectedly terminated when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the general tab in the emulator configuration window, set OpenGL ES version to version 2.0 or to version 3.0.
  - When you launch Emulator Manager in the Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.
  - Basic Web applications are not installed on SD cards.
- CLI and SDB
  - Tizen Studio does not support the [Smart Development Bridge](../common-tools/smart-development-bridge.md) (SDB) bash auto-completion on Windows (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:
    - The Core Frequency information is not shown.
    - The screenshots on scene transitions feature will not work.
  - When analyzing applications on the Tizen 4.0 emulator or reference device, the startup profiling information is not shown.
  - The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot show lifecycle information for Web applications.
  - Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
  - The Dynamic Analyzer sometimes get's stuck which is caused by an internal security checking program.
