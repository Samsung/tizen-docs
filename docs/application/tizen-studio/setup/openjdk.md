# OpenJDK 12 and OpenJFX installation guide

> [!NOTE]
> It is highly recommended to use the latest version of Tizen Studio. Since Tizen Studio 3.7, the JDK installation is bundled with Tizen Studio. There is no need to explicitly install JDK or set the variable paths. The following procedure of installing the JDK and setting the JDK variables is applicable for Tizen Studio 3.6 or lower. 

Open Java Development Kit (OpenJDK) is an open source implementation of the Java Standard Edition (Java SE) platform with contribution from Oracle and the open Java community. For more information, see [OpenJDK](http://openjdk.java.net/).

Open JavaFX (OpenJFX) is an open source, next generation client application platform for desktop, mobile and embedded systems built on Java. For more information, see [JavaFX](https://openjfx.io/).

Before JDK version 9, JavaFX libraries were included in the JDK distribution. Since JDK version 9, JavaFX (JFX) is provided as a separate package.

This document explains how to install the OpenJDK version 12 along with OpenJFX libraries for the following operating systems:

- [Windows](#install-openjdk-for-windows)
- [Linux](#install-openjdk-for-ubuntu)
- [MacOS](#install-openjdk-for-macos)

## Install OpenJDK

To install OpenJDK, you must download it as follow:
1. Download the OpenJDK version 12 from [https://jdk.java.net/archive/](https://jdk.java.net/archive/).

2. Extract the .tar file. The `jdk-12.0.2` folder appears.

### Install OpenJDK for Windows

This section explains how to install the OpenJDK version 12 for Windows:

1. Go to **Start** > **Control Panel** > **System and Security** > **System**.

2. Click **Advanced system settings**. The **System Properties** window appears.

3. Click **Environment Variables...**. The **Environment Variables** window appears.

4. Click **New...** in the **User variables for \<user name\>** section.
    
    > [!NOTE]
    > If your `JAVA_HOME` variable is already created, select it and click **Edit...**.

5. Enter `JAVA_HOME` in the variable name field and the JDK directory path, for example, `C:\Users\user\Desktop\jdk-12.0.2\bin` in the Variable value field.

6. Click **OK**. The Environment Variables window appears.

7. If you cannot find `JAVA_HOME` in **System variables** section, add the variable by repeating the 4, 5, and 6 steps.

8. Save and close the **Environment Variables** window.

9. Launch **Command Prompt**.

10. Run the following command to verify whether the OpenJDK version 12 is installed:
    ```
    java -version
    ```
> [!NOTE]
> The ability to deploy or debug may be affected, if you have not installed and set the recommended JDK as default on your system.

### Install OpenJDK for Ubuntu

This section explains how to install the OpenJDK version 12 for Ubuntu:

1. Launch the **Terminal** application.

2. Run the following command in the terminal to set the `JAVA_HOME` as OpenJDK directory path, for example:
    ```
    JAVA_HOME=/home/<username>/Desktop/openJDK/jdk-12.0.2/
    ```

3. Run the following commands in the terminal:
    ```
    sudo update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java 20000
    sudo update-alternatives --install /usr/bin/javac javac ${JAVA_HOME}/bin/javac 20000
    ```

4. Run the following command to get a list of JDK versions installed:
    ```
    sudo update-alternatives --config java
    ```
    > [!NOTE]
    > If multiple versions of JDK are installed, select the required Java version by entering the selection number.

5. Run the following command:
    ```
    sudo update-alternatives --config javac
    ```
    > [!NOTE]
    > `javac` is for compilation. For more information on differences between java and javac, see https://docs.oracle.com.

4. Select the required `javac` version as mentioned in step 5.

6. Run the following command to verify whether the OpenJDK version 12 is installed:
    ```
    java -version
    ```

### Install OpenJDK for macOS

This section explains how to install the OpenJDK version 12 for macOS:

1. Copy the downloaded jdk folder to the `Library/Java/JavaVirtualMachines` location. This is the default location where all the JDKs are available. Use the following command to copy the JDK directory.
    ```
    cp -aR <downloaded_jdk_path> /Library/Java/JavaVirtualMachines/
    ```

2. Launch **Terminal** application.

3. Run the following command to verify whether the OpenJDK version 12 is installed:
    ```
    java -version
    ```

    > [!NOTE]
    > If the OpenJDK version 12 is not installed, add the `export JAVA_HOME = /Library/Java/JavaVirtualMachines/jdk-12.jdk/Contents/Home` command in the `.profile` or `.bash_profile` file.


## Install OpenJFX

After installing OpenJDK, install the OpenJFX:

1. Download the OpenJFX version 11 from [https://gluonhq.com/products/javafx](https://gluonhq.com/products/javafx/).
    
    > [!NOTE]
    > Download the appropriate JavaFX product for your operating system.

2. Extract the downloaded zip file.

3. Copy all files in `lib` folder to `lib` folder of `JAVA_HOME`.
   
   > [!NOTE]
   > On Ubuntu, run the following command:
   > ```
   > cd javafx-sdk-11.0.1
   > sudo cp -arf lib/* ${JAVA_HOME}/lib/
   > ```

4. Copy all files in `bin` folder to `bin` folder of `JAVA_HOME`.
   > [!NOTE]
   >
   > This step is only required for Windows.

