# Managing Emulator Instances

You can use emulators to run your application in a virtual environment.

In order to test the application in a variety of environments, you need a variety of emulators. The Emulator Manager helps you easily create and manage emulator instances. Basically, the Emulator Manager allows you to generate emulator instances from a predefined platform and template. In addition, you can define the settings of the virtual device, such as skin, resolution, and hardware devices.

The main features of the Emulator Manager are:
- Defining a new emulator instance or hardware profile
- Editing an existing emulator instance or hardware profile
- Deleting an emulator instance or hardware profile
- Starting and stopping the emulator instance

<a name="access"></a>
## Accessing the Emulator Manager

If you do not have the Emulator Manager installed, you can install it using the Tizen Studio Package Manager.

There are 2 different ways to access the Emulator Manager:

- Click the Emulator Manager icon on the desktop or in the Start menu.

  **Table: Starting the Emulator Manager**

  | Ubuntu                                   | Windows&reg;                                 | macOS                                    |
  |----------------------------------------|----------------------------------------|----------------------------------------|
  | **Desktop > Applications > Emulator Manager:** <br> ![Shortcut Ubuntu](./media/emulator_manager_linux_shortcut.png) | **Start > All Programs > Tizen Studio > Emulator Manager:** <br> ![Shortcut Windows](./media/emulator_manager_win_shortcut.png) | **Finder > Applications > Tizen Studio > Emulator Manager:** <br> ![Shortcut macOS](./media/emulator_manager_mac_shortcut.png) |

- In the Tizen Studio, select **Tools > Emulator Manager** or click the Emulator Manager icon on the toolbar.

  **Figure: Launch the Emulator Manager in the Tizen Studio**

  ![Launch the Emulator Manager](./media/emulator_manager_launch.png)

<a name="create"></a>
## Creating an Emulator Instance

The Emulator Manager can help you to select the recommended platform and template. When you need another device environment, you can edit an existing emulator instance, or create a new one with a more suitable platform and template. You can also create new platforms and templates to suit your needs.

**Figure: Emulator Manager**

![Emulator Manager](./media/emulator_manager_common.png)

To create a new emulator instance:

1. In the Emulator Manager, click **Create**.

2. Select the platform (system image), and click **Next**.

3. Select the template (device definition), and click **Next**.

4. Modify the properties as needed, and click **Finish**.

   The emulator instance appears in the Emulator Manager.

   To view the emulator instance details, right-click the instance and select **Detail**.

   > **Note**  
   > To run the application faster, switch on CPU VT and GPU. If CPU VT is disabled, check [Increasing the Application Execution Speed](emulator.md#speed) for more information. If GPU is disabled, [install the latest vendor-provided graphic driver](../setup/prerequisites.md#emulator).

### Creating Platforms

To create an emulator, you must first select the platform. You can create, modify, and delete a custom platform, and view the generated platforms. Most application developers do not need a custom platform, but it can be useful for a platform developer.

**Figure: Platform list**

![Platform list](./media/emulator_manager_platforms.png)

To create a custom platform:

1. In the Emulator Manager, click **Create**.

2. Click **+**.

3. In the **Platform Configuration** dialog, select a base platform and platform image file.

   You can create a custom platform using a qcow2 or raw format image. Qcow2 is a platform image format that is released with the Tizen Studio. You can also create a qcow2 image by [exporting an emulator](#export).

   A platform image in the development stage is in raw format. If you launch an emulator with a raw image, you can see the current state of the image. This can be useful for platform developers.

4. Click **OK** to save your configuration.

   The new platform is added to the list.

   **Figure: Platform Configuration dialog**

   ![Platform Configuration dialog](./media/emulator_manager_platform_config.png)

To manage the created platforms:

- To edit a platform, click **Edit** (![Edit platform](./media/emulator_manager_modify.png)), make the desired changes, and click **OK**. You can only edit the custom platforms you have created.
- To delete a platform, click **Delete** (![Delete](./media/emulator_manager_delete.png)). You can only delete the custom platforms you have created.

### Creating Templates

The Emulator Manager provides several device template types. A device template defines, for example, the screen resolution and size, and the sensors in the device specification. You can make an emulator instance based on the desired template.

**Figure: Device templates**

![Device templates](./media/emulator_manager_device_template.png)

You can create a custom template in 2 ways:

1. In the Emulator Manager, click **Create**.

2. Select a platform and click **Next**.

3. To create a new template:

   - To create a new template from the beginning:
     1. Click **+**.
     2. Define the features for the template.
     3. Click **OK**.The new template is added to the list with a settings icon.

   - To create a new template based on an existing one:
     1. Select the template you want to clone.
     2. Click **clone template** (![Clone icon](./media/emulator_manager_clone.png)).
     3. Make the desired changes.
     4. Click **OK**.  
        The new template is added to the list with a settings icon.

        **Figure: Template Configuration dialog**

        ![Template Configuration dialog](./media/emulator_manager_template_config.png)

To manage the created templates:

- To edit a template, click **edit template** (![Edit template](./media/emulator_manager_modify.png)), make the desired changes, and click **OK**. You can only edit the custom templates you have created.
- To delete a template, click **delete** (![Delete](./media/emulator_manager_delete.png)). You can only delete the custom templates you have created.

<a name="manage"></a>
## Managing and Launching Emulator Instances

In the Emulator Manager, you can launch, edit, delete, reset, and export emulator instances:

1. Launch the Emulator Manager.

2. Select an emulator instance from the list.

3. Manage the instance:
   - To launch the emulator, click **Launch**.
   - To edit an emulator, click **Edit**, make the desired changes, and click **Confirm**.
   - To delete an emulator, click **Delete**.
   - To reset an emulator, right-click it and select **Reset**.
     <a name="export"></a>
   - To export an emulator, right-click it and select **Export as**. Specify the new image file location.  
     When you export the emulator instance, the state of the platform image is replicated.

<a name="control"></a>
## Controlling the Emulator Manager from the Command Line

You can create, modify, delete, and list your VMs through the command line interface commands. The CLI binary is located in:

- Ubuntu:

  `<TIZEN_STUDIO>/tools/emulator/bin/em-cli`

- Windows&reg;:

  `<TIZEN_STUDIO>\tools\emulator\bin\em-cli.bat`

For more information, see the CLI help messages.

**Figure: Emulator Manager command line**

![Emulator Manager command line](./media/emulator_manager_cli.png)

In the following figure, you can see the details of a specific command using the `-h` command option.

**Figure: Emulator Manager command details**

![Emulator Manager command details](./media/emulator_manager_cli_detail.png)

The following figure shows an example of how to create and launch an emulator using the CLI.

**Figure: Launching the emulator using the command line**

![Launching the emulator using the command line](./media/emulator_manager_cli_create.png)

In the `create` command, the `–p` option is the platform name. You can see the available platforms using the `list -vm` command.

## Related information
* Dependencies
  - Tizen Studio 1.0 and Higher
