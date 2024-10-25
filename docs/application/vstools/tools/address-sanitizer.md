# Detecting Runtime Memory Errors with Address Sanitizer

The Address Sanitizer is a profiling tool used to detect runtime memory errors in Tizen Native Applications. With this, you can discover whether specific parts of the code can potentially cause memory corruption at runtime. You can also avoid crashes or bugs during the execution of the application. The Address Sanitizer tool detects memory corruption at runtime by instrumenting the code during the application compilation. A program with no bugs does not crash when the Address Sanitizer tool is used, suggesting that the code is safe from potential memory corruption.

The Address Sanitizer tool can detect the following types of bugs:
*	Out-of-bounds accesses to heap and stack
*	Use-after-free
*	Use-after-return (to some extent)
*	Double free and invalid free


## To use the Address Sanitizer
> [!NOTE]  
> Before you run the Address Sanitizer, follow the steps below:
> - Make sure that you have an Emulator or a connected target device running
> - If you want to try out the tool but do not have an applicable project to test, create a test project with the **Project Wizard** using a template or a sample. For more information on creating a project, see [Create Tizen Native Application](https://docs.tizen.org/application/vstools/Tizen/native)


To use the Address Sanitizer, follow the steps below:
1.	In the Project Explorer view, select **Tools > Tizen > Profiler > Profile With Address Sanitizer**. 

    The profiling instruments the code and compiles the project for the Address Sanitizer. Finally, it launches the application on the connected target or Emulator. As illustrated in the following figure:
      
      <img src="./media/Asan Menu.png" alt="ASAN" width="980"/>

2.	If there is any memory error, Visual Studio Code shows the profiling result as illustrated in the following figure:

    In the example shown in the figure, the application crashes as soon as it is launched because the memory corruption happens in the `main()` function.

      <img src="./media/Asan Tz9.PNG" alt="ASAN" width="980"/>
      
