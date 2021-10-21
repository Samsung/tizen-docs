# Native application development


## Develop application

The following sections explain how to use Visual Studio for Tizen to develop your applications.


### Create Tizen Native project

To create a Tizen Native project:

1. In the Visual Studio menu, select **File &gt; New &gt; Project**.

2. For creating Native application, select **C++** and **Tizen** options in the dropdown list. Then, select **Tizen Native project** and click **Next**.

    ![Create Tizen project](media/native_create_project.PNG)

3. In the configure window, type the name for your project and click **Create**.

    ![Configure project](media/native_configure_project.PNG)

4. In the **Tizen Profile Select** window, select the required profile, platform version, and template for your project, then click **OK**.

5. The visual studio window with newly created project appears on the screen.

    ![Visual Studio screen](media/native_vs_screen.PNG)


### Building your project

1. To build your project, select **Build Solution** in the **Solution Explorer** window.

    ![Build project](media/native_build_project.PNG)

2. To deploy and run your application, select **Debug &gt; Start without Debugging**.
    
    [!NOTE] Ensure the emulator is running in your system.

    ![Run application](media/native_run_application1.PNG)

    ![Application](media/native_run_application2.PNG)


### Debug your application in emulator

1. Open .c file in your visual studio application.

2.	Add a break point in your source code.

    ![Add break point](media/native_debug_application.PNG)

3.	Start the debugging session by selecting **Debug &gt; Start Debugging** in the menu bar, or pressing **F5**, or by clicking the **Debug** button in the menu bar.
    
