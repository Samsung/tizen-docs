# Tizen Studio 2.5 Release Notes

-   Release Date: Aug 8, 2018


## IDE and Tools


### New Features

-   SDB
	-  `wait-for-device` command added, when this command is issued SDB waits indefinitely for the target to come to `device` state.
-   RT IDE Certificate Manager
	-   Integrated Certificate Manager into RT IDE.
-   Baseline SDK Size Optimizations
	-   Optimized baseline SDK size from 480MB to 320MB.

### Fixed Bugs
-   Certificate Manager
	-   Added validation for .pem and .der files when they are imported as a new IoT profile in the Certificate Manager.

-   Installer  and Package Manager
	-   Fixed the extension download failure, which occurs when URL starts with https.
	-   Fixed an issue of the uninstaller window, earlier the window gets closed while uninstalling.
	-   Fixed an issue of the target directory, now it is possible to set the target directory after an invalid path.
-   Base IDE
	-   Supports **Show in History** view of eclipse team service. 
-   CLI
	-   Fixed CLI build failure for IoT Headless App.
	> **Note**
	>
	> If you have projects with old CLI build scripts, you must re-create the build script by running `export to CLI` before running the CLI commands.
-   Others
	-   Fixed the security issues in Tizen Studio source code.

### Known Issues
-	Tizen Studio
	-	In case of Mac, if the UI perspectives are not displayed properly after updating the Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from previous installation.
	-	In case if you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
-	Common
	-   If you install the Tizen Studio in a directory that requires administrator privileges for access. For example, for C:\ProgramFiles, administrator privileges are required to run the Tizen SDK tools. The Tizen Installer and the baseline SDK Installer alerts you, if you try to install into such a directory.
-	Web and Native IDE
	-   From Tizen Studio 2.0 onwards, the Connection Explorer is replaced with the Device Manager, this can cause errors in the Connection Explorer view. You can fix this in two ways:
	    -   Reset the perspective.
            In the Tizen Studio menu, select Window > Perspective > Reset Perspective
	    -   After updating to the Tizen Studio 2.0, run the *eclipse.exe -clean -clearPersistedState* command. Then launch the Tizen Studio normally.
	-   You can create unit tests only for Tizen 2.3.2 and later version projects. Currently, Tizen Studio does not support unit tests for the earlier versions.
-	Web IDE
	-   The preview tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature **Ctrl + 4** of the Web SDK HTML Editor.
	-   In RDS (Rapid Development Support) mode, the web unit test result is not updated.
-	Certificate Manager
	-   Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
	-   IoT certification currently requires a user to manually download and select the certificate.
-	Native UI Builder
	-   If the expanded attribute in a multibutton entry component is set to false, + is displayed.
-	Native Component Designer
	-   The vector-type part is not supported. You cannot see the vector image and change the SVG file.
	-   Playing sound is not supported on Windows&reg; or macOS.
	-   The Component Designer crashes if an alias is selected as the source group of an added item.
-	Emulator
	-   To use the Tizen emulator, install an Intel VTx supported by the CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for the Tizen emulator, see [Prerequisites for the Tizen Studio](https://developer.tizen.org/development/tizen-studio/download/installing-tizen-studio/prerequisites).
	    -   If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [bumblebee project](https://wiki.ubuntu.com/Bumblebee ). For Windows&reg;, select *High Speed NVIDIA&reg; Processor* as *Preferred Graphics processor* in the NVIDIA&reg; control panel.
	    -   On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session occasionally logs out while launching the Emulator Manager, or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
	-   On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
	-   On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
	-   On Windows&reg;, if an error with message "failed to allocate memory" occurs while executing the emulator, try the following:
	    -   Close some other programs and try to launch the emulator again.
	    -   If the RAM size is set to 768 or 1024 MB for the VM in the Emulator Manager, change it to 512 MB.
	    -   Increase the user area of the virtual memory in the system to 3 GB by entering the *bcdedit /setincreaseuserva 3072* command on the console with administrator rights (only in Windows&reg; 7), and reboot.
	-   If you use a MacBook Pro which has both Intel HD and NVIDIA&reg; GPUs, the emulator can unexpectedly terminate when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in the Emulator Manager and on the general tab in the emulator configuration window, set OpenGL ES version to version 2.0 or to version 3.0.
	-   When you launch the Emulator Manager in the Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.
	-   Basic Web applications does not install on SD cards.
-	CLI and SDB
	-   The Tizen Studio does not support the SDB ([Smart Development Bridge](https://developer.tizen.org/development/tizen-studio/web-tools/running-and-testing-your-app/sdb)) bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
-	Dynamic Analyzer
	-   When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:
	    -   The Core Frequency information is not shown.
	    -   The screenshots on scene transitions feature will not work.
	-   When analyzing applications on the Tizen 4.0 emulator or reference device, the startup profiling information is not shown.
	-   The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.
	-   The Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device, due to the security policy.
	-   The Dynamic Analyzer cannot show lifecycle information for Web applications.
	-   Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
-	Web Inspector
	-   If your Google Chrome™ browser version is higher than 54, the Web Inspector console and some other functions does not work properly due to Web core compatibility issues.
