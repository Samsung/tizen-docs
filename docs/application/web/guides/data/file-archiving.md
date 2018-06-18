# File Archiving

You can manage ZIP archives and operate on the archived files.

The Archive API is mandatory for Tizen mobile, wearable, and TV profiles, which means that it is supported on all mobile, wearable, and TV devices. All mandatory APIs are supported on the Tizen Emulators.

The main features of the Archive API include:

- Accessing archive content   

  You can [read the content of an archive file](#reading-the-content-of-an-archive).

- Creating new archives

  You can [create archive files and add files into them](#creating-an-archive).

- Extracting archived files

  You can [extract a single file or all files from an archive file](#extracting-files-from-an-archive).

- Aborting operations

  You can [abort an on-going archive operation](#aborting-file-operations).

To start any kind of ZIP operation (packing or unpacking), you must first call the `open()` method of the `ArchiveManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveManager), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveManager), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveManager) applications). The first parameter is a `FileReference` object (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#FileReference), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#FileReference), and [TV](../../api/latest/device_api/tv/tizen/archive.html#FileReference) applications), which can be a `File` object (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#File), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#File), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#File) applications) or the virtual path. The second parameter is a `FileMode` enumerator (in [mobile](../../api/latest/device_api/mobile/tizen/filesystem.html#FileMode), [wearable](../../api/latest/device_api/wearable/tizen/filesystem.html#FileMode), and [TV](../../api/latest/device_api/tv/tizen/filesystem.html#FileMode) applications), whose values are described in the following table.

**Table: File modes**

| Mode | Description                              |
| ---- | ---------------------------------------- |
| `r`  | Use this mode to extract or get information about the archive file content.<br> The file must exist, or the `NotFoundError` exception occurs. <br> When the archive file is opened in this mode, the `add()` method is not available. |
| `w`  | Use this mode to create an archive file and add files to it. <br> If the file does not exist, it is created. If it exists and the `overwrite` option is `true`, the existing file is overwritten with an empty archive. If the file exists and the `overwrite` option is `false`, the error callback is invoked. <br> When the archive file is opened in this mode, the `getEntries()`, `getEntryByName()`, and `extractAll()` methods are not available. |
| `rw` | Use this mode to zip or unzip an archive file. <br> If the file does not exist, it is created. If it exists and the `overwrite` option is `true`, the existing file is overwritten with an empty archive. If the file exists and the `overwrite` option is `false`, the existing content is preserved, and both adding and extracting are available. |
| `a`  | Use this mode to add new files to an archive file. <br> If the file does not exist, it is created. If it exists, the previous content of the archive file is preserved and new files can be added. <br> When the archive file is opened in this mode, the `getEntries()`, `getEntryByName()`, and `extractAll()` methods are not available. |

## Prerequisites

To use the Archive API (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html), [wearable](../../api/latest/device_api/wearable/tizen/archive.html), and [TV](../../api/latest/device_api/tv/tizen/archive.html) applications), the application has to request permission by adding the following privileges to the `config.xml` file:

```
<tizen:privilege name="http://tizen.org/privilege/filesystem.read"/>
<tizen:privilege name="http://tizen.org/privilege/filesystem.write"/>
```

## Reading the Content of an Archive

Opening an archive and accessing a list of its members is a basic archive management skill:

1. To access the archive file, use the `open()` method of the `ArchiveManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveManager), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveManager), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveManager) applications). The provided callback receives an `ArchiveFile` object (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveFile), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveFile), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveFile) applications).

   ```
   var myArchive = null;
   function openSuccess(arch) {
       console.log('ArchiveFile mode: ' + arch.mode);
       myArchive = arch;
   }
   tizen.archive.open('downloads/archive.zip', 'r', openSuccess);
   ```

2. Get the list of all files contained inside the archive using the `getEntries()` method of the `ArchiveFile` interface.

   ```
   function listSuccess(members) {
       if (members.length === 0) {
           console.log('The archive is empty');

           return;
       }
       console.log('Files in the archive:')
       for (var i = 0; i < members.length; i++) {
           console.log(members[i].name);
       }
   }
   myArchive.getEntries(listSuccess);
   ```

3. After the work with the archive is finished, close the archive  using the `close()` method of the `ArchiveFile` interface.

   ```
   archive.close();
   ```

## Creating an Archive

Creating an archive and adding files to it is a basic archive management skill:

1. To create the archive file, use the `open()` method of the `ArchiveManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveManager), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveManager), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveManager) applications) and set the mode as `w`:

   ```
   tizen.archive.open('downloads/new_archive.zip', 'w', createSuccess);
   ```

2. Add a file to the archive using the `add()` method. The file can be specified using a virtual path:

   ```
   function progressCallback(opId, val, name) {
       console.log('opId: ' + opId + ' with progress val: ' + (val * 100).toFixed(0) + '%');
   }
   function successCallback() {
       console.log('File added');
   }
   function createSuccess(archive) {
       archive.add('downloads/file.txt', successCallback, null, progressCallback);
   }
   ```

## Extracting Files from an Archive

Extracting a file from an archive is a basic archive management skill:

1. To access an archive file, use the `open()` method of the `ArchiveManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveManager), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveManager), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveManager) applications). The "r" mode is suitable for extracting from the archive.

   ```
   tizen.archive.open('downloads/some_archive.zip', 'r', openSuccess, openError);
   ```

2. To extract files:

   - To extract all files from the archive, use the `extractAll()` method of the `ArchiveFile` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveFile), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveFile), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveFile) applications).

     ```
     function progressCallback(opId, val, name) {
         console.log('extracting operation (: ' + opId + ') is in progress (' + (val * 100).toFixed(1) + '%)');
     }

     function openSuccess(archive) {
         archive.extractAll('music', null, null, progressCallback);
     }
     ```

   - To extract only a selected file from the archive, use the `extract()` method of the `ArchiveFileEntry` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveFileEntry), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveFileEntry), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveFileEntry) applications).

     First, get the `archiveFileEntry` object using the `getEntryByName()` or `getEntries()` method of the `ArchiveFile` interface.

     ```
     function extractSuccessCallback() {
         console.log('File extracted');
     }
     function getEntrySuccess(entry) {
         entry.extract('downloads/extract', extractSuccessCallback);
     }

     function openSuccess(archive) {
         archive.getEntryByName('my_file.txt', getEntrySuccess);
     }
     ```

## Aborting File Operations

You can abort an on-going file archive operation for the `open()`, `add()`, `extractAll()`, `getEntries()`, `getEntryByName()`, and `extract()` methods.

To abort the file archive operation, use the operation ID and the `abort()` method of the `ArchiveManager` interface (in [mobile](../../api/latest/device_api/mobile/tizen/archive.html#ArchiveManager), [wearable](../../api/latest/device_api/wearable/tizen/archive.html#ArchiveManager), and [TV](../../api/latest/device_api/tv/tizen/archive.html#ArchiveManager) applications):

```
function openSuccess(archive) {
    operationId = archive.extractAll('downloads/extracted');
    tizen.archive.abort(operationId);
}

tizen.archive.open('downloads/some_archive.zip', 'r', openSuccess);
```

## Related Information
* Dependencies
  - Tizen 2.4 and Higher for Mobile
  - Tizen 2.3.1 and Higher for Wearable
  - Tizen 3.0 and Higher for TV
