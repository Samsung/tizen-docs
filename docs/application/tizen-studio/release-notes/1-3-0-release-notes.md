# Tizen Studio 1.3 Release Notes

-   Release Date: Sep 11, 2017


## IDE and Tools


### New Features

-   Native UI Builder
    -   EDC supports `group.parts.part.description.text.ellipsize` feature and keywords. This feature includes text marquee (slide) and text fade-in and -out effects.
-   RT IDE
    -   The standalone RT IDE installer is available.

### Changed Features

-   Native IDE
    -   Previously, symbols were not removed when building a project in release mode, so the generated TPK package was unnecessarily large. The symbols are now removed when building in release mode.
    -   To support various widget sizes, the manifest validation logic for widget size checks has been removed.
-   Web IDE
    -   On the Tizen 3.0 platform, the background category has been enabled in the configuration file editor.

### Fixed Bugs

-   Native IDE
    -   Fixed a bug where an invalid manifest attribute (`setup-appid`) was automatically generated when a user created a multi-application package (native widget and native UI application). This caused the application to be rejected from the Tizen Store.
-   Certificate Manager
    -   Added certificate validation to prevent an author certificate from being imported as a distributor certificate.

### Known Issues

-   Installer, Package Manager, and Uninstaller
    -   If there is a multibyte character in the Tizen Studio installation path, some development packages have a difficulty in finding the installation location when they are working.
    -   In Windows&reg; CLI Package Manager, the execution file disappears when forcibly terminated (**Ctrl + C**) during execution.
-   Web and Native IDE
    -   On a MacBook Pro using macOS version 10.12, the touch bar can turn black. As a workaround, upgrade your macOS version to 10.13.
    -   You can create unit tests for Tizen 2.3.2 and higher version projects only. The Tizen Studio currently does not support unit testing for all earlier versions.
-   Web IDE
    -   The **Preview** tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the **Preview** tab in the Web Page Editor, use the preview (**Ctrl + 4**) feature of the Web SDK HTML Editor.
    -   The unit test application crashes on launch from the Tizen Studio.
-   Native UI Builder
    -   If the `expanded` attribute in a multibutton entry component is set to `false`, **+** is displayed.
    -   When you create a new project with UI Builder, the `layout.xml` file does not open in the **Design** tab. As a workaround, go to the **Source** tab and remove the `page_location_x` and `page_location_y` attributes, then save and reopen the `layout.xml` file.
-   Native Component Designer
    -   The vector-type part is not supported. You cannot see the vector image and change the SVG file.
    -   Playing sound is not supported on Windows&reg; or macOS.
    -   The Component Designer crashes if an alias is selected as an added item's source group.
-   Emulator
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
-   CLI and SDB
    -   The Tizen Studio does not support the SDB bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
-   Dynamic Analyzer
    -   The UI Hierarchy viewer feature and start-up profiling are not performed simultaneously.
    -   The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device due to the security policy.
    -   The Dynamic Analyzer cannot show life-cycle information for Web applications.
    -   Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
-   Web Inspector
    -   If your Google Chrome&trade; browser version is higher than 54, the Web Inspector console and some other functions do not work properly due to Web core compatibility issues.
