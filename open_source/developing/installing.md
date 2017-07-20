# Installing development tools

PUBLISHED 21 DEC 2016

## 1 Introduction

This document provides information about how to install development tools in Ubuntu, openSUSE, Fedora, and CentOS, including the following:

- **Git Build System (GBS):** command line tool that supports Tizen package development.
- **Image Creator (MIC):** command line tool that supports Tizen image creation.
- **bmaptool:** generic tool for creating the block map (bmap) for a file and copying files using the block map.

**Note:** GBS and MIC are shown as examples because they are mandatory development tools for Tizen developers.

For a list of all supported Linux distribution versions, refer to [Setting up Development Environment](https://source.tizen.org/documentation/developer-guide/environment-setup).

## 2 Installing Development Tools

This section provides information about installing development tools.

### 2.1 Installing Development Tools in Ubuntu and Debian

To install a development tool in Ubuntu, perform the following procedure:

1. Open the source list by using text editor.

   An example using VIM is shown below:

   ```
   $ sudo vim /etc/apt/sources.list
   ```

2. Add Tizen tools repository to the source list.

   Take Ubuntu 16.04 as an example, append the following content in the source list:

   ```
   deb [trusted=yes] http://download.tizen.org/tools/latest-release/Ubuntu_16.04 /
   ```

   Take Ubuntu 14.04 as an example, append the following content in the source list:

   ```
   deb http://download.tizen.org/tools/latest-release/Ubuntu_14.04 /
   ```

   **Note:** Pay special attention to the space between the URL and "/".

3. Resynchronize the package index files from the sources specified in the source list by executing the following command:

   ```
   $ sudo apt-get update
   ```

4. Install a development tool by executing the following command:

   ```
   $ sudo apt-get install <Package_Name>
   ```

   An example of installing GBS and MIC is shown below:

   ```
   $ sudo apt-get install gbs mic
   ```

5. Upgrade a development tool by using one of following methods, as appropriate:

   ```
   $ sudo apt-get install <Package_Name>
   ```

   or

   ```
   $ sudo apt-get update$ sudo apt-get upgrade
   ```

   **Note:** The apt-get update command is recommended because it upgrades one or more already installed packages without upgrading every package installed, whereas the apt-get upgrade command installs the newest version of all currently installed packages. In addition, apt-get update command must be executed before an upgrade to resynchronize the package index files.

### 2.2 Installing Development Tools in openSUSE

Install a development tool in openSUSE, perform the following procedure:

1. Add Tizen tools repository to the source list.

   Take openSUSE 12.1 as an example, execute the following command:

   **Note:** Pay special attention to the space between the URL and "tools".

   ```
   $ sudo zypper addrepo http://download.tizen.org/tools/latest-release/openSUSE_12.1/ tools
   ```

2. Install a development tool by executing the following commands:

   ```
   $ sudo zypper refresh$ sudo zypper install <Package_Name>
   ```

   An example of installing GBS and MIC is shown below:

   ```
   $ sudo zypper refresh$ sudo zypper install gbs mic
   ```

3. Upgrade a development tool by executing the following commands:

   ```
   $ sudo zypper refresh$ sudo zypper update <Package_Name>
   ```

### 2.3 Installing Development Tools in Fedora and CentOS

To install a development tool in Fedora and CentOS, perform the following procedure:

1. Add Tizen tools repository to the source list.

   Take Fedora 20 as an example, execute the following command:

   ```
   $ sudo wget -O /etc/yum.repos.d/tools.repo http://download.tizen.org/tools/latest-release/Fedora_20/tools.repo
   ```

2. Install a development tool by executing the following commands:

   ```
   $ sudo yum makecache$ sudo yum install <Package_Name>
   ```

   An example of installing GBS and MIC is shown below:

   ```
   $ sudo yum makecache$ sudo yum install gbs mic
   ```

3. Upgrade a development tool by executing the following commands:

   ```
   $ sudo yum makecache$ sudo yum update <Package_Name>
   ```