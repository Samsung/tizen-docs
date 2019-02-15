# Tizen Studio 3.1 Release Notes

-   Release Date: Jan 17, 2019


## IDE and Tools


### New Features
-   OpenJDK
	-  The support for OpenJDK 10 has been added.

### Fixed Bugs
-   Tizen IDE
	-   Changing the profile and platform version now updates the rootstrap in project configuration.
	-   The error message, which appears while adding an incorrect privilege file to a native application has been modified.
	-   The issues with log filtering in log tab have been fixed.
-   Certificate manager
	-   The failure in generating a new certificate profile after 01 January 2019 has been fixed.
	-   The issue in network proxy settings has been fixed. Now, the network proxy setting change is applied for all network accesses.
	-   The unnecessary input fields have been changed to optional in UI while creating IoT certificates. 
-   Device Manager
	-   The issues with log filtering in log tab have been fixed.
-   TizenRT
	-   The issue in RT IDE has been fixed. Now, the IoT certificates are copied to the project while building instead of flashing.
	-   RT IDE installation prompts user to install libwebkitgt to avoid "browser path not set" error message.
	-   The issues that occurs while debugging TizenRT application have been fixed. 

### Known Issues
-	Tizen Studio
	-	In MacOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from previous installation.
	-	In case if you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
-	Common
	-   If you install Tizen Studio in a directory that requires administrator privileges for access. For example, for C:\ProgramFiles, administrator privileges are required to run the Tizen SDK tools. The Tizen Installer and the baseline SDK Installer alerts you, if you try to install into such a directory.
-	Web and Native IDE
	-   From Tizen Studio 2.0 onwards, Connection Explorer is replaced with Device Manager, this can cause errors in the Connection Explorer view. You can fix this in two ways:
	    -   Reset the perspective.
            In the Tizen Studio menu, select Window > Perspective > Reset Perspective
	    -   After updating to Tizen Studio 2.0, run the **eclipse.exe -clean -clearPersistedState** command. Then launch Tizen Studio normally.
	-   You can create unit tests for Tizen 2.3.2 and higher version projects only. Now Tizen Studio does not support unit testing for older versions.
-	Web IDE
	-   The preview tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature **Ctrl + 4** of the Web SDK HTML Editor.
	-   In Rapid Development Support (RDS) mode, the web unit test result is not updated.
-	Certificate Manager
	-   Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
-	Native UI Builder
	-   If the expanded attribute in a multibutton entry component is set to false, + is displayed.
-	Native Component Designer
	-   The vector-type part is not supported. You cannot see the vector image and change the SVG file.
	-   Playing sound is not supported on Windows&reg; or macOS.
	-   The Component Designer crashes if an alias is selected as the source group of an added item.
-	Emulator
	-   To use the Tizen emulator, install an Intel VTx supported by the CPU, and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for the Tizen emulator, see [Prerequisites for Tizen Studio](../setup/prerequisites.md).
	    -   If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows&reg;, you must set the Tizen emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [bumblebee project](https://wiki.ubuntu.com/Bumblebee ). For Windows&reg;, select **High Speed NVIDIA&reg; Processor** as **Preferred Graphics processor** in the NVIDIA&reg; control panel.
	    -   On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session occasionally logs out while launching Emulator Manager, or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
	-   On Ubuntu 14.04, a shortcut menu can sometimes appear transparent.
	-   On Windows&reg;, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
	-   On Windows&reg;, if an error with message "failed to allocate memory" occurs while executing the emulator, try the following:
	    -   Close some other programs and try to launch the emulator again.
	    -   If the RAM size is set to 768 or 1024 MB for VM in Emulator Manager, change it to 512 MB.
	    -   Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /setincreaseuserva 3072** command on the console with administrator rights (only in Windows&reg; 7), and reboot.
	-   If you use a MacBook Pro that has both Intel HD and NVIDIA&reg; GPUs, the emulator can unexpectedly terminate when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the general tab in the emulator configuration window, set OpenGL ES version to version 2.0 or to version 3.0.
	-   When you launch Emulator Manager in the Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.
	-   Basic Web applications does not install on SD cards.
	-   Samsung Certificate cannot be used to sign application while launching application on 5.0 Emulator.
-	CLI and SDB
	-   The Tizen Studio does not support the [Smart Development Bridge](../common-tools/smart-development-bridge.md) (SDB) bash auto-completion on Windows&reg; (it is available on Ubuntu and macOS).
-	Dynamic Analyzer
	-   When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:
	    -   The Core Frequency information is not shown.
	    -   The screenshots on scene transitions feature will not work.
	-   When analyzing applications on the Tizen 4.0 emulator or reference device, the startup profiling information is not shown.
	-   The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.
	-   Dynamic Analyzer cannot perform Web application profiling with a commercial Tizen device, due to the security policy.
	-   Dynamic Analyzer cannot show lifecycle information for Web applications.
	-   Widget applications cannot be profiled with Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
-	Web Inspector
	-   If your Google Chrome&trade; browser version is higher than 54, the Web Inspector console and some other functions does not work properly due to Web core compatibility issues.
