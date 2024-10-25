# Detect Runtime Memory Leaks with Leak Sanitizer

The Leak Sanitizer is a profiling tool used to detect runtime memory leaks in Tizen Native Applications. The Leak Sanitizer lets you discover whether specific parts of the code can potentially cause memory leaks at runtime. You can also avoid leaks in memory after application execution. The Leak Sanitizer tool detects memory leaks at runtime by instrumenting the code during the application compilation. A program with no bugs does not crash when the Leak Sanitizer tool is used, suggesting that the code is safe from potential memory leaks.

## To use the Leak Sanitizer

> [!NOTE]: 
>
> Before you run the Leak Sanitizer, follow the steps below:
	> - Make sure that you have an Emulator or a connected target device running
	> -	If you want to try out the tool and do not have an applicable project to test, create a test project with the **Project Wizard** using a template or a sample. For more information on creating a project, see [Create Tizen Native Application](../Tizen/native)

To use the Leak Sanitizer, follow the steps below:
1. In the Project Explorer view, select **Tools >  Tizen > Profiler > Profile With Leak Sanitizer**. 
  
    The profiler links your program to a runtime library containing the bare necessities required for Leak Sanitizer to work, this is done by setting the option `-fsanitize` to `leak`, and no compile-time instrumentation is applied here. Whilst the option is set, the application launches on the connected target device or the Emulator to detect any runtime memory leaks. As illustrated in the following figure:

	<img src="./media/LSan Menu.png" alt="Leak Sanitizer Menu" width="880"/>

2. After the application launches, run the application scenario that you want to test. Unlike the Address Sanitizer, Visual Studio Code checks and shows the profiling result when you exit the application. As illustrated in the following figure:
  
   <img src="./media/Lsan Stop profiling.PNG" alt="Leak Sanitizer Stop" width="880"/>

   After clicking the **Stop Profiling** button, VS Code will collect and show the profiling report. As illustrated in the following figure:
  
   <img src="./media/LSan report.PNG" alt="Leak Sanitizer Report" width="880"/>

