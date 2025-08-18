# Tizen Development Activity and Native Application Tools

"Visual Studio for Tizen" provides comprehensive development tools to help you through the overall native development process phases and you can perform all the development activities from the application project creation to testing.

## Managing Projects
<!-- 
  - createing project
  - app sigining (\w certificate manager)
-->
 You can create new application projects in the Visual Studio menu, select **File > New > Project**, and manage the existing applications in the **Solution Explorer** view in Visual Studiofor Tizen. You can also simply manage necessary toolchain and target architecture for your native application project, and register certificates for your applications to allow them to be published in the application stores.

## Editing Code & Building Your Application
You can use the content assist and API and Privilege Checker tools to speed up the code writing and verification task. The API Privilege Checker tool helps developers identify and resolve previlege-related issues in Tizen applications by analyzing API usage and ensuring complicance with security requirements. It provides detailed reports and suggestions to enhance application security and functionality.
<!-- 
  - content assist
  - api & privilege checker
-->

<!-- ## Configuring Your Application 
 - manifest editor
 - resource manager (po editor)
-->

## Debugging and Profiling Your Application
<!-- 
 - Debug Application
 - ASAN / LSAN
-->
You can debug your application using the built-in debugger in Visual Studio for Tizen. You can set breakpoints, inspect variables, and step through your code to identify and fix issues. ASAN (Address Sanitizer) and LSAN(Leak Sanitizer) are two tools that can help you find memory-related issues in your application. They can detect memory leaks, buffer overflows, and other memory-related problems that could cause crashes or security vulnerabilities in your application.
These tools provide detailed information about the application's behavior and help you optimize its performance.

## Running and Testing Your Application
<!-- 
- emulator
- sdb
- device manager
- Native Unit Test Application
-->
You can run and test your application on an emulator or a real device. You can also use the SDB tool to connect to a device and transfer files between the device and your computer. Additionally, you can use the Device Manager tool to manage connected devices and their settings. Finally, you can create a Native Unit Test Application to test the functionality of your application's code. This allows you to ensure that your application works correctly and meets the required specifications.

<!-- ## Command Line Interface
- CLI
-->
If you prefer a command line interface (CLI) instead of using Visual Studio for Tizen, you can use the Tizen CLI tool. The Tizen CLI tool is a command-line tool that allows you to create, build, test, and package Tizen native applications without using Visual Studio for Tizen. It provides similar functionalities as Visual Studio for Tizen, but through a command-line interface.

<!-- ## Advanced Topics
- Hybrid Application Development
- RPK Application Development
- Tizen Command Palette commands
-->
You also refer to the advanced topics section to learn more about hybrid application development, RPK application development, and other advanced features provided by Visual Studio for Tizen. These topics cover more specialized scenarios and provide additional tools and techniques for developing Tizen applications.