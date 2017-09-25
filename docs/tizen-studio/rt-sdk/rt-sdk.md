# RT IDE
## Dependencies
- Ubuntu Only


The Tizen Studio for RT provides a lightweight RTOS (real-time operating system)-based application development environment that helps you develop, build, and flash applications in Ubuntu. The Tizen Studio for RT allows you to easily develop and test your RT application:

1. [Install the Tizen Studio for RT](rt-install.md) on your computer.
2. [Create a project](rt-create-project.md) from local templates or remote git.
3. [Create an application](rt-create-app.md) within a project.
4. [Build the project](rt-build.md) to be able to flash it.
5. [Flash the project](rt-flash.md) on the board.
6. [Use the serial terminal](rt-terminal.md) to communicate with the board.

## Prerequisites

Check the following prerequisites before installing the Tizen Studio for RT:

- Java Development Kit (JDK) requirements

  You must install a JDK 8 or higher to use the Tizen Studio. Do not install OpenJDK.

  To install the appropriate JDK version for your Ubuntu system, go to the Ubuntu Web site and follow the detailed instructions for installing the Oracle® JDK version 8 or higher.

- Operating system and hardware requirements

  The following table lists the supported operating systems and hardware requirements for the Tizen Studio for RT.

  **Table: Operating system and hardware requirements**

  | OS           |                              |
  | ------------ | ---------------------------- |
  | Version      | Ubuntu 16.04 / 14.04 / 12.04 |
  | Bit          | 64 bit / 32 bit              |
  | Hardware     |                              |
  | CPU          | Dual Core, 2 GHz or faster   |
  | Architecture | x64                          |
  | Memory       | 3 GB or more                 |
  | Disk space   | 6 GB or more                 |

- RT platform requirements

  For the additional requirements and guides related to building and flashing an RT application, see:

  - [Tizen RT Github](https://github.com/Samsung/TizenRT)[ARTIK053 board](https://github.com/Samsung/TizenRT/blob/master/build/configs/artik053/README.md)[sidk_s5jt200 board](https://github.com/Samsung/TizenRT/blob/master/build/configs/sidk_s5jt200/README.md)
  - [Tizen RT Getting Started](https://wiki.tizen.org/wiki/Tizen_RT_Getting_Started)

- Package requirements for developing applications in Ubuntu

  You must install the webkitgtk package. At the terminal prompt, enter the following command:

  `$ sudo apt-get install libwebkitgtk-1.0-0`