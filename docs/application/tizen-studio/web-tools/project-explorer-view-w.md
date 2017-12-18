# Managing Tizen Projects with Project Explorer View
## Dependencies
- Tizen Studio 1.0 and Higher


The **Project Explorer** view allows you to view and manage Tizen projects. You can view and change the resources of a project in the view, and build, export, and convert projects through the view.

**Figure: Project Explorer**

![Project Explorer](./media/proj_explorer_w.png) 

In this view, you can:

- Browse the file elements
- Open files in the editor view
- Open projects in a new window
- Create new projects, classes, files, or folders
- Manage existing files (cut, paste, delete, move, or rename files)
- Restore deleted files from local history
- Import or export files and projects

## Opening the Project Explorer View<a name="opening"></a>

Usually, the **Project Explorer** view is located in the upper-left side of the Tizen Studio. You can change the position by dragging and dropping it. If you close the view, you can show it again by selecting **Project Explorer** in **Window > Show View > Other > General**.

**Figure: Opening the view**

![Opening the view](./media/proj_explorer_general.png) 

## Using the Project Explorer View<a name="view"></a>

The files that you select in the **Project Explorer** view affect the information that is displayed in the other views. You can execute and set some operations and configurations by clicking the icons (![Toolbar icons](./media/proj_explorer_op_config.png)) in the toolbar.

**Figure: Executing operations**

![Executing operations](./media/proj_explorer_right_click_w.png) 

To execute operations, such as copying, moving, creating new resources, and comparing resources with each other, right-click on any resource in the **Project Explorer** view, and select the desired action in the context menu. The items in the context menu depend on the focused item. Different folder and file types have different action options.

**Table: Project Explorer toolbar**

| Icon                                     | Name                 | Description                              |
| ---------------------------------------- | -------------------- | ---------------------------------------- |
| ![Collapse all](./media/proj_explorer_collapse.png) | **Collapse all**     | Collapses the tree expansion state of all resources in the view. |
| ![Link with editor](./media/proj_explorer_link.png) | **Link with editor** | Toggles whether the view selection is linked to the active editor. When this option is selected, changing the active editor automatically updates the selection to the resource being edited. |
| ![Menu](./media/proj_explorer_menu.png) | **Menu**             | Click the icon to open a menu of items specific to the view: <br />**Project Presentation**	 <br />Display projects in a flat or hierarchical form.<br />**Top Level Elements**	 <br />Show working sets or projects as top-level elements. <br />Choosing working sets allows easy grouping of projects in large workspaces.<br />**Folder Presentation**	 <br />Display folders in a flat or grouped form.<br />**Select Working Set**	 <br />Open a dialog to select a working set for the view.<br />**Deselect Working Set**	 <br />Deselect the current working set.<br />**Edit Active Working Set**	 <br />Open a dialog to change the current working set.<br />**Customize View**	<br /> Allow customization of view filters and content modules. The filters allow you to suppress the display of certain types of files while the content modules allow entirely new types of content to be shown in the view.<br />**Link Editor**	<br /> See the toolbar item description above. |



**Table: Project Explorer context menu**

| Menu                         | Description                              |
| ---------------------------- | ---------------------------------------- |
| **New**                      | Allows you to create a new resource in the workbench. Select the type of resource to create from the submenu. |
| **Copy**                     | Copies the selected resource to the clipboard. |
| **Paste**                    | Pastes resources on the clipboard into the selected project or folder. If a resource is selected, the resources on the clipboard are pasted as siblings of the selected resource. |
| **Delete**                   | Deletes the selected resource from the workspace. |
| **Move**                     | Moves the selected resource to another location. A dialog appears, prompting for the destination location to which the resource are to be moved. |
| **Rename**                   | Allows you to specify a new name for the selected resource. |
| **Import**                   | Opens the import wizard and allows you to select the resources to import into the workbench. |
| **Export**                   | Opens the export wizard and allows you to export the resources to an external location. |
| **Export to CLI project**    | Exports the Tizen Studio native project to a CLI (command line interface) project. This option also makes or converts some files. |
| **Build Signed Package**     | Makes a 'signed' package. This option requires a certificate profile. You can create a certificate profile in **Tools > Certificate Manager**. |
| **Localization**             | Opens the localization view and allows you to add or update languages and localize the string or resources. |
| **Refresh**                  | Refreshes the **Workbench** view of the selected resource and its children. For example, this is used when you create a new file for an existing project outside the **Workbench** and want the file to appear in the **Project Explorer** view. |
| **Close Project**            | Closes the selected project (visible when an open project is selected). |
| **Close Unrelated Projects** | Closes any project unrelated to the selected project. |
| **Open Project**             | Opens the selected project (visible when a closed project is selected). |
| **Team**                     | Menu items in the **Team** sub-menu are related to version control management and are determined by the version control management system that is associated with the project. Eclipse provides the special menu item **Share Project...** for projects that are not under version control management. This command presents a wizard that allows you to share the project with any version control management systems that have been added to Eclipse. Eclipse ships with support for CVS. |
| **Compare With**             | Allows you to do one of the following types of compares:  <br />  - Compare 2 or 3 selected resources with each other.<br />  - Compare the selected resource with remote versions (if the project is associated with a version control management system).<br />  - Compare the selected resource with a local history state.	<br />After you select the type of compare you want to do, you either see a compare editor or a compare dialog. In the compare editor, you can browse and copy various changes between the compared resources.  In the compare dialog, you can only browse through the changes. |
| **Replace With**             | Allows you to replace the selected resource with another state from the local history. If the project is under version control management, there can be additional items supplied by the version control management system as well. |
| **Properties**               | Displays the properties of the selected resource. The displayed properties depend on what type of resource is selected. Resource properties can include (but are not limited to):  <br />  - Path relative to the project in which it is held<br />  - Type of the resource<br />  - Absolute file system path, or name of the path variable when using linked resources<br />  - Resolved path variable when using a path variable for a linked resource<br />  - Size of the resource<br />  - Last modified date<br />  - Read-only status<br />  - Derived resource status<br />  - Execution arguments, if it is an executable resource<br />  - Program launchers, if it is able to be launched<br />  - Project dependencies, if any |