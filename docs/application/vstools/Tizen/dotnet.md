# .NET application development


## Develop application

The following sections explain how to use Visual Studio for Tizen to develop your applications.


### Create Tizen .Net project

To create a Tizen .Net project:

1. In the Visual Studio menu, select **File &gt; New &gt; Project**.

2. For creating .Net application, select **C#** and **Tizen** options in the dropdown list. Then, select the required template for your project and click **Next**.

    ![Create Tizen project](media/dotnet_create_project.png)

3. In the configure window, type the name for your project and click **Create**.

    ![Configure project](media/dotnet_configure_project.png)

4. In the **Tizen Project Wizard** window, select the platform version and click **OK**.

    ![Version selection](media/dotnet_platform_version.png)


### Building your project

1. To build your project, select **Build Solution** in the **Solution Explorer** window.

    ![Build project](media/dotnet_build_project.png)

2. To deploy and run your application, select **Debug &gt; Start without Debugging**.
    
    ![NOTE] Ensure the emulator is running in your system.

    ![Run application](media/dotnet_run_application1.png)

    ![Application](media/dotnet_run_application2.png)


### Debug your application in emulator

1.	Open the .cs file in your visual studio application.

2.	Add a break point in your source code.

    [Add break point](media/dotnet_debug_application.png)

3.	Start the debugging session by selecting **Debug &gt; Start Debugging** in the menu bar, or pressing **F5**, or by clicking the **Debug** button in the menu bar.
