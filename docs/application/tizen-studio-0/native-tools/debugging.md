# Debugging Your Application

The Tizen Studio provides the following set of tools to help you debug your native application projects:

- [Log View](../common-tools/log-view.md) **(Checking Logs with Log View)**  
The **Log** view allows you to check the logs of your application based on the logging methods you have inserted to your code. It helps to debug your application by capturing all the events logged by the platform and your application.

- [Dynamic Analyzer](../common-tools/dynamic-analyzer/overview.md) **(Monitoring Performance with Dynamic Analyzer)**  
The Dynamic Analyzer tool monitors the performance of your application on a target device or emulator. It analyzes your application for potential performance issues, such as high usage of CPU, memory, file or network operations.

- [Call Stack View](call-stack-view.md) **(Getting Crash Data from Call Stack View)**  
The **Call Stack** view provides useful information for debugging the application when the application crashes while running. It provides generic information about the crashed application, traces where the memory block has crashed, and shows the latest debug messages.

- [Static Analyzer](static-analyzer.md) **(Analyzing the Source Code)**  
The Static Analyzer tool is used for source code analysis to finds issues in Tizen applications. It can be helpful in detecting a variety of issues in the code during compilation, well before the application deployment. The tool uses clang static analyzer to analyze C/C++ code.

- [Valgrind](valgrind.md) **(Profiling Memory with Valgrind)**  
The Valgrind tools is used for performance profiling. It detects memory errors and memory leaks in an application.

- [T-trace](t-trace.md) **(Optimizing Performance with T-trace)**  
The T-trace tool allows you to detect and analyze performance issues by measuring and visualizing instrumented function calls in the Tizen platform. It helps you to understand what the system is doing while your application is running.

- [Address Sanitizer](address-sanitizer.md) **(Detecting Runtime Memory Errors with Address Sanitizer)**  
The Address Sanitizer tool is used to discover runtime memory errors. It helps you to prevent application crashes and bugs.

- [Code Coverage](code-coverage.md) **(Getting Code Execution Information with Code Coverage)**  
The Code Coverage tool gives information about the parts of code that are executed during a particular scenario. It helps you to detect uncovered code parts which must be further studied to ensure that they do not cause errors.

## Related Information
* Dependencies
  - Tizen Studio 1.0 and Higher
