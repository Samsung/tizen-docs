# Emulator Manager

You can use emulators to run your application in a virtual environment.

In order to test the application in a variety of environments, you need a variety of emulators. The Emulator Manager helps you easily create and manage emulator instances. Basically, the Emulator Manager allows you to generate emulator instances from a predefined platform and template. In addition, you can define the settings of the virtual device, such as skin, resolution, and hardware devices.

The main features of the Emulator Manager are:

- Defining a new emulator instance or hardware profile
- Editing an existing emulator instance or hardware profile
- Deleting an emulator instance or hardware profile
- Starting and stopping the emulator instance


## Accessing the Emulator Manager

If you do not have the Emulator Manager installed, you can install it using the Visual Studio Tools for Tizen installer.

There are 2 different ways to access the Emulator Manager from Visual Studio:

- In the Visual Studio menu, go to **Tools &gt; Tizen &gt; Tizen Emulator Manager**.

    **Figure: Launch the Emulator Manager in the Tools menu**

    ![Launch the Emulator Manager in the Tools menu](media/em-vstoolbar1.png)

-   On the Visual Studio toolbar, click **Launch Tizen Emulator**.

    **Figure: Launch the Emulator Manager in Visual Studio**

    ![Launch from the Visual Studio toolbar](media/em-vstoolbar2.png)


<a name="create"></a>
## Creating Emulator Instances

The Emulator Manager can help you to select the recommended platform and template. When you need another device environment, you can edit an existing emulator instance, or create a new one with a more suitable platform and template. You can also create new platforms and templates to suit your needs.

**Figure: Emulator Manager**

![Emulator Manager](media/em-vs1.png)

To create a new emulator instance:

1.  In the Emulator Manager, click **Create**.
2.  Select the platform (system image), and click **Next**.
3.  Select the template (device definition), and click **Next**.
4.  Modify the properties as needed, and click **Finish**.

The emulator instance appears in the Emulator Manager.

To view the emulator instance details, right-click the instance and select **Detail**.

> **Note**  
> To run the application faster, switch on CPU VT and GPU. If CPU VT is disabled, see [Increasing the Application Execution Speed](../../tizen-studio/common-tools/emulator.md#speed) for more information. If GPU is disabled, install the latest vendor-provided graphic driver.
>
> The mobile emulator supports HD (720x1280) and WVGA (480x800) resolutions.


## Creating Platforms

To create an emulator, you must first select the platform. You can create, modify, and delete a custom platform, and view the generated platforms. Most application developers do not need a custom platform, but it can be useful for a platform developer.

**Figure: Platform list**

![Platform list](media/em-vs3.png)

To create a custom platform:

1. In the Emulator Manager, click **Create**.
2. Click **+**.
3. In the **Platform Configuration** dialog, select a base platform and platform image file.

    You can create a custom platform using a qcow2 or raw format image. Qcow2 is a platform image format that is released with the Tizen Studio. You can also create a qcow2 image by [exporting an emulator](#export).

    A platform image in the development stage is in raw format. If you launch an emulator with a raw image, you can see the current state of the image. This can be useful for platform developers.

4. Click **OK** to save your configuration.

   The new platform is added to the list.

**Figure: Platform Configuration dialog**

![Platform Configuration dialog](media/em-vs4.png)

To manage the created platforms:

- To edit a platform, click **Edit** (![Edit icon](media/em-modify.png)), make the desired changes, and click **OK**. You can only edit the custom platforms you have created.
- To delete a platform, click **Delete** (![Delete icon](media/em-delete.png)). You can only delete the custom platforms you have created.

## Creating Templates

The Emulator Manager provides several device template types. A device template defines, for example, the screen resolution and size, and the sensors in the device specification. You can make an emulator instance based on the desired template.

**Figure: Device templates**

![Device templates](media/em-device-template.png)

You can create a custom template in 2 ways:

1. In the Emulator Manager, click **Create**.
2. Select a platform and click **Next**.
3. To create a new template:
   - To create a new template from the beginning:
     1. Click **+**.
     2. Define the features for the template.
     3. Click **OK**.

        The new template is added to the list with a settings icon.

   - To create a new template based on an existing one:
     1. Select the template you want to clone.
     2. Click **clone template** (![Clone icon](media/em-clone-icon.png)).
     3. Make the desired changes.
     4. Click **OK**.

        The new template is added to the list with a settings icon.

**Figure: Template Configuration dialog**

![Template Configuration dialog](media/em-template-config.png)

To manage the created templates:

- To edit a template, click **edit template** (![Modify icon](media/em-modify.png)), make the desired changes, and click **OK**. You can only edit the custom templates you have created.
- To delete a template, click **delete** (![Delete icon](media/em-delete.png)). You can only delete the custom templates you have created.

## Managing and Launching Emulator Instances

In the Emulator Manager, you can launch, edit, delete, reset, and export emulator instances:

1. Launch the Emulator Manager.
2. Select an emulator instance from the list.
3. Manage the instance:
   - To launch the emulator, click **Launch**.

     The debug and launch options are activated after the emulator has booted. The name of the emulator instance is displayed on the Visual Studio toolbar.

	 ![Launched emulator instance](media/em-launched.png)

     ![Activated debug option](media/em-activated-debug.png)

   - To edit an emulator, click **Edit**, make the desired changes, and click **Confirm**.

   - To delete an emulator, click **Delete**.

   - To reset an emulator, right-click it and select **Reset**.

     <a name="export"></a>
   - To export an emulator, right-click it and select **Export as**. Specify the new image file location.

     When you export the emulator instance, the state of the platform image is replicated.
