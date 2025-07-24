# Test Profile App ASAN/LSAN

## Detect Runtime Memory Leaks with Leak Sanitizer

> [!NOTE]
>
> Before you run the Leak Sanitizer, follow the steps below:
    > - Make sure that you have an Emulator or a connected target device running
    > -	If you want to try out the tool and do not have an applicable project to test, create a test project with the **Project Wizard** using a template or a sample. For more information on creating a project, see [Create Tizen Native Application](../Tizen/native.md)

To use the Leak Sanitizer, follow the steps below:
1. In the Project Explorer view, select **Tools >  Tizen > Profiler > Profile With Leak Sanitizer**. 
  
    The profiler links your program to a runtime library containing the bare necessities required for Leak Sanitizer to work, this is done by setting the option `-fsanitize` to `leak`, and no compile-time instrumentation is applied here. Whilst the option is set, the application launches on the connected target device or the Emulator to detect any runtime memory leaks. As illustrated in the following figure:

    <img src="./media/LSan Menu.png" alt="Leak Sanitizer Menu" width="880"/>

2. After the application launches, run the application scenario that you want to test. Unlike the Address Sanitizer, Visual Studio Code checks and shows the profiling result when you exit the application. As illustrated in the following figure:
  
   <img src="./media/Lsan Stop profiling.PNG" alt="Leak Sanitizer Stop" width="880"/>

   After clicking the **Stop Profiling** button, VS Code will collect and show the profiling report. As illustrated in the following figure:
  
   <img src="./media/LSan report.PNG" alt="Leak Sanitizer Report" width="880"/>


## Detect Runtime Memory Errors with Address Sanitizer
> [!NOTE]  
> Before you run the Address Sanitizer, follow the steps below:
> - Make sure that you have an Emulator or a connected target device running
> - If you want to try out the tool but do not have an applicable project to test, create a test project with the **Project Wizard** using a template or a sample. For more information on creating a project, see [Create Tizen Native Application](../Tizen/native.md)


To use the Address Sanitizer, follow the steps below:
1.	In the Project Explorer view, select **Tools > Tizen > Profiler > Profile With Address Sanitizer**. 

    The profiling instruments the code and compiles the project for the Address Sanitizer. Finally, it launches the application on the connected target or Emulator. As illustrated in the following figure:
      
      <img src="./media/Asan Menu.png" alt="ASAN" width="980"/>

2.	If there is any memory error, Visual Studio Code shows the profiling result as illustrated in the following figure:

    In the example shown in the figure, the application crashes as soon as it is launched because the memory corruption happens in the `main()` function.

      <img src="./media/Asan Tz9.PNG" alt="ASAN" width="980"/>
      
