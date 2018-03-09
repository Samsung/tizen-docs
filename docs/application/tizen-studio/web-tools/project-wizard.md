# Creating Tizen Projects with Tizen Project Wizard

The Tizen Project Wizard is a Tizen Studio tool that is used to create a Web application project.

The Tizen Studio provides various project templates and samples that make it easier for you to start coding your application. When you create a new project, you can select a specific template, which the Tizen Project Wizard uses to automatically create basic functionalities for the application. The default project files and folders are also created.

In the Tizen Project Wizard, you can select a profile and version, application type, and template or sample to create the project. In addition, you can set basic project properties, such as the project name, location, and working sets.

To open the Tizen Project Wizard, use one of the following:

- In the Tizen Studio menu, select **File > New > Tizen Project**.
- In the Tizen Studio toolbar, click the **New** icon (![New icon](./media/project_wizard_icon_new.png)).
- Right-click in the **Project Explorer** view, and select **New > Tizen Project**.
- If there is no project in the workspace, click the **New** icon (![New icon](./media/project_wizard_icon_new.png)) in the **Project Explorer** view toolbar.

<a name="type"></a>
## Project Type

When the Tizen Project Wizard opens, you must first select the project type.

**Figure: Selecting the project type**

![Selecting the project type](./media/project_wizard_type.png)

The Tizen Studio provides various project templates and samples for mobile and wearable devices according to the installed platform. The Tizen Project Wizard helps you select a template or sample for your project.

The **Template** option provides a list of templates with a basic structure where you can start the Web application project:

- **Common**

  - **Basic UI**: Empty template project for developing basic UI applications.

- **Mobile**

  - **TAU MasterDetail**: Empty template project for developing UI applications using TAU (Tizen Web UI Framework).  
  - **TAU MultiPage/SinglePage**: Empty template projects for developing multiple page and single page applications using TAU.

- **Wearable**

  - **TAU Basic**: Empty template project for developing basic circular UI applications using TAU.  
  - **TAU List**: Empty template project for developing UI applications using a TAU list.  
  - **Web Input Method Editor**: Empty template project for developing Web-based IME (Input Method Editor) applications using HTML, CSS, and JavaScript code.  
  - **Widget**: Empty template project for developing widget applications.

The **Sample** option provides a list of sample applications demonstrating various API usage and UI design.

To move to the next step, select the project type and click **Next**.

<a name="version"></a>
## Profile and Version

You can select the profile and version supported by your project, such as a mobile or wearable device. In addition, the Tizen Studio shows you which platforms among the supported platforms have been installed.

Based on the selected profile and version, a list of templates is shown in the template selection step.

**Figure: Selecting the profile and version**

![File analysis](./media/project_wizard_profile.png)

To move to the next step, select the profile and version, and click **Next**.

<a name="app_type"></a>
## Application Type

You can select the Web or native application type for your project. For more information, see [Web Application](../../web/index.md) and [Native Application](../../native/index.md).

Based on the selected application type, a list of templates is shown in the template selection step.

**Figure: Selecting the application type**

![Selecting the application type](./media/project_wizard_app_type_w.png)

To move to the next step, select the application type and click **Next**.

<a name="template"></a>
## Template

You can select the template for your project while viewing information about a variety of templates. The Tizen Project Wizard creates the project based on the selected template.

**Figure: Selecting the template**

![Selecting the template](./media/project_wizard_template_w.png)

To move to the next step, select the template and click **Next**.

<a name="properties"></a>
## Project Properties

You can set basic project properties, such as the project name, location, and working sets.

**Figure: Setting project properties**

![Setting project properties](./media/project_wizard_properties_w.png)

The options you can set are listed in the following table.

**Table: Project properties**

| Property                 | Description                              |
|------------------------|----------------------------------------|
| **Project name**         | A name for the project to be created.    |
| **Use default location** | If you check this option, the project is created in the `$<workspace_location>/<project_name>` directory. |
| **Location**             | Manually select the location of the project.<br> If you check the **Use default location** checkbox, this option is disabled. |
| **Working sets**         | If you want to include the project to a specific working set, select a [working set](http://help.eclipse.org/mars/index.jsp?topic=%2Forg.eclipse.platform.doc.user%2Fconcepts%2Fcworkset.htm). |

After specifying the options, click **Finish** to create the new project.

## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
