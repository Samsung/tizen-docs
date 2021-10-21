# Visual Studio Code Extension for Tizen Web

The VS code extension installation can be done in two different ways. Refer to [VS code extension installation](dotnet.md) section for details. 

## Develop application

The following sections explain how to use Visual Studio Code Extension for Tizen to develop your applications.

### Create Tizen Web project

To create a Tizen Web project:

1. Create a new directory as the root directory for your project.

2. In Visual Studio Code, open the project directory you created.

   ![Open directory](media/web_directory.PNG)

3. In the pop up window, select **Trust folder and enable all features** button.

   ![Trust folder](media/web_trust.PNG)

4. Open the **Command Palette** and select **Tizen: Create Tizen project**.

   ![Create project](media/web_project_create.PNG)

5.	Select the project type as **Web**.

   ![Select project](media/web_project_type.PNG)

6.	Select the required profile for your application development.

   ![Select profile](media/web_project_profile.PNG)

7. Select the profile version for your application.

   ![Select version](media/web_profile_version.PNG)

8.	Select the required project template for your application from template list.

   ![Select template](media/web_project_template.PNG)

9.	Enter the project name.

   ![project name](media/web_project_name.PNG)


### Building your project

1.	Open the **Command Palette** and enter build. Select **Tizen: Build Tizen project**.

   ![Build project](media/web_build.PNG)

2.	Review the build results in the output window, and check the location of the package file (.tpk).

   ![Review result](media/web_build_review.PNG)

### Deploy and run your application in emulator

1.	To launch the Tizen Emulator Manager, open the **Command Palette** and enter emulator. Select **Tizen: Launch Tizen Emulator Manager**.

   ![Launch emulator](media/web_deploy.PNG)

2.	Create and launch an emulator instance in the Emulator Manager.

3.	To deploy your application to the target, enter install Tizen in the **Command Palette** and select **Tizen: Install Tizen application**.

   ![Install application](media/web_install_app.PNG)

4.	To run the application on the emulator, enter run in the **Command Palette** and select **Tizen: Run Tizen application**.

   ![Run application](media/web_run_app1.PNG)

   ![application](media/web_run_app2.PNG)

### Debug your application in emulator

1.	Deploy and run your application in the emulator.

2.	In the command palette, type run debug and then select **Tizen: Debug Tizen application**.

   [!NOTE] If the chrome path is not available in the default location, you need to enter the chrome path before debugging process begins.
   
   ![Debugger](media/web_debug.PNG)

3.	Add a break point in your source code.
   
   ![Break point](media/web_add_breakpoint.PNG)

### Debug your application in web simulator

1. In VS Code, click **View &gt; Command Palette**.

2.	In the input field of the Command Palette that appears type simulator, then select **Tizen Web: Run Web Simulator**.
   
   ![Web simulator](media/web_debug_simulator1.PNG)
      
   ![Web simulator](media/web_debug_simulator2.PNG)
