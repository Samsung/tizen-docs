# File System Directory Hierarchy


The Tizen platform uses the underlying Linux file system.

The following rules apply to the file system access:

-   Native applications can access the file system using native APIs and
    open source libraries, such as eglibc and glib.
-   Applications can use relative paths.
-   The file system is case-sensitive.
-   The I/O resources and limitations depend on the underlying Linux
    file system or system configuration.
    -   The maximum number of file or directory handles: 1024
    -   The maximum length of a file or directory name: 255
    -   The maximum length of a full path name: 4096

The following table shows the application directory hierarchy:

**Table: Application package directory hierarchy**

| Name             | Description                              | Permission                               |
|----------------|----------------------------------------|----------------------------------------|
| `bin`            | Executable binary path                   | Owner: Read<br>Others: Access denied     |
| `lib`            | Library path                             | Owner: Read<br>Others: Access denied     |
| `data`           | Used to store private data of an application.<br>To get the application data directory path, call the `app_get_data_path()` function of the App Common module. | Owner: Read and Write<br>Others: Access denied |
| `res`            | Used to read resource files that are delivered with the application package.<br>To get the application resource directory path, call the `app_get_resource_path()` function of the App common module. | Owner: Read<br>Others: Access denied     |
| `shared`         | Parent directory of the data, res, and trusted sub-directories. Files in this directory cannot be delivered with the application package. | Owner: Read<br>Others: Read              |
| `shared/data`    | Used to share data with other applications.<br>To get this directory path of your own application, call the `app_get_shared_data_path()` function of the App common module.<br>Files stored in the shared/data directory can be read by other applications. Do not store application's private data in the shared/data directory. | Owner: Read and Write<br>Others: Read    |
| `shared/res`     | Used to share resources with other applications. The resource files are delivered with the application package.<br>To get this directory path of your own application, call the `app_get_shared_resource_path()` function of the App common module.<br>Files stored in the shared/res directory can be read by other applications. Do not pack application's private resource files in the shared/res directory. | Owner: Read<br>Others: Read              |
| `shared/trusted` | Used to share data with family of trusted applications. The family applications signed with the same certificate can access data in the shared/trusted directory.<br>To get this directory path of your own application, call the `app_get_shared_trusted_path()` function of the App common module. | Owner: Read and Write<br>Family: Read and Write<br>Others: Access denied |

Every application can access a storage area where media files are
stored. This is the media directory. In native applications, to obtain
the media directory path, call the `storage_get_directory()` function of
Storage module. The following table lists the sub-directories of the
media directory.

**Table: Media directory hierarchy**

| Name               | Description                        | Permission     |
|------------------|----------------------------------|--------------|
| `Images`           | Used for Image data.               | Read and Write |
| `Sounds`           | Used for Sound data.               | Read and Write |
| `Videos`           | Used for Video data.               | Read and Write |
| `Cameras`          | Used for Camera pictures.          | Read and Write |
| `Downloads`        | Used for Downloaded data.          | Read and Write |
| `Music`            | Used for Music data.               | Read and Write |
| `Documents`        | Used for Documents.                | Read and Write |
| `System Ringtones` | Used for System default ringtones. | Read           |
| `Others`           | Used for other types.              | Read and Write |

Every application can also access the external storage, such as MMC.
This is the external storage directory. In native applications, to
obtain the external storage directory path, call the
`storage_get_directory()` function of the Storage module. The following
table lists the sub-directories of the external storage directory.

**Table: External storage directory hierarchy**

| Name        | Description               | Permission     |
|-----------|-------------------------|--------------|
| `Images`    | Used for Image data.      | Read and Write |
| `Sounds`    | Used for Sound data.      | Read and Write |
| `Videos`    | Used for Video data.      | Read and Write |
| `Cameras`   | Used for Camera pictures. | Read and Write |
| `Downloads` | Used for Downloaded data. | Read and Write |
| `Music`     | Used for Music data.      | Read and Write |
| `Documents` | Used for Documents.       | Read and Write |
| `Others`    | Used for other types.     | Read and Write |
