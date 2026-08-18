# .NET application development

## Develop application

The following sections explain how to use Visual Studio for Tizen to develop your applications.

## Create a project

1. Open Visual Studio.
2. Select **File > New > Project**.

   ![Create new project](/docs/application/vstools/media/vs2022_project_create_1.png)

3. In **Create a new project**, filter by **C#** and **Tizen**, select **Tizen DotNet Project**, and select **Next**.

   ![Select the Tizen .NET project template](/docs/application/vstools/media/vs2022_project_create_2_dotnet.png)

4. Enter the project name, location, and solution name, then select **Create**.

   ![Configure the Tizen .NET project](/docs/application/vstools/media/vs2022_project_create_3_dotnet.png)

5. In the Tizen Project Wizard, select the profile, platform version, and template, then select **OK**.

   ![Select the Tizen project profile](/docs/application/vstools/media/vs2022_project_create_4_dotnet.png)

6. After you click OK, the project gets created. Before doing anything, please wait while the required development packages are installed.

    ![Required development package installation](/docs/application/vstools/media/dotnet_dev_pkg_install.png)

The Solution Explorer displays the newly created Tizen .NET project.

![New Tizen .NET project](/docs/application/vstools/media/vs2022_project_create_5_dotnet.png)

## Build the application

Before building, register a signing certificate if required. See [Certificate Manager](../../tools/certificate-manager.md).

You can build the application in either of the following ways:

1. Select **Build > Build Solution**.

   ![Build solution](/docs/application/vstools/media/vs2022_build_1_dotnet.png)

2. In **Solution Explorer**, right-click the solution and select **Build**.

   ![Build from Solution Explorer](/docs/application/vstools/media/vs2022_build_2_dotnet.png)

### Troubleshoot build problems

1. **Tizen is not found during the build**

   If the build reports that Tizen cannot be found, complete these steps:

   ![Tizen not found build error](/docs/application/vstools/media/build_tizen_not_found.png)

   1. Verify that the required visual studio workloads are installed. See [Prerequisites](../prequisite.md).
   2. In Visual Studio, select **Tools > Options > Tizen > Tools**, then select **Update Tizen Workload** which will update the tizen workload.

      ![Update Tizen Workload](/docs/application/vstools/media/build_tizen_not_found_solve.png)

## Deploy and run the application

1. Launch Emulator Manager from the **Launch Tizen Emulator** button on the Visual Studio toolbar, or select **Tools > Tizen > Tizen Emulator Manager**.

   ![Launch Emulator Manager](/docs/application/vstools/media/vs2022_run_1_dotnet.png)

2. Select an emulator whose Tizen platform version matches or exceeds the application platform version, then select **Launch**.

   ![Select and launch an emulator](/docs/application/vstools/media/emulator_manager_launch_highlighted.png)

3. Wait for the emulator to boot, then select it in the Visual Studio run/debug target list.

   ![Emulator window](/docs/application/vstools/media/vs2022_run_4_emulator.png)

4. Select the green **Start Debugging** button to debug, or select **Debug > Start Without Debugging** to run without the debugger.

   ![Deploy and run the application](/docs/application/vstools/media/vs2022_run_5_dotnet.png)

5. Verify the application in the emulator.

   ![Tizen .NET application running in the emulator](/docs/application/vstools/media/vs2022_run_6_dotnet.png)

## Debug the application

1. Open the `.cs` source file that you want to debug.
2. Click the left margin next to a line of code, or press **F9**, to add a breakpoint.

   ![Set a breakpoint](/docs/application/vstools/media/vs2022_debug_dotnet.png)

3. Select **Debug > Start Debugging**, select the green toolbar button, or press **F5**. When execution reaches a breakpoint, inspect variables and use the standard Visual Studio debugging controls.
