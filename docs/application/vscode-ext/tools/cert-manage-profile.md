# Managing Certificate Profile

Before installing your application on a device or submitting it to the official site for Tizen applications, it must be signed with a certificate profile.
The signature verifies the source of the application and ensures that it is not tampered with since its publication.
A certificate profile is a combination of the certificates used for signing.

## General information

In the VSCode activity bar click:

 **(1) Tizen extension** > **(2) ACTIVE TARGETS > (3) Certificates: *Active certificate profile***.

The **Tizen Panel** will be opened with **CERTIFICATE** tab selected.

![Tizen Certificate Manager with two profile](media/certificate-manager/manage-profile-1.jpg)

- The active profile is indicated by the green indicator bullet.
- All of the application in this SDK will be signed with this active profile.
- You can create, delete, and set a profile to active here.
- Lower window shows the information of each certificate.
- You can replace the certificate with an existing one.
- The Tizen platform allows multiple distributor certificates up to two, which supports other device manufacturers or telecommunication companies. However, it is not needed for most of the developers generally.

## Importing existing certificates

If you already have:
- both the **author keyfile(.p12)** and **distributor keyfile(.p12)** certificates 

- only **author keyfile(.p12)**

- or **distributor keyfile(.p12)**

And you do not require a new certificate from Tizen or Samsung, you can import and use the available certificates to sign your application.
In that case, create a new certificate profile and select existing certificates at each step.

Follow the same steps as mentioned in creating certificate before [creating a new profile or selecting an old profile](creating-certificates.md#create_new_or_select_old_profile).

### Select an existing author certificate

  The author certificate must be the same for the application that is to be upgraded.
  1. Select **Import an existing author key file** and click **Next**.
  2. Click the **Browse** button and locate your author certificate key file.
  3. Enter the password of the key file.
  4. Click **Import file** button
  5. If the password is verified, the author key import successful notification will pop up.
  ![Select an existing author certificate](media/certificate-manager/author-import.jpg)


### Select an existing distributor certificate

  Click **Import an existing distributor key file**, click **Browse** to select your distributor key file(.p12), enter the password and then click **Import file**.

  ![Select an existing author certificate](media/certificate-manager/distributor-import.jpg)

### Create and find the created profile in the list

  After importing and creating, now you can find the created profile in the list.

  ![Select an existing author certificate](media/certificate-manager/imported-profile-create.jpg)

## Troubleshooting

- Question : I lost the **author.p12**. Can I upgrade my application?
- Answer : No. If the author key is different, the application cannot be upgraded.
