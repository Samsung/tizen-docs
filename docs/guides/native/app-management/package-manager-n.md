# Package Manager
## Dependencies
- Tizen 2.4 and Higher for Mobile
- Tizen 2.3.1 and Higher for Wearable

The package manager is used to retrieve detailed information on the installed packages on the device. This information includes the package name, label, path to the icon image, version, type, and installed storage.

The main features of the Package Manager API include:

- Retrieving information for all installed packages

  Use the `package_manager_foreach_package_info()` function to [retrieve the package information for all installed packages](#retrieve). As a result, the `package_manager_package_info_cb()` callback is invoked and you can get the package information.

- Retrieving individual package information

  To [retrieve package information](#info), get the `package_info_h` object using the `package_info_create()` or `package_manager_get_package_info()` function.

- Monitoring changes

  You can [monitor package events](#listen), such as installation, uninstallation, and updates.

## Prerequisites

To enable your application to use the package manager functionality:

1. To use the Package Manager API (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__PACKAGE__MANAGER__MODULE.html) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__PACKAGE__MANAGER__MODULE.html) applications), the application has to request permission by adding the following privilege to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/packagemanager.info</privilege>
   </privileges>
   ```

2. To use the functions and data types of the Package Manager API, include the `<package_manager.h>` header file in your application:

   ```
   #include <package_manager.h>
   ```

## Retrieving All Package Information

To retrieve all package information for installed packages:

1. Define the `package_info_cb()` callback function, which is invoked for each retrieved package and used to access the package information:
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
2. Use the `package_manager_foreach_package_info()` function to retrieve all package information by invoking a callback for each retrieved package:
```
ret = package_manager_foreach_package_info(package_info_cb, NULL);
if (ret != PACKAGE_MANAGER_ERROR_NONE)
    dlog_print(DLOG_ERROR, TAG, "foreach_package_info error: %d", ret);
```

## Retrieving Specific Package Information

To get specific package information:

1. Use the `package_manager_get_package_info()` function.The function fills the second parameter with the package information handle, which can then be used with the following `package_info_get_*()` functions to retrieve the specific information:
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

2. When no longer needed, release the package information handle with the `package_info_destroy()` function:
    ```
    package_info_destroy(package_info);
    ```

## Monitoring Package Events

To detect package events, such as installation, uninstallation, and updates:

1. Create the package manager handle (`package_manager_h`) using the `package_manager_create()` function:

   ```
   package_manager_create(package_manager_h *manager);
   ```

2. Set the package event to monitor by calling the `package_manager_set_event_status()` function.The second parameter defines the package status that you want to monitor. The possible values are listed in the `package_manager_status_type_e` enumeration (in [mobile](../../../../org.tizen.native.mobile.apireference/group__CAPI__PACKAGE__MANAGER__MODULE.html#ga405444ebd6254b9cfbaedec829558882) and [wearable](../../../../org.tizen.native.wearable.apireference/group__CAPI__PACKAGE__MANAGER__MODULE.html#ga405444ebd6254b9cfbaedec829558882) applications).
    ```
    package_manager_set_event_status(manager, PACKAGE_MANAGER_STATUS_TYPE_ALL);
    ```

3. Register a callback function to be invoked when the event (status change) you set above happens, and implement the callback:

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

4. Free the package manager:

   ```
   package_manager_destroy(package_manager_h manager);
   ```