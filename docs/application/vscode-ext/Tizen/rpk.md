# RPK (Resource Package) Application Development

The VS Code extension installation can be done in two different ways. Refer to [VS Code extension installation](dotnet.md) for details. 

## Develop application

The following sections explain how to use Visual Studio Code Extension for Tizen to develop RPK applications.

### Create Tizen RPK project

To create a Tizen RPK project, follow these steps:

1. Create a new directory as the root directory for your project.

2. In Visual Studio Code, open the project directory you created.

   ![Open directory](media/rpk_directory.png)

3. In the pop up window, select the **Trust folder and enable all features** button.

   ![Trust folder](media/web_trust.PNG)

4. Open the **Command Palette** and select **Tizen: Create Tizen project**.

   ![Create project](media/rpk_project_create.png)

5. Select the project type as **Rpk**.

   ![Select project](media/rpk_project_type.png)

6. Select the required profile for your application development.

   ![Select profile](media/rpk_project_profile.png)

7. Select the profile version(mobile-7.0/mobile-6.5) for your application.

   ![Select version](media/rpk_project_version.png)

8. Select the required project template for your application from the template list.

   ![Select template](media/rpk_project_template.png)

9. Enter the project name.

   ![project name](media/rpk_project_name.png)


### Build your project

1. Open the **Command Palette** and enter Tizen build. Select **Tizen: Build Tizen project**.

   ![Build project](media/rpk_build.png)

2. Review the build results in the output window, and check the location of the package file (.rpk).

   ![Review result](media/rpk_build_result.png)

### Deploy and run your application in emulator

1. To launch the Tizen Emulator Manager, open the **Command Palette** and enter Tizen Emulator. Select **Tizen: Launch Tizen Emulator Manager**.

   ![Launch emulator](media/rpk_deploy.png)

2. Create and launch an emulator instance in the Emulator Manager.

3. To deploy your application to the target, enter Tizen Install in the **Command Palette** and select **Tizen: Install Tizen application**.

   ![Install application](media/rpk_install_app.png)

   ![Install application](media/rpk_install_app_result.png)

4. To run the application on the emulator, enter run in the **Command Palette** and select **Tizen: Run Tizen application**.

   ![Run application](media/rpk_run_app1.png)

   ![application](media/rpk_run_app2.png)

   > [!NOTE] 
   > An info popup will be displayed, showing the message "Resource project is Installed, but resource project cannot be launched by Run".

<!--
## Tizen workspace YAML validation

1. Create Tizen project using command **Tizen: Create Tizen project**.

2. Open the tizen_workspace.yaml file and append the character 'd' to type:hybrid. After that, a red line displays under the word 'hybridd' when the mouse is hovered on it. An error message will also be displayed.
  
   ![worksplace validation](media/rpk_tizen_workspace_yaml_open.png)

   ![worksplace validation](media/rpk_tizen_workspace_yaml_validation.png)


## Dotnet workload installation

1. Dotnet workload installation will be installed on VS Code activation OR by using the command **Tizen: Install Dotnet Workload**.

2. For Windows OS, Run VS Code as Administrator.

3. For Ubuntu/macOS, enter system password as the installation requires sudo permission. Or you can press Esc to skip installation.
  
   ![dotnet workload installation](media/dotnet_workload_install_password.png)

   ![dotnet workload installation](media/dotnet_workload_install_password_enter.png)
   
   ![dotnet workload installation](media/dotnet_workload_install_success.png)
   
   > [!NOTE] 
   > Dotnet workload installation requires .NET Core SDK (.NET6 or higher).
   > Download and install the latest version of .NET Core SDK from <https://www.microsoft.com/net/download/>

-->