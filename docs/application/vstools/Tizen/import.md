# Importing Tizen Studio projects into Visual Studio

The following sections explain how to use Visual Studio Extension for Tizen to import your projects created in Tizen Studio to Visual Studio.

##### NOTE: 
Ensure that the Tizen Studio project was exported to CLI before importing to Visual Studio

### Add Tizen Native project

To add a Tizen Native project into the above created .NET project to make the Hybrid solution:

1. Go to Tools Menu in Visual Studio, select Tizen > Import Tizen Studio Project from the dropdown menu. Tizen Project Wizard will open.
   ![Import project](media/import_project_menu.PNG)

2. In Wizard, browse and select the path of project to be imported.
   ![Configure project](media/import_project_wizard_named.PNG)

3. Browse and select the path where the new workspace will be created.

4. Select the platform type(Mobile/Wearable/TV) and version of the project to be imported, then click OK.

5. The Visual Studio window with newly imported project appears on the Solution Explorer.

   ![Visual Studio screen](media/import_project_screen.PNG)

