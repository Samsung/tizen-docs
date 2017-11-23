Storages
========

## Dependencies

- Tizen 4.0 and Higher

You can access storage information and manage directories within certain
parts of the file system, represented as [virtual root
locations](#virtualroots). These virtual roots form a collection of
locations that function as a single virtual device file system.

The main features of the `Tizen.System.Storage` class include:

-   Storage management

    You can manage different storage locations on the device.

    You can [retrieve additional information about the storage
    locations](#storage), including which storage is supported on the
    device, using the
    [Tizen.System.StorageManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1StorageManager.html) class.
    You can also [monitor storage state changes](#state).

- Storage space management

    You can [get the available and total size](#space) of the storage.


Prerequisites
-------------

To use the methods and properties of the
[Tizen.System.Storage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Storage.html)
and
[Tizen.System.StorageManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1StorageManager.html)
classes, include the
[Tizen.System](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html)
namespace in your application:

``` {.prettyprint}
using Tizen.System;
```


Retrieving Storage Information <a id="storage"></a>
------------------------------

To retrieve storage information:

1.  Retrieve all storages on a device by using the `Storages` property
    of the
    [Tizen.System.StorageManager](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1StorageManager.html)
    class, which returns a list of all device storages as instances of
    the
    [Tizen.System.Storage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Storage.html)
    class:

    ``` {.prettyprint}
    var storages = StorageManager.Storages;
    var internalStorage = storages.Where(s => s.StorageType == StorageArea.Internal).FirstOrDefault();
    ```

2. Get information about each storage instance:
    -   Get the ID of a specific storage by using the `Id` property:

        ``` {.prettyprint}
        var result = internalStorage.Id;
        ```

    - Get the root directory of a specific storage by using the
        `RootDirectory` property:

        ``` {.prettyprint}
        var result = internalStorage.RootDirectory;
        ```

    - Get the directory path for a storage of a specific type.

        The `GetAbsolutePath()` method of the `Tizen.System.Storage`
        class retrieves the absolute path to a storage of a particular
        type, which is defined by the values of the
        [Tizen.System.DirectoryType](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html#a31be3bb6e3bebcfb2d3a6c5c7a66fe37) enumeration.

        To get the directories of all storage types:

        ``` {.prettyprint}
        foreach (DirectoryType directoryType in Enum.GetValues(typeof(DirectoryType)))
        {
            var result = internalStorage.GetAbsolutePath(directoryType);
        }
        ```

    - Get the storage type of a specific storage by using the
        `StorageType` property, which takes values from the
        [Tizen.System.StorageArea](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html#a5c408f85972f9b602d72d299549297e7)
        enumeration:

        ``` {.prettyprint}
        var result = internalStorage.StorageType;
        ```

    - Get the mount state of a specific storage by using the `State`
        property, which takes values from the
        [Tizen.System.StorageState](https://developer.tizen.org/dev-guide/csapi/namespaceTizen_1_1System.html#a8d686e878c0ffed2d2b0ccf0eaf52e33)
        enumeration:

        ``` {.prettyprint}
        var result = internalStorage.State;
        ```


Monitoring Storage State Changes <a id="state"></a>
--------------------------------

To monitor storage state changes:

1.  Define an event handler, which is called when the storage state
    changes:

    ``` {.prettyprint}
    EventHandler storageEventHandler = (s, e) =>
    {
        var storage = s as Storage;
        if (storage == null)
        {
            return;
        }
        if (storage.State == StorageState.Unmountable)
        {
            unmountableStateAchieved = true;
        }
    };
    ```

    The event handler checks whether storage can be mounted or is
    corrupted and unmountable.

2. Register the event handler for the `StorageStateChanged` event of
    the
    [Tizen.System.Storage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Storage.html)
    class:

    ``` {.prettyprint}
    foreach (var storage in StorageManager.Storages)
    {
        storage.StorageStateChanged += storageEventHandler;
    }
    ```

3. When no longer needed, deregister the event handler:

    ``` {.prettyprint}
    foreach (var storage in StorageManager.Storages)
    {
        storage.StorageStateChanged -= storageEventHandler;
    }
    ```


Retrieving Storage Space Information <a id="space"></a>
------------------------------------

To get the available and total size of the storage, use the `TotalSpace`
and `AvailableSpace` properties in the
[Tizen.System.Storage](https://developer.tizen.org/dev-guide/csapi/classTizen_1_1System_1_1Storage.html)
class. For internal storage, they return the storage size, excluding the
minimum memory size to launch the low memory pop-up in a low memory
situation. Consequently, the available size must be less than the
original available size, and you must use these properties to get the
memory size.

To retrieve storage space information:

-   Get the total space of the storage by using the `TotalSpace`
    property, which returns the total space of the given storage in
    bytes:

    ``` {.prettyprint}
    var storages = StorageManager.Storages;
    var internalStorage = storages.Where(s => s.StorageType == StorageArea.Internal).FirstOrDefault();
    var result = internalStorage.TotalSpace;
    ```

- Get the available space of the storage by using the `AvailableSpace`
    property, which returns the available space of the given storage in
    bytes:

    ``` {.prettyprint}
    var storages = StorageManager.Storages;
    var internalStorage = storages.Where(s => s.StorageType == StorageArea.Internal).FirstOrDefault();
    var result = internalStorage.AvailableSpace;
    ```


Virtual Roots <a id="virtualroots"></a>
-------------

The following table lists the supported virtual roots.

**Table: File system virtual roots**

| Virtual root | Description                              |
| ------------ | ---------------------------------------- |
| `Images`     | Location for storing images.             |
| `Sounds`     | Location for storing sound files.        |
| `Videos`     | Location for storing video files.        |
| `Camera`     | Location for storing photos.             |
| `Downloads`  | Location for storing downloaded items.   |
| `Music`      | Location for storing audio files.        |
| `Documents`  | Location for storing documents.          |
| `Others`     | Location for storing other files.        |
| `Ringtones`  | Location for ringtones (read-only location). |