# Security


The security features introduce how private information remains private, and how the user knows when they are trying to access privileged information. You can use a repository and cryptographic operations to manage keys, certificates, and sensitive user data. When the user tries to access privileged information, you can display information about the data.

You can use the following security features in your native applications:

- [Secure Key Management](secure-key.md)

  You can provide a secure repository for keys, certificates, and sensitive data related to users and their password-protected applications. You can also use secure cryptographic operations for non-exportable keys without revealing the key values to clients.

- [Privilege Information](privilege.md)

  You can retrieve information about existing permissions granted by a privilege. The information can be delivered to the user as a notification.

- [Privacy-related Permissions](privacy-related-permissions.md)

  You can check current permissions for privacy-related privileges and request user permission to use specific privileges.

- [Cryptographic Operations](yaca.md)

  You can encrypt and decrypt data with symmetric or asymmetric encryption, and manage keys with YACA (Yet Another Crypto API). You can also digest messages and create digital signatures.

- [Device Policy Management](dpm.md)

  You can create security-aware applications to manage device policies. In enterprise settings, you can provide rich control for IT administrators over employee devices.

- [Malware Scanning and Web Protection](csr.md)

  You can scan data, files, and directories to detect malware. You can also check the URL reputation before accessing a specific URL.

For information on how to minimize any accidental introduction of security vulnerabilities in your application, see [Security Tips](security-tip.md) (**in mobile applications only**).

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
