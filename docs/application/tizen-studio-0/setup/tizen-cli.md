
## Install Tizen Studio using CLI  

This page guides you with Command Line Installation (CLI) of Tizen Studio. The CLI installer provides functional tools for running Tizen Studio without GUI environment.
The CLI installation is mostly intended for advanced users. The Tizen Studio CLI installation for all major operating systems is covered in the following sections.  

### Prerequisites

1. Ensure that you download the appropriate CLI installer for your operating system. For more information, see [Download page](https://developer.tizen.org/development/tizen-studio/download#).
2. Ensure that you have Open JDK 10 or Oracle JDK 10 installed on your development hardware, for more information, see the following table  to setup Open JDK: 

     | Operating System  | Open JDK Setup Information  |  
     |---|----|
     |  Windows   | <link to section on GUI installation>  |
     |Ubuntu |       <link>| 
     |MacOS  |       <link> | 

### Installation 


The CLI installation takes minimal network bandwidth to download. Follow the Console window to see the installation progress. 

To install the Tizen Studio using the CLI installer, proceed as follows:

Run the CLI installer:   
- In Windows, double click on the installer file, The console windows opens and the installer automatically executes.

- In Ubuntu and MacOS, follow these steps: 

    1. Open the terminal
    2. Navigate to the directory where you downloaded the installer file
    3. Enter the `chmod +x` command
    4. Enter the command with following syntax:

       ```
       web-cli_Tizen_Studio_<version> [options] [<directory path>]
       ```
The following table identifies the standard command line options for CLI installation. Command line options are case insensitive.
   
   **Table: Install options**

   | Option             | Description                              |
   |--------------------|------------------------------------------|
   | `--show-license`   | Displays the Tizen Studio software license agreement.<br/> You must use this option alone. Do not use with other options. |
   | `--accept-license` | Accepts the license terms.               |
   | `--no-java-check`  | Skips the Java version check.            |


The following table identifies the standard command line parameters for installation related tasks. Command line options are case insensitive.

   **Table: Install command parameters**

   | Parameter        | Description                              |
   |------------------|------------------------------------------|
   | `directory path` | Specifies the installation directory path.<br/> If you do not enter the path, the Tizen Studio is installed in the default directory (`/home/{user}/tizen-studio`). |

3. Agree to the license terms, enter **Y** when prompted, to proceed with installation.

4. Enter the Tizen Studio installation location. The CLI installer begins  installing Tizen Studio. 

> **Note**
>
>- By default, the Web App Development platform and related tools are installed. For installing Native application platform and tools use the CLI Package Manager.

## Install Additional Packages with CLI

The CLI package manager tool alos provides you the option to install other required packages and tools.

To run the CLI Package Manager with the `install` command use the following syntax:

```
package-manager-cli install [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] <package name>[,...]
```
The following table identifies the standard command line parameters for CLI package management tasks. Command line options are case insensitive.

**Table: Install command parameters**

| Parameter                   | Description                              |
|-----------------------------|------------------------------------------|
| `--accept-license`          | Accepts the license terms.               |
| `--no-java-check`           | Skips the Java version check.            |
| `--proxy <value>`           | Proxy configuration value. Use one of the following values: **direct**, **auto**, or **ip:port**. |
| `-f, --file <file path>`    | If you want to install packages from a local SDK image, specify the full path of the SDK image file. |
| `-p, --password <password>` | Administrator (sudo) password for authentication. (Ubuntu only). |
| `<package name>[,...]`        | Name of the package that you want to install. You can enter multiple package names (such as **NativeIDE** and **Emulator**).<br/>To retrieve the names of installable packages, use the following command:<br/>`package-manager-cli show-pkgs` |

