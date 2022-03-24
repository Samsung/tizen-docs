# Tizen Studio 4.6 Release Notes

- Release Date: Mar 31, 2022

## IDE and tools

### New feature

- macOS Monterey support
  - Tizen IDE is now supported on macOS Monterey
  - Visual Studio Code Extension for Tizen is now supported on macOS Monterey
- Multi App and Hybrid App support
  - Added the following Multi app and Hybrid app support in CLI (TZ), VS, and VSCode extension for Tizen

  **Multi App**
  Developers can now have multiple dependent applications in a single workspace and perform all app life cycle events like app creation, building, packaging, installing, and testing: 
    - Tizen.Native App + Tizen.Native App
    - Tizen.Web App + Tizen.Web App
    - Tizen.Dotnet App + Tizen.Dotnet App

|   | Legend               |
|---|----------------------|
| M | Multiple   allowed   |
| 0 | Not   allowed        |
| 1 | Single  app allowed |


**Native Apps**

|     Apps               | UI App (Dependent) | Service App (Dependent) | Widget App (Dependent) | Component App (Dependent) | Shared Lib (Dependent) | Static Lib (Dependent) | Watch App (Dependent) |
|------------------------|--------------------|-------------------------|------------------------|---------------------------|------------------------|------------------------|-----------------------|
| UI   App (Main)         | M                  | M                       | M                      | 0                         | M                      | M                      | 0                     |
| Service   App (Main)    | 0                  | 0                       | 0                      | 0                         | M                      | M                      | 0                     |
| Widget   App (Main)     | 0                  | 0                       | 0                      | 0                         | M                      | M                      | 0                     |
| Component   App (Main)  | 0                  | 0                       | 0                      | 0                         | M                      | M                      | 0                     |
| Shared   Library (Main) | 0                  | 0                       | 0                      | 0                         | M                      | M                      | 0                     |
| Static   Library (Main) | 0                  | 0                       | 0                      | 0                         | M                      | M                      | 0                     |
| Watch   App (Main)      | 0                  | M                       | 0                      | 0                         | M                      | M                      | 0                     |

**Web Apps**

| Apps               | Native Service App (Dependent) | Native Widget App (Dependent) | Web App (Dependent) | Web Widget (Dependent) | Dotnet UI app (Dependent) | Dotnet Service App (Dependent) |   |
|--------------------|--------------------------------|-------------------------------|---------------------|------------------------|---------------------------|--------------------------------|---|
| Web   App (Main)    | M                              | M                             | 1                   | M                      | M                         | M                              |   |
| Web   Widget (Main) | 0                              | 0                             | 0                   | 0                      | 0                         | 0                              |   |


  **Hybrid App**
  Developers can now have multiple dependent applications **of different types** in a single workspace and perform all app life cycle events like app creation, building, packaging, installing, and testing.
    
| Main App          | Possible Sub App Combinations |
|-------------------|-------------------------------|
| Native   Main App | Native + Dotnet               |
| Dotnet   Main App | Dotnet + Native               |
| Web   Main App    | Web + Native +   Dotnet       |

- CLI
  - Added support for importing Hybrid and Multi projects.
- VSCode
  - Added support for importing Hybrid and Multi projects. Developers can import a Tizen.Native/Tizen.Web/Tizen.Dotnet project to VSCode and then can build and package.
  - Added support for importing wgt (Tizen Web application package file) into Visual Studio Code Extension for Tizen.
- Visual Studio (Windows)
  - Added support for importing Hybrid and Multi projects. Developers can import a Tizen.Native/Tizen.Web/Tizen.Dotnet project to VS and then can build and package.
  - Added support for importing wgt (Tizen Web application package file) into Visual Studio Extension for Tizen.


### Fixed bugs
  - Fixed the issue in API Checker due to which warnings were not displayed for web apps in VS extension for Tizen.
  - Fixed the error that occurred on selecting TV profile while creating a new project in VS extension for Tizen.
  - Fixed the failure to open YAML config files for native apps in VS extension for Tizen. 
  - Fixed the issue due to which there was no option to import Tizen TV web app projects in VS & VSCode extension for Tizen.
  - Fixed the issue in import functionality and added missing support to import wgt (Web Application Package file) in VS & VSCode extension for Tizen.

### Deprecated
  - Bridge networking support in emulators will be deprecated in future Tizen Studio releases.


### Known issues

- Installer
  - In macOS, Tizen Studio related files are marked as Malware, hence it is recommended to select **Anywhere** under allow apps as described in https://www.imore.com/how-open-apps-anywhere-macos-catalina-and-mojave.
- Tizen Studio
  - Valgrind profiling is not supported in Tizen 6.5 platform.
  - In macOS, if the UI perspectives are not displayed properly after updating Tizen Studio, it is recommended to restart the IDE. This issue is because of the uncleared cache from the previous installation.
  - In case if you see any old perspective, it is recommended to create a new workspace and import the projects to the new workspace to resolve the issue.
  - In macOS from catalina and above versions, Native Templates-5.5 will not build with CLI when compiler is set to **gcc**.
- Common
  - If you install Tizen Studio in a directory that requires administrator privileges for access. For example, for **C:\ProgramFiles** location administrator privilege is needed to run the Tizen SDK tools. The Tizen Installer and the baseline SDK Installer alerts you if you try to install it into such a directory.
- Web and Native IDE
  - You can create unit tests for Tizen 2.3.2 and higher version projects only. Unit testing for older versions is not supported.
- Web IDE
  - The preview tab in the Web Page Editor sometimes does not appear properly. Use an alternative feature, named Web SDK HTML Editor, which has enhanced features compared to the Web Page Editor. Instead of the preview tab in the Web Page Editor, use the preview feature **Ctrl + 4** of the Web SDK HTML Editor.
  - In Rapid Development Support (RDS) mode, the web unit test result is not updated.
  - Remote Inspector does not allow audit in the updated version of Chrome.
- Certificate Manager
  - Overwriting a duplicate certificate profile in the migration wizard works incorrectly on macOS.
- Emulator
  - In the Tizen 5.5 version, the emulator images app un-installation might take some time to complete if the app name contains more than 14 characters. A patch for the same is expected to be released in the next update.
  - To use Tizen Emulator, use Intel VTx supported CPU and the latest version of the graphic card driver provided by the vendor. To verify the prerequisites for Tizen Emulator, see [Prerequisites for Tizen Studio](../setup/prerequisites.md).
    - If the host machine is using NVIDIA&reg; Optimus&reg; technology on either Ubuntu or Windows, you must set the Tizen Emulator to run with your NVIDIA&reg; graphics card. For Ubuntu, verify the [bumblebee project](https://wiki.ubuntu.com/Bumblebee). For Windows, select **High Speed NVIDIA&reg; Processor** as **Preferred Graphics Processor** in the NVIDIA&reg; control panel.
    - On Ubuntu, if the graphics driver is out-of-date, your Ubuntu desktop session occasionally logs out while launching Emulator Manager, or the emulator skin is displayed improperly. Verify the prerequisites and upgrade to the latest graphics driver.
  - On Windows, depending on your OS theme (such as Non-Aero themes and Windows XP themes), a display surface can be erased for a while if the emulator window is covered with another window. If you click the emulator window, the display surface runs correctly again.
  - On Windows, if an error with message "failed to allocate memory" occurs while executing the emulator, try the following:
    - Close some other programs and try to launch the emulator again.
    - If the RAM size is set to 768 or 1024 MB for the VM in Emulator Manager, change it to 512 MB.
    - Increase the user area of the virtual memory in the system to 3 GB by entering the **bcdedit /setincreaseuserva 3072** command on the console with administrator rights (only in Windows 7), and reboot.
  - If you use a MacBook Pro that has both Intel HD and NVIDIA&reg; GPUs, the emulator can terminate unexpectedly when you execute the emulator with OpenGL ES version 1.1 or 2.0. Verify the emulator configuration in Emulator Manager and on the **General** tab in the emulator configuration window, set OpenGL ES version to version 2.0, or to version 3.0.
  - When you launch Emulator Manager in Tizen IDE, the shortcut image of Emulator Manager may not be displayed properly.
  - Basic Web applications are not installed on SD cards.
  - To use Tizen Emulator in Tizen platform 3.0 or lower, disable the CPU VT option in the **HW Support** tab of Emulator Configuration.
- CLI and SDB
  - Tizen Studio does not support the [Smart Development Bridge](../common-tools/smart-development-bridge.md) (SDB) bash auto-completion on Windows (it is available on Ubuntu and macOS).
- Dynamic Analyzer
  - When analyzing applications on commercial devices running Tizen 3.0, newly-released or after a firmware update, the following problems exist:
    - The Core Frequency information is not shown.
    - The screenshots on the scene transitions feature will not work.
  - When analyzing applications on the Tizen 4.0 emulator or reference device, the startup profiling information is not shown.
  - The UI Hierarchy viewer feature and startup profiling are not performed simultaneously.
  - The Dynamic Analyzer cannot show lifecycle information for web applications.
  - Widget applications cannot be profiled with the Dynamic Analyzer. They are hidden in the application list on the toolbar for all Tizen platforms, except Tizen 2.3.2.
  - The Dynamic Analyzer sometimes gets stuck which is caused by an internal security checking program.
- Visual Studio
  - NUI XAML application build error can be resolved by doing clean and then build again.
- VS Mac
  - NUI XAML application build error can be resolved by doing clean and then build again.
