# Creating Application Projects

<style>
    img {
        border: 1px solid #000000;
        max-width: 100% !important;
        max-height: 100%;
    }
</style>

The **Visual Studio Extension for Tizen** allows you to easily and efficiently create applications for Tizen. This guide provides step-by-step instructions to help you familiarize yourself with the **.NET**, **Web**, and **Native** application development process. By following these steps, you can create and run a basic Tizen application that displays text on the screen without user interaction.

1.  [Set Up the Development Environment](../install.md)<br>

    Before you begin developing Tizen applications, ensure that your development environment is properly set up. This includes installing **Visual Studio**, the **Visual Studio Tools for Tizen**, and required toolsets.

2.  [Create a Project](#create-a-project)

    Use a **predesigned project template** to create a Tizen application. These templates generate the essential files and folders needed to start development. Select the appropriate template for **.NET**, **Web**, or **Native** applications.

3.  [Build Your Application](#build-your-application)

    After adding the necessary code and features, build your application to **validate and compile** the code. This step ensures there are no syntax errors or missing dependencies.

4.  [Deploy and Run Your Application](#deploy-and-run-your-application)

    Deploy the application to an **emulator or a real Tizen device** and run it to verify its functionality.

5.  [Debug your Application in Emulator](#debug-your-application-in-emulator)

    Use debugging tools to **analyze, troubleshoot, and fix** issues in your application. The Tizen emulator provides a testing environment for debugging before deployment on actual devices.


<div>
    <button onclick="showContent('dotnet')">.NET Application </button>
    <button onclick="showContent('web')">Web Application </button>
    <button onclick="showContent('native')">Native Application</button>
</div>

## Create a Project

<div class="content dotnet">
   <p>The following example shows Step-by-Step Guide to Creating a <b>Tizen .NET</b> Application.</p>
    <ol>
        <li><b>Open Visual Studio</b><br>
        Launch Visual Studio on your development machine.</li>
        <li><b>Create a New Project</b><br>
        In the Visual Studio menu, select <b>File</b> > <b>New</b> > <b>Project</b>.</li>
        <img alt="Create new project" src="/docs/application/vstools/media/vs2022_project_create_1.png" />
        <p></p>
        <li><b> Select the Tizen .NET Project Template</b><br>
        In <b>Create a New project</b> window, select <b>#C</b> and <b>Tizen</b> from the dropdown menu, and choose <b>Tizen DotNet Project</b>. Then click <b>Next</b>.</li>
        <img  src="/docs/application/vstools/media/vs2022_project_create_2_dotnet.png" />
        <p></p>
        <p>Configure the project properties by entering the <b>Project Name</b>, <b>Location</b>, and <b>Solution Name</b>, then click <b>Create</b>.</p>
        <img  src="/docs/application/vstools/media/vs2022_project_create_3_dotnet.png"/>
        <p></p>
        <p>Then the <b>Tizen Project Wizard</b> pop-up window appears.</p>
        <li><b>Select Profile, Platform Version, and Template</b><br>
        Choose the appropriate <b>Profile</b> (e.g., Mobile, Wearable, TV). Select the <b>Platform Version</b> compatible with your target device. Pick a <b>Project Template</b> based on your application requirements. Click <b>OK</b> to finalize the project creation.</li>
        <img src="/docs/application/vstools/media/vs2022_project_create_4_dotnet.png" />
        <p></p>
        <p>The following figure illustrates the solution explorer for newly created <b>TizenDotNet</b> project:</p><img src="/docs/application/vstools/media/vs2022_project_create_5_dotnet.png"/>
        <p></p>
    </ol>
    <p>Once the project is created, you can start adding your application logic and UI elements.</p>
</div>

<div class="content web">
    <p>The following example shows Step-by-Step Guide to Creating a <b>Tizen Web</b> Application.</p>
    <ol>
        <li><b>Open Visual Studio</b><br>
        Launch Visual Studio on your development machine.</li>
        <li><b>Create a New Project</b><br>
        In the Visual Studio menu, select <b>File</b> > <b>New</b> > <b>Project</b>. </li>
        <img alt="Create new project" src="/docs/application/vstools/media/vs2022_project_create_1.png" />
        <p></p>
        <li><b> Select the Tizen Web Project Template</b><br>
        In <b>Create a New project</b> window, select <b>javaScript</b> and <b>Tizen</b> from the dropdown menu, and choose <b>Tizen Web Project</b>. Then click <b>Next</b>.</li>
        <img alt="New project menu" src="/docs/application/vstools/media/vs2022_project_create_2_web.png" />
        <p></p>
        <p>Configure the project properties by entering the <b>Project Name</b>, <b>Location</b>, and <b>Solution Name</b>, then click <b>Create</b>.</p>
        <img alt="Configure your project" src="/docs/application/vstools/media/vs2022_project_create_3_web.png"/>
        <p></p>
        <p>Then the <b>Tizen Project Wizard</b> pop-up window appears.</p>
        <li><b>Select Profile, Platform Version, and Template</b><br>
        Choose the appropriate <b>Profile</b> (e.g., Mobile, Wearable, TV). Select the <b>Platform Version</b> compatible with your target device. Pick a <b>Project Template</b> based on your application requirements. Click <b>OK</b> to finalize the project creation.</li>
        <img alt="Tizen Profile Select" src="/docs/application/vstools/media/vs2022_project_create_4_web.png" />
        <p></p>
        <p>The following figure illustrates the solution explorer for newly created <b>TizenWeb</b> project:</p>
        <img alt="Project Folder" src="/docs/application/vstools/media/vs2022_project_create_5_web.png" />
        <p></p>
    </ol>
    <p>Once the project is created, you can start adding your application logic and UI elements.</p>
</div>
<div class="content native">
     <p>The following example shows Step-by-Step Guide to Creating a <b>Tizen Native</b> Application.</p>
    <ol>
        <li><b>Open Visual Studio</b><br>
        Launch Visual Studio on your development machine.</li>
        <li><b>Create a New Project</b><br>
        In the Visual Studio menu, select <b>File</b> > <b>New</b> > <b>Project</b>.</li>
        <img alt="Create new project" src="/docs/application/vstools/media/vs2022_project_create_1.png" />
        <p></p>
        <li><b> Select the Tizen Native Project Template</b><br>
        In <b>Create a New project</b> window, select <b>C++</b> and <b>Tizen</b> from the dropdown menu, and choose <b>Tizen Native Project</b>. Then click <b>Next</b></li>
        <img alt="New project menu" src="/docs/application/vstools/media/vs2022_project_create_2_native.png" />
        <p></p>
        <p>Configure the project properties by entering the <b>Project Name</b>, <b>Location</b>, and <b>Solution Name</b>, then click <b>Create</b>.</p>
        <img alt="Configure your project" src="/docs/application/vstools/media/vs2022_project_create_3_native.png"/>
        <p></p>
        <p>Then the <b>Tizen Project Wizard</b> pop-up window appears.</p>
        <li><b>Select Profile, Platform Version, and Template</b><br>
        Choose the appropriate <b>Profile</b> (e.g., Mobile, Wearable, TV). Select the <b>Platform Version</b> compatible with your target device. Pick a <b>Project Template</b> based on your application requirements. Click <b>OK</b> to finalize the project creation.</li>
        <img alt="Tizen Profile Select" src="/docs/application/vstools/media/vs2022_project_create_4_native.png" />
        <p></p>
        <p>The following figure illustrates the solution explorer for newly created <b>TizenNative</b> project:</p>
        <img alt="Project Folder" src="/docs/application/vstools/media/vs2022_project_create_5_native.png" />
        <p></p>
    </ol>
    <p>Once the project is created, you can start adding your application logic and UI elements.</p>
</div>
</div>

## Build Your Application
After creating the Tizen application project, you can implement the required features. In this example, we use the default project template without making any code changes.

When your application code is ready, you need to **build the application**. The build process performs validation checks and compiles your project files. Additionally, the application package must be signed with an author certificate. If you have not yet registered a Tizen certificate in Visual Studio, refer to the [Certificate Manager](../../vstools/tools/certificate-manager.md) for setup instructions.

### Build the Project

<div class="content dotnet">
<p>There are two ways to build your <b>Tizen .NET</b> Application:</p>
    <ol>
        <li><b>Using the Visual Studio Menu</b><br>In the Visual Studio , navigate to <b>Build > Build Solution</b>.</li>
        <img alt="Build solution" src="/docs/application/vstools/media/vs2022_build_1_dotnet.png" />
        <p></p>
        <li><b>Using Solution Explorer</b><br>
        In the <b>Solution Explorer</b> view, right-click on the solution name and select <b>Build</b>.</li>
        <img alt="Solution Explorer" src="/docs/application/vstools/media/vs2022_build_2_dotnet.png" />
        <p></p>
    </ol>
</div>
<div class="content web">
    <p>There are two ways to build your <b>Tizen Web</b> Application:</p>
    <ol>
        <li><b>Using the Visual Studio Menu</b><br>In the Visual Studio , navigate to <b>Build > Build Solution</b>.</li>
        <img alt="Build solution" src="/docs/application/vstools/media/vs2022_build_1_web.png" />
        <p></p>
        <li><b>Using Solution Explorer</b><br>
        In the <b>Solution Explorer</b> view, right-click on the solution name and select <b>Build</b>.</li>
        <img alt="Solution Explorer" src="/docs/application/vstools/media/vs2022_build_2_web.png" />
        <p></p>
    </ol>
</div>
<div class="content native">
<p>There are two ways to build your <b>Tizen Native</b> Application:</p>
    <ol>
        <li><b>Using the Visual Studio Menu</b><br>In the Visual Studio , navigate to <b>Build > Build Solution</b>.</li>
        <img alt="Build solution" src="/docs/application/vstools/media/vs2022_build_1_native.png" />
        <p></p>
        <li><b>Using Solution Explorer</b><br>
        In the <b>Solution Explorer</b> view, right-click on the solution name and select <b>Build</b>.</li>
        <img alt="Solution Explorer" src="/docs/application/vstools/media/vs2022_build_2_native.png" />
        <p></p>
    </ol>
</div>

## Deploy and Run Your Application

<div class="content dotnet">
    <p>Once your <b>Tizen .NET</b> application is built successfully, you can deploy and run it on an emulator or a real Tizen device. Follow the steps below to launch and test your application in the <b>Tizen Emulator</b>.</p>
    <ol>
        <li><b>Launch the Tizen Emulator Manager</b><br>Click the <b>Launch Tizen Emulator</b> from the Visual Studio toolbar.
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_1_dotnet.png"/>
        <p></p>
        Alternatively, open <b>Tizen Emulator Manager</b> from <b>Tools > Tizen > Tizen Emulator Manager</b>.</li>
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_2_dotnet.png"/>
        <p></p>
        <li><b>Select and Launch an Emulator</b><br>Choose an emulator instance that matches or has a higher <b>Tizen platform version</b> than your application. Click <b>Launch</b> to start the selected emulator.<br>
        <img alt="Choosing emulator"  src="/docs/application/vstools/media/vs2022_run_3_emulator.png"/>
        <p>Once the emulator window is visible, switch back to Visual Studio.</p></li>
        <img alt="Emulator window" src="/docs/application/vstools/media/vs2022_run_4_emulator.png"/>
        <li><b>Run or Debug Your Application</b><br>In Visual Studio, the newly launched emulator should now appear in the <b>Run and Debug</b> dropdown. Click the <b>bold green arrow</b> button to debug the application. Click the unfilled <b>light green button</b> to run the application without debugging.</li>
        <img alt="Deploy and run applicaion" src="/docs/application/vstools/media/vs2022_run_5_dotnet.png"/>
        <li><b> View the Application in the Emulator</b><br>Once deployed, the <b>Tizen .NET application UI</b> will be displayed on the emulator screen. You can now interact with it to verify its functionality.</li>
        <img alt="Visible project UI on emulator screen" src="/docs/application/vstools/media/vs2022_run_6_dotnet.png"/>
        <p></p>
    </ol>
</div>
<div class="content web">
    <p>Once your <b>Tizen web</b> application is built successfully, you can deploy and run it on an emulator or a real Tizen device. Follow the steps below to launch and test your application in the <b>Tizen Emulator</b>.</p>
    <ol>
        <li><b>Launch the Tizen Emulator Manager</b>Click the <b>Launch Tizen Emulator</b> from the Visual Studio toolbar.
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_1_web.png"/>
        <p></p>
        Alternatively, open <b>Tizen Emulator Manager</b> from <b>Tools > Tizen > Tizen Emulator Manager</b>.</li>
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_2_web.png"/>
        <p></p>
        <li><b>Select and Launch an Emulator</b><br>Choose an emulator instance that matches or has a higher <b>Tizen platform version</b> than your application. Click <b>Launch</b> to start the selected emulator.<br>
        <img alt="Choosing emulator"  src="/docs/application/vstools/media/vs2022_run_3_emulator.png"/>
        <p>Once the emulator window is visible, switch back to Visual Studio.</p></li>
        <img alt="Emulator window" src="/docs/application/vstools/media/vs2022_run_4_emulator.png"/>
        <li><b>Run or Debug Your Application</b><br>In Visual Studio, the newly launched emulator should now appear in the <b>Run and Debug</b> dropdown. Click the <b>bold green arrow</b> button to debug the application. Click the unfilled <b>light green button</b> to run the application without debugging.</li>
        <img alt="Deploy and run applicaion" src="/docs/application/vstools/media/vs2022_run_5_web.png"/>
        <li><b> View the Application in the Emulator</b><br>Once deployed, the <b>Tizen Web application UI</b> will be displayed on the emulator screen. Yon can now interact with it to verify its functionality.</li>
        <img alt="Visible project UI on emulator screen" src="/docs/application/vstools/media/vs2022_run_6_web.png"/>
        <p></p>
    </ol>
</div>
<div class="content native">
    <p>Once your <b>Tizen Native</b> application is built successfully, you can deploy and run it on an emulator or a real Tizen device. Follow the steps below to launch and test your application in the <b>Tizen Emulator</b>.</p>
    <ol>
        <li><b>Launch the Tizen Emulator Manager</b><br>Click the <b>Launch Tizen Emulator</b> from the Visual Studio toolbar.
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_1_native.png"/>
        <p></p>
        Alternatively, open <b>Tizen Emulator Manager</b> from <b>Tools > Tizen > Tizen Emulator Manager</b>.</li>
        <img alt="Launching Tizen Emulation Manager" src="/docs/application/vstools/media/vs2022_run_2_native.png"/>
        <p></p>
        <li><b>Select and Launch an Emulator</b><br>Choose an emulator instance that matches or has a higher <b>Tizen platform version</b> than your application. Click <b>Launch</b> to start the selected emulator.<br>
        <img alt="Choosing emulator"  src="/docs/application/vstools/media/vs2022_run_3_emulator.png"/>
        <p>Once the emulator window is visible, switch back to Visual Studio.</p></li>
        <img alt="Emulator window" src="/docs/application/vstools/media/vs2022_run_4_emulator.png"/>
        <li><b>Run or Debug Your Application</b><br>In Visual Studio, the newly launched emulator should now appear in the <b>Run and Debug</b> dropdown. Click the <b>bold green arrow</b> button to debug the application. Click the unfilled <b>light green button</b> to run the application without debugging.</li>
        <img alt="Deploy and run applicaion" src="/docs/application/vstools/media/vs2022_run_5_native.png"/>
        <li><b> View the Application in the Emulator</b><br>Once deployed, the <b>Tizen native application UI</b> will be displayed on the emulator screen. You can now interact with it to verify its functionality.</li>
        <img alt="Visible project UI on emulator screen" src="/docs/application/vstools/media/vs2022_run_6_native.png"/>
        <p></p>
</div>

## Debug Your Application in Emulator
<div class="content dotnet">
<p>Debugging allows you to analyze and fix issues in your <b>Tizen .NET</b> application by pausing execution and inspecting variable values. Follow these steps to debug your application effectively.</p>
    <ol>
        <li><b>Open the Source Code File</b> <br>In Visual Studio, open the <b>.cs</b> file of your Tizen .NET application where you want to debug.</li>
        <p></p>
        <li><b>Add a Breakpoint</b><br>Click on the left margin of the code editor next to the line where you want execution to pause. Alternatively, select a line and press <b>F9</b> to set a breakpoint.</li>
        <img alt="Debugging application" src="/docs/application/vstools/media/vs2022_debug_dotnet.png"/>
        <p></p>
        <li><b>Start the Debugging Session</b><br> Navigate to <b>Debug > Start Debugging</b>.Or, click the <b>green arrow (emulator name)</b> in the toolbar.You can also press <b>F5</b> to begin debugging.</li>
    </ol>
<div>
<div class="content web">
<p>Debugging allows you to analyze and fix issues in your <b>Tizen Web</b> application by pausing execution and inspecting variable values. Follow these steps to debug your application effectively.</p>
    <ol>
        <li><b>Setting Up Google Chrome for Debugging</b><br>Before starting web application debugging in Tizen, ensure that the Google Chrome path is correctly set in <b>Visual Studio</b>. Go to <b>Tools > Options > Tizen > Tools</b>, and check if the Chrome path is specified. If not, manually enter the path to the Chrome executable (e.g., C:\Program Files\Google\Chrome\Application\chrome.exe) and click <b>OK</b> to save the changes.</li>
         <img alt="Setting Goggle Chrome path" src="/docs/application/vstools/media/vs2022_debug_web_option.png"/>
        <p></p>
       <li><b>Open the Source Code File</b> <br>In Visual Studio, open the <b>.js</b> file of your Tizen Web application where you want to debug.</li>
        <p></p>
        <li><b>Add a Breakpoint</b><br>Click on the left margin of the code editor next to the line where you want execution to pause. Alternatively, select a line and press <b>F9</b> to set a breakpoint.</li>
        <img alt="Debugging application" src="/docs/application/vstools/media/vs2022_debug_web.png"/>
        <p></p>
        <li><b>Start the Debugging Session</b><br> Navigate to <b>Debug > Start Debugging</b>.Or, click the <b>green arrow (emulator name)</b> in the toolbar.You can also press <b>F5</b> to begin debugging.</li>
    </ol>
<div>
<div class="content native">
<p>Debugging allows you to analyze and fix issues in your <b>Tizen Native</b> application by pausing execution and inspecting variable values. Follow these steps to debug your application effectively.</p>
    <ol>
        <li><b>Open the Source Code File</b><br>In Visual Studio, open the <b>.c</b> file of your Tizen Native application where you want to debug.</li>
        <p></p>
        <li><b>Add a Breakpoint</b><br>Click on the left margin of the code editor next to the line where you want execution to pause. Alternatively, select a line and press <b>F9</b> to set a breakpoint.</li>
        <img alt="Debugging application" src="/docs/application/vstools/media/vs2022_debug_native.png"/>
        <p></p>
        <li><b>Start the Debugging Session</b><br> Navigate to <b>Debug > Start Debugging</b>.Or, click the <b>green arrow (emulator name)</b> in the toolbar.You can also press <b>F5</b> to begin debugging.</li>
    </ol>
<div>
<script>
    function showContent(className) {
        // Get all content divs
        const allContents = document.querySelectorAll('.content');
        // Hide all content divs
        allContents.forEach(content => content.classList.remove('active'));
        // Show only divs with the matching class
        const selectedContents = document.querySelectorAll(`.${className}`);
        selectedContents.forEach(content => content.classList.add('active'));
    }
    // Show .NET content by default
    document.addEventListener('DOMContentLoaded', () => {
    showContent('dotnet');
    });
</script>
</body>
