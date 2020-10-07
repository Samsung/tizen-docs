
# Install Tizen Studio using CLI  

This page explains how to install the Command Line Interface (CLI) version of Tizen Studio. The CLI installer provides functional tools for running Tizen Studio without a Graphical User Interface (GUI) environment.
The CLI installation is mostly intended for advanced developers. Tizen Studio CLI installation is supported on all the major operating systems. 

## Prerequisites

For seamless experience, ensure the following: 
 - Download the appropriate CLI installer for your operating system. For more information, see the [Download page](https://developer.tizen.org/development/tizen-studio/download#).
 - Install and set the appropriate JDK on your development hardware. For more information see [JDK Installation for CLI](./openjdk.md).

## Tizen Studio Command Line Installation  

Tizen Studio command-line installation takes minimal network resources, and time to download and install on your development hardware. 

 - To install Tizen Studio on Windows&reg; using the CLI installer, double click the installer file. The console window appears, and the installer gets executed automatically. You can follow the console window to see the installation progress. 
   
 - To install Tizen Studio on Ubuntu&reg; and macOS&reg;, navigate to the directory where you have downloaded the installer file and follow these steps:
      
    1. Open the terminal, type the `chmod +x` command to apply the execute permission to the installer file.
    3. Type the command with the following syntax:

       ```
       web-cli_Tizen_Studio_<version> [options] [<directory path>]
       ```
        The following table identifies the standard command line options for the CLI installation. Command line options are case insensitive:
   
        | Options             | Descriptions                              |
        |--------------------|------------------------------------------|
        | `--show-license`   | Displays Tizen Studio software license agreement.<br><br><b>Note:</b><br><br> You must use this option alone. Do not use with other options.</br> |
        | `--accept-license` | Accepts the license terms.               |
        | `--no-java-check`  | Skips the Java version check.            |

        The following table identifies the standard command line parameter for installation related tasks. Command line options are case insensitive:

       | Parameter        | Description                              |
       |------------------|------------------------------------------|
       | `directory path` | Specifies the installation directory path.<br/> <br>**Note:**<br><br> If you do not enter the path, Tizen Studio is installed in the default directory (`/home/{user}/tizen-studio`). |

    4. Accept the license terms and type **Y** when prompted, to proceed with the installation.
    5. Type Tizen Studio installation location. 

   The CLI installer begins installing Tizen Studio. 

> [!NOTE]
> By default, the Web App Development platform and related tools are installed. For installing the Native application platform and tools use CLI Package Manager.

## Install Additional Packages

The CLI package manager tool provides you the option to install additional required packages and tools.

To run the CLI Package Manager with the `install` command, use the following syntax:

```
package-manager-cli install [--accept-license] [--no-java-check] [--proxy <value>] [-f <file path>] [-p <password>] <package name>[,...]
```
The following table identifies the standard command-line parameters for CLI package management tasks: 

 > [!Note]
 > Command-line options are case insensitive.


| Parameters                  | Descriptions                             |
|-----------------------------|------------------------------------------|
| `--accept-license`          | Accepts the license terms.               |
| `--no-java-check`           | Skips the Java version check.            |
| `--proxy <value>`           | Proxy configuration value. Use any one of the following values: direct, auto, or ip:port. |
| `-f, --file <file path>`    | If you want to install packages from a local SDK image, specify the full path of the SDK image file. |
| `-p, --password <password>` | Administrator (sudo) password for authentication in Ubuntu only. |
| `<package name>[,...]`        | Name of the package you want to install. You can enter multiple package names such as **NativeIDE** and **Emulator**.<br/><br>To retrieve the names of the installable packages, use the following command:<br/>`package-manager-cli show-pkgs` |

