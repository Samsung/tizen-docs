# Hybrid application development

The VS code extension installation can be done in two different ways. Refer to [VS code extension installation](dotnet.md) section for details. 

## Develop Hybrid application

The following sections explain how to use Visual Studio Code Extension for Tizen to develop your hybrid applications.

### Create Tizen Native project

To create a Tizen Native project: Refer to [Create Tizen Native project](native.md)

### Create Tizen Dotnet project

1. Open the **Command Palette** and select **Tizen: Create Tizen project**.

   ![Create project](media/dotnet_project_create.png)

2. Select the project type as **Dotnet**.

   ![Select project](media/dotnet_project_select.png)

3. Select the required profile for your application development.

   ![Select profile](media/dotnet_profile.png)

4. Select the profile version for your application.

   ![Select version](media/dotnet_profile_version.png)

5. Select the required project template(eg:TizenNUIapp) for your application from template list.

   ![Select template](media/dotnet_project_template.png)

6. Enter the project name.

   ![project name](media/dotnet_project_name.png)

7. If prompts for setting current project as working folder, select Yes or No.

   ![project name](media/dotnet_project_working_folder.png)

### Select Working Folder 

1. Open the **Command Palette** and select **Tizen: Set Tizen Working Folder**.

   ![Set working folder](media/set_working_folder.png)

2. Select the working folder of Tizen.

   ![Select working folder](media/select_working_folder_project.png)

3. Selected working folder will be updated in workspace.yaml file.

   ![Selected working folder](media/selected_working_folder_workspace_yaml.png)

Selected working folder will be considered as **main app**.

### Update Dependency projects

1. From vscode File explorer Right click on **main app** and select **Tizen:Update Dependency Projects**.

   ![Set dependency projects](media/select_update_dependency_project.png)

2. Quick pick list with project list for selection will be displayed.

   ![Display depencency project list](media/select_dependency_project.png)

3. Select the dependency projects and press OK button.

   ![Select dependency project](media/selected_dependency_project.png)

4. Selected dependencies will be updated in workspace.yaml file

   ![Selected dependencies projects](media/selected_dependency_workspace_yaml.png)

The Hybrid app is successfully created with selected working folder as main app, and selected dependency projects to main app as sub apps.


### Build your project

1. Open the **Command Palette** and enter build. Select **Tizen: Build Tizen project**.

   ![Build project](media/hybrid_project_build.png)

2. Review the build results in the output window, and check the location of the package file (.tpk).

   ![Review result](media/hybrid_build_result.png)

### Deploy and run your application in emulator

1. To launch the Tizen Emulator Manager, open the **Command Palette** and enter emulator. Select **Tizen: Launch Tizen Emulator Manager**.

   ![Launch emulator](media/hybrid_deploy.png)

2. Create and launch an emulator instance in the Emulator Manager.

3. To deploy your application to the target, enter install Tizen in the **Command Palette** and select **Tizen: Install Tizen application**.

   ![Install application](media/hybrid_install_application.png)

   ![Install application](media/hybrid_install_result.png)

4. To run the application on the emulator, enter run in the **Command Palette** and select **Tizen: Run Tizen application**.

   ![Run application](media/hybrid_run_application.png)

   ![application](media/hybrid_run_result.png)

### Debug your application in emulator

1. Deploy and run your application in the emulator.

2. In the Visual Studio Code Activity Bar, select the **Debug** icon.

3. In the Debug view, open the Configuration drop-down menu and select **Add Configuration** or select **Create a Launch.json file**.

4. Select **GDB for Tizen Native** in the list of configurations.

   ![Debugger](media/hybrid_debug.png)

5. Add a break point in your source code.

   ![Break point](media/hybrid_add_breakpoint.png)

6. Start the debugging session by pressing **F5**.

   ![Start debug](media/hybrid_select_start_debug.png)

   ![Start debug](media/hybrid_start_debug.png)

To debug dotnet application, set dotnet app as main app, set native app as dependency app to dotnet app. Refer to [Debug your application in emulator](../../dotnet/get-started/first-app.md#debug-your-application-in-emulator) section for details. 

### Remove dependency projects

- Already added dependency projects (sub apps) can be removed  from main app

1. From vscode File explorer Right click on **main app** and select **Tizen:Update Dependency Projects**.

   ![Selected dependencies projects](media/selected_dependency_workspace_yaml.png)

   ![remove dependency project](media/remove_update_dependency_project.png)

2. Quick pick list with project list for select/deselect  will be displayed.

   ![Display depencency project list](media/deselect_dependency_project.png)

3. DeSelect the dependency projects and press OK button.

   ![Deselect dependency project](media/deselected_dependency_project.png)

4. removed dependencies will be updated in workspace.yaml file

   ![Removed dependencies projects](media/removed_dependency_workspace_yaml.png)

Deselected projects will be removed from dependency project list from main app.

## Import Tizen project

### Import Tizen workspace folder

1. Open the **Command Palette** and select **Tizen: Import Tizen project**.

   ![Import project](media/Tizen_import_project.png)

2. Select the required profile for your importing project.

   ![Select profile](media/Tizen_import_select_profile.png)

3. Select the profile version for your importing project.

   ![Select version](media/Tizen_import_select_profile_version.png)

4. Select the import type as Workspace folder.

   ![Select type](media/Tizen_import_select_workspace_folder.png)

5. Select the workspace folder which needed to be imported.

   ![Select folder](media/Tizen_import_selected_workspace_folder.png)

6. On private rootstrap selection prompt, select NO if private rootstrap is not required.

   ![Select rootstrap](media/Tizen_import_select_private_rootstrap_no.png)

7. Import settings will be applied in selected workspace folder and vscode reloads the selected workspace folder.

   ![Select folder](media/Tizen_import_selected_workspace_folder_reloaded.png)


### Import Tizen wgt file (Tizen Web application package file)

- Importing Tizen wgt file will import the wgt file to current workspace folder after deleting the current workspace contents.

To import wgt file to some other workspace:

Before importing wgt file, Select the workspace folder (empty folder) in which the wgt file is to be imported using open folder from File->Open Folder.

1. Open the **Command Palette** and select **Tizen: Import Tizen project**.

   ![Import project](media/Tizen_import_project_wgt.png)

2. Select the required profile for your importing project.

   ![Select profile](media/Tizen_import_select_profile_wgt.png)

3. Select the profile version for your importing project.

   ![Select version](media/Tizen_import_select_profile_version_wgt.png)

4. Select the import type as WGT.

   ![Select type](media/Tizen_import_select_wgt.png)

5. Select the wgt file which needed to be imported to current workspace.

   ![Select wgt](media/Tizen_import_selected_wgtfile.png)

6. On private rootstrap selection prompt Select No if private rootstrap is not required.

   ![Select rootstrap](media/Tizen_import_select_private_rootstrap_no_wgt.png)

7. Current workspace folder will be updated with imported wgt file.

   ![Select folder](media/Tizen_import_finish_wgt.png)
