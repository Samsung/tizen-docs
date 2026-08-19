# Native application development


## Develop application

The following sections explain how to use Visual Studio Tools for Tizen to create, build, run, and debug a Native application.

### Create a Tizen Native project

1. Open Visual Studio. Select **File > New > Project**.

   ![Create a new project](media/vs2022_project_create_1.png)

2. In **Create a new project**, select **C++** and **Tizen**, choose **Tizen Native Project**, and select **Next**.

   ![Select the Tizen Native project template](media/vs2022_project_create_2_native.png)

3. Enter the project name, location, and solution name, then select **Create**.

   ![Configure the Native project](media/vs2022_project_create_3_native.png)

4. In the **Tizen Project Wizard**, select the required profile, platform version, and template, then select **OK**.

   ![Select the Native project profile, platform version, and template](media/vs2022_project_create_4_native.png)

5. Verify that the new project appears in Solution Explorer.

   ![New Native project in Solution Explorer](media/vs2022_project_create_5_native.png)

6. Wait for the required development packages to finish installing before continuing.

   ![Required development package installation](media/native_dev_pkg_install.png)

### Build your project

Build the project in either of the following ways:

1. Select **Build > Build Solution**.

   ![Build the solution from the Visual Studio menu](media/vs2022_build_1_native.png)

2. Or, in Solution Explorer, right-click the solution and select **Build**.

   ![Build the solution from Solution Explorer](media/vs2022_build_2_native.png)

#### Troubleshoot build problems

1. **Tizen is not found during the build**

   If the build reports that Tizen cannot be found, complete these steps:

   ![Tizen not found build error](media/build_tizen_not_found.png)

   1. Verify that the required visual studio workloads are installed. See [Prerequisites](../prequisite.md).
   2. In Visual Studio, select **Tools > Options > Tizen > Tools**, then select **Update Tizen Workload** which will update the tizen workload.

      ![Update Tizen Workload](media/build_tizen_not_found_solve.png)

2. **Clean Solution fails**

   Right-click the Native project in Solution Explorer and select **Properties > Configuration Properties > Advanced > Build Log File**. Clear the **Build Log File** field.

   ![Clear the build log file](media/properties_window.png)

### Deploy and run your application

1. Open Emulator Manager from the **Launch Tizen Emulator** button on the Visual Studio toolbar. Alternatively, select **Tools > Tizen > Tizen Emulator Manager**.

   ![Launch Emulator Manager from the toolbar](media/vs2022_run_1_native.png)

   ![Launch Emulator Manager from the Tools menu](media/vs2022_run_2_native.png)

2. Select an emulator whose platform version matches or is later than the application platform version, then select **Launch**.

   ![Select and launch an emulator](media/emulator_manager_launch_highlighted.png)

3. Wait for the emulator to boot, then select it as the run target in Visual Studio. Select the green **Start** button to debug, or select **Debug > Start Without Debugging** to run without debugging.

   ![Running emulator](media/vs2022_run_4_emulator.png)

   ![Deploy and run the Native application](media/vs2022_run_5_native.png)

4. Verify that the application is running in the normal Tizen emulator.

   ![Native application running in the emulator](media/vs2022_run_6_native.png)

### Debug your application in the emulator

1. Open a `.c` source file and set a breakpoint.

   ![Add a breakpoint](media/native_debug_application.PNG)

2. Start debugging by selecting **Debug > Start Debugging**, selecting the **Debug** button, or pressing **F5**.
