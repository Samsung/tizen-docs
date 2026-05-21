# Tizen SDK 10.0 Release Notes

- Release Date: November 04, 2025

## IDE and tools

### New features
- Visual Studio Code
  - **Enhanced SDK Performance:** Lightweight Node.js + TypeScript engine and modernized welcome page and project wizard UI deliver faster, more responsive, and intuitive development.
  - **Automated Installation:** SDK now auto-installs required components on demand, simplifying setup and reducing manual effort.
  - **Integrated Baseline Tools:** Previously Java-based baseline tools are now seamlessly integrated into the VSCode extension enhancing speed, stability, and development workflow.
- Visual Studio (Windows)
  - Added Web Unit Test feature for testing functionalities of user developed web application.
  - Added support for debugging/running/profiling applications in devices with RISC-V architecture.
  - Added support for incremental build(build will be skipped when there is no modification in code).
  - Integrated new Tizen Memory Profiler.
- Tizen SDK and Tizen-core
  - Tizen SDK now natively supports RISC-V architecture.
  - The SDB tool now includes **sdb reverse** command.
  - Tizen SDK officially supports Ubuntu 24.04 and macOS Sequoia.
  - Tizen-10.0 platform support is added with GCC and related tools updated to 14.2 version.
  - Added new command in Tizen-core for running Tizen web app unittests.
  - Added project template for Tizen .NET RPK library development.
  - x86 emulators and related tools have been deprecated for Tizen-10.0 and later versions.
  - LLVM toolchain is deprecated for Tizen-10.0 version.
  - Removed TAU library and unused templates.
  - Removed outdated GCC 6.x toolchain.
- Tizen Doctor
  - A new CLI based tool is provided for diagnosing the developer environment setup for Tizen SDK and will analyze the system and display a list of any issues it detects, along with suggestions for resolving them.
    

### Fixed bugs
  - Fixed issue of source exclude files not being processed while native build in tizen-core.
  - Fixed issue of certain XML tags getting excluded from tizen-manifest.xml file in the tpk built from tizen-core.
  - Fixed the issue of launch occurring in unselected device in a complex scenario in VS extension.
  - Fixed the issue of VS crashing after rebuild and apply pressed while modifying code in debug mode.
  - Fixed the issue of hybrid project(native dependent on dotnet) build failed in VS extension.


### Known issues

  - On macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from the previous installation.
  - In case you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
  - On macOS, since Catalina and above versions, Native Templates-5.5 will not build with CLI when the compiler is set to **GCC**.
- Common
  - If you install Tizen Studio in a directory that requires administrator privileges for access, an alert will be given. For example, for **C:\ProgramFiles**, location administrator privilege is needed to run Tizen SDK tools. Tizen Installer and Baseline SDK Installer alerts you if you try to install it into such a directory.
  - On macOS, Tizen Studio will not work properly if it is installed on Desktop directory, that is **$HOME/Desktop**. However, it works properly if it is installed on any other directory.
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
  - sdb install for rpk is not supported in TV 8.0 emulator(it will be supported in TV 9.0 emulator) and makes sdb freeze, press Ctrl+C to unfreeze.
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
