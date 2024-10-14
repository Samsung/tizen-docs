# Detecting Runtime Memory Errors with Leak Sanitizer
- The Leak Sanitizer is a profiling tool designed to identify runtime memory leaks in Tizen native applications. It helps developers pinpoint sections of code that may lead to memory leaks during execution. By instrumenting the code during application compilation, the tool can detect memory leaks at runtime. If the program runs without crashing under Leak Sanitizer, it indicates that the code is free from potential memory leaks. This ensures safer and more efficient memory management in Tizen applications.

## Using Leak Sanitizer
- In the **File Explorer view**, click on view and select **Command Palette > Tizen: Profile with Leak Sanitizer**.
  
  The profiling instruments the code and compiles the project for the Leak Sanitizer. Finally, it launches the application on the connected target or emulator, as illustrated in the following figure.
  
  ![Launch Command](media/launch_lsan.png)
  <br>

- After the application is launched, run the application scenario you want to test
- Visual studio code shows the profiling result after clicking on **Stop Profiling Button**.

  ![Stop Profile Button](media/stop_profiling_button.png)
   <br>
    
- Once clicked on the **Stop Profiling Button**, application will crash if there are any errors hence the report will be generated and if there are no memory errors it will give the message no error found, as illustrated in the following figure.

  ![Lsan UI Report](media/lsan_failure_report.png)

## Source File Navigation on Failure
  - When a failure occurs, you can click on the **line number associated with the failure which is generated in UI Report**. This action will open the corresponding source file in your editor and **navigate to the exact location where the failure has occurred**, as illustrated in the following figure.

 ![Failure occured](media/failure_line_lsan.png)