# Security


The security features introduce how private information remains private, and how the user knows when they are trying to access privileged information. You can use a repository and cryptographic operations to manage keys, certificates, and sensitive user data. When the user tries to access privileged information, you can display information about the data.

You can use the following security features in your .NET applications:

-   [Secure Key Management](secure-repository.md)

    You can use a secure repository to store keys, certificates, and sensitive data related to users and their password-protected applications. In addition, the repository provides cryptographic operations for generating new key pairs and verifying signatures.

-   [Privilege Information](privilege.md)

    You can retrieve information about existing permissions granted by a privilege. The information can be delivered to the user as a notification.

-   [Privacy-related Permissions](requesting-permissions.md)

    You can check current permissions for privacy-related privileges and request user permission to use specific privileges.

-   [TEE Communication](tee-client.md)

    You can create secure communications by executing your application in a trusted execution environment (TEE), and communicating with other applications within that environment.


## Related Information
* Dependencies
  -   Tizen 4.0 and Higher
