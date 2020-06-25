# Tizen Studio 1.0 Release Notes

- Release Date: Sep 1, 2016

## IDE and Tools

### New Features

- Common
  - The name of the **Tizen SDK** has been changed to the **Tizen Studio**. The Tizen Studio 1.0 has been updated from the Tizen 2.4, and a new UX/UI has been applied to it.
  - The Eclipse version has been upgraded from Kepler (4.3) to Mars (4.5.2). For more information, see [https://eclipse.org/mars/noteworthy/](https://eclipse.org/mars/noteworthy/).
- Installer, Package Manager, and Uninstaller
  - The Package Manager supports installing and removing a profile unit. You do not need to install a package one by one for a profile. By clicking the install button next to each profile, you can install all packages for the profile.
  - The Uninstaller allows you to keep the `Data` and `Keystore` directories when you uninstall the Tizen Studio.
- Web and Native IDE
  - The Tizen theme has been renewed. Simple and flat design has been applied to the IDE.
  - The project wizard has been changed and improved.
  - The Configuration (for Web) and Manifest (for native) Editors have been changed and improved.
  - The Certificate Manager has been introduced to easily create and manage a certificate profile. The IDE provides a default certificate profile to develop faster without creating an additional certificate.
  - The default font in the editing views is changed to "Eco Sans Mono", which shows characters more lucidly in the same screen size.
  - Support to develop a Web widget application has been added for the wearable profile.
  - The Dropdown Target Combo has been inserted into the top trim bar of the workbench windows. With this, you can easily launch your projects on a device.
  - Support to develop Tizen 2.3.2-based applications has been added.
- EDC Editor
  - Support has been added for the Wireframe function that displays the outlines for the preview parts.
  - Support has been added for EDC Editor tooltips.
  - Support has been added for a Keyword Reference popup (**F5**), which helps you to understand the EDC grammar.
  - Support has been added for multi-file editing. The **File Browser** and **File** tabs have been added to navigate multiple EDC files.
- Emulator
  - By using the drag and drop operation, you can copy the files and directories of the host computer to the specific location of the emulator instance, and install the application files (WGT, TPK, and RPM).
  - The **Force reboot** menu, which reboots an emulator instance on the hardware level, has been added to the context menu.
  - Without converting the snapshot image (RAW file format) into a qcow2-formatted image, you can launch an emulator instance directly by using the latest snapshot image.
- CLI and SDB
  - Support to develop a Web widget application has been added for the wearable profile.
  - The `manual` command has been added to display the description, syntax, options, and examples of the specific command.
  - Support has been added to develop native widget and watch applications.
  - The use of the `PROJ_PATH`, `BUILD_ARCH`, and `BUILD_CONFIG` environment variables has been added in the `project_def.prop` and `build_def.prop` files.
- Dynamic Analyzer
  - The new UX has been applied to the Dynamic Analyzer.
  - The command line-based interface has been introduced.
  - The template selection during the launch of the Dynamic Analyzer has been change to allow you to select the profiling features. This change leads you easily understand what you want to profile.
  - The memory analysis functionality has been added to analyze memory allocation and application free memory deeply.
  - A marker system has been introduced to add markers to the **Timeline** tab.
  - A range analysis system has been introduced between specific 2 markers or a user-selected area.
  - A dlog table has been added to help you to understand the tracing start and end point.
  - A zoom/scroll key shortcut has been added to handle the Dynamic Analyzer results more conveniently.
  - A screen capture can be conducted without selecting the feature.

### Changed Features

- Installer, Package Manager, and Uninstaller
  - The Tizen Studio does not support OpenJDK any longer. Also, it requires Oracle&reg; JDK 1.8 or higher.
  - The new UX has been applied to the Installer, Package Manager (Update Manager), and Uninstaller.
  - The Update Manager title has been changed to **Package Manager**. The older versions of the Update Manager do not support the auto-update to the new Package Manager. If you want to use the new Package Manager, install the Tizen Studio using the new Installer.
  - The Package Manager tabs have been changed to **Main SDK**, **Extension SDK**, and **Progress**:
    - You can install, update, and remove the main packages in the **Main SDK** tab. In general, there are platforms and SDK tools for each profile in this tab.
    - You can install, update, and remove extended packages in the **Extension SDK** tab.
    - After clicking the install, update, or remove button in the **Main SDK** or **Extension SDK** tab, you can monitor the operation status in the **Progress** tab and on the head area of the Package Manager. You can cancel the operation while installing and updating packages.
- Web and Native IDE
  - Unnecessary Eclipse plugins, such as JDT, PDE, mylin, birt, and egit, have been removed. Consequently, the required disk space for installing the IDE has been decreased about 100 MiB.
  - The new UX has been applied to the **Preference** and **Properties** dialogs. Various abundant items have been removed for simplicity.
  - The `/home/developer/sdk_tools/lib` directory has been excluded in the linking reference of the native project&apos;s `-rpath` option.
- Native UI Builder
  - The new UX has been applied.
  - Due to the new UX, the location of several views has changed:
    - The **Navigation** view has been deprecated and integrated into the **Outline** view.
    - The **Connection Explorer** and **Console** views have been moved to the right pane of the IDE.
  - Due to the new UX, the distances of some mouse movements have been reduced:
    - The alignment toolbar has been moved to the WYSIWYG editor toolbar.
    - The **Palette** has been moved to the right of the **Canvas**.
  - The **Event** tab of the **Properties** view has been removed and its functions have been merged to the **Attribute** tab. The **Attribute** tab provides the event information for a UI component.
  - The **Outline** view provides the UI component hierarchy of an application.
  - The **Palette** has been improved to serve new users better:
    - The UI component category has been redefined for simplicity.
    - The **Palette** has been changed to show only the UI components that can be placed.
- EDC Editor
  - The EDC Editor is renamed from **Enventor**.
  - The new UX has been applied.
  - Support to jump to the part body in the EDC source has been added. Press **F3** when the editor cursor is placed at a referenced part name in the source code.
  - Syntax color has been applied to the error messages in the **Console** view.
  - Only a single **EDC Editor** instance is allowed at a time.
  - Support has been added for an individual group view size and view scale, so that each group keeps its own view size and view scale.
  - Code for various new templates has been added.
  - The `base_scale` value has been applied to the Live Edit object.
  - The main EDC file can be changed in the settings.
  - Help content has been newly designed.
  - Whole macro functions are identified to have syntax color.
- Emulator
  - The new UX has been applied to the Emulator Manager:
    - Simplified main view: the main view provides the menus, such as creating, listing, modifying execution, and deletion for an emulator instance. Comparatively less used features, such as managing platforms and templates, are provided in the Create view.
    - Like the project wizard, the emulator instance creating process has been divided into several steps.
    - To increase understandability and decrease complexity, the emulator configuration has been separated into several tabs.
  - The event injection scenario has been changed. The UX of the Emulator Control Panel (ECP) has been renewed and improved:
    - To improve the user&apos;s concentration on the values of an event injection device, the UX has been designed with a card selection style.
- Toolchain
  - The version of msys (collection of GNU utilities, such as bash, make, and gawk) tools has been upgraded to msys2.
- Dynamic Analyzer
  - Save and load functionalities have been changed to store and restore the trace data on an arbitrary path.

### Fixed Bugs

- Web IDE and Native IDE
  - If JRE 1.8 was installed on your computer and you selected **IDE > Help > Help Contents**, the "HTTP ERROR:500" message sometimes appeared in the Help page due to the Eclipse Kepler bug. This issue has been fixed.
  - Only on Windows&reg;, if the project had a file with its name containing a non-ASCII character, the project packaging sometimes failed. This issue has been fixed.
- Native IDE
  - When you tried to debug an application running on the connected target device through **Debug As > Tizen Native Application - Attach**, you could not attach the debugger to the application by using the **Debug Configurations** dialog. This issue has been fixed.
  - When you exported to the CLI project multiple projects packaged together, and one of the projects was the Static and Shared Library, the information for the referenced library project was not set in the `project_def.prop` file of the reference project. This issue has been fixed.
- Native UI Builder
  - The representation difference issues of the UI component between the layout editor and the emulator have been fixed.
- EDC Editor
  - The map template code typo has been fixed. Previously, the index in the `color[4]` was grammatically wrong. It has been fixed to `color[3]`.
  - The Go to window closing issue has been fixed. The Go to window used to be closed when you just clicked the window title.
  - The dummy swallow/spacer selection issue has been fixed. You could not select the swallow/spacer parts, even when they were on top of the other parts. This was caused by incorrect event handling.
- Emulator
  - Due to an internal problem, the ECP CLI did not provide correct acceleration values for the 3-axis sensors. This issue has been fixed.
- CLI and SDB
  - The build failure of the `.po` files, which occurred if the project type was an IME (Input Method Editor) application, has been fixed.
  - When you executed the parallel build command with the `-j` option on Ubuntu, the `-j` option did not work. This issue has been fixed.

### Known Issues

- Installer, Package Manager, and Uninstaller
  - If the SDK Update Notification appears when you start the Tizen IDE or emulator on macOS, a terminal (`shell.exec`) icon can appear on the dock for a few seconds.
  - If there is a multibyte character in the Tizen SDK installation path, some development packages have a difficulty in finding the installed SDK&apos;s location when they are working.
- Web IDE
  - The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
- Native IDE
  - On Windows&reg;, when you build a native project containing a PO file, the IDE sometimes stops responding. In this case, create a new workspace and move the project to it. The project may be built successfully there.
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows&reg; is running, a project deletion does not work properly. To solve the problem, close the editor.
  - If the WYSIWYG editor of the Native UI Builder for Windows&reg; runs over 12 hours, your computer slows down because of the editor&apos;s high memory usage. To solve the problem, restart the Tizen IDE.
- EDC Editor
  - You cannot add a new EDC file from the IDE if the EDC Editor is already launched. To avoid this problem, quit the EDC Editor before you add a new EDC file.
  - The EDC Editor application instances are limited to a single instance. However, due to a technical issue, multiple EDC Editor instances are allowed on macOS.
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
- SDB
  - To use the SDB bash completion feature, enter the `source .sdb-complete.bash` command on the bash shell. The feature runs manually since the official Tizen 2.4 release due to the Installer and Update Manager issue.
