# Tizen Studio 1.1.1 Release Notes

- Release Date: Feb 27, 2017

## IDE and Tools

### Fixed Bugs

- Installer, Package Manager, and Uninstaller
  - The bug that caused the installer to start the installation process even when trying to install the Tizen Studio to a non-existing drive has been fixed.
- Web and Native IDE
  - During the IME project installation, an error occurred and caused the project to occupy 30% of the CPU. This issue has been fixed.
  - The issue where the second debugging stopped when running the application debugging continuously in the Web IDE has been fixed.
  - The tooltip error in the toolbar debug and run icon has been fixed.
- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows&reg; ran over 12 hours, your computer slowed down because of the editor&apos;s high memory usage. This issue has been fixed.
- Emulator
  - The bug that sometimes caused NFC to work improperly or not at all on the emulator has been fixed.
  - The bug that caused WebGL&trade; to fail in watch applications has been fixed.

### Known Issues

- Installer, Package Manager, and Uninstaller
  - If there is a multibyte character in the Tizen Studio installation path, some development packages have a difficulty in finding the installation location when they are working.
- Web and Native IDE
  - You can create unit tests for the Tizen SDK 2.3.2 and higher version projects only. The Tizen Studio currently does not support unit testing for all earlier versions.
- Web IDE
  - The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
- Native Component Designer
  - The vector-type part is not supported. You cannot see the vector image and change the SVG file.
  - Playing sound is not supported on Windows&reg; or macOS.
- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the &apos;ibus-daemon -drx&apos; command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](../setup/prerequisites.md#emulator).If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA graphics card. For Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). For Windows&reg;, select &quot;High Speed NVIDIA Processor&quot; as &quot;Preferred Graphics processor&quot; in the NVIDIA control panel.On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows&reg;, if a &apos;failed to allocate memory&apos; error occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the `bcdedit /set increaseuserva 3072` command on the console with administrator rights (Windows&reg; 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, when you execute the emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- CLI and SDB
  - The Tizen Studio does not support the SDB bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - The Dynamic Analyzer is not available for x86-64 Tizen 3.0 emulators.
  - The UI Hierarchy viewer feature and start-up profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device due to the security policy.
  - The Dynamic Analyzer cannot show life-cycle information for Web applications.
  - Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
- Web Inspector
  - If your Google Chrome&trade; browser version is higher than 54, the Web Inspector console and some other functions do not work properly due to Web core compatibility issues.
  - To debug your watch application, you must use the latest emulator version.
