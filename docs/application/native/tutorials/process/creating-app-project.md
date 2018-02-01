# Creating the Application Project

You can create a native application project by selecting from a variety of templates and samples. The following instructions are specific for creating the project with a template.

To create a native application project:

1. In the Tizen Studio, select **File > New > Tizen Project**.  
![Creating a new project](media/create_project_1.png)

 The Project Wizard opens.

2. In the Project Wizard, define the project details.

   The Project Wizard is used to create the basic application skeleton with the required folder structure and mandatory files. You can easily create different applications by selecting an applicable template or sample for the Project Wizard to use.

   a. Select the **Template** project type and click **Next**.

      ![Selecting the project type](media/create_project_wizard_type.png)

   b. Select the profile (**Mobile** or **Wearable**) and version from a drop-down list and click **Next**.

      ![Selecting the profile and version](media/create_project_wizard_version_wearable.png)

   c. Select the **Native Application** application type and click **Next**.

      ![Selecting the application type](media/create_project_wizard_app_wearable.png)

   d. Select the template you want to use and click **Next**.

      ![Selecting the template](media/create_project_wizard_template_wn.png)

   e. Define the project properties and click **Finish**.

      You can fill the project name. You can also select the location and working sets by clicking **More properties**.

      > **Note**  
      > The Tizen API names cannot be used as project names. The project name must be more than 2 characters and is restricted to the following regular expression: [a-zA-Z][a-zA-Z0-9-]{2,49}.

      ![Defining properties](media/create_project_wizard_properties_wn.png)

      The Project Wizard sets up the project, creates the application files using the default content from the template, and closes. For more information on the Project Wizard and the available templates, see [Creating Tizen Projects with Tizen Project Wizard](../../../tizen-studio/native-tools/project-wizard.md).

The new application project is shown in the **Project Explorer** view of the Tizen Studio, with default content in the `tizen-manifest.xml` file as well as in several project folders.

## Importing a Project

If you have an existing Tizen application project, you can import it into the Tizen Studio:

1. In the Tizen Studio menu, go to **File > Import > Tizen > Tizen Project**, and click **Next**.
2. Select the location of the root directory or archive file of the Tizen project and click **Next**.
3. If you want to convert the project profile and version, use the **Profile/Version** combo box.
4. Click **Finish**.

The project appears in the **Project Explorer** view.
