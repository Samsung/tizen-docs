# Tizen Studio 2.0 Release Notes

-   Release Date: Oct 25, 2017


## IDE and Tools


### New Features

-   Web and Native IDE
    -   The Device Manager is a stand-alone tool that supports viewing connected device information, internal folder structure, and device logs.
    -   The Certificate Manager allows you to create and manage certificates using wizards.
-   Manifest/Configuration Editor
    -   Support for trust anchor elements and `app-appdefined-privilege` functionalities have been added.
-   Configurable SDK
    -   The Configurable SDK supports tools to develop applications from custom profiles (IoT Headed and IoT Headless).
-   Native UI Builder
    -   Integrated Design Editor and Storyboard Editor
        -   You can develop UI layouts and applications in the same workspace.
        -   The layout editor area has been extended by removing the sub-tabs at the top.
        -   A toolbar button to toggle between the Design Editor and the Source Editor has been added.
        -   WYSIWYG design features have been added, to associate multiple views on 1 screen at application creation.
        -   In the Design View palette area, 3 views have been added: an empty view, a Ctxpopup view, and a popup view. You can easily drag and drop views from the palette. Wearable profiles only support empty views.
        -   The entry/exit line policy for creating connections between views has been improved.
        -   An **Auto Layout** toolbar button has been added to automatically arrange multiple views in the editor.
-   CLI
    -   The .NET CLI Extension tool adds extended features, specific to Tizen .NET application development, to the .NET Command Line Interface tool. You can develop a Tizen .NET application with the same user experience as the .NET Command Line Interface tool.
    -   Enhanced certificate and profile management has been implemented. For testing purposes, instead of creating your own certificate and security profile, you can generate Tizen packages using default certificates and security profiles. However, these packages cannot be run on real target devices.
    -   You can specify an active security profile from among several profiles. If you do not select a specific profile when packaging your application, the build tool automatically applies the currently-active profile.
    -   Support for platform add-on frameworks has been added. You can build a native application with specific platform add-on frameworks. Use the `-f` option for the `build-native` command to specify add-on frameworks to a base platform.
    -   You can set up a trust anchor for your application certification.
-   Emulator Manager
    -   The Emulator Manager supports platform image installation. If you open the Emulator Manager and the platform is not installed, the Emulator Manager displays a dialog box to help you install the required platform.
-   RT IDE
    -   Application management features for using added applications have been included.
    -   SDK-related features for SmartThings cloud integration have been included, making it easy to generate code for interworking with SmartThings.
    -   Support for line debugging on Ubuntu 32/64 bit has been added.

### Changed Features

-   Web and Native IDE
    -   The Rapid Development Support (RDS) speed has been improved. When using RDS, after you first build and run the application, RDS detects the modification, addition, and deletion of files, and builds and executes them in the background as needed.
    -   The Connection Explorer has been deprecated. Use the Device Manager instead.
    -   The **Callstack** view has been enabled for Tizen 3.0 and higher.
-   Native IDE and CLI
    -   For Tizen 4.0 applications, the native toolchain has been upgraded from GCC toolchain version 4.9 to 6.2.
    -   In the past, all toolchain versions have been exposed, but now the toolchain version that can be selected depends on the platform version.
-   Native UI Builder
    -   XML layout editor stabilization and UX improvements have been implemented.
-   CLI
    -   Long argument support on Windows&reg; has been added.
-   RT IDE
    -   Several build configurations (configure, custom toolchain, and kernel config) have been separated based on their functions. The batch build feature has been improved by showing the necessary settings sequentially.

### Fixed Bugs

-   Installer, Package Manager, and Uninstaller
    -   Fixed a bug that caused `package-manager-cli.exe` to disappear if **Ctrl + C** was pressed while it was running.
    -   Fixed a bug where, after loading a local package image file in the Package Manager configuration dialog, the **OK** button on the dialog box did not work on the second attempt to make configuration changes.
    -   Fixed `package-manager-cli` to work properly in the headless version of Ubuntu.

### Known Issues

-   Common
    -   The Java Development Kit (JDK) 9 is not supported.
    -   If you install the Tizen Studio in a directory that requires administrator privileges for access, such as `C:\Program Files`, administrator privileges are required to run the Tizen SDK tools. The Tizen Installer and Baseline SDK Installer alert you if you try to install into such a directory.
- Web and Native IDE
    -   Since Tizen Studio 2.0, the Connection Explorer has been replaced with the Device Manager, which can cause errors in the Connection Explorer view. You can fix this in 2 ways:
        -   Reset the perspective.

            In the Tizen Studio menu, select **Window &gt; Perspective &gt; Reset Perspective**.

        - After updating to the Tizen Studio 2.0, run the `eclipse.exe -clean -clearPersistedState` command. Then launch the Tizen Studio normally.

    - On a MacBook Pro using macOS version 10.12, the touch bar can turn black.
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
    -   To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. Check the prerequisites for the Tizen emulator from [Prerequisites for the Tizen Studio](../setup/prerequisites.md#emulator).
        -   If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA graphics card. For Ubuntu, check the bumblebee project (<https://wiki.ubuntu.com/Bumblebee>). For Windows&reg;, select "High Speed NVIDIA Processor" as "Preferred Graphics processor" in the NVIDIA control panel.
        -   On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session can be occasionally logged out when launching the Emulator Manager, or the emulator skin can be drawn improperly. Check the prerequisites and upgrade to the latest graphics driver.
    -   On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
    -   On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
    -   On Windows&reg;, if a "failed to allocate memory" error occurs while executing the emulator, try the following:
        -   Close some other programs and try to launch the emulator again.
        -   If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
        -   Increase the user area of the virtual memory in the system to 3 GB by entering the `bcdedit /set increaseuserva 3072` command on the console with administrator rights (Windows&reg; 7 only), and reboot.
    -   If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, when you execute the emulator with the **OpenGL ES ver. v1.1 & v2.0** option, the emulator can be unexpectedly terminated. Use the **OpenGL ES ver. v2.0 & v3.0** option.
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
