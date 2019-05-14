# Installation in Macintosh

## Introduction
This section guides you with downloading and installing Tizen Studio on your development hardware. 

Follow the sub sections chronologically to get Tizen Studio installed with ease:

- Pre-Installation check
  - Operating System prerequisites
  - Hardware prerequisites
  - Software prerequisites
- Setup OpenJDK in Macintosh
- Launch Installer
<!--- Troubleshooting 
- Uninstalling-->

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
    <td>CPU</td>
    <td colspan="3">Dual Core, 2Ghz or faster</td>
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
> - Download the relevant version based on target device operating system, for example, **openjdk-10_osx-x64_bin.tar.gz**. 
> - Ensure you download the JavaFX <OS> SDK product only, for example: JavaFX Mac OS X SDK.	
> - Alternatively, you can also try using Oracle JDK 10 or less instead of OpenJDK, see the official site for the installation steps.

## Setup OpenJDK in Macintosh

Following steps help you to setup OpenJDK: 

1. Extract the downloaded **openjdk-10_osx-x64_bin.tar.gz**.
   - Locate **jdk** directory.
   > **Note:**
   >
   >  jdk directory gets created as a result of extraction. 
   
2. Copy the **jdk** folder and paste in the following location:
     **Library/Java/JavaVirtualMachines**. 
    > **Note:**
    >
    >  This is the default location where all the JDKs are available.
	
3. Open Terminal.
4. Type the following command to verify whether the OpenJDK version 10 is installed:

    `java –version`
5. If the OpenJDK version 10 is not installed, add **export JAVA_HOME =
/Library/Java/JavaVirtualMachines/jdk-10.jdk/Contents/Home** command in the **.profile** or
**.bash_profile file**.
6. Type the following command to verify whether the OpenJDK version 10 is installed:

   `java –version`

## Launch Installer
 
 Following steps help you to launch the installer:

1. Launch the Tizen Studio installer by double clicking on the downloaded installer file **web-ide_Tizen_Studio_3.2-64.dmg**.

2. Accept the software license.

   > **Note:**
   >
   >  The license contains important legal notices for using Tizen Studio. Read it fully, and click **Accept** only if you agree with the license terms:

   ![Tizen Studio License Agreement](./media/install_sdk_license.png)

3. Click the **...** and specify a new directory to set the SDK and data location. If the new directory is valid and shows no errors, click **Install**:

   ![Set SDK and data location](./media/install_sdk_directory.png)

4. Click **Install** to install the required packages and tools in the specified directory.

   You can monitor the installation process or cancel the installation. The installation process is completed in a few minutes, unless you cancel it.

5. Click **Finish** and close the installer:


   ![Installation complete](./media/migration_finish_instal.png)

   > **Note**
   >
   > - If you want to install additional platforms and tools, launch the Package Manager by checking the **Launch the Package Manager** check box and click **Finish**.
   > - Using the Tizen Studio Package Manager, you can install and update additional tools. For more information on the Package Manager, see [Updating Tizen Studio](./update-sdk.md).