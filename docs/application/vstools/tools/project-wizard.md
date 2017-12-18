# Project Wizard

The Project Wizard in Visual Studio Tools for Tizen is used to create a Tizen .NET application project.

In the Project Wizard, you can select templates and a profile to create the project. In addition, you can set basic project properties, such as the project name, package name, and location.

The Project Wizard provides 3 project templates with which you can start a native application project:

- **Blank App (Xamarin.Forms)**  
Use this template for creating a Tizen Xamarin application (Common, Mobile, and TV). You can also use this template for a cross-platform projects to add a Tizen project into a Xamarin.Forms solution.

  **Figure: Project Wizard for a cross-platform project**

  ![Project Wizard for a cross-platform project](media/projectwizard-crossnew.png)

- **Blank App (ElmSharp-Beta)**  
Use this template for creating a Tizen application using ElmSharp APIs.
- **Blank App (Tizen.NUI)**  
Use this template for creating a Tizen application using Tizen NUI APIs.

  **Figure: Project Wizard for a native project**

  ![Project Wizard for a native project](media/projectwizard-nativenew.png)

- **Class Library (.NET Standard)**  
Use this template for creating .NET Standard class library.

When you create a new project with a specific template, the Project Wizard automatically creates basic functionalities for the application based on the template. The default project files and folders are also created.

To create a Tizen .NET application project:

1. To open the Project Wizard:

   1. In the Visual Studio menu, go to **File &gt; New &gt; Project &gt; Templates &gt; Visual C# &gt; Tizen**.

   2. Select a template for your project.

      The Project Wizard creates the project based on the selected template.

   3. Set the basic project properties, such as the project name and its location in your local repository, and click **OK**.

2. If you selected the **Blank App (Xamarin.Forms)** template, the Tizen Project Wizard dialog opens.

   Define the package name, select the profiles that you want to add to your solution, and click **OK**.

   ![Select profiles](media/projectwizard-profile.png)

The following figure shows a new .NET application project solution that contains both mobile and TV profiles.

**Figure: Solution with mobile and TV profiles**

![Solution with mobile and TV profiles](media/projectwizard-solution.png)