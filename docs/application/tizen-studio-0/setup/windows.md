# Install Tizen Studio on Windows

This page explains the process to download and install Tizen Studio on your development hardware.

To have optimal installation experience, follow these steps chronologically:

- System prerequisites
  - Hardware requirements
  - Software requirements
- Setup OpenJDK in Windows
- Launch installer
- Verify installation

<style type="text/css">
a.clickable   { width: 100%; height: 100%; }
a.clickable:hover   { background-color: ; color: #FFFFF; }
</style>

## System Prerequisites

Ensure that the following system prerequisites are met:

### Hardware Requirements
<table>
  <tr>
      <td width=150px>CPU</td>
    <td colspan="3" width=50px>Dual Core, 2Ghz or faster</td>
  </tr>
  <tr>
    <td>Architecture</td>
    <td width=520px>x32 or x64 </td>
  </tr>
  <tr>
    <td>Memory</td>
    <td colspan="3">3GB or more </td>
  </tr>
  <tr>
    <td>Disk space</td>
    <td colspan="3">6 GB or more </td>
  </tr>
</table> 

### Software Requirements
<table>
  <tr>
    <th colspan="2" align=left>Windows</th>
  </tr>
  <tr>
    <td width=150px>Version</td>
    <td width=520px>7/8/10</td>
  </tr>
  <tr>
    <td>Bit</td>
    <td>32 or 64 bit</td>
  </tr>
</table>

<table>
  <tr>
    <th>Software</th>
    <th>Download Link </th>
  </tr>
  <tr>
    <td>Open JDK</td>
    <td width=520px><a href="https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_windows-x64_bin.tar.gz" class="clickable" target="_blank">https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_windows-x64_bin.tar.gz</a></td>
  </tr>
  <tr>
    <td>OpenJavaFX</td>
    <td><a href=http://gluonhq.com/download/javafx-11-0-2-sdk-windows/ class="clickable" target="_blank">http://gluonhq.com/download/javafx-11-0-2-sdk-windows/</a></td>
  </tr>
  <tr>
    <td>Tizen Studio setup file</td>
    <td><a href="https://developer.tizen.org/development/tizen-studio/download#" class="clickable" target="_blank">https://developer.tizen.org/development/tizen-studio/download#</a></td>
  </tr>
</table>

> **Note:**
>
> - Download the relevant version based on the target device operating system, for example, **openjdk-10_windows-x64_bin.tar.gz** and **openjfx-11.0.2_windows-x64_bin-sdk.zip**
> - Ensure that you download the JavaFX <OS> SDK product only, for example: JavaFX Windows SDK.

**Disclaimer:** The third party download links are subjected to change. Search and download the appropriate software.

## Set Up Open JDK

 To set up the Open JDK, follow these steps: 

1. Extract the downloaded **openjdk-10_windows-x64_bin.tar.gz**, and **openjfx-11.0.2_windows-x64_bin-sdk.zip** files at your preferred location.
     >**Note**
     >
     >The **openjdk-10_windows-x64_bin > jdk-10**, **openjfx-11.0.2_windows-x64_bin-sdk** directories are created as a result of extraction. 
2. Locate the **jdk-10** and the **javafx-sdk-11.0.2** directories after extraction.
    > **Note**
    >
    > - The **jdk-10** is the sub directory under the **openjdk-10_windows-x64_bin** directory.
    >- The **javafx-sdk-11.0.2** is the sub directory under the **openjfx-11.0.2_windows-x64_bin-sdk** directory.
3. Double click to open the **javafx-sdk-11.0.2** directory.
4. Copy all the files except the **src.zip** from the **lib** sub directory located in the **javafx-sdk-11.0.2** directory.
5. Paste all the copied files in the **lib** sub directory of the  **jdk-10** directory.
6. Copy all the files from the **bin** sub directory in the **javafx-sdk-11.0.2**.
7. Paste all the copied files in the **bin** sub directory of the **jdk-10** directory.

   >**Note**
   >
   >- In this installation guide, setting up OpenJDK is covered. However, Oracle JDK versions until version 10 are also supported.
   >- For Oracle JDK 10 installation steps, see the [Oracle Documentation](https://docs.oracle.com/javase/10/install/installation-jdk-and-jre-microsoft-windows-platforms.htm#JSJIG-GUID-DAF345BA-B3E7-4CF2-B87A-B6662D691840).
   >- If you have installed Oracle JDK 10 or below already, you can skip setting up OpenJDK. 
 
### Set Up Open JDK Path 

To set up the JDK path, follow these steps:

1. On the Windows desktop, click **Start > Control Panel > System and security > System > Advanced system settings**, the System Properties window appears. 
3. In the **Startup and Recovery** section, click **Environment Variables** the Environment Variables window appears.  
4. Click **New** under **User variables for {user}** section, also in case the **JAVA_HOME** variable is already in the list, select it and click **Edit**, enter the following details: 
	- Variable name: **JAVA_HOME** 
	- Variable value: **C:\Path\to\your\openJDKtype**, i.e. browse for the JDK directory path (for example, C:\Users\user\Desktop\jdk-10.0.2) 	
5. Click **OK**, the Environment Variable list is updated with the **JAVA_HOME** variable.
6. Click **New** under the **System variables** section also in case, if the **Path variable** already exists, select it and click **Edit**, and enter the following details: 
	- Variable name: **Path** 
	- Variable value: **C:\Path \to\ openJDK\bin directory**; i.e. browse for the **bin** subdirectory path in the JDK directory  (for example, C:\Users\user\Desktop\jdk-10.0.2\bin ) 
8. Click **OK**, the System Variable list is updated with the **Path** variable.
9. Save and close the **Environment Variables** window.
10. Open Command Prompt and type the `java –version` command to verify whether the OpenJDK version 10 is installed or not. Entering the command must give the following output: 

   ```windows console
   C:\Users\exampleconsole>java -version
   openjdk version "10" 2018-03-20
   OpenJDK Runtime Environment 18.3 (build 10+46)
   OpenJDK 64-Bit Server VM 18.3 (build 10+46, mixed mode)
   ```

## Launch Installer
 
To launch the installer, follow these steps:

1. Double click **web-ide_Tizen_Studio_x.x_windows-64.exe** file.
	>**Note:** 
	>
	>**x.x** represents the latest version of Tizen Studio, for example:web-ide_Tizen_Studio_**3.3**_windows-64.exe.

2. Accept the software license.

   >**Note:**
   >
   >The license contains important legal notices for using Tizen Studio. Read it fully, and click **Accept** only if you agree with the license statement.

   ![Tizen Studio License Agreement](./media/install_sdk_license.png)

3. Click **Browse** and specify a new directory to set the SDK data location. 

   ![Set SDK and data location](./media/install_sdk_directory.png)
  
   >**Note:** 
   > 
   >If the new directory is valid, it shows no errors.

4. Click **Install**.
5. Click **Finish** to close the installer.

   ![Installation complete](./media/migration_finish_instal.png)

   >**Note:**
   >
   > - If you install the Tizen Studio in a directory that requires administrator privileges for access, such as `C:\Program Files`, then administrator privileges are required to run the Tizen SDK tools.
   > - If you want to install additional platforms and tools, launch Package Manager by selecting the Launch the Package Manager **check box** and click **Finish**.
   > - Use Tizen Package Manager, to install and update additional tools. 
   > - For more information on the Package Manager, see [Updating Tizen Studio](./update-sdk.md).

## Verify Installation   

   To verify whether the installation is successful or not, click **Tizen Studio icon**. The Tizen Studio startup window must appear.