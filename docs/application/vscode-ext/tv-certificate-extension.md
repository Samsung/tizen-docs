# Install TV extension & certificate extenstion guide

This function provides a step-by-step guide to installing TV and certificate extensions using the Tizen Studio Package Manager.

## Installing Required Extensions

You can install the required extensions using the online repository. If your firewall settings do not allow you to access the repository, you can also install the extensions from local images.

To install the extensions using the online repository:

1. Open the Package Manager: **Tizen Extension > Package Manger**. The Package Manager window opens.

    ![Open package manager](media/package-manager-ui.png)


2. In the Package Manager, select the "Extension SDK" tab.

    ![Extension SDK tab](media/package-manager-1.png)

3. Click "install" next to TV Extensions-<version> and "Samsung Certificate Extension".

    ![Required extensions](media/package-manager-2.png)

4. Accept the software licenses.
The licenses contain important legal notices. Read them in full, and click "Accept All" only if you agree with the license statements.

5. Wait while the extensions are installed.

    ![Extensions installing](media/package-manager-3.png)

To install the extensions from local images:

1. Dowanload the following images:
    * [Samsung TV Extensions](https://developer.samsung.com/smarttv/develop/tools/tv-extension/download.html)
    * [Samsung Certificate Extension (direct download)](https://d3unf4s5rp9dfh.cloudfront.net/SmartTV_doc/tizen-certificate-extension_2.0.11.zip)

2. In the Package Manager, click "Configuration"

    ![Configuration button](media/package-manager-4.png)

3. Unfold the Extension SDK configuration panel by clicking "Extension SDK" at the bottom of the dialog box.

    ![Unfold Extension SDK Panel](media/package-manager-5.png)

4. To add a local image, click "+".

    ![Add button](media/package-manager-6.png)

    The "Add Repository" dialog opens.

5. Enter values to the "Name" and "Repository" fields.
    Enter the full path of the SDK image file in the "Repository" box, or click "..." next to the field to open the file browser and select the image file.

6. Click "OK" to close the "Add Repository" dialog.

    ![Add Repository Dialog](media/package-manager-7.png)

    When you select the image file in the repository list, the image's origin information is displayed.

7. Click "OK" to confirm.

    ![Confirm added images](media/package-manager-8.png)

8. Select the "Extension SDK" tab.

9. Click "Install" next to the added extensions.

10. Accept the software licenses.
The licenses contain important legal notices. Read them in full, and click "Accept" only if you agree with the license statements.

11. Wait while the extensions are installed.

Through the Tizen Studio Package Manager, you can also [update the SDK tools](https://developer.samsung.com/SmartTV/develop/getting-started/setting-up-sdk/installing-tv-sdk/updating-tv-sdk.html) or [uninstall them](https://developer.samsung.com/SmartTV/develop/getting-started/setting-up-sdk/installing-tv-sdk/uninstalling-tv-sdk.html).
