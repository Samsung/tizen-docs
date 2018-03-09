# Managing Tizen Projects with Project Explorer View

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

<a name="opening"></a>
## Opening the Project Explorer View

Usually, the **Project Explorer** view is located in the upper-left side of the Tizen Studio. You can change the position by dragging and dropping it. If you close the view, you can show it again by selecting **Project Explorer** in **Window > Show View > Other > General**.

**Figure: Opening the view**

![Opening the view](./media/proj_explorer_general.png)

<a name="view"></a>
## Using the Project Explorer View

The files that you select in the **Project Explorer** view affect the information that is displayed in the other views. You can execute and set some operations and configurations by clicking the icons (![Toolbar icons](./media/proj_explorer_op_config.png)) in the toolbar.

**Figure: Executing operations**

![Executing operations](./media/proj_explorer_right_click_w.png)

To execute operations, such as copying, moving, creating new resources, and comparing resources with each other, right-click on any resource in the **Project Explorer** view, and select the desired action in the context menu. The items in the context menu depend on the focused item. Different folder and file types have different action options.

**Table: Project Explorer toolbar**
<table>
	<thead>
		<tr>
			<th>Icon</th>
			<th>Name</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center"><img alt="Collapse all" src="/sites/default/files/images/proj_explorer_collapse.png" /></td>
			<td><strong>Collapse all</strong></td>
			<td>Collapses the tree expansion state of all resources in the view.</td>
		</tr>
		<tr>
			<td align="center"><img alt="Link with editor" src="/sites/default/files/images/proj_explorer_link.png" /></td>
			<td><strong>Link with editor</strong></td>
			<td>Toggles whether the view selection is linked to the active editor. When this option is selected, changing the active editor automatically updates the selection to the resource being edited.</td>
		</tr>
		<tr>
			<td align="center"><img alt="Menu" src="/sites/default/files/images/proj_explorer_menu.png" /></td>
			<td><strong>Menu</strong></td>
			<td>Click the icon to open a menu of items specific to the view:
			<ul>
				<li><strong>Project Presentation</strong>
				<p>Display projects in a flat or hierarchical form.</p>
				</li>
				<li><strong>Top Level Elements</strong>
				<p>Show working sets or projects as top-level elements. Choosing working sets allows easy grouping of projects in large workspaces.</p>
				</li>
				<li><strong>Folder Presentation</strong>
				<p>Display folders in a flat or grouped form.</p>
				</li>
				<li><strong>Select Working Set</strong>
				<p>Open a dialog to select a working set for the view.</p>
				</li>
				<li><strong>Deselect Working Set</strong>
				<p>Deselect the current working set.</p>
				</li>
				<li><strong>Edit Active Working Set</strong>
				<p>Open a dialog to change the current working set.</p>
				</li>
				<li><strong>Customize View</strong>
				<p>Allow customization of view filters and content modules. The filters allow you to suppress the display of certain types of files while the content modules allow entirely new types of content to be shown in the view.</p>
				</li>
				<li><strong>Link Editor</strong>
				<p>See the toolbar item description above.</p>
				</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>

**Table: Project Explorer context menu**
<table>
	<thead>
		<tr>
			<th>Menu</th>
			<th>Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><strong>New</strong></td>
			<td>Allows you to create a new resource in the workbench. Select the type of resource to create from the submenu.</td>
		</tr>
		<tr>
			<td><strong>Copy</strong></td>
			<td>Copies the selected resource to the clipboard.</td>
		</tr>
		<tr>
			<td><strong>Paste</strong></td>
			<td>Pastes resources on the clipboard into the selected project or folder. If a resource is selected, the resources on the clipboard are pasted as siblings of the selected resource.</td>
		</tr>
		<tr>
			<td><strong>Delete</strong></td>
			<td>Deletes the selected resource from the workspace.</td>
		</tr>
		<tr>
			<td><strong>Move</strong></td>
			<td>Moves the selected resource to another location. A dialog appears, prompting for the destination location to which the resource are to be moved.</td>
		</tr>
		<tr>
			<td><strong>Rename</strong></td>
			<td>Allows you to specify a new name for the selected resource.</td>
		</tr>
		<tr>
			<td><strong>Import</strong></td>
			<td>Opens the import wizard and allows you to select the resources to import into the workbench.</td>
		</tr>
		<tr>
			<td><strong>Export</strong></td>
			<td>Opens the export wizard and allows you to export the resources to an external location.</td>
		</tr>
		<tr>
			<td><strong>Export to CLI project</strong></td>
			<td>Exports the Tizen Studio native project to a CLI (command line interface) project. This option also makes or converts some files.</td>
		</tr>
		<tr>
			<td><strong>Build Signed Package</strong></td>
			<td>Makes a 'signed' package. This option requires a certificate profile. You can create a certificate profile in <strong>Tools</strong> &gt; <strong>Certificate Manager</strong>.</td>
		</tr>
		<tr>
			<td><strong>Localization</strong></td>
			<td>Opens the localization view and allows you to add or update languages and localize the string or resources.</td>
		</tr>
		<tr>
			<td><strong>Refresh</strong></td>
			<td>Refreshes the <strong>Workbench</strong> view of the selected resource and its children. For example, this is used when you create a new file for an existing project outside the <strong>Workbench</strong> and want the file to appear in the <strong>Project Explorer</strong> view.</td>
		</tr>
		<tr>
			<td><strong>Close Project</strong></td>
			<td>Closes the selected project (visible when an open project is selected).</td>
		</tr>
		<tr>
			<td><strong>Close Unrelated Projects</strong></td>
			<td>Closes any project unrelated to the selected project.</td>
		</tr>
		<tr>
			<td><strong>Open Project</strong></td>
			<td>Opens the selected project (visible when a closed project is selected).</td>
		</tr>
		<tr>
			<td><strong>Team</strong></td>
			<td>Menu items in the <strong>Team</strong> sub-menu are related to version control management and are determined by the version control management system that is associated with the project. Eclipse provides the special menu item <strong>Share Project...</strong> for projects that are not under version control management. This command presents a wizard that allows you to share the project with any version control management systems that have been added to Eclipse. Eclipse ships with support for CVS.</td>
		</tr>
		<tr>
			<td><strong>Compare With</strong></td>
			<td>Allows you to do one of the following types of compares:
			<ul>
				<li>Compare 2 or 3 selected resources with each other.</li>
				<li>Compare the selected resource with remote versions (if the project is associated with a version control management system).</li>
				<li>Compare the selected resource with a local history state.</li>
			</ul>
			After you select the type of compare you want to do, you either see a compare editor or a compare dialog. In the compare editor, you can browse and copy various changes between the compared resources. In the compare dialog, you can only browse through the changes.</td>
		</tr>
		<tr>
			<td><strong>Replace With</strong></td>
			<td>Allows you to replace the selected resource with another state from the local history. If the project is under version control management, there can be additional items supplied by the version control management system as well.</td>
		</tr>
		<tr>
			<td><strong>Properties</strong></td>
			<td>Displays the properties of the selected resource. The displayed properties depend on what type of resource is selected. Resource properties can include (but are not limited to):
			<ul>
				<li>Path relative to the project in which it is held</li>
				<li>Type of the resource</li>
				<li>Absolute file system path, or name of the path variable when using linked resources</li>
				<li>Resolved path variable when using a path variable for a linked resource</li>
				<li>Size of the resource</li>
				<li>Last modified date</li>
				<li>Read-only status</li>
				<li>Derived resource status</li>
				<li>Execution arguments, if it is an executable resource</li>
				<li>Program launchers, if it is able to be launched</li>
				<li>Project dependencies, if any</li>
			</ul>
			</td>
		</tr>
	</tbody>
</table>



## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
