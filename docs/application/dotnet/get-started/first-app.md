<style>
    .tabcontent img {
        border: 1px solid #555;
        max-width: 100% !important;
        max-height: 100%;
    }
</style>

# Create Your First Tizen .NET Application

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

To create a new Tizen .NET project you can use 3 following tools: Visual Studio, Visual Studio Code with Tizen SDK extensions or CLI tools included in Tizen SDK.

<div id="TabSection1">
    <div class="sampletab" id="ProjectCreateTab">
        <button id="create-button1" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-2019-Create', 'TabSection1')">Visual Studio 2019</button>
        <button id="create-button2" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-Code-Create', 'TabSection1')">Visual Studio Code</button>
        <button id="create-button3" class="tablinks" onclick="openTabSection(event, 'CLI-Create', 'TabSection1') ">CLI</button>
    </div>
    <div id="Visual-Studio-2019-Create" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Launch Visual Studio.</li>
                        <li>In the Visual Studio menu, select <b>File</b> > <b>New</b> > <b>Project</b>.</li>
                        <img alt=" " src="media/vs2019_project_create_1.png" />
                        <p></p>
                        <li>In <b>New project</b> menu, select <b>Tizen</b> > <b>Blank App (Tizen.NUI)</b>. Click <b>Next</b>.</li>
                        <img alt=" " src="media/vs2019_project_create_2.png" />
                        <p></p>
                        <p>Configure the project properties and click <b>Create</b>. You can enter the <b>Project name</b>, <b>Location</b>, <b>Solution</b>, and <b>Solution name</b>.</p>
                        <img alt=" " src="media/vs2019_project_create_3.png" />
                        <p></p>
                        <p>The <b>Tizen Project Wizard</b> pop-up window appears.</p>
                        <li>Select <b>Platform Version</b> and click <b>OK</b></li>
                        <img alt=" " src="media/vs2019_project_create_4.png" />
                        <p></p>
                        <p>The following figure illustrates a solution explorer for created <b>HelloWorld</b> project:</p>
                        <img alt=" " src="media/vs2019_project_create_5.png" />
                        <p></p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="Visual-Studio-Code-Create" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Launch Visual Studio Code.</li>
                        <li>Use <b>ctrl + P</b> to open commands tool and type <b>Tizen .NET: Create</b> and hit Enter key.</li>
                        <img alt=" " src="media/vscode_project_create_1.png"/>
                        <p></p>
                        <li>Choose NUI Application template: <b>tizen-6.0 TizenNUIApp</b></li>
                        <img alt=" " src="media/vscode_project_create_2.png"/>
                        <p></p>
                        <li>Choose the Tizen .NET project name. In this case <b>HelloWorld</b> was used.</li>
                        <img alt=" " src="media/vscode_project_create_3.png"/>
                        <p></p>
                        <li>If the project is created properly a popup will appear in the bottom corner of the Vscode window.</li>
                        <img alt=" " src="media/vscode_project_create_4.png"/>
                        <p></p>
                        <p>If <b>Yes</b> option is selected, the Vscode will change working directory to the created project</p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="CLI-Create" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <p>go to directory where project will be created and type:</p>
                    <code>$ tizen create cs-project -t Tizen.NUI.Template55.Single -v tizen-5.5 -n HelloWorld</code>
                </tr>
            </tbody>
        </table>
    </div>
</div>

## Build Your Application

After you have created the application project, you can implement the required features. In this example, only the default features from the project template are used, and no code changes are required.

When your application code is ready, build the application. The building process performs a validation check and compiles your files. You must sign the application package with an author certificate when building the application. If you have not yet registered a Tizen certificate in Visual Studio, see [Certificate Manager](../../../vstools/tools/certificate-manager.md).

<div id="TabSection2">
    <div class="sampletab" id="ProjectBuildTab">
        <button id="build-button1" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-2019-Build', 'TabSection2')">Visual Studio 2019</button>
        <button id="build-button2" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-Code-Build', 'TabSection2')">Visual Studio Code</button>
        <button id="build-button3" class="tablinks" onclick="openTabSection(event, 'CLI-Build', 'TabSection2')">CLI</button>
    </div>
    <div id="Visual-Studio-2019-Build" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <p>There are two different ways to build the application:</p>
                    <ol>
                        <li>In the Visual Studio menu, select <b>Build > Build Solution</b>.</li>
                        <img alt=" " src="media/vs2019_build_1.png" />
                        <p></p>
                        <li>In the <b>Solution Explorer</b> view, right-click the solution name and select <b>Build</b></li>
                        <img alt=" " src="media/vs2019_build_2.png" />
                        <p></p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="Visual-Studio-Code-Build" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Use `ctrl + P` to show command panel</li>
                        <li>Type Tizen .NET</li>
                        <img alt=" " src="media/vscode_build_1.png" />
                        <p></p>
                        <li>Choose Tizen .NET: Build Tizen .NET project</li>
                        <img alt=" " src="media/vscode_build_2.png" />
                        <li>Now build system should create tpk file with the NUI application.</li>
                        <img alt=" " src="media/vscode_build_3.png" />
                        <p></p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="CLI-Build" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Change working directory to the <b>HelloWorld</b> project, <b>helloworld.sln</b> file should be placed in the changed directory.</li>
                        <li>Type <code>$ tizen build-cs</code> in your terminal.</li>
                        <li>Output <b>.tpk</b> file should be created in the <b>helloworld/bin/Debug/tizen80/</b> directory.</li>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
</div>

Tizen .NET applications are always deployed as installed packages. The package files have the `.tpk` file extension, and the process of generating a package is controlled by the [manifest file](../../../vstools/tools/manifest-editor.md). The Tizen SDK tools generate the manifest file (`tizen-manifest.xml`) to the top level of the \<projectname\>.Tizen project.

For this example application, the default manifest is sufficient. If you want to make any changes in the application, such as changing the application icon or installing resources that are used by the application at runtime, see [Package Your Application](#package-your-application).

After you have built the application, deploy and run it.

## Deploy and Run Your Application

To run the application, you must first deploy it to the target: either a device or an emulator. Deploying means transferring the package file (`.tpk`) to the target and invoking the Tizen Package Manager to install it.

To deploy and run the application on the emulator:

<div id="TabSection3">
    <div class="sampletab" id="ProjectRunTab">
        <button id="run-button1" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-2019-Run', 'TabSection3')">Visual Studio 2019</button>
        <button id="run-button2" class="tablinks" onclick="openTabSection(event, 'Visual-Studio-Code-Run', 'TabSection3')">Visual Studio Code</button>
        <button id="run-button3" class="tablinks" onclick="openTabSection(event, 'CLI-Run', 'TabSection3')">CLI</button>
    </div>
    <div id="Visual-Studio-2019-Run" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Launch <b>Tizen Emulator Manager</b> from menu <b>Tools > Tizen > Tizen Emulator Manager</b>.</li>
                        <img alt=" " src="media/vs2019_run_1.png"/>
                        <p></p>
                        <li>Choose Emulator. For basic NUI template there is no difference which platform will be used. In this example the application is tested on TV emuator.</li>
                        <img alt=" " src="media/vs2019_run_2.png"/>
                        <li>When emulator window will be visible you can swich back to the Visual Studio.</li>
                        <img alt=" " src="media/vs2019_run_3.png"/>
                        <li>In Visual Studio new launch mode shoud be visible with valid emulator name. To deploy and run application green arrow can be used.</li>
                        <img alt=" " src="media/vs2019_run_4.png"/>
                        <li>After point above <b>HelloWorld</b> project UI should be visible on emulator screen.</li>
                        <img alt=" " src="media/vs2019_run_5.png"/>
                        <p></p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="Visual-Studio-Code-Run" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Use <b>ctrl + P</b> to show command panel.</li>
                        <li>Type <b>Tizen .NET: Emul</b> and launch the Tizen Emulator Manager.</li>
                        <img alt=" " src="media/vscode_run_1.png"/>
                        <p></p>
                        <li>Choose Emulator. For basic NUI template there is no difference which platform will be used. In this example the application is tested on TV emuator.</li>
                        <img alt=" " src="media/vs2019_run_2.png"/>
                        <p></p>
                        <li>When emulator window will be visible you can swich back to the Visual Studio Code.</li>
                        <img alt=" " src="media/vs2019_run_3.png"/>
                        <li>Use <b>ctrl + P</b> to open command panel again and type <b>Tizen .NET: Set</b> and set the Tizen Device<b>.</li>
                        <img alt=" " src="media/vscode_run_2.png"/>
                        <p></p>
                        <p>After that popup in the right corner of the Visual Studio code will appear.</p>
                        <img alt=" " src="media/vscode_run_3.png"/>
                        <p></p>
                        <li>Use <b>ctrl + P</b> to open the command panel and type <b>Tizen .NET: Run</b>and choose available option</li>
                        <img alt=" " src="media/vscode_run_4.png"/>
                        <li>After point above <b>HelloWorld</b> project UI should be visible on emulator screen.</li>
                        <img alt=" " src="media/vs2019_run_5.png"/>
                        <p></p>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
    <div id="CLI-Run" class="tabcontent">
        <table>
            <tbody>
                <tr>
                    <ol>
                        <li>Run the Tizen SDK emulator manager manually and start the Emulator Image.</li>
                        <li>Choose Emulator. For basic NUI template there is no difference which platform will be used. In this example the application is tested on TV emuator.</li>
                        <img alt=" " src="media/vs2019_run_2.png"/>
                        <p></p>
                        <li>In project diretory locate application <b>.tpk</b> file. Then use command:</li>
                        <code>$ sdb install helloworld/bin/Debug/tizen80/org.tizen.example.helloworld-1.0.0.tpk</code>
                        <li>To run application on TV emulator type:</li>
                        <code>$ tizen run -p org.tizen.example.helloworld</code>
                    </ol>
                </tr>
            </tbody>
        </table>
    </div>
</div>

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

**Figure: Modified Hello World App**
|  Startup State|  Clicked State |
|---------------------------------------------------------|----------------------------------------------------|
| ![Enhanced application](media/cs_nui_helloworld_1.png)  | ![Enhanced application](media/cs_nui_helloworld_2.png)                                      |

At startup, the text above the button is **Clicked Counter: 0**. After a couple of clicks, the click counter is changed.

This topic only introduces the controls in use in the example above.For more information, see the [NUI Guides](../../guides/index.md).

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

![Project layout](media/vs2019_project_create_5.png)

It includes the `lib`, `res`, and `shared` (with a `res` subdirectory containing an image file) directories, and the **tizen-manifest.xml** file. There is also the `bin` directory, which Visual Studio only shows if you select the **Show all files** option for the solution. These pieces all go into the package.

Package generation (and in fact installation) is controlled by the **tizen-manifest.xml** package manifest file. The following figure shows the `.tpk` file for the initial application, to illustrate how the combination of the directory layout and the package manifest leads to the actual package.

![Package content](media/tpk_package_content.png)

When packaging your application, you also need to consider whether any feature or privilege declarations are needed in the manifest file, and how to place any language-specific files.

<script>
    function openTabSection(evt, profileName, sectionId) {
        var i, tabcontent, tablinks, section;
        let selected = 0;

        section = document.getElementById(sectionId);
        tabcontent = section.getElementsByClassName("tabcontent");

        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
            if (tabcontent[i].id == profileName) {
                selected = i;
            }
        }

        tablinks = section.getElementsByClassName("tablinks");

        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }

        tabcontent[selected].style.display = "block";
        evt.currentTarget.className += " active";
    }

    document.getElementById("create-button1").click();
    document.getElementById("build-button1").click();
    document.getElementById("run-button1").click();
</script>