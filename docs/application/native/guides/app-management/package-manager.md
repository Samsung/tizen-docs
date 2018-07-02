# Package Manager


The package manager is used to retrieve detailed information of the installed packages on the device. This information includes the package name, label, path to the icon image, version, type, and installed storage.

The main features of the Package Manager API include:

- Retrieving information for all installed packages

  Use the `package_manager_foreach_package_info()` function to [retrieve the package information for all installed packages](#retrieve). As a result, the `package_manager_package_info_cb()` callback function is invoked and you can get the package information.

- Retrieving individual package information

  To [retrieve package information](#info), get the `package_info_h` object using the `package_info_create()` or `package_manager_get_package_info()` function.

- Retrieving package information from archives

  To [retrieve package information from archives](#archive), get the `package_archive_info_h` object using the `package_archive_info_create()` function.

- Monitoring changes

  You can [monitor package events](#listen), such as installation, uninstallation, and updates.

## Prerequisites

To enable your application to use the package manager functionality, ensure that the following prerequisites are met:

1. To use the Package Manager API (in [mobile](../../api/mobile/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html) applications), the application must request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Package Manager API, include the `<package_manager.h>` header file in your application:

   ```
   #include <package_manager.h>
   ```

<a name="retrieve"></a>
## Retrieve All Package Information

To retrieve all package information for installed packages:

1. Define the `package_info_cb()` callback function, which is invoked for each retrieved package and is used to access the package information:
   ```
   void
   package_info_cb(package_info_h package_info, void *user_data)
   {
       int ret;

       char *pkg = NULL;
       char *label = NULL;
       char *icon = NULL;
       char *version = NULL;
       char *type = NULL;
       package_info_installed_storage_type_e storage;
       bool system;
       bool removable;
       bool preload;

       package_info_get_package(package_info, &pkg);
       package_info_get_label(package_info, &label);
       package_info_get_icon(package_info, &icon);
       package_info_get_version(package_info, &version);
       package_info_get_type(package_info, &type);
       package_info_get_installed_storage(package_info, &storage);
       package_info_is_system_package(package_info, &system);
       package_info_is_removable_package(package_info, &removable);
       package_info_is_preload_package(package_info, &preload);

       dlog_print(DLOG_INFO, TAG, "pkg \t= [%s]\n", pkg);
       dlog_print(DLOG_INFO, TAG, "label \t= [%s]\n", label);
       dlog_print(DLOG_INFO, TAG, "icon \t= [%s]\n", icon);
       dlog_print(DLOG_INFO, TAG, "version \t= [%s]\n", version);
       dlog_print(DLOG_INFO, TAG, "type \t= [%s]\n", type);
       dlog_print(DLOG_INFO, TAG, "storage \t= [%d]\n", storage);
       dlog_print(DLOG_INFO, TAG, "system \t= [%d]\n", system);
       dlog_print(DLOG_INFO, TAG, "removable \t= [%d]\n", removable);
       dlog_print(DLOG_INFO, TAG, "preload \t= [%d]\n", preload);

       free(pkg);
       free(label);
       free(icon);
       free(version);
       free(type);
   }
   ```
2. Use the `package_manager_foreach_package_info()` function to retrieve all package information by invoking a callback function for each retrieved package:
   ```
   ret = package_manager_foreach_package_info(package_info_cb, NULL);
   if (ret != PACKAGE_MANAGER_ERROR_NONE)
       dlog_print(DLOG_ERROR, TAG, "foreach_package_info error: %d", ret);
   ```

<a name="info"></a>
## Retrieve Specific Package Information

To retrieve specific package information:

1. Use the `package_manager_get_package_info()` function. This function fills the second parameter with the package information handle, which is then used with the following `package_info_get_*()` functions to retrieve the specific information:
   - package_info_get_label()
   - package_info_get_icon()
   - package_info_get_version()
   - package_info_get_type()
   - package_info_get_installed_storage()
   - package_info_get_root_path()
   - package_info_is_system_package()
   - package_info_is_removable_package()
   - package_info_is_preload_package()
   - package_info_is_accessible()

    ```
    char *version = NULL;
    char *label = NULL;
    char *type = NULL;
    package_info_h package_info = NULL;
    package_manager_get_package_info("PACKAGE-ID", &package_info);

    package_info_get_version(package_info, &version);
    package_info_get_label(package_info, &label);
    package_info_get_type(package_info, &type);

    dlog_print(DLOG_INFO, TAG, "label \t= [%s]\n", label);
    dlog_print(DLOG_INFO, TAG, "icon \t= [%s]\n", icon);
    dlog_print(DLOG_INFO, TAG, "version \t= [%s]\n", version);

    free(label);
    free(icon);
    free(version);

    /* Use package information */
    ```

2. Release the package information handle with the `package_info_destroy()` function when the package information is no longer needed:
    ```
    package_info_destroy(package_info);
    ```

<a name="archive"></a>
## Retrieve Package Information from Archives

To retrieve package information from archives:

1. Use the `package_archive_info_create()` function. This function fills the second parameter with the package archive information handle, which is then used with the following `package_archive_info_get_*()` functions to retrieve the specific information:
   - package_archive_info_get_package()
   - package_archive_info_get_type()
   - package_archive_info_get_version()
   - package_archive_info_get_api_version()
   - package_archive_info_get_description()
   - package_archive_info_get_label()
   - package_archive_info_get_author()
   - package_archive_info_get_icon()

    ```
    int ret;
    char *package = NULL;
    char *version = NULL;
    char *description = NULL;
    unsigned char *icon = NULL;
    size_t icon_size = 0;
    package_archive_info_h archive_info = NULL;

    ret = package_archive_info_create("/path/to/your/archive", &archive_info);
    /* error handling */

    ret = package_archive_info_get_package(archive_info, &package);
    /* error handling */
    ret = package_archive_info_get_version(archive_info, &version);
    /* error handling */
    ret = package_archive_info_get_description(archive_info, &description);
    /* error handling */
    ret = package_archive_info_get_icon(archive_info, &icon, &icon_size);
    /* error handling */

    /* do something */
    /* note that icon is read as binary data */

    free(package);
    free(version);
    free(description);
    free(icon);
    ```

2. Release the package archive information handle with the `package_archive_info_destroy()` function when the package information is no longer needed:
    ```
    package_archive_info_destroy(archive_info);
    ```

<a name="listen"></a>
## Monitor Package Events

To monitor package events, such as installation, uninstallation, and updates:

1. Create the package manager handle (`package_manager_h`) using the `package_manager_create()` function:

   ```
   package_manager_create(package_manager_h *manager);
   ```

2. Set the package event to monitor by calling the `package_manager_set_event_status()` function.

   The second parameter defines the package status that you want to monitor. The possible values are listed in the `package_manager_status_type_e` enumeration (in [mobile](../../api/mobile/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html#ga405444ebd6254b9cfbaedec829558882) and [wearable](../../api/wearable/latest/group__CAPI__PACKAGE__MANAGER__MODULE.html#ga405444ebd6254b9cfbaedec829558882) applications):

    ```
    package_manager_set_event_status(manager, PACKAGE_MANAGER_STATUS_TYPE_ALL);
    ```

3. Register a callback function to be invoked when the event (status change) you set in the previous step takes place, and implement the callback function:

   ```
   void
   event_cb(const char *type, const char *package, package_manager_event_type_e event_type,
            package_manager_event_state_e event_state, int progress,
            package_manager_error_e error, void *user_data)
   {
       if (event_state == PACKAGE_MANAGER_EVENT_STATE_STARTED)
           dlog_print(DLOG_INFO, LOG_TAG, "Started");
       else if (event_state == PACKAGE_MANAGER_EVENT_STATE_PROCESSING)
           dlog_print(DLOG_INFO, LOG_TAG, "Progress: %d", progress);
       else if (event_state == PACKAGE_MANAGER_EVENT_STATE_COMPLETED)
           dlog_print(DLOG_INFO, LOG_TAG, "Completed");
       else
           dlog_print(DLOG_INFO, LOG_TAG, "Failed");
   }

   package_manager_set_event_cb(manager, event_cb, NULL);
   ```

4. Release the package manager with the `package_manager_destroy(package_manager_h manager)` function when the package manager is no longer needed:

   ```
   package_manager_destroy(package_manager_h manager);
   ```

## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
