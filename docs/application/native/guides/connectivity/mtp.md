# File Transfer with MTP


The Media Transfer Protocol (MTP) is an extension of the Picture Transfer Protocol (PTP), a protocol for file transfers between 2 devices.

This feature is supported in mobile applications only.

The extension consists of the MTP initiator and MTP responder. The host, which connects to the MTP device, is called the MTP initiator, and the MTP device is called the MTP responder. One MTP initiator can manage multiple MTP responders. The MTP initiator only sends requests to the MTP responder, and the MTP responder only responds to the MTP initiator.

The MTP consists of 3 components:

- MTP device is a device that supports MTP. It has an MTP responder role and 1 or more MTP storages.

- MTP storage is the storage on the MTP device. It has 0 or more MTP objects.

- MTP object is the actual file. Each file on the device has a unique handle called "object handle". (The handle is not unique in each storage.)

  The MTP object has a parent object, so it can indicate a file hierarchy. If the parent object is 0, the object is in the root of the storage.

The MTP API supports importing the MTP object and its metadata to the MTP initiator from the MTP responder. There is no MTP Responder API because it is only used in responding to a request from the initiator.

The main features of the MTP API include:

- Managing MTP

  With the [MTP Manager](../../api/mobile/latest/group__CAPI__NETWORK__MTP__MANAGER__MODULE.html) API you can initialize and deinitialize the MTP, [set callbacks for MTP events](#events), and get various information, such as the [device list](#device_list), [storage list](#storages), [object handle](#object_handle), [object, and thumbnail](#object_and_thumbnail).

- Retrieving device information

  The [MTP Device Information](../../api/mobile/latest/group__CAPI__NETWORK__MTP__DEVICEINFO__MODULE.html) API allows you to [obtain various device details](#device_info), such as the device manufacturer name, model name, serial number, and version.

- Retrieving storage information

  The [MTP Storage Information](../../api/mobile/latest/group__CAPI__NETWORK__MTP__STORAGEINFO__MODULE.html) API allows you to [obtain various storage details](#storage_info), such as the storage free space, description, and type.

- Retrieving object information

  The [MTP Object Information](../../api/mobile/latest/group__CAPI__NETWORK__MTP__OBJECTINFO__MODULE.html) API allows you to [obtain various object details](#object_info), such as the object format, name, and size.

The MTP API can be used in other profiles, but it is most popular in the TV profile.

The internal implementation of the MTP references the [MTP specification](http://www.usb.org/developers/docs/devclass_docs/MTPv1_1.zip) and uses [LIBMTP](http://libmtp.sourceforge.net/).

> **Note**
>
> Currently, the MTP API has the following limitations in Tizen 3.0:
> - Only the PTP subset of the MTP is supported.
> - The transportation layer is possible only through USB.

## Prerequisites

To enable your application to use the MTP functionality:

1. To use the [MTP](../../api/mobile/latest/group__CAPI__NETWORK__MTP__MODULE.html) API, the application has to request permission by adding the following privileges to the `tizen-manifest.xml` file:

   ```
   <privileges>
      <privilege>http://tizen.org/privilege/mtp</privilege>
      <!--To store a file if the input or output path leads to a media storage-->
      <privilege>http://tizen.org/privilege/mediastorage</privilege>
      <!--To store a file if the input or output path leads to an external storage-->
      <privilege>http://tizen.org/privilege/externalstorage</privilege>
   </privileges>
   ```

2. To use the functions and data types of the MTP API, include the `<mtp.h>` header file in your application:

   ```
   #include <mtp.h>
   ```

3. Make sure that MTP is supported on your target device.

4. To initialize the MTP connection, call the `mtp_initialize()` function. If the function does not return an error, the MTP is ready for use.

   ```
   int
   manager_test_initialize(void)
   {
       int ret = 0;

       ret = mtp_initialize();
       if (ret == MTP_ERROR_NONE)
           dlog_print("Initialize successful");
       else
           dlog_print("Initialize failed, ret [%d]", ret);

       return ret;
   }
   ```

5. When the MTP is no longer needed, free all resources and deinitialize it:

   ```
   int
   manager_test_deinitialize(void)
   {
       int ret = 0;

       ret = mtp_deinitialize();
       dlog_print("ret[%d]: deinitialize", ret);

       return ret;
   }
   ```

<a name="device_list"></a>
## Getting the MTP Device List

To get the MTP devices connected to the MTP initiator, retrieve the MTP device list with the `mtp_get_devices()` function.

To select the device you want, retrieve information about the devices in the device list with the `mtp_deviceinfo_get_XXX()` functions. The following example retrieves the manufacturer (for example, "Samsung Electronics Co., Ltd.") and model name (for example, "SM-A700L") for each device in the list.

```
int
manager_test_get_devices(void)
{
    int i;
    int ret = 0;
    int bus_location = 0;
    int device_number = 0;
    int device_count;
    mtp_device_h *mtp_devices = NULL;
    char *name = NULL;

    ret = mtp_get_devices(&mtp_devices, &device_count);

    if (ret != MTP_ERROR_NONE) {
        dlog_print("mtp_get_devices failed!!!");

        return -1;
    }

    if (device_count == 0) {
        dlog_print("device does not exist!!!");
        END();

        return -1;
    }

    for (i = 0; i < device_count; i++) {
        dlog_print("mtp_device[%d] handle - %d", i, mtp_devices[i]);
        ret = mtp_deviceinfo_get_manufacturer_name(mtp_devices[i], &name);
        g_free(name);
        ret = mtp_deviceinfo_get_model_name(mtp_devices[i], &name);
        g_free(name);
    }

    dlog_print("Select first device");

    mtp_device = mtp_devices[0];

    dlog_print("ret[%d]: 1st mtp device [%d]", ret, mtp_device);

    END();

    return ret;
}
```

<a name="device_info"></a>
## Getting MTP Device Information

To obtain information on the MTP device, use the `mtp_deviceinfo_get_XXX()` functions. To avoid memory leaks, free the character array variable with the `free()` function when no longer needed.

The following example retrieves the device serial number:

```
mtp_device_h mtp_device; /* Get this variable using mtp_get_devices() */

int
deviceinfo_test_get_serialnumber(void)
{
    int ret = 0;
    char *serial_number = NULL;

    ret = mtp_deviceinfo_get_serial_number(mtp_device, &serial_number);
    dlog_print("ret[%d]: serialnumber[%s]", ret, serial_number);

    if (serial_number == NULL)
        free(serial_number);

    return ret;
}
```

<a name="storages"></a>
## Getting the MTP Storages

To obtain a list of MTP storages on an MTP device, use the `mtp_get_storages()` function. To avoid memory leaks, free the storage array variable with the `free()` function when no longer needed.

> **Note**  
> The storage variable is used in all storage-related functions. Manage it with care.

```
mtp_device_h mtp_device; /* Get this variable using mtp_get_devices() */

int
manager_test_get_storages(void)
{
    mtp_storage_h *mtp_storages = NULL;

    ret = mtp_get_storages(mtp_device, &mtp_storages, &storage_count);
    dlog_print("ret[%d]: storage_count[%d]", ret, storage_count);

    if (storage_count == 0) {
        dlog_print("storage does not exist!!!");

        return -1;
    }

    for (i = 0; i < storage_count; i++)
        dlog_print("mtp storage %d [%d]", i, mtp_storages[i]);

    if (mtp_storages != NULL)
        free(mtp_storages);

    return ret;
}
```

<a name="storage_info"></a>
## Getting MTP Storage Information

To obtain information on the MTP storage, use the `mtp_storageinfo_get_XXX()` functions. To avoid memory leaks, free the character array variable with the `free()` function when no longer needed.

The following example retrieves the storage description:

```
mtp_device_h mtp_device; /* Get this variable using mtp_get_devices() */
mtp_storage_h mtp_storage; /* Get this variable using mtp_get_storages() */

int
storageinfo_test_get_description(void)
{
    int ret = 0;
    char *description = NULL;

    ret = mtp_storageinfo_get_description(mtp_device, mtp_storage, &description);
    dlog_print("ret[%d]: description[%s]", ret, description);

    if (description != NULL)
        free(description);

    return ret;
}
```

<a name="object_handle"></a>
## Getting the Object Handle

To obtain the object handle, get the unique ID value of the object handles from the MTP responder.

When first using the `mtp_get_object_handles()` function, set the parent object handle to 0 to search the root folder of the storage.

> **Note**  
> Because the object handle uses a value from another function as a parameter, manage the variable with care.

```
mtp_device_h mtp_device;
mtp_storage_h mtp_storage;

int
manager_test_get_object_handles(void)
{
    mtp_object_h *folder_list;
    mtp_object_h *file_list;
    int folder_count;
    int file_count;

    ret = mtp_get_object_handles(mtp_device, mtp_storage, MTP_FILETYPE_FOLDER, 0, &folder_list, &folder_count);
    dlog_print("ret[%d]: folder_count in root [%d]", ret, folder_count);

    for (i = 0; i < folder_count; i++) {
        ret = mtp_objectinfo_get_file_name(mtp_device, folder_list[i], &folder_name);
        dlog_print("ret[%d]: object handle [%d], folder name [%s]", ret, folder_list[i], folder_name);
    }

    ret = mtp_get_object_handles(mtp_device, mtp_storage, MTP_FILETYPE_JPEG, mtp_object, &file_list, &file_count);
    dlog_print("ret[%d]: file_count in root [%d]", ret, file_count);

    for (i = 0; i < file_count; i++) {
        ret = mtp_objectinfo_get_file_name(mtp_device, file_list[i], &file_name);
        dlog_print("ret[%d]: object handle [%d] file name [%s]", ret, file_list[i], file_name);
    }

    return ret;
}
```

> **Note**
>
> Depending on how you use this API, the performance of the application varies greatly. Typically, MTP transfer through the USB layer is not fast. In addition, larger files on the MTP device take a longer time for the function to handle.
>
> Rather than getting the object handles inside the device all at once, consider gradually obtaining them through user input. (It is easier to understand the MTP device when it is plugged into the computer.)

<a name="object_info"></a>
## Getting MTP Object Information

To obtain information on the MTP object, use the `mtp_objectinfo_get_XXX()` functions. To avoid memory leaks, free the character array variable with the `free()` function when no longer needed.

The following example retrieves the object file name:

```
mtp_device_h mtp_device; /* Get this variable using mtp_get_devices() */
mtp_object_h mtp_object; /* Get this variable using mtp_get_object_handles() */

int
objectinfo_test_get_filename(void)
{
    int ret = 0;
    char *name = NULL;

    ret = mtp_objectinfo_get_file_name(mtp_device, mtp_object, &name);
    dlog_print("ret[%d]: object id[%d] filename[%s]", ret, mtp_object, name);

    if (name != NULL)
        free(name);

    return ret;
}
```

<a name="object_and_thumbnail"></a>
## Getting the Object and Thumbnail

To get the object and thumbnail:

1. Get the object data from the MTP responder using the `mtp_get_object()` function:

   ```
   mtp_device_h mtp_device;
   mtp_object_h mtp_object_handle;

   int
   manager_test_get_object(void)
   {
       char filepath[100] = {0,};
       snprintf(filepath, 100, "/opt/usr/media/Downloads/JpegObject_%d.jpg", mtp_object_handle);

       ret = mtp_get_object(mtp_device, mtp_object_handle, filepath);
       dlog_print("ret[%d]: input id[%d]", ret, mtp_object_handle);

       return ret;
   }
   ```

2. If the file is an image file and has a thumbnail, import the thumbnail using the `mtp_get_thumbnail()` function:

   ```
   mtp_device_h mtp_device;
   mtp_object_h mtp_object_handle;

   int
   manager_test_get_object(void)
   {
       char filepath[100] = {0,};
       snprintf(filepath, 100, "/opt/usr/media/Downloads/JpegObject_%d.jpg", mtp_object_handle);

       ret = mtp_get_thumbnail(mtp_device, mtp_object_handle, filepath);
       dlog_print("ret[%d]: input id[%d]", ret, mtp_object_handle);

       return ret;
   }
   ```

<a name="events"></a>
## Managing MTP Events

To receive an event that occurred in the MTP initiator, add the event callback with the `mtp_add_mtp_event_cb()` function and define the callback.

The `event_parameter` parameter defines the type of the event:

- Device event type is `mtp_device_h`.
- Storage event type is `mtp_storage_h`.
- Object event type is `mtp_object_h`.

If the received event is `MTP_EVENT_TURNED_OFF`, the `event_parameter` parameter has no meaning. When this event occurs, free all MTP-related resources.

```
void
__test_mtp_event_cb(mtp_event_e state, int event_parameter, void *user_data)
{
    int ret = 0;
    dlog_print("state [%d]: %d", state, event_parameter);
    if (state == MTP_EVENT_DEVICE_ADDED || state == MTP_EVENT_DEVICE_REMOVED) {
        mtp_device_h mtp_device = (mtp_device_h) event_parameter;
        /* Do something */
    } else if (state == MTP_EVENT_STORAGE_ADDED || state == MTP_EVENT_STORAGE_REMOVED) {
        mtp_storage_h mtp_storage = (mtp_storage_h) event_parameter;
        /* Do something */
    } else if (state == MTP_EVENT_OBJECT_ADDED || state == MTP_EVENT_OBJECT_ADDED) {
        mtp_object_h mtp_object = (mtp_object_h) event_parameter;
        /* Do something */
    } else if (state == MTP_EVENT_TURNED_OFF) {
        ret = mtp_deinitialize();
        dlog_print("ret[%d]: Terminated daemon", ret);
    } else {
        /* Error handling */
    }
}

int
application_test_event_callback(void)
{
    int ret;

    ret = mtp_add_mtp_event_cb(__test_mtp_event_cb, NULL);

    return ret;
}
```

## Related Information
- Dependencies
  - Tizen 3.0 and Higher for Mobile
