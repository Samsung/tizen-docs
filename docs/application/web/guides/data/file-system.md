# File System

You can [access the files and directories](#file-and-directory-access) in the device file system.

The Filesystem API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The Filesystem API provides access to accessible parts of the file system, which are represented as [virtual root locations](#supported-virtual-roots).

The main features of the Filesystem API include:

- File storage management   

  You can [manage different storages](#managing-file-storages) on the device and retrieve additional information about the storages, including listing available storages and receiving storage change notifications.

- Files and directory management   

  You can [perform basic file and directory management tasks](#managing-files-and-directories) using the `File` interface:

  - You can [create files and directories](#creating-and-deleting-files-and-directories) in the file system.
  - You can [retrieve a list of files in a directory](#retrieving-files-and-file-details), the URI of a file, or the file content as a `DOMString`.
  - You can [read or write to a file](#managing-files-and-directories).
  - You can [copy and move files and directories](#managing-files-and-directories) within the virtual file system.
  - You can [delete files and directories](#creating-and-deleting-files-and-directories) from the virtual file system.

## File and Directory Access

You can access the virtual file system using the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications):

- To access a file or directory within the virtual file system, you must use the fully qualified path, `<root name>/<path>`, where `<rootname>` is the name of the virtual root and `<path>` is the relative path to the file or directory within the root.

   > **Note**  
   > When you use a path to access the device file system, make sure that the file path encoding uses the default encoding of the platform.

- To access a file or directory, you must also retrieve a file handle using the `resolve()` method of the `FileSystemManager` interface.  
  A file handle is a reference object that points to and represents a file or directory.

The `isFile` and `isDirectory` attributes of the `File` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#File), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#File), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#File) applications) identify the type of the object: for example, for a file, the `isFile` attribute is set to `true` and the `isDirectory` attribute to `false`.

## Prerequisites

To use the Filesystem API (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
<tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>
```

## Managing File Storages

You can manage different storages on the device with the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications).

You can retrieve additional information about the storages, including listing available storages and receiving storage change notifications with the `listStorages()` and `addStorageStateChangeListener()` methods provided by the `FileSystemManager` interface.

To manage file storages:

1. To list available storages, use the `listStorages()` method of the `FileSystemManager` interface to search for the storages available on the device.

   If the search is successful, a list of found `FileSystemStorage` objects (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemStorage), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemStorage), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemStorage) applications) is passed to the success event handler.

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

2. To get storage details by storage name (the `label` attribute), use the `getStorage()` method.

   The success callback receives the `FileSystemStorage` object containing the storage details as an input parameter.

   ```
   /* Success event handler */
   function onStorage(storage) {
       console.log('Storage found:' + storage.label);
   }

   /* Retrieve a storage */
   tizen.filesystem.getStorage('music', onStorage);
   ```

3. To receive notifications on the storage state changes, for example, additions and removals, register an event handler with the `addStorageStateChangeListener()` method.

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

4. To stop receiving the notifications, use the `removeStorageStateChangeListener()` method:

   ```
   tizen.filesystem.removeStorageStateChangeListener(watchID);
   ```

## Creating and Deleting Files and Directories

You can create files and directories using the `createFile()` and `createDirectory()` methods. The file or directory is created relative to the current directory that the operation is performed on.

> **Note**  
> Do not use "." or ".." characters in the directory or file path components.

To create and delete files and directories:

1. To create a file in the current directory, use the `createFile()` method of the `File` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#File), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#File), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#File) applications):

   ```
   var documentsDir, newFile;
   tizen.filesystem.resolve('documents', function(result) {
       documentsDir = result;
       newFile = documentsDir.createFile('newFilePath');
   });
   ```

2. To create a directory within the file system, use the `createDirectory()` method.

   The directory (and any sub-directories defined in the method parameter) is created relative to the current directory where the operation is performed on.

   ```
   var newDir = documentsDir.createDirectory('newDir');
   var anotherNewDir = documentsDir.createDirectory('newDir1/subNewDir1');
   ```

3. To delete a file, use the `deleteFile()` method:

   ```
   function onDelete() {
       console.log('deletedFile() is successfully done.');
   }

   documentsDir.deleteFile(newFile.fullPath, onDelete);
   ```

4. To delete a directory, use the `deleteDirectory()` method.

   The second parameter defines whether the deletion is performed recursively for the sub-directories as well. If the parameter is set to `false`, the directory is deleted only if it is empty.

   ```
   documentsDir.deleteDirectory(newDir.fullPath, false, onDelete);
   anotherNewDir.parent.deleteDirectory(anotherNewDir.fullPath, false, onDelete);
   ```

## Retrieving Files and File Details

You can retrieve a list of files or file URIs using the `listFiles()` and `toURI()` methods. The URI can be used to identify the file, for example, by using it as the `src` attribute on an HTML `img` element.

You can retrieve file content as a `DOMString` with the `readAsText()` method. The encoding input parameter of the method defines the format in which the file content is returned.

To get files and file details from the file system:

1. To access a specific file or directory within the file system, retrieve a file handle using the `resolve()` method of the `FileSystemManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileSystemManager), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileSystemManager), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileSystemManager) applications):

   ```
   tizen.filesystem.resolve('documents', onResolveSuccess, null, 'r');
   ```

   The `File` object (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#File), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#File), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#File) applications) is returned in the success event handler.

2. To retrieve a list of all the files and their directories located in a specified directory, use the `listFiles()` method of the `File` object:

   ```
   function onResolveSuccess(dir) {
       dir.listFiles(onsuccess);
   }
   ```
   
   The method returns an array of `File` objects.

3. To retrieve the file URI, use the `toURI()` method:

   ```
   function onsuccess(files) {
       for (var i = 0; i < files.length; i++) {
           /* Display the file name and URI */
           console.log('File name is ' + files[i].name + ', URI is ' + files[i].toURI());
   ```

4. To retrieve the file content as a DOMString, use the `readAsText()` method.

   The encoding input parameter of the method defines the format in which the file content is returned.

   ```
           if (files[i].isDirectory == false) {
               files[i].readAsText(function(str) {
                   console.log('File content: ' + str);
               }, null, 'UTF-8');
           }
       }
   }
   ```

## Managing Files and Directories

You can manage files and directories in many ways:

- You can read and write to a file by first using the `openStream()` method to open the file. You can specify the file mode and encoding.  
   The `openStream()` method returns a `FileStream` object (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileStream), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileStream), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileStream) applications), which is a handle to the opened file. All actual operations, such as read, write, or close, on the file are performed through the `FileStream` object based on a position attribute, which represents the current position in the file.
 - You can copy and move files and directories within the virtual file system with the `copyTo()` and `moveTo()` methods.  
    If a file or directory of the same name already exists in the target location, the overwrite input parameter of the method defines whether the existing file is overwritten.
	> **Note**  
	> The file or directory to be copied or moved must be located under the current directory.

To read and write to files, and move and copy files and directories:

1. To open a file, use the `openStream()` method of the `File` interface (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#File), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#File), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#File) applications).

   The method returns a `FileStream` object, which is a handle to the opened file.

   ```
   var documentsDir;

   tizen.filesystem.resolve('documents', function(result) {
       documentsDir = result;
   });

   var testFile = documentsDir.createFile('test.txt');
   if (testFile != null) {
       testFile.openStream('rw', onOpenSuccess, null, 'UTF-8');
   }
   ```

2. Perform all actual operations, such as reading, writing, or closing, on the file through the `FileStream` object based on a position attribute, which represents the current position in the file:
   ```
   function onOpenSuccess(fs) {
       /* Write HelloWorld to the file */
       fs.write('HelloWorld');

       /* Move pointer to the beginning */
       fs.position = 0;

       /* Read the file content from the beginning */
       fs.read(testFile.fileSize);

       /* Close the file */
       fs.close();
   }
   ```

3. To copy a file or directory, use the `copyTo()` method. The following example copies the files to the `images/backup/` directory. Since the third parameter is set to `true`, any existing files with the same name in the target directory are overwritten.

   ```
   var files; /* Assume that this is an array of File objects */
   function onSuccess() {
       console.log('success');
   }

   for (var i = 0; i < files.length; i++) {
       documentsDir.copyTo(files[i].fullPath, 'images/backup/' + files[i].name,
                           true, onSuccess);
   }
   ```

4. To move a file or directory, use the `moveTo()` method. The following example moves the files to the `images/newFolder/` directory. Since the third parameter is set to `false`, no existing files with the same name in the target directory are overwritten.

   ```
   var files; /* Assume that this is an array of File objects */

   for (var i = 0; i < files.length; i++) {
       documentsDir.moveTo(files[i].fullPath, 'images/newFolder/' + files[i].name,
                           false, onSuccess);
   }
   ```

## Supported Virtual Roots

The virtual roots form a collection of locations that function as a single virtual device file system. The following table lists the supported virtual roots.

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
