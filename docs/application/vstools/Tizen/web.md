# Web application development


## Develop application

The following sections explain how to use Visual Studio for Tizen to develop your applications.


### Create Tizen Web project

To create a Tizen web project:

1. In the Visual Studio menu, select **File &gt; New &gt; Project**.

2. For creating web application, select **JavaScript** and **Tizen** options in the dropdown list. Then, select **Tizen Web project** and click **Next**.

   ![Create Tizen project](media/web_create_project.PNG)

3. In the configure window, type the name for your project and click **Create**.

   ![Configure project](media/web_configure_project.PNG)

4. In the **Tizen Profile Select** window, select the required profile, platform version, and template for your project, then click **OK**.

   ![Version selection](media/web_version_selection.PNG)

5. The visual studio window with newly created project appears on the screen.

   ![Visual Studio screen](media/web_vs_screen.PNG)


### Build your project

1. To build your project, select **Build Solution** in the **Solution Explorer** window.

   ![Build project](media/web_build_project.PNG)

2. To deploy and run your application, select **Debug &gt; Start without Debugging**.

   > [!NOTE]
   > Ensure the emulator is running in your system.

   ![Run application](media/web_run_application1.PNG)

   ![Application](media/web_run_application2.PNG)


### Debug your application in chrome

1. Start the debugging session by selecting **Debug &gt; Start Debugging** in the menu bar, or pressing **F5**, or by clicking the **Debug** button in the menu bar.

   > [!NOTE]
   > If the chrome path is not available in the default location, you need to enter the chrome path before debugging process begins.

2. Open .js file in the chrome and add a break point in your source code.

   ![Add break point](media/web_debug_application.PNG)


### Debug your application in web simulator

1. Open .js file in chrome and select **Run as Tizen Web Simulator Application** in the **Solution Explorer** window.

   ![Debug in simulator](media/web_debug_simulator1.PNG)

   ![Debug in simulator](media/web_debug_simulator2.PNG)
