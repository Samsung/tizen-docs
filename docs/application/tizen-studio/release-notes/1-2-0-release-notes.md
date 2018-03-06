# Tizen Studio 1.2 Release Notes

- Release Date: May 10, 2017

## IDE and Tools

### New Features

- Installer, Package Manager, and Uninstaller

  - The Package Manager saves the profile filter state and shows it when launched again.
  - A Tizen Studio for RT installer has been added.

- Native UI Builder

  - You can bind static and remote type data sources to a UI component in the UI Builder. Databinding generates code on the backend and the data is displayed on components at runtime. The data displayed on UI components bound to a remote data source stay in sync with the remote data.

    This feature is available for mobile profiles since Tizen 2.4, and for wearable profiles since Tizen 3.0.

- Dynamic Analyzer

  - Support for using function profiling for application libraries has been added.
  - A memory map can be shown for the selected time.
  - Support for copying and exporting data from tables has been added.
  - Filter and sort icons have been added to the tables.
  - Notification popups on device connect and disconnect have been added.
  - Target connection status icons have been added to the feature selection dialog.
  - A guide text appears on the **Timeline** tab if the connected device does not match the selected device.
  - Features can be configured from the feature selection dialog.
  - A progress bar has been added for time-consuming operations.

- RT IDE

  - You can create RT projects from either a local template or remote Git.
  - You can create RT applications with basic file sets.
  - An easy-to-use build and flash wizard has been added.
  - You can communicate with the board using the **Terminal** view.
  - Code assist and hover functionalities for C source files have been added to the Code Editor.

### Changed Features

- Installer, Package Manager, and Uninstaller
  - On Windows&reg;, the CLI Package Manager now runs as a foreground process that stays in sync with the command line and supports the self-update feature.
- Native UI Builder
  - The new UX has been applied to the **Convert to UI Builder Project** wizard.
- Dynamic Analyzer
  - Memory usage and performance for Heap Allocation profiling has been improved.
  - UI performance has been improved by removing redundant double updates in left table views.
  - In the chart view, the **Analyze range** pop-up menu item has been renamed **Select range**.
  - Logging of SWAP messages has been disabled by default to improve performance.
- Manifest Editor
  - You can add multiple widget classes from the **Advanced** tab.

### Fixed Bugs

- Web and Native IDE
  - The bug where the IDE hangs when a shared library unit test project is run without the &quot;Launch in background&quot; option has been fixed.
  - The bug where the test result field does not display the result when a shared library unit test project is run has been fixed.
- EDC Editor
  - The EDC Editor did not work in Ubuntu due to a current shared library reference error. This issue has been fixed.
- Dynamic Analyzer
  - The bug with incorrect callstack construction has been fixed. The callstack is shown only after tracing is stopped.
  - The behavior of the **Cancel** button in the start tracing progress bar has been fixed.
  - Memory map building has been fixed.
  - The Core Usage feature did not work when it was the only feature selected. This issue has been fixed.
  - The **Callstack** table in the **Memory** tab is now shown only when needed.
- Platform IDE
  - The bug where the IDE failed to build for Tizen 3.0 has been fixed.
  - The bug where the IDE failed to install the output RPM binary using `pkgcmd` has been fixed.

### Known Issues

- Installer, Package Manager, and Uninstaller
  - If there is a multibyte character in the Tizen Studio installation path, some development packages have a difficulty in finding the installation location when they are working.
  - In Windows&reg; CLI Package Manager, the execution file disappears when forcibly terminated (**Ctrl + C**) during execution.
- Web and Native IDE
  - You can create unit tests for Tizen 2.3.2 and higher version projects only. The Tizen Studio currently does not support unit testing for all earlier versions.
- Web IDE
  - The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
  - The unit test application crashes on launch from the Tizen Studio.
- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
- Native UI Builder
  - If the `expanded` attribute in a multibutton entry component is set to `false`, **+** is displayed.
- Native Component Designer
  - The vector-type part is not supported. You cannot see the vector image and change the SVG file.
  - Playing sound is not supported on Windows&reg; or macOS.
  - The Component Designer crashes if an alias is selected as an added item&apos;s source group.
- Emulator
  - To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](../setup/prerequisites.md#emulator).If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA graphics card. For Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). For Windows&reg;, select &quot;High Speed NVIDIA Processor&quot; as &quot;Preferred Graphics processor&quot; in the NVIDIA control panel.On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows&reg;, if a &quot;failed to allocate memory&quot; error occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the `bcdedit /set increaseuserva 3072` command on the console with administrator rights (Windows&reg; 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, when you execute the emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
  - When you launch the Emulator Manager in the Tizen IDE, the Emulator Manager shortcut image is not exposed properly.
  - Basic Web applications do not install on SD cards.
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
