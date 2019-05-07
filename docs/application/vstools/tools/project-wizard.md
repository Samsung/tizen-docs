# Project Wizard

You can use Project Wizard to create Tizen .NET application projects. In Project Wizard, you can select a template and a profile to create the project. Aditionally, you can set the basic project properties, such as the project name, package name, location, and so on.

The Project Wizard provides the following project templates using which you can start a Tizen application project:

Template | Description | Supported Versions
-------- | ----------- | -------------------
**Blank App (ElmSharp-Beta)** | Use this template to create Tizen applications using the ElmSharp APIs. | Tizen 4.0, Tizen 5.0
**Blank App (Tizen.NUI)** | Use this template to create Tizen applications using Natural User Interface (NUI) toolkit. | Tizen 4.0, Tizen 5.0
**Blank App (Xamarin.Forms)** | Use this template to create Tizen applications with Xamarin.Forms for multiple profiles (Common, Mobile, TV, and Wearable). | Tizen 4.0, Tizen 5.0
**Class Library (.NET Standard)** | Use this template to create .NET standard class library for Tizen. | Tizen 4.0, Tizen 5.0
**Service App** | Use this template to create service applications for the Tizen platform. | Tizen 4.0, Tizen 5.0
**Tizen OpenTK App** | Use this template to create Tizen applications using the Open Toolkit library. | Tizen 5.0
**Tizen Watchface App** | Use this template to create Tizen Watchface applications for wearable devices. | Tizen 4.0, Tizen 5.0
**Tizen Wearable App** | Use this template to create Tizen .NET applications for wearable devices. | Tizen 4.0, Tizen 5.0
**Tizen Wearable Xaml App** | Use this template to create Tizen XAML applications for wearable devices. | Tizen 4.0, Tizen 5.0
**Tizen XAML App (Xamarin.Forms)** | Use this template to create XAML applications using Xamarin.Forms for multiple profiles (Common, Mobile, TV, and Wearable). | Tizen 4.0, Tizen 5.0
**UI Test APP** | Use this template to create automated UI test applications for Tizen. | Tizen 4.0, Tizen 5.0

You can navigate to the Project Wizard templates:

![Project Wizard templates for .NET projects](media\v5_project_templates.gif)

## Create New Project

When you create a new project with a specific template, the Project Wizard automatically creates the basic functionalities for the application based on the selected template. It also creates the default project files and folders.

To create a Tizen .NET application project:

1. Open Visual Studio.
2. Click **File &gt; New &gt; Project**. The **New Project Window** appears. 
3. Click **Installed &gt; Visual C#**. 
4. Select one of the available Tizen versions, **Tizen 4.0** or **Tizen 5.0** based on your requirement.
5. Select one of the available templates for your project (let us assume that you selected **Tizen 5.0 > Blank App (Xamarin.Forms)**).
6. Set the basic project properties:
    - **Name**: Name of the project.
    - **Location**: Location of the local repository in your computer. Aditionally, you can also **Browse** for the local repository.
    - **Solution name**: The name of the solution file for the project. This option is enabled only if you select **Create directory for solution**.
    - **Create directory for solution**: Select this option to create a directory where the solution file will be automatically saved.
    - **Create new Git repository**: Select this option to create a new Git repository for your project.
7. Click **OK**. The **New Project Window** appears.
8. Select the profiles (Common, Mobile, TV, Wearable (preview)) for which you want to create a solution, and click **OK**.

    ![Select profiles](media/projectwizard-profile.png) 

    The following figure shows a new .NET application project solution that contains Mobile, TV, and Wearable profiles:

    ![Solution with mobile and TV profiles](media/projectwizard-solution.png)

The new project is created.

![New project](media/new-project.png)