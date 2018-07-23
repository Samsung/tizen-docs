# Getting the Certificates

In order to install a Tizen application onto Samsung Tizen wearable devices, you must first register certificates containing the DUID (Device Unique Identifier) of the device.
Two types of certificates are needed; the author and the distributor certificate.
These certificates are used for signing and verifying the application.

These certificates ensure that your signed application will run only on devices which you registered.
The certification process is necessary not only for testing your apps on the actual devices but also for uploading your apps to Galaxy Apps.

It guarantees that your application will not be distributed by someone else even if your application package is leaked.
This document describes how to generate certificates from Samsung and how to maintain them also packaging the application.

Contents:

- [Installing Certificates Extension](installing-certificate-extension.md)
- [Creating Certificates](creating-certificates.md)
- [Permit Device To Install Applications](permit-device-to-install-apps.md)
- [Managing Certificate Profile](managing-certificate-profile.md)

## Certificates

Tizen certificate follows the exact specifications of [XML Digital signature for widgets](http://www.w3.org/TR/widgets-digsig/) from W3C.
Samsung issues certificates for Samsung Tizen devices based on the Tizen certificate.
The author certificate identifies the author, ensures future updates to the application and is used for secure IPC.
The same key must be used in all versions of your application so it should be kept in a safe and secure place.
The distributor certificate identifies distributor, i.e. Galaxy Apps, Tizen Store, and grants privilege.
However the issued distributor certificate is not from the real distributor but just allows the installation to the registered device.
After the application is uploaded to the Stores, it is replaced by the official distributor certificate.

## Secure Your Certificates

Keep your author certificate(author.p12) file in a safe and secure place.
Ensure that you have secure backups.
When you upload your applications at the Store without the original author certificate (which signs your app), you will not be able to publish any updates on to your applications.
The same key must be used in all versions of your applications.
