# Tizen Studio 1.0.1 Release Notes

- Release Date: Oct 28, 2016

## IDE and Tools

### New Features

- Installer, Package Manager, and Uninstaller
  - The Confirm dialog for deleting the emulator has been updated: when user updates the Tizen Studio including the emulators, the Package Manager requires user confirmation to delete the old emulator versions on which the user has created images. Previously, the old emulators and images were deleted without user confirmation. However, since running an old version of images on newer emulators can cause compatibility issues, the Package Manager now opens a dialog to get user confirmation before deleting them. If the user rejects the deletion, the update process is canceled.
- Emulator
  - A default VM instance is provided to run an application without the creation process in the emulator.
  - The high color AOD (Always On Display) is supported in Tizen 2.3.2 wearable applications.
- Dynamic Analyzer
  - A memory call stack trace has been added for all memory allocation traces.
  - A range analysis feature has been added for memory analysis. It enables the user to analyze candidate memory leaks between scenario starts and stops.
  - Persistent memory charts have been added to show the increase or decrease of the memory allocation per each library and executable.
  - The UI Event dialog has been added for the UI Event chart.

### Changed Features

- Web and Native IDE
  - In the Preferences and Properties, Eclipse options have been enabled.
  - In the Remote Device Manager, you can cancel the scanning of nearby devices.
  - The keyboard shortcuts for Preference (**Alt + Shift + Enter**), Emulator Manager (**Alt + Shift + E**), Dynamic Analyzer (**Alt + Shift + D**), Package Manager (**Alt + Shift + P**), and Certificate Manager (**Alt + Shift + C**) have been added. You can see the shortcut information in the **Tools** menu in the Tizen Studio.
  - In the Web IDE, the directory structure of the widget package has been changed.
  - In the Web application configuration editor, a short description of the privilege is displayed.
  - Native project creation has been improved by reducing the latency for indexing.
  - Latency for building a project has been reduced, and unnecessary builds of referred projects have been removed.
- Platform IDE
  - On Ubuntu, the platform IDE has been re-enabled.
- Native UI Builder
  - New feedback UX has been applied in the Design mode.
- Emulator
  - Support has been added for Google Maps&apos; search box in the location card.
- Dynamic Analyzer
  - Memory allocation trace table has been improved. The table name has been changed from **Memory Allocation** to **Persistent Allocation**, to make it clear that the table contains whole un-freed (persistent) memory allocations.
  - Timeline markers pinning a specific event are numbered.
  - Preference selection for the Screenshot feature has changed in both GUI and CLI. You can now select both options at the same time: take a screenshot on scene transition and take it periodically.
  - Memory Map table shows memory mapping data for each process of the traced application.

### Fixed Bugs

- Installer, Package Manager, and Uninstaller
  - Some texts in the Package Manager info dialog were displayed in a different font setting on Windows&reg;. This issue has been fixed.
  - Texts were cut when the font size was set to "Large" on Windows&reg;. This issue has been fixed.
- Native UI Builder
  - on Windows&reg;, when the layout editor was running, the project deletion did not work properly. This issue has been fixed.
- EDC Editor
  - Selected font in the Settings text editor was applied not only to the code text but also to the text in Settings. This issue has been fixed.
  - Input text became non-editable in the Find/Replace and Go to Line windows when the windows were resumed after being minimized on Windows&reg;. This issue has been fixed.
- CLI and SDB
  - When the Remote Device Manager displayed the Gear device connected over Wi-Fi, the device name was shown as "unknown" due to the SDB internal error. This issue has been fixed.
  - The bug, which caused the Unity 5.4.x and 5.5.x project to fail to be packaged, has been fixed.
- Dynamic Analyzer
  - Function profiling information has been fixed to be properly collected and shown.
  - The bug, which caused the selected features not to be updated on a target change, has been fixed.
  - The `--output` option in CLI has been fixed to save the result to the specified path.

### Known Issues

- Installer, Package Manager, and Uninstaller
  - If there is a multibyte character in the Tizen Studio installation path, some development packages have a difficulty in finding the installation location when they are working.
- Web and Native IDE
  - You can create unit tests for the Tizen SDK 2.3.2 and higher version projects only. The Tizen Studio currently does not support unit testing for all earlier versions.
- Web IDE
  - The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
- Native UI Builder
  - If the WYSIWYG editor of the Native UI Builder for Windows&reg; runs over 12 hours, your computer slows down because of the editor&apos;s high memory usage. To solve the problem, restart the Tizen Studio.
- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the `ibus-daemon –drx` command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](../setup/prerequisites.md).
    - If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA graphics card. For Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). For Windows&reg;, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the NVIDIA control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows&reg;, if a 'failed to allocate memory' error occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the `bcdedit /set increaseuserva 3072` command on the console with administrator rights (Windows&reg; 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, when you execute the emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- CLI and SDB
  - To use the SDB bash completion feature, enter the `source .sdb-complete.bash` command on the bash shell. The Tizen Studio does not support the SDB bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - The UI Hierarchy viewer feature and start-up profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device due to the security policy.
