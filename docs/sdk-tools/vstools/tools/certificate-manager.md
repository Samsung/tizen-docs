# Certificate Manager

Every Tizen application must be signed before deployment or Store submission. A certificate profile contains an author certificate that identifies the developer and one or more distributor certificates that authorize distribution.

Open Certificate Manager from **Tools > Tizen > Tizen Certificate Manager**.

![Certificate Manager](media/certificate_manager.png)

## Selecting the Certificates

To select the certificates used to package your application:

1. In the Visual Studio menu, go to **Tools > Options > Tizen > Certification**.
2. Define the certificates in one of the following ways:
   - **Using the default certificates**

     If you do not need to upload your application to the store, you can use a default certificate and deploy your application in the Tizen Emulator for testing purposes.

     To use the default certificates, uncheck the **Sign the .TPK file using the following option.** checkbox.

     ![Use default certificates](media/vstools_cert_default.png)

   - **Using an existing certificate profile**

     If you have used Tizen Studio before and have already generated a certificate profile using the Tizen Certificate Manager, you can import the profile by selecting **Use profile of Tizen Certificate Manager** from the drop-down list.

     If you want to create a new certificate profile, see [Create a certificate profile](#create-a-certificate-profile).

     ![Use existing certificate profile](media/vstools_cert_profile1.png)

   - **Using your own certificates**

     If you already have author and distributor certificates from another application store, you can import them by selecting **Direct registration** from the drop-down list and entering the required information.

     ![Use own certificates](media/vstools_cert_certificate1.png)

3. Select **OK**.

## Create a Certificate Profile

1. Select **Create a new Certificate**.

   ![Create a new Certificate button](media/certificate_manager_create_new_certificate_highlighted.png)

2. Enter a profile name and choose either **Tizen** or **Samsung** as the certificate type.

   ![Enter the certificate profile information](media/certificate_profile_information.png)

3. Enter the author information, such as your name and organization.

   ![Enter author certificate details](media/certificate_author_details.png)

4. For the distributor certificate, use the default Tizen distributor certificate or provide your own.

   ![Enter distributor certificate details](media/certificate_distributor_details.png)

5. Confirm and save the profile.

   ![Certificate profile created successfully](media/certificate_profile_created.png)

The video below shows how to create a Tizen certificate profile:

<video controls height="400">
  <source src="media/create_tizen_certificate.mp4" type="video/mp4">
</video>

The video below shows how to create a Samsung certificate profile:

<video controls height="400">
  <source src="media/create_samsung_certificate.mp4" type="video/mp4">
</video>

Use a default certificate only for quick emulator testing. It is not valid for Store submission. You can also use an existing Certificate Manager profile or import custom author and distributor certificates.

## Manage Profiles

Select a profile to show author, distributor, and expiration details in the lower panel. Select its radio button to make it active; the active profile is used for packaging and is synchronized with **Tools > Options > Tizen > Certification**. Use the trash icon to delete a profile.

The following image highlights the trash controls and the certificate-details section for the selected profile.

![Certificate Manager profile controls and details](media/certificate_manager_profiles_highlighted.png)

Keep certificate files and their passwords secure. Do not commit them to a source repository.

## Issue Report

Select **Issue Report** in the upper-right corner of Certificate Manager to open the GitHub issues page and report an issue.

![Issue Report button](media/certificate_manager_issue_report_highlighted.png)
