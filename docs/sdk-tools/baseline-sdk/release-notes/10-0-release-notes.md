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
### Fixed bugs
  - Fixed issue of source exclude files not being processed while native build in tizen-core.
  - Fixed issue of certain XML tags getting excluded from tizen-manifest.xml file in the tpk built from tizen-core.
  - Fixed the issue of launch occurring in unselected device in a complex scenario in VS extension.
  - Fixed the issue of VS crashing after rebuild and apply pressed while modifying code in debug mode.
  - Fixed the issue of hybrid project(native dependent on dotnet) build failed in VS extension.


### Known issues

  - On macOS, since Catalina and above versions, Native Templates-5.5 will not build with CLI when the compiler is set to **GCC**.
- Emulator
  - In Tizen 5.5 version, the emulator images app uninstallation might take some time to complete if the app name contains more than 14 characters. A patch for the same is expected to be released in the next update.
  - To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, see [Prerequisites for the Tizen SDK](../setup/prerequisites.md).
  - If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows, you must set Tizen Emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [Bumblebee Project](https://wiki.ubuntu.com/Bumblebee){:target="_blank"}. For Windows, select **High Speed NVIDIA&reg; Processor** as **Preferred Graphics Processor** in the NVIDIA&reg; Control Panel.    
  - On Ubuntu, if the graphics driver is out-of-date while launching Emulator Manager, your Ubuntu desktop session occasionally logs out or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows, if an error with the message "failed to allocate memory" occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /setincreaseuserva 3072** command on the console with administrator rights (only in Windows 7), and reboot.
  - If you use a MacBook Pro that has both Intel HD and NVIDIA&reg; GPUs, the emulator can terminate unexpectedly when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the **General** tab in the emulator configuration window, set OpenGL ES version to version 2.0, or to version 3.0.
  - Basic web applications are not installed on SD cards.
  - To use Tizen Emulator in Tizen platform 3.0 or lower, disable the CPU VT option in the **HW Support** tab of emulator configuration.
- CLI and SDB
  - sdb install for rpk is not supported in TV 8.0 emulator(it will be supported in TV 9.0 emulator) and makes sdb freeze, press Ctrl+C to unfreeze.
- Visual Studio
  - NUI XAML application build error can be resolved by doing a clean build.
