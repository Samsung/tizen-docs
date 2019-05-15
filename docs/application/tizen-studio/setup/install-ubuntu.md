# Installation in Ubuntu

## Introduction
This section guides you with downloading and installing Tizen Studio on your development hardware. 

Follow the sub sections chronologically to get Tizen Studio installed with ease:

- Pre-Installation check
  - Operating System prerequisites
  - Hardware prerequisites
  - Software prerequisites
- Setup OpenJDK in Ubuntu
- Install dependencies
- Launch Installer
<!---- Troubleshooting 
- Uninstalling -->

## Pre-Installation Check 
To successfully install Tizen Studio, ensure all the prerequisites are met.

### Operating System Prerequisites
Ensure that the target system meets the following operating system requirements:
<table>
  <tr>
    <th colspan="2">Module </th>
    <th>Microsoft Windows</th>
    <th>MacOS</th>
    <th>Ubuntu</th>
  </tr>
  <tr>
    <td>Operating System<br></td>
    <td><br>Version <br><br><br><br>Bit</td>
    <td><br>7/8/10<br><br><br><br>64/32 bit</td>
    <td><br>10.13 (High Sierra)<br>10.12 (Sierra)<br>1.100 (El Captain)<br><br><br>64 bit only</td>
    <td><br>16.04/14.04/18.04<br><br><br><br><br>64/32 bit</td>
  </tr>
</table>

### Hardware Prerequisites
Ensure that the target system meets the following hardware requirements: 
<table>
  <tr>
    <th rowspan="4">Hardware </th>
    <th>CPU</th>
    <th colspan="3">Dual Core, 2Ghz or faster</th>
  </tr>
  <tr>
    <td>Architecture</td>
    <td>x64 (64 bit) / x86 (32 bit)<br>(Windows)</td>
    <td>x64 only<br>(Macintosh) </td>
    <td>x64 /x86 <br>(Ubuntu)<br></td>
  </tr>
  <tr>
    <td>Memory</td>
    <td colspan="3">3GB or more </td>
  </tr>
  <tr>
    <td>Disk Space</td>
    <td colspan="3">6 GB or more </td>
  </tr>
</table>

### Software Prerequisites
Ensure that the target system meets the following software requirements: 
<table>
  <tr>
    <th>Software</th>
    <th>Download Link </th>
  </tr>
  <tr>
    <td>Open JDK</td>
    <td>https://jdk.java.net/archive/</td>
  </tr>
  <tr>
    <td>OpenJavaFX</td>
    <td>https://gluonhq.com/products/javafx/</td>
  </tr>
  <tr>
    <td>Tizen Studio setup file</td>
    <td>https://developer.tizen.org/development/tizen-studio/download#</td>
  </tr>
</table>

> **Note:**
>
> - Download the relevant version based on target device operating system, for example, **openjdk-10_linux-x64_bin.tar.gz**. 
> - Ensure you download the JavaFX <OS> SDK product only, for example: JavaFX Linux SDK.
> - Alternatively, you can also try using Oracle JDK 10 or less instead of OpenJDK, see the official site for the installation steps.

## Setup OpenJDK in Ubuntu

Following steps help you to setup OpenJDK: 

1. Extract the downloaded **openjdk-10_linux-x64_bin.tar.gz**, and **javafx-11-0-2-sdk-linux.zip** files.
   - Locate **jdk-10** and **javafx-sdk-11.0.2** directories in your file system.
   > **Note:**
   >
   >  jdk-10, javafx-sdk-11.0.2 directories get created as a result of extraction. 
   
2. Navigate to the **lib** folder in the **javafx-sdk-11.0.2** directory and copy all the files except **src.zip**.
3. Navigate to the **lib** folder in the **jdk-10** directory and paste all the copied files.

Following steps help you to set up the JDK path:  

1.	Open the Terminal.
2.	Type the following command in the terminal to set the JAVA_HOME as OpenJDK directory path, for example:
	JAVA_HOME=/home/<username>/Desktop/openJDK/jdk-10.0.2/
	
3.	Type the following commands in the terminal one after the other:
	- `sudo update-alternatives --install /usr/bin/java java ${JAVA_HOME%*/}/bin/java 20000`
	- `sudo update-alternatives --install /usr/bin/javac javac ${JAVA_HOME%*/}/bin/javac 20000`
	
4.	Type the following command to get a list of JDK versions installed:
	- `sudo update-alternatives --config java`
	
	> **Note:**
    >
    >  If there are multiple JDK installed, enter the selection number to choose your desired JDK version.
	
5.	Type the following command:
	- `sudo update-alternatives --config javac`
	
	> **Note:**
    >
    >  javac is used for compilation. For more information on the differences between java and javac, see the official [site](https://docs.oracle.com).
	
6.	Type the following command to verify whether the OpenJDK version 10 is installed:
	`java –version`

## Install Dependencies

The Tizen Studio application may require additional libraries in order to work properly. The installer already provides the immediate libraries needed. Various distributions differ on how they are bundled; however, users have to manually install additional packages in order to have error free installation experience:

Open your Terminal, and execute the following commands: 
- `sudo apt-get install expect\`
- `sudo apt-get install gtk2-engines-pixbuf\`
- `sudo apt-get install libgnome2-0\`
- `sudo apt-get install qemu-user-static\`
- `sudo apt-get install libwebkitgtk-1.0-0\`
- `sudo apt-get install gettext\`
- `sudo apt-get install gksudo\`
- `sudo apt-get install module-init-tools\`
- `sudo apt-get install libudev-dev\`
- `sudo apt-get install libsdl1.2debian\`
- `sudo apt-get install bridge-utils\`
- `sudo apt-get install openvpn\`

## Launch Installer 
Following steps help you to launch the installer:

1. Open your terminal and execute the following command:
	- `chmod +x web-ide_Tizen_Studio_3.1_ubuntu-64.bin`
	- `./web-ide_Tizen_Studio_3.1_ubuntu-64.bin` 

2. Accept the software license

   > **Note:**
   >
   >  The license contains important legal notices for using Tizen Studio. Read it fully, and click **Accept** only if you agree with the license terms:

   ![Tizen Studio License Agreement](./media/install_sdk_license.png)

3. Click the **...** and specify a new directory to set the SDK and data location. If the new directory is valid and shows no errors, click **Install**:

   ![Set SDK and data location](./media/install_sdk_directory.png)

4. Clicking **Install** installs the required packages and tools in the specified directory.

   You can monitor the installation process or cancel the installation. The installation process is completed in a few minutes, unless you cancel it.

5. Click **Finish** and close the installer:


   ![Installation complete](./media/migration_finish_instal.png)

   > **Note**
   >
   > - If you install the Tizen Studio in a directory that requires administrator privileges for access, such as `C:\Program Files`, administrator privileges are required to run the Tizen SDK tools.
   > - If you want to install additional platforms and tools, launch the Package Manager by checking the **Launch the Package Manager** check box and click **Finish**.
   > - Using the Tizen Studio Package Manager, you can install and update additional tools. For more information on the Package Manager, see [Updating Tizen Studio](./update-sdk.md).

