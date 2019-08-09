## Frequently Asked Questions 

This page contains answers to most commonly asked questions or errors that you may encounter while installing Tizen studio and developing apps in Tizen Studio.


- **How to run Tizen Studio on Ubuntu 18.04?**

  Tizen studio supports Ubuntu 18.04. However, Ubuntu 18.04 distribution does not include the runtime libraray **libpng12-0**. To experience optimal installation experience, install the runtime library and run the following command:
   ```
   $ wget http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb
   $ sudo dpkg -i libpng12-0_1.2.54-1ubuntu1_amd64.deb 
   ```
   
   Generally, installing packages from older distributions may break apt installation system. Since its dependencies are also present in Ubuntu-18.04, it will not break apt installation system.

- **How to manage certificates and package applications in different Ubuntu setups?**

    In Linux operating systems, Tizen Certificate Manager in Tizen Studio stores the passwords of the certificates in the **gnome-keyring** application. Therefore, you must enable the gnome-keyring application to ensure that Tizen Studio functions flawlessly.

    The remote login in a Linux desktop system does not have the **DBUS_SESSION_BUS_ADDRESS** variable set in the session. 
    To store and lookup passwords in the host's Login keyring, you must set the **DBUS_SESSION_BUS_ADDRESS** variable.
    For more information, see Manage certificates through [remote login, headless Linux sytems, and Docker containers](https://developer.tizen.org/community/tip-tech/how-manage-certificates-and-package-applications-different-ubuntu-setups).

- **What to do when Tizen Studio fails to launch?**

  Tizen Studio fails to launch if you have incorrect JDK version installed on your system. Ensure that you have recommended version of JDK, OpenJDK installed. 

  Check your JDK version and download an appropriate version.

   Verify you are using a supported version  JDK 8 or OpenJDK 10.  

   1. On your terminal or console window,  type `java -version`.
      If this command does not show which version is installed, see [How can I find which version of Java is installed without running an applet in Windows or Mac](https://www.java.com/en/download/help/version_manual.xml).
   2. Verify whether the available version is JDK 8 and OpenJDK 10.
   3. Set or update your JAVA_HOME environment variable. For more information, see the installation pages.

   To download an earlier version of the JDK, see [Oracle Java Archive](https://www.oracle.com/technetwork/java/archive-139210.html).

- **How to do form validation using Tizen Web?**

  Form validation normally occurs at the server end after the client enters all necessary data. The user clicks **Submit** button to send the data to the server. 
  If the data entered by a client is incorrect or the data is missing, the server responds back and user needs to resubmit the form with corrrect information. 
  This process  server was an overhead on the server and time elaped was on higher side, For more information, see [simple form validation in Tizen Web app](https://developer.tizen.org/community/tip-tech/form-validation-using-tizen-web).

- **How to implement vibration API in Tizen Web app?**

   To provide tactile feedback to the user or to interact with user even when the device volume is low, vibration provides a better user experience and improves the perception of application. When it comes to the Tizen app development, external third party library is not required to implement vibration feature, as you can use the internal Tizen API, for more information, see [Vibration API](https://developer.tizen.org/community/tip-tech/vibration-api-tizen-web-app).

- **How to troubleshoot compatibility with previous versions of Tizen Studio?**

  The Following are the various conditions that can cause compatibility issues:
   - You are using an older workspace in the installed version of Tizen Studio.
  - The Tizen Web, Tizen Native and Tizen Native UI Builder perspectives are used.
  - The Tizen Native or Tizen Native Builder perspective was used previously.
  - After installing the latest Tizen Studio using the installer without installing other tools using package manager.

   For more information, see [troubleshooting for compatibility](https://developer.tizen.org/community/tip-tech/trouble-shooting-compatibility-previous-versions-tizen-studio).

