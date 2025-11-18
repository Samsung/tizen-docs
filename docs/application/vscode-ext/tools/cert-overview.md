# Certificates

In order to install Tizen applications on Samsung Tizen devices, you must first register certificates containing the Device Unique Identifier (DUID) of a device.
There are two types of certificates, author certificate and distributor certificate. These certificates are used for signing and verifying the application.

These certificates ensure that your signed application runs only on those devices that are registered by you. 
The certification process is necessary not only for testing your apps on the actual devices but also for uploading them to Galaxy Store. 

The certification process guarantees that your application will not be distributed by someone else even if your application package is leaked.
The following pages describe how to generate certificates, how to maintain them, and how to package your application:

- [Installing the Extension](installing-the-extension.md)
- [Creating Certificate Profile](cert-create-profile.md)
- [Signing Application with Certificate](signing-application-with-certificate.md)
- [Managing Certificate Profile](cert-manage-profile.md)

## Tizen certificate

Tizen certificate follows the exact specifications of [XML Digital Signature for widgets](http://www.w3.org/TR/widgets-digsig/) from W3C.
Samsung issues certificates for Samsung Tizen devices based on the Tizen certificate. It provides the security foundation for the Tizen platform and applies to all Tizen apps across any device.

A Tizen certificate profile has two main parts:

### 1. Author Certificate
The author certificate uniquely identifies the developer or organization that created the application.

It ensures:

- Verifies the app's origin so users know where it came from
- Enables secure communication between components signed with the same certificate (via IPC)
- Maintains update rights across all versions—you must use the same key for every update

**Critical:** Keep this key safe. Lose it, and you can't update your own app.tion identity, the author key must be stored carefully and protected from loss.

### 2. Distributor Certificate

The distributor certificate identifies the party that distributes the application (such as app stores or device vendors).
It also grants the privilege levels allowed for the application.

During local development and testing, the distributor certificate included in the profile is not the official store certificate. Instead, it is a temporary developer distributor certificate that allows installation on test devices.
Once the application is submitted to the appropriate store, the distributor certificate inside the package is replaced by the official store-issued certificate.

## Samsung Certificate

The Samsung Certificate Profile is an extension of the Tizen security framework specifically required for Samsung’s Tizen-based devices such as smart TVs, older Galaxy Watches, and IoT appliances. It incorporates Samsung’s device-level verification and permission controls on top of the standard Tizen certification model.

### Author Certitficate
This identifies the developer to Samsung’s ecosystem and is validated through Samsung’s developer portal.

It ensures:
- Binding the app to a verified Samsung developer account
- Maintaining update rights for Samsung Tizen devices
- Verifying the authenticity of applications developed for Samsung hardware

Although structurally similar to the generic Tizen author certificate, Samsung’s author certificate is tied to Samsung’s online developer infrastructure and requires account verification.

### Distributor Certificate
Generated specifically for Samsung hardware after the user authenticate and validate the DUID (Device Unique ID) of the device.

It enables:
- Installation of apps on registered Samsung devices
- Access to Samsung-specific APIs and privileged capabilities
- Debugging and sideloading on real devices via DUID-base verification

When the application is later uploaded to the Samsung store (e.g., for Samsung Smart TV or wearable distribution), the temporary distributor certificate is replaced with Samsung’s official store distributor certificate during the signing process.

## Security

Keep your author certificate (author.p12) file in a safe and secure place.
Ensure that you have secure backups.

> [!NOTE]
> If you upload your applications to the respective stores without the original author certificate that signs your app, you will not be able to publish any updates on your applications.
