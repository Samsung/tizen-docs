# Tizen Studio 1.1 Release Notes

- Release Date: Jan 18, 2017

## IDE and Tools

### New Features

- Web and Native IDE

  - The partner-level certificate type for second-party developers has been added. In the Certificate Manager, you can select between the public and partner level when creating a certificate.
  - The **Install New Software** option in the **Help** menu has been reopened.
  - The Tizen ViewManager template has been uploaded.

- Native IDE

  - The Address Sanitizer has been added. It is a fast memory error detector that can be used to detect memory corruption issues in Tizen native applications.
  - The Code Coverage has been added. It is a profiling tool that can be used to find the coverage information for Tizen native applications.

- Native UI Builder

  - The conversion is supported from an existing EFL-code-based project to a new UI Builder project. In the converted project, you can use the UI Builder features and develop new views.
  - The Component Designer tool has been added to the mobile and wearable 3.0 platforms. With it, you can make customized styles for the components by extending and modifying embedded themes.
  - In the UI Builder project for the mobile 3.0 platform, you can change the color property of a UI component.
  - The hoversel UI component has been added to the mobile 2.4 and 3.0 platforms.
  - The **UI Builder - Navigation View (Circle)** project template has been added to the wearable 2.3.1, 2.3.2, and 3.0 platforms.

- Emulator

  - On the Emulator Control Panel, you can enable and disable sensor cards and the NFC card. (This feature is not supported in the Emulator Manager.)

    Any card unsupported by the platform is displayed as a disabled one.

- CLI and SDB

  - Support has been added for referencing other projects for a multi-project application.
  - By using the new `build-app` command with various options, you can build and package multiple projects at once.
  - Support has been added for encrypting all data packets transferred to a target.

- Dynamic Analyzer

  - A Leak Sanitizer tool for memory leak detection has been added to the Heap Allocation profiling in Tizen 3.0.
  - Any application from a single package containing multiple applications can be selected for profiling.

### Changed Features

- Installer, Package Manager, and Uninstaller

  - The UX of the package repository **Configuration** window has been improved through merging 2 tabs. On the new UI, change the **Main SDK** package by doing one of the following:
      - Type the package repository URL or the SDK image path in the text box.
      - Open the file browser through the **...** button on the right side of the text box to locate the SDK image file.
  - The repositories of the **Extension SDK** have been changed and reset along with the package repository of the **Main SDK**.
  - When you select an SDK image for the **Main SDK** package repository, the original repository URL is displayed at the bottom of the text box.

- Web and Native IDE

  - The target device information in the **Target** box on the Tizen Studio toolbar has been detailed by adding information about online or offline, emulator or real device, architecture, and a bit of a target.

  - The naming convention of the package name has been changed to include the target architecture information:

    `{package name}-{package version}-{architecture info}`

  - New path validation rules have been added to the Certificate Manager.

  - The **Notification** popup UI has been improved.

  - The **Rename**, **Delete**, **Close Project**, and **Refresh** commands have been added to the context menu of the project in the **Project Explorer** view.

  - A new UI has been applied to the **Import/Convert** wizard.

  - If the project uses the 3.0 platform or higher, the IDE does not automatically provide the **rpath** option.

- Native UI Builder

  - In the WYSIWYG editor, a new icon for launching the EDC editor has been added to the **layout** UI component.
  - Previously, when the **popup** and **ctxpopup** UI components were executed at runtime, they appeared as new pages on the screen. This has been changed, and they now appear as new windows superimposed on the parent window.
  - The `itemselected` event of the **Index** UI component has been removed from the wearable 2.3, 2.3.1, and 3.0 platforms.

- Emulator

  - By using the keyboard shortcuts on the Emulator Control Panel, you can select a device card and move a page.

- CLI and SDB

  - The speed of the data transfer has been increased by 2.5 to 10 times compared to before.

- Dynamic Analyzer

  - **Persistent Allocations** table is hidden by default.
  - Filter and search functionality is available for all plain tables.
  - Table column resize behavior has been improved.
  - New "Preparing for trace" life-cycle state has been added.
  - New `version` command has been added for the CLI.
  - UI for empty tables has been unified.

### Fixed Bugs

- Web and Native IDE
  - The malfunctions of the **Restore default** option in the **Window > Preferences > Tizen Studio > Native > Debug** and **Properties > Tizen Studio > JSON Properties** settings have been fixed.
  - The bug that caused an error to occur during the IME project installation has been fixed.
  - The RDS failure on Windows&reg; has been fixed.
- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows&reg; ran over 12 hours, your computer slowed down because of the editor&apos;s high memory usage. This issue has been fixed.
- Dynamic Analyzer
  - The launch time on Windows&reg; has been improved.
  - The bug that caused empty fields in the **Texture** table of the OpenGL&reg; ES profiling has been fixed.
  - The bug in screenshot capturing when tracing is started repeatedly has been fixed.
  - The **Reset to default** button behavior in the **Preferences** window has been fixed.
  - The bug that caused an incorrect state in the **View > Report** toggle after trace opening has been fixed.

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
  - The vector-type "part" is not supported. You cannot see the vector image and change the SVG file.
  - Playing sound is not supported on Windows&reg; or macOS.
- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the `ibus-daemon -drx` command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](../setup/prerequisites.md#emulator).
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
  - The Tizen Studio does not support the SDB bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - The Dynamic Analyzer is not available for x86-64 Tizen 3.0 emulators.
  - The UI Hierarchy viewer feature and start-up profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device due to the security policy.
  - The Dynamic Analyzer cannot show life-cycle information for Web applications.
  - Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
- Web Inspector
  - If your Google Chrome&trade; browser version is higher than 54, the Web Inspector console and some other functions do not work properly due to Web core compatibility issues.
