# Data Storages


You can access storage information and manage directories within certain parts of the file system, represented as [virtual root locations](#virtualroots). These virtual roots form a collection of locations that function as a single virtual device file system.

The main features of the Storage API include:

- Storage management

  You can manage different storage locations on the device.

  You can [retrieve additional information about the storage locations](#storage), including which storage is supported on the device, by using the `storage_foreach_device_supported()` function. The callback function returns the storage type, mount state, and virtual root path. You can also [retrieve memory sizes](#memory) and [monitor storage state changes](#state).

- Storage space management

  You can [get the available and total size](#space) of the storage.

## Prerequisites

To use the functions and data types of the Storage API (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html) applications), include the `<storage.h>` header file in your application:

```
#include <storage.h>
```

<a name="memory"></a>
## Retrieving Memory Sizes

Use the statvfs wrapper to get memory sizes:

- Get the internal memory size with the `storage_get_internal_memory_size()` function.

  The function returns the internal memory size. Use it instead of the statvfs function when you need the internal memory size.

  When the memory is low, the system must at least be able to launch a low memory pop-up. To do that, it reserves a minimum memory, whose size depends on the device storage size. The memory size returned by the `storage_get_internal_memory_size()`function excludes the minimum memory size.

  The statvfs structure has a different structure size than the `__USE_FILE_OFFSET64` option. If you define this option, libstorage changes the `storage_get_internal_memory_size()` function to `storage_get_internal_memory_size64()` automatically.

    ```
    int error;
    struct statvfs s;
    error = storage_get_internal_memory_size(&s);
    ```

- Get the external memory size with the `storage_get_external_memory_size()` function.

  The function returns the external memory size. Use it instead of the statvfs function when you need the external memory size.

  When the memory is low, the system must at least be able to launch a low memory pop-up. To do that, it reserves a minimum memory, whose size depends on the device storage size. The memory size returned by the `storage_get_external_memory_size()`function excludes the minimum memory size.

  The statvfs structure has a different structure size than the `__USE_FILE_OFFSET64` option. If you define this option, libstorage changes the `storage_get_external_memory_size()` function to `storage_get_external_memory_size64()` automatically.

    ```
    int error;
    struct statvfs s;
    error = storage_get_external_memory_size(&s);
    ```

<a name="storage"></a>
## Retrieving Storage Information

Files saved on the internal or external storage are readable or writeable by all applications. When an application is uninstalled, the files written by that application are not removed from the internal or external storage.

To retrieve storage information:

- Retrieve all storages on a device by using the `storage_foreach_device_supported()` function.

  The function triggers a separate callback for each storage. As long as the callback returns `true`, the foreach function continues to loop over the storages.

  Within the callback, you can get information about the individual storage type, state, location, and ID.

    ```
    static int internal_storage_id;
    static bool
    storage_cb(int storage_id, storage_type_e type, storage_state_e state,
               const char *path, void *user_data)
    {
        if (type == STORAGE_TYPE_INTERNAL) {
            internal_storage_id = storage_id;

            return false;
        }

        return true;
    }

    int error;
    error = storage_foreach_device_supported(storage_cb, NULL);
    ```

- Get the root directory of a specific storage by using the `storage_get_root_directory()` function.

  The function retrieves the absolute path to the root directory.

    ```
    int error;
    char *path;
    error = storage_get_root_directory(internal_storage_id, &path);

    free(path);
    ```

- Get the directory path for a storage of a specific type by using the `storage_get_directory()` function.

  The function retrieves the absolute path to the directory.

  The second parameter defines the directory type based on the `storage_directory_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gaacf2209a06b947c1cee4ba223679383a) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gaacf2209a06b947c1cee4ba223679383a) applications).

  To get the media directory:

    ```
    int error;
    char *path;
    error = storage_get_directory(internal_storage_id, STORAGE_DIRECTORY_IMAGES, &path);

    free(path);
    ```

- Get the storage type of a specific storage by using the `storage_get_type()` function.

  The `storage_type_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gabdf32571260b6c253da5bfcdecaa2f1f) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gabdf32571260b6c253da5bfcdecaa2f1f) applications) defines the available storage types.

    ```
    int error;
    storage_type_e type;
    error = storage_get_type(internal_storage_id, &type);
    ```

- Get the mount state of a specific storage by using the `storage_get_state()` function.

  The `storage_state_e` enumerator (in [mobile](../../api/mobile/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gac72d0e57e790d888dfd7bd57d52fbfee) and [wearable](../../api/wearable/latest/group__CAPI__SYSTEM__STORAGE__MODULE.html#gac72d0e57e790d888dfd7bd57d52fbfee) applications) defines the available storage states.

    ```
    int error;
    storage_state_e state;
    error = storage_get_state(internal_storage_id, &state);
    ```

<a name="state"></a>
## Monitoring Storage State Changes

To monitor storage state changes:

1. Define a callback, which is called when the storage state changes:

   ```
   static void
   storage_changed_cb(int storage_id, storage_state_e state, void *user_data)
   {
       if (storage_id != internal_storage_id)
           return;
       dlog_print(DLOG_DEBUG, LOG_TAG, "state changed to %d", state);
   }
   ```

2. Register the callback:

   ```
   int error;
   error = storage_set_state_changed_cb(internal_storage_id, storage_changed_cb, NULL);
   ```

3. When no longer needed, deregister the callback:

   ```
   int error;
   error = storage_unset_state_changed_cb(internal_storage_id, storage_changed_cb);
   ```

<a name="space"></a>
## Retrieving Storage Space Information

To get the available and total size of the storage, use the `storage_get_total_space()` and `storage_get_available_space()` functions. They return the storage size, excluding the minimum memory size to launch the low memory pop-up in a low memory situation. Consequently, the available size must be less than the original available size, and you must use these functions to get the memory size. For the same reason, you cannot use the `statvfs` function directly in Tizen. Instead, use `storage_get_internal_memory_size()`and `storage_get_external_memory_size()`. The Statvfs structure has a different structure size defined by "\__USE\_FILE\_OFFSET64". However, you can ignore this, since the Storage API uses a proper function automatically.

To retrieve storage space information:

- Get the total space of the storage by using the `storage_get_total_space()` function.

  The function returns the total space of the given storage in bytes. It invokes the `storage_get_internal_memory_size()` or `storage_get_external_memory_size()` function internally.

    ```
    int error;
    unsigned long long bytes;
    error = storage_get_total_space(internal_storage_id, &bytes);
    ```

- Get the available space of the storage by using the `storage_get_available_space()` function.

  The function returns the available space of the given storage in bytes. It invokes the `storage_get_internal_memory_size()` or `storage_get_external_memory_size()` function internally.

    ```
    int error;
    unsigned long long bytes;
    error = storage_get_available_space(internal_storage_id, &bytes);
    ```

<a name="virtualroots"></a>
## Virtual Roots

The following table lists the supported virtual roots.

**Table: Filesystem virtual roots**

| Virtual root | Description                              |
|--------------|------------------------------------------|
| `images`     | Location for storing images.             |
| `sounds`     | Location for storing sound files.        |
| `videos`     | Location for storing video files.        |
| `camera`     | Location for storing photos.             |
| `downloads`  | Location for storing downloaded items.   |
| `music`      | Location for storing audio files.        |
| `documents`  | Location for storing documents.          |
| `others`     | Location for storing other files.        |
| `ringtones`  | Location for ringtones (read-only location). |


## Related Information
- Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
