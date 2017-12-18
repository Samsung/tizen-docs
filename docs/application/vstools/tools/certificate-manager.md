# Certificate Manager

Before installing your application on a device or submitting it to the Tizen Store, it must be signed with a certificate profile. The signature verifies the source of the application and makes sure it has not been tampered with since its publication. A certificate profile is a combination of the certificates used for signing.

You can use the Certificate Manager to create, edit, and remove certificates, and set them as active. The active certificates are used when packaging your application.

## Selecting the Certificate Profile

To select the certificates used to package your application:

1. In the Visual Studio menu, go to **Tools &gt; Options &gt; Tizen &gt; Certification**.
2. Define the certificates in one of the following ways:

   - **Using the default certificate**  
     If you do not need to upload your application to the Tizen Store, you can use a default certificate and deploy your application in the Tizen Emulator for testing purposes.  
	 To use the default certificates, uncheck the **Sign the .TPK file using the following option.** checkbox.

     ![Using the default certificate](media/certificatemgr-defaultcert.png)

   - **Using an existing certificate profile**  
     If you have used the Tizen Studio before and have already generated a certificate profile using the Tizen Certificate Manager, you can import the profile by selecting **Use profile of Tizen Certificate Manager** from the drop-down list.  
     If you want to create a new certificate profile with the Certificate Manager, see [Creating a Certificate Profile](#creating-a-certificate-profile). The new profile is then set as default automatically.

     ![Using an existing certificate profile](media/certificatemgr-certificateprofile.png)

   - **Using your own certificate**  
     If you already have author and distributor certificates from another application store, you can import them by selecting **Direct registration** from the drop-down list and entering the required information.



     ![Using your own certificate](media/certificatemgr-directcert.png)
3. Click **OK**.

## Creating a Certificate Profile

A certificate profile consists of an author certificate and 1 or 2 distributor certificates:

- An author certificate includes information about the author of the application. It is used to create an author signature, which ensures the integrity of the application from the author since the publication of the application.
- A distributor certificate includes information about the distributor of the application, such as a store. It is used to create a distributor signature, which ensures the integrity of the application from the distributor since the distribution of the application.


To distribute your application, you must create a certificate profile and sign the application with it. You can create a new certificate profile with the Certificate Manager:

1. In the Visual Studio menu, select **Tools &gt; Tizen &gt; Tizen Certificate Manager**.

2. In the Certificate Manager, click **+** to create a new profile.

   ![Generating a certificate profile](media/certificatemgr-step1.png)

3. Enter a name for the profile and click **Next**.

   ![Certificate creation wizard](media/certificatemgr-step2.png)

4. Add the author and distributor certificates:

   1. Select whether to create a new author certificate or use a previously created author certificate, and click **Next**.

      ![Creating the author certificate](media/certificatemgr-step3.png)

      Define the existing author certificate or enter the required information for a new certificate, and click **Next**.

      ![Entering the author certificate information](media/certificatemgr-step4.png)

   2. You can use the default Tizen distributor certificate or another distributor certificate if you have one. In general, the default Tizen distributor certificate is used and you do not need to modify distributor certificates. You can also select the privilege level of the distributor certificate (for native and Web applications)).

      ![Creating the distributor certificate](media/certificatemgr-step5.png)
	  
5. Click **Finish**.

## Managing Certificate Profiles

You can view, edit, and remove the certificate profiles you have created in the Certificate Manager.

**Figure: Managing certificate profiles**

![Managing certificate profiles](media/certificatemgr-step6.png)

To manage a certificate profile:

- To see the details of an individual certificate within the selected certificate profile, click the info button (![Info icon](media/certificatemgr-infoicon.png)).

  ![Certificate information](media/certificatemgr-step7.png)

- To change the author or distributor certificate of the selected certificate profile, click the pencil button (![Pencil icon](media/certificatemgr-infopencil.png)).

  ![Change certificate](media/certificatemgr-step8.png)

- To remove the selected certificate profile, click the trash button (![Trash icon](media/certificatemgr-infotrash.png)).

- To set the selected certificate profile as active, click the check button (![Check icon](media/certificatemgr-infocheck.png)).

  The active profile is used when you package your application. The active profile is also automatically set in **Tools &gt; Options &gt; Tizen &gt; Certification**.

  ![Remove certificate](media/certificatemgr-step9.png)