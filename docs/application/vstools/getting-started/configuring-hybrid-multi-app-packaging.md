# Hybrid Application Development

This guide explains how to use the **Visual Studio Extension for Tizen** to develop hybrid applications. Hybrid application for Tizen supports different types of projects (**.NET, Native, Web**) within the same **solution/workspace**.

### 1. Creating Tizen .NET Project

To create a **Tizen .NET** project, refer to the [Creating Application Projects](../../vstools/getting-started/creating-application-projects.md) section.

### 2. Adding a Tizen Native Project

To integrate a **Tizen Native project** into the existing **.NET project** and form a hybrid solution, follow these steps:

1. **Add a New Project**<br>
In **Visual Studio Solution Explorer**, right-click on the **Solution**. Select **Add > New Project** or import existing project by **Add > Existing Project**.
<img alt="Create Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_1.png" />
<p></P>

2.  **Select the Tizen Native Project Template**<br>
For creating Native application,In **Create a New project** window, select **C++** and **Tizen** from the dropdown menu, and choose **Tizen Native Project**. Then click **Next**.
<img alt="Create Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_project_create_2_native.png" />
<p></P>

3. **Configure the Project**<br>
Enter the **Project Name** and click **Create**.
<img alt="Configure Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_2.png" />
<p></P>

4. **Select the Tizen Profile and Template**<br>
Pick a **Project Template** based on your application requirements. Click **OK** to finalize the project creation.
<img alt="Tizen Profile and Template Selection" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_3.png" />
The following figure illustrates the solution explorer for newly created <b>Tizen Native</b> project.
<img alt="Native project in solution explorer" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_4.png" />
<p></P>


### 3. Setting Startup Project

In **Solution Explorer**, right click on the desired project and select **Set as Startup Project**.
<img alt="Setting startup project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_5.png" />
<p></P>

### 4. Adding Project Dependency

1. **Open Project Dependencies**<br>
In **Solution Explorer**, right-click on the **Startup Project**. Select **Add Tizen Project Dependency**.
<img alt="Tizen Project Dependency" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_6.png" />
<p></P>

2. **Select Dependency Projects**<br>
A window displaying a list of projects will appear.
<img alt="Tizen Project Dependency" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_7.png" />
<p></P>

3. **Confirm Selection**<br>
Select the **required dependency projects** and click **OK**.
<img alt="Confirm Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_8.png" />
<p></P>


### 5. Building and Running the Project

1. **Build the Solution**<br>
In the **Visual Studio** , navigate to **Build > Build Solution**.
<img alt="Build Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_9.png" />
<p></P>

2. **Deploy and Run the Application**<br>
In Visual Studio, the launched emulator should appear in the Run and Debug dropdown. Click the **bold green arrow** button to debug the application. Click the **unfilled light green button** to run the application without debugging or navigate to **Debug > Start without Debugging**.
<img alt="Deploy and Run Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_10.png" />
<p></P>


### 6. Debugging the Hybrid Application

1. **Open the Source Code File**<br>
Open the relevant **.cs** file (for .NET) or **.cpp** file (for Native).

2. **Add a Breakpoint** <br>
Click on the left margin of the code editor next to the line where you want execution to pause. Alternatively, select a line and press **F9** to set a breakpoint.
<img alt="Debug Tizen project" style="border: 1px solid #000000;" src="/docs/application/vstools/media/vs2022_hybrid_11.png" />
<p></P>

3. **Start the Debugging Session**<br>
Navigate to **Debug > Start Debugging**. Or, click the **green arrow (emulator name)** in the toolbar.You can also press **F5** to begin debugging.
