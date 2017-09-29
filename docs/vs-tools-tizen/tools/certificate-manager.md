## Certificate Manager ##

Before installing your applications on a device or submitting it to the Tizen Store, it must be signed with a certificate profile. The certificate ensures the source of the application and makes sure it has not been tampered with since its publication. A certificate profile consists of author and distributor certificates. They can be made in Certificate Manager and they can be managed in Tools > Options > Tizen > Certification. The certificates can be created, edited, removed, and set as active in the Certificate Manager. The active certificates are used when packaging your application.

In Visual Studio Tools for Tizen, the certification can be defined in the following ways:

### Using the default certificate ###
   * If you do not need to upload your application to the Tizen Store, you can use a default certificate and deploy your application in the Tizen Emulator. For using this option, set the certification as illustrated in the following figure.

   ![Using the default certificate](../image/CertificateMgr_defaultcert.png)

### Using an existing certificate profile ###
   * If you have used Tizen Studio and have already generated a certificate profile using the Tizen Certificate Manager, it can be imported in Tools > Options > Tizen > Certification. If you create a Certificate Profile using the ```Tizen Certificate Manager```, it is set as default automatically.

   ![Using an existing certificate profile](../image/CertificateMgr_certificateprofile.png)

### Using your own certificate ###
   * If you already have author and distributor certificates, you can import them in Menu > Tools > Options > Tizen > Certification.

   ![Using your own certificate](../image/CertificateMgr_directcert.png)

## Certificate Profile and Certificates ##
The certificate profile consists of an author certificate and 1 or 2 distributor certificates. To distribute your application, you must create a certificate profile and sign the application with it:

   * An author certificate includes information about the author of the application. It is used to create an author signature, which ensures the integrity of the application from the author since the publication of the application.
   * A distributor certificate includes information about the distributor of the application, such as a store. It is used to create a distributor signature, which ensures the integrity of the application from the distributor since the distribution of the application.

### Creating the Certificate Profile ###

You can create a new certificate profile with the Certificate Manager. To run the Certificate Manager, in the Visual Studio menu, select Tools > Tizen > Tizen Certificate Manager.

![Run Certicate Manager](../image/CertificateMgr_menu.png)

In the Certificate Manager, click the plus icon (Plus icon) to create a new profile.

![Generate Certificate Stpe #1](../image/CertificateMgr_step1.png)

You can create a new certificate profile with the creation wizard.

![Generate Certificate Stpe #2](../image/CertificateMgr_step2.png)

### Adding the Author and Distributor Certificates ###

To add author and distributor certificates:

1. Create a new author certificate or use a previously created author certificate.

![Generate Certificate Stpe #3](../image/CertificateMgr_step3.png)

2. Fill in the required information.

![Generate Certificate Stpe #4](../image/CertificateMgr_step4.png)

3. You can use the default Tizen distributor certificate or another distributor certificate if you have one. In general, the default Tizen distributor certificate is used and you do not need to modify distributor certificates. You can also select the privilege level of the distributor certificate (in native and Web applications)).

![Generate Certificate Stpe #5](../image/CertificateMgr_step5.png)

### Managing the Certificate Profile ###

You can also view, edit, and remove the certificate profiles you have created.

![Generate Certificate Stpe #6](../image/CertificateMgr_step6.png)

To manage a certificate profile:

* Click the info icon (![Info](../image/CertificateMgr_infoicon.png)) to see detailed information of the certificate.

![Generate Certificate Stpe #7](../image/CertificateMgr_step7.png)

* Click the pencil icon (![Pencil](../image/CertificateMgr_infopencil.png)) to change the author or distributor certificate of the selected certificate profile.

![Generate Certificate Stpe #8](../image/CertificateMgr_step8.png)

* Click the trash icon (![Trash](../image/CertificateMgr_infotrash.png)) to remove the selected certificate profile.

![Generate Certificate Stpe #9](../image/CertificateMgr_step9.png)

* The active profile is used when you package your application. Click the check icon to set the selected certificate profile as active. The active profile is also set in Tools > Options > Tizen > Certification automatically.