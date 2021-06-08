# Create Your First Tizen Mobile .NET Application

The Tizen .NET framework allows you to easily and efficiently create applications for Tizen. Study the following instructions to help familiarize yourself with the Tizen .NET application development process. With the instructions, you can create and run a basic .NET application, which displays some text on the screen with no user interaction.

1.  Before you get started with developing Tizen applications, set up the [development environment](../../../vstools/install.md).

2. [Create a Project](#create-a-project)

    This step shows how you can use a predesigned project template that creates all the basic files and folders required for your project.

3. [Build Your Application](#build-your-application).

    After you have implemented code for the features you want, this step shows how you can build the application to validate and compile the code.

4. [Deploy and Run Your Application](#deploy-and-run-your-application).

    This step shows how you can deploy and run the application on the emulator or a real target device.

5. [Enhance Your Application](#enhance-your-application).

    This step shows how you can enhance your application by creating a UI and making small alterations to it to improve the usability of the application.

## Create a Project

The following example shows you how to create and configure a basic Tizen .NET application.

The following figure illustrates the output of application. The application screen displays a message, **Welcome to Tizen .NET Application!** and there is no user interaction.

![Application running on the mobile emulator](media/cs_first_building_emulator_mobile.png)

To create a new Tizen .NET project you can use 3 following tools: Visual Studio, Visual Studio Code with Tizen SDK extensions or CLI tools included in Tizen SDK.

<link href="../css/dotnet-samples.css" ref="stylesheet">

<div class="sampletab">
    <button class="tablinks" onclick="openProfile(event, 'Visual-Studio-2019')" id="defaultOpen">Visual Studio 2019</button> 
    <button class="tablinks" onclick="openProfile(event, 'Visual-Studio-Code')">Visual Studio Code</button> 
    <button class="tablinks" onclick="openProfile(event, 'CLI')">CLI</button>
</div>

<!-- Tab content -->
<div id="Visual-Studio-2019" class="tabcontent">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="267" src="media/m21sampleaccount2.png" width="150"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/Xamarin.Forms/Accounts" target="_blank"><strong>(M) SampleAccount</strong></a></p>
			<p>This sample application demonstrates how to implement an account provider, which adds and configures an account using <a href="/application/dotnet/api/TizenFX/latest/api/Tizen.Account.AccountManager.html" target="_blank">Tizen.Account.AccountManager</a>.</p>
			</td>
		</tr>
		<tr>
			<td><img alt="" height="267" src="media/m20samplesync.png" width="150"/></td>
			<td>
			<p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Mobile/Xamarin.Forms/SampleSync" target="_blank"><strong>(M) SampleSync</strong></a></p>
			<p>This sample application demonstrates how to manage data synchronization schedule between the target device and the server.</p>
			</td>
		</tr>
	</tbody>
</table>
</div>

<div id="Visual-Studio-Code" class="tabcontent">
<table>
	<tbody>
		<tr>
			<td><img alt="" height="180" src="media/waccounts.png" width="180"/></td>
			<td>
                        <p><a href="https://github.com/Samsung/Tizen-CSharp-Samples/tree/master/Wearable/Xamarin.Forms/Accounts" target="_blank"><strong>(W) Accounts</strong></a></p>
			<p>This sample application demonstrates how to implement an account provider, which adds and configures an account using <a href="/application/dotnet/api/TizenFX/latest/api/Tizen.Account.AccountManager.html" target="_blank">Tizen.Account.AccountManager</a>. It also demonstrates how to create circular UI using <a href="https://samsung.github.io/Tizen.CircularUI/api/index.html" target="_blank">Tizen.Wearable.CircularUI</a>.</p>
			</td>
		</tr>
		<tr>
	</tbody>
</table>
</div>

<div id="CLI" class="tabcontent">
<table>
	<tbody>
		<tr>
			<td>There is no sample.</td>
		</tr>
	</tbody>
</table>
</div>

### Create a Project Using Visual Studio 2019

1.  Launch Visual Studio 2019.

2. In the Visual Studio menu, select **File \> New \> Project**.

    ![Create a new project](media/cs_first_creating_menupath.png)

    A New Project window appears.

3. Select **C\#** in languages and **Tizen** in platforms, select **Blank App (Xamarin.Forms)** template, and then click **Next**.

    ![Select a template](media/cs_first_creating_new_project.png)

    Configure the project properties and click **Create**. You can enter the **Project name**, **Location**, **Solution**, and **Solution name**.

    ![Select a template](media/cs_first_creating_configure_project.png)

    The **Tizen Project Wizard** pop-up window appears.

4. Select the profile, **Mobile** and click **OK**.

    ![Tizen Project Wizard](media/cs_first_creating_project_wizard_mobile.png)

    If you select the **Common** profile, you cannot select **Mobile**, **TV**, or **Wearable**.

The following figure illustrates a solution with four projects created and displayed in the **Solution Explorer** view:

![Project with mobile, TV, and wearable profiles](media/vs_solution_explorer_mobile.png)

-   The **\<projectname\>** project contains the Xamarin.Forms code shared across platforms.
-   If you select the common profile in the Tizen Project Wizard, a common project titled **\<projectname\>.Tizen** is added. It contains code to instantiate your common application within the Tizen framework.
-   If you select the mobile profile in the Tizen Project Wizard, a mobile project titled **\<projectname\>.Tizen.Mobile** is added. It contains code to instantiate your mobile application within the Tizen framework.

If you are already familiar with Xamarin.Forms, this project has the same structure as a Xamarin.Forms portable application. The **\<projectname\>** project is the portable class library and the others are the platform-specific projects; however, in Tizen .NET, only the Tizen platform-specific project is generated.

The `.cs` file in the portable project already contains simple Xamarin.Forms code that makes a basic UI.

### Create a Project Using Visual Studio Code Tizen Extension
1. Use `ctrl + P` to open commands tool and type Tizen .NET 
2. Choose **Create a Tizen .NET Project**
3. Choose NUI Application template: **tizen-6.0 TizenNUIApp**

### Create a Project Uisng CLI
1. go to directory where project will be created
2. `tizen create cs-project -t Tizen.NUI.Template55.Single -v tizen-5.5 -n HelloWorld`

## Build Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, build the application. The building process performs a validation check and compiles your files. You must sign the application package with an author certificate when building the application. If you have not yet registered a Tizen certificate in Visual Studio, see [Certificate Manager](../../../vstools/tools/certificate-manager.md).


### Build using Visual Studio 2019
There are two different ways to build the application:

-   In the Visual Studio menu, select **Build \> Build Solution**.
-   In the **Solution Explorer** view, right-click the solution name and select **Build**.

### Build using Visual Studio Code
-   use `ctrl + P` to show command panel 
-   type Tizen .NET 
-   choose Tizen .NET: Build Tizen .NET project

### Build using CLI
-   go to project directory 
-   use `$ tizen build-cs command`

Tizen .NET applications are always deployed as installed packages. The package files have the `.tpk` file extension, and the process of generating a package is controlled by the [manifest file](../../../vstools/tools/manifest-editor.md). The Visual Studio template generates the manifest file (`tizen-manifest.xml`) to the top level of the \<projectname\>.Tizen project (if you create projects with mobile, TV, or wearable profiles, a separate manifest file is generated for each profile).

For this example application, the default manifest is sufficient. If you want to make any changes in the application, such as changing the application icon or installing resources that are used by the application at runtime, see [Package Your Application](#package-your-application).

After you have built the application, deploy and run it.

## Deploy and Run Your Application

To run the application, you must first deploy it to the target: either a device or an emulator. Deploying means transferring the package file (`.tpk`) to the target and invoking the Tizen Package Manager to install it.

To deploy and run the application on the emulator:

1.  In the Visual Studio menu, select **Tools \> Tizen \> Tizen Emulator Manager**.

    Alternatively, click **Launch Tizen Emulator** in the Visual Studio toolbar to launch the Tizen Emulator Manager.

    ![Launch Tizen Emulator](media/cs_launch_tizen_emu.png)

2. In the Emulator Manager, select an emulator from the list and click **Launch**.

    If no applicable emulator instance exists, [create one](../../../vstools/tools/emulator-manager.md#create).

    ![Tizen Emulator Manager](media/cs_first_building_emulator_manager_mobile.png)

3. Once you launch an emulator instance, you can deploy the application by clicking the emulator instance in the Visual Studio toolbar. Make the Mobile project **Set as StartUp Project**.

    ![Deploy your package](media/vs_emulator_launch_mobile.png)

    In the Visual Studio toolbar, you can select the target from the drop-down list to change the deployment target.

    ![Tizen Emulator Manager](media/vs_emulator_dropdown.png)

4. If deployment is successful, the application icon is visible on the emulator or device screen. Click the icon to launch the application.

    The following figure shows the launched application on the mobile emulator:

    ![Application running on the mobile
    emulator](media/cs_first_building_emulator_mobile.png)

Visual Studio uses the Smart Development Bridge (SDB) to communicate with the target device or emulator. If you encounter problems with detecting the device in Visual Studio, you can check the SDB manually:

1.  In the Visual Studio menu, select **Tools \> Tizen \> Tizen Sdb Command Prompt**.
2.  In the command prompt, enter `sdb devices`.

    ![Emulator detection](media/cs_first_building_sdb_prompt_mobile.png)

    A list of the attached devices appears.

If you face any issues during deployment, it is recommended to manually install the application using SDB:

-   Mobile application:

    ```bash
    $ sdb install <path-to-package>/org.tizen.example.CrossTemplate1.Tizen.Mobile-1.0.0.tpk
    ```

## Enhance Your Application

Tizen .NET provides a way to build portable applications which run in a native way. It provides a set of controls for building a user interface, as well as generates code which adapts the user interface code to use the native facilities of the supported platforms. The following is a brief introduction to the NUI controls, and how to use them to build on the application you have just created.

### Understand the Source Code

The C\# code from your first application displays and rotate a label centered on the screen, containing the **Hello Tizen NUI Wolrd** text. This application created from the template is set up and ready to be built and run right after you create it, as described above.

The following shows code generated by template project **HelloWorld.cs** file, generated by the template:

```csharp
using System;
using Tizen.NUI;
using Tizen.NUI.BaseComponents

namespace helloworld
{
    class Program : NUIApplication
    {
        protected override void OnCreate()
        {
            base.OnCreate();
            Initialize();
        }

        void Initialize()
        {
            Window.Instance.KeyEvent += OnKeyEvent;

            TextLabel text = new TextLabel("Hello Tizen NUI World");
            text.HorizontalAlignment = HorizontalAlignment.Center;
            text.VerticalAlignment = VerticalAlignment.Center;
            text.TextColor = Color.Blue;
            text.PointSize = 12.0f;
            text.HeightResizePolicy = ResizePolicyType.FillToParent;
            text.WidthResizePolicy = ResizePolicyType.FillToParent;
            Window.Instance.GetDefaultLayer().Add(text);

            Animation animation = new Animation(2000);
            animation.AnimateTo(text, "Orientation", new Rotation(new Radian(new Degree(180.0f)), PositionAxis.X), 0, 500);
            animation.AnimateTo(text, "Orientation", new Rotation(new Radian(new Degree(0.0f)), PositionAxis.X), 500, 1000);
            animation.Looping = true;
            animation.Play();
        }

        public void OnKeyEvent(object sender, Window.KeyEventArgs e)
        {
            if (e.Key.State == Key.StateType.Down && (e.Key.KeyPressedName == "XF86Back" || e.Key.KeyPressedName == "Escape"))
            {
                Exit();
            }
        }

        static void Main(string[] args)
        {
            var app = new Program();
            app.Run(args);
        }
    }
}
```

This application is constructed with the following NUI components:

- The `Program` class is declared, deriving from the `NUIApplication` class
- The `Program` class implements Main function and creates application instance. Then the main application loop is started by calling `app.Run(args)` method.
- A basic NUI applictation requires `OnCreate` callback implementation which is called shortly after `app.Run(args)`. In this example this is the entry point of UI components initialization.
- In the example above `Initialize` method is responsible for setup the key events handler, create the text label and the animation. 

### Add a Button and the HelloWorld application

The basic template uses a label which displays text in an area of the screen. The properties inherited from the base classes of `Label` give control over the display: font attributes, families, and sizes, as well as layout options. Modify the application by adding a button control. It is similar to the label, but is specifically designed to react to click events. As a result, the `Button` class defines the `Clicked` event, which tells the application what to do when the click event takes place.

In order to do something visible on the screen to show that you have received the click event, define another label. Give the new label a value to be displayed in the initial state, and make the button click event handler update the text and button color once the click event triggers.

To modify the application by adding a button and label:

1. Since the click event triggers outside the class constructor, declare the label, and a click counter at the class level:

    ```csharp
    class Program : NUIApplication
    {
        private TextLabel ButtonStateLabel;
        private int ClickedCounter = 0;

        void Initialize()
        {
    ```
2. To avoid placing elements in the window manually the `View root` object is created. This is a container for the application components.
    
    ```csharp
            Window.Instance.KeyEvent += OnKeyEvent;

            View root = new View();
            root.WidthResizePolicy = ResizePolicyType.FillToParent;
            root.HeightResizePolicy = ResizePolicyType.FillToParent;
            Window.Instance.GetDefaultLayer().Add(root);
    ```

3. The `root` object layouts items vertically using `LinearLayout` component. 

    ```csharp
            LinearLayout rootLayout = new LinearLayout();
            rootLayout.LinearOrientation = LinearLayout.Orientation.Vertical;
            rootLayout.LinearAlignment = LinearLayout.Alignment.Center;
            rootLayout.CellPadding = new Size2D(10, 10);
            root.Layout = rootLayout;
    ```

4. The `ButtonStateLabel` shows how many times button was clicked.

    ```csharp
            TextLabel text = new TextLabel("Hello Tizen NUI World");
            text.HorizontalAlignment = HorizontalAlignment.Center;
            text.VerticalAlignment = VerticalAlignment.Center;
            text.TextColor = Color.Blue;
            text.PointSize = 12.0f;
            text.HeightResizePolicy = ResizePolicyType.FitToChildren;
            text.WidthResizePolicy = ResizePolicyType.FitToChildren;
            root.Add(text);

            ButtonStateLabel.Text = string.Format("Clicked counter: {0}", ClickedCounter);
            ButtonStateLabel.HorizontalAlignment = HorizontalAlignment.Center;
            ButtonStateLabel.VerticalAlignment = VerticalAlignment.Center;
            ButtonStateLabel.TextColor = Color.Blue;
            ButtonStateLabel.PointSize = 12.0f;
            ButtonStateLabel.HeightResizePolicy = ResizePolicyType.FitToChildren;
            ButtonStateLabel.WidthResizePolicy = ResizePolicyType.FitToChildren;
            root.Add(ButtonStateLabel);
    ```

5. The `Button` object with the clicked event handler assignement is depicted below. 

    ```csharp
            Button testButton = new Button();
            testButton.Text = "Click Me!";
            testButton.HeightResizePolicy = ResizePolicyType.FitToChildren;
            testButton.WidthResizePolicy = ResizePolicyType.FitToChildren;
            root.Add(testButton);

            testButton.Clicked += OnTestButtonClicked;
        }
    ```

6.  To change the new label's properties when the button is clicked, define the `OnTestButtonClicked` event handler.

    When an event triggers, two parameters are delivered to any handler set up to watch it. The first parameter is an object representing the control that triggered the event and the second parameter is the event data appropriate to the event type.

    Increment the click counter, build a string showing how many times the button has been clicked, and set the `Text` property of the label to that string.

    ```csharp
            void OnTestButtonClicked(object sender, EventArgs args)
            {
                ClickedCounter += 1;
                label.Text = String.Format("Number of clicks: {0}", ClickedCounter);
            }
        }
    }
    ```

The following image shows what happens when you run the modified code.

![Enhanced application](media/cs_first_building_emulator_enhanced.png)

At startup, the text below the button is **unclicked**. After a couple of clicks, the click counter is displayed below the button, and the button color has changed.

This topic only introduces the controls in use in the example above. For more information on Xamarin.Forms, see the [Xamarin Developer Center](https://developer.xamarin.com/guides/xamarin-forms/). There is also [a comprehensive book about Xamarin.Forms](https://developer.xamarin.com/guides/xamarin-forms/creating-mobile-apps-xamarin-forms/)
available as a free download from Microsoft Press.

## Package Your Application

A Tizen .NET application is deployed in the form of an installable package, with the package file extension `.tpk`. A Tizen .NET package has a relatively simple structure: internally it is a ZIP file with content that matches the directory layout of the project.

The package contains the following:

- The `shared` directory, which is for items that are considered system-wide (shareable).

    The application icon is packaged in the `shared/res` directory on installation, and the icon appears on the home screen with the icons for the other applications. You can either replace the icon (which is just a copy of the default Tizen logo) with one of your own using the file name generated by Visual Studio, or put a new icon in the same project directory and update the package manifest to indicate the new name.

- The `res` directory, which is for application-private resources.

    If the application needs a file to open at runtime, it can be placed here.

- The `bin` directory, which contains the generated application executable.
- The `lib` directory, which contains the generated application support code.

    If you use nugget libraries, they are imported in the lib directory.

- The package manifest, which defines the application properties and is used at the installation time.
- Two signature files (author and distributor), which are checked at the installation time.

The following figure shows the layout of the platform-specific (Tizen) project. 

![Project layout](media/vs_solution_explorer_mobile.png)

It includes the `lib`, `res`, and `shared` (with a `res` subdirectory containing an image file) directories, and the **tizen-manifest.xml** file. There is also the `bin` directory, which Visual Studio only shows if you select the **Show all files** option for the solution. These pieces all go into the package.

Package generation (and in fact installation) is controlled by the **tizen-manifest.xml** package manifest file. The following figure shows the `.tpk` file for the initial application, to illustrate how the combination of the directory layout and the package manifest leads to the actual package.

![Package content](media/cs_first_packaging_content_mobile.png)

When packaging your application, you also need to consider whether any feature or privilege declarations are needed in the manifest file, and how to place any language-specific files.
