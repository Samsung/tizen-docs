
# Install Tizen Studio on MacOS

This page explains the process to download and install Tizen Studio on your development hardware. 

To have the optimal installation experience, follow these steps chronologically:

- System prerequisites
   - Hardware requirements
   - Software requirements
   - Additional requirements
- Setup OpenJDK in Macintosh
- Launch installer
- Verify installation

<style type="text/css">
a.clickable   { width: 100%; height: 100%; }
a.clickable:hover   { background-color:; color: #FFFFF; }
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
    <td width=520px>x64 only</td>
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

### Software Requirements
<table>
  <tr>
    <th colspan="2" align=left>MacOSX</th>
  </tr>
  <tr>
    <td width=150px>Version</td>
    <td width=520px>10.13 (High Sierra)<br>10.12 (Sierra)<br>10.11 (El Captain)</td>
  </tr>
  <tr>
    <td>Bit</td>
    <td>64 bit only</td>
  </tr>
</table>

<table>
  <tr>
    <th>Software</th>
    <th>Download Link </th>
  </tr>
  <tr>
    <td>Open JDK</td>
    <td width=520px><a href="https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_osx-x64_bin.tar.gz" class="clickable" target="_blank">https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_osx-x64_bin.tar.gz" </a></td>
  </tr>
  <tr>
    <td>OpenJavaFX</td>
    <td><a href="http://gluonhq.com/download/javafx-11-0-2-sdk-mac" class="clickable" target="_blank"> http://gluonhq.com/download/javafx-11-0-2-sdk-mac</a></td>
  </tr>
  <tr>
    <td>Tizen Studio setup file</td>
    <td><a href="https://developer.tizen.org/development/tizen-studio/download#" class="clickable" target="_blank">https://developer.tizen.org/development/tizen-studio/download# </a></td>
  </tr>
</table>


>**Note:**
>
> - Download the relevant version based on the target device operating system, for example: **openjdk-10_osx-x64_bin.tar.gz**. 
> - Ensure that you download the JavaFX <OS> SDK product only, for example: JavaFX Mac OS X SDK.
  
**Disclaimer:** The third party download links are subjected to change. Search and download the appropriate software.


### Additional Requirements

<table>
<thead>
<tr>
<th>Component</th>
<th>Requirement</th>
</tr>
</thead>
<tbody>
<tr>
<td>Prerequisite packages (<code>msgfmt</code>) to build PO files
</td>
<td>On the terminal prompt, type the following commands:
<pre><code>$ brew install gettext
$ brew link gettext -force
$ which msgfmt
/usr/local/bin/msgfmt
</code></pre>
<strong>Note</strong><br>
To install Homebrew, see the<a href="http://brew.sh/">Homebrew documentation</a>.
</td>
</tr>
</tbody>
</table>

## Set Up Open JDK

To set up Open JDK, follow these steps: 

1. Extract the downloaded **openjdk-10_osx-x64_bin.tar.gz** file at your preferred location.
   - Locate the **jdk** directory where you extracted the **openjdk-10_osx-x64_bin.tar.gz** file.
     
	   >**Note:**
     >
     > The **jdk** directory is created as a result of extraction. 
   
2. Copy the **jdk** folder, paste it in the **Library/Java/JavaVirtualMachines** location. 
    
   >**Note:**
   >
   >This is the system default location, for all JDK files.
3. Open terminal.
4. Type the `java –version` command to verify whether the OpenJDK version 10 is installed.
   >**Note:**
   > 
   >If the OpenJDK version 10 is not installed, proceed with step 5.
5. Open the **.profile** or the **.bash_profile file**, add the `export JAVA_HOME =/Library/Java/JavaVirtualMachines/jdk-10.jdk/Contents/Home` line. 
6. Type `java –version` command to verify whether the OpenJDK version 10 is installed.
   >Note:
   >
   >- In this installation guide, setting up OpenJDK is covered. However,  Oracle JDK versions until version 10 are also supported.
   >- For Oracle JDK 10 installation steps, see the [Oracle official site](https://docs.oracle.com/javase/10/install/installation-jdk-and-jre-macos.htm#JSJIG-GUID-F575EB4A-70D3-4AB4-A20E-DBE95171AB5F). 
   >- If you have installed Oracle JDK 10 or below already, you can skip the step. 

## Launch Installer
 
To launch the installer, follow these steps:

1. Double click on the downloaded installer file **web-ide_Tizen_Studio_x.x-64.dmg**.
   >Note: 
   >
   >**x.x** represents the latest version of Tizen Studio, for example:web-ide_Tizen_Studio_**3.2**-64.dmg.

2. Accept the software license.
   >**Note:**
   >
   >The license contains important legal notices for using Tizen Studio. Read it fully, and click **Accept** only if you agree with the license terms.

   ![Tizen Studio License Agreement](./media/install_sdk_license.png)
3. Click **Browse** and specify a new directory to set the SDK location and the data location. 
   
   ![Set SDK and data location](./media/install_sdk_directory.png)
   
   >**Note:** 
   > 
   >If the new directory is valid, it shows no errors.
4. Click **Install**.
5. Click **Finish** and close the installer.
   
   ![Installation complete](./media/migration_finish_instal.png)
   > **Note:**
   >
   > - If you want to install additional platforms and tools, launch  Package Manager by selecting the Launch Package Manager **check box** and click **Finish**.
   > - Use Tizen Studio Package Manager, to install and update additional tools. 
   > - For more information on the Package Manager, see [Updating Tizen Studio](./update-sdk.md).

## Verify Installation

To verify whether the installation is successful or not, click **Tizen Studio icon**. The Tizen Studio startup window must appear.

