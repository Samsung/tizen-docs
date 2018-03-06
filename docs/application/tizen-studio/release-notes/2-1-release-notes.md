# Tizen Studio 2.1 Release Notes

-   Release Date: Dec 21, 2017


## IDE and Tools

### New Features

-   Common
    -   Support for macOS 10.13 has been added.
    -   The DALi template has been added for the Tizen 4.0 platform.
-   Installer, Package Manager, and Uninstaller
    -   The Installer and Package Manager Launcher (NSIS) have been upgraded to the latest version to prevent DLL hijacking on 64-bit versions of Windows&reg;.
-   Certificate Manager
    -   Usability has been improved by eliminating unnecessary user actions on Windows&reg; when setting the proxy.
    -   Security has been enhanced by supporting the HTTPS protocol when connecting to online sample server.
-   Device Manager
    -   The **Permit to install** option has been added to the context menu in the connected target view. The TV emulator does not allow shell commands and does not show the tree view of the device file system in the Device Manager. Consequently, the **Permit to install** option has been added to support application installation on TV emulators.
-   SDB
    -   `device_name` has been added to the return value of the `sdb capability` command.
-   Native UI Builder
    -   Support for custom UI components has been added:
        -   Custom components can be created based on EDC (Edje Data Collection) in the UI Builder's Design Editor.
        -   The descriptor describes the abstracted attribute for the UI component implemented by the EDC.
        -   Specialized components can be used as well as the basic components provided by the UI Builder.
        -   UI components can be reused, improving development productivity.
-   SmartThings&trade; SDK
    -   Support has been added for SmartThings&trade; application projects:
        -   Online Model Server
        -   SmartThings&trade; device templates
        -   Device Model Manager (importing, exporting, and creating device models)
        -   Automatic code generation
        -   SmartThings&trade; Certificate Management (creating, importing, and setting certificates as active)

### Changed Features

-   Web and Native IDE
    -   Usability of automatic updates has been improved.
-   Emulator
    -   The platform image installation UI of the Emulator Manager has been improved.
-   Native UI Builder
    -   A search field has been added for UI components to the Design Editor palette area.
    -   Changes to EDJ resources added or updated by outside processes (EDC Editor or Component Designer) are now automatically reflected in the Design Editor without having to manually refresh the view.

### Fixed Bugs

-   Installer, Package Manager, and Uninstaller
    -   Fixed a bug on Windows&reg; computers that prevented the Package Manager and Uninstaller from creating or deleting shortcuts to a user account directory whose name contains multi-byte characters or spaces.
-   Web and Native IDE
    -   Fixed a bug that caused the touch bar to turn black in macOS versions 10.12 and 10.13.
    -   Fixed a bug that prevented the log viewer from working properly with Gear S3 and Gear Sport devices.
-   Device Manager
    -   Fixed a bug that made the DUID appear incorrectly.
-   CLI
    -   Fixed a bug that made the specified relative paths unable to be resolved normally when installing a package or adding a security profile.
    -   Fixed a bug that caused packaging Web applications to fail when using the command line, if the native command line tools were not installed.

### Known Issues

-   Common
    -   The Java Development Kit (JDK) 9 is not supported.
    -   If you install the Tizen Studio in a directory that requires administrator privileges for access, such as `C:\Program Files`, administrator privileges are required to run the Tizen SDK tools. The Tizen Installer and the Baseline SDK Installer alert you if you try to install into such a directory.
- Web and Native IDE
    -   Since Tizen Studio 2.0, the Connection Explorer has been replaced with the Device Manager, which can cause errors in the Connection Explorer view. You can fix this in 2 ways:
        -   Reset the perspective.

            In the Tizen Studio menu, select **Window &gt; Perspective &gt; Reset Perspective**.

        - After updating to the Tizen Studio 2.0, run the `eclipse.exe -clean -clearPersistedState` command. Then launch the Tizen Studio normally.

    - You can create unit tests for Tizen 2.3.2 and higher version projects only. The Tizen Studio currently does not support unit testing for all earlier versions.
- Web IDE
    -   The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
    -   In RDS mode, the Web unit test result does not update.
- Certificate Manager
    -   Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
- Native UI Builder
    -   If the `expanded` attribute in a multibutton entry component is set to `false`, **+** is displayed.
- Native Component Designer
    -   The vector-type part is not supported. You cannot see the vector image and change the SVG file.
    -   Playing sound is not supported on Windows&reg; or macOS.
    -   The Component Designer crashes if an alias is selected as an added item's source group.
- Emulator
    -   To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](https://developer.tizen.org/development/tizen-studio/download/installing-tizen-studio/prerequisites#emulator).
        -   If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA graphics card. For Ubuntu, check the bumblebee project (<https://wiki.ubuntu.com/Bumblebee>). For Windows&reg;, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the NVIDIA control panel.
        -   On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
    -   On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
    -   On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
    -   On Windows&reg;, if a "failed to allocate memory" error occurs while executing the emulator, try the following:
        -   Close some other programs and try to launch the emulator again.
        -   If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
        -   Increase the user area of the virtual memory in the system to 3 GB by entering the `bcdedit /set increaseuserva 3072` command on the console with administrator rights (Windows&reg; 7 only), and reboot.
    -   If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, the emulator can be unexpectedly terminated when you execute the emulator with **OpenGL ES Ver** set to **v1.1 & v2.0**. Check the emulator configuration in the Emulator Manager, and on the **General** tab in the **Emulator Configuration** window, set **OpenGL ES Ver** to **v2.0 & v3.0**.
    -   When you launch the Emulator Manager in the Tizen IDE, the Emulator Manager shortcut image is not exposed properly.
    -   Basic Web applications do not install on SD cards.
- CLI and SDB
    -   The Tizen Studio does not support the SDB bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
- Dynamic Analyzer
    -   When analyzing applications on commercial devices running Tizen 3.0, both newly-released or after a firmware update, the following problems exist:
        -   The **Core Frequency** information is not shown.
        -   The **Screenshots on scene transitions** feature is not working.
    -   When analyzing applications on the Tizen 4.0 emulator or reference device, the start-up profiling information is not shown.
    -   The UI Hierarchy viewer feature and start-up profiling are not performed simultaneously.
    -   The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device, due to the security policy.
    -   The Dynamic Analyzer cannot show life-cycle information for Web applications.
    -   Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
- Web Inspector
    -   If your Google Chrome&trade; browser version is higher than 54, the Web Inspector console and some other functions do not work properly due to Web core compatibility issues.


