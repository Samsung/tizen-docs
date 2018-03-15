# Security Tips


When you design an application or service, you must minimize any accidental introduction of security vulnerabilities. The following practices aim to reduce the likelihood of security vulnerabilities caused by programming in the Tizen platform.

This feature is supported in mobile applications only.

## Storing Data Safely

By using a proper way to store data, you can minimize any data-related security concerns. Tizen provides 3 fundamental ways for an application to store data on the device:

- Using an internal storage

  A Tizen application is sandboxed by SMACK. This means that files that you create in an internal storage are not accessible by other applications by default. This is sufficient for most applications.

  If you want to share data between your own applications only, use a shared trusted directory. Only applications signed with the same key can access data in a shared trusted directory.

  To provide additional protection for sensitive data, use the [key manager](#key).

- Using an external storage

  All applications can access an external storage, such as an SD card. The user can remove the external storage, and extract or modify the data in it outside the device. This means that you must not store any sensitive data in an external storage.

  If you use data in an external storage as input for dynamic loading or a database query, validate the data before using it.

<a name="key"></a>
- Using the key manager

  The [key manager](secure-key.md) provides a secure repository for the keys, certificates, and sensitive data of the user and their applications.

  A client can specify simple access rules when storing data in the key manager:

  - If the data is tagged as exportable, the key manager returns the raw value of the data.

  - If the data is tagged as non-exportable, the key manager does not return its raw value.

    In that case, the key manager provides secure cryptographic operations for non-exportable keys without revealing key values to clients.

  All of the data in the key manager is protected by an internal key. In addition, a client can encrypt its data using its own password. If a client provides a password when storing data, the data is encrypted with that password. To obtain the data from the key manager later, the same password must be provided. The additional password provides protection in case the device is lost.

  When storing data:

  - For small amounts of sensitive data, store the data within the key manager.
  - For large amounts of sensitive data, store the data as a local file and encrypt it with a key stored within the key manager.
  - For very sensitive data, supply an additional password.
  - For keys, tag them as non-exportable when storing them.

## Using Privileges for API Access Control

All native applications have a manifest file (`tizen-manifest.xml`) describing permissions. The manifest file describes SMACK labels and allows the application to get proper privileges.

In a mandatory access control system, an application that accesses sensitive resources must acquire proper permissions from the system. In Tizen 2.X, permissions can be granted by loading proper SMACK rules:

- For efficiency, the rules are grouped by their purpose, such as getting permissions to retrieve contact information or send text messages. In Tizen, each grouped rule set with a specific purpose is called a privilege.

- To ask for a permission it requires, the application can declare privileges in the manifest file.

- Tizen provides API-level access control for security-sensitive operations that can harm user privacy and system stability, if not used properly. If the application uses such sensitive APIs, it must declare the required privileges in the manifest file.

  To determine whether an API requires privileges to be used, see the [API Reference](../../api/mobile/latest/index.html).

In Tizen 3.0, the platform uses core privileges for access control, but the concept of the application privilege declaration is not changed. As in Tizen 2.X, the application can declare required privileges in the manifest file according to their own application type.

### Privacy-related Privileges

Some privileges are related to the user privacy and sensitive data (such as contact, calendar, message, and camera).

Because these privileges are used to access very sensitive user data, when an application tries to use them, the system opens a popup window to ask the user whether they allow the data to be accessed. The user can enable and disable those privileges for specific applications from the device **Settings** menu.

## Communicating Securely Between Applications

Tizen supports APIs for communicating between application processes. You can use various methods when developing your Tizen application to ensure secure communication: file sharing, message ports, and data control.

### File Sharing

File sharing is a basic mechanism for interchanging data between application processes. By sharing a data file, the application process can send and receive data:

- The Tizen application process can write a file to the path that is returned by the `app_get_data_path()` function.

  Because the application data path is created for each application package, the applications in the same package can share files in the data path. This is a totally secure file sharing method, because applications in the same package are trusted applications.

- Tizen applications can write a file to the path that is returned by the `app_get_shared_data_path()` function, and share the file among all other applications on the device.

  The files in the shared data path can be read by all other applications on the device. Since you cannot control which applications are able to read the file in the shared data path, do not share private information in this way. Sharing data among applications through the shared data path is insecure, and consequently the shared data path is going to be deprecated in the next Tizen release.

  As an alternative to the shared data path, Tizen 2.4 introduced a feature of sharing a file in its data path using application controls. When an application requests an application control, it can specify a URI and the `APP_CONTROL_DATA_PATH` extra key. If you pass the file path to the application control as the `APP_CONTROL_DATA_PATH` extra key, the platform grants temporary read permission to the receiving application. This method is much more secure than sharing a file in the shared data path.

- To share files among applications that you have developed, use the path that is returned by the `app_get_shared_trusted_path()` function.

  The files in the shared trusted path can be read and written by the applications that are developed by the same developer. This is a secure way of sharing files among your applications.

**Table: File sharing functions**

| Function                        | Read and write permissions               | Security                                 |
|---------------------------------|------------------------------------------|------------------------------------------|
| `app_get_data_path()`           | Applications in the same package         | Strong                                   |
| `app_get_shared_data_path()`    | Read: all applications on the device<br> Write: applications in the same package | Weak<br> Do not use this function if you are not sure about its security. |
| `app_get_shared_trusted_path()` | Applications signed with the same certificate | Strong                                   |

### Message Ports

The Message Port API [supports one-to-one communication](../app-management/message-port.md) between 2 applications. Tizen also supports trusted communication as an option for a more secure communication between 2 trusted applications.

When you use the `message_port_register_trusted_local_port()` and `message_port_send_trusted_message()` functions, you can make the communication valid only between the applications that are developed by you. Since the platform checks the application author certificate for trusted communications, you can use these functions to make your applications communicate through a more secure channel.

### Data Control

The Data Control API supports [communication between provider and consumer applications](../app-management/data_control.md). One provider can provide data to many consumers in a structured way, such as SQL or map.

The consumer can request data from any provider, as long as the consumer knows the provider ID of the provider application. If the provider does not want to provide data to arbitrary consumers, it can check the application ID of the consumer in the callback handlers, such as `data_control_provider_sql_insert_request_cb()` or `data_control_provider_sql_select_request_cb()`. The provider can get the consumer application ID though the `data_control_provider_get_client_appid()` function, and then determine whether it allows that consumer to access its data.

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
