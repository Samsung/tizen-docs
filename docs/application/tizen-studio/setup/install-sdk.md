# Installing Tizen Studio

The installer has been renewed to provide a better user experience and show the unique Tizen philosophy. Using the new installer, you can now install the basic platform and the useful tools with a few clicks.

You can use either the GUI or the CLI version of the installer.

## Using the GUI Installer

To install Tizen Studio:

1. Launch the Tizen Studio installer.

2. Accept the software license.

   The license contains important legal notices for using Tizen Studio. Read it fully, and click **Accept** only if you agree with the license statement:

   ![Tizen Studio License Agreement](./media/install_sdk_license.png)

3. Click the ![Browse](./media/advanced_conf_browse.png) button and specify a new directory to set the SDK and data location. If the new directory is valid and shows no errors, click **Install**:

   ![Set SDK and data location](./media/install_sdk_directory.png)

4. Click **Install** to install the required packages and tools in the specified directory.

   You can monitor the installation process or cancel the installation. The installation process is completed in a few minutes, unless you cancel it.

5. Click **Finish** and close the installer:


   ![Installation complete](./media/migration_finish_instal.png)

   If you want to install additional platforms and tools, launch the Package Manager by checking the **Launch the Package Manager** check box and click **Finish**.

   Using the Tizen Studio Package Manager, you can install and update additional tools. For more information on the Package Manager, see [Updating Tizen Studio](./update-sdk.md).


   > **Note**
   >
   > If you install Tizen Studio in a directory that requires administrator privileges for access, such as `C:\Program Files`, administrator privileges are required to run the Tizen SDK tools.

The video below shows how Tizen Studio is installed in Windows using the IDE installer:

<video controls height="400">
  <source src="../media/tizenstudio-ideinstaller.mp4" type=video/mp4>
</video>

The video below shows how Tizen Studio is installed in Linux using the IDE installer:

<video controls height="400">
  <source src="../media/tizenstudio-ideinstaller-linux.mp4" type=video/mp4>
</video>


## Using the CLI Installer

The CLI (command line interface) provides functional tools for running the CLI installer without the GUI environment.

To install Tizen Studio using the CLI installer:

1. [Download the appropriate CLI installer for your platform](https://developer.tizen.org/development/tizen-studio/download).

2. Run the CLI installer:

   - On Microsoft Windows&reg;, the command prompt opens and the installer is automatically executed.
   - On Ubuntu and macOS, open the terminal, go to the directory where the installer is downloaded, and enter the `chmod +x` command to apply the execute permission to the installer file. Then, execute the installer by entering the command with the following syntax:

   ```
   web-cli_Tizen_Studio_<version> [options] [<directory path>]
   ```

   **Table: Install options**

   | Option             | Description                              |
   |--------------------|------------------------------------------|
   | `--show-license`   | Displays the Tizen Studio software license agreement.<br/> You must use this option alone. Do not use with other options. |
   | `--accept-license` | Accepts the license terms.               |
   | `--no-java-check`  | Skips the Java version check.            |

   **Table: Install command parameters**

   | Parameter        | Description                              |
   |------------------|------------------------------------------|
   | `directory path` | Specifies the installation directory path.<br/> If you do not enter the path, Tizen Studio is installed in the default directory (`/home/{user}/tizen-studio`). |

3. If you agree to the software license and the license terms, enter **Y(yes)** for the conditions.

4. Enter the Tizen Studio installation location.

   The CLI installer begins to install the Web App Development platform and tools on your computer.

> **Note**
>
> If you want to develop a native application on the CLI, you must install the Native App Development platform and tools using the CLI Package Manager.

The video below shows how Tizen Studio is installed in Windows using the CLI installer:

<video controls height="400">
  <source src="../media/tizenstudio-cliinstaller.mp4" type=video/mp4>
</video>

The video below shows how Tizen Studio is installed in Linux using the CLI installer:

<video controls height="400">
  <source src="../media/tizenstudio-cliinstaller-linux.mp4" type=video/mp4>
</video>

## Display packages with CLI

Run the CLI Package Manager with the `show-pkgs` command using the following syntax:

```
package-manager-cli show-pkgs [--proxy <value>] [--tree]
```
**Table: show-pkgs command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--proxy <value>`           | Proxy configuration value. Use one of the following values: **direct**, **auto**, or **ip:port**. |
| `--tree`                    | Display packages with tree. |

**Examples:**

- Run show-pkgs command with CLI.

  Windows&reg;, Ubuntu and macOS:

  ```
  > package-manager-cli show-pkgs --tree

  Display installed packages' information
  Package Manager (0.5.39)

  Status    Package Name                           Package Version      Component Name
   --------------------------------------------------------------------------------------------------
   u    	MOBILE-7.0                              			0.0.13         	7.0 Mobile      
   i    		MOBILE-7.0-Emulator                     		0.0.13         	Emulator            
   i    		MOBILE-7.0-NativeAppDevelopment         		0.0.13         	Native app. development (IDE)
   i    		MOBILE-7.0-WebAppDevelopment            		0.0.13         	Web app. development (IDE)
   ni   		AdvancedMOBILE-7.0                      		0.0.0          	Advanced         
   i    			MOBILE-7.0-NativeAppDevelopment-CLI     	0.0.13         	Native app. development (CLI)
   i    			MOBILE-7.0-WebFramework-TAU-CLI         	0.0.13         	TAU (CLI)           
   i    			MOBILE-7.0-WebFramework-TAU             	0.0.13         	TAU (IDE)           
   i    			MOBILE-7.0-WebAppDevelopment-CLI        	0.0.13         	Web app. development (CLI)
   ni   	WEARABLE-7.0                            			0.0.13         	7.0 Wearable        
   ni   		WEARABLE-7.0-Emulator                   		0.0.13         	Emulator            
   ni   		WEARABLE-7.0-NativeAppDevelopment       		0.0.13         	Native app. development (IDE)
   ni   		WEARABLE-7.0-WebAppDevelopment          		0.0.13         	Web app. development (IDE)
   ni   		AdvancedWEARABLE-7.0                    		0.0.0          	Advanced            
   ni   			WEARABLE-7.0-NativeAppDevelopment-CLI   	0.0.13         	Native app. development (CLI)
   ni   			WEARABLE-7.0-WebFramework-TAU-CLI       	0.0.13         	TAU (CLI)           
   ni   			WEARABLE-7.0-WebFramework-TAU           	0.0.13         	TAU (IDE)           
   ni   			WEARABLE-7.0-WebAppDevelopment-CLI      	0.0.13         	Web app. development (CLI)
   ni    	MOBILE-6.5                              			0.0.9          	6.5 Mobile          
   ni   		MOBILE-6.5-Emulator                     		0.0.9          	Emulator            
   ni   		MOBILE-6.5-NativeAppDevelopment         		0.0.9          	Native app. development (IDE)
   ni   		MOBILE-6.5-WebAppDevelopment            		0.0.9          	Web app. development (IDE)
   ni   		AdvancedMOBILE-6.5                      		0.0.0          	Advanced            
   ni   			MOBILE-6.5-NativeAppDevelopment-CLI     	0.0.9          	Native app. development (CLI)
   ni   			MOBILE-6.5-WebFramework-TAU-CLI         	0.0.9          	TAU (CLI)           
   ni   			MOBILE-6.5-WebFramework-TAU             	0.0.9          	TAU (IDE)           
   ni   			MOBILE-6.5-WebAppDevelopment-CLI        	0.0.9          	Web app. development (CLI)
   ni   	WEARABLE-6.5                            			0.0.9          	6.5 Wearable        
   ni   		WEARABLE-6.5-Emulator                   		0.0.9          	Emulator            
   ni   		WEARABLE-6.5-NativeAppDevelopment       		0.0.9          	Native app. development (IDE)
   ni   		WEARABLE-6.5-WebAppDevelopment          		0.0.9          	Web app. development (IDE)
   ni   		AdvancedWEARABLE-6.5                    		0.0.0          	Advanced            
   ni   			WEARABLE-6.5-NativeAppDevelopment-CLI   	0.0.9          	Native app. development (CLI)
   ni   			WEARABLE-6.5-WebFramework-TAU-CLI       	0.0.9          	TAU (CLI)           
   ni   			WEARABLE-6.5-WebFramework-TAU           	0.0.9          	TAU (IDE)           
   ni   			WEARABLE-6.5-WebAppDevelopment-CLI      	0.0.9          	Web app. development (CLI)
  ```


## Installing Additional Packages with CLI

Run the CLI Package Manager with the `install` command using the following syntax:

```
package-manager-cli install [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] <package name>[,...]
```

**Table: Install command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--accept-license`          | Accepts the license terms.               |
| `--no-java-check`           | Skips the Java version check.            |
| `--proxy <value>`           | Proxy configuration value. Use one of the following values: **direct**, **auto**, or **ip:port**. |
| `-f, --file <file path>`    | If you want to install packages from a local SDK image, specify the full path of the SDK image file. |
| `-p, --password <password>` | Administrator (sudo) password for authentication. Ubuntu only. |
| `<package name>[,...]`        | Name of the package you want to install. You can enter multiple package names (such as **NativeIDE** and **Emulator**).<br/>To retrieve the names of installable packages, use the following command:<br/>`package-manager-cli show-pkgs` |


## Update installed packages with CLI

Run the CLI Package Manager with the `update` command using the following syntax:

```
package-manager-cli update [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] [--latest]
```

**Table: Update command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--accept-license`          | Accepts the license terms.               |
| `--no-java-check`           | Skips the Java version check.            |
| `--proxy <value>`           | Proxy configuration value. Use one of the following values: **direct**, **auto**, or **ip:port**. |
| `-f, --file <file path>`    | If you want to install packages from a local SDK image, specify the full path of the SDK image file. |
| `-p, --password <password>` | Administrator (sudo) password for authentication. Ubuntu only. |
| `--latest`                  | Set latest snapshot (work on show-repo-info, update). |

**Examples:**

- Update package with CLI.

  Windows&reg;, Ubuntu and macOS:

  ```
  > package-manager-cli update --accept-license --no-java-check -p <password> --latest

  Package Manager (0.5.39)

  ****************************************
  ******* Start to update packages *******
  ****************************************
  Under packages will be updated.
           * Baseline-SDK
           * Certificate-Manager
           * Emulator
           * NativeCLI
           * MOBILE-7.0-NativeAppDevelopment-CLI
           * MOBILE-7.0-NativeAppDevelopment
           * MOBILE-7.0-WebAppDevelopment-CLI
           * MOBILE-7.0-WebAppDevelopment
           * MOBILE-7.0-Emulator
           * MOBILE-7.0-WebFramework-TAU-CLI
           * MOBILE-7.0-WebFramework-TAU
   [Baseline-SDK]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [Certificate-Manager]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [Emulator]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [NativeCLI]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-NativeAppDevelopment-CLI]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-NativeAppDevelopment]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-WebAppDevelopment-CLI]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-WebAppDevelopment]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-Emulator]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-WebFramework-TAU-CLI]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   [MOBILE-7.0-WebFramework-TAU]
   0% [------------------------------------]100%
      [++++++++++++++++++++++++++++++++++++]
   Updating has been completed.

  ```


## Uninstall packages with CLI

Run the CLI Package Manager with the `uninstall` command using the following syntax:

```
package-manager-cli uninstall [-p <password>] <package name>[,...]|--all
```

**Table: Uninstall command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `-p, --password <password>` | Administrator (sudo) password for authentication. Ubuntu only. |
| `<package name>[,...]`        | Name of the package you want to uninstall. You can enter multiple package names (such as **NativeIDE** and **Emulator**).<br/>To retrieve the names of uninstallable packages, use the following command:<br/>`package-manager-cli show-pkgs` |
| `--all`                     | Uninstall all packages. |

**Examples:**

- Uninstall package with CLI.

  Windows&reg;, Ubuntu and macOS:

  ```
  > package-manager-cli uninstall -p <password> MOBILE-4.0

  Package Manager (0.5.39)

   *****************************************
   **** Start to uninstall Tizen Studio ****
   *****************************************
   [MOBILE-4.0-WebFramework-TAU] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-WebFramework-TAU-CLI] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-WebAppDevelopment] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-NativeAppDevelopment] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-WebAppDevelopment-CLI] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-NativeAppDevelopment-CLI] 
   0% [----------------------------------------] 100 %
      [----------------------------------------]
   [MOBILE-4.0-Emulator] 
   0% [----------------------------------------] 100 %
   Uninstall has been completed
  ```


## Activate/Deactivate extra server with CLI

Run the CLI Package Manager with the `extra` command using the following syntax:

```
package-manager-cli extra -act|-dact <index[,...]>
```

**Table: Activate/Deactivate command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `-act`                      | Activate extra server. |
| `-dact`                     | Deactivate extra server.|
| `index[,...]`               | Index of extra servers. |

**Examples:**

**To get the index of different servers**

Run the command using the following syntax:

- Windows&reg;, Ubuntu and macOS:

  ```
  > package-manager-cli extra --list

  Package Manager (0.5.39)
   Preparing...
   Validating...
   Index        : 1
   Name         : Samsung Certificate Extension
   Repository   : https://download.tizen.org/sdk/extensions/tizen-certificate-extension_2.0.61.zip
   Default      : true
   Activate     : true

   Index        : 2
   Name         : Samsung Wearable Extension
   Repository   : https://developer.samsung.com/sdk-manager/repository/tizen-wearable-extension-sdk-1.5.0.zip
   Default      : true
   Activate     : true

   Index        : 3
   Name         : Samsung Tizen TV SDK
   Repository   : https://sdf.samsungcloudcdn.com/Public/smart_tv_sdk/releases/samsung_tizen_studio_tv_sdk/stv_ext_public/TV
   Default      : true
   Activate     : true

   Index        : 4
   Name         : Tizen IoT Headed
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headed
   Default      : true
   Activate     : true

   Index        : 5
   Name         : Tizen IoT Headless
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headless
   Default      : true
   Activate     : true

   Index        : 6
   Name         : Tizen IoT Setup Manager
   Repository   : https://download.tizen.org/sdk/extensions/iot-setup-mgr
   Default      : false
   Activate     : true

  ```
Run the act/dact command using the above index:
- Example: extra -act command
   ```
   > package-manager-cli extra -act 1

   Package Manager (0.5.39)
   Preparing...
   Validating...

   Extension         : Samsung Certificate Extension
   Activation status : true
  ```
- Example: extra -dact command
   ```
   > package-manager-cli extra -dact 1

   Package Manager (0.5.39)
   Preparing...
   Validating...

   Extension         : Samsung Certificate Extension
   Activation status : false
   ```

## Remove existing extra server with CLI

Run the CLI Package Manager with the `extra` command using the following syntax:

```
package-manager-cli extra --remove <index[,...]>
```
**Table: Activate/Deactivate command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--remove`                  | Remove existing extra server. |
| `index[,...]`               | Index of extra servers. |

**Examples:**

**To get the index of different servers, use the following command:**

- Windows&reg;, Ubuntu, and macOS:

  ```
  > package-manager-cli extra --list
  ```

**To remove existing extra server**

Run the commands using the following syntax:

- Windows&reg;, Ubuntu, and macOS:

  ```
  > package-manager-cli extra --remove 6

   Package Manager (0.5.39)
   Preparing...
   Validating...
   Tizen IoT Setup Manager is removed.

   > package-manager-cli extra --list

   Package Manager (0.5.39)
   Preparing...
   Validating...
   Index        : 1
   Name         : Samsung Certificate Extension
   Repository   : https://download.tizen.org/sdk/extensions/tizen-certificate-extension_2.0.61.zip
   Default      : true
   Activate     : true

   Index        : 2
   Name         : Samsung Wearable Extension
   Repository   : https://developer.samsung.com/sdk-manager/repository/tizen-wearable-extension-sdk-1.5.0.zip
   Default      : true
   Activate     : true

   Index        : 3
   Name         : Samsung Tizen TV SDK
   Repository   : https://sdf.samsungcloudcdn.com/Public/smart_tv_sdk/releases/samsung_tizen_studio_tv_sdk/stv_ext_public/TV
   Default      : true
   Activate     : true

   Index        : 4
   Name         : Tizen IoT Headed
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headed
   Default      : true
   Activate     : true

   Index        : 5
   Name         : Tizen IoT Headless
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headless
   Default      : true
   Activate     : true
  ```

## Add new extra server with CLI

Run the CLI Package Manager with the `extra` command using the following syntax:

```
package-manager-cli extra --add -n <name> -r <address>|-f <extra path>
```
**Table: Activate/Deactivate command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--add`                     | Add new extra server. |
| `-n <name>`                 | Server name. |
| `-r <address>`              | Set repository address. |
| `-f <extra path>`           | Set extra file path. |

**Examples:**

**To add a new server**

Run the commands using the following syntax:

- Windows&reg;, Ubuntu and macOS:

  ```
  > package-manager-cli extra --add -n "Tizen-IoT-Setup-Manager" -r https://download.tizen.org/sdk/extensions/iot-setup-mgr

   Package Manager (0.5.39)
   Preparing...
   Validating...
   Extension name : Tizen-IoT-Setup-Manager
   Extension url  : https://download.tizen.org/sdk/extensions/iot-setup-mgr

   Result
   New extension is successfully added.
   Index        : 6
   Name         : Tizen-IoT-Setup-Manager
   Repository   : https://download.tizen.org/sdk/extensions/iot-setup-mgr
   Id           : b2ee4215-c8ab-4ef0-a13c-2898b8eaee54
   Vendor       : none
   Description  : none
   Default      : false
   Activate     : true

   > package-manager-cli extra --list

   Package Manager (0.5.39)
   Preparing...
   Validating...
   Index        : 1
   Name         : Samsung Certificate Extension
   Repository   : https://download.tizen.org/sdk/extensions/tizen-certificate-extension_2.0.61.zip
   Default      : true
   Activate     : true

   Index        : 2
   Name         : Samsung Wearable Extension
   Repository   : https://developer.samsung.com/sdk-manager/repository/tizen-wearable-extension-sdk-1.5.0.zip
   Default      : true
   Activate     : true

   Index        : 3
   Name         : Samsung Tizen TV SDK
   Repository   : https://sdf.samsungcloudcdn.com/Public/smart_tv_sdk/releases/samsung_tizen_studio_tv_sdk/stv_ext_public/TV
   Default      : true
   Activate     : true

   Index        : 4
   Name         : Tizen IoT Headed
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headed
   Default      : true
   Activate     : true

   Index        : 5
   Name         : Tizen IoT Headless
   Repository   : https://download.tizen.org/sdk/extensions/Tizen_IoT_Headless
   Default      : true
   Activate     : true

   Index        : 6
   Name         : Tizen-IoT-Setup-Manager
   Repository   : https://download.tizen.org/sdk/extensions/iot-setup-mgr
   Default      : false
   Activate     : true

   > package-manager-cli install --accept-license --no-java-check Tizen-IoT-Setup-Manager
   
   > package-manager-cli uninstall -p <password> Tizen-IoT-Setup-Manager
  ```

## Related information
- Dependencies
  - Tizen Studio 1.0 and Higher
