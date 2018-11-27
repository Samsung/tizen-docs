# File System

> **Note**  
> 
> With the introduction of Tizen version 5.0, the Filesystem API has undergone a major overhaul. Many of the existing methods are deprecated and new methods are introduced. For information on the previous versions of API, see [Deprecated Filesystem Guide](./file-system-old.md). This guide explains about the APIs for Tizen 5.0 and its newly introduced methods.


You can [access the files and directories](#file-and-directory-access) in the device file system.

The Filesystem API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The Filesystem API provides access to accessible parts of the file system, which are represented as [virtual root locations](#supported-virtual-roots).

The main features of the Filesystem API include:

- File storage management

  You can [manage different storages](#manage-file-storages) on the device and retrieve additional information about the storages, which includes listing available storages and receiving storage change notifications.

- Files and directory management

  You can [perform basic file and directory management tasks](#manage-files-and-directories) using the `File` interface:

  - You can [create and delete directories](#create-and-delete-directories) in the file system.
  - You can [delete files](#delete-files) from the virtual file system.
  - You can [retrieve a list of files in a directory](#retrieve-files-and-file-details), the URI of a file, or the file content as a `DOMString`.
  - You can [read or write to a file](#manage-files-and-directories).
  - You can [copy and move files and directories](#manage-files-and-directories) within the virtual file system.

## File and Directory Access

You can access the virtual file system using the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications):

- To access a file or directory within the virtual file system, you can use the fully qualified path, `<rootname>/<path>`, where `<rootname>` is the name of the virtual root and `<path>` is the relative path to the file or directory within the root. Alternatively, you can use the absolute path to a file located in the target device memory. Regardless of virtual root usage, rights to access file location as well as rights to read and write to a file are needed when applicable.

  > **Note**
  >
  > When you use a path to access the device file system, ensure that the file path encoding uses the default encoding of the platform.

## Prerequisites

To use the Filesystem API (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
<tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>
```

## Manage File Storages

You can manage different storages on the device with the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications).

You can retrieve additional information about the storages, including listing available storages and receiving storage change notifications with the `listStorages()` and `addStorageStateChangeListener()` methods provided by the `FileSystemManager` interface.

To manage file storages:

- To list available storages, use the `listStorages()` method of the `FileSystemManager` interface to search for the storages available on the device.

   If the search is successful, the list of found `FileSystemStorage` objects (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemStorage), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemStorage), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemStorage) applications) is passed to the success event handler.

   ```
   /* Success event handler */
   function checkCorruptedRemovableDrives(storages) {
       for (var i = 0; i < storages.length; i++) {
           if (storages[i].type != 'EXTERNAL')
               continue;
           if (storages[i].state == 'UNMOUNTABLE')
               console.log('External drive ' + storages[i].label + ' is corrupted.');
       }
   }

   /* Search for the storages */
   tizen.filesystem.listStorages(checkCorruptedRemovableDrives);
   ```

- To get storage details by storage name (the `label` attribute), use the `getStorage()` method.

   The success callback receives the `FileSystemStorage` object containing the storage details as an input parameter.

   ```
   /* Success event handler */
   function onStorage(storage) {
       console.log('Storage found:' + storage.label);
   }

   /* Retrieve a storage */
   tizen.filesystem.getStorage('music', onStorage);
   ```

- To receive notifications on the storage state changes, for example, additions and removals, register an event handler with the `addStorageStateChangeListener()` method.

   An event is generated each time the storage state changes.

   ```
   var watchID;

   /* Define the event handler */
   function onStorageStateChanged(storage) {
       if (storage.state == 'MOUNTED')
           console.log('Storage ' + storage.label + ' was added!');
   }

   /* Register the event handler */
   watchID = tizen.filesystem.addStorageStateChangeListener(onStorageStateChanged);
   ```

- To stop receiving the notifications, use the `removeStorageStateChangeListener()` method.

   ```
   tizen.filesystem.removeStorageStateChangeListener(watchID);
   ```

## Create and Delete Directories

You can create directories using the `createDirectory()` method. The directory is created at `path` specified in parameter.
You can delete directories using  `deleteDirectory()` method. Target pointed by the path specified will be deleted from the file system.

- To create a directory within the file system, use the `createDirectory()` method.

   The directory is created, in destination pointed by `path` and successCallback function should be called. If directory can not be created for some reason, the errorCallback is called and error message can be logged.

   ```
   var newPath = 'documents/subDir'
   var successCallback = function(newPath) {
       console.log('New directory has been created: ' + newPath);
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.createDirectory('documents/newDir',successCallback, errorCallback);
   ```

- To delete a directory, use the `deleteDirectory()` method.

   The second parameter defines whether the deletion is performed recursively for the sub-directories as well. If the parameter is set to `false`, the directory is deleted only if it is empty.

   ```
   var fullPath = 'documents/subDir'
   var callback = function(modifiedDirectory) {
       console.log('deleteDirectory() is successfully done. Modified (parent) directory: ' + modifiedDirectory);
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.deleteDirectory(fullPath, true, callback, errorCallback);
   ```

## Delete Files

You can create directories using the `createDirectory()` method. The directory is created at the `path` specified in the parameter.
You can delete files using the `deleteFile()` method. Target pointed by the path specified will be deleted from the file system.

- To delete a file, use the `deleteFile()` method:

   ```
   var fullPath = 'documents/file_to_be_deleted.txt'
   var callback = function(modifiedDirectory) {
       console.log('deleteFile() is successfully done. Modified (parent) directory: ' + modifiedDirectory);
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.deleteFile(fullPath, callback, errorCallback);
   ```

## Retrieve Files and File Details

You can retrieve a list of files or file URIs using the `listDirectory()` and `toURI()` methods. The URI can be used to identify the file, for example, by using it as the `src` attribute on an HTML `img` element.

- To retrieve a list of all files and directories located in a specified directory, use the `listDirectory()` method of the `filesystem` object. The method returns an array of `DOMString` elements, each being a path with name of file inside a directory pointed by `path`.

   ```
   function onsuccess(files) {
       for (var i = 0; i < files.length; i++) {
           /* Display the file path with name */
           console.log('File path and name is: ' + files[i]);
       }
   }
   function onerror(error) {
       console.log(error);
   }
   tizen.filesystem.listDirectory('documents/subDir', onsuccess, onerror);
   ```

- To retrieve the file URI, use the `toURI()` method.

   ```
   function onsuccess(files) {
       for (var i = 0; i < files.length; i++) {
           /* Display the file URI */
           console.log('File URI is: ' + toURI(files[i]));
       }
   }
   function onerror(error) {
       console.log(error);
   }
   tizen.filesystem.listDirectory('documents/subDir', onsuccess, onerror);
   ```

- To retrieve the file content as a `DOMString`, binary data or to put its contents to a `Blob` object, use one of the following functions on `FileHandle` object opened in modes appropriate for reading ('r', 'rw'):

   - Firstly, open a file using the `openFile()` function with the `mode` parameter allowing to read its contents.
      ```
      /* Opening file for read - this code assumes that there is */
      /* a file named 'file' in documents directory */
      var fileHandleRead = tizen.filesystem.openFile('documents/file', 'r');
      console.log('File opened for reading');
      ```

   - Use readString() or readStringNonBlocking() to retrieve the file content as a DOMString.
      ```
      var fileContents = fileHandleRead.readString();
      console.log('File contents: ' + fileContents);
      ```

   - Use readData() or readDataNonBlocking() to retrieve the file content as a Uint8Array object (binary data).
      ```
      var fileContents = fileHandleRead.readData();
      console.log('File binary contents in array:');
      console.log(fileContents);
      ```

   - Use readBlob() or readBlobNonBlocking() to retrieve the file content as a Blob object.
      ```
      var fileContents = fileHandleRead.readBlob();
      console.log('Blob object:');
      console.log(fileContents);
      /* FileReader is a W3C API class, not related to webapi-plugins */
      /* and is capable of extracting blob contents */
      var reader = new FileReader();
      /* Event fires after the blob has been read/loaded */
      reader.addEventListener('loadend', function(contents)
      {
         const text = contents.srcElement.result;
         console.log('File contents: ' + text);
      });
      /* Start reading the blob as text */
      reader.readAsText(fileContentsInBlob);
      ```

   - Close the file when it is not in use.
       ```
       fileHandleRead.close();
       ```

> **Note**
>
> When you use readString(), readData(), readBlob() or one of their NonBlocking equivalent, FileHandle position is set right where the reading operation ended. To read file again from the beggining, use seek() method on FileHandle object.

## Manage Files and Directories

You can manage files and directories in many ways:

- You can read and write to a file by first using the `openFile()` method to open the file. You can specify the file mode. The `openFile()` method returns a `FileHandle` object (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileHandle), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileHandle), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileHandle) applications), which is a handle to the opened file. All actual operations, such as read, write, or close, on the file are performed through the `FileHandle` object based on a curent position, which can be obtained or modified through calling `seek()` operation on `FileHandle` object.

To write to files:

- To open or create a file, use the `openFile()` method of the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications).

   The method returns a `FileHandle` object, which is a handle to the opened or newly created file.

   > **Note**
   >
   > openFile() method used with mode 'w' creates new file or opens existing file and erases its contents. Any data contained in a file opened in that mode will be lost.

   Perform all actual operations, such as reading, writing, or closing on the file through the `FileHandle` object based on a current position, which can be obtained or modified through calling `seek()` operation on `FileHandle` object.

   ```
   /* Opening file for write - file is created if not exists, */
   /* otherwise existing file is truncated */
   var fileHandleWrite = tizen.filesystem.openFile('documents/file', 'w');
   console.log('File opened for writing');
   ```

   - use writeString() or writeStringNonBlocking() to write `DOMString` to file.
   ```
   var stringToWrite = 'example string';
   fileHandleWrite.writeString(stringToWrite);
   ```

   - use writeData() or writeDataNonBlocking() to write `Uint8Array` object contents to file.
   ```
   var arrayToWrite = new Uint8Array([11,22,88,99]);
   fileHandleWrite.writeData(arrayToWrite);
   ```

   - use writeBlob() or writeBlobNonBlocking() to write `Blob` object contents to file.
   ```
   var blobToWrite = new Blob(['example blob content']);
   fileHandleWrite.writeBlob(blobToWrite);
   ```

   - Close the file when it is not in use.
   ```
   fileHandleRead.close();
   ```
 You can copy, move and rename files and directories within the file system with the `copyFile()`, `copyDirectory()`, `moveFile()`, `moveDirectory()` and `rename()` methods. During copy or move operations, if a file or directory of the same name already exists in the target location, the overwrite input parameter of the method defines whether the existing file is overwritten.

 - To copy a file, use the `copyFile()` method. The following example copies the file to the `images` directory. Since the third parameter is set to `true`, any existing file or directory with the same name in the target directory is overwritten:

   ```
   var filePathAndName = 'documents/exampleFile.jpg';
   var destination = 'images/copyOfExampleFile.jpg';
   function onSuccess() {
       console.log('success');
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.copyFile(filePathAndName, destination, true, onSuccess, errorCallback);
   ```

- To copy a directory, use the `copyDirectory()` method. The following example copies the directory to the `documents/` directory. Since the third parameter is set to `true`, any existing file or directory with the same name in the target directory is overwritten:

   ```
   var directoryPathAndName = 'downloads/exampleDirectory';
   var destination = 'documents/copyOfExampleDirectory';
   function onSuccess() {
       console.log('success');
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.copyDirectory(directoryPathAndName, destination, true, onSuccess, errorCallback);
   ```

- To move a file, use the `moveFile()` method. The following example moves the files to the `music/` directory. Since the third parameter is set to `false`, no existing files with the same name in the target directory are overwritten:

   ```
   var filePathAndName = 'downloads/exampleFile.mp3';
   var destination = 'music';
   function onSuccess() {
       console.log('success');
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.moveFile(filePathAndName, destination, true, onSuccess, errorCallback);
   ```

- To move a directory, use the `moveDirectory()` method. The following example moves the directory to the `camera/` directory. Since the third parameter is set to `true`, existing file or directory with the same name in the target directory is overwritten:

   ```
   var directoryPathAndName = 'documents/exampleDirectory';
   var destination = 'camera';
   function onSuccess() {
       console.log('success');
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.moveDirectory(directoryPathAndName, destination, true, onSuccess, errorCallback);
   ```

- To rename either a file or a directory, use the `rename()` method. The following example changes file name to the `newName.txt`:

   ```
   var filePathAndName = 'documents/exampleFile.txt';
   var newName = 'newName.txt';
   function onSuccess() {
       console.log('success');
   }
   var errorCallback = function(error) {
       console.log(error);
   }
   tizen.filesystem.rename(filePathAndName, newName, onSuccess, errorCallback);
   ```


## Supported Virtual Roots

The virtual roots form a collection of locations that function as a single virtual device file system. The following table lists the supported virtual roots:

**Table: Filesystem virtual roots**

| Virtual root      | Description                              |
| ----------------- | ---------------------------------------- |
| `camera`          | Location for storing pictures and videos taken by a device (supported since Tizen 2.3). |
| `documents`       | Location for storing documents.          |
| `downloads`       | Location for storing downloaded items.   |
| `images`          | Location for storing images.             |
| `music`           | Location for storing audio files.        |
| `ringtones`       | Location for ringtones (read-only location).<br>**Note**<br>The `ringtones` virtual root is not supported on TV devices. |
| `videos`          | Location for storing videos.             |
| `wgt-package`     | Location for storing Web application packages (read-only location). |
| `wgt-private`     | Location for the Web application private storage. |
| `wgt-private-tmp` | Location for the Web application private temporary storage. |


## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
