# Web Application Development


## Develop application

The following sections explain how to use Visual Studio Tools for Tizen to create, build, run, and debug a Web application.

### Create a Tizen Web project

1. Open Visual Studio. Select **File > New > Project**.

   ![Create a new project](media/vs2022_project_create_1.png)

2. In **Create a new project**, select **JavaScript** and **Tizen**, choose **Tizen Web Project**, and select **Next**.

   ![Select the Tizen Web project template](media/vs2022_project_create_2_web.png)

3. Enter the project name, location, and solution name, then select **Create**.

   ![Configure the Web project](media/vs2022_project_create_3_web.png)

4. In the **Tizen Project Wizard**, select the required profile, platform version, and template, then select **OK**.

   ![Select the Web project profile, platform version, and template](media/vs2022_project_create_4_web.png)

5. Verify that the new project appears in Solution Explorer.

   ![New Web project in Solution Explorer](media/vs2022_project_create_5_web.png)

6. Wait for the required development packages to finish installing before continuing.

   ![Required development package installation](media/web_dev_pkg_install.png)

### Build your project

Build the project in either of the following ways:

1. Select **Build > Build Solution**.

   ![Build the solution from the Visual Studio menu](media/vs2022_build_1_web.png)

2. Or, in Solution Explorer, right-click the solution and select **Build**.

   ![Build the solution from Solution Explorer](media/vs2022_build_2_web.png)

### Deploy and run your application

1. Open Emulator Manager from the **Launch Tizen Emulator** button on the Visual Studio toolbar. Alternatively, select **Tools > Tizen > Tizen Emulator Manager**.

   ![Launch Emulator Manager from the toolbar](media/vs2022_run_1_web.png)

   ![Launch Emulator Manager from the Tools menu](media/vs2022_run_2_web.png)

2. Select an emulator whose platform version matches or is later than the application platform version, then select **Launch**.

   ![Select and launch an emulator](media/emulator_manager_launch_highlighted.png)

3. Wait for the emulator to boot, then select it as the run target in Visual Studio. Select the green **Start** button to debug, or select **Debug > Start Without Debugging** to run without debugging.

   ![Running emulator](media/vs2022_run_4_emulator.png)

   ![Deploy and run the Web application](media/vs2022_run_5_web.png)

4. Verify that the application is running in the normal Tizen emulator.

   ![Web application running in the emulator](media/vs2022_run_6_web.png)

### Debug your application in Chrome

1. Start debugging by selecting **Debug > Start Debugging**, selecting the **Debug** button, or pressing **F5**.

   > [!NOTE]
   > If Chrome is not installed in its default location, set the Chrome path before starting the debugging session.

2. Open a `.js` source file in Chrome and set a breakpoint.

   ![Add a breakpoint](media/web_debug_application.PNG)
