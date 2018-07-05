# File Management

You can perform operations on files and directories stored in the device filesystem.

The File API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the File API include:

- Resolving the filesystem

  A basic step necessary to perform other file actions is to [resolve a filesystem](#resolving-filesystem-entries), which results in a `FileSystem` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#FileSystem), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#FileSystem), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#FileSystem) applications) being retrieved. You can use the `root` member to perform other actions on this filesystem.

- Operating on directories

  You can [create or remove a directory or file, or read all entries from a specific directory](#operating-on-directories).

- Operating on entries

  You can [get metadata, and move, copy, and remove entries](#operating-on-entries). You can also look up the parent directory of the entry or return the entry URL.

- Operating on files

  You can [access file details](#operating-on-files).

- Reading and writing file content

  You can [read file content, and create and write data to a file](#reading-and-writing-file-content). Using the file readers and writers, you can read Blob objects in a specific format (data URL, test, binary string, and array buffer).

## Prerequisites

To enable your application to use the file functionality:

1. To perform any Cordova-related operations, you must wait until Cordova is fully set up (the `deviceready` event occurs):

   ```
   document.addEventListener('deviceready', onDeviceReady, false);

   function onDeviceReady() {
       console.log('Cordova features now available');
   }
   ```

2. To use the File API (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

   ```
   <!--To read from files-->
   <tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
   <!--To write to files-->
   <tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>
   ```

## Resolving Filesystem Entries

To resolve the initial root for other filesystem operations:

- Use the `requestFileSystem()` global async method:

    - Define a callback for handling the success and failure of the operation:

      ```
      successCallback = function(fs) {
          console.log('File system name ' + fs.name);
      };

      errorCallback = function(err) {
          console.log(err.code);
      };
      ```

    - Call the method with the created callbacks. The filesystem request can use a temporary or persistent filesystem with a defined size.

      ```
      requestFileSystem(TEMPORARY, 1024*1024, successCallback, errorCallback);
      ```

    The following output is shown in the system log:
    ```
    File system name temporary
    ```

- Use the `resolveLocalFileSystemURL()` global async method.  
   This method is used to retrieve `DirectoryEntry` objects (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#DirectoryEntry), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#DirectoryEntry), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#DirectoryEntry) applications) or `FileEntry` objects (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#FileEntry), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#FileEntry), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#FileEntry) applications) using a local URI.

    - Define the callbacks:

        ```
        successCallback = function(entry) {
            console.log('Entry name ' + entry.name);
        };

        errorCallback = function(err) {
            console.log(err.code);
        };
        ```

    - Call the method with the provided valid URI for an existing file or directory:

        ```
        var uri = 'file:///home/owner/content/Documents/example.txt';
        resolveLocalFileSystemURL(uri, successCallback, errorCallback);
        ```

    The following output is shown in the system log:

    ```
    Entry name example.txt   
    ```

## Operating on Directories

To create directories and files, delete directories, and read entries within directories:

- To create a directory, you can use the `getDirectory()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getDirectory('ert', {create:true}, function(dir) {
          console.log('Created dir: ' + dir.name);
      });
  });
  ```

  If the third parameter is `{create:false}` or `NULL`, the entry of the existing directory is returned in the success callback.  
  The following output is shown in the system log:

  ```
  Created dir: ert
  ```

- To create a file, use the `getFile()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getFile('qa.txt', {create:true}, function(file) {
          console.log('Created file: ' + file.name);
      });
  });
  ```

  Similarly as when creating a directory, if the third parameter is `{create:false}` or `NULL`, the entry of the existing file is returned in the success callback.  
  The following output is shown in the system log:

  ```
  Created file: qa.txt
  ```

- To delete a directory and its entire content, you can use the `removeRecursively()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getDirectory('testDirectory', {create:true}, function(directoryEntry) {
          directoryEntry.removeRecursively(function() {
              console.log('success');
          });
      });
  });
  ```

  The following output is shown in the system log:

  ```
  success
  ```

- To read entries, first create a reader with the `createReader()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(entry) {
      entry.root.getDirectory('MyDocument', {create:true}, function(dirEntry) {
          var directoryReader = dirEntry.createReader();
      });
  });
  ```

  With the reader, you can read the next block of entries from the current directory with the `readEntries()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      var a = fs.root.createReader();
      a.readEntries(function successCallback(entries) {
          console.log('success');
      });
  });
  ```

  The following output is shown in the system log:

  ```
  success
  ```

## Operating on Entries

To move, copy, and delete entries, or access entry metadata, parent information, and URL:

- To look up metadata about an entry, you can use the `getMetadata()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getMetadata(function(metadata) {
          /* Get metadata successfully */
          console.log('Last modification time: ' + metadata.modificationTime);
      });
  });
  ```

  The following output is shown in the system log:

  ```
  Last modification time: Fri Jan 02 2015 03:58:08 GMT+0900 (KST)
  ```

- To move an entry to a different location in the file system, you can use the `moveTo()` method:

  ```
  successCallback = function(entry) {
      console.log('Full path to the moved file: ' + entry.fullPath)
  };
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getDirectory('testDirectory', {create:true}, function(direntry) {
          fs.root.getFile('aa.txt', {create:true}, function(fileentry) {
              console.log('Full path before move: ' + fileentry.fullPath);
              fileentry.moveTo(direntry, 'newname.txt', successCallback);
          });
      });
  });
  ```

  The following output is shown in the system log:

  ```
  Full path before move: /aa.txt
  Full path to the moved file: /testDirectory/newname.txt
  ```

- To copy an entry to a different location on the file system, you can use the `copyTo()` method:

  ```
  successCallback = function(entry) {
      console.log('Full path to the copied file: ' + entry.fullPath);
  };
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getDirectory('testDirectory', {create:true}, function(direntry) {
          fs.root.getFile('test.txt', {create:true}, function(fileentry) {
              fileentry.copyTo(direntry, 'newname.txt', successCallback);
          });
      });
  });
  ```

  The following output is shown in the system log:

  ```
  Full path to the copied file: /testDirectory/newname.txt
  ```

- To look up the parent directory entry containing the current entry, you can use the `getParent()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getParent(function(entry) {
          console.log('success');
      });
  });
  ```

  If the entry is the root of its filesystem, its parent is itself.  
  The following output is shown in the system log:

  ```
  success
  ```

- To delete a file or directory, you can use the `remove()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getFile('test.txt', {create: true}, function(fileEntry) {
          fileEntry.remove(function() {
              console.log('success');
          });
      });
  });
  ```

  > **Note**  
  > You cannot delete a non-empty directory or the filesystem root directory.

  The following output is shown in the system log:

  ```
  success
  ```

- To return a URL that can be used to identify the entry, you can use the `toURL()` method:

  ```
  requestFileSystem(TEMPORARY, 100, function(fs) {
      fs.root.getDirectory('testDirectory', {create:true}, function(entry) {
          var url = entry.toURL();
          console.log('URL: ' + url);
      });
  });
  ```

  The following output is shown in the system log:

  ```
  URL: file:///home/owner/apps_rw/WfigBlWDyf/tmp/testDirectory/
  ```

## Operating on Files

To create files, see [Resolving Filesystem Entries](#resolving-filesystem-entries). To create a writer for a file and access file details:

- To create a `FileWriter` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#FileWriter), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#FileWriter), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#FileWriter) applications), use the `createWriter()` method:

  ```
  var f; /* Must be a FileEntry object resolved using the methods presented before */
  f.createWriter(function(fileWriter) {
      console.log('created fileWriter object for ' + fileWriter.fileName);
  });
  ```

  The following output is shown in the system log:

  ```
  created fileWriter object for testFile.txt
  ```

- To access a `File` object (in [mobile](../../api/latest/device_api/mobile/tizen/cordova/file.html#File), [wearable](../../api/latest/device_api/wearable/tizen/cordova/file.html#File), and [TV](../../api/latest/device_api/tv/tizen/cordova/file.html#File) applications), use the `file()` method. The object represents the current state of the file.

  ```
  var f; /* Must be a FileEntry object resolved using methods presented before */
  f.file(function(file) {
      console.log('created file object for ' + file.name);
  });
  ```

  The following output is shown in the system log:

  ```
  created file object for example.txt
  ```

## Reading and Writing File Content

To read and write file content:

- To read a file and return the data as a base64-encoded data URL, you can use the `readAsDataURL()` method:

  ```
  var blob = new Blob(['abc']);
  var fileReader = new FileReader();
  fileReader.onload = function() {
      console.log('Loaded, result = ' + fileReader.result);
  };
  fileReader.readAsDataURL(blob);
  ```

  The following output is shown in the system log:

  ```
  Loaded, result = data:;base64,YWJj
  ```

- To read a file and return the data as a text, you can use the `readAsText()` method:

  ```
  var blob = new Blob(['abc']);
  var fileReader = new FileReader();
  fileReader.onload = function() {
      console.log('Loaded, result = ' + fileReader.result);
  };
  fileReader.readAsText(blob);
  ```

  The following output is shown in the system log:

  ```
  Loaded, result = abc
  ```

- To read a file and return the data as a binary string, you can use the `readAsBinaryString()` method:

  ```
  var blob = new Blob(['abc']);
  var fileReader = new FileReader();
  fileReader.onload = function() {
      console.log('Loaded, result = ' + fileReader.result);
  };
  fileReader.readAsBinaryString(blob);
  ```

  The following output is shown in the system log:

  ```
  Loaded, result = abc
  ```

- To read a file and return the data as an array buffer (`byte[]`), you can use the `readAsArrayBuffer()` method:

  ```
  var blob = new Blob(['abc']);
  var fileReader = new FileReader();
  fileReader.onload = function() {
      resultValue = fileReader.result;
      console.log('Result: ' + resultValue.toString() + ' ' + 'ByteLength: ' + resultValue.byteLength);
  };
  fileReader.readAsArrayBuffer(blob);
  ```

  The following output is shown in the system log:

  ```
  Result: [object ArrayBuffer]
  ByteLength: 3
  ```

- To abort the current operation of reading a file, you can use the `abort()` method:

  ```
  var blob = new Blob(['abc']);
  var fileReader = new FileReader();
  fileReader.onload = function() {
      console.log('Loaded');
  };
  fileReader.onabort = function() {
      console.log('aborted');
  };
  fileReader.readAsDataURL(blob);
  fileReader.abort();
  ```

  The following output is shown in the system log:

  ```
  aborted
  ```

- To write data to a file, you can use the `write()` method:

  ```
  successCallback = function(writer) {
      writer.onwrite = function(evt) {
          console.log('write success');
      };
      writer.write('some sample text');
  };
  errorCallback = function(err) {
      console.log(err.code);
  };
  /* Entry is a FileEntry object retrieved by getFile() of the DirectoryEntry interface */
  entry.createWriter(successCallback, errorCallback);
  ```

  The following output is shown in the system log:

  ```
  write success
  ```

- To move the file pointer to a specified byte, you can use the `seek()` method:

  ```
  successCallback = function(writer) {
      /* Fast forwards the file pointer to the end of file */
      writer.seek(writer.length);
  };

  errorCallback = function(err) {
      console.log(err.code);
  };

  /* Entry is a FileEntry object retrieved by getFile() of the DirectoryEntry interface */
  entry.createWriter(successCallback, errorCallback);
  ```

- To shorten the file to the specified length, you can use the `truncate()` method:

  ```
  successCallback = function(writer) {
      writer.onwrite = function(evt) {
          console.log('truncate success');
      };
      writer.truncate(10);
  };

  errorCallback = function(err) {
      console.log(err.code);
  };

  /* Entry is a FileEntry object retrieved by getFile() of the DirectoryEntry interface */
  entry.createWriter(successCallback, errorCallback);
  ```

  The following output is shown in the system log:

  ```
  truncate success
  ```

- To abort writing a file, you can use the `abort()` method:

  ```
  successCallback = function(writer) {
      writer.onwrite = function(evt) {
          console.log('write success');
      };
      writer.onabort = function(e) {
          console.log('abort');
      };
      writer.write('some sample text');
      writer.abort();
  };

  errorCallback = function(err) {
      console.log(err.code);
  };

  /* Entry is a FileEntry object retrieved by getFile() of the DirectoryEntry interface */
  entry.createWriter(successCallback, errorCallback);
  ```

  The following output is shown in the system log:

  ```
  abort
  ```

## Related Information
* Dependencies
  - Tizen 3.0 and Higher for Mobile
  - Tizen 3.0 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
