# Certificates

In order to install Tizen applications on Samsung Tizen wearable devices, you must first register certificates containing the Device Unique Identifier (DUID) of a device.
There are two types of certificates, author certificate and distributor certificate. These certificates are used for signing and verifying the application.

These certificates ensure that your signed application runs only on those devices that are registered by you. 
The certification process is necessary not only for testing your apps on the actual devices but also for uploading them to Galaxy Store. 

The certification process guarantees that your application will not be distributed by someone else even if your application package is leaked.
The following pages describe how to generate certificates, how to maintain them, and how to package your application:

- [Installing the Extension](installing-the-extension.md)
- [Creating Certificates](creating-certificates.md)
- [Signing Application with Certificate](signing-application-with-certificate.md)
- [Managing Certificate Profile](managing-certificate-profile.md)

## Tizen Certificate

Tizen certificate follows the exact specifications of [XML Digital Signature for widgets](http://www.w3.org/TR/widgets-digsig/) from W3C.
Samsung issues certificates for Samsung Tizen devices based on the Tizen certificate.
The author certificate identifies the author, ensures future updates to the application, and is used for secure IPC.
The same key must be used in all versions of your application, therefore, it should be kept in a safe and secure place.
The distributor certificate identifies the distributors such as Galaxy Store, Tizen Store, and so on, and grants privilege.
However, the issued distributor certificate is not from the real distributor but allows the installation to the registered device.
After the application is uploaded to the respective store, it is replaced by the official distributor certificate.

## Security

Keep your author certificate (author.p12) file in a safe and secure place.
Ensure that you have secure backups.

> [!NOTE]
> If you upload your applications to the respective stores without the original author certificate that signs your app, you will not be able to publish any updates on your applications.
