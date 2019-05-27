# Setting up SmartThings Cloud

To develop applications that integrate with the SmartThings Cloud, you must register the function of your device (called a resource or capability in the SmartThings Cloud) and generate a private key and a cloud certificate.

## Registering your Device

To register the function of your device:

1.  Create a cloud-connected device in the Developer Workspace site (<https://smartthings.developer.samsung.com/>), by following the instructions on the [SmartThings Developers site](https://smartthings.developer.samsung.com/docs/workspace/tutorials/create-a-cloud-connected-device.html):

    -   Choose the **SmartApp Connector** type of Cloud Connector

        ![Web Console Project Example](media/devworkspace_project.png)

2.  After the cloud-connected device is created, add a device profile by following the instructions on the [SmartThings Developers site](https://smartthings.developer.samsung.com/docs/workspace/tutorials/add-a-device-profile.html)

    For more information, see [Developing Applications with Things SDK API](things-app-development-5.0.md).

## Generating Cloud Certificates

SmartThings&trade; uses OpenSSL for security. To begin development, you need to get certificates for both plugins (PPK) and devices. For instructions on installing OpenSSL, see the OpenSSL documentation.

Generate the IoT certificate and private key using the Certificate Manager:

1.  In Tizen Studio menu, open the Certificate Manager by going to **Tools &gt; Certificate Manager**.

    ![Certificate Manager menu Item](media/certificate_manager_menu_item.png)

2.  In the Tizen Certificate Manager window, select the **IoT Cloud Service** tab and click **+** to create a new certificate and key pair.

    ![Certificate Manager IoT Tab](media/cm_iot_tab.png)

3.  Fill the requested information in the Certificate Generation Dialog and click **OK**.

    ![Certificate Generation Dialog](media/certificate_generation_dialog.png)

4.  In the next page of Certificate Generation Dialog, fill the requested Device and Manufacturer information and click **OK**.

    ![Certificate Generation Dialog](media/certificate_generation_device_dialog.png)
   
   > **NOTE**
   > 
   > "Device Name" must be the same as the "device name", which you define in `master.json`.

5.  Sign in to Samsung account.

    ![Samsung account sign-in](media/samsung_sign_in.png)

6.  Once you have signed in successfully, you can see the generated certificate and private key in the **Certificate Profile** list.

    ![Certificate List](media/certificate_list.png)

## Using the Generated IoT certificate

The IoT certificate and key pair generated in the previous section needs to be copied to the application in a designated directory. This enables the device to connect to the SmartThings cloud using the IoT certificate.

To add the IoT certificate to the application:

1.  In Tizen Studio **Project Explorer** view, **right-click** the project and select **Build Signed Package**.

    ![Build signed package](media/build_signed_package.png)

2.  The certificate and private key must be copied to the **res** folder of the application.

    ![Certificate in res folder](media/res_certificate.png)
