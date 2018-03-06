# Tizen 2.4

Release Date: Oct 30, 2015

The Tizen 2.4 release provides developers with the Tizen kernel, device drivers, middleware subsystems, and Web/native APIs, necessary to develop future Tizen compliant solutions.

#### Release Details

- [Getting source code](http://review.tizen.org/git/) (Tizen 2.4 source code is in the **tizen_2.4** branch.)
- [Getting binaries and images](http://download.tizen.org/releases/2.4/)
- [How to flash to a device](https://wiki.tizen.org/wiki/Flash_Tizen_2.4_Image_to_Reference_Device)


## SDK Release Notes

### Tizen 2.4 Rev8  (Aug. 2, 2016)

#### **IDE and Tools**

**New Features        **

- CLI/SDB
  - When you specify commands to be executed during the pre-build or post-build steps in the build_def.prop file, you can use the PROJ_PATH, BUILD_CONFIG, and BUILD_ARCH environment variables in the commands.

**Changed Features**

- Native UI Builder
  - When you build the UI of a wearable application, you cannot use the Panel UI component. The component is not supported in wearable applications.
  - Support for new APIs for the wearable widget have been added. Old APIs in the project code of the wearable widget, which were shared with the wearable application, have been replaced with the new APIs.

**Fixed Bugs**

- Web IDE
  -  The first execution of the **Build Package** command for Web application projects sometimes failed due to a JavaScript validation problem. This bug has been fixed.
- Native IDE
  - When you tried to debug an application running on a connected target device through the **Debug As > Tizen Native Application – Attach **menu, you could not attach the debugger to the application in the **Debug Configurations** dialog. This bug has been fixed.
  - When you exported a package with multiple projects to a CLI project, and one of the projects was a Static and Shared Library project, the information of the referenced library project was not set in the def.prop file of the reference project. This bug has been fixed.
- Native UI Builder
  - The Tizen Store did not accept a wearable circle application developed by the native UI Builder, because some blacklist APIs were used in the Builder. This bug has been fixed.
  - When an event handler was added to a view layout, if the view layout contained an event-handler-added UI component, an error occurred. This bug has been fixed.
- Emulator
  - Due to an internal problem, the ECP CLI did not provide the correct acceleration values of the 3-axis sensors. This bug has been fixed.

**Known Issues**

- Installer and Update Manager
  - If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.
  - If there is a multibyte character in the Tizen SDK installation path, some development packages cannot find the installed SDK’s location when they are running.
- Web and Native IDE
  - When you select **IDE > Help > Help Contents**, if JRE 1.8 is installed on your computer, the "HTTP ERROR:500" message can appear in the Help page due to an Eclipse Kepler bug. To see the Help page, see [https://developer.tizen.org/development](https://developer.tizen.org/development) or use JRE 1.7.
  - On Windows, if there is a file name in the project containing a non-ASCII character, the project packaging can fail. This issue does not occur on Ubuntu or Mac OS X.
- Web IDE
  - The **Preview** tab in the** Web Page Editor** sometimes does not appear properly. Use an alternative feature, named **Web SDK HTML Editor, **which has enhanced features compared to the** Web Page Editor**. Instead of the** Preview **tab in the **Web Page Editor**, use the preview (**Ctrl+4**) feature of the **Web SDK HTML Editor**.
- Native IDE
  - On Windows, when you build a native project containing a PO file, the IDE sometimes stops responding. In this case, create a new workspace and move the project to it. The project may be built successfully there.
  - When you import some projects generated in Tizen 2.3 Rev2, the import can take some time.
- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows is running, a project deletion does not work properly. To solve the problem, close the editor.
  - If the WYSIWYG editor of the Native UI Builder for Windows runs over 12 hours, your computer slows down because of the editor's high memory usage. To solve the problem, restart the Tizen IDE.
- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the ibus-daemon –drx command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again.
  - On Windows, if a ‘failed to allocate memory’ error occurs while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and Nvidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- SDB
  - To use the SDB bash completion feature, enter the source .sdb-complete.bash command on the bash shell. The feature runs manually from the official Tizen 2.4 release onwards due to the Installer and Update Manager issue.



### Tizen 2.4 Rev7 (Jun. 30, 2016)

#### **IDE and Tools**

**New Features**

- CLI/SDB
  - CLI support for .c, .cc, .cxx, .and .c++ source files has been added.
  - In the CLI, you can use multi-byte character and space character when you specify the path of an workspace and a source file.

**Changed Features**

- Web & Native IDE
  - The IDEs have increased the language support set of the following tools: configuration editor, web localization, manifeset editor, PO editor, and resource manager view.
- Emulator
  - The NFC module value in the wearable circular emulator is set to ON by default.
- CLI/SDB
  - After building on the CLI is finished, the name of the generated .mo file is automatically set to be the same as the name of the IDE.
- JavaScript Analyzer
  - The Stale Object Checker for the Web IDE has been updated to support Windows 10 (64-bit).

**Fixed Bugs**

- Installer and Update Manager
  - The bug, where the SDK Update Notification did not appear when you ran the dynamic analyzer on Mac OS X, has been fixed.
- Web & Native IDE
  - When you tried to convert a project to an earlier version, an error occurred and the conversion failed. This bug has been fixed. You can convert the project to earlier versions.
- Native IDE
  - In a native project, the **Restore Defaults** feature in **Properties >** **C/C++ Build** did not work properly. This bug has been fixed.
  - The project build failure on the Mac OS X, which occurred due to the missing **msgfmt** binary, has been fixed.
- CLI/SDB
  - When you used the package command with the -r option for multi-packaging, a non-signed file was wrongly included in the multi-package. This bug has been fixed.

**Known Issues**

- Installer and Update Manager
  - If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.
- Web & Native IDE
  - When you select in the IDE menu Help > Help Contents, if JRE 1.8 is installed on your computer, the "HTTP ERROR:500" message may appear in the Help page due to an Eclipse Kepler bug. See [https://developer.tizen.org/development](https://developer.tizen.org/development) or use JRE 1.7.
- Web IDE
  - The **Preview** tab in the** Web Page Editor** sometimes does not appear properly. Use an alternative feature, named **Web SDK HTML Editor, **which has enhanced features compared to the** Web Page Editor**. Instead of the** Preview **tab in the **Web Page Editor**, use the preview (**Ctrl+4**) feature of the **Web SDK HTML Editor**.
- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
  - On Windows, when you build a native project containing a PO file, the IDE sometimes stops responding. In this case, create a new workspace and move the project to it. The project may be built successfully there.
- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows is running, a project deletion does not work properly. To solve the problem, close the editor.
  - If the WYSIWYG editor of the Native UI Builder for Windows runs over 12 hours, your computer slows down because of the editor's high memory usage. To solve the problem, restart the Tizen IDE.
  - The Tizen Store currently does not accept a wearable circle app which is developed by the Native UI Builder because some blacklist apis are used in the Builder. This issue will be solved at upcoming release.
- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the ibus-daemon –drx command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again
  - On Windows, if a ‘failed to allocate memory’ error occurs while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and Nvidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- SDB
  - To use the SDB bash completion feature, enter the source .sdb-complete.bash command on the bash shell. The feature runs manually from the official Tizen 2.4 release onwards due to the Installer and Update Manager issue.



### Tizen 2.4 Rev6 (May 19, 2016)

#### IDE and Tools

**Changed Features**

- Installer and Update Manager
  - The notification for the Update Manager, which appears at the bottom right corner of the screen, has been changed to inform you more clearly of the actions (install, update, cancel, or remove).
- CLI/SDB
  - When you copy a file or directory by using the SDB's push command, a "WARNING: Your data is to be sent over an unencrypted connection and could be read by others." security warning message appears to inform you what risk exists in the push command.
  - If you use the SDB’s forward command, the remote port ”0” is disabled.



**Fixed Bugs**

- Installer and Update Manager
  - Since the SDK does not support multi-byte characters, some bugs appeared when you configured an installation directory or folder location in the Installer. This issue has been fixed, and now a function checks the multi-byte characters on the directory and folder path for the Installer.
  - The bug, where the Update Manager sometimes removed meta packages not selected for  removal, has been fixed.
- Native UI Builder
  - The bug that caused abnormal layout rendering on Mac OS has been fixed.
  - The bug, where you could not control the Toolbar UI component, has been fixed.
  - The bug, where you could not apply the timepicker_layout style of the Datetime UI component, has been fixed.
  - The bug, where you could not set the min and max property of the Spinner UI component, has been fixed.
  - The bug, where you could not use the Genlist UI component, has been fixed.
  - In the layout.xml editor, the bugs of the bidirectional editing at the source and user interface level have been fixed.
- Enventor
  - Proper calculation of the indent depth has been fixed after adding a multi-line comment.
  - Title icon is supported on Windows.
  - Compile issue for the empty template code has been fixed. Previously, empty template code was unavailable to build.
  - When adding image template code, the definition part for the defined images has been added to the group template code.
  - Unicode symbols have been fixed to work correctly in redo/undo.
  - Incorrect line increasing has been fixed in the editor when inserting the group template code.
- T-Trace
  - The issue where T-trace sometimes causes UI hangs-up on Window10 has been fixed. This issue is caused by the background thread which checks the SDB connection periodically, and the logic has been changed to check the SDB connection by on-demand, not periodically.



**Known Issues**

- Web IDE

  - The **Preview** tab in the** **Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor**, **which has enhanced features compared to the** **Web Page Editor. Instead of the** Preview **tab in the Web Page Editor, use the preview (Ctrl+4) feature of the Web SDK HTML Editor.

- Installer and Update Manager

  - When you run the dynamic analyzer on Mac OS X, the SDK Update Notification does not appear though there are available SDK updates.
  - If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.

- Native IDE

  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
  - The **Restore Defaults** feature in the native project’s **properties > C/C++ Build** does not work properly.

- Native UI Builder

  - When the WYSIWYG editor of the Native UI Builder for Windows is running, a project deletion does not work properly. To solve the problem, close the editor.
  - If the WYSIWYG editor of the Native UI Builder for Windows runs over 12 hours, your computer slows down because of the editor's high memory usage. To solve the problem, restart the Tizen IDE.

- Emulator

  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to a bug of IBus (Intelligent Input Bus). When the issue occurs, restart the ibus-daemon by entering the ibus-daemon –drx command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver which the vendor provides. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select **High Speed NVIDIA Processor** as **Preferred Graphics processor** in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is out-of-date, the Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparently.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again.
  - On Windows, if a ‘failed to allocate memory’ error occurs while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only). And reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.

- SDB

  - To use the SDB bash completion feature, enter the **source .sdb-complete.bash** command on the bash shell. The feature runs manually from the official Tizen 2.4 release onwards due to the Installer and Update Manager issue.

    ​

#### Tizen 2.4.0 Platform

**Changed Features**

- Security
  - Permission (privilege) check routine has been improved.
  - Enhanced security feature has been applied: prohibition of Openssl SSL v2 APIs



#### Tizen 2.3.1 Platform

**Changed Features**

- Security
  - Permission (privilege) check routine has been improved.
  - Enhanced security feature has been applied: prohibition of Openssl SSL v2 APIs



### Tizen 2.4 Rev5  (Apr. 4, 2016)

#### IDE and Tools

**New Features**

- Installer and Update Manager
  - The Update Manager supports one-click removal of the entire profile and its related packages.
  - On the **All Packages** tab of the Update Manager, the profile filter icon changes to be unclickable when the related profile and packages do not exist in the repository.


- Native IDE
  - The native IDE supports unit testing for UI and service applications.


- Native UI Builder
  - Supported operating systems are updated. You can also use the Native UI Builder on the Mac OS X 10.10 (Yosemite) / 10.9 (Mavericks) / 10.8 (Mountain Lion).
  - The **Source** tab to the layout.xml editor has been added. With the **Design** tab, you can edit the layout.xml file bidirectionally at source and user interface level.The **Source** tab supports the auto-completion and suggestion of element names and attributes.In the **Source** tab, you can edit the layout XML document at source level.The **Preview** tab has been moved to the **Source** tab as an internal pane. The pane shows a read-only preview of the layout.xml file.
  - The app development environment named M-Screen has been added to help you develop an app compatible with supported various screen configurations (resolution, DPI, and orientation).
    - The M-Screen supports UI layoutting for the selected screen configuration.
    - By using alternative resources in the M-Screen, you can localize text strings and optimize images and layouts. 
  - New UI components and view templates are provided:
    - The map component has been added to mobile 2.3, 2.3.1 and 2.4.
    - The calendar and filpselector components have been added to mobile 2.4.
    - The templates forctxpopup and popup components have been added to mobile 2.3, 2.3.1, and 2.4


- Emulator
  - New features and enhancements have been added and applied to the Emulator Manager. The Emulator Manager supports new device templates and the customization of a platform.
  - The 'list-template' command has been added to the Emulator Manager CLI.


- Enventor
  - Supported operating systems are updated. You can also use the Enventor on the Mac OS X 10.10 (Yosemite) / 10.9 (Mavericks) / 10.8 (Mountain Lion).
  - The Editor supports highlighting of open and closed brackets.
  - The statusbar supports the view inverting function (for simulating device rotation).
  - The statusbar supports the live view zooming function.
  - The statusbar supports the view size setting for various resolutions.
  - The EDC Navigator is newly introduced.
  - The Editor contextual popup supports a color selector GUI for “color” keywords.
  - The error detector marks the corresponding lines and guides to the related source code which contains errors in the EDC editor.
  - The Live view supports displaying a dummy spacer.


- Dynamic Analyzer
  - The Table Filtering feature has been added to show the information filtered by the keyword a user set in the analysis results.



**Changed Features**

- Installer and Update Manager
  - If a 32bit version of the JRE/JDK is installed on a 64bit OS, the Installer/Update Manager displays a message leading to install the 64bit version of the JRE/JDK.
  - The CLI Update Manager commands and options have been changed.
    - The 'show-info' command displays equivalent information to the GUI Update Manager.
    - The 'show-pkgs' with '--tree' option displays packages information in the tree structure.
    - When installing a package, the Update Manager installs its required packages together.


- Web IDE
  - The CSS Editor uses CSSLint instead of W3C CSS Validation for syntax check.
  - The JavaScript Editor uses the JSHint instead of the JSLint for syntax check.


- Native IDE
  - You can use the underscore "_", the dash "-", and the period "." in the project name when creating a native project.


- Native UI Builder
  - The **Resource View** has been replaced by the **Resource Manager View**When you open an older project version than 2.4 Rev5, the **Resource View** still remains in the perspective. To update to the **Resource Manager View**, click **Tizen Native** on the Perspective Toolbar, open the context menu, and click **Reset**.
  - The drag-and-drop method of the resource file has been changed.
    - If you drag an image file from the **Project Explorer View** and drop it to the UI component which has an image property (such as image or layout), the path of image file is automatically set to the image property in the **Design** tab.
    - You can drag the resource file from the **Resource Manager View** only in a Tizen 2.4 based project.
  - The meta XML schema of the layout.xml file has been changed by using simple terms for the element name, attribute name, and attribute value instead of somewhat unfamiliar EFL terms.
    - The old schema of the layout.xml is automatically changed to the new schema.
  - UI Component
    - The View Container in the Palette has been removed. The naviframe component in the View Container is also removed.
    - Instead of the removed naviframe, which worked as the background and navigation for the app's views, the Native UI Builder offers simple view-transition methods, such as clicking a component (if its link property is set) on the view object and double-clicking the reference to the view object in the **Navigation View.**
    - The icon component has been removed.
  - Native UI Builder project resources
    - The name of the layout meta file has been changed from "layout.tuml" to "layout.xml".
    - The app.xml file has been removed.


- Enventor
  - Enventor jumps into the related code with the current clicked part in the live view.
  - The Editor popup supports realtime live view updates for the attribution sliders.
  - The auto completion guides offer more correct candidates and code generations.
  - The EDC Editor supports previewing group name macros.
  - Enventor applies auto indentations for a whole source code when it opens an EDC file.
  - The auto indentation logic has been improved for better smart results.
  - The real-time live view updates when undoing and redoing the code.
  - Support for monospace font types has been added.
  - The Editor popup supports the back key to reset the modification.


- Emulator
  - In the the Emulator Manager CLI, to clear the relationship among the options, the option '-p, --path' of 'create-image' command has been changed to the '-d, --directory' ('-p' meant 'platform' and 'path'). 



**Fixed Bugs**

- Installer and Update Manager
  - The SDK update and installation failure from the image file has been fixed.
  - On Mac OS, the installer does not work properly if there are several mounted installers. This bug has been fixed by setting the volume name of the installer in the 'RELEASE_NAME' format.
  - When a user stopped the old installer while installing, the older installer did not delete the installation directory, such as 'tizen-sdk' (default installation directory). This bug has been fixed. The new installer deletes the installation directory if the installation is canceled.


- Web IDE
  - When you open the context menu in the source editor, the **Run Configurations**, **Debug Configurations**, and **Profile Configurations** submenus of **Run As**, **Debug As**, **Profile As** did not appear. This bug has been fixed in this release.
  - The bug that caused the previlege checker not to work properly sometimes has been fixed.


- Enventor
  - Enventor now creates a config home folder properly if it does not exist.
  - The bug that caused the last item in the candidate list to be unselectable has been fixed.
  - Enventor dismisses a contextual popup properly when EDC has a compile error.
  - Enventor dismisses a contextual popup when a warning popup is shown up at window exit.
  - The incorrect display size of the live view has been fixed.
  - The template code logic which was wrongly inserted has been fixed.



**Known Issues**

- Installer and Update Manager
  - Some errors in the update command of the 2.4 rev1 and rev2 CLI Installer have been found. If you use the 2.4 rev1 or rev2 CLI Installer, you fail to update your Tizen SDK. To solve the problem, CLI installer patch files are released. Download the patch at the *download location *and do the following:Open the terminal or command line, and go to the location where the downloaded patch file exists.Move the patch file to the location where the SDK is installed.At the prompt, type **update-manager-cli_2.4_patch update_{OS}_{bit}.{bin|exe}** to install the patch.
  - You can also upgrade your CLI Installer to the 2.4 rev3 at the [Tizen SDK Download page](https://developer.tizen.org/development/tools/download).If there is a multibyte character in the Tizen SDK installation path, some development packages have a difficulty in finding the installed SDK’s location when they are working.When you run the dynamic analyzer on Mac OS X, the SDK Update Notification does not appear even though there are available SDK updates.If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.


- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
  - The **Restore Defaults** feature in the native project’s **Properties > C/C++ Build** does not work properly.


- Native UI Builder
  - When the WYSIWYG editor of the Native UI Builder for Windows is running, project deletion does not work properly. To deal with this problem, close the editor.
  - If the WYSIWYG editor of the Native UI Builder for Windows runs for more than 12 hours, your computer slows down because of the editor's high memory usage. To free  from this situation, restart the Tizen IDE.


- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to an IBus (Intelligent Input Bus) bug. When the issue occurs, restart the ibus-daemon by entering the **ibus-daemon –drx** command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen Emulator from [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again
  - On Windows, if a ‘failed to allocate memory’ error occurred while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /set increaseuserva 3072** command on the console with administrator rights (Windows 7 only), and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.


- SDB
  - To use the SDB bash completion feature, enter the source **.sdb-complete.bash** command on the bash shell. The feature runs manually from Tizen 2.4 official due to the Installer and Update Manager issue.

#### Tizen 2.3.1 Platform

**Changed Features**

- Application
  - The org.tizen.clocksetting GUI has been improved.
- Web UI Framework
  - The GUI of data/time picker of the WebUI framework has been improved.



**Fixed Bugs**

- WRT
  - Support for using the back button in the remote URLs to move to the previous URL has been added.
  - The gID to remove the resource leak in wrt-plugin-tizen has been added.
- ISF
  - The bug that caused some Chinese characters not to appear in the candidate word list has been fixed.
  - The bug that caused the Input panel to hide slowly after the candidate window is shown has been fixed.
- eglibc
  - Patches of CVE-2015-8799 and CVE-2015-7547 for eglibc have been added.



### Tizen 2.4 Rev4 (Mar. 4, 2016)

#### IDE and Tools

**New Features**

- Installer and Update Manager
  - The GUI installer's version information, which was displayed on the title bar, has been moved behind an exclamation mark icon at the bottom-left corner. If you click the icon, a dialog box opens and shows the version information.
  - A prerequisite step to check the free disk space has been added. If there is not enough free disk space, the installation of the Tizen SDK cannot proceed.
  - The CLI installer for Ubuntu allows the tilde character ('~'). When you specify the installation path, you can use the tilde character (it generally refers to the user's home directory).
  - The Manager for Windows uses the SHA256 code signing certificate.
- Native UI Builder
  - The native UI Builder supports Windows 8/7 (64/32-bit) in Tizen 2.3.


- CLI and SDB
  -  A new -r, --rootstrap option has been added to the tizen build-native CLI command. You can build a native application using a rootstrap name.
- Dynamic Analyzer
  - The UI hierarchy analysis supports the Tizen 2.3.1-based devices.



**Changed Features**

- Web IDE
  - Error dialog box, which appears when you launch a project, has been changed to show an original raw message instead of the 'Unknown' message.



**Fixed Bugs**

- Installer and Update Manager
  - The installation failure of the CLI installer for Windows, which did not execute the user input for getting the license agreement or setting the installation path, has been fixed.
  - In Ubuntu, the bug which allowed the user to close the main window of the GUI installer even though the select-directory dialog box was open has been fixed. Now, you can only close the main window after closing the select-directory dialog box.


- Web IDE
  - The bug, where the re-import of a WIDL file failed after removing the WIDL file at the **Project Explorer **view, has been fixed.
- Native IDE
  -  The build failure of a unit test project, which occurred when using the arm build configuration, has been fixed.
  -  The unit test failure, which occurred when you reran the test at the **Unit Test** view, has been fixed.


- CLI and SDB
  - The bug, where the -S, --strip option in the tizen package CLI command did not work properly, has been fixed.



**Known Issues**

- Installer and Update Manager
  -  The update command of the 2.4 rev1 and rev2 CLI installer has some errors. If you use the 2.4 rev1 or rev2 CLI installer, the Tizen SDK update fails.  To solve the problem, download [CLI installer patch files](https://download.tizen.org/sdk/patches/), and do the following (or upgrade your CLI installer to the 2.4 rev3 at the [Tizen SDK Download page](https://developer.tizen.org/development/tools/download).):
    - Open the terminal or command line, and go to the location where you have downloaded the patch file.
    - Move the patch file to the location where the SDK is installed.
    - At the prompt, enter the update-manager-cli_2.4_patch update_{OS}_{bit}.{bin|exe} command to install the patch.
  -  If there is a multibyte character in the Tizen SDK installation path, some development packages have a difficulty in finding the installed SDK’s location when they are working.
  -  When you run the dynamic analyzer on Mac OS X, the SDK Update Notification does not appear though there are available SDK updates.
  -  If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.


- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
  - The **Restore Defaults** feature in the **native project’s properties > C/C++ Build** does not work properly.
- Native UI Builder
  - When the WYSIWYG editor of the native UI Builder for Windows is running, project deletion does not work properly. To deal with this problem, close the editor.
  - If the WYSIWYG editor of the native UI Builder for Windows runs over 12 hours, your computer slows down because of the editor's high memory usage. To deal with this problem, restart the Tizen IDE.


- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to a bug of IBus (Intelligent Input Bus). When the issue occurs, restart the ibus-daemon by entering the ibus-daemon –drx command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver which the vendor provides. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can appear transparently sometimes.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again.
  - On Windows, if a ‘failed to allocate memory’ error occurred while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only). And reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- SDB
  - To use the SDB bash completion feature, enter the source .sdb-complete.bash command on the bash shell. The feature runs manually from Tizen 2.4 official due to the Installer and Update Manager issue.



### Tizen 2.4 Rev3 (Feb. 5, 2016)

#### IDE and Tools

**New Features**

- Common
  - The Update Manager has been upgraded. With the 2.4 and 2.3.1 SDKs, you can also install the 2.3.0 SDK by using the new Update Manager.
  - The remote device manager in the Connection Explorer supports the scanning of the remote targets, such as the emulator and devices connected through Wi-Fi.
- Installer and Update Manager
  - The Update Manager is automatically updated. In addition, it supports the Uninstaller instead of the ‘uninstall all’ feature of the earlier Update Manager.
  - On the **Progress** tab of the Update Manager, you can cancel an ongoing installation and update of the packages individually.


- Web IDE
  - The Select Emulator Wizard has been added. When you launch a project without the emulator, the Wizard helps you to start the emulator which the application runs on and develop the application seamlessly.
  - You can select the highlight color in the Live Editing preferences.


- Native IDE
  - Unit testing for the library project has been updated:
    - Supports the automatic test discovery and XML test report generation, based on the Google test framework.
  - Platform IDE has been enabled:
    - Offers a set of tools that helps you develop preloaded Tizen applications, libraries, and device drivers.
    - Builds a platform module directly from the IDE by using appropriate architecture and rootstrap.
    - Updates the rootstrap automatically.
    - Offers you effective building and debugging tools.
    - Allows you to look up and clone the git repositories.
  - Through the **Problems** view, you can go to the source code of the .edj file that is causing compile errors. The code highlighting is supported.
  - By using the Migration Wizard, you can convert the profile of an imported project from wearable to mobile (or vice versa).


- CLI and SDB
  - Parallel builds for the native application are supported.
  - Application slicing for re-signing the packages has been added.
  - Significant performance improvements for SDB push/pull over the Bluetooth have been added.


- Dynamic Analyzer
  - The UI hierarchy analysis has been added (supports 2.4 mobile applications only). It shows the information of the EFL UI objects (Evas, Elementary, and Edje). It also provides the hierarchy relationship of all UI objects and detailed information of each UI object.
  - The energy analysis for Wi-Fi and Bluetooth has been added. It shows the power consumption of Wi-Fi and Bluetooth (target device only).



**Changed Features**

- Common
  - A new filtering option, Required Version, has been added to the Text filter in the Project Wizard. You can look up the samples built on the version you have entered in the new option.
  - You can type the dot (“.”) in the project name when you create a project.


- Native IDE
  - Native UI Builder has been enabled for developing 2.3.1 project on the Windows OS.


- Installer and Update Manager
  - User interaction messages, which appear when you install the Java, have been changed.
  - The SDK uninstalling process of the Update Manager has been changed.
  - When you uninstall, update, or remove the SDK, the Update Manager checks the SDK version, and informs you whether the Uninstaller must be run.
  - If the version of the installed SDK on your computer is higher than that of the SDK you selected from an outdated repository for installing, the Update Manager recommends you to re-configure the Install Option where the repository option exists.



**Fixed Bugs**

- Common
  - The bug, where the Project Wizard was abnormally closed because of the memory leak, has been fixed. This bug appeared when you created projects continuously over 30 times by using the Project Wizard.


- Web IDE
  - The bug, where you could not go to the source code to which the result view of the unit test refers, has been fixed.


- Installer and Update Manager
  - The stability of downloading the SDK packages has been improved.
  - When you retried the downloading of the SDK package which the Update Manager had failed to download, the retry sometimes did not work correctly. This bug has been fixed.
  - The shortcut name has been changed to ‘**Update Manager**’. 
  - The bug, where an update of the extension packages sometimes failed, has been fixed.


- CLI and SDB
  - The bug, where the SDB failed to connect with Mac OS X 10.11 El Capitan because of the USB misconfiguration, has been fixed.
  - The bug, where the IDE failed to connect with the Tizen TVs 2015, has been fixed.



**Known Issues**

- Installer and Update Manager
  - The update command of the 2.4 rev1 and rev2 CLI Update Manager has some errors. If you use the 2.4 rev1 or rev2 CLI Update Manager, the Tizen SDK update fails.  To solve the problem, use the CLI Update Manager patch files. Download the patch at the *download location *and do the following (or upgrade your CLI Update Manager to the 2.4 rev3 at the [Tizen SDK Download page](https://developer.tizen.org/development/tools/download).). For detailed information, see the [CLI Installer Patch Guide](https://developer.tizen.org/community/tip-tech/patch-cli-installer).
    - Open the terminal or command line (with Administrator privileges on Windows), and go to the location where you have downloaded the patch file.
    - Move the patch file to the location where the SDK is installed.
    - At the prompt, enter the **update-manager-cli_2.4_patch_{OS}{bit}.{bin|exe} **command to install the patch.
  - If there is a multibyte character in the Tizen SDK installation path, some development packages have a difficulty in finding the installed SDK’s location when they are working.
  - When you run the dynamic analyzer on Mac OS X, the SDK Update Notification does not appear though there are available SDK updates. 
  - If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS X, a terminal (shell.exec) icon can appear on the dock for a few seconds.


- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the importing can take some time.
  - The **Restore Defaults** feature in the native project’s **properties > C/C++ Build** does not work properly.
  - When you run some filtered test cases with the native Unit Test tool, the test application can crash.


- Emulator
  - Ubuntu sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to a bug of IBus (Intelligent Input Bus). When the issue occurs, restart the ibus-daemon by entering the ibus-daemon –drx command at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver which the vendor provides. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu 14.04, a shortcut menu can appear transparently sometimes.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again.
  - On Windows, if a ‘failed to allocate memory’ error occurred while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only). And reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the Emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
- SDB
  - To use the SDB bash completion feature, enter the source .sdb-complete.bash command on the bash shell. The feature runs manually from Tizen 2.4 official due to the Installer and Update Manager issue.



#### Tizen 2.4.0 Platform

**Changed Features**

- UI Framework
  - he Ecore_Buffer header has been changed to remove forward references to the enum type for C++.

**Fixed Bugs**

- Application Framework

  - Some fixes have been made for bugs, including an undeleted child process in the debug-launchpad.


#### Tizen 2.3.1 Platform

**New Features**

- Network Connectivity
  - Push features for the wearable profile have been enabled.

**Changed Features**

- UI Framework
  - Color emoji font has been updated. It is now the same as the color emoji font in Tizen 2.4.

**Fixed Bugs**

- Application
  - A bug, where the wearable home screen layout broke when the widget name was long and widgets were listed only if they had a supported size type (in case of the wearable, only the 2x2 size widget can be used), has been fixed.


- Application FW
  - The bug, where amd could not get the dead signal from the debug-Launchpad when an application was terminated, has been fixed.
  - The bug, which caused an application package using a higher API version than the platform-supported API version to be installed successfully, has been fixed.


- Network Connectivity
  - A bug for NFC Tag Read/Write in the wearable emulator has been fixed.



### Tizen 2.4 Rev2 (Dec. 23, 2015)

#### IDE and Tools

**Fixed Bugs**

- Web IDE
  - The bug, which caused the TV-Extension-installed SDK to fail to install and launch a TV application on the target, such as the Tizen emulator, has been fixed.
  - The library conflict between the TV-Extension and the SDK, which occurs when the TV-Extension-installed SDK debugs an application, has been fixed.
- Web Inspector
  - The bug, which caused the socket connection between the Web Inspector and the Tizen emulator to close, has been fixed.



### Tizen 2.4 Rev1 (Dec. 1, 2015)

#### IDE and Tools

**New Features**

- Common
  - **Tizen 2.4 Rev1 SDK supports developing an application on multi-platform environments. In the 2.4 Rev1 SDK, you can also develop 2.3.1 based applications.**
  - **From Tizen 2.4 Rev1, the SDK image installation is not officially supported. Use the Tizen package server for installation. **
  - From Tizen 2.4 Rev1, the Update Manager supports the package server mirroring. Without uninstalling the Tizen SDK, you can enhance the installation speed of the new SDK version by changing the target repository address to an alternative repository that exists in your country or region.
- CLI
  - Support has been added for the package/install/run/uninstall features for the 2.3.0 projects.
- Native UIB and Enventor
  - Supports the following host operating systems :
    - Tizen 2.3.1 (Mobile/Wearable): Ubuntu™ 12.04/14.04 32-bit/64-bit
    - Tizen 2.4 (Mobile): Ubuntu™ 12.04/14.04 32-bit/64-bit, Windows 7/8 32-bit/64bit

**Changed Features**

- Common
  - The Project wizard has been enhanced to be opened and closed faster than in the 2.4 official version.
  - To improve the security of a connected Tizen device, the execute permission has been changed from the root/administrator to the developer in some features that control the device, such as the dynamic analyzer and SDBD.
  - The IDE has been changed to hold the settings (**filter, log level, category**) of the Log view after the device is disconnected.
  - The default value for the **log level **property of the Log view has been changed from **Verbose** to **Error**.
- Installer and Update Manager
  - A combo box has been added to the Update Manager to easily change the URL of the target repository.
- Web IDE
  - The Localize wizard has been replaced with the Localization view.
    - You can localize your resource files and strings.
    - You can export or import a localized string as a CSV (comma-separated value) file.
- Native IDE
  - The content/code assist feature has been added for the **i18n_get_text()** function. After you complete the **i18n_get_text()** function on the C/C++ source file editor by pressing **Ctrl + Space**, you can see a candidate parameter list which consists of original untranslated strings you added to the PO file.
  - When you develop a multi-project packaged application (such as a combination of UI and service projects, or UI and shared library projects), the res.xml files of the projects are automatically merged. If a project has no res.xml file, a res.xml is automatically generated for that project and merged with the other res.xml files. 
  - The “Export to CLI” menu has been added, and appears when multiple projects are selected, .
  - The Resource Explorer view has been added. It appears only for Tizen 2.4-based projects, not Tizen 2.3.1.
  - Multi-project packaging policy has been updated.
    - A Web UI project can be packaged with several native-widget type projects.
    - A native IME project can be packaged with several UI application type projects.

**Fixed Bugs**

- Common
  - The Apple JDK dependency issue, which appeared when starting the Tizen IDE and dynamic analyzer, has been fixed.
- Native IDEThe bug, which caused unnecessary files (such as .EDC file) to be included when native modules were packaged into the .tpk file, has been fixed.
- CLI
  - The bug, which caused the native CLI to return success codes even though a build failed, has been fixed.

**Known Issues**

- Installer and Update Manager
  - If there is a multibyte character in the installation path of the Tizen SDK, some development packages cannot find the installed SDK’s location when they are working.
  - When you install packages by using the All Packages tab in the Update Manager, the number of the progress indicator is only changed each time a package in dependency is downloaded. While downloading, the number of the progress indicator is not changed. 
  - When you run the dynamic analyzer on Mac OS, the SDK Update Notification does not appear though there are available SDK updates.
  - If the SDK Update Notification appears when you start the Tizen IDE or Emulator on Mac OS, a terminal (shell.exec) icon can appear on the dock for a few seconds.
- Native IDE
  - When you import some projects generated from Tizen 2.3 Rev2, the import can take some time.
  - The **Restore Defaults **feature in the Native project’s **properties > C/C++ Build**, does not work properly.
- Emulator
  - Ubuntu™ sometimes stops responding for a few seconds after closing the Emulator Manager. This issue is related to a bug of IBus (Intelligent Input Bus). When the issue occurs, restart the ibus-daemon by typing **ibus-daemon –drx** at the command prompt, and use another framework, such as uim and fcitx, for multilingual input.
  - To use the Tizen Emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor.
    - Check the prerequisites for the Tizen Emulator from:
      [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk).
    - If the host machine is using the Nvidia Optimus™ technology on either Ubuntu™ or Windows, you must set the Tizen Emulator to run with your Nvidia graphics card. If you use Ubuntu™, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). If you use Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu™, if the graphics driver is outdated, your Ubuntu™ desktop session can be occasionally logged out when launching the Emulator Manager, or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
  - On Ubuntu™ 14.04, the shortcut menu can sometimes appear transparently.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered by another window. If you click the Emulator window, the display surface runs correctly again
  - On Windows, if a memory allocation error occurs while executing the Emulator, try  the following:
    - Close some other programs and try to launch the Emulator again
    - If the RAM size is set as 768 or 1024 MB for the VM in the Emulator Manager, change the RAM size to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by typing **bcdedit /set increaseuserva 3072** on the console with administrator rights (Windows 7 only) and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, the Emulator may be unexpectedly terminated when you execute with the OpenGL ES ver. v1.1 & v2.0 option. Use the OpenGL ES ver. v2.0 & v3.0 option.
- SDBTo use the SDB bash completion feature, type the **source .sdb-complete.bash** command on the bash shell. The feature runs manually from the Tizen 2.4 official version due to the Installer and Update Manager issue.
- Native UIB
  - The Native UIB does not support the storyboard for the Tizen 2.3.1 platforms.



### Tizen 2.4

#### IDE and Tools

**New Features**

- Web IDE and Tools
  - Rest Viewer has been added.
  - Multi Package preference panel has been added to **Project Properties > Tizen SDK > Package**. You must refer projects to other projects in this panel, not in the Project Reference panel. The hybrid project referencing feature is removed from the Project Reference panel.
- Native IDE
  - New project template types (IME, widget, and watch) have been added.
  - Project migration wizard, which imports 2.3-based projects for making 2.4-based projects, has been added.
  - Resource Manager View, which places application resources to support specific device configurations, such as different screen densities and locales, has been added.
  - Select Emulator Wizard, which calls a previously run emulator automatically while ‘Run As’ is called and Emulator Manager is not running, has been added.
  - Ninja build system for enhancing the application build time has been added.
  - LLVM-3.6 and GCC-4.9 toolchains have been added.
  - New function generating author signatures to support App slicing has been added.
  - New function exporting an IDE project to a CLI project has been added.
- Native UI Builder
  - Supports the following host operating systems:
    - Windows 7 32-bit/64-bit and Windows 8 32-bit/64-bit
    - Ubuntu 12.04 32-bit/64-bit and Ubuntu 14.04 32-bit/64-bit
  - Supports the making of a custom UI component by combining ready-made UI components.
  - Provides a storyboard, which represents a transition from one view to the next.
- Eventor
  - Supports the following host operating systems:
    - Windows 7 32-bit/64-bit and Windows 8 32-bit/64-bit
    - Ubuntu 12.04 32-bit/64-bit and Ubuntu 14.04 32-bit/64-bit
- Emulator
  - SMP with CPU VT acceleration is enabled for enhancing performance.
  - OpenGL ES 3.0 is supported.
  - Virtual camera is supported. Applications which use a camera can be developed without a Webcam.
  - Multi-touch simulation has been added. Multi-touch drag and pinch-zoom gestures are also supported.
  - H.264 video compression format is supported.
  - Bridged networking feature is enabled. It can connect the emulator to  the PC’s Ethernet adapter directly.
  - Proxy setting is enabled in the Emulator Manager. It allows the emulator to get a proxy network separated from the PC network.
  - Sharing host PC’s directories with the emulator is supported. The shared directory can be added or removed in the ECP (Emulator Control Panel) while the emulator is running.
  - Low-memory event in the ECP has been added.
  - Shortcut keys for Windows and Ubuntu have been added. **Ctrl + Shift + S **or **Ctrl + F6  **can be used to open the sdb shell when the emulator is focused.
- Dynamic Analyzer
  - Checkpoint analysis has been added. It displays the checked variable value of the application in real time.
  - App startup analysis has been added. It displays information both before and after the application starts.
  - UI gesture event chart has been added. It displays the UI application’s gesture events.
- T-trace
  - Profiling tool has been added to optimize the application performance by measuring and visualizing instrumented function calls in the Tizen platform.
- Stale Object Checker
  - Dynamic analysis tool has been added to examine whether JavaScript objects of a Web application can cause possible memory leaks.
- CLI
  - Certificate management named 'Security Profiles' has been added, to enable developer certificates to sign Tizen applications.

**Changed Features**

- Web IDE and tools
  - Various sample projects can be downloaded in the Online Sample of the New Project Wizard.
  - Localization Wizard has been changed to Localization View. If you click Localization in the project shortcut menu, the Localization View appears.
- Native IDE
  - PO editor’s UX has been improved.
- Native UI Builder
  - Some “widget” terms have been changed to “UI component”.
  - WYSIWYG UX has been improved.
    - Z-order index (back, backward, front, frontward) of the UI components arranged on the canvas can be changed.
    - UI components can overlap each other.
    - UI components can be handled outside the canvas.
    - UX of selecting a container UI component (box) has been improved.
    - UX of Direct Text Editing has been added.
  - View template category has been removed.
  - Method for selecting a view in the Navigation view has been changed from a single-click to double-click.
- TEP (Tizen Expansion Package) feature will be supported in the later  version.

**Fixed Bugs**

- Web IDE and tools
  - The bug, where a wrong hyperlink appears when the log message at the JavaScript console contains a number, has been fixed.
- Emulator
  - The bug, which appears while installing the Tizen HAX driver on a computer where Android HAX driver is already installed, has been fixed. The Tizen HAX driver overwrites the Android HAX driver.
  - The bug, where the emulator is terminated abnormally due to the misconfiguration of SOCKS (SOCKet Secure) proxy on Mac OS X, has been fixed.

**Known Issues**

- Install Manager and Update Manager
  - If there is a multibyte character in the installation path of the Tizen SDK, some development packages cannot find the installed SDK’s location when they are working.
  - When you install packages by using the All Packages tab in the Update Manager, the number of the progress indicator is changed only each time a package in dependency is downloaded. While downloading, the number of the progress indicator is not changed. 
- Native IDE
  - Generating the res.xml file in Multi-Packaged projects is not available.
  - When you import some projects generated from the Tizen 2.3 Rev2 SDK, the importing can take some time.
- Emulator
  - To use the Tizen Emulator, you must install an Intel VTx supported by the CPU, and the latest version of the graphic card driver which the vendor provides. Check the prerequisites for the Tizen Emulator from:
    - [https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk](https://developer.tizen.org/downloads/sdk/installing-sdk/prerequisites-tizen-sdk)
    - If the host machine is using Nvidia Optimus™ technology on either Ubuntu™ or Windows, set the Tizen Emulator to run with your Nvidia graphics card. In case of Ubuntu™, check the bumblebee project ([https://wiki.ubuntu.com/Bumblebee](https://wiki.ubuntu.com/Bumblebee)). In case of Windows, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the Nvidia control panel.
    - On Ubuntu™, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager. Or the Emulator skin can be drawn improperly. Check the prerequisites and upgrade the latest graphics driver.
  - On Ubuntu™ 14.04, the shortcut menu can sometimes appear transparently.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the Emulator window is covered with another window. If you click the Emulator window, the display surface runs correctly again.
  - On Windows, if ‘failed to allocate memory’ error occurs while executing the Emulator, try the following:
    - Close some other programs and try to launch the Emulator again.
    - If the RAM size is set as 768 or 1024 MB for the VM in the Emulator Manager, change the RAM size to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by typing the bcdedit /set increaseuserva 3072 command on the console with administrator rights (Windows 7 only) and reboot.
  - If you use a MacBook Pro which has both Intel HD and NVidia GPUs, when you execute the Emulator with the OpenGL ES ver. v1.1 & v2.0 option, the Emulator can be unexpectedly terminated. Use the OpenGL ES ver. v2.0 & v3.0 option.
- SDB
  - To use the SDB bash completion feature, you must type the source .sdb-complete.bash command on the bash shell. The feature runs manually from the Tizen 2.4 due to the Installer and Update Manager issue.

#### UI FW

New Features

-  Tizen 2015 UX support has been added (new winset and style).
-  Vector winset support has been added.
-  Unicode 6.1 Colored Emoticons have been added.
-  Gamepad support has been added.
-  Cancel Event support has been added.
-  ATK has been integrated.
-  Ecore Buffer has been added.
  - New API abstracts the graphic buffer and allows you to share it between processes.

**Change Notes**

- Open source upgrade
  - EFL version has been upgraded from 1.7 to 1.13.
- API changes
  - Eina_Bool edje_text_class_get (const char *text_class, char **font, Evas_Font_Size *size) has been changed to  Eina_Bool edje_text_class_get (const char *text_class, const char **font, Evas_Font_Size *size).
  - void elm_win_wm_rotation_preferred_rotation_set(Evas_Object *obj, const int rotation) has been changed to void elm_win_wm_rotation_preferred_rotation_set(const Evas_Object *obj, int rotation).

#### Network Connectivity

**New Features**

- NFC
  - New HCE (Host Card Emulation) APIs for NFC has been added.
- Smartcard
  - New APIs for smartcards (Smartcard API) have been added.
- Bluetooth
  - New APIs for AVRCP have been added.
  - SDK extension APIs have been moved into bluetooth_extension.h.
- Connection Manager
  - New API to get MAC address has been added.
  - New APIs for Ethernet cable state have been added.
- Wi-Fi 
  - New APIs for a specific scan have been added.
  - New APIs for Wi-Fi configuration have been added.
- Wi-Fi direct
  - New APIs for a Wi-Fi display have been added.
- Telephony
  - New APIs for a call status have been added.
  - New APIs for a modem power status have been added.
  - New APIs for SIM application lists have been added.
  - New APIs for a network have been added.

** Change Notes**

- Open source upgrade
  - ConnMan has been upgraded from 1.3.313 to 1.29.15.
  - Bluez has been upgraded from 5.27 to 5.28.
  - libsoup has been upgraded from 2.38.1 to 2.46.0, gnutls from 2.12.20 to 3.3.5, and glib-networking from 2.32.3 to 2.38.0.
- Notice of deprecated APIs
  - Bluetooth
    - Legacy LE discovery APIs have been deprecated.
    - Legacy GATT client APIs have been deprecated.
  - Wi-Fi Direct
  - Telephony
    - Call status API has been deprecated. 

#### Contact and Calendar Service

**New Features**

- New APIs for the phonenumber-utils module (phone number location, formatting, location data replace) have been added.
- Lunar calendar has been added in the Event schedule.

**Change Notes**

- PIMS-ipc abnormal disconnection recovery feature has been added.
- _contacts_event.is_leap_month property has been deprecated.
- On-demand launching has been applied.

#### Multimedia FW

**New Features**

- Media Content
  - Empty folder management support has been added.
  - Mass-storage scanning has been added.
  - Export and Import Playlist File (.m3u) service has been added.
- Media Controller
  - Media Controller Service has  been added.
- Mediavision
  - Mediavision component, supporting generation and detection of various barcodes (such as UPC-A, CODE128, and QR) has been added.
- Camera
  - New API to get the FPS list in each resolution has been added.
  - T-trace support has been added.
- Recorder
  - Maximum file size in the recording has been increased (larger than 4 GB).
- Image util
  - NV12 for JPEG encoding/decoding support has been added.
  - Jpeg downscale decoding support has been added.
- Player
  - New APIs to play a demuxed AV elementary stream which is pushed from application have been added.
  - New APIs to monitor the QoS of the elementary stream have been added.
  - New APIs to give notifications about the changing of the video stream have been added.
  - New APIs to select the audio and subtitle language have been added.
- Audio I/O 
  - New APIs to flush the playback/capture stream have been added.
  - New API to drain the playback stream has been added.
- Media codec
  - New API to query which codecs are supported has been added.
  - New API to flush buffers has been added.
  - New API to check the buffer status has been added.
- Media tool
  - New APIs to get some TBM surface info have been added.
  - New API to get codec data has been added.
  - New enum in media_format_mimetype_e has been added.
- Radio
  - New API to get the min. and max. frequency has been added.
  - New API to get the channel spacing value has been added.
- Metadata Editor
  - Media Content metadata editing service has been added.
- Thumbnail Util
  - Support for extracting a thumbnail in various resolutions has been added.
- Screen Mirroring
  - Sink device can play the mirrored stream.

**Change Notes**

- Media Content
  - Exposure time, fnumber, iso, and model can be extracted from Exif.
  - media_info_increase_played_count() has replaced video_meta_set_played_count() and audio_meta_set_played_count().
  - media_info_set_played_time() has replaced video_meta_set_played_time() and audio_meta_set_played_time().
- Camera 
  - Flash control behavior has changed. (Flash control can fail if the flash is pre-empted by another API.)
  - Code for removing remaining messages when destroying a handle has been updated.
  - dbus has been replaced with gdbus.
  - Signal handler has been added to reset vconf keys updated by the camera and recorder.
  - MMVideoBuffer has been applied.
- Notice
  - Media Content ignores the hidden file and the hidden folder.
  - ffmpeg (1.0) has been replaced with libav (11.3).
  - GStreamer0.10.36 ´has been replaced with GStreamer1.4.5.

#### Email and Message Service

**New Features**

- SMS, CB, and PUSH incoming message events are published using the event-system.

**Change Notes**

- vconf-keys have been moved from the spec file into 'vconf-internal-keys'.
- Unused vconf-keys have been removed.

#### Context/Location/Account/Interaction FW

**New Features**

- Context FW
  - New Contextual Trigger APIs have been added for creating context-aware app-launching and notification rules, based on time, several device status and events, and communication events.
  - New Contextual History APIs have been added for getting device usage statistics, including what are the most frequently, recently, and rarely used applications, and when the user most intensively uses the applications or listens to music.
- Interaction FW
  - Voice control
    - New APIs to control application features with voice recognition have been added.
    - New APIs to control EFL-supported UI components with voice recognition have been added.
  - Text Input
    - New APIs to develop downloadable Native IME have been added.
    - New APIs to manage IMEs (providing list and selector menus) have been added.
- Account FW
  - Account Manager
    - Account connect/disconnect APIs have been deprecated to avoid applications using them inappropriately.
  - Sync Manager
    - New APIs to schedule the operation of applications which need synchronization with a server have been added.
  - OAuth 2.0
    -  New APIs for easy usage of the OAuth 2.0 protocol have been added.
- Location FW 
  - Location Manager
    - New API for distance-based location updates has been added.
    - New API to enable location with the [http://tizen.org/privilege/location.enable](http://tizen.org/privilege/location.enable) privilege has been added.
    - New API for location update callback has been added.
  - Maps Service 
    - New Maps Service API (Geocoder, Places, and Routes) has been added.
    - Support for the HereMaps plugin based on the HERE REST API has been added.
  - Geofence Manager (Mobile) 
    - New Geofence Manager API has been added.

**Known Issues **

- Geofence Manager 
  - This feature is optional, and is only supported is certain device models.

#### Web UI Framework (TAU)

**New Features**

- Tizen 2015 UX (new UI and style)
  - New floating actions, PanelChanger, PageIndicator, SectionChanger and Tabs have been added as UI components.
- Gesture Event APIs that help to detect the user gesturing input have been added.
- Animation Utility that provides APIs to easily animate DOM elements with great performance has been added.
- Globalization Utility that provides APIs to convert user-entered string, date, or numbers into a country-specific format has been added.

**Change Notes**

- Changed APIs
  - CheckboxRadio has been separated into Checkbox and Radio.
  - Collapsible has been renamed to Expandable.
  - FastScroll has been renamed to IndexScrollbar.
  - ProgressBar has been renamed to Progress.
  - SelectMenu has been renamed to DropdownMenu.
  - TokenTextArea has been renamed to TextEnveloper.
  - A plugin, "support-2.3", is provided for backward compatibility.
- Deprecated APIs
  - Gallery, Autodividers, ControlGroup, DatetimePicker, MultimediaView, Notification, ScrollHandler, and Swipe have been deprecated.

#### Graphics

**New Features**

- DALi has been added.
  - OpenGL ES-based light-weight rendering engine
  - Dedicated rendering thread and resource loading threads
  - 2D and 3D draw mode
  - Basic UI components
    - TextField
    - TextLabel
    - ImageView
    - Buttons
    - TableView
    - ItemView
    - ScrollView
    - ScrollBar
    - GaussianBlurView
  - Properties-based animations
  - Platform adaptation 
    - Virtual keyboard
    - Clipboard
    - Native application life-cycle management
- Evas GL/Engine
  - Support for OpenGL ES 3.0 has been added.
  - Support for DRI3 in SW-X11 Backend has been added.
- CoreGL
  - Support for driver-independent performance optimization (called FASTPATH) has been added.
  - Helps OpenGL ES v2.0 debugging.
  - Provides performance logging (called TRACEPATH).

**Change Notes**

- Evas GL/Engine
  - Provides Evas GL Context Restoring when the current context is changed.
  - Evas GL cache files (shader, capability) have been recreated by micro version.
  - Render buffer has been changed from pixmap to FBO for GLES 1.1 and 3.0.
- ARM Mali driver (kernel & OpenGL ES driver)
  - Driver version has been updated to r4p0 from r3p0.
  - TIZEN_image_native_surface feature has been added.
  - Support for DRI3 has been added.
  - Surface pitch alignment has been changed from 8 bytes to 64 bytes.

#### Applications

**New Reference Applications**

- Call, Message, Email, Video, Music, and more have been added.

**New Features**

- Attach panel
  - Module to help attach content with ease has been added.
  - New set of APIs have been added.
  - Gallery, Camera, Voice-recorder, and many applications can be used to attach various types of content.
- Share panel
  - Module to share content with ease has been added.
  - You can call the share panel with the app_control protocol.

#### Application FW

**New Features**

- Application background policy
  - Restricting CPU resources for background application processes has been added according to the background categories that are specified in the application manifest.
- Alarm API
  - Alarm APIs for inexact periodic processing have been added.
- App group launching management API
  - New API to group applications has been added.
- Application event system
  - New API to handle event broadcasting has been added.
- Resource management API for multiple devices
  - New API to get a proper resource for multiple devices has been added.

**Change Notes**

- Alarm API
  - Alarm API has been changed to support explicit app control only.
  - Some alarm APIs have been changed to register UI applications only.

#### Windows System

**New Features**

-  X11
  - Two X input drivers have been integrated into one:
    X Evdev + X Evdev-multitouch => X Evdev
  - Support for the pointer barrier which restricts pointer movement has been added.
  - Support for input event generation for touchscreen and hardware key devices has been added.
  - Support for input redirection has been added to enable input event redirection to the transformed windows by compositor.
  - Support for keycode remapping has been added to remap the keycode more than 248 in the X Evdev driver.
  - Support for touch cancel event generation has been added.
  - Support for DRI3 and Present extension has been added.
  - Support for HWA (hardware access) extension has been added.
-  EOM
  - New APIs for EOM (External Output Manager) have been added.
-  Window Manager
  - Support for window and input transformation has been added.
  - Support for starting a window with an iconic state has been added.
  - Support for screen on/off control using the pm-helper module has been added.
  - Support for Ecore_buffer management has been added.
  - tizen-ws-shell library has been provided for communicating between the window manager and system service applications.

**Change Notes**

- X11
  - xorg-server has been upgraded from 1.13.0 to 1.16.0.
  - [Profile] ttrace has been added to xorg-server.
  - [DRI2] DRI2SwapBuffers are skipped when the size of the front buffer differs from the back buffer.
  - [DRI2] Sync draw done at DRI2SwapBuffers is sent.
  - [XV] Access control mechanism has been added regarding the screen capture request (XVPutStill).
  - [Input] Access control mechanism has been added regarding input event generation.
- Window Manager
  - e17.service file has been moved to each e17-misc-xxx package from the e17 package.
  - Modules have been separated to e17-mod-tizen-xxx.
  - Blinking problem when the window manager is restarted has been fixed.
- TBM
  - drm_slp so file has been removed.
  - Creation of tbm_surface with multiple buffers is allowed.

**Known Issues **

- X11
  - Emulator X video driver does not support DRI3 and Present extension.

#### Settings and Base library

**New Features**

- New tizen locale (ckb_IR, ckb_IQ, raj_IN, ce_RU) has been added.
- XML-based configuration tool has been adopted for all modules (vconf-internal-keys).
  - Content in vconf-keys.h has been moved from 'vconf' into 'vconf-internal-keys' (refactoring).
  - All unused keys have been removed.
  - All un-initialized keys have been removed.

**Change Notes**

- Open-source base libraries
  - Upgrades: SQLite3, glib2, json-glib, json-c, and boost
  - Patches: swig, libsolve, libzypp, python, tizen-locale, and tzdata
  - Security patches: procps, gawk and etc.
- org.tizen.setting
  - Enhanced EFL library has been adopted.
  - Tizen 2.4 coding rules have been adopted.
  - More than 120 vconf keys have been removed from the spec and moved to vconf-internal-keys.
  - Event system functions have been moved to system settings and changed the calls with system-settings. (Refactoring)
- system-settings
  - More than 100 UTC test-cases (system-settings) have been added and ITC, UTC test made to pass with 100%.
  - Bugs have been fixed: between logic, get/set/notifiers from EAP binary (2.3.1)
  - Event-system has been integrated into system-settings.

#### Convergence Service FW

**New Features**

- New APIs for Service-Adaptor have been added.
  - You can use a public infrastructure (such as Cloud Storage) as a local device.

#### Web Runtime/Web Device APIs

**New Features**

- Media controller API
  - This interface provides a media server (which plays media content) and a client interface (which requests the server to control the media server state, such as play and pause).
  - Normally, the server and client are created by the same application developer and the client can act as a remote controller for the media server.
  - It helps to transfer the information, such as playback info, shuffle/repeat mode, and metadata, from the media controller server to client.
  - You can control the server state by sending commands from the client.
- Application API
  - Application interface provides application event broadcasting and listening features. The application can broadcast user events to other listening applications.
  - "GROUP" mode has been added to the Application API, and used to set an application group before launching an application using the Application Control. Specifies the application launch mode when the application is launched by the launchAppControl() method.
- SystemInformation API
  - SystemInfoCameraFlash interface has been added to control the camera flash (getter and setter for the brightness of the camera flash).
  - SystemInfoEthernetNetwork interface has been added to get Ethernet information, such as IP address, mac address, and status.
- Notification API
  - playLEDCustomEffect() and stopLEDCustomEffect() methods have been added in the NotificationManager interface to control the LED of the device.
  - You can play the custom effect of the service LED that is located on the front of a device.
- Contents API
  - scanDirectory() and cancelScanDirectory() methods have been added to the ContentManager interface to perform media content scanning of a specific directory.
- Bluetooth API
  - Bluetooth LE-related interfaces have been added.
  - API is related to the [http://tizen.org/feature/network.bluetooth.le](http://tizen.org/feature/network.bluetooth.le) feature.
- InputDevice API
  - This interface provides functions to subscribe to the key events of the input device.
  - You can handle device-dependent key events after registration.
- NFC API
  - NFC host-based card emulation interfaces have been added.
  - They are only supported on the HCE-enabled devices (no SDK support).
  - API is related to the [http://tizen.org/feature/network.nfc.card_emulation.hce](http://tizen.org/feature/network.nfc.card_emulation.hce) feature.
- Web Runtime
  - In the tizen:application element in the config.xml file, "launch_mode" is added to set the launch mode to "single", "caller", or "group". For more information, see Guides > Native Application > Application Framework > Application Group.
  - In the tizen:app-control element in the config.xml file, "reload" is added to enable or disable a page reload when an application control request is received.
  - Feature for restricting CPU resources for a background application process according to the background categories that are specified in the config.xml file has been added.

**Change Notes**

- BT privileges ([http://tizen.org/privilege/bluetooth.xx](http://tizen.org/privilege/bluetooth.xx)) have been deprecated to synchronize the privilege names between Web and native Bluetooth APIs. From 2.4, [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth) must be used instead of the listed [http://tizen.org/privilege/bluetooth.xx](http://tizen.org/privilege/bluetooth.xx) privileges.[http://tizen.org/privilege/bluetooth.xx](http://tizen.org/privilege/bluetooth.xx) -> [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth)[http://tizen.org/privilege/bluetooth.admin](http://tizen.org/privilege/bluetooth.admin)[http://tizen.org/privilege/bluetooth.gap](http://tizen.org/privilege/bluetooth.gap)[http://tizen.org/privilege/bluetooth.health](http://tizen.org/privilege/bluetooth.health)[http://tizen.org/privilege/bluetooth.spp](http://tizen.org/privilege/bluetooth.spp)
- Unnecessary and misplaced exception errors have been removed and added in the Web Device API specification.  
  - Alarm 
    - TypeMismatchError of remove() has been removed.
    - TypeMismatchError of get() has been removed.
  - Calendar
    - TypeMismatchError and InvalidValuesError of removeChangeListener() have been removed.
  - Messaging
    - TypeMismatchError and InvalidValuesError of stopSync() have been removed.
    - UnknownError of stopSync() has been added.
  - Messageport 
    - TypeMismatchError and InvalidValuesError of requestRemoteMessagePort() have been removed.
    - TypeMismatchError and InvalidValuesError of requestTrustedRemoteMessagePort() have been removed.
  - Secure element
    - TypeMismatchError and InvalidValuesError of unregisterSEListener() have been removed.
- websetting privilege has been removed from websetting.removeAllCookies. Thus, websetting requires no privilege from 2.4 (no application change required for the applications written before 2.4).
- BT API
  - Txpowerlevel attribute type of BT has been changed to long.
- Alarm API
  - Behavior of AlarmRelative has changed. In order to decrease the power consumption, the operating system decides when it is going to be fired and what is the period between subsequent executions.
- Calendar API
  - Default Enum values of CalendarItemPriority and CalendarItemStatus have been changed to None.
- Notification API
  - Behavior of the ONGOING StatusNotificationType has been changed by a new UX policy.
  - On-going type notifications can be removed by user action.
- SystemInfo API
  - getCapability() handles custom features which are additional custom device capability keys specified by OEMs.

#### Webkit

**New Features**

- GamePad API support
  - GamePad API allows Web applications to directly act on gamepad data.
  - W3C specification: [http://www.w3.org/TR/2014/WD-gamepad-20140225/](http://www.w3.org/TR/2014/WD-gamepad-20140225/)
- New EWK APIs for reference browser
  - 26 APIs have been added as public APIs (such as ewk_autofill_profile_* and ewk_context_form_*).
  - Full specification and documentation will be added.
- GetUserMedia - Facing Mode support
  - You can select the front or rear camera using JavaScript.
  - W3C specification: [http://www.w3.org/TR/mediacapture-streams/#constraints](http://www.w3.org/TR/mediacapture-streams/#constraints)

**Change Notes**

- Layout (WebCore) changes (open source adaptation) 
  - "-webkit-calc": [https://bugs.webkit.org/show_bug.cgi?id=91951](https://bugs.webkit.org/show_bug.cgi?id=91951)
  - flexbox: [https://bugs.webkit.org/show_bug.cgi?id=110389](https://bugs.webkit.org/show_bug.cgi?id=110389)
  - flexbox: [https://bugs.webkit.org/show_bug.cgi?id=81809](https://bugs.webkit.org/show_bug.cgi?id=81809)
  - flexbox: [https://bugs.webkit.org/show_bug.cgi?id=7077](https://bugs.webkit.org/show_bug.cgi?id=7077)

#### Security

**New Features**

- Enforce security
  - Number of root daemons has been reduced and non-root daemons are mostly running as "system(200)" user.
  - -fpie build options have been applied to system services to achieve ASLR (Address Space Layout Randomization).
  - Smack labels have been dramatically reduced for vconf keys.
- Tizen App DRM
  - drm-service-core-tizen package has been introduced to decrypt DRM-protected applications.

**Change Notes**

- Unified Privilege Check for native and Web applications
  - wrt-security checking the privilege of Web applications has been removed.
  - privilege-checker is responsible for checking the privileges of native applications as well as Web applications.
  - Privilege backward compatibility is supported so that a 2.4 device can install applications which have 2.3, 2.3.1, or 2.2.1 in the required version field.
- Smack labeling and rule management module architecture has been changed
  - Smack rules and labels management modules are integrated into security-server to centralize the Smack configuration.
- User Certificate Management has been changed
  - User's trusted certificates have been categorized into e-mail, VPN, and Wi-Fi.
  - User can add, remove, enable, and disable their certificates for each category.
- APIs for Key manager
  - New APIs to handle PKCS12 files, such as ckmc_save_pkcs12, and ckmc_get_pkcs12 have been added.
  - New API for certificate verification with designated trust certificates has been added.
  - New API for OCSP (Online Certificate Status Protocol) has been added.
  - New API to manage access control rules efficiently (kmc_set_permission function) has been added.
  - New API that deletes data in the database using an alias (ckmc_remove_alias) has been added.
  - New error code (CKMC_ERROR_AUTHENTICATION_FAILED) for per-row password mismatched error has been added.
  - Platform level privilege from key-manager's control APIs has been deleted.
  - Getting a certificate chain with aliases API has been deprecated.
- Privileges
  - Native privileges for the mobile profile
    - New privileges:
      - [http://tizen.org/privilege/apphistory.read](http://tizen.org/privilege/apphistory.read)
      - [http://tizen.org/privilege/appmanager.kill.bgapp](http://tizen.org/privilege/appmanager.kill.bgapp)
      - [http://tizen.org/privilege/ime](http://tizen.org/privilege/ime)
      - [http://tizen.org/privilege/imemanager](http://tizen.org/privilege/imemanager)
      - [http://tizen.org/privilege/inputgenerator](http://tizen.org/privilege/inputgenerator)
      - [http://tizen.org/privilege/keygrab](http://tizen.org/privilege/keygrab)
      - [http://tizen.org/privilege/mapservice](http://tizen.org/privilege/mapservice)
      - [http://tizen.org/privilege/mediacontroller.client](http://tizen.org/privilege/mediacontroller.client)
      - [http://tizen.org/privilege/mediacontroller.server](http://tizen.org/privilege/mediacontroller.server)
      - [http://tizen.org/privilege/mediahistory.read](http://tizen.org/privilege/mediahistory.read)
      - [http://tizen.org/privilege/minicontrol.provider](http://tizen.org/privilege/minicontrol.provider)
      - [http://tizen.org/privilege/packagemanager.clearcache](http://tizen.org/privilege/packagemanager.clearcache)
      - [http://tizen.org/privilege/systemmonitor](http://tizen.org/privilege/systemmonitor)
    - Deprecated privileges:
      - [http://tizen.org/privilege/keymanager.admin](http://tizen.org/privilege/keymanager.admin)
  - Web privileges for the mobile profile
    - New privileges:
      - [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth)
      - [http://tizen.org/privilege/ime](http://tizen.org/privilege/ime)
      - [http://tizen.org/privilege/led](http://tizen.org/privilege/led)
      - [http://tizen.org/privilege/mediacontroller.client](http://tizen.org/privilege/mediacontroller.client)
      - [http://tizen.org/privilege/mediacontroller.server](http://tizen.org/privilege/mediacontroller.server)
    - Deprecated privileges:
      - [http://tizen.org/privilege/bluetooth.admin](http://tizen.org/privilege/bluetooth.admin) (Use [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth) instead.)
      - [http://tizen.org/privilege/bluetooth.gap](http://tizen.org/privilege/bluetooth.gap) (Use [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth) instead.)
      - [http://tizen.org/privilege/bluetooth.health](http://tizen.org/privilege/bluetooth.health) (Use [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth) instead.)
      - [http://tizen.org/privilege/bluetooth.spp](http://tizen.org/privilege/bluetooth.spp) (Use [http://tizen.org/privilege/bluetooth](http://tizen.org/privilege/bluetooth) instead.)
      - [http://tizen.org/privilege/websetting](http://tizen.org/privilege/websetting)

**Known Issues **

- Root processes can override the Smack access control check. Smack-related capabilities on root processes have been limited.

#### Kernel

**New Features**

- Support for a new mobile reference board TM1 with HD LCD has been added.
- Support for the 6Lowpan module for Bluetooth Low Energy has been added.
- Support for Samsung Game Pad I-GP20 has been added.
- Support for HID device drivers (BT mouse and keyboard) has been added.
- Built-in SWAP kernel module has been added for supporting the dynamic analyzer.

**Change Notes**

- Linux kernel version for the mobile profile has been upgraded to Linux-3.10.65.

#### System FW

**New Features**

- New APIs to get system CPU / memory usage info have been added to runtime-info.
- New feedback APIs to play sound or vibration associated with properties have been added.
- Tizen zip file system based on user-level filesystem has been provided.
- Forced reclaim based on a hard limit of swap cgroup has been added.
- System event has been exposed to give notifications through the application event system.

**Change Notes**

- Removable storage management has been enhanced.
- Restricting CPU resources for background application processes has been enhanced.
- Support for default process smack-labeling for security enhancement has been added.
- Open source upgrades
  - dbus version has been upgraded to v1.8.16.
  - systemd version has been upgraded to v216.

#### Compatibility Issues Between 2.4.0 Beta and 2.4.0

**DALi**

- [Changed] PixmapImage class name has been changed to NativeImageSource:
  - Old: PixmapImage
  - New: NativeImageSource

**Service Adaptor**

- [Removed] API has been removed, because it is not designed properly for the Service Adaptor:
  - service_adaptor_query_plugin_by_file()

**Sync Manager**

- For API enhancement, several changes have been applied to Sync Manager. For more detailed information, see the API Reference.
- [Changed] 2 APIs may require a proper privilege to work correctly:
  - sync_manager_add_data_change_sync_job()
    - [http://tizen.org/privilege/calendar.read](http://tizen.org/privilege/calendar.read)
    - [http://tizen.org/privilege/contact.read](http://tizen.org/privilege/contact.read)
    - Or both
  - sync_manager_add_periodic_sync_job()
    - [http://tizen.org/privilege/alarm.set](http://tizen.org/privilege/alarm.set)
- [Added] New capabilities have been added for media:
  - SYNC_SUPPORTS_CAPABILITY_CALENDAR
  - SYNC_SUPPORTS_CAPABILITY_CONTACT
  - SYNC_SUPPORTS_CAPABILITY_IMAGE
  - SYNC_SUPPORTS_CAPABILITY_VIDEO
  - SYNC_SUPPORTS_CAPABILITY_SOUND
  - SYNC_SUPPORTS_CAPABILITY_MUSIC
- [Removed] Some sync_period_e enumeration items have been removed:
  - SYNC_PERIOD_INTERVAL_5MIN
  - SYNC_PERIOD_INTERVAL_10MIN
  - SYNC_PERIOD_INTERVAL_15MIN
  - SYNC_PERIOD_INTERVAL_20MIN
  - SYNC_PERIOD_INTERVAL_45MIN
- [Changed] Parameters have been changed:
  - sync_manager_add_periodic_sync_job()
    - Old: (account_h account, const char* capability, bundle *extra, sync_period_e sync_period)
    - New: (account_h account, const char *sync_job_name, sync_period_e sync_period, sync_option_e sync_option, bundle *sync_job_user_data, int *sync_job_id)
- [Removed] Some APIs have been removed:
  - sync_adapter_init()
  - sync_adapter_destroy()
  - sync_manager_connect()
  - sync_manager_disconnect()
  - sync_manager_add_sync_job()
  - sync_manager_remove_sync_job()
  - sync_manager_remove_periodic_sync_job()

**Feedback**

- [Removed] feedback_type_e enumeration item has been removed:
  - FEEDBACK_TYPE_LED

**Media Controller**

- [Changed] Item names of several enumerations have been changed to avoid type name duplication. The prefix MC_ is added to all items of each enumeration:
  - mc_meta_e
    - Old: MEDIA_TITLE, ...
    - New: MC_META_MEDIA_TITLE, ...
  - mc_playback_states_e
    - Old: MEDIA_PLAYBACK_STATE_NONE, ...
    - New: MC_PLAYBACK_STATE_NONE, ...
  - mc_shuffle_mode_e
    - Old: SHUFFLE_MODE_ON, ...
    - New: MC_SHUFFLE_MODE_ON, ...
  - mc_repeat_mode_e
    - Old: REPEAT_MODE_ON, ...
    - New: MC_REPEAT_MODE_ON, ...

**Key Manager**

- [Removed] API has been removed, because it does not work correctly:
  - ckmc_get_cert_chain_with_trustedcert_alias()
- [Deprecated] API has been deprecated, because new APIs added since 2.4 are recommended for use:
  - ckmc_get_cert_chain_with_alias()

**Media Vision**

- [Removed] Non-supported definition and enumeration have been removed:
  - MV_BARCODE_DETECT_ATTR_MODE
  - mv_barcode_detect_attr_mode_e

**Tone/Wav Player**

- [Removed] Non-supported tone_player_error_e enumeration item has been removed:
  - TONE_PLAYER_ERROR_NOT_SUPPORTED

**Phonenumber Utils**

- [Removed] Non-supported phone_number_error_e enumeration item has been removed:
  - PHONE_NUMBER_ERROR_PERMISSION_DENIED

**Application Framework**

- [Deprecated] 2 APIs that are not supported since 2.4 have been deprecated:
  - app_get_external_shared_data_path()
  - app_get_external_data_path()
- [Deprecated] Non-supported operations of application control have been deprecated:
  - APP_CONTROL_OPERATION_SEND
  - APP_CONTROL_OPERATION_SEND_TEXT

**Context Trigger**

- [Changed] API behavior has changed. The launch request of the service application is restricted. The function returns CONTEXT_TRIGGER_ERROR_VALID_RULE, if the launch request is for the service application.
  - context_trigger_rule_set_action_app_control()

**Maps Service**

- [Changed] Some APIs require additional privileges to work properly:
  - maps_service_create()
  - maps_service_geocode()
  - maps_service_geocode_inside_area()
  - maps_service_geocode_by_structured_address()
  - maps_service_reverse_geocode()
  - maps_service_search_place()
  - maps_service_search_place_by_area()
  - maps_service_search_place_by_address()
  - maps_service_search_route()
  - maps_service_search_route_waypoints()
  - [http://tizen.org/privilege/network.get](http://tizen.org/privilege/network.get)
  - [http://tizen.org/privilege/internet](http://tizen.org/privilege/internet)
  - Or both

**Event**

- [Added] New state definition of the battery charger has been added to clarify “discharging”:
  - EVENT_KEY_BATTERY_CHARGER_STATUS

**NFC**

- [Changed] nfc_record_tnf_e type name has been changed to correct a typo:
  - Old: NFC_RECORD_TNF_UNCHAGNED
  - New: NFC_RECORD_TNF_UNCHANGED

**Device**

- [Deprecated] 2 APIs have been deprecated to restrict misuse:
  - device_display_change_state()
  - device_power_wakeup()
