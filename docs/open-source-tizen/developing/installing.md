# Installing Development Tools

Tizen SCM tools support the following Linux distribution versions:

- Ubuntu 16.04/14.04/12.04
- openSUSE 13.2/13.1/12.3/Leap 42.1
- Fedora 23/22/21/20
- CentOS 7/6
- Debian 8/7

You can install a variety of development tools, including:

- **Git Build System (GBS)** command line tool that supports Tizen package building.
- **Image Creator (MIC)** command line tool that supports Tizen image creation.

> **Note**
>
> GBS and MIC are used as examples because they are mandatory development tools for Tizen developers.

## Installing Development Tools in Ubuntu or Debian

To install a development tool in Ubuntu or Debian:

> **Note**
>
> The `apt-get install <Package_Name>` command is recommended because it upgrades 1 or more already installed packages without upgrading every package installed, whereas the `apt-get upgrade` command installs the newest version of all currently installed packages. In addition, `apt-get update` must always be executed before `apt-get install <Package_Name>` or `apt-get upgrade`, to resynchronize the package index files.

1. Open the package manager source list using a text editor.

   VIM is used in the following example:

   ```bash
   $ sudo vim /etc/apt/sources.list
   ```

2. Add the Tizen tools repository to the source list.

   For example:

   - In Ubuntu 16.04, append the following line to the source list:

     ```
     deb [trusted=yes] http://download.tizen.org/tools/latest-release/Ubuntu_16.04/ /
     ```

   - In Ubuntu 14.04, append the following line to the source list:

     ```
     deb http://download.tizen.org/tools/latest-release/Ubuntu_14.04/ /
     ```

   > **Note**
   >
   > Pay special attention to the space between the URL and "/".

3. Resynchronize the package index files from the sources specified in the source list:

   ```bash
   $ sudo apt-get update
   ```

4. Install a development tool:

   ```bash
   $ sudo apt-get install <Package_Name>
   ```

   For example, to install GBS and MIC:

   ```bash
   $ sudo apt-get install gbs mic
   ```

You can upgrade a development tool using 1 of following methods, as appropriate:

```bash
$ sudo apt-get update && sudo apt-get install <Package_Name>
$ sudo apt-get update && sudo apt-get upgrade
```

## Installing Development Tools in openSUSE

To install a development tool in openSUSE:

1. Add the Tizen tools repository to the package manager source list.

   In openSUSE 13.2, for example:

   ```bash
   $ sudo zypper addrepo http://download.tizen.org/tools/latest-release/openSUSE_13.2/ tools
   ```

   > **Note**
   >
   > Pay special attention to the space between the URL and "tools".

2. Install a development tool:

   ```bash
   $ sudo zypper refresh$ sudo zypper install <Package_Name>
   ```

   For example, to install GBS and MIC:

   ```bash
   $ sudo zypper refresh
   $ sudo zypper install gbs mic
   ```

You can upgrade a development tool with the following commands:

```bash
$ sudo zypper refresh
$ sudo zypper update <Package_Name>
```

## Installing Development Tools in Fedora or CentOS

To install a development tool in Fedora or CentOS:

1. Add the Tizen tools repository to the package manager source list.

   In Fedora 23, for example:

   ```bash
   $ sudo wget -O /etc/yum.repos.d/tools.repo http://download.tizen.org/tools/latest-release/Fedora_23/tools.repo
   ```

2. Install a development tool:

   ```bash
   $ sudo yum makecache
   $ sudo yum install <Package_Name>
   ```

   For example, to install GBS and MIC:

   ```bash
   $ sudo yum makecache
   $ sudo yum install gbs mic
   ```

You can upgrade a development tool with the following commands:

```bash
$ sudo yum makecache
$ sudo yum update <Package_Name>
```
