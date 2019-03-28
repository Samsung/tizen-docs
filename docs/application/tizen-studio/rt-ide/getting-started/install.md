# Install Tizen Studio for RT

This section explains about the prerequisites required to install Tizen Studio for RT. It also walks you through the installation steps.

## Prerequisites

Before installing Tizen Studio for RT, ensure that the following prerequisites are met:

1. Download the appropriate JDK version from the [official Oracle website](https://www.oracle.com/technetwork/java/javase/downloads/index.html).
   
   The following table list the supported Ubuntu version and JDK version for the Tizen Studio with RT:

   **Table: Operating System Version and JDK Version**
   
	
     | Ubuntu Version|JDK Version  | 
     |---------------|--------------|
     | 16.04 or 18.04 | 8, 9, or 10 |
   
   ![JDK Installation](media\v1_install_jdk_10.gif)
   
2. Install the required prerequisite packages (`webkitgtk` and `cpio`) for developing applications:

    `sudo apt-get install libwebkitgtk-1.0-0 cpio rpm2cpio`

3. Install the required [Docker CE](https://docs.docker.com/install/linux/docker-ce/ubuntu/) package for Ubuntu.

 ![Docker](media\v2_install_docker.gif)
 
## Install Tizen Studio for RT

To install Tizen Studio for RT:

1. Go to the [Download](https://developer.tizen.org/development/tizen-studio/download) page.

2. Select **Ubuntu** from the **Select OS** drop down list.

3. Download **Tizen Studio 3.1 for RT IDE installer**.

4. On your Ubuntu system, open the terminal. 

   ![Download RT IDE](media\v3_download_rtide.gif)

5. Go to the directory where the installer is downloaded, and enter the `chmod +x` command to apply the execute permission to the installer file:
    
	`chmod +x tizen-sdk-3.1-ubuntu-64.bin./tizen-sdk-<version>-ubuntu<bits>.bin`

     For example, `chmod +x RT_Tizen_Studio_3.1_ubuntu-64.bin`.    
	 
	 ![Install RT IDE](media\v4_install_rtide.gif)

6.	Execute the following command to launch:

    `./RT_Tizen_Studio_3.1_ubuntu-64.bin`

   
## Launch Tizen Studio for RT

   After launching the Tizen Studio for RT from the application shortcut, select a workspace for your development:

   ![Launch the IDE](./media/rt_install_launch.png)

The following figure illustrates launching Tizen Studio for RT IDE:

![Launching the Tizen Studio for RT IDE](./media/rt_running_studio.png)

Tizen RT IDE is now installed.
